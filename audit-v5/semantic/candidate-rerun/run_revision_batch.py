#!/usr/bin/env python3
"""Cross-platform revision batch controller (Windows-safe; no fcntl).

Freezes a new revision batch from revision-pilot-001/inventory.jsonl without
touching revision-pilot-001, captures source leads, and runs one isolated
read-only Codex adjudication per revision. Model JSON ACCEPTED is only a vote;
delivery as REVISED_SUPPORTED still requires the separate primary source review.

  python run_revision_batch.py build   --batch revision-aero-001 --industry "Aerospace & Defense"
  python run_revision_batch.py capture --batch revision-aero-001
  python run_revision_batch.py run     --batch revision-aero-001 --parallel 3 [--only <revision_id> ...]
  python run_revision_batch.py status  --batch revision-aero-001
"""
from __future__ import annotations

import argparse
import hashlib
import io
import json
import os
import re
import shutil
import subprocess
import sys
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path

BASE = Path(__file__).resolve().parents[3]
HERE = BASE / 'audit-v5/semantic/candidate-rerun'
CACHE_ROOT = BASE / 'audit-v5/source-cache/candidate-rerun'
INVENTORY = HERE / 'revision-pilot-001/inventory.jsonl'
PILOT_QUEUE = HERE / 'revision-pilot-001/queue.jsonl'
PILOT_SCHEMA = CACHE_ROOT / 'adjudication/claims/9da61548d684833d6e4b/attempt-1/claim-output-schema.json'
PILOT_PROMPT = CACHE_ROOT / 'adjudication/claims/9da61548d684833d6e4b/attempt-1/prompt-1.txt'
PROMPT_SPLIT = 'One isolated original claim and source discovery leads:\n'
ASSESSMENT_DATE = '2026-10-08'
MODEL = 'gpt-6-sol'
EFFORT = 'high'
BUDGET_SECONDS = 1200
CONTROLLER_SHA256 = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


QUOTA_PATTERN = re.compile(r"out of credits|usage limit|rate[ _-]?limit(ed)?|quota (exceeded|exhausted)|429", re.I)


def quota_hit(events: str, stderr: str) -> bool:
    """Only error channels count; tool output and prompt text (e.g. 'quotation') must not."""
    lines = [l for l in stderr.splitlines() if 'ERROR' in l or 'error' in l.lower()[:200]]
    lines += [l for l in events.splitlines() if '"type":"error"' in l or '"type":"turn.failed"' in l]
    return any(QUOTA_PATTERN.search(l) for l in lines)


def now():
    return datetime.now(timezone.utc).isoformat()


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def rel(path: Path) -> str:
    return path.resolve().relative_to(BASE).as_posix()


def write_json(path: Path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + '.tmp')
    tmp.write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding='utf-8')
    os.replace(tmp, path)


def read_jsonl(path: Path):
    return [json.loads(l) for l in path.read_text(encoding='utf-8').splitlines() if l.strip()]


def paths(batch):
    return HERE / batch, CACHE_ROOT / batch


class VisibleText(HTMLParser):
    def __init__(self):
        super().__init__(); self.parts = []; self.skip = 0

    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style', 'noscript'):
            self.skip += 1
        if tag in ('p', 'br', 'div', 'li', 'tr', 'h1', 'h2', 'h3', 'h4', 'td', 'th'):
            self.parts.append('\n')

    def handle_endtag(self, tag):
        if tag in ('script', 'style', 'noscript') and self.skip:
            self.skip -= 1

    def handle_data(self, data):
        if not self.skip and data.strip():
            self.parts.append(data.strip() + ' ')


