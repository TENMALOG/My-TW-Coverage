#!/usr/bin/env python3
"""Mechanical capture gate for a revision batch: every cited URL is captured (or
reuses an existing capture) and each support_excerpt must appear verbatim
(whitespace-normalised) in the captured text. Writes a worksheet for the human /
Claude primary source review; it never sets REVISED_SUPPORTED by itself.

  python check_batch_excerpts.py --batch revision-aero-001
  python check_batch_excerpts.py --batch company-research-aero-001 --company
"""
from __future__ import annotations

import argparse
import json
import re
import unicodedata
from pathlib import Path

from run_revision_batch import BASE, CACHE_ROOT, HERE, capture, read_jsonl, write_json, now


def norm(s: str) -> str:
    s = unicodedata.normalize('NFKC', s)
    return re.sub(r'\s+', '', s)


def check_evidence(ev, cache, text_cache):
    url = ev['url']
    if url not in text_cache:
        cap = capture(url, cache)
        text = ''
        if cap.get('status') == 'captured':
            text = (BASE / cap['text_path']).read_text(encoding='utf-8', errors='replace')
        text_cache[url] = (cap, text)
    cap, text = text_cache[url]
    ex = norm(ev.get('support_excerpt', ''))
    found = bool(ex) and ex in norm(text)
    return {'url': url, 'inspection_method': ev.get('inspection_method'), 'locator': ev.get('locator'),
            'capture_status': cap.get('status'), 'capture_error': cap.get('error'),
            'text_path': cap.get('text_path'), 'text_sha256': cap.get('text_sha256'),
            'excerpt': ev.get('support_excerpt'), 'excerpt_found': found}


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--batch', required=True)
    p.add_argument('--company', action='store_true')
    a = p.parse_args()
    root, cache = HERE / a.batch, CACHE_ROOT / a.batch
    text_cache = {}
    rows = []
    if a.company:
        for final in sorted((cache / 'companies').glob('*/attempt-*/final.json')):
            out = json.loads(final.read_text(encoding='utf-8'))
            items = [('statement', s['key'], s['verdict'], at['status'], at['text'], at['evidence'])
                     for s in out['statements'] for at in s['atomic_claims']]
            items += [('fact', f"{out['ticker']}-F{i+1:02d}", None, 'SUPPORTED', f['text'], f['evidence'])
                      for i, f in enumerate(out['additional_facts'])]
            for kind, key, verdict, status, text, evs in items:
                rows.append({'kind': kind, 'key': key, 'verdict': verdict, 'atom_status': status, 'text': text,
                             'output': str(final.relative_to(BASE).as_posix()),
                             'evidence': [check_evidence(e, cache, text_cache) for e in evs]})
    else:
        latest = {}
        for r in read_jsonl(root / 'adjudication/results.jsonl'):
            latest[r['claim_id']] = r
        for cid, r in latest.items():
            o = r['output']
            for at in o['atomic_claims']:
                rows.append({'kind': 'revision', 'key': cid, 'ticker': r['ticker'], 'verdict': o['verdict'],
                             'atom_status': at['status'], 'text': at['text'],
                             'output_sha256': r['execution'].get('output_sha256'),
                             'evidence': [check_evidence(e, cache, text_cache) for e in at['evidence']]})
    for row in rows:
        sup = row['atom_status'] == 'SUPPORTED'
        row['gate'] = ('PASS' if any(e['excerpt_found'] for e in row['evidence']) else 'NEEDS_MANUAL') if sup else 'N/A'
    write_json(root / 'capture-gate.json', {'generated_at': now(), 'rows': rows})
    n = sum(r['gate'] == 'NEEDS_MANUAL' for r in rows)
    print(f'{len(rows)} atoms/facts; {sum(r["gate"] == "PASS" for r in rows)} PASS; {n} NEEDS_MANUAL')
    for r in rows:
        if r['gate'] == 'NEEDS_MANUAL':
            print(' -', r['key'][:40], r['text'][:60], [(e['capture_status'], e['url'][:60]) for e in r['evidence']])


if __name__ == '__main__':
    main()
