#!/usr/bin/env python3
"""Bind historical results to matching saved worker payloads without new research."""
from __future__ import annotations
import argparse
import copy
import fcntl
import hashlib
import importlib.util
import json
from pathlib import Path
import re

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('candidate_runner', HERE / 'run_hermes_batch.py')
runner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(runner)
BASE = runner.BASE
BACKUP = runner.CACHE / 'operational-repair/20261008-finalization/originals/audit-v5/semantic/candidate-rerun/run_hermes_batch.py'
old_spec = importlib.util.spec_from_file_location('historical_candidate_runner', BACKUP)
historical = importlib.util.module_from_spec(old_spec)
old_spec.loader.exec_module(historical)
BATCH = 'rerun-009'


def projection(payload, item):
    atoms = []
    for atom in payload.get('atomic_claims', []):
        status = str(atom.get('status', 'UNKNOWN')).upper()
        if status == 'ACCEPTED':
            status = 'SUPPORTED'
        sources = historical.normalize_sources(atom.get('sources'), atom, item)
        atoms.append({'text': str(atom['text']), 'status': status, 'period': atom.get('period'),
                      'evidence_ids': [s['source_id'] for s in sources], 'note': atom.get('note')})
    overall = str(payload.get('overall', 'UNKNOWN')).upper()
    overall = {'ACCEPTED': 'CANDIDATE_ACCEPTED', 'SUPPORTED': 'CANDIDATE_ACCEPTED',
               'PARTIALLY_SUPPORTED': 'PARTIAL'}.get(overall, overall)
    if payload.get('candidate_accepted') or payload.get('requires_final_adjudication'):
        overall = 'CANDIDATE_ACCEPTED'
    if overall == 'CANDIDATE_ACCEPTED' and not all(
            a['status'] == 'SUPPORTED' and a['evidence_ids'] for a in atoms):
        overall = 'PARTIAL' if any(a['status'] == 'SUPPORTED' for a in atoms) else 'UNKNOWN'
    return {'atomic_claims': atoms, 'verdict': overall,
            'revised_claim': str(payload.get('revised_claim') or '').strip() or None,
            'research_exhausted': bool(payload.get('research_exhausted', False)),
            'research_stop_reason': payload.get('research_stop_reason')}


