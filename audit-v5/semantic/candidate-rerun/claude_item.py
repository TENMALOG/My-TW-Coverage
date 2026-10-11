#!/usr/bin/env python3
"""Claude takeover helper: show one pending queue item and search its captured sources.

  python claude_item.py --batch revision-batch-003 --idx 0                 # show item (pending list order)
  python claude_item.py --batch revision-batch-003 --idx 0 --grep 台光電 第一  # search captured texts (±90 chars)
  python claude_item.py --batch revision-batch-003 --idx 0 --skeleton out.json # write output JSON skeleton
Prior verdicts for this item are not shown (only the frozen queue row and its source leads).
"""
from __future__ import annotations

import argparse
import json
import re
import unicodedata

from run_revision_batch import BASE, CACHE_ROOT, HERE, digest, read_jsonl


def norm(s):
    return re.sub(r'\s+', '', unicodedata.normalize('NFKC', s))


def pending(batch):
    root = HERE / batch
    done = set()
    if (root / 'adjudication/results.jsonl').exists():
        done = {r['claim_id'] for r in read_jsonl(root / 'adjudication/results.jsonl') if r.get('output')}
    return [r for r in read_jsonl(root / 'queue.jsonl') if r['claim_id'] not in done]


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--batch', required=True); p.add_argument('--idx', type=int, required=True)
    p.add_argument('--grep', nargs='*'); p.add_argument('--skeleton')
    a = p.parse_args()
    row = pending(a.batch)[a.idx]
    caps = []
    for lead in row['source_leads']:
        meta = CACHE_ROOT / a.batch / 'sources' / (digest(lead['url'].encode()) + '.json')
        m = json.loads(meta.read_text(encoding='utf-8')) if meta.exists() else {'status': 'not_captured'}
        caps.append((lead, m))
    if a.skeleton:
        sk = {'claim_id': row['claim_id'], 'normalized_claim_hash': row['normalized_claim_hash'], 'verdict': '',
              'rationale': '', 'period_assessment': '', 'qualifier_coverage_complete': False,
              'complete_original_supported': False, 'all_sources_inspected': True, 'atomic_claims': [],
              'revised_claim': None, 'revised_claim_supported': False, 'unresolved_qualifiers': [], 'contradictions': [],
              'research_complete': True, 'research_stop_reason': ''}
        open(a.skeleton, 'w', encoding='utf-8').write(json.dumps(sk, ensure_ascii=False, indent=1))
        print('skeleton ->', a.skeleton); return
    if a.grep:
        for lead, m in caps:
            if m.get('status') != 'captured':
                continue
            t = (BASE / m['text_path']).read_text(encoding='utf-8', errors='replace')
            n = norm(t)
            for kw in a.grep:
                for hit in list(re.finditer(re.escape(norm(kw)), n))[:3]:
                    page = re.findall(r'\[PDFPAGE(\d+)\]', n[:hit.start()])
                    print(f'[{lead["url"][:70]}] p{page[-1] if page else "-"} «{kw}»: {n[max(0, hit.start() - 90):hit.end() + 90]}')
        return
    print('CLAIM_ID:', row['claim_id'])
    print('ISSUER:', row['issuer_ticker'], row['issuer_company'], '| report:', row['report_path'])
    print('TEXT:', row['original_text'])
    for lead, m in caps:
        print(f'- {m.get("status")} | {lead.get("title")} | {lead.get("locator")} | {lead["url"][:120]}'
              + (f' | {m.get("text_characters")} chars' if m.get('status') == 'captured' else f' | {m.get("error", "")[:60]}'))


if __name__ == '__main__':
    main()
