#!/usr/bin/env python3
"""Derive delivery artifacts; never treat a progress snapshot as completion."""
import hashlib
import json
import importlib.util
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

BASE = Path(__file__).resolve().parents[3]
ROOT = Path(__file__).resolve().parent
FINAL = ROOT / 'adjudication'
DELIVERY = ROOT / 'delivery'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_rows(path):
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()] if path.exists() else []


def dump(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


def main():
    DELIVERY.mkdir(parents=True, exist_ok=True)
    candidate = {}
    for path in sorted((ROOT / 'batches').glob('batch-*.jsonl')):
        for row in read_rows(path):
            candidate[row['queue_sequence']] = row
    final = {row['claim_id']: row for row in read_rows(FINAL / 'results.jsonl')}
    primary = {row['claim_id']: row for row in read_rows(FINAL / 'primary-source-review.jsonl')}
    blockers = []
    module_spec = importlib.util.spec_from_file_location('final_controller', ROOT / 'run_final_adjudication.py')
    controller = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(controller)
    cohorts = {}
    for cohort in ('original', 'candidate'):
        path = FINAL / f'{cohort}-queue.jsonl'
        queue = read_rows(path)
        manifest = json.loads(path.with_suffix('.manifest.json').read_text()) if path.exists() else None
        if manifest and (sha(path) != manifest['sha256'] or len(queue) != manifest['count']):
            blockers.append({'kind': 'frozen_queue_integrity', 'cohort': cohort})
        missing = [row['claim_id'] for row in queue if row['claim_id'] not in final]
        reviewed = [final[row['claim_id']] for row in queue if row['claim_id'] in final]
        cohorts[cohort] = {'frozen': path.exists(), 'queued': len(queue), 'reviewed': len(reviewed),
                           'remaining': len(missing), 'verdicts': dict(Counter(row['verdict'] for row in reviewed))}
        blockers.extend({'kind': 'missing_adjudication', 'claim_id': identity} for identity in missing)
        if not path.exists():
            blockers.append({'kind': 'unfrozen_cohort', 'cohort': cohort})
        if cohort == 'original' and len(queue) != 111:
            blockers.append({'kind': 'original_cohort_count', 'actual': len(queue)})
        if cohort == 'candidate' and path.exists():
            expected = {row['claim']['claim_id'] for row in candidate.values() if row['verdict'] == 'CANDIDATE_ACCEPTED'}
            if {row['claim_id'] for row in queue} != expected:
                blockers.append({'kind': 'candidate_cohort_membership'})
        for item in reviewed:
            frozen = next(row for row in queue if row['claim_id'] == item['claim_id'])
            if item['original_claim'] != frozen:
                blockers.append({'kind': 'original_claim_identity', 'claim_id': item['claim_id']})
    published = []
    for identity, row in final.items():
        if row.get('proof_capture_repair'):
            repair = row['proof_capture_repair']
            parent_path = BASE/repair['parent_row_path']
            repair_code = controller.CACHE/'capture-repairs/controllers'/(repair['repair_code_sha256']+'.py')
            valid = (parent_path.is_file() and sha(parent_path) == repair['parent_row_sha256'] and
                repair_code.is_file() and sha(repair_code) == repair['repair_code_sha256'])
            if valid:
                parent = json.loads(parent_path.read_text())
                immutable_keys = ('claim_id', 'cohort', 'original_claim', 'adjudication', 'model_verdict', 'execution', 'output_sha256', 'adjudicated_at')
                valid = (all(row[key] == parent[key] for key in immutable_keys) and
                    parent['verdict'] == 'PENDING_PROOF_REVIEW' and parent['model_verdict'] == 'ACCEPTED' and
                    bool(parent['acceptance_hold_reasons']) and all(reason.startswith('Direct supporting excerpt not reproduced in captured source: ') for reason in parent['acceptance_hold_reasons']) and
                    repair.get('model_output_unchanged') is True and repair.get('new_model_execution') is False)
            if not valid:
                blockers.append({'kind': 'proof_capture_repair_integrity', 'claim_id': identity})
                continue
        execution = row['execution']
        if execution.get('claim_output_schema_snapshot'):
            binding = execution['claim_output_schema_snapshot']
            schema_path = BASE/binding['path']
            valid = schema_path.is_file() and sha(schema_path) == binding['sha256']
            if valid:
                claim_schema = json.loads(schema_path.read_text())
                valid = all(claim_schema['properties'][field].get('enum') == [row['original_claim'][field]] for field in ('claim_id', 'normalized_claim_hash'))
            if not valid:
                blockers.append({'kind': 'claim_output_schema_integrity', 'claim_id': identity})
        if execution.get('controller_version_path'):
            version = BASE/execution['controller_version_path']
            if not version.is_file() or sha(version) != execution['controller_sha256']:
                blockers.append({'kind': 'controller_version_integrity', 'claim_id': identity})
        if execution.get('supplemental_leads_snapshot'):
            binding = execution['supplemental_leads_snapshot']
            snapshot = BASE/binding['path']
            if not snapshot.is_file() or sha(snapshot) != binding['sha256']:
                blockers.append({'kind': 'supplemental_leads_integrity', 'claim_id': identity})
        if execution.get('original_report_context_snapshot'):
            binding = execution['original_report_context_snapshot']
            context_snapshot = BASE/binding['path']
            original_report = BASE/binding['report_path']
            if (not context_snapshot.is_file() or sha(context_snapshot) != binding['sha256'] or
                    not original_report.is_file() or sha(original_report) != binding['report_sha256']):
                blockers.append({'kind': 'original_report_context_integrity', 'claim_id': identity})
        for kind in ('prompt', 'output'):
            artifact = BASE / execution[f'{kind}_path']
            expected_hash = execution['prompt_sha256'] if kind == 'prompt' else row['output_sha256']
            if not artifact.is_file() or sha(artifact) != expected_hash:
                blockers.append({'kind': f'{kind}_integrity', 'claim_id': identity})
        selection = execution['runtime_selection']
        if (not selection['verified'] or not selection['public_turn_configuration'] or
            any(turn != {'model': 'gpt-6-sol', 'effort': execution['requested_effort']}
                for turn in selection['public_turn_configuration'])):
            blockers.append({'kind': 'runtime_selection', 'claim_id': identity})
        for capture in row['source_captures']:
            if capture.get('status') != 'captured':
                continue
            for kind in ('raw', 'text'):
                artifact = Path(capture[f'{kind}_path'])
                if not artifact.is_file() or sha(artifact) != capture[f'{kind}_sha256']:
                    blockers.append({'kind': 'source_integrity', 'claim_id': identity, 'url': capture['url']})
        semantic_review = primary.get(identity, {})
        if (semantic_review.get('status') == 'REVIEW_REQUIRED' and
                semantic_review.get('output_sha256') == row['output_sha256']):
            blockers.append({'kind': 'primary_semantic_review_required', 'claim_id': identity,
                             'reason': semantic_review.get('review_basis')})
        if row['verdict'] == 'PENDING_PROOF_REVIEW':
            blockers.append({'kind': 'proof_hold', 'claim_id': identity, 'reasons': row['acceptance_hold_reasons']})
        if row['verdict'] != 'ACCEPTED':
            continue
        captures = {capture['url']: capture for capture in row['source_captures']}
        reasons, _ = controller.acceptance_problems(row['adjudication'], selection,
                           lambda url: captures.get(url, {'url': url, 'status': 'uncaptured'}))
        if reasons:
            blockers.append({'kind': 'independent_acceptance_gate', 'claim_id': identity, 'reasons': reasons})
            continue
        audit = primary.get(identity)
        if not audit or audit['status'] != 'PASS' or audit['output_sha256'] != row['output_sha256']:
            blockers.append({'kind': 'primary_source_review_pending', 'claim_id': identity})
            continue
        if audit.get('original_report_context_snapshot'):
            binding = audit['original_report_context_snapshot']
            artifact = BASE/binding['path']
            original_report = BASE/binding['report_path']
            if (not artifact.is_file() or sha(artifact) != binding['sha256'] or
                    not original_report.is_file() or sha(original_report) != binding['report_sha256']):
                blockers.append({'kind': 'primary_report_context_integrity', 'claim_id': identity})
                continue
        published.append({'claim_id': identity, 'cohort': row['cohort'], 'claim': row['original_claim'],
                          'verdict': 'ACCEPTED', 'adjudication': row['adjudication'],
                          'source_captures': row['source_captures'], 'execution': row['execution'],
                          'output_sha256': row['output_sha256'], 'primary_source_review': audit})
    quality_path = ROOT / 'validation/ledger-quality.json'
    quality = json.loads(quality_path.read_text()) if quality_path.exists() else {}
    if not quality.get('ready_for_final_candidate_queue'):
        blockers.append({'kind': 'candidate_quality_gate_pending'})
    if len(candidate) != 1283:
        blockers.append({'kind': 'candidate_count', 'actual': len(candidate)})
    integrity_path = ROOT / 'validation/protected-integrity.json'
    integrity = json.loads(integrity_path.read_text()) if integrity_path.exists() else None
    if not integrity or integrity['mismatches']:
        blockers.append({'kind': 'protected_integrity_pending_or_failed'})
    proposals = []
    for seq, row in sorted(candidate.items()):
        if row.get('revised_claim'):
            proposals.append({'claim_id': row['claim']['claim_id'], 'queue_sequence': seq,
                              'stage': 'luna_proposal', 'original_verdict': row['verdict'],
                              'proposed_text': row['revised_claim'], 'evidence_manifest': row['evidence_manifest'],
                              'final_ACCEPTED': False, 'corpus_modified': False})
    for row in final.values():
        adjudication = row['adjudication']
        if row['verdict'] != 'ACCEPTED' and adjudication.get('revised_claim'):
            proposals.append({'claim_id': row['claim_id'], 'stage': 'sol_proposal',
                              'original_verdict': row['verdict'], 'proposed_text': adjudication['revised_claim'],
                              'model_reports_rewrite_supported': adjudication['revised_claim_supported'],
                              'atomic_claims': adjudication['atomic_claims'], 'source_captures': row['source_captures'],
                              'final_ACCEPTED': False, 'corpus_modified': False})
    for name, rows in [('accepted-original-claims.jsonl', published), ('revised-claim-proposals.jsonl', proposals)]:
        (DELIVERY / name).write_text(''.join(json.dumps(row, ensure_ascii=False) + '\n' for row in rows))
    accepted_ids = {row['claim_id'] for row in published}
    consolidated = {}
    for row in candidate.values():
        identity = row['claim']['claim_id']
        consolidated[identity] = {'claim_id': identity, 'claim': row['claim'], 'stage': 'luna_reverification',
                                 'verdict': row['verdict'], 'final_ACCEPTED': False,
                                 'candidate_result_id': row['rerun_id'], 'evidence_manifest': row['evidence_manifest'],
                                 'requires_final_adjudication': row['verdict'] == 'CANDIDATE_ACCEPTED'}
    for item in read_rows(FINAL / 'original-queue.jsonl'):
        consolidated[item['claim_id']] = {'claim_id': item['claim_id'], 'claim': item,
             'stage': 'original_author_acceptance_awaiting_final_review',
             'verdict': 'PENDING_FINAL_ADJUDICATION', 'final_ACCEPTED': False, 'requires_final_adjudication': True}
    for identity, row in final.items():
        verdict = row['verdict']
        if verdict == 'ACCEPTED' and identity not in accepted_ids:
            verdict = 'ACCEPTED_PENDING_PRIMARY_REVIEW'
        audit = primary.get(identity, {})
        if audit.get('status') == 'REVIEW_REQUIRED' and audit.get('output_sha256') == row['output_sha256']:
            verdict = 'PENDING_SEMANTIC_REVIEW'
        consolidated[identity] = {'claim_id': identity, 'claim': row['original_claim'],
             'stage': 'strong_adjudication', 'verdict': verdict, 'final_ACCEPTED': identity in accepted_ids,
             'output_sha256': row['output_sha256'], 'adjudication_ledger': str((FINAL/'results.jsonl').relative_to(BASE)),
             'requires_final_adjudication': verdict in {'PENDING_PROOF_REVIEW', 'ACCEPTED_PENDING_PRIMARY_REVIEW', 'PENDING_SEMANTIC_REVIEW'}}
    (DELIVERY / 'consolidated-status.jsonl').write_text(''.join(
        json.dumps(row, ensure_ascii=False) + '\n' for _, row in sorted(consolidated.items())))
    if len(consolidated) != 1394:
        blockers.append({'kind': 'consolidated_scope_count', 'actual': len(consolidated)})
    summary = {'generated_at': datetime.now(timezone.utc).isoformat(), 'complete': not blockers,
               'candidate_rerun': {'requested': 1283, 'effective': len(candidate),
                  'verdicts': dict(Counter(row['verdict'] for row in candidate.values())),
                  'verified_execution_bindings': quality.get('execution_bindings_verified'),
                  'metadata_corrections': quality.get('metadata_correction_rows'),
                  'supplemental_research': quality.get('superseding_research_rows')},
               'strong_adjudication': cohorts, 'accepted_model_and_capture_gate': sum(row['verdict'] == 'ACCEPTED' for row in final.values()),
               'accepted_with_primary_source_review': len(published), 'rewrite_proposals': len(proposals),
               'consolidated_scope': len(consolidated),
               'outside_requested_scope': {'UNSUPPORTED': 2, 'SOURCE_UNAVAILABLE': 3},
               'protected_integrity': integrity, 'blocking_issue_count': len(blockers),
               'reports_and_author_ledgers_modified': False,
               'notes': ['Counts use latest append-only result per identity.',
                         'UNKNOWN and PARTIAL are successful research outcomes.',
                         'Supported rewrites remain proposals, never final acceptance of the original.']}
    dump(DELIVERY / 'summary.json', summary)
    dump(DELIVERY / 'remaining-issues.json', blockers)
    print(json.dumps({key: summary[key] for key in (
        'generated_at', 'complete', 'candidate_rerun', 'strong_adjudication',
        'accepted_with_primary_source_review', 'blocking_issue_count')}, ensure_ascii=False))


if __name__ == '__main__':
    main()