def capture(url: str, cache: Path) -> dict:
    """Content-addressed raw + extracted text snapshot; metadata keyed by URL hash."""
    src = cache / 'sources'; src.mkdir(parents=True, exist_ok=True)
    meta = src / (digest(url.encode()) + '.json')
    if meta.exists():
        result = json.loads(meta.read_text(encoding='utf-8'))
        if result.get('status') == 'captured':
            return result
    result = {'url': url, 'captured_at': now(), 'capture_method': 'urllib_http_get'}
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (compatible; TW-Coverage evidence audit)'})
        with urllib.request.urlopen(req, timeout=45) as resp:
            raw = resp.read(64 * 1024 * 1024 + 1)
            if len(raw) > 64 * 1024 * 1024:
                raise ValueError('Source exceeds 64 MiB capture ceiling')
            result.update({'resolved_url': resp.geturl(), 'http_status': resp.status,
                           'content_type': resp.headers.get('Content-Type')})
            charset = resp.headers.get_content_charset() or 'utf-8'
        if raw.startswith(b'%PDF'):
            from pypdf import PdfReader
            pdf = PdfReader(io.BytesIO(raw))
            text = '\n'.join(f'\n[PDF PAGE {i+1}]\n' + (p.extract_text() or '') for i, p in enumerate(pdf.pages))
            kind = 'pdf'
        else:
            decoded = raw.decode(charset, errors='replace')
            if '<html' in decoded.lower() or '<!doctype' in decoded.lower():
                parser = VisibleText(); parser.feed(decoded); text = ''.join(parser.parts); kind = 'html'
            else:
                text = decoded; kind = 'text'
        raw_path = src / (digest(raw) + '.bin')
        text_bytes = text.encode('utf-8')
        text_path = src / (digest(text_bytes) + '.txt')
        raw_path.write_bytes(raw); text_path.write_bytes(text_bytes)
        result.update({'status': 'captured', 'kind': kind, 'raw_path': rel(raw_path), 'raw_sha256': digest(raw),
                       'text_path': rel(text_path), 'text_sha256': digest(text_bytes), 'text_characters': len(text)})
    except Exception as exc:  # recorded, never converted into a factual verdict
        result.update({'status': 'capture_failed', 'error': f'{type(exc).__name__}: {str(exc)[:250]}'})
    write_json(meta, result)
    return result


def cmd_build(args):
    root, cache = paths(args.batch)
    queue_path = root / 'queue.jsonl'
    if queue_path.exists():
        sys.exit(f'{queue_path} already frozen; refusing to rebuild')
    pilot_parents = {r['parent_claim_id'] for r in read_jsonl(PILOT_QUEUE)}
    done_elsewhere = set(pilot_parents)
    for other in HERE.glob('revision-*/queue.jsonl'):
        if other.parent.name != args.batch:
            done_elsewhere |= {r['parent_claim_id'] for r in read_jsonl(other)}
    rows = []
    for item in read_jsonl(INVENTORY):
        parent = item['parent_claim']
        ticker = parent['issuer_ticker']
        cur = list((BASE / 'Pilot_Reports').glob(f'*/{ticker}_*.md'))
        if len(cur) != 1:
            raise SystemExit(f'ticker {ticker}: {len(cur)} reports')
        cur = cur[0]
        industries = [s.strip() for s in args.industry.split('|')]
        if item['parent_claim_id'] in done_elsewhere or ('ALL' not in industries and cur.parent.name not in industries):
            continue
        ctx = item['report_context']
        ph = item['preferred_proposal_sha256']
        cid = item['parent_claim_id']
        report_bytes = cur.read_bytes()
        rows.append({
            'claim_id': 'revision:' + digest(cid.encode())[:20] + ':' + ph[:16],
            'normalized_claim_hash': ph,
            'issuer_ticker': ticker, 'issuer_company': parent['issuer_company'],
            'original_text': item['preferred_proposal'],
            'report_path': rel(cur), 'cohort': args.batch,
            'parent_claim_id': cid, 'parent_claim': parent,
            'parent_effective_verdict': item['parent_effective_verdict'],
            'source_leads': item['source_leads'],
            'proposed_target_section': '業務與歷史資料',
            'qualifier_changes': item['qualifier_changes'],
            'proposal_binding': {'input_path': rel(INVENTORY), 'input_sha256': digest(INVENTORY.read_bytes()),
                                 'record_sha256': item['preferred_proposal_record_sha256'],
                                 'proposed_text_sha256': ph, 'preferred_stage': item['preferred_stage']},
            'parent_report_context': ctx,
            'current_report_sha256': digest(report_bytes),
            'report_changed_since_inventory': digest(report_bytes) != ctx.get('report_sha256'),
            'assessment_date': ASSESSMENT_DATE,
            'industry_folder': cur.parent.name,
        })
    order = {name: i for i, name in enumerate(industries)}
    rows.sort(key=lambda r: (order.get(r['industry_folder'], len(order)), r['issuer_ticker'], r['parent_claim_id']))
    if args.limit:
        rows = rows[:args.limit]
    if len({r['claim_id'] for r in rows}) != len(rows):
        raise SystemExit('duplicate revision ids')
    root.mkdir(parents=True, exist_ok=True)
    data = b''.join(json.dumps(r, ensure_ascii=False, sort_keys=True).encode() + b'\n' for r in rows)
    queue_path.write_bytes(data)
    tmpl = PILOT_PROMPT.read_text(encoding='utf-8')
    template = tmpl[:tmpl.index(PROMPT_SPLIT) + len(PROMPT_SPLIT)]
    (root / 'prompt-template.txt').write_text(template, encoding='utf-8')
    shutil.copyfile(PILOT_SCHEMA, root / 'claim-output-schema.template.json')
    write_json(root / 'queue.manifest.json', {
        'schema': 'revision-batch-queue-1', 'batch': args.batch, 'selection': {'industry_folder': args.industry, 'limit': args.limit,
        'rule': 'inventory parents not in any prior revision queue, ordered by the given industry priority (| separated, ALL = any), then ticker; first N'},
        'created_at': now(), 'assessment_date': ASSESSMENT_DATE, 'count': len(rows),
        'queue_sha256': digest(data),
        'inputs': {rel(INVENTORY): digest(INVENTORY.read_bytes()), rel(PILOT_QUEUE): digest(PILOT_QUEUE.read_bytes())},
        'prompt_template': {'derived_from': rel(PILOT_PROMPT), 'sha256': digest(template.encode())},
        'schema_template': {'derived_from': rel(PILOT_SCHEMA), 'sha256': digest(PILOT_SCHEMA.read_bytes())},
        'model': MODEL, 'effort': EFFORT, 'controller_sha256': CONTROLLER_SHA256,
        'original_acceptance_authority': False})
    print(f'froze {len(rows)} revisions -> {rel(queue_path)}')


