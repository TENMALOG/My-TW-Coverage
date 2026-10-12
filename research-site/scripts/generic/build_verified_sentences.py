"""Collect every publishable audited claim with its evidence citations.

A claim is publishable only if `adoptable_text` is non-empty in release-scope-claims.csv.
Evidence:
  - original sentences (adoption_basis '原句最終 ACCEPTED'):
      audit-v5/semantic/candidate-rerun/delivery/accepted-original-claims.jsonl (field adjudication)
  - revised sentences: the batch named in adoption_basis; LAST line in
      {batch}/adjudication/results.jsonl whose claim_id == revision_id and output is not null
      (revision-pilot-001: delivery/accepted-revisions.jsonl, field adjudication)
Citations = adjudication.atomic_claims[].evidence[] (deduplicated, excerpts verbatim).
Stops with exit code 1 if any publishable claim has no adjudication or no citation.

  python research-site/scripts/generic/build_verified_sentences.py
"""
from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from industries import ROOT, VERIFIED, claims, jsonl  # noqa: E402

CR = ROOT / 'audit-v5/semantic/candidate-rerun'
CITE_FIELDS = ('url', 'title', 'locator', 'publication_date', 'support_excerpt', 'inspection_method')
ORIGINAL = '原句最終 ACCEPTED'


def batch_of(basis: str) -> str | None:
    m = re.search(r'(revision-[a-z]+(?:-[a-z]+)*-\d{3})', basis)
    return m.group(1) if m else None


class Evidence:
    def __init__(self):
        self._cache: dict[str, dict] = {}
        self.original = {r['claim_id']: r['adjudication'] for r in jsonl(CR / 'delivery/accepted-original-claims.jsonl')}

    def batch(self, name: str) -> dict:
        if name not in self._cache:
            idx = {}
            if name == 'revision-pilot-001':
                for r in jsonl(CR / name / 'delivery/accepted-revisions.jsonl'):
                    if r.get('adjudication'):
                        idx[r['revision_id']] = r['adjudication']
            else:
                path = CR / name / 'adjudication/results.jsonl'
                if not path.exists():
                    raise SystemExit(f'missing adjudication file {path}')
                for r in jsonl(path):          # later lines overwrite earlier ones -> LAST wins
                    if r.get('output') is not None:
                        idx[r['claim_id']] = r['output']
            self._cache[name] = idx
        return self._cache[name]


def citations(adj: dict) -> list[dict]:
    out, seen = [], set()
    for ac in adj.get('atomic_claims') or []:
        for ev in ac.get('evidence') or []:
            c = {k: ev.get(k) for k in CITE_FIELDS}
            sig = json.dumps(c, ensure_ascii=False, sort_keys=True)
            if sig not in seen:
                seen.add(sig)
                out.append(c)
    return out


def build(out_path: Path = VERIFIED) -> Counter:
    ev = Evidence()
    rows, errors, stats = [], [], Counter()
    for c in claims():
        text = c['adoptable_text'].strip()
        if not text:
            continue
        basis = c['adoption_basis']
        if basis == ORIGINAL:
            adj, src = ev.original.get(c['claim_id']), 'accepted-original-claims'
        else:
            b = batch_of(basis)
            if not b:
                errors.append(f'{c["claim_id"]}: cannot parse batch from adoption_basis {basis!r}')
                continue
            if c['revision_id'] and c['revision_id'] not in basis:
                errors.append(f'{c["claim_id"]}: revision_id {c["revision_id"]} not named in adoption_basis')
                continue
            adj, src = ev.batch(b).get(c['revision_id']), b
        if adj is None:
            errors.append(f'{c["claim_id"]}: adjudication not found in {src}')
            continue
        cites = citations(adj)
        if not cites:
            errors.append(f'{c["claim_id"]}: adjudication in {src} has no evidence citations')
            continue
        rows.append({'claim_id': c['claim_id'], 'ticker': c['ticker'], 'company': c['company'],
                     'industry_folder': c['industry_folder'], 'claim_type': c['claim_type'],
                     'text': text, 'basis': basis, 'period': c['period_note'], 'citations': cites})
        stats['sentences'] += 1
        stats['citations'] += len(cites)
        stats['original' if basis == ORIGINAL else 'revised'] += 1
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        raise SystemExit(f'{len(errors)} publishable claims lack adjudication/evidence; nothing written')
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, 'w', encoding='utf-8', newline='\n') as fh:
        for r in rows:
            fh.write(json.dumps(r, ensure_ascii=False) + '\n')
    stats['companies'] = len({r['ticker'] for r in rows})
    stats['industries'] = len({r['industry_folder'] for r in rows})
    return stats


def main():
    s = build()
    print(f'verified sentences {s["sentences"]} (revised {s["revised"]}, original {s["original"]}); '
          f'citations {s["citations"]}; companies {s["companies"]}; industries {s["industries"]} -> {VERIFIED}')


if __name__ == '__main__':
    main()
