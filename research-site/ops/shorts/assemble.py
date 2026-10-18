"""Assemble the deterministic part of each company Short, and the fact list the script writer may use.

  python research-site/ops/shorts/assemble.py [tickers...]     (default: all companies)

Writes research-site/ops/shorts/base/{ticker}.json:
  ticker, name (catalog short name), legal_name, industry (zh), source (annual-report filename/url),
  fin: {year: {revenue_k, gross_margin_pct}} from the MOPS summary,
  relations: listed counterparties (published edges) as [{name, ticker, side: supplier|customer, share}],
  renames: verified name history,
  facts: PASS and not-rejected facts [{id, field, period, statement, attribution}] for the script writer.
"""
import csv
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]          # research-site
OUT = Path(__file__).resolve().parent / 'base'
FACTS = ROOT / 'data/company-facts'


def rejected():
    last = {}
    for line in (FACTS / '_semantic-review.jsonl').read_text(encoding='utf-8').splitlines():
        if line.strip():
            r = json.loads(line)
            last[r['id']] = r['verdict']
    return {k for k, v in last.items() if v == 'REJECT'}


def main(tickers):
    OUT.mkdir(exist_ok=True)
    rej = rejected()
    cat = {r['ticker']: r['company'] for r in csv.DictReader(open(ROOT / 'catalog/release-scope-companies.csv', encoding='utf-8-sig'))}
    fin = {r['ticker']: r for r in json.loads((ROOT / 'data/financials/fy2025-financials-all.json').read_text(encoding='utf-8'))}
    renames = json.loads((ROOT / 'data/company-renames.json').read_text(encoding='utf-8'))
    edges = list(csv.DictReader(open(ROOT / 'data/relations/listed_edges.csv', encoding='utf-8-sig')))
    published = None  # listed_edges.csv is already the reviewed, publishable edge list
    todo = tickers or sorted(cat)
    n = 0
    for tk in todo:
        p = FACTS / f'{tk}.json'
        if not p.exists():
            continue
        doc = json.loads(p.read_text(encoding='utf-8'))
        page = ROOT / 'chapters/companies' / f'{tk}.qmd'
        m = re.search(r'產業分類\*\*：([^（\n]+)', page.read_text(encoding='utf-8')) if page.exists() else None
        f = {}
        for y, v in (fin.get(tk, {}).get('years') or {}).items():
            rev = (v.get('items_k') or {}).get('營業收入')
            if rev:
                f[y] = {'revenue_k': rev, 'gross_margin_pct': v.get('gross_margin_pct')}
        rel, seen = [], set()
        for r in edges:
            if published is not None and r['relation_id'] not in published:
                continue
            # the share is always a share of the REPORTING company's sales (counterparty = customer)
            # or purchases (counterparty = supplier); the basis label names that company
            if r['ticker'] == tk:          # this company's own report names the counterparty
                other, otk, side = r['counterparty_company'], r['counterparty_ticker'], r['role']
                reporter = cat.get(tk, doc['company'])
            elif r['counterparty_ticker'] == tk:   # the other company's report names this company
                other, otk = r['company'], r['ticker']
                side = {'customer': 'supplier', 'supplier': 'customer'}.get(r['role'], r['role'])
                reporter = other
            else:
                continue
            kind = '銷貨' if r['role'] == 'customer' else '進貨'
            me = cat.get(tk, doc['company'])
            basis = f'{me}占{reporter}{kind}' if reporter == other else f'占{me}{kind}'
            if side not in ('customer', 'supplier') or (otk, side) in seen:
                continue
            seen.add((otk, side))
            share = r['share_text'] if re.search(r'\d', r['share_text'] or '') else ''
            rel.append({'name': other, 'ticker': otk, 'side': side, 'share': share,
                        'label': f'{basis} {share}' if share else '', 'period': r['period']})
        facts = [{'id': x['id'], 'field': x['field'], 'period': x['period'], 'statement': x['statement'],
                  'attribution': x.get('attribution', '')}
                 for x in doc['facts'] if (x.get('verification') or {}).get('status') == 'PASS' and x['id'] not in rej]
        base = {'ticker': tk, 'name': cat.get(tk, doc['company']), 'legal_name': doc.get('legal_name', ''),
                'industry': m.group(1).strip() if m else '', 'source': {'filename': doc['source'].get('filename'),
                'url': doc['source'].get('citation_url'), 'fy': doc['source'].get('fy')},
                'fin': f, 'relations': rel[:8], 'renames': renames.get(tk, []), 'facts': facts}
        (OUT / f'{tk}.json').write_text(json.dumps(base, ensure_ascii=False, indent=1), encoding='utf-8')
        n += 1
    print('companies', n)


if __name__ == '__main__':
    main(sys.argv[1:])
