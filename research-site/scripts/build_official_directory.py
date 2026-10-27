"""Official directory of listed (上市), OTC (上櫃) and emerging (興櫃) companies, snapshotted with SHA256.

  .venv/Scripts/python.exe -X utf8 research-site/scripts/build_official_directory.py [--refresh]

Sources (government open data, low frequency: five requests, 3 s apart):
  TWSE OpenAPI t187ap03_L (上市公司基本資料), TPEx OpenAPI mopsfin_t187ap03_O / _R (上櫃／興櫃公司基本資料),
  TWSE ISIN lists strMode=2 / 4 (上市／上櫃 股票＋創新板) for companies the basic data has not picked up yet.
Raw responses go to audit-v5/source-cache/research-site/official-directory/; the merged list goes to
research-site/data/official-directory.json. Depositary receipts (-DR) are kept but marked security_type TDR;
ISIN-only rows (listed after the basic data's 出表日, or scheduled to list) carry no legal name.
"""
import argparse
import hashlib
import html
import json
import re
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CACHE = ROOT / 'audit-v5/source-cache/research-site/official-directory'
OUT = ROOT / 'research-site/data/official-directory.json'
UA = {'User-Agent': 'Mozilla/5.0 (compatible; TW-Coverage research)', 'Accept': 'application/json'}
SOURCES = {
    'twse_L': ('https://openapi.twse.com.tw/v1/opendata/t187ap03_L', '上市'),
    'tpex_O': ('https://www.tpex.org.tw/openapi/v1/mopsfin_t187ap03_O', '上櫃'),
    'tpex_R': ('https://www.tpex.org.tw/openapi/v1/mopsfin_t187ap03_R', '興櫃'),
    'isin_2': ('https://isin.twse.com.tw/isin/C_public.jsp?strMode=2', '上市'),
    'isin_4': ('https://isin.twse.com.tw/isin/C_public.jsp?strMode=4', '上櫃'),
}


def sha(b):
    return hashlib.sha256(b).hexdigest()


def fetch(key, refresh):
    meta_path = CACHE / f'{key}.json'
    if meta_path.exists() and not refresh:
        return json.loads(meta_path.read_text(encoding='utf-8'))
    url = SOURCES[key][0]
    raw = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=120).read()
    CACHE.mkdir(parents=True, exist_ok=True)
    ext = 'html' if key.startswith('isin') else 'json'
    (CACHE / f'{sha(raw)}.{ext}').write_bytes(raw)
    meta = {'key': key, 'url': url, 'captured_at': datetime.now(timezone.utc).isoformat(),
            'raw_path': (CACHE / f'{sha(raw)}.{ext}').relative_to(ROOT).as_posix(), 'raw_sha256': sha(raw)}
    meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding='utf-8')
    time.sleep(3)
    return meta


def roc_date(s):
    """'1151023' or '20260723' -> '2026-10-23'; anything else -> None."""
    d = re.sub(r'\D', '', str(s or ''))
    if len(d) == 7:
        d = f'{int(d[:3]) + 1911}{d[3:]}'
    return f'{d[:4]}-{d[4:6]}-{d[6:]}' if len(d) == 8 else None


def basic_rows(meta, market):
    rows = json.loads((ROOT / meta['raw_path']).read_text(encoding='utf-8'))
    out = []
    for r in rows:
        code = str(r.get('公司代號') or r.get('SecuritiesCompanyCode') or '').strip()
        short = str(r.get('公司簡稱') or r.get('CompanyAbbreviation') or '').strip()
        if not code:
            continue
        out.append({'ticker': code, 'short_name': short,
                    'legal_name': str(r.get('公司名稱') or r.get('CompanyName') or '').strip() or None,
                    'market': market, 'industry_code': str(r.get('產業別') or r.get('SecuritiesIndustryCode') or '').strip() or None,
                    'listed_on': roc_date(r.get('上市日期') or r.get('DateOfListing')),
                    'security_type': 'TDR' if short.endswith('-DR') else 'stock',
                    'data_date': roc_date(r.get('出表日期') or r.get('Date')), 'source': meta['key']})
    return out


def isin_rows(meta, market):
    text = (ROOT / meta['raw_path']).read_bytes().decode('big5hkscs', errors='replace')
    section, out = None, []
    for row in re.findall(r'<tr>(.*?)</tr>', text, re.S):
        cells = [html.unescape(re.sub(r'<[^>]+>', '', c)).strip() for c in re.findall(r'<td[^>]*>(.*?)</td>', row, re.S)]
        if cells and len([c for c in cells if c]) == 1:
            section = cells[0]
            continue
        if section in ('股票', '創新板') and len(cells) >= 6:
            m = re.match(r'^(\S+)\s+(.+)$', cells[0].replace('　', ' ').strip())
            if m:
                out.append({'ticker': m.group(1), 'short_name': m.group(2).strip(), 'listed_on': roc_date(cells[2]),
                            'market': market, 'industry': cells[4] or None})
    return out


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--refresh', action='store_true'); a = ap.parse_args()
    metas = {k: fetch(k, a.refresh) for k in SOURCES}
    rows = {}
    for key in ('twse_L', 'tpex_O', 'tpex_R'):
        for r in basic_rows(metas[key], SOURCES[key][1]):
            if r['ticker'] in rows:
                raise SystemExit(f"{r['ticker']} appears in two basic-data lists")
            rows[r['ticker']] = r
    as_of = max(r['data_date'] for r in rows.values() if r['data_date'])
    added = []
    for key in ('isin_2', 'isin_4'):
        for r in isin_rows(metas[key], SOURCES[key][1]):
            if r['ticker'] in rows:
                continue
            status = 'scheduled' if r['listed_on'] and r['listed_on'] > as_of else 'listed_after_basic_data'
            rows[r['ticker']] = {'ticker': r['ticker'], 'short_name': r['short_name'], 'legal_name': None,
                                 'market': r['market'], 'industry_code': None, 'listed_on': r['listed_on'],
                                 'security_type': 'stock', 'data_date': None, 'source': key, 'isin_status': status}
            added.append((r['ticker'], r['short_name'], r['market'], r['listed_on'], status))
    doc = {'as_of': as_of, 'built_at': datetime.now(timezone.utc).isoformat(),
           'sources': {k: {'url': m['url'], 'captured_at': m['captured_at'], 'raw_sha256': m['raw_sha256']} for k, m in metas.items()},
           'companies': sorted(rows.values(), key=lambda r: r['ticker'])}
    OUT.write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding='utf-8')
    count = {}
    for r in rows.values():
        k = (r['market'], r['security_type'], r.get('isin_status', 'basic_data'))
        count[k] = count.get(k, 0) + 1
    print('as_of', as_of, 'companies', len(rows), sorted(count.items()))
    print('ISIN-only rows:', added)


if __name__ == '__main__':
    main()