ORIG_PROMPT = CACHE_ROOT / 'adjudication/claims/00a55ba1dfc2d675f476/attempt-2/prompt-2.txt'


def cmd_build_orig(args):
    """Re-research UNKNOWN parent claims that never received a rewrite proposal.

    The original sentence is adjudicated under the stage-2 original-claim contract; the model's
    revised_claim (if any) becomes a proposal that needs its own later revision review.
    Prior verdicts are withheld; prior search notes' URLs are passed only as discovery leads.
    """
    import ast
    root, cache = paths(args.batch)
    queue_path = root / 'queue.jsonl'
    if queue_path.exists():
        sys.exit(f'{queue_path} already frozen; refusing to rebuild')
    inv = {r['parent_claim_id'] for r in read_jsonl(INVENTORY)}
    rows = []
    for rec in read_jsonl(HERE / 'delivery/consolidated-status.jsonl'):
        if rec['claim_id'] in inv or rec['verdict'] != 'UNKNOWN':
            continue
        claim = rec['claim'] if isinstance(rec['claim'], dict) else ast.literal_eval(rec['claim'])
        ticker = claim['issuer_ticker']
        cur = list((BASE / 'Pilot_Reports').glob(f'*/{ticker}_*.md'))
        if len(cur) != 1:
            raise SystemExit(f'ticker {ticker}: {len(cur)} reports')
        cur = cur[0]
        leads, seen = [], set()
        manifest = BASE / rec['evidence_manifest'] if rec.get('evidence_manifest') else None
        if manifest and manifest.exists():
            for s in json.loads(manifest.read_text(encoding='utf-8')).get('sources', []):
                if s.get('url') and s['url'] not in seen:
                    seen.add(s['url']); leads.append({'url': s['url'], 'title': s.get('title'), 'locator': s.get('locator')})
        text = cur.read_text(encoding='utf-8')
        occ = []
        for i, line in enumerate(text.splitlines(), 1):
            if claim['original_text'][:30] in line:
                occ.append({'line': i, 'containing_line': line})
        h = claim['normalized_claim_hash']
        rows.append({'claim_id': 'orig-recheck:' + digest(rec['claim_id'].encode())[:20] + ':' + h[:16],
                     'normalized_claim_hash': h, 'issuer_ticker': ticker, 'issuer_company': claim['issuer_company'],
                     'original_text': claim['original_text'], 'report_path': rel(cur), 'cohort': args.batch,
                     'parent_claim_id': rec['claim_id'], 'parent_claim': claim, 'parent_effective_verdict': 'UNKNOWN',
                     'source_leads': leads, 'proposed_target_section': None, 'qualifier_changes': [],
                     'parent_report_context': {'report_sha256': digest(cur.read_bytes()), 'occurrences': occ},
                     'current_report_sha256': digest(cur.read_bytes()), 'assessment_date': ASSESSMENT_DATE,
                     'industry_folder': cur.parent.name, 'mode': 'original_recheck'})
    rows.sort(key=lambda r: (r['issuer_ticker'], r['parent_claim_id']))
    root.mkdir(parents=True, exist_ok=True)
    data = b''.join(json.dumps(r, ensure_ascii=False, sort_keys=True).encode() + b'\n' for r in rows)
    queue_path.write_bytes(data)
    tmpl = ORIG_PROMPT.read_text(encoding='utf-8')
    (root / 'prompt-template.txt').write_text(tmpl[:tmpl.index(PROMPT_SPLIT) + len(PROMPT_SPLIT)], encoding='utf-8')
    shutil.copyfile(PILOT_SCHEMA, root / 'claim-output-schema.template.json')
    write_json(root / 'queue.manifest.json', {
        'schema': 'revision-batch-queue-1', 'batch': args.batch, 'mode': 'original_recheck',
        'selection': {'rule': 'consolidated UNKNOWN parents without any rewrite proposal'},
        'created_at': now(), 'assessment_date': ASSESSMENT_DATE, 'count': len(rows), 'queue_sha256': digest(data),
        'prompt_template': {'derived_from': rel(ORIG_PROMPT), 'sha256': digest((root / 'prompt-template.txt').read_bytes())},
        'model': MODEL, 'effort': EFFORT, 'controller_sha256': CONTROLLER_SHA256, 'prior_verdicts_withheld': True})
    print(f'froze {len(rows)} original re-checks -> {rel(queue_path)}')


