"""Prospectus rules v2: pick second-review ids for first-review groups and split them into review files.

  .venv/Scripts/python.exe -X utf8 research-site/ops/full-coverage-p2/prospectus/second_select.py r04 r05 ... --out d e [--seed 20261024]

Must-review: every non-ACCEPT, every glyph-flagged id and review/second-extra.txt; plus a seeded 15 % sample of
the remaining ACCEPTs of the named groups only (the pilot groups were second-reviewed in full). Writes
review/second-{x}.txt for each --out name, ids split evenly.
"""
import argparse
import json
import random
from pathlib import Path

D = Path(__file__).resolve().parent / 'review'
ap = argparse.ArgumentParser()
ap.add_argument('groups', nargs='+'); ap.add_argument('--out', nargs='+', required=True); ap.add_argument('--seed', type=int, default=20261024)
a = ap.parse_args()


def load(f):
    return [json.loads(l) for l in Path(f).read_text(encoding='utf-8').splitlines() if l.strip()]


rows = {}
for g in a.groups:
    ids = [l.strip() for l in (D / f'{g}.txt').read_text(encoding='utf-8').splitlines() if l.strip()]
    out = load(D / f'{g}.out.jsonl')
    assert ids == [r['id'] for r in out], f'{g}: ids differ from the id file'
    rows.update({r['id']: r for r in out})
gf = D.parent / 'glyph-flags.jsonl'
flags = {json.loads(l)['id'] for l in gf.read_text(encoding='utf-8').splitlines() if l.strip()} if gf.exists() else set()
ef = D / 'second-extra.txt'
extra = {l.strip() for l in ef.read_text(encoding='utf-8').splitlines() if l.strip()} if ef.exists() else set()
must = {i for i, r in rows.items() if r['verdict'] != 'ACCEPT' or i in flags or i in extra}
acc = sorted(i for i in rows if i not in must)
sample = random.Random(a.seed).sample(acc, round(len(acc) * 0.15))
ids = sorted(must | set(sample))
n = len(a.out)
for k, name in enumerate(a.out):
    part = ids[k * len(ids) // n:(k + 1) * len(ids) // n]
    (D / f'second-{name}.txt').write_text('\n'.join(part) + '\n', encoding='utf-8')
print(f'first pass {len(rows)}, must {len(must)}, sample {len(sample)} -> {len(ids)} ids in {n} files')
