#!/usr/bin/env python3
"""Record primary-source review decisions and write delivery/outcomes.jsonl + summary.json.

Decisions file (JSON): {"<claim_id or unique suffix>": ["PASS"|"FAIL", "review basis in Traditional Chinese"], ...}
Only model-ACCEPTED results can become REVISED_SUPPORTED (revision batches) or
ORIGINAL_SUPPORTED (orig-recheck batches), and only with a PASS decision.

  python finalize_batch.py --batch revision-batch-003 --decisions decisions.json [--partial]
--partial allows finalizing while some ACCEPTED results are still unreviewed (they stay PENDING_REVIEW).
"""
from __future__ import annotations

import argparse
import collections
import json
from pathlib import Path

from run_revision_batch import HERE, digest, now, read_jsonl, write_json

REVIEWER = 'claude-opus-5-5 (independent reviewer per owner decision 2026-10-11)'


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--batch', required=True); p.add_argument('--decisions', required=True); p.add_argument('--partial', action='store_true')
    a = p.parse_args()
    root = HERE / a.batch
    queue = {r['claim_id']: r for r in read_jsonl(root / 'queue.jsonl')}
    latest = {}
    for r in read_jsonl(root / 'adjudication/results.jsonl'):
        latest[r['claim_id']] = r
    raw = json.loads(Path(a.decisions).read_text(encoding='utf-8'))
    psr_path = root / 'adjudication/primary-source-review.jsonl'
    existing = {r['claim_id']: r for r in read_jsonl(psr_path)} if psr_path.exists() else {}
    for key, (status, basis) in raw.items():
        match = [c for c in latest if c == key or c.endswith(key)]
        if len(match) != 1:
            raise SystemExit(f'decision key {key} matches {len(match)} results')
        cid = match[0]
        if latest[cid]['output']['verdict'] != 'ACCEPTED':
            raise SystemExit(f'{cid}: not a model-ACCEPTED result')
        existing[cid] = {'claim_id': cid, 'ticker': latest[cid]['ticker'], 'company': latest[cid]['company'],
                         'output_sha256': latest[cid]['execution'].get('output_sha256'), 'status': status, 'reviewer': REVIEWER,
                         'reviewed_at': now(), 'review_basis': basis, 'parent_original_acceptance_changed': False}
    psr_path.write_text(''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in existing.values()), encoding='utf-8')
    orig_mode = any(q.get('mode') == 'original_recheck' for q in queue.values())
    passed_label = 'ORIGINAL_SUPPORTED' if orig_mode else 'REVISED_SUPPORTED'
    outs, pending = [], []
    for cid, q in queue.items():
        r = latest.get(cid)
        if r is None:
            outs.append({'claim_id': cid, 'parent_claim_id': q['parent_claim_id'], 'ticker': q['issuer_ticker'],
                         'company': q['issuer_company'], 'verdict': 'NOT_RUN', 'proposed_text': q['original_text']})
            continue
        o = r['output']; rev = existing.get(cid)
        if o['verdict'] == 'ACCEPTED':
            verdict = passed_label if rev and rev['status'] == 'PASS' else ('PRIMARY_REVIEW_FAILED' if rev else 'PENDING_REVIEW')
            if verdict == 'PENDING_REVIEW':
                pending.append(cid)
        else:
            verdict = o['verdict']
        outs.append({'claim_id': cid, 'parent_claim_id': q['parent_claim_id'], 'ticker': q['issuer_ticker'], 'company': q['issuer_company'],
                     'industry_folder': q.get('industry_folder'), 'verdict': verdict, 'model_verdict': o['verdict'],
                     'proposed_text': q['original_text'], 'rationale': o['rationale'], 'alternative_text': o['revised_claim'],
                     'alternative_requires_new_review': bool(o['revised_claim']), 'output_sha256': r['execution'].get('output_sha256'),
                     'primary_source_review': rev['status'] if rev else None, 'parent_original_acceptance_changed': False})
    if pending and not a.partial:
        raise SystemExit(f'{len(pending)} ACCEPTED results still unreviewed; use --partial to write an interim delivery')
    d = root / 'delivery'; d.mkdir(exist_ok=True)
    (d / 'outcomes.jsonl').write_text(''.join(json.dumps(x, ensure_ascii=False) + '\n' for x in outs), encoding='utf-8')
    c = collections.Counter(x['verdict'] for x in outs)
    write_json(d / 'summary.json', {'schema': 'revision-batch-summary-1', 'batch': a.batch, 'generated_at': now(),
                                    'assessment_date': '2026-10-08', 'queue_count': len(queue), 'reviewed': sum(1 for x in outs if x['verdict'] != 'NOT_RUN'),
                                    'verdicts': dict(c), 'interim': bool(pending), 'mode': 'original_recheck' if orig_mode else 'revision',
                                    'outcomes_sha256': digest((d / 'outcomes.jsonl').read_bytes()),
                                    'parent_original_acceptance_changed': False})
    print(dict(c))


if __name__ == '__main__':
    main()
