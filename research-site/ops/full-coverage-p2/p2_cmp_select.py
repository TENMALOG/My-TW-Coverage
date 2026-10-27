"""b03 model comparison: pick 6 companies (2 per market) with a readable FY report, seeded and reproducible.

  .venv/Scripts/python.exe -X utf8 research-site/ops/full-coverage-p2/p2_cmp_select.py

Writes batches/b03cmp.json (same shape as a batch file) so p2_codex.py can run it into out/b03cmp/.
"""
import json
import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
rows = json.loads((HERE / 'batches' / 'b03.json').read_text(encoding='utf-8'))
log = {json.loads(l)['ticker']: json.loads(l) for l in (HERE / 'out' / 'b03' / 'fetch.jsonl').read_text(encoding='utf-8').splitlines() if l.strip()}
ok = []
for r in rows:
    if not log.get(r['ticker'], {}).get('fy'):
        continue
    s = json.loads((ROOT / f"research-site/data/annual-slices/{r['ticker']}.json").read_text(encoding='utf-8'))
    if not s['garbled']:
        ok.append(r)
rng = random.Random(20261024)
pick = []
for market in ('上市', '上櫃', '興櫃'):
    pool = [r for r in ok if r['market'] == market]
    pick += rng.sample(pool, min(2, len(pool)))
(HERE / 'batches' / 'b03cmp.json').write_text(json.dumps(pick, ensure_ascii=False, indent=1), encoding='utf-8')
(HERE / 'out' / 'b03cmp').mkdir(parents=True, exist_ok=True)
print(' '.join(r['ticker'] for r in pick))
print([(r['ticker'], r['company'], r['market']) for r in pick])
