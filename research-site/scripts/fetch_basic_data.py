"""Snapshot MOPS 公司基本資料 (ajax_t05st03) for every catalog company and extract key fields.

  python research-site/scripts/fetch_basic_data.py [--tickers 2330 ...] [--delay 8]

Raw HTML goes to audit-v5/source-cache/research-site/mops-basic/ (SHA256-named, with metadata);
parsed fields go to research-site/data/basic-data.jsonl (one line per company, latest snapshot).
Only company-level fields are kept; contact persons, phone numbers and e-mail addresses are not
copied into the dataset. On 查詢過量 the run pauses (doubling, up to 30 minutes) and retries.
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
CACHE = ROOT / 'audit-v5/source-cache/research-site/mops-basic'
OUT = ROOT / 'research-site/data/basic-data.jsonl'
URL = 'https://mopsov.twse.com.tw/mops/web/ajax_t05st03'
KEEP = {'股票代號': 'ticker_mops', '產業類別': 'industry_mops', '外國企業註冊地國': 'foreign_domicile',
        '公司名稱': 'legal_name', '地址': 'address', '董事長': 'chairman', '總經理': 'president',
        '主要經營業務': 'business_registered', '公司成立日期': 'established_roc', '實收資本額': 'paid_in_capital',
        '上市日期': 'twse_listed_roc', '上櫃日期': 'tpex_listed_roc', '興櫃日期': 'emerging_roc',
        '公開發行日期': 'public_offering_roc', '英文簡稱': 'name_en_short', '英文全名': 'name_en',
        '簽證會計師事務所': 'auditor_firm'}


class Cells(HTMLParser):
    def __init__(self):
        super().__init__(); self.cells = []; self.cur = None

    def handle_starttag(self, tag, attrs):
        if tag in ('td', 'th'):
            self.cur = []

    def handle_endtag(self, tag):
        if tag in ('td', 'th') and self.cur is not None:
            self.cells.append(re.sub(r'\s+', ' ', ''.join(self.cur)).replace('\xa0', ' ').strip()); self.cur = None

    def handle_data(self, data):
        if self.cur is not None:
            self.cur.append(data)


class RateLimited(Exception):
    pass


def sha(b):
    return hashlib.sha256(b).hexdigest()


def fetch(ticker):
    data = {'encodeURIComponent': '1', 'step': '1', 'firstin': '1', 'off': '1', 'queryName': 'co_id',
            'inpuType': 'co_id', 'TYPEK': 'all', 'co_id': ticker}
    req = urllib.request.Request(URL, data=urllib.parse.urlencode(data).encode(), headers={'User-Agent': 'Mozilla/5.0'})
    raw = urllib.request.urlopen(req, timeout=60).read()
    if '查詢過量'.encode() in raw:
        raise RateLimited(ticker)
    CACHE.mkdir(parents=True, exist_ok=True)
    (CACHE / f'{sha(raw)}.html').write_bytes(raw)
    meta = {'ticker': ticker, 'url': URL, 'post': data, 'captured_at': datetime.now(timezone.utc).isoformat(),
            'raw_path': (CACHE / f'{sha(raw)}.html').relative_to(ROOT).as_posix(), 'raw_sha256': sha(raw)}
    (CACHE / f'{ticker}.json').write_text(json.dumps(meta, ensure_ascii=False, indent=1), encoding='utf-8')
    return meta


def parse(meta):
    p = Cells(); p.feed((ROOT / meta['raw_path']).read_bytes().decode('utf-8', errors='replace'))
    rec = {'ticker': meta['ticker']}
    cells = p.cells
    for i, c in enumerate(cells[:-1]):
        key = KEEP.get(c)
        if key and key not in rec:
            rec[key] = cells[i + 1]
    rec['source'] = {k: meta[k] for k in ('url', 'post', 'captured_at', 'raw_sha256')}
    html = (ROOT / meta['raw_path']).read_bytes().decode('utf-8', errors='replace')
    if rec.get('legal_name'):
        rec['status'] = 'parsed'
    elif '不繼續公開發行' in html:
        rec['status'] = 'ceased_public_offering'  # MOPS: 公開發行公司不繼續公開發行
    else:
        rec['status'] = 'no_company'
    return rec


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--tickers', nargs='*'); ap.add_argument('--delay', type=float, default=8.0)
    ap.add_argument('--refresh', action='store_true')
    a = ap.parse_args()
    tickers = a.tickers or [r['ticker'] for r in csv.DictReader(
        open(ROOT / 'research-site/catalog/release-scope-companies.csv', encoding='utf-8-sig'))]
    for tk in tickers:
        meta_path = CACHE / f'{tk}.json'
        if meta_path.exists() and not a.refresh:
            continue
        pause = 120
        while True:
            try:
                fetch(tk); break
            except RateLimited:
                print(f'{tk} rate limited, pausing {pause}s', flush=True); time.sleep(pause); pause = min(pause * 2, 1800)
            except Exception as exc:  # logged; the ticker is retried on the next run
                print(f'{tk} error {type(exc).__name__}: {exc}', flush=True); break
        print(tk, 'ok' if meta_path.exists() else 'missing', flush=True)
        time.sleep(a.delay)
    # rebuild the dataset from every snapshot on disk
    rows = [parse(json.loads(p.read_text(encoding='utf-8'))) for p in sorted(CACHE.glob('*.json'))]
    OUT.write_text(''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in rows), encoding='utf-8')
    print(f'basic data: {sum(r["status"] == "parsed" for r in rows)} parsed / {len(rows)} snapshots')


if __name__ == '__main__':
    main()
