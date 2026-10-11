#!/usr/bin/env python3
"""Read unreviewed source evidence in bounded, per-claim batches."""
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent/'revision-pilot-001'


def read(path):
    return [json.loads(x) for x in path.read_text().splitlines() if x.strip()] if path.exists() else []


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--limit', type=int, default=2)
    ap.add_argument('--ticker')
    args = ap.parse_args()
    latest = {x['claim_id']: x for x in read(ROOT/'adjudication/results.jsonl')}
    primary = {x['claim_id']: x for x in read(ROOT/'adjudication/primary-source-review.jsonl')}
    pending = [r for cid, r in latest.items() if (args.ticker and r['original_claim']['issuer_ticker']==args.ticker)
        or (not args.ticker and (cid not in primary or primary[cid]['output_sha256']!=r['output_sha256']))]
    print('Pending primary reviews:', len(pending))
    for r in pending[:args.limit]:
        item = r['original_claim']
        print('\nCLAIM', r['claim_id'], item['issuer_ticker'], item['issuer_company'], r['verdict'])
        print('PROPOSED', item['original_text'])
        print('PARENT', item['parent_claim']['original_text'])
        print('CONTEXT', json.dumps(item['parent_report_context'], ensure_ascii=False))
        verdict = r['adjudication']
        print('ADJUDICATION', json.dumps({k: verdict[k] for k in ['verdict', 'rationale', 'period_assessment',
            'unresolved_qualifiers', 'contradictions', 'research_complete', 'revised_claim']}, ensure_ascii=False))
        print('ATOMS', json.dumps([{k: a[k] for k in ['text', 'status', 'period', 'reason']}
            for a in verdict['atomic_claims']], ensure_ascii=False))
        for c in r['source_captures']:
            print('SOURCE', c['url'], c['status'], 'RAW', c.get('raw_path'))
            if c['status']!='captured':
                continue
            text = re.sub(r'\s+', '', Path(c['text_path']).read_text())
            seen = set()
            for a in r['adjudication']['atomic_claims']:
                for e in a['evidence']:
                    if e['url']!=c['url'] or e['support_excerpt'] in seen:
                        continue
                    seen.add(e['support_excerpt'])
                    quote = re.sub(r'\s+', '', e['support_excerpt']); pos = text.find(quote)
                    print('LOCATOR', e['locator'], 'PUBLICATION', e['publication_date'], 'PERIOD', e['effective_period'], 'FOUND', pos,
                          'ACTUAL_CONTEXT', text[max(0, pos-160):pos+len(quote)+260] if pos>=0 else 'NOT FOUND')


if __name__=='__main__':
    main()
