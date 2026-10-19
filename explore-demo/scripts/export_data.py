"""Export the verified research data the explore-layer demo renders (no new facts are created here).

  py explore-demo/scripts/export_data.py

Writes explore-demo/src/data/:
  companies.json   one record per company: name, legal name, industry (corrected) + 證交所產業別, Shorts script
                   (hook/what/mix/regions/cards, all validated against annual-report facts), FY2024/2025 revenue
                   and gross margin, listed counterparties, and a `sources` map fact id -> {page, period, url}
  industries.json  slug, name, company count, tickers
Every number shown by the demo comes from these records, and every card carries the fact ids it rests on.
"""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SITE = ROOT / 'research-site'
OUT = ROOT / 'explore-demo/src/data'


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    names = {r['industry_folder']: r for r in csv.DictReader(open(SITE / 'data/industry-names.csv', encoding='utf-8-sig'))}
    cat = list(csv.DictReader(open(SITE / 'catalog/release-scope-companies.csv', encoding='utf-8-sig')))
    basic = {json.loads(l)['ticker']: json.loads(l) for l in open(SITE / 'data/basic-data.jsonl', encoding='utf-8')}
    fixes = {r['ticker']: r for r in csv.DictReader(open(SITE / 'data/industry-corrections.csv', encoding='utf-8-sig'))}
    comps, inds = [], {}
    for r in cat:
        tk = r['ticker']
        sb_p = ROOT / 'research-site/ops/shorts/storyboard' / f'{tk}.json'
        base_p = ROOT / 'research-site/ops/shorts/base' / f'{tk}.json'
        if not sb_p.exists() or not base_p.exists():
            continue
        sb = json.loads(sb_p.read_text(encoding='utf-8'))
        base = json.loads(base_p.read_text(encoding='utf-8'))
        doc = json.loads((SITE / 'data/company-facts' / f'{tk}.json').read_text(encoding='utf-8'))
        pages = {f['id']: f for f in doc['facts']}
        cited = set()
        for k in ('hook', 'what', 'mix', 'regions'):
            if sb.get(k):
                cited.update(sb[k].get('facts') or [])
        for c in sb.get('cards') or []:
            cited.update(c.get('facts') or [])
        src = base['source']
        sources = {i: {'page': pages[i].get('page'), 'period': pages[i].get('period'), 'statement': pages[i]['statement']}
                   for i in cited if i in pages}
        ind = names[r['industry_folder']]
        fx = fixes.get(tk)
        comps.append({
            'ticker': tk, 'name': r['company'], 'legal_name': base.get('legal_name') or '',
            'industry': {'slug': ind['slug'], 'name': ind['name_zh'].rstrip('?？')},
            'mops_industry': (basic.get(tk) or {}).get('industry_mops') or '',
            'corrected_from': names[fx['original_folder']]['name_zh'].rstrip('?？') if fx else None,
            'report': {'fy': src.get('fy'), 'filename': src.get('filename'), 'url': src.get('url')},
            'hook': sb.get('hook'), 'what': sb.get('what'), 'mix': sb.get('mix'), 'regions': sb.get('regions'),
            'cards': sb.get('cards') or [], 'tags': sb.get('tags') or [],
            'fin': sb.get('fin') or {}, 'relations': sb.get('relations') or [], 'sources': sources,
            # every verified fact (PASS, not rejected) for the 「年報重點全文」 section and the search index
            'facts': [{'id': f['id'], 'field': f['field'], 'statement': f['statement'], 'page': pages[f['id']].get('page')}
                      for f in base['facts'] if f['id'] in pages],
        })
        i = inds.setdefault(ind['slug'], {'slug': ind['slug'], 'name': ind['name_zh'].rstrip('?？'), 'tickers': []})
        i['tickers'].append(tk)
    (OUT / 'companies.json').write_text(json.dumps(comps, ensure_ascii=False), encoding='utf-8')
    (OUT / 'industries.json').write_text(json.dumps(sorted(inds.values(), key=lambda x: -len(x['tickers'])),
                                                   ensure_ascii=False), encoding='utf-8')
    print('companies', len(comps), 'industries', len(inds))


if __name__ == '__main__':
    main()
