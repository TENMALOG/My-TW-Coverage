"""Apply the semantic review of listed-company edges and write the publishable edge list.

  python research-site/scripts/relations/apply_edge_review.py

Reads data/relations/relations.csv (edges with a counterparty_ticker) and data/relations/
edge_review.jsonl (one verdict per edge, keyed by fact_id + counterparty + counterparty_ticker:
ACCEPT, FIX_ROLE|<role> or REJECT|<reason>). Writes data/relations/listed_edges.csv with only the
accepted edges (role corrected where reviewed) and fails if any edge has no verdict.
"""
from __future__ import annotations

import csv
import json
from pathlib import Path

DATA = Path(__file__).resolve().parents[2] / 'data/relations'
ROLES = {'customer', 'supplier', 'parent', 'subsidiary', 'affiliate', 'investee'}


def key(r: dict) -> tuple:
    return (r['fact_id'], r['counterparty'], r['counterparty_ticker'])


def main():
    edges = [r for r in csv.DictReader((DATA / 'relations.csv').open(encoding='utf-8-sig')) if r['counterparty_ticker']]
    review = {}
    for line in (DATA / 'edge_review.jsonl').read_text(encoding='utf-8').splitlines():
        if line.strip():
            v = json.loads(line)
            review[(v['fact_id'], v['counterparty'], v['counterparty_ticker'])] = v['verdict']
    missing = [r['relation_id'] for r in edges if key(r) not in review]
    assert not missing, f'edges without a review verdict: {missing[:10]} ({len(missing)})'
    out, counts = [], {'ACCEPT': 0, 'FIX_ROLE': 0, 'REJECT': 0}
    for r in edges:
        verdict = review[key(r)]
        kind = verdict.split('|')[0]
        counts[kind] += 1
        if kind == 'REJECT':
            continue
        if kind == 'FIX_ROLE':
            role = verdict.split('|')[1]
            assert role in ROLES, verdict
            r = {**r, 'role': role}
        out.append(r)
    with (DATA / 'listed_edges.csv').open('w', encoding='utf-8-sig', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=list(edges[0].keys()))
        w.writeheader()
        w.writerows(out)
    print(f'edges={len(edges)} {counts} published={len(out)}')


if __name__ == '__main__':
    main()
