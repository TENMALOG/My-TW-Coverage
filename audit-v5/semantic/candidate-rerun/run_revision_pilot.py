#!/usr/bin/env python3
"""Independently judge proposed text; never change acceptance of its parent."""
import argparse
import fcntl
import json
import re
import signal
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import run_final_adjudication as worker

ROOT = Path(__file__).resolve().parent / 'revision-pilot-001'
SELF = Path(__file__).read_bytes()
SELF_HASH = worker.digest(SELF)
SELF_ARCHIVE = worker.CACHE / 'revision-controllers' / (SELF_HASH+'.py')
ORIGINAL_CONTROLLER_BYTES = worker.CONTROLLER_BYTES
ORIGINAL_CONTROLLER_SHA = worker.CONTROLLER_SHA256
ORIGINAL_ROOT = worker.ROOT


def placement_context(item):
    original = item['parent_report_context']
    path = worker.BASE / original['resolved_report_path']
    if worker.digest(path.read_bytes()) != original['report_sha256']:
        raise ValueError('Parent report changed after pilot freeze')
    return {'requested_report_path': original['requested_report_path'], 'resolved_report_path': original['resolved_report_path'],
        'report_sha256': original['report_sha256'], 'occurrences': [{'line': None,
            'headings': [{'level': 1, 'text': item['issuer_ticker']+' '+item['issuer_company']},
                         {'level': 2, 'text': item['proposed_target_section']}],
            'containing_line': item['original_text'], 'placement': 'proposed draft, not currently in parent report'}],
        'parent_occurrences': original['occurrences'], 'purpose': 'Evaluate the proposed text in its planned neutral section. Parent text is lineage only, not evidence and not the text to approve.'}


def configure(effort):
    worker.EFFORT = effort
    worker.ROOT = ROOT / 'adjudication'
    worker.ROOT.mkdir(parents=True, exist_ok=True)
    worker.report_context = placement_context
    contract = worker.CONTRACT.replace('ORIGINAL', 'PROPOSED').replace('original', 'proposed')
    worker.CONTRACT = contract + """
This is a NEW revision claim, linked to an unchanged parent claim. Judge only the complete proposed wording in original_text. The legacy JSON field complete_original_supported means complete proposed wording supported for this revision execution. ACCEPTED is only a model vote for this new text; external delivery requires the independent capture gate and primary source check, and is labelled REVISED_SUPPORTED. You have no authority to accept or modify the parent claim.
The placement context has a neutral 業務與歷史資料 section. Parent occurrences show where the old wording came from; they do not impose a current main-customer or main-supplier label on this dated revision. Evaluate the new text's own qualifiers, attribution, scope and dates exactly. A dated disclosure may support an explicitly dated statement; do not quietly add current validity. Verify that the report filename company and ticker match the intended issuer, including subsidiaries and customer entities. A ratio of cost to another denominator must not be renamed as market share. Preserve reported forecasts and plans as forecasts/plans, not delivered or completed events. New information after 2026-10-08 must not establish facts as of that assessment date unless it directly documents an earlier historical event within that scope.
The supplied sources are discovery leads only. Prior judgments and atom statuses are withheld. Do not use unavailable evidence, search snippets, or model notes as proof. If the proposed wording still overstates evidence, reject that wording and give a narrower alternative in revised_claim. Do not accept your alternative in this same execution. Source-bound attributed sentences must prove both the actual source attribution and the underlying date/period and entity; quoted issuer rankings can remain attributed, not converted to independent objective rankings.
"""


