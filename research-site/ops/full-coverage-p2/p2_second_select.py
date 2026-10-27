"""P2: pick the second-review ids for one batch and split them in two (second-a.txt / second-b.txt).

  .venv/Scripts/python.exe -X utf8 research-site/ops/full-coverage-p2/p2_second_select.py b08 [--seed 20261024]

First pass = review/r??.out.jsonl with review/*.fix.jsonl applied. Must-review: every non-ACCEPT,
every glyph-flagged id (out/{b}/glyph-flags.jsonl) and review/second-extra.txt; plus a seeded 15 % sample
of the remaining ACCEPTs. Ids already listed in an earlier second*.txt round are skipped (addenda use
--suffix c to write second-c.txt only).
"""
import argparse
import glob
import json
import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
ap = argparse.ArgumentParser()
ap.add_argument('batch'); ap.add_argument('--seed', type=int, default=20261024); ap.add_argument('--suffix')
a = ap.parse_args()
D = HERE / 'out' / a.batch / 'review'


def load(f):
    return [json.loads(l) for l in Path(f).read_text(encoding='utf-8').splitlines() if l.strip()]


for f in sorted(glob.glob(str(D / 'r??.out.jsonl'))):
    ids = [l.strip() for l in Path(f.replace('.out.jsonl', '.txt')).read_text(encoding='utf-8').splitlines() if l.strip()]
    assert ids == [r['id'] for r in load(f)], f'{f}: ids differ from the id file'
rows = {r['id']: r for f in sorted(glob.glob(str(D / 'r??.out.jsonl'))) for r in load(f)}
for f in sorted(glob.glob(str(D / '*.fix.jsonl'))):
    for r in load(f):
        rows[r['id']] = r
flags = {json.loads(l)['id'] for l in (HERE / 'out' / a.batch / 'glyph-flags.jsonl').read_text(encoding='utf-8').splitlines() if l.strip()}
extra_f = D / 'second-extra.txt'
extra = {l.strip() for l in extra_f.read_text(encoding='utf-8').splitlines() if l.strip()} if extra_f.exists() else set()
done = set()
if a.suffix:
    for f in glob.glob(str(D / 'second*.txt')):
        if not f.endswith(('second-extra.txt', f'second-{a.suffix}.txt')):
            done |= {l.strip() for l in Path(f).read_text(encoding='utf-8').splitlines() if l.strip()}
must = {i for i, r in rows.items() if r['verdict'] != 'ACCEPT' or i in flags} | (extra & set(rows))
acc = sorted(i for i, r in rows.items() if r['verdict'] == 'ACCEPT' and i not in flags and i not in done)
sample = random.Random(a.seed).sample(acc, round(len(acc) * 0.15))
ids = sorted((must | set(sample)) - done)
if a.suffix:
    (D / f'second-{a.suffix}.txt').write_text('\n'.join(ids) + '\n', encoding='utf-8')
else:
    h = (len(ids) + 1) // 2
    (D / 'second.txt').write_text('\n'.join(ids) + '\n', encoding='utf-8')
    (D / 'second-a.txt').write_text('\n'.join(ids[:h]) + '\n', encoding='utf-8')
    (D / 'second-b.txt').write_text('\n'.join(ids[h:]) + '\n', encoding='utf-8')
print(f'{a.batch}: first pass {len(rows)}, must {len(must)}, sample {len(sample)} -> {len(ids)} ids')