def cmd_build_alt(args):
    """Freeze a re-review batch from narrower alternatives proposed in a finished batch.

    Each alternative is a new text with a new revision ID. Prior verdicts and rationales
    are withheld; URLs cited by the prior execution are passed only as discovery leads.
    """
    root, cache = paths(args.batch)
    queue_path = root / 'queue.jsonl'
    if queue_path.exists():
        sys.exit(f'{queue_path} already frozen; refusing to rebuild')
    src_root = HERE / args.source_batch
    src_queue = {r['claim_id']: r for r in read_jsonl(src_root / 'queue.jsonl')}
    outcomes = read_jsonl(src_root / 'delivery/outcomes.jsonl')
    results = {}
    for r in read_jsonl(src_root / 'adjudication/results.jsonl'):
        results[r['claim_id']] = r
    rows = []
    for oc in outcomes:
        alt = oc.get('alternative_text')
        if not alt or oc['verdict'] == 'REVISED_SUPPORTED':
            continue
        prev = src_queue[oc['claim_id']]
        ah = digest(alt.encode('utf-8'))
        cited = []
        for at in results[oc['claim_id']]['output']['atomic_claims']:
            for ev in at['evidence']:
                cited.append({'url': ev['url'], 'title': ev['title'], 'locator': ev['locator']})
        leads, seen = [], set()
        for lead in prev['source_leads'] + cited:
            if lead['url'] not in seen:
                seen.add(lead['url']); leads.append({k: lead[k] for k in ('url', 'title', 'locator') if k in lead})
        cur = BASE / prev['report_path']
        rows.append({
            'claim_id': 'revision:' + digest(prev['parent_claim_id'].encode())[:20] + ':' + ah[:16],
            'normalized_claim_hash': ah,
            'issuer_ticker': prev['issuer_ticker'], 'issuer_company': prev['issuer_company'],
            'original_text': alt, 'report_path': prev['report_path'], 'cohort': args.batch,
            'parent_claim_id': prev['parent_claim_id'], 'parent_claim': prev['parent_claim'],
            'parent_effective_verdict': prev['parent_effective_verdict'],
            'supersedes_revision_id': oc['claim_id'],
            'source_leads': leads,
            'proposed_target_section': prev['proposed_target_section'],
            'qualifier_changes': prev['qualifier_changes'],
            'proposal_binding': {'input_path': rel(src_root / 'delivery/outcomes.jsonl'),
                                 'input_sha256': digest((src_root / 'delivery/outcomes.jsonl').read_bytes()),
                                 'proposed_text_sha256': ah, 'proposed_by': 'alternative from ' + args.source_batch},
            'parent_report_context': prev['parent_report_context'],
            'current_report_sha256': digest(cur.read_bytes()),
            'assessment_date': ASSESSMENT_DATE,
        })
    rows.sort(key=lambda r: (r['issuer_ticker'], r['claim_id']))
    if len({r['claim_id'] for r in rows}) != len(rows):
        raise SystemExit('duplicate revision ids')
    root.mkdir(parents=True, exist_ok=True)
    data = b''.join(json.dumps(r, ensure_ascii=False, sort_keys=True).encode() + b'\n' for r in rows)
    queue_path.write_bytes(data)
    # alternatives are new revision texts: always use the revision contract, even when the
    # source batch was an original re-check
    tmpl = PILOT_PROMPT.read_text(encoding='utf-8')
    (root / 'prompt-template.txt').write_text(tmpl[:tmpl.index(PROMPT_SPLIT) + len(PROMPT_SPLIT)], encoding='utf-8')
    shutil.copyfile(PILOT_SCHEMA, root / 'claim-output-schema.template.json')
    for row in rows:
        if not row['proposed_target_section']:
            row['proposed_target_section'] = '業務與歷史資料'
    data = b''.join(json.dumps(r, ensure_ascii=False, sort_keys=True).encode() + b'\n' for r in rows)
    queue_path.write_bytes(data)
    write_json(root / 'queue.manifest.json', {
        'schema': 'revision-batch-queue-1', 'batch': args.batch,
        'selection': {'rule': f'narrower alternatives proposed in {args.source_batch} for non-passed revisions'},
        'created_at': now(), 'assessment_date': ASSESSMENT_DATE, 'count': len(rows), 'queue_sha256': digest(data),
        'inputs': {rel(src_root / 'delivery/outcomes.jsonl'): digest((src_root / 'delivery/outcomes.jsonl').read_bytes()),
                   rel(src_root / 'queue.jsonl'): digest((src_root / 'queue.jsonl').read_bytes())},
        'prompt_template_sha256': digest((root / 'prompt-template.txt').read_bytes()),
        'model': MODEL, 'effort': EFFORT, 'controller_sha256': CONTROLLER_SHA256,
        'prior_verdicts_withheld': True, 'original_acceptance_authority': False})
    print(f'froze {len(rows)} alternatives -> {rel(queue_path)}')


