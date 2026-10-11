#!/usr/bin/env python3
"""Append capture repairs without changing the isolated model judgment."""
import argparse
import json
from pathlib import Path
import run_revision_pilot as revision


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('claim_id'); args = ap.parse_args()
    revision.configure('high'); worker = revision.worker
    rows = [json.loads(x) for x in (worker.ROOT/'results.jsonl').read_text().splitlines()]
    row = next(r for r in reversed(rows) if r['claim_id']==args.claim_id)
    if row['verdict']!='PENDING_PROOF_REVIEW' or row['model_verdict']!='ACCEPTED':
        raise ValueError('Only an acceptance held for captured proof may be repaired')
    if not row['acceptance_hold_reasons'] or any(not x.startswith('Direct supporting excerpt not reproduced in captured source: ') for x in row['acceptance_hold_reasons']):
        raise ValueError('Non-capture hold requires a new independent judgment')
    for path, expected in [(row['execution']['output_path'], row['output_sha256']),
                           (row['execution']['prompt_path'], row['execution']['prompt_sha256'])]:
        if worker.digest((worker.BASE/path).read_bytes())!=expected:
            raise ValueError('Immutable execution artifact changed')
    if json.loads((worker.BASE/row['execution']['output_path']).read_text())!=row['adjudication']:
        raise ValueError('Stored adjudication differs from actual model output')
    for field in ['original_report_context_snapshot', 'claim_output_schema_snapshot', 'revision_controller_snapshot']:
        b = row['execution'][field]
        if worker.digest((worker.BASE/b['path']).read_bytes())!=b['sha256']:
            raise ValueError('Execution snapshot changed')
    if revision.placement_context(row['original_claim'])!=json.loads((worker.BASE/row['execution']['original_report_context_snapshot']['path']).read_text()):
        raise ValueError('Frozen placement context changed')
    reasons, proof = worker.acceptance_problems(row['adjudication'], row['execution']['runtime_selection'])
    if reasons:
        raise ValueError('New proof still fails unchanged gate: '+str(reasons))
    parent = (json.dumps(row, ensure_ascii=False, indent=2)+'\n').encode()
    code = Path(__file__).read_bytes(); directory = worker.CACHE/'revision-capture-repairs'; directory.mkdir(exist_ok=True)
    parent_path = directory/(worker.digest(parent)+'.json'); code_path = directory/(worker.digest(code)+'.py')
    for path, data in [(parent_path, parent), (code_path, code)]:
        if path.exists() and path.read_bytes()!=data:
            raise ValueError('Content address collision')
        path.write_bytes(data)
    corrected = {**row, 'verdict': 'CANDIDATE_REVISED_SUPPORTED', 'acceptance_hold_reasons': [],
        'source_captures': list(proof.values()), 'proof_capture_repair': {'repaired_at': worker.now(),
            'parent_row_path': str(parent_path.relative_to(worker.BASE)), 'parent_row_sha256': worker.digest(parent),
            'repair_code_path': str(code_path.relative_to(worker.BASE)), 'repair_code_sha256': worker.digest(code),
            'model_output_unchanged': True, 'new_model_execution': False}}
    # Retain the wrapper fingerprint of the actual model execution.
    queue = [json.loads(x) for x in (revision.ROOT/'queue.jsonl').read_text().splitlines()]
    revision.save(corrected, queue)
    print(json.dumps({'claim_id': args.claim_id, 'status': corrected['verdict'], 'requires_primary_review': True}))


if __name__=='__main__':
    main()
