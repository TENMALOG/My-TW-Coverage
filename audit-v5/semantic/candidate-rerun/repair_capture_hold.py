#!/usr/bin/env python3
"""Append a capture-only correction for a verified Sol acceptance output.

Never changes the model output, claim, execution binding or semantic decision.
Primary-source semantic review remains mandatory before delivery acceptance.
"""
import argparse
import json
from pathlib import Path
import run_final_adjudication as controller


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('claim_id')
    args = parser.parse_args()
    rows = [json.loads(line) for line in (controller.ROOT/'results.jsonl').read_text().splitlines()]
    row = next(r for r in reversed(rows) if r['claim_id'] == args.claim_id)
    if row['verdict'] != 'PENDING_PROOF_REVIEW' or row['model_verdict'] != 'ACCEPTED':
        raise ValueError('Only an existing Sol acceptance held for captured proof can be repaired')
    if not row['acceptance_hold_reasons'] or any(not r.startswith('Direct supporting excerpt not reproduced in captured source: ') for r in row['acceptance_hold_reasons']):
        raise ValueError('Hold is not exclusively an evidence capture failure')
    for kind, expected in [('prompt', row['execution']['prompt_sha256']), ('output', row['output_sha256'])]:
        path = controller.BASE/row['execution'][kind+'_path']
        if controller.digest(path.read_bytes()) != expected:
            raise ValueError('Immutable execution artifact mismatch')
    if json.loads((controller.BASE/row['execution']['output_path']).read_text()) != row['adjudication']:
        raise ValueError('Adjudication differs from actual Sol output')
    context = row['execution'].get('original_report_context_snapshot')
    if not context or any(controller.digest((controller.BASE/context[path_key]).read_bytes()) != context[hash_key]
        for path_key, hash_key in [('path', 'sha256'), ('report_path', 'report_sha256')]):
        raise ValueError('The Sol review must contain a verified original report-context snapshot')
    reasons, proof = controller.acceptance_problems(row['adjudication'], row['execution']['runtime_selection'])
    if reasons:
        raise ValueError('Actual captures do not yet satisfy the unchanged acceptance gate: '+str(reasons))
    parent_bytes = (json.dumps(row, ensure_ascii=False, indent=2)+'\n').encode()
    parent_sha = controller.digest(parent_bytes)
    parent_path = controller.CACHE/'capture-repairs'/(parent_sha+'.json')
    parent_path.parent.mkdir(parents=True, exist_ok=True)
    if parent_path.exists() and parent_path.read_bytes() != parent_bytes:
        raise ValueError('Parent snapshot collision')
    parent_path.write_bytes(parent_bytes)
    code_bytes = Path(__file__).read_bytes()
    code_sha = controller.digest(code_bytes)
    code_path = controller.CACHE/'capture-repairs/controllers'/(code_sha+'.py')
    code_path.parent.mkdir(parents=True, exist_ok=True)
    if code_path.exists() and code_path.read_bytes() != code_bytes:
        raise ValueError('Repair controller snapshot collision')
    code_path.write_bytes(code_bytes)
    corrected = {**row, 'verdict': row['model_verdict'], 'acceptance_hold_reasons': [],
        'source_captures': list(proof.values()),
        'proof_capture_repair': {'repaired_at': controller.now(), 'parent_row_path': str(parent_path.relative_to(controller.BASE)),
            'parent_row_sha256': parent_sha, 'model_output_unchanged': True, 'new_model_execution': False,
            'repair_code_sha256': code_sha}}
    queue = controller.make_queue(row['cohort'])
    controller.save(corrected, queue)
    print(json.dumps({'claim_id': args.claim_id, 'verdict': corrected['verdict'], 'model_output_unchanged': True,
        'requires_primary_source_review': True}, ensure_ascii=False))


if __name__ == '__main__':
    main()