def cmd_capture(args):
    root, cache = paths(args.batch)
    urls = sorted({l['url'] for r in read_jsonl(root / 'queue.jsonl') for l in r['source_leads'] if l.get('url')})
    ok = 0
    with ThreadPoolExecutor(6) as ex:
        for res in ex.map(lambda u: capture(u, cache), urls):
            ok += res['status'] == 'captured'
            if res['status'] != 'captured':
                print('FAILED', res['url'][:100], res.get('error'))
    print(f'captured {ok}/{len(urls)}')


def schema_for(row, template):
    s = json.loads(template)
    s['properties']['claim_id']['enum'] = [row['claim_id']]
    s['properties']['normalized_claim_hash']['enum'] = [row['normalized_claim_hash']]
    return s


def claim_dir(cache, row):
    return cache / 'claims' / digest(row['claim_id'].encode())[:20]


def run_one(row, root, cache):
    cdir = claim_dir(cache, row)
    attempt = 1
    while (cdir / f'attempt-{attempt}').exists():
        attempt += 1
    adir = cdir / f'attempt-{attempt}'; adir.mkdir(parents=True)
    leads = []
    for lead in row['source_leads']:
        meta = cache / 'sources' / (digest(lead['url'].encode()) + '.json')
        cap = json.loads(meta.read_text(encoding='utf-8')) if meta.exists() else {'status': 'not_captured'}
        if cap.get('status') == 'captured':
            cap = {**cap, 'text_path': str((BASE / cap['text_path']).resolve()), 'raw_path': str((BASE / cap['raw_path']).resolve())}
        leads.append({**lead, 'capture': cap})
    pctx = row['parent_report_context']
    context = {
        'requested_report_path': row['report_path'], 'resolved_report_path': row['report_path'],
        'report_sha256': row['current_report_sha256'],
        'occurrences': [{'line': None, 'headings': [{'level': 1, 'text': f"{row['issuer_ticker']} {row['issuer_company']}"},
                         {'level': 2, 'text': row['proposed_target_section']}],
                         'containing_line': row['original_text'], 'placement': 'proposed draft, not currently in parent report'}],
        'parent_occurrences': pctx.get('occurrences', []),
        'purpose': 'Evaluate the proposed text in its planned neutral section. Parent text is lineage only, not evidence and not the text to approve.'}
    if row.get('mode') == 'original_recheck':
        context = {'requested_report_path': row['report_path'], 'resolved_report_path': row['report_path'],
                   'report_sha256': row['current_report_sha256'], 'occurrences': pctx.get('occurrences', []),
                   'purpose': 'Original statement context only; not factual evidence.'}
    write_json(adir / 'original-report-context.json', context)
    payload = {'claim_id': row['claim_id'], 'normalized_claim_hash': row['normalized_claim_hash'],
               'issuer_ticker': row['issuer_ticker'], 'issuer_company': row['issuer_company'],
               'original_text': row['original_text'], 'original_report_context': context, 'source_leads': leads}
    prompt = (root / 'prompt-template.txt').read_text(encoding='utf-8') + json.dumps(payload, ensure_ascii=False)
    (adir / 'prompt.txt').write_text(prompt, encoding='utf-8')
    schema = schema_for(row, (root / 'claim-output-schema.template.json').read_text(encoding='utf-8'))
    write_json(adir / 'claim-output-schema.json', schema)
    final = adir / 'final.json'
    codex = shutil.which('codex') or shutil.which('codex.cmd')
    cmd = [codex, '--search', 'exec', '--ignore-user-config', '--ignore-rules', '--model', MODEL,
           '-c', f'model_reasoning_effort="{EFFORT}"', '-c', 'approval_policy="never"', '-c', 'windows.sandbox="unelevated"',
           '--sandbox', 'read-only', '--skip-git-repo-check', '--color', 'never', '--json',
           '--cd', str(adir), '--output-schema', str(adir / 'claim-output-schema.json'),
           '--output-last-message', str(final), '-']
    started = time.time(); errors = []; code = None
    with open(adir / 'public-events.jsonl', 'wb') as out, open(adir / 'stderr.txt', 'wb') as err:
        try:
            proc = subprocess.run(cmd, input=prompt.encode('utf-8'), stdout=out, stderr=err, timeout=BUDGET_SECONDS)
            code = proc.returncode
        except subprocess.TimeoutExpired:
            errors.append(f'timeout after {BUDGET_SECONDS}s')
    events = (adir / 'public-events.jsonl').read_text(encoding='utf-8', errors='replace')
    stderr = (adir / 'stderr.txt').read_text(encoding='utf-8', errors='replace')
    thread = re.search(r'"thread_id"\s*:\s*"([^"]+)"', events)
    models = sorted(set(re.findall(r'"model"\s*:\s*"([^"]+)"', events + stderr)))
    if quota_hit(events, stderr):
        errors.append('quota_or_rate_limit')
    output = None
    if final.exists() and final.read_text(encoding='utf-8').strip():
        try:
            output = json.loads(final.read_text(encoding='utf-8'))
        except json.JSONDecodeError as exc:
            errors.append(f'final not JSON: {exc}')
    else:
        errors.append('no final output')
    execution = {'requested_model': MODEL, 'requested_effort': EFFORT,
                 'runtime_selection': {'thread_id': thread.group(1) if thread else None, 'models_seen_in_public_events': models,
                                       'private_reasoning_inspected': False},
                 'controller_sha256': CONTROLLER_SHA256, 'controller_path': rel(Path(__file__)),
                 'command': [Path(c).name if i == 0 else c for i, c in enumerate(cmd)],
                 'process_exit_code': code, 'attempt': attempt, 'started_at': datetime.fromtimestamp(started, timezone.utc).isoformat(),
                 'completed_at': now(), 'elapsed_seconds': round(time.time() - started), 'run_budget_seconds': BUDGET_SECONDS,
                 'prompt_path': rel(adir / 'prompt.txt'), 'prompt_sha256': digest(prompt.encode('utf-8')),
                 'output_path': rel(final), 'output_sha256': digest(final.read_bytes()) if final.exists() else None,
                 'errors': errors}
    write_json(adir / 'execution.json', execution)
    return row['claim_id'], output, execution


