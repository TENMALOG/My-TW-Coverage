"""Write the second-pass review into the ledger and apply the adjudication of flagged facts.

  python research-site/ops/codex-review/apply_second_pass.py

1. Every ACCEPT from out/ (Codex) and out_sonnet/ (Sonnet) is appended to the review ledger.
2. adj_out_*.jsonl (adjudication of second-pass REJECTs and of the rank sweep):
   KEEP -> ledger ACCEPT; DROP -> ledger REJECT; FIX -> statement (and attribution) rewritten,
   logged to _manual-fixes.jsonl, re-verified with verify_extraction.py; ledger ACCEPT if the
   fact still passes, otherwise the old text is restored and the fact is rejected.
Idempotent per run: ids already carrying a second-pass verdict are skipped.
"""
import datetime as dt
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
FACTS = ROOT / 'research-site/data/company-facts'
LEDGER = FACTS / '_semantic-review.jsonl'
FIXLOG = FACTS / '_manual-fixes.jsonl'
import argparse
_ap = argparse.ArgumentParser()
_ap.add_argument('--adj', default=str(HERE / 'adj_out_*.jsonl'))
_ap.add_argument('--tag', default='second-pass-2026-10-18')
_ap.add_argument('--no-review-outputs', action='store_true')
_A = _ap.parse_args()
TAG = _A.tag
ATTR = {'公司年報揭露', '公司年報自述（未經獨立驗證的排名或評價）', '公司年報引述第三方資料'}
now = dt.datetime.now(dt.timezone.utc).isoformat(timespec='seconds')

done = set()
for line in LEDGER.read_text(encoding='utf-8').splitlines():
    if line.strip() and json.loads(line).get('batch') == TAG:
        done.add(json.loads(line)['id'])

entries, fixes = [], []
adj = {}
import glob as _glob
for f in sorted(Path(x) for x in _glob.glob(_A.adj)):
    for line in f.read_text(encoding='utf-8').splitlines():
        if line.strip():
            r = json.loads(line)
            adj[r['id']] = r

for src, folder, who in (() if _A.no_review_outputs else (('codex', 'out', 'Codex（GPT）第二輪審查'), ('sonnet', 'out_sonnet', 'Claude Sonnet 子代理第二輪審查'))):
    for f in sorted((HERE / folder).glob('cr*.jsonl')):
        for line in f.read_text(encoding='utf-8').splitlines():
            if not line.strip():
                continue
            r = json.loads(line)
            if r['id'] in done or r['id'] in adj:
                continue
            if str(r['verdict']).startswith('ACCEPT'):
                entries.append({'id': r['id'], 'verdict': 'ACCEPT', 'reason': r.get('reason', ''), 'reviewer': who,
                                'reviewed_at': now, 'batch': TAG})

by_ticker = {}
for fid, r in adj.items():
    if fid in done:
        continue
    by_ticker.setdefault(fid.split('-AR-')[0], []).append(r)

touched = []
for t, rows in by_ticker.items():
    p = FACTS / f'{t}.json'
    doc = json.loads(p.read_text(encoding='utf-8'))
    idx = {x['id']: x for x in doc['facts']}
    for r in rows:
        f = idx.get(r['id'])
        if f is None:
            continue
        act = r.get('action')
        if act == 'FIX' and r.get('new_statement', '').strip():
            old = {k: f[k] for k in ('statement', 'attribution')}
            f['statement'] = r['new_statement'].strip()
            if r.get('new_attribution') in ATTR:
                f['attribution'] = r['new_attribution']
            fixes.append({'ticker': t, 'id': f['id'], 'field': 'statement/attribution', 'old': old,
                          'new': {k: f[k] for k in ('statement', 'attribution')}, 'reason': r.get('reason', ''), 'at': now})
            touched.append(t)
        elif act == 'DROP':
            entries.append({'id': r['id'], 'verdict': 'REJECT', 'reason': r.get('reason', ''), 'reviewer': 'Claude 複核',
                            'reviewed_at': now, 'batch': TAG})
        elif act == 'KEEP':
            entries.append({'id': r['id'], 'verdict': 'ACCEPT', 'reason': '複核：' + r.get('reason', ''), 'reviewer': 'Claude 複核',
                            'reviewed_at': now, 'batch': TAG})
    p.write_text(json.dumps(doc, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')

# re-verify fixed companies; failing fixes are reverted and rejected
touched = sorted(set(touched))
if touched:
    subprocess.run([sys.executable, '-X', 'utf8', str(ROOT / 'research-site/scripts/annual/verify_extraction.py'), '--tickers', *touched],
                   cwd=ROOT, check=False, capture_output=True)
fixed_ids = {x['id']: x for x in fixes}
for t in touched:
    p = FACTS / f'{t}.json'
    doc = json.loads(p.read_text(encoding='utf-8'))
    for f in doc['facts']:
        if f['id'] not in fixed_ids:
            continue
        if (f.get('verification') or {}).get('status') == 'PASS':
            entries.append({'id': f['id'], 'verdict': 'ACCEPT', 'reason': '複核後修正：' + fixed_ids[f['id']]['reason'],
                            'reviewer': 'Claude 複核', 'reviewed_at': now, 'batch': TAG})
        else:
            f['statement'] = fixed_ids[f['id']]['old']['statement']
            f['attribution'] = fixed_ids[f['id']]['old']['attribution']
            fixes.append({'ticker': t, 'id': f['id'], 'field': 'statement', 'old': fixed_ids[f['id']]['new'],
                          'new': fixed_ids[f['id']]['old'], 'reason': '修正後未通過自動驗證，還原並退回', 'at': now})
            entries.append({'id': f['id'], 'verdict': 'REJECT', 'reason': '修正後未通過自動驗證：' + fixed_ids[f['id']]['reason'],
                            'reviewer': 'Claude 複核', 'reviewed_at': now, 'batch': TAG})
    p.write_text(json.dumps(doc, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
if touched:
    subprocess.run([sys.executable, '-X', 'utf8', str(ROOT / 'research-site/scripts/annual/verify_extraction.py'), '--tickers', *touched],
                   cwd=ROOT, check=False, capture_output=True)

with LEDGER.open('a', encoding='utf-8') as fh:
    for e in entries:
        fh.write(json.dumps(e, ensure_ascii=False) + '\n')
with FIXLOG.open('a', encoding='utf-8') as fh:
    for x in fixes:
        fh.write(json.dumps(x, ensure_ascii=False) + '\n')
acc = sum(1 for e in entries if e['verdict'] == 'ACCEPT')
print(f'ledger entries {len(entries)} (ACCEPT {acc}, REJECT {len(entries) - acc}); fixes logged {len(fixes)}; companies re-verified {len(touched)}')
