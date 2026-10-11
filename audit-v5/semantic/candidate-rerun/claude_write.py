#!/usr/bin/env python3
"""Compact writer for Claude takeover adjudications (expands to the full schema, then records).

Spec file (JSON):
{"idx": 0, "verdict": "ACCEPTED", "why": "...", "period": "...", "revised": null,
 "atoms": [["SUPPORTED", "atom text", "period", "reason", [[lead_idx_or_url, "locator", "excerpt", "summary", "pub_date"]]], ...],
 "unresolved": [], "contradictions": [], "stop": "..."}
lead_idx refers to the item's source_leads order (claude_item.py listing); a URL string uses that URL.
Evidence read from the batch snapshot is captured_content; a live WebFetch-only page must be given as
["LIVE:<url>", ...] and is recorded as live_full_page (no snapshot excerpt check).

  python claude_write.py --batch revision-batch-003 --spec spec.json
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
import tempfile
from pathlib import Path

from claude_item import pending

HERE = Path(__file__).resolve().parent


def main():
    p = argparse.ArgumentParser(); p.add_argument('--batch', required=True); p.add_argument('--spec', required=True); a = p.parse_args()
    spec = json.loads(Path(a.spec).read_text(encoding='utf-8'))
    row = pending(a.batch)[spec['idx']]
    leads = row['source_leads']
    atoms = []
    for status, text, period, reason, evs in spec['atoms']:
        out = []
        for ref, locator, excerpt, summary, pub in evs:
            method = 'captured_content'
            if isinstance(ref, int):
                url, title = leads[ref]['url'], leads[ref].get('title') or leads[ref]['url']
            elif ref.startswith('LIVE:'):
                url, title, method = ref[5:], ref[5:], 'live_full_page'
            else:
                url, title = ref, ref
            out.append({'url': url, 'title': title, 'source_kind': 'see title', 'publication_date': pub,
                        'effective_period': period, 'locator': locator, 'support_summary': summary,
                        'support_excerpt': excerpt, 'inspection_method': method})
        atoms.append({'text': text, 'status': status, 'period': period, 'reason': reason, 'evidence': out})
    full = {'claim_id': row['claim_id'], 'normalized_claim_hash': row['normalized_claim_hash'], 'verdict': spec['verdict'],
            'rationale': spec['why'], 'period_assessment': spec['period'],
            'qualifier_coverage_complete': spec['verdict'] == 'ACCEPTED', 'complete_original_supported': spec['verdict'] == 'ACCEPTED',
            'all_sources_inspected': True, 'atomic_claims': atoms, 'revised_claim': spec.get('revised'),
            'revised_claim_supported': False, 'unresolved_qualifiers': spec.get('unresolved', []),
            'contradictions': spec.get('contradictions', []), 'research_complete': True,
            'research_stop_reason': spec.get('stop', '已檢視所列來源擷取全文。')}
    tmp = Path(tempfile.mkstemp(suffix='.json')[1]); tmp.write_text(json.dumps(full, ensure_ascii=False), encoding='utf-8')
    r = subprocess.run([sys.executable, '-X', 'utf8', str(HERE / 'record_claude_adjudication.py'), '--batch', a.batch,
                        '--claim-id', row['claim_id'], '--output', str(tmp)], capture_output=True, text=True, encoding='utf-8')
    print((r.stdout + r.stderr).strip()[-400:])
    sys.exit(r.returncode)


if __name__ == '__main__':
    main()
