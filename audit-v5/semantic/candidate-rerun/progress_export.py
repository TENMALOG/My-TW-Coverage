#!/usr/bin/env python3
"""Export revision-verification progress as JSON rows for the progress dashboard.

  python progress_export.py --out <dir>

Writes <dir>/batches.json (one row per batch, plus a "未排入" row for revisions not yet queued)
and <dir>/overall.json (one row: totals and Codex quota). Read-only over the batch folders.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

from run_revision_batch import HERE, read_jsonl

ORDER = ['revision-pilot-001', 'revision-aero-001', 'revision-aero-002', 'revision-orig-alt-001']
EST_BATCH = 100


def batch_rows():
    dirs = [d for d in HERE.glob('revision-*') if (d / 'queue.jsonl').exists()]
    dirs.sort(key=lambda d: (ORDER.index(d.name) if d.name in ORDER else 99, d.name))
    inv = {r['parent_claim_id'] for r in read_jsonl(HERE / 'revision-pilot-001/inventory.jsonl')}
    queued, rows, fin_p, work_p = set(), [], set(), set()
    for i, d in enumerate(dirs, 1):
        q = list(read_jsonl(d / 'queue.jsonl'))
        queued |= {r['parent_claim_id'] for r in q}
        res = d / 'adjudication/results.jsonl'
        results = [r for r in read_jsonl(res) if r.get('output')] if res.exists() else []
        last = {r['claim_id']: r for r in results}
        done_ids = set(last)
        runtime = Counter(r['execution'].get('runtime') == 'claude_takeover' for r in last.values())
        out = d / 'delivery/outcomes.jsonl'
        outcomes = Counter()
        if out.exists():
            for r in read_jsonl(out):
                outcomes[r.get('verdict') or 'OTHER'] += 1
        finalized = sum(outcomes.values())
        if d.name == 'revision-pilot-001':
            finalized = len(q)  # frozen pilot, delivered before this pipeline
        status = '已結案' if finalized >= len(q) else ('覆核中' if len(done_ids) >= len(q) else ('裁定中' if done_ids else '待開始'))
        (fin_p if status == '已結案' else work_p).update(r['parent_claim_id'] for r in q)
        rows.append({
            'order': i, 'batch': d.name, 'size': len(q), 'adjudicated': len(done_ids),
            'by_claude': runtime.get(True, 0), 'by_codex': runtime.get(False, 0), 'finalized': finalized,
            'supported': outcomes.get('REVISED_SUPPORTED', 0),
            'partial': outcomes.get('PARTIALLY_SUPPORTED', 0),
            'other': finalized - outcomes.get('REVISED_SUPPORTED', 0) - outcomes.get('PARTIALLY_SUPPORTED', 0) if outcomes else 0,
            'status': status,
        })
    remaining = len(inv - queued)
    n = len(rows)
    last_no = max([int(m[1]) for r in rows if (m := re.match(r'revision-batch-(\d+)$', r['batch']))] or [0])
    k = 0
    while remaining > 0:
        k += 1
        size = min(EST_BATCH, remaining)
        rows.append({'order': n + k, 'batch': f'（預估）revision-batch-{last_no + k:03d}', 'size': size, 'adjudicated': 0,
                     'by_claude': 0, 'by_codex': 0, 'finalized': 0, 'supported': 0, 'partial': 0, 'other': 0,
                     'status': '未建立'})
        remaining -= size
    return rows, len(inv), len(fin_p & inv), len((work_p - fin_p) & inv)


def quota():
    try:
        r = subprocess.run([sys.executable, '-X', 'utf8', str(HERE / 'codex_quota.py')], capture_output=True,
                           text=True, encoding='utf-8', timeout=60)
        m = re.search(r'five_hour=([\d.]+)% \(resets ([^)]+)\) weekly=([\d.]+)% \(resets ([^)]+)\)', r.stdout)
        if m:
            return {'codex_5h_used': float(m[1]), 'codex_5h_reset': m[2], 'codex_week_used': float(m[3]),
                    'codex_week_reset': m[4]}
    except Exception:  # noqa: BLE001
        pass
    return {'codex_5h_used': None, 'codex_5h_reset': '', 'codex_week_used': None, 'codex_week_reset': ''}


def main():
    p = argparse.ArgumentParser(); p.add_argument('--out', required=True); a = p.parse_args()
    out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
    rows, total, fin, working = batch_rows()
    current = next((r['batch'] for r in rows if r['status'] in ('裁定中', '覆核中', '待開始')), '')
    overall = {'total': total, 'finalized': fin, 'in_progress': working, 'not_queued': total - fin - working,
               'batches_total': len(rows), 'batches_done': sum(r['status'] == '已結案' for r in rows),
               'current_batch': current,
               'as_of': datetime.now(timezone.utc).astimezone().strftime('%Y-%m-%d %H:%M'), **quota()}
    (out / 'batches.json').write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding='utf-8')
    (out / 'overall.json').write_text(json.dumps([overall], ensure_ascii=False, indent=1), encoding='utf-8')
    print(json.dumps(overall, ensure_ascii=False))


if __name__ == '__main__':
    main()