def locate(row, item):
    directory = runner.CACHE / item['issuer_ticker'] / str(item['queue_sequence'])
    matches = []
    errors = []
    for path in sorted(directory.glob('**/hermes-attempt-*.stdout.txt')):
        if path.is_symlink() or not path.is_file():
            continue
        try:
            raw = path.read_bytes()
            payload = historical.parse_response(raw.decode('utf-8', errors='replace'))
            expected = projection(payload, item)
            if any(row.get(key) != value for key, value in expected.items()):
                continue
            prompt = path.parent / 'isolated-prompt.txt'
            prompt_raw = prompt.read_bytes()
            prompt_item = json.loads(prompt_raw.decode('utf-8').split('Isolated queue item:\n', 1)[1])
            if prompt_item != item:
                continue
            matches.append((path, raw, payload, prompt, prompt_raw))
        except (OSError, ValueError, KeyError, TypeError, IndexError) as exc:
            errors.append(type(exc).__name__)
    hashes = {runner.sha_bytes(m[1]) for m in matches}
    if len(hashes) != 1:
        return None, 'no exactly matching payload/prompt' if not hashes else 'multiple distinct matching stdout artifacts'
    # Prefer the recorded execution batch's directory when duplicate identical
    # artifacts exist. No semantic content is reconstructed from a model label.
    matches.sort(key=lambda m: (m[0].parent.name != row['rerun_batch_id'], str(m[0])))
    return matches[0], None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--apply', action='store_true')
    args = ap.parse_args()
    queue = {item['queue_sequence']: item for item in runner.read_queue()}
    physical = runner.read_result_rows()
    original = {r['queue_sequence']: r for r in physical
                if runner.batch_num(r['rerun_batch_id']) <= 8}
    existing_ids = {r['rerun_id'] for r in physical}
    plan = []; unresolved = []; direct = []
    for seq, row in sorted(original.items()):
        if not row.get('model_identifier', '').startswith('Hermes Agent'):
            direct.append(seq)
            continue
        matched, reason = locate(row, queue[seq])
        if not matched:
            unresolved.append({'sequence': seq, 'reason': reason})
            continue
        path, raw, payload, prompt, prompt_raw = matched
        manifest_path = BASE / row['evidence_manifest']
        manifest = json.loads(manifest_path.read_text())
        entry = {'sequence': seq, 'original_result_id': row['rerun_id'],
                 'original_result_sha256': runner.sha_bytes(json.dumps(row, sort_keys=True, ensure_ascii=False).encode()),
                 'original_manifest_sha256': runner.sha_bytes(manifest_path.read_bytes()),
                 'matched_stdout': runner.relative_to_base(path), 'matched_stdout_sha256': runner.sha_bytes(raw),
                 'matched_prompt': runner.relative_to_base(prompt), 'matched_prompt_sha256': runner.sha_bytes(prompt_raw),
                 'old_stdout_binding': manifest.get('hermes_raw_output'),
                 'binding_changed': manifest.get('hermes_raw_output') != runner.relative_to_base(path),
                 'new_result_id': f'{BATCH}-{seq:06d}'}
        plan.append(entry)
    report = {'schema': 'candidate-provenance-repair-1', 'at': runner.now_utc(),
              'new_research': False, 'matching_results': len(plan), 'old_path_mismatches': sum(x['binding_changed'] for x in plan),
              'direct_model_records_needing_execution_reconstruction': direct,
              'unresolved': unresolved, 'corrections': plan, 'applied_this_run': 0}
    out = HERE / 'validation/provenance-repair-report.json'
    if args.apply:
        max_batch = max(runner.batch_num(r['rerun_batch_id']) for r in physical)
        if max_batch > 9:
            raise SystemExit('A later research pass exists; refusing to supersede it with historical metadata.')
        lock = (HERE / 'runtime/runner.lock').open('a+')
        fcntl.flock(lock.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        for entry in plan:
            if entry['new_result_id'] in existing_ids:
                continue
            seq = entry['sequence']; old = original[seq]; item = queue[seq]
            matched, reason = locate(old, item)
            if not matched:
                raise ValueError(f'Artifact changed after planning for {seq}: {reason}')
            path, raw, payload, prompt, prompt_raw = matched
            if runner.sha_bytes(raw) != entry['matched_stdout_sha256'] or runner.sha_bytes(prompt_raw) != entry['matched_prompt_sha256']:
                raise ValueError('Artifact hash changed after planning')
            row = copy.deepcopy(old); new_id = entry['new_result_id']
            row.update({'rerun_id': new_id, 'rerun_batch_id': BATCH,
                        'metadata_only': True, 'supersedes_result_id': old['rerun_id'],
                        'corrected_at': runner.now_utc(), 'correction_reason': 'Recovered exact stdout/prompt and atom-level citation metadata; semantic verdict unchanged.'})
            sources = {}
            for atom, raw_atom in zip(row['atomic_claims'], payload['atomic_claims']):
                restored = runner.normalize_sources(raw_atom.get('sources'), raw_atom, item)
                atom['evidence_ids'] = [s['source_id'] for s in restored]
                sources.update({s['source_id']: s for s in restored})
            execution = {'execution_batch_id': old['rerun_batch_id'],
                         'successful_attempt': int(re.search(r'attempt-(\d+)', path.name).group(1)),
                         'hermes_raw_output': entry['matched_stdout'], 'hermes_raw_output_sha256': entry['matched_stdout_sha256'],
                         'prompt_path': entry['matched_prompt'], 'prompt_sha256': entry['matched_prompt_sha256'],
                         'requested_model': 'gpt-6-luna', 'requested_reasoning': 'xhigh',
                         'observed_model': None, 'resolved_model': None,
                         'binding_basis': 'Exact historical payload projection and frozen queue prompt match',
                         'request_settings_recovered_from_command': False}
            row.update(execution)
            evidence_dir, mp, np = runner.evidence_output_paths(new_id)
            if mp.exists() or np.exists():
                raise ValueError(f'Uncommitted evidence already exists for {new_id}; inspect before resume')
            manifest = json.loads((BASE / old['evidence_manifest']).read_text())
            manifest.update({'rerun_id': new_id, 'sources': list(sources.values()), **execution,
                             'metadata_only': True, 'supersedes_manifest': old['evidence_manifest'],
                             'supersedes_manifest_sha256': entry['original_manifest_sha256'],
                             'corrected_at': row['corrected_at']})
            notes = (BASE / old['inspection_notes']).read_text()
            notes += '\n\n追溯補正：僅復原與原結果完全吻合的 stdout、prompt 及各原子句來源定位。此補正未重新研究，原語意結論及原研究日期保持不變。\n'
            runner.safe_write_bytes(mp, (json.dumps(manifest, ensure_ascii=False, indent=2)+'\n').encode(), HERE/'evidence', 'Corrected manifest')
            runner.safe_write_bytes(np, notes.encode(), HERE/'evidence', 'Corrected notes')
            row['evidence_manifest'] = runner.relative_to_base(mp)
            row['inspection_notes'] = runner.relative_to_base(np)
            if runner.persist_result(row, allow_superseding=True):
                report['applied_this_run'] += 1
            existing_ids.add(new_id)
        lock.close()
    runner.atomic_write_json(out, report)
    print(json.dumps({k:v for k,v in report.items() if k not in ('corrections', 'direct_model_records_needing_execution_reconstruction')}, ensure_ascii=False))


if __name__ == '__main__':
    main()