def save(row, queue):
    row['review_type'] = 'proposed_revision'
    row['parent_claim_id'] = row['original_claim']['parent_claim_id']
    row['parent_original_acceptance_changed'] = False
    row['execution']['revision_controller_snapshot'] = {'path': str(SELF_ARCHIVE.relative_to(worker.BASE)), 'sha256': SELF_HASH}
    if row['verdict'] == 'ACCEPTED':
        row['verdict'] = 'CANDIDATE_REVISED_SUPPORTED'
    with worker.WRITE_LOCK, (worker.ROOT/'persist.lock').open('a+') as lock:
        fcntl.flock(lock.fileno(), fcntl.LOCK_EX)
        p = worker.ROOT/'results.jsonl'
        with p.open('a') as f:
            f.write(json.dumps(row, ensure_ascii=False, separators=(',', ':'))+'\n')
            f.flush()
        latest = {x['claim_id']: x for x in map(json.loads, p.read_text().splitlines())}
        worker.write_json(ROOT/'checkpoint.json', {'updated_at': worker.now(), 'queue_count': len(queue),
            'processed': len(latest), 'remaining': sum(x['claim_id'] not in latest for x in queue),
            'verdict_counts': {v: sum(x['verdict']==v for x in latest.values()) for v in sorted({x['verdict'] for x in latest.values()})},
            'model': worker.MODEL, 'effort': worker.EFFORT})


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--workers', type=int, default=3)
    ap.add_argument('--budget', type=int, default=900)
    ap.add_argument('--effort', choices=['high', 'max'], default='high')
    ap.add_argument('--recheck-claim-id')
    ap.add_argument('--limit', type=int)
    args = ap.parse_args()
    if not 1 <= args.workers <= 3 or args.budget <= 0:
        ap.error('Invalid worker count or budget')
    configure(args.effort)
    signal.signal(signal.SIGUSR1, lambda signum, frame: worker.request_stop('graceful_checkpoint'))
    lock = (worker.ROOT/'runner.lock').open('a+')
    fcntl.flock(lock.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
    original_lock = (ORIGINAL_ROOT/'runner.lock').open('a+')
    fcntl.flock(original_lock.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
    queue = [json.loads(x) for x in (ROOT/'queue.jsonl').read_text().splitlines()]
    manifest = json.loads((ROOT/'queue.manifest.json').read_text())
    if manifest['count'] != 30 or worker.digest((ROOT/'queue.jsonl').read_bytes()) != manifest['sha256']:
        raise ValueError('Frozen revision queue integrity failure')
    worker.CONTROLLER_VERSION_PATH.parent.mkdir(parents=True, exist_ok=True)
    if worker.CONTROLLER_VERSION_PATH.exists() and worker.digest(worker.CONTROLLER_VERSION_PATH.read_bytes()) != ORIGINAL_CONTROLLER_SHA:
        raise ValueError('Shared controller archive changed')
    worker.CONTROLLER_VERSION_PATH.write_bytes(ORIGINAL_CONTROLLER_BYTES)
    SELF_ARCHIVE.parent.mkdir(parents=True, exist_ok=True)
    if SELF_ARCHIVE.exists() and SELF_ARCHIVE.read_bytes() != SELF:
        raise ValueError('Revision controller archive changed')
    SELF_ARCHIVE.write_bytes(SELF)
    path = worker.ROOT/'results.jsonl'
    latest = {x['claim_id']: x for x in map(json.loads, path.read_text().splitlines())} if path.exists() else {}
    pending = [x for x in queue if x['claim_id'] not in latest]
    if args.recheck_claim_id:
        pending = [x for x in queue if x['claim_id']==args.recheck_claim_id]
        if len(pending)!=1:
            raise ValueError('Revision ID not unique in frozen pilot')
    if args.limit:
        pending = pending[:args.limit]
    print('Independent Sol '+args.effort.title()+' revision pilot: pending='+str(len(pending))+', workers='+str(args.workers), flush=True)
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {pool.submit(worker.review, x, args.budget): x for x in pending}
        for future in as_completed(futures):
            item = futures[future]
            try:
                row = future.result()
                if row is None:
                    continue
                if row.get('status') == 'OPERATIONAL_FAILURE':
                    with (worker.ROOT/'operational-failures.jsonl').open('a') as f:
                        f.write(json.dumps(row, ensure_ascii=False)+'\n')
                    print('OPERATIONAL_FAILURE '+item['claim_id'], flush=True)
                else:
                    save(row, queue)
                    print(row['verdict']+' '+item['claim_id']+' '+item['issuer_company'], flush=True)
            except Exception as exc:
                with (worker.ROOT/'operational-failures.jsonl').open('a') as f:
                    f.write(json.dumps({'claim_id': item['claim_id'], 'at': worker.now(), 'error': type(exc).__name__+': '+str(exc)[:350]}, ensure_ascii=False)+'\n')
                print('OPERATIONAL_FAILURE '+item['claim_id']+' '+type(exc).__name__, flush=True)
    print('Revision pilot run finished; stop_reason='+str(worker.STOP_REASON), flush=True)


if __name__ == '__main__':
    main()
