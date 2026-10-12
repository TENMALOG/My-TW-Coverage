"""FY2024/FY2025 consolidated income-statement figures for every catalog company.

Source: MOPS 綜合損益表彙總報表 (ajax_t163sb04, 第四季＝全年度), the same snapshots used by
build_aero_financials.py. The report is split into tables by industry format (一般業、銀行業、
證券業、保險業、金控業、異業); each company keeps the line items of its own table, recorded
verbatim (仟元). Margins are computed only where 營業收入 exists.

  python research-site/scripts/build_financials_all.py [--refresh]

Writes research-site/data/financials/fy2025-financials-all.json and a coverage CSV.
"""
from __future__ import annotations

import argparse
import csv
import json

from build_aero_financials import ROOT, Tables, fetch, num

OUT = ROOT / 'research-site/data/financials'
GROSS = ('營業毛利（毛損）淨額', '營業毛利（毛損）')


def table_kind(head):
    """Name the table format from its distinctive columns."""
    h = set(head)
    if '利息淨收益' in h:
        return '銀行業'
    if '營業毛利（毛損）' in h or '營業毛利（毛損）淨額' in h:
        return '一般業'
    if '承保費收入' in h or '保險負債準備淨變動' in h:
        return '保險業'
    if '經紀手續費收入' in h:
        return '證券業'
    if '利息以外淨損益' in h:
        return '金控業'
    if '收入' in h and '支出' in h:
        return '收入支出格式（證券、保險或異業）'
    return '其他格式'


def parse_all(meta):
    html = (ROOT / meta['raw_path']).read_bytes().decode('utf-8', errors='replace')
    p = Tables(); p.feed(html)
    rows = {}
    for table in p.tables:
        if not table or '公司代號' not in table[0]:
            continue
        head = table[0]
        kind = table_kind(head)
        for r in table[1:]:
            if len(r) == len(head):
                rows[r[0]] = {'kind': kind, 'row': dict(zip(head, r))}
    return rows


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--refresh', action='store_true'); a = ap.parse_args()
    catalog = list(csv.DictReader(open(ROOT / 'research-site/catalog/release-scope-companies.csv', encoding='utf-8-sig')))
    data, sources = {}, {}
    for year in (113, 114):
        for typek in ('sii', 'otc'):
            meta = fetch(typek, year, a.refresh)
            for tk, rec in parse_all(meta).items():
                data.setdefault(tk, {})[year] = rec
                sources.setdefault(tk, {})[year] = meta
    out, coverage = [], []
    for c in catalog:
        tk = c['ticker']
        years = data.get(tk, {})
        coverage.append({'ticker': tk, 'company': c['company'], 'industry_folder': c['industry_folder'],
                         'has_2024': 113 in years, 'has_2025': 114 in years,
                         'kind': (years.get(114) or years.get(113) or {}).get('kind', '')})
        if not years:
            continue
        rec = {'ticker': tk, 'company': c['company'], 'industry_folder': c['industry_folder'],
               'basis': '合併綜合損益表彙總（公開資訊觀測站 t163sb04，第四季＝全年度）', 'years': {}}
        for year, label in ((113, '2024'), (114, '2025')):
            if year not in years:
                continue
            row, kind = years[year]['row'], years[year]['kind']
            items = {k: num(v) for k, v in row.items() if k not in ('公司代號', '公司名稱')}
            y = {'mops_company_name': row.get('公司名稱'), 'table_kind': kind, 'items_k': items}
            rev = items.get('營業收入')
            gp = next((items[g] for g in GROSS if items.get(g) is not None), None)
            oi = items.get('營業利益（損失）')
            if rev:
                y['gross_margin_pct'] = round(gp / rev * 100, 2) if gp is not None else None
                y['operating_margin_pct'] = round(oi / rev * 100, 2) if oi is not None else None
            m = sources[tk][year]
            y['source'] = {'url': m['url'], 'post': m['post'], 'raw_sha256': m['raw_sha256'], 'captured_at': m['captured_at']}
            rec['years'][label] = y
        rec['formula'] = 'margin = item / 營業收入 × 100，四捨五入至小數第二位'
        out.append(rec)
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / 'fy2025-financials-all.json').write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding='utf-8')
    with open(OUT / 'financials-coverage.csv', 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(coverage[0])); w.writeheader(); w.writerows(coverage)
    both = sum(r['has_2024'] and r['has_2025'] for r in coverage)
    kinds = {}
    for r in coverage:
        kinds[r['kind'] or '缺漏'] = kinds.get(r['kind'] or '缺漏', 0) + 1
    print(f'companies {len(coverage)}, with both years {both}, any year {len(out)}; table kinds {kinds}')


if __name__ == '__main__':
    main()
