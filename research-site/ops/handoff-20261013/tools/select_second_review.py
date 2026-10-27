"""Pick the ids for the second, independent review (review_rules_v4.md, "Second review").

  .venv/Scripts/python.exe -X utf8 research-site/ops/handoff-20261013/tools/select_second_review.py OUT_IDS FIRST_PASS.jsonl [...] [--rate 0.15] [--seed 20261024]

Every REJECT/FIX of the first pass, every fact flagged by scan_glyphs.py, and a seeded random
--rate share of the remaining ACCEPTs. Same inputs + seed -> same selection.
"""
import argparse
import json
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
FLAGS = ROOT / 'research-site/data/company-facts/_glyph-flags.jsonl'

ap = argparse.ArgumentParser()
ap.add_argument('out'); ap.add_argument('first', nargs='+')
ap.add_argument('--rate', type=float, default=0.15); ap.add_argument('--seed', type=int, default=20261024)
a = ap.parse_args()
rows = [json.loads(l) for f in a.first for l in Path(f).read_text(encoding='utf-8').splitlines() if l.strip()]
flagged = {json.loads(l)['id'] for l in FLAGS.read_text(encoding='utf-8').splitlines() if l.strip()} if FLAGS.exists() else set()
must = [r['id'] for r in rows if r['verdict'] != 'ACCEPT' or r['id'] in flagged]
accepts = sorted(r['id'] for r in rows if r['verdict'] == 'ACCEPT' and r['id'] not in flagged)
k = max(1, round(len(accepts) * a.rate)) if accepts else 0
sample = random.Random(a.seed).sample(accepts, k)
ids = sorted(set(must) | set(sample))
Path(a.out).write_text('\n'.join(ids) + '\n', encoding='utf-8')
print(f'first-pass {len(rows)}: non-accept/flagged {len(must)}, accept sample {k}/{len(accepts)} -> {len(ids)} ids')
