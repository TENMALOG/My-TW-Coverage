"""Comparable FY2025 metrics for the aerospace & defense chapter, read from MOPS annual reports.

Every number carries an excerpt that must be re-located (whitespace-normalised) in the
snapshot text, plus the PDF page where it was found. Unit: NT$ thousand (仟元) as filed.
Top-customer share is the largest single customer in the annual report's ≥10% customer table
(a disclosure concentration measure, not market share). Names stay anonymous when filed so.
"""
from __future__ import annotations

import csv
import json
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MOPS = ROOT / 'audit-v5/source-cache/research-site/mops-annual'
OUT = ROOT / 'research-site/data/aerospace-defense'

# ticker, company, segment, revenue_k, rev_excerpt, top_customer, top_share_pct, named, cust_excerpt, notes
ROWS = [
    ('2208', '台船', '造船', 21780245, '合計 14,494,347 100.00% 2 1,780,245 100.00%',
     '國防部海軍造船發展中心', 54.77, True, '11,928,237 54.77', '艦艇建造占營收66.53%；台灣中油15.32%、海巡署10.57%亦逾10%'),
    ('2630', '亞航', '航空器維修', 5454110, '合計 5,454,110 100.00',
     'A客戶（匿名）', 52.28, False, 'A 客戶 2,851,630 52.28', '零附件維修類（自修）占42.62%'),
    ('2634', '漢翔', '軍民用航空製造與維修', 35452130, '合計 39,338,315 100.00 35,452,130 100.00',
     'A公司（匿名）', 48.92, False, 'A 公司 17,341,794 48.92', '飛機及航空器維修類50.45%、引擎類46.90%'),
    ('2644', '中信造船', '造船', 6129692, '合計 6,129,692 100 4,829,989 100',
     '甲客戶（匿名）', 49.28, False, '甲客戶 3,020,655 49.28', '船舶建造占93.69%；內銷99.01%'),
    ('2645', '長榮航太', '航空器維修與零組件', 18179185, '14,140,133 4,039,052 18,179,185',
     '長榮航空（母公司）', 33.30, True, '6,053,724 2,582,003 9,543,458 18,179,185 33.30', '航空器維修及其他占77.78%；外銷55.96%'),
    ('4541', '晟田', '航空零組件', 1644010, '合 計 1,416,505 100.00 1,644,010 100.00',
     '甲公司（匿名）', 37.36, False, '甲公司 614,211 37.36', '航太零組件合計占68.29%；半導體設備零組件25.36%'),
    ('4546', '長亨', '航空發動機零組件', 2011427, '合計 2,011,427 100',
     'C公司（匿名）', 48.86, False, 'C 公司 982,712 48.86', '外銷美國48.70%、法國16.37%'),
    ('4572', '駐龍', '航空機體結構零組件', 670865, '合計 670,865 100.00 871,452 100.00',
     'A公司（匿名）', 52.73, False, 'A公司 353,752 52.73', '飛機結構零組件占94.07%'),
    ('6753', '龍德造船', '造船', 5246333, '5,246,333 100.00%',
     'C客戶（匿名）', 80.03, False, 'C客戶 4,198,858 80.03', '船舶建造占88.56%；內銷86.59%'),
    ('8222', '寶一', '航空發動機零組件', 961015, '銷貨淨額 824,132 100 銷貨淨額 961,015 100',
     'c公司（匿名）', 37.0, False, 'c 公司 353,341 37', '年報稱產品以外銷為主'),
]


# FY2024 revenue (same table, prior-year column) with its own excerpt
PRIOR = {
    '2208': (14494347, '合計 14,494,347 100.00%'), '2630': (5200056, '較 113 年度 5,200,056'),
    '2634': (39338315, '合計 39,338,315 100.00'), '2644': (4829989, '4,829,989 100'),
    '2645': (16284500, '6,765,050 9,519,450 16,284,500'), '4541': (1416505, '合 計 1,416,505 100.00'),
    '4546': (1399039, '銷貨淨額 1,399,039 100.00'), '4572': (871452, '871,452 100.00'),
    '6753': (5119080, '5,119,080 100.00%'), '8222': (824132, '銷貨淨額 824,132 100'),
}


def norm(s):
    return re.sub(r'\s+', '', unicodedata.normalize('NFKC', s))


def locate(text, excerpt):
    n = norm(text)
    i = n.find(norm(excerpt))
    if i < 0:
        return None
    # map back to page: count page markers before the matched position in the normalised text
    pages = [m.start() for m in re.finditer(re.escape(norm('[PDF PAGE ')), n)]
    nums = re.findall(r'\[PDFPAGE(\d+)\]', n)
    page = None
    for pos, num in zip(pages, nums):
        if pos <= i:
            page = int(num)
    return page


def main():
    out, fail = [], []
    for tk, co, seg, rev, rev_ex, cust, share, named, cust_ex, notes in ROWS:
        meta = json.loads((MOPS / f'{tk}_2025_F04.json').read_text(encoding='utf-8'))
        text = (ROOT / meta['text_path']).read_text(encoding='utf-8')
        rp, cp = locate(text, rev_ex), locate(text, cust_ex)
        prev, prev_ex = PRIOR[tk]
        pp = locate(text, prev_ex)
        if rp is None or cp is None or pp is None:
            fail.append((tk, rp, cp, pp))
        out.append({'ticker': tk, 'company': co, 'segment': seg, 'fiscal_year': 2025, 'revenue_k_twd': rev,
                    'revenue_page': rp, 'revenue_2024_k_twd': prev, 'revenue_2024_page': pp,
                    'revenue_change_pct': round((rev - prev) / prev * 100, 1), 'top_customer': cust, 'top_customer_share_pct': share, 'top_customer_named': named,
                    'customer_table_page': cp, 'notes': notes, 'source_url': meta['citation_url'],
                    'source_filename': meta['filename'], 'text_sha256': meta['text_sha256'],
                    'basis': '合併或個體依各公司年報營業比重／主要銷貨客戶表；仟元；Claude 依年報原文核對'})
    if fail:
        print('NOT LOCATED', fail); sys.exit(1)
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / 'fy2025-metrics.json').write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding='utf-8')
    with open(OUT / 'fy2025-metrics.csv', 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(out[0])); w.writeheader(); w.writerows(out)
    for r in out:
        print(r['ticker'], r['company'], r['revenue_k_twd'], r['revenue_page'], r['top_customer_share_pct'], r['customer_table_page'])


if __name__ == '__main__':
    main()
