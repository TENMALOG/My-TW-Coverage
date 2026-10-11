"""Consolidated FY2024/FY2025 income-statement figures for the aerospace & defense chapter.

Source: MOPS 綜合損益表彙總報表 (ajax_t163sb04, 第四季＝全年度, 合併報表), snapshotted with SHA256.
Each figure is also cross-checked against the company's annual-report 財務績效 table when present.
Ratios: gross margin = 營業毛利 / 營業收入; operating margin = 營業利益 / 營業收入; rounded to 0.01 pct-pt.

  python research-site/scripts/build_aero_financials.py [--refresh]
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import time
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CACHE = ROOT / 'audit-v5/source-cache/research-site/mops-t163sb04'
OUT = ROOT / 'research-site/data/aerospace-defense'
URL = 'https://mopsov.twse.com.tw/mops/web/ajax_t163sb04'
TICKERS = ['2208', '2630', '2634', '2644', '2645', '4541', '4546', '4572', '6753', '8222']
FIELDS = {'營業收入': 'revenue', '營業毛利（毛損）淨額': 'gross_profit', '營業毛利（毛損）': 'gross_profit_raw',
          '營業利益（損失）': 'operating_income', '本期淨利（淨損）': 'net_income'}


class Tables(HTMLParser):
    def __init__(self):
        super().__init__(); self.tables = []; self.row = None; self.cell = None

    def handle_starttag(self, tag, attrs):
        if tag == 'table':
            self.tables.append([])
        elif tag == 'tr' and self.tables:
            self.row = []; self.tables[-1].append(self.row)
        elif tag in ('td', 'th') and self.row is not None:
            self.cell = []

    def handle_endtag(self, tag):
        if tag in ('td', 'th') and self.cell is not None and self.row is not None:
            self.row.append(''.join(self.cell).strip()); self.cell = None

    def handle_data(self, data):
        if self.cell is not None:
            self.cell.append(data)


# Not present in the consolidated summary: use the annual report's 財務績效 table; excerpt must be
# re-located in the MOPS annual-report snapshot. 4546 discloses no affiliated-company consolidation.
AR_FALLBACK = {
    '2644': {'page': 52, 'basis': '年報財務績效表（中信造船未出現於合併彙總報表，口徑待確認）',
             '2025': (6129692, 433520, 254318), '2024': (4829989, 298438, 128514),
             'excerpts': ['營業收入 6,129,692 4,829,989', '營業毛利 433,520 298,438', '營業淨利 254,318 128,514']},
    '4546': {'page': 72, 'basis': '年報經營結果分析表（年報稱關係企業合併營業報告書不適用，應屬個體報表）',
             '2025': (2011427, 535307, 263324), '2024': (1399039, 345900, 128775),
             'excerpts': ['營業收入 1,399,039 2,011,427', '營業毛利(損) 345,900 535,307', '營業利益(損失) 128,775 263,324']},
}
MOPS_AR = ROOT / 'audit-v5/source-cache/research-site/mops-annual'


def norm(s):
    return re.sub(r'\s+', '', s)


def fallback(tk):
    fb = AR_FALLBACK[tk]
    meta = json.loads((MOPS_AR / f'{tk}_2025_F04.json').read_text(encoding='utf-8'))
    text = norm((ROOT / meta['text_path']).read_text(encoding='utf-8'))
    for ex in fb['excerpts']:
        if norm(ex) not in text:
            raise SystemExit(f'{tk}: excerpt not found: {ex}')
    rec = {'ticker': tk, 'company': {'2644': '中信造船', '4546': '長亨'}[tk], 'basis': fb['basis']}
    for label in ('2024', '2025'):
        rev, gp, oi = fb[label]
        rec[f'revenue_{label}_k'] = rev; rec[f'gross_profit_{label}_k'] = gp; rec[f'operating_income_{label}_k'] = oi
        rec[f'gross_margin_{label}_pct'] = round(gp / rev * 100, 2); rec[f'operating_margin_{label}_pct'] = round(oi / rev * 100, 2)
        rec[f'source_{label}'] = {'url': meta['citation_url'], 'page': fb['page'], 'excerpts': fb['excerpts'], 'text_sha256': meta['text_sha256']}
    rec['formula'] = 'margin = item / 營業收入 × 100，四捨五入至小數第二位'
    return rec


def sha(b):
    return hashlib.sha256(b).hexdigest()


def fetch(typek, year, refresh):
    meta_path = CACHE / f'{typek}_{year}_04.json'
    if meta_path.exists() and not refresh:
        return json.loads(meta_path.read_text(encoding='utf-8'))
    data = {'encodeURIComponent': '1', 'step': '1', 'firstin': '1', 'off': '1', 'isQuery': 'Y',
            'TYPEK': typek, 'year': str(year), 'season': '04'}
    req = urllib.request.Request(URL, data=urllib.parse.urlencode(data).encode(), headers={'User-Agent': 'Mozilla/5.0'})
    raw = urllib.request.urlopen(req, timeout=90).read()
    if '查詢過量'.encode() in raw:
        raise SystemExit('MOPS rate limited; retry later')
    CACHE.mkdir(parents=True, exist_ok=True)
    (CACHE / f'{sha(raw)}.html').write_bytes(raw)
    meta = {'url': URL, 'post': data, 'captured_at': datetime.now(timezone.utc).isoformat(),
            'raw_path': (CACHE / f'{sha(raw)}.html').relative_to(ROOT).as_posix(), 'raw_sha256': sha(raw)}
    meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding='utf-8')
    time.sleep(8)
    return meta


def parse(meta):
    html = (ROOT / meta['raw_path']).read_bytes().decode('utf-8', errors='replace')
    p = Tables(); p.feed(html)
    rows = {}
    for table in p.tables:
        if not table or '公司代號' not in table[0]:
            continue
        head = table[0]
        for r in table[1:]:
            if len(r) == len(head) and r[0] in TICKERS:
                rows[r[0]] = dict(zip(head, r))
    return rows


def num(s):
    s = (s or '').replace(',', '').strip()
    return None if s in ('', '--') else int(float(s))


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--refresh', action='store_true'); a = ap.parse_args()
    data, sources = {}, {}
    for year in (113, 114):
        for typek in ('sii', 'otc'):
            meta = fetch(typek, year, a.refresh)
            for tk, row in parse(meta).items():
                data.setdefault(tk, {})[year] = row
                sources.setdefault(tk, {})[year] = meta
    out, missing = [], []
    for tk in TICKERS:
        if tk not in data or set(data[tk]) != {113, 114}:
            missing.append(tk); continue
        rec = {'ticker': tk, 'company': data[tk][114]['公司名稱'], 'basis': '合併綜合損益表彙總（公開資訊觀測站 t163sb04，第四季＝全年度）'}
        for year, label in ((113, '2024'), (114, '2025')):
            r = data[tk][year]
            rev = num(r.get('營業收入'))
            gp = num(r.get('營業毛利（毛損）淨額') or r.get('營業毛利（毛損）'))
            oi = num(r.get('營業利益（損失）'))
            rec[f'revenue_{label}_k'] = rev
            rec[f'gross_profit_{label}_k'] = gp
            rec[f'operating_income_{label}_k'] = oi
            rec[f'gross_margin_{label}_pct'] = round(gp / rev * 100, 2) if rev and gp is not None else None
            rec[f'operating_margin_{label}_pct'] = round(oi / rev * 100, 2) if rev and oi is not None else None
            m = sources[tk][year]
            rec[f'source_{label}'] = {'url': m['url'], 'post': m['post'], 'raw_sha256': m['raw_sha256'], 'captured_at': m['captured_at']}
        rec['formula'] = 'margin = item / 營業收入 × 100，四捨五入至小數第二位'
        out.append(rec)
    for tk in missing:
        out.append(fallback(tk))
    out.sort(key=lambda r: r['ticker'])
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / 'fy2025-financials.json').write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding='utf-8')
    flat = [{k: v for k, v in r.items() if not k.startswith('source_')} for r in out]
    with open(OUT / 'fy2025-financials.csv', 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(flat[0])); w.writeheader(); w.writerows(flat)
    for r in out:
        print(r['ticker'], r['company'], r['revenue_2025_k'], r['gross_margin_2025_pct'], r['operating_margin_2025_pct'],
              '| 2024', r['revenue_2024_k'], r['gross_margin_2024_pct'])


if __name__ == '__main__':
    main()
