#!/usr/bin/env python3
"""Primary-source review worksheet for a batch: every model-ACCEPTED result with its atoms,
cited excerpts and the surrounding captured text (or NOT FOUND / NO CAPTURE flags).
Run check_batch_excerpts.py first. Reviewed claim ids (already in primary-source-review.jsonl)
are skipped.

  python review_worksheet.py --batch revision-batch-003 [--out worksheet.md]
"""
from __future__ import annotations

import argparse
import json
import re
import unicodedata
from pathlib import Path

from run_revision_batch import BASE, HERE, read_jsonl


def norm(s):
    return re.sub(r'\s+', '', unicodedata.normalize('NFKC', s or ''))


def main():
    p = argparse.ArgumentParser(); p.add_argument('--batch', required=True); p.add_argument('--out'); a = p.parse_args()
    root = HERE / a.batch
    latest = {}
    for r in read_jsonl(root / 'adjudication/results.jsonl'):
        latest[r['claim_id']] = r
    queue = {r['claim_id']: r for r in read_jsonl(root / 'queue.jsonl')}
    done = set()
    psr = root / 'adjudication/primary-source-review.jsonl'
    if psr.exists():
        done = {r['claim_id'] for r in read_jsonl(psr)}
    gate = json.loads((root / 'capture-gate.json').read_text(encoding='utf-8'))['rows']
    cache = {}
    out = []
    n = 0
    for cid, r in latest.items():
        o = r['output']
        if o['verdict'] != 'ACCEPTED' or cid in done:
            continue
        n += 1
        q = queue[cid]
        out.append(f'## [{n}] {q["issuer_ticker"]} {q["issuer_company"]} — {cid}')
        out.append(f'TEXT: {q["original_text"]}')
        out.append(f'WHY: {o["rationale"]}')
        out.append(f'PERIOD: {o["period_assessment"]}')
        for row in [g for g in gate if g['key'] == cid]:
            out.append(f'- [{row["gate"]}] {row["atom_status"]}: {row["text"]}')
            for e in row['evidence']:
                ctx = 'NO CAPTURE ' + str(e.get('capture_error'))
                if e.get('text_path'):
                    if e['text_path'] not in cache:
                        cache[e['text_path']] = norm((BASE / e['text_path']).read_text(encoding='utf-8', errors='replace'))
                    t = cache[e['text_path']]
                    i = t.find(norm(e['excerpt']))
                    ctx = t[max(0, i - 80):i + len(norm(e['excerpt'])) + 80] if i >= 0 else 'NOT FOUND: ' + (e['excerpt'] or '')
                out.append(f'    * {e["url"][:90]} | {e["locator"]} | {e["inspection_method"]}')
                out.append(f'      {ctx}')
        out.append('')
    text = '\n'.join(out)
    if a.out:
        Path(a.out).write_text(text, encoding='utf-8')
        print(f'{n} accepted results to review -> {a.out}')
    else:
        print(text)


if __name__ == '__main__':
    main()
