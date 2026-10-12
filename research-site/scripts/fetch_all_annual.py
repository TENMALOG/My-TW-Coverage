"""Fetch the latest MOPS annual report (F04) for every company in the release catalog.

  python research-site/scripts/fetch_all_annual.py [--limit N] [--workers 2] [--delay 2]

Tries FY2025 first, then FY2024. Already-captured reports are reused (fetch() reads the
cached metadata), so the run can be interrupted and resumed. Progress is appended to
audit-v5/source-cache/research-site/mops-annual/fetch-all-log.jsonl.
"""
from __future__ import annotations

import argparse
import csv
import json
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone

from fetch_mops_annual import CACHE, ROOT, RateLimited, fetch

LOG = CACHE / 'fetch-all-log.jsonl'
lock = threading.Lock()


backoff_until = [0.0]


def wait_for_backoff():
    while True:
        with lock:
            left = backoff_until[0] - time.time()
        if left <= 0:
            return
        time.sleep(min(left, 30))


def fetch_with_backoff(ticker, fy):
    pause = 120
    while True:
        wait_for_backoff()
        try:
            return fetch(ticker, fy)
        except RateLimited:
            # every worker pauses together; the pause doubles up to 30 minutes
            with lock:
                backoff_until[0] = max(backoff_until[0], time.time() + pause)
            print(f'{ticker} rate limited, pausing {pause}s', flush=True)
            pause = min(pause * 2, 1800)


def one(ticker, delay):
    result = {'ticker': ticker}
    for fy in (2025, 2024):
        try:
            meta = fetch_with_backoff(ticker, fy)
        except Exception as exc:  # network or PDF errors are logged, never fatal
            meta = {'status': 'error', 'error': f'{type(exc).__name__}: {exc}'[:300]}
        time.sleep(delay)
        result = {'ticker': ticker, 'fy': fy, 'status': meta.get('status'), 'error': meta.get('error')}
        if meta.get('status') == 'captured':
            break
    result['at'] = datetime.now(timezone.utc).isoformat()
    with lock:
        with open(LOG, 'a', encoding='utf-8') as f:
            f.write(json.dumps(result, ensure_ascii=False) + '\n')
    print(result['ticker'], result['fy'], result['status'], result.get('error') or '', flush=True)
    return result


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--limit', type=int)
    p.add_argument('--workers', type=int, default=1)
    p.add_argument('--delay', type=float, default=6.0)
    a = p.parse_args()
    rows = list(csv.DictReader(open(ROOT / 'research-site/catalog/release-scope-companies.csv', encoding='utf-8-sig')))
    # largest industries first, matching the chapter order
    size = {}
    for r in rows:
        size[r['industry_folder']] = size.get(r['industry_folder'], 0) + 1
    rows.sort(key=lambda r: (-size[r['industry_folder']], r['industry_folder'], r['ticker']))
    tickers = [r['ticker'] for r in rows][:a.limit]
    CACHE.mkdir(parents=True, exist_ok=True)
    with ThreadPoolExecutor(a.workers) as ex:
        results = list(ex.map(lambda t: one(t, a.delay), tickers))
    ok = sum(r['status'] == 'captured' for r in results)
    print(f'captured {ok}/{len(results)}')


if __name__ == '__main__':
    main()
