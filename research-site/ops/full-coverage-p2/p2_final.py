"""P2: final adjudication for one batch (conservative: REJECT if either pass rejects), plus manager overrides.

  .venv/Scripts/python.exe -X utf8 research-site/ops/full-coverage-p2/p2_final.py b05 [--override ID=reason ...] [--note ID=text ...]

Reads out/{batch}/review/r??.out.jsonl (+ any first-pass *.first.jsonl) and second-?.out.jsonl;
writes out/{batch}/review/final-adjudication.jsonl and prints the overturn rate and the REJECT list.
"""
import glob
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
batch = sys.argv[1]
D = HERE / 'out' / batch / 'review'
over_ride, notes = {}, {}
for flag, val in zip(sys.argv[2:], sys.argv[3:]):
    if flag in ('--override', '--note'):
        k, v = val.split('=', 1)
        (over_ride if flag == '--override' else notes)[k] = v


def load(f):
    return [json.loads(l) for l in Path(f).read_text(encoding='utf-8').splitlines() if l.strip()]


first = {r['id']: r for f in sorted(glob.glob(str(D / 'r??.out.jsonl'))) + sorted(glob.glob(str(D / '*.first.jsonl'))) for r in load(f)}
# *.fix.jsonl: re-review of first-pass verdicts given under a wrong instruction (2026-10-25: 「N年」 counted as an
# unlabelled ROC year); the fix replaces only those ids and records the original verdict
for f in sorted(glob.glob(str(D / '*.fix.jsonl'))):
    for r in load(f):
        r['reason'] = f"{r['reason']}（重審；原判 {first[r['id']]['verdict']}：{first[r['id']]['reason'][:60]}）"
        first[r['id']] = r
sec = {}
for f in sorted(glob.glob(str(D / 'second-*.out.jsonl'))):
    for r in load(f):
        if r['id'] not in sec or r['verdict'] != 'ACCEPT':
            sec[r['id']] = r
acc = [i for i in sec if first[i]['verdict'] == 'ACCEPT']
over = [i for i in acc if sec[i]['verdict'] != 'ACCEPT']
print(f'first {len(first)}; second {len(sec)}; first-accept reviewed {len(acc)}; overturned {len(over)} '
      f'({len(over) / max(1, len(acc)):.1%}) {over}')
out, rej = [], []
for i, r in sorted(first.items()):
    s = sec.get(i)
    final = 'ACCEPT' if r['verdict'] == 'ACCEPT' and (s is None or s['verdict'] == 'ACCEPT') else 'REJECT'
    reason = '' if final == 'ACCEPT' else (s['reason'] if s and s['verdict'] != 'ACCEPT' else r['reason'])
    if i in over_ride:
        final, reason = 'REJECT', '總經理改判：' + over_ride[i]
    if i in notes:
        reason = '總經理核對：' + notes[i]
    if final != 'ACCEPT':
        rej.append(i)
    out.append(dict(id=i, first=r['verdict'], first_reason=r['reason'], second=s and s['verdict'],
                    second_reason=s and s['reason'], final=final, final_reason=reason))
(D / 'final-adjudication.jsonl').write_text(''.join(json.dumps(x, ensure_ascii=False) + '\n' for x in out), encoding='utf-8')
print(f'final {len(out)}: ACCEPT {len(out) - len(rej)}, REJECT {len(rej)} {rej}')
