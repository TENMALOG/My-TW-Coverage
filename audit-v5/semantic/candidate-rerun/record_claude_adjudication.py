#!/usr/bin/env python3
"""Record an adjudication performed by Claude (takeover when Codex quota is exhausted).

Claude results are stored with their own runtime label; they never reuse a Codex/Sol
thread id or output hash. The output must satisfy the same per-claim schema.

  python record_claude_adjudication.py --batch revision-aero-001 --claim-id <id> --output <final.json>
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from run_revision_batch import (BASE, CACHE_ROOT, HERE, claim_dir, digest, now, read_jsonl, rel, schema_for,
                                write_json)

CLAUDE_MODEL = 'claude-opus-5-5'


def validate(value, schema, path='$'):
    t = schema.get('type')
    types = t if isinstance(t, list) else [t]
    pymap = {'object': dict, 'array': list, 'string': str, 'boolean': bool, 'null': type(None)}
    if t and not any(isinstance(value, pymap[x]) for x in types):
        raise ValueError(f'{path}: expected {t}')
    if 'enum' in schema and value not in schema['enum']:
        raise ValueError(f'{path}: {value!r} not in enum')
    if isinstance(value, dict):
        for k in schema.get('required', []):
            if k not in value:
                raise ValueError(f'{path}: missing {k}')
        if schema.get('additionalProperties') is False:
            extra = set(value) - set(schema.get('properties', {}))
            if extra:
                raise ValueError(f'{path}: unexpected {sorted(extra)}')
        for k, v in value.items():
            if k in schema.get('properties', {}):
                validate(v, schema['properties'][k], f'{path}.{k}')
    if isinstance(value, list) and 'items' in schema:
        for i, v in enumerate(value):
            validate(v, schema['items'], f'{path}[{i}]')


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--batch', required=True)
    p.add_argument('--claim-id', required=True)
    p.add_argument('--output', required=True)
    a = p.parse_args()
    root, cache = HERE / a.batch, CACHE_ROOT / a.batch
    row = next(r for r in read_jsonl(root / 'queue.jsonl') if r['claim_id'] == a.claim_id)
    output = json.loads(Path(a.output).read_text(encoding='utf-8'))
    output['claim_id'] = row['claim_id']
    output['normalized_claim_hash'] = row['normalized_claim_hash']
    validate(output, schema_for(row, (root / 'claim-output-schema.template.json').read_text(encoding='utf-8')))
    # every captured_content excerpt must be re-locatable in this batch's snapshot of that URL
    import re
    import unicodedata
    from run_revision_batch import capture
    norm = lambda s: re.sub(r'\s+', '', unicodedata.normalize('NFKC', s or ''))
    for at in output['atomic_claims']:
        for ev in at['evidence']:
            if ev['inspection_method'] != 'captured_content' or at['status'] != 'SUPPORTED':
                continue
            cap = capture(ev['url'], cache)
            if cap.get('status') != 'captured':
                raise SystemExit(f'not captured: {ev["url"]}')
            if norm(ev['support_excerpt']) not in norm((BASE / cap['text_path']).read_text(encoding='utf-8', errors='replace')):
                raise SystemExit(f'excerpt not found in snapshot: {ev["support_excerpt"]}')
    cdir = claim_dir(cache, row)
    adir = cdir / 'claude-1'
    n = 1
    while adir.exists():
        n += 1; adir = cdir / f'claude-{n}'
    adir.mkdir(parents=True)
    final = adir / 'final.json'
    final.write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding='utf-8')
    execution = {'runtime': 'claude_takeover', 'model': CLAUDE_MODEL,
                 'reason': 'Codex quota exhausted or Codex run failed; Claude performed independent research in its own session.',
                 'research_tools': ['WebSearch', 'WebFetch', 'local captured sources'],
                 'independence_note': 'Owner decision 2026-10-11: Claude counts as an independent third-party reviewer. '
                                      'Claude adjudicated without using prior verdicts for this revision; Claude also '
                                      'orchestrated the batch (recorded for transparency).',
                 'completed_at': now(), 'output_path': rel(final), 'output_sha256': digest(final.read_bytes()),
                 'errors': []}
    write_json(adir / 'execution.json', execution)
    rec = {'claim_id': row['claim_id'], 'parent_claim_id': row['parent_claim_id'], 'ticker': row['issuer_ticker'],
           'company': row['issuer_company'], 'recorded_at': now(), 'output': output, 'execution': execution}
    with open(root / 'adjudication/results.jsonl', 'a', encoding='utf-8') as f:
        f.write(json.dumps(rec, ensure_ascii=False) + '\n')
    print('recorded', row['claim_id'], output['verdict'])


if __name__ == '__main__':
    main()
