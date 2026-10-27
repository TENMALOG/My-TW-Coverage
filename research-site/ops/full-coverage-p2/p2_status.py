"""P2: per-batch status after verify_extraction.py — files, facts, FAIL facts (with failed checks), schema-blocked files.

  .venv/Scripts/python.exe -X utf8 research-site/ops/full-coverage-p2/p2_status.py b01
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
FACTS = ROOT / 'research-site/data/company-facts'
rows = json.loads((HERE / 'batches' / f'{sys.argv[1]}.json').read_text(encoding='utf-8'))
have = [r for r in rows if (FACTS / f"{r['ticker']}.json").exists()]
n = unverified = 0
fails = []
for r in have:
    d = json.loads((FACTS / f"{r['ticker']}.json").read_text(encoding='utf-8'))
    for f in d['facts']:
        n += 1
        v = f.get('verification')
        if not v:
            unverified += 1
        elif v.get('status') != 'PASS':
            fails.append((f['id'], [k for k, ok in v['checks'].items() if not ok], f['statement'][:70]))
print(f"companies with facts {len(have)}/{len(rows)}; facts {n}; unverified (schema-blocked) {unverified}; FAIL {len(fails)}")
for x in fails:
    print(' ', *x)
print('missing:', [r['ticker'] + ' ' + r['company'] for r in rows if r not in have])