def latest(root):
    path = root / 'adjudication/results.jsonl'
    res = {}
    if path.exists():
        for r in read_jsonl(path):
            res[r['claim_id']] = r
    return res


def cmd_run(args):
    root, cache = paths(args.batch)
    queue = read_jsonl(root / 'queue.jsonl')
    done = {k for k, v in latest(root).items() if v.get('output') is not None}
    todo = [r for r in queue if r['claim_id'] not in done and (not args.only or r['claim_id'] in args.only)]
    if args.limit:
        todo = todo[:args.limit]
    print(f'{len(todo)} to run, parallel {args.parallel}', flush=True)
    results = root / 'adjudication/results.jsonl'; results.parent.mkdir(parents=True, exist_ok=True)
    failures = root / 'adjudication/operational-failures.jsonl'
    stop = False
    with ThreadPoolExecutor(args.parallel) as ex:
        futs = {ex.submit(run_one, r, root, cache): r for r in todo}
        for fut in as_completed(futs):
            row = futs[fut]
            try:
                cid, output, execution = fut.result()
            except Exception as exc:
                cid, output, execution = row['claim_id'], None, {'errors': [f'{type(exc).__name__}: {exc}']}
            rec = {'claim_id': cid, 'parent_claim_id': row['parent_claim_id'], 'ticker': row['issuer_ticker'],
                   'company': row['issuer_company'], 'recorded_at': now(), 'output': output, 'execution': execution}
            with open(results if output is not None else failures, 'a', encoding='utf-8') as f:
                f.write(json.dumps(rec, ensure_ascii=False) + '\n')
            print(row['issuer_ticker'], cid, (output or {}).get('verdict'), execution.get('errors'), flush=True)
            if 'quota_or_rate_limit' in execution.get('errors', []):
                stop = True
                for f2 in futs:
                    f2.cancel()
    if stop:
        print('STOPPED: quota or rate limit reported by Codex', flush=True)


def cmd_status(args):
    root, _ = paths(args.batch)
    queue = read_jsonl(root / 'queue.jsonl')
    res = latest(root)
    for r in queue:
        o = (res.get(r['claim_id']) or {}).get('output') or {}
        print(r['issuer_ticker'], r['issuer_company'], o.get('verdict', 'PENDING'), '|', r['original_text'][:70])


def main():
    p = argparse.ArgumentParser()
    p.add_argument('command', choices=['build', 'build-alt', 'build-orig', 'capture', 'run', 'status'])
    p.add_argument('--batch', required=True)
    p.add_argument('--industry')
    p.add_argument('--source-batch')
    p.add_argument('--parallel', type=int, default=3)
    p.add_argument('--limit', type=int)
    p.add_argument('--only', nargs='*')
    a = p.parse_args()
    {'build': cmd_build, 'build-alt': cmd_build_alt, 'build-orig': cmd_build_orig, 'capture': cmd_capture, 'run': cmd_run, 'status': cmd_status}[a.command](a)


if __name__ == '__main__':
    main()
