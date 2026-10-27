"""P2: list the companies still to add (official directory minus the original 1,733 reports minus the P1
pilot) and split them into batches of 50, ordered by ticker. Writes batches/b01.json ... and plan.json.

  .venv/Scripts/python.exe -X utf8 research-site/ops/full-coverage-p2/p2_plan.py
"""
import collections
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
SIZE = 50
directory = json.loads((ROOT / 'research-site/data/official-directory.json').read_text(encoding='utf-8'))
reports = {m.group(1) for p in (ROOT / 'Pilot_Reports').rglob('*.md') if (m := re.match(r'(\w+?)_', p.name))}
pilot = {r['ticker'] for r in json.loads((ROOT / 'research-site/ops/full-coverage-p1/p1-selection.json').read_text(encoding='utf-8'))['pilot']}
todo = [c for c in directory['companies'] if c['security_type'] == 'stock' and c['ticker'] not in reports | pilot]
todo.sort(key=lambda c: c['ticker'])
(HERE / 'batches').mkdir(exist_ok=True)
batches = []
for i in range(0, len(todo), SIZE):
    name = f'b{i // SIZE + 1:02d}'
    rows = [{'ticker': c['ticker'], 'company': c['short_name'], 'legal_name': c['legal_name'], 'market': c['market']} for c in todo[i:i + SIZE]]
    (HERE / 'batches' / f'{name}.json').write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding='utf-8')
    batches.append({'batch': name, 'count': len(rows), 'markets': dict(collections.Counter(r['market'] for r in rows))})
plan = {'directory_as_of': directory['as_of'], 'reports': len(reports), 'pilot': len(pilot), 'todo': len(todo), 'batches': batches}
(HERE / 'plan.json').write_text(json.dumps(plan, ensure_ascii=False, indent=1), encoding='utf-8')
print(json.dumps({k: v for k, v in plan.items() if k != 'batches'}, ensure_ascii=False), len(batches), 'batches')
print('by market', dict(collections.Counter(c['market'] for c in todo)))
