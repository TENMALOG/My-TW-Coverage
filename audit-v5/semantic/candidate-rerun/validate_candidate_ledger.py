#!/usr/bin/env python3
"""Audit effective coverage and execution bindings; never assert semantic truth."""
import argparse
from collections import Counter
import hashlib
import importlib.util
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('candidate_validation_runner', HERE/'run_hermes_batch.py')
runner = importlib.util.module_from_spec(spec); spec.loader.exec_module(runner)


def inspect():
    queued = runner.read_queue(); queue = {q['queue_sequence']: q for q in queued}
    rows = runner.read_result_rows(queued); effective = runner.effective_result_projection(rows)
    problems = []; provenance_pending = []; citation_gaps = []; verified = []
    statuses = Counter(); counts = Counter(r['verdict'] for r in effective)
    if {r['queue_sequence'] for r in effective} != set(queue):
        problems.append('Effective sequence coverage differs from frozen queue')
    for row in effective:
        seq = row['queue_sequence']; item = queue[seq]
        mp = runner.BASE/row['evidence_manifest']; np = runner.BASE/row['inspection_notes']
        if not mp.is_file() or not np.is_file():
            problems.append({'sequence':seq,'error':'Manifest or notes missing'}); continue
        manifest = json.loads(mp.read_text()); sources = {s['source_id']:s for s in manifest.get('sources',[])}
        if manifest.get('claim_id') != item['claim_id'] or manifest.get('normalized_claim_hash') != item['normalized_claim_hash']:
            problems.append({'sequence':seq,'error':'Manifest claim identity mismatch'})
        for number, atom in enumerate(row.get('atomic_claims',[]),1):
            statuses[atom['status']] += 1
            if atom['status'] not in {'SUPPORTED','UNKNOWN','CONTRADICTED'}:
                problems.append({'sequence':seq,'error':'Invalid atom status'})
            refs = atom.get('evidence_ids',[])
            if atom['status']=='SUPPORTED' and not refs:
                problems.append({'sequence':seq,'atom':number,'error':'Supported atom has no evidence'})
            for ref in refs:
                if ref not in sources:
                    problems.append({'sequence':seq,'atom':number,'error':'Unknown citation ID'}); continue
                src=sources[ref]
                if not src.get('url') or not src.get('title') or not src.get('locator'):
                    citation_gaps.append({'sequence':seq,'atom':number,'source_id':ref,'error':'URL/title/locator incomplete'})
        raw_ref=manifest.get('hermes_raw_output'); raw_hash=manifest.get('hermes_raw_output_sha256')
        prompt_ref=manifest.get('prompt_path'); prompt_hash=manifest.get('prompt_sha256')
        if not all((raw_ref,raw_hash,prompt_ref,prompt_hash)):
            provenance_pending.append({'sequence':seq,'reason':'Missing hash-bound stdout/prompt'});continue
        try:
            raw=(runner.BASE/raw_ref).read_bytes(); prompt=(runner.BASE/prompt_ref).read_bytes()
            if hashlib.sha256(raw).hexdigest()!=raw_hash or hashlib.sha256(prompt).hexdigest()!=prompt_hash:
                raise ValueError('Captured execution hash mismatch')
            prompt_item=json.loads(prompt.decode().split('Isolated queue item:\n',1)[1])
            if prompt_item != item: raise ValueError('Prompt does not match frozen claim')
            payload=runner.parse_response(raw.decode('utf-8',errors='replace'))
            raw_atoms=payload['atomic_claims']
            if len(raw_atoms)!=len(row['atomic_claims']):raise ValueError('Atom count differs from captured response')
            for atom, raw_atom in zip(row['atomic_claims'], raw_atoms):
                expected_status=str(raw_atom.get('status','UNKNOWN')).upper()
                if expected_status=='ACCEPTED':expected_status='SUPPORTED'
                expected=runner.normalize_sources(raw_atom.get('sources'),raw_atom,item)
                if (atom['text']!=str(raw_atom['text']) or atom['status']!=expected_status or
                        atom.get('period')!=raw_atom.get('period') or atom.get('note')!=raw_atom.get('note') or
                        atom['evidence_ids'] != [s['source_id'] for s in expected] or
                        any(sources.get(s['source_id'])!=s for s in expected)):
                    raise ValueError('Atom or citation metadata differs from captured response')
            verified.append(seq)
        except (OSError,ValueError,KeyError,TypeError,IndexError) as exc:
            provenance_pending.append({'sequence':seq,'reason':str(exc)})
    cp=json.loads(runner.CHECKPOINT_PATH.read_text())
    if cp['processed']!=len(effective) or cp['verdict_counts']!=dict(counts) or sum(cp['verdict_counts'].values())!=len(effective):
        problems.append('Checkpoint counts differ from effective unique projection')
    if hashlib.sha256(runner.QUEUE_PATH.read_bytes()).hexdigest()!=cp['queue_sha256']:
        problems.append('Frozen queue hash mismatch')
    return {'schema':'candidate-ledger-quality-check-1','checked_at':runner.now_utc(),
            'queue_count':len(queue),'physical_rows':len(rows),'effective_rows':len(effective),'verdict_counts':dict(counts),
            'metadata_correction_rows':sum(bool(r.get('metadata_only')) for r in rows),
            'superseding_research_rows':sum(not r.get('metadata_only') and runner.batch_num(r['rerun_batch_id'])>=10 for r in rows),
            'atom_counts':dict(statuses),'execution_bindings_verified':len(verified),'provenance_pending':provenance_pending,
            'structural_blockers':problems,'citation_metadata_gaps':citation_gaps,
            'final_ACCEPTED_in_candidate_ledger':sum(r['verdict']=='ACCEPTED' for r in effective),
            'semantic_truth_certified_by_this_program':False,
            'semantic_review_policy':'Full original qualifiers are independently reviewed by Sol; partial rewrites remain proposals.',
            'ready_for_final_candidate_queue':not problems and not provenance_pending}


if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--output',default=str(HERE/'validation/ledger-quality.json'));args=ap.parse_args()
    report=inspect();runner.atomic_write_json(Path(args.output),report)
    print(json.dumps({k:v for k,v in report.items() if k not in ('provenance_pending','citation_metadata_gaps','structural_blockers')},ensure_ascii=False))
    print(json.dumps({'structural_blockers':len(report['structural_blockers']),'provenance_pending':len(report['provenance_pending']),
                      'citation_metadata_gaps':len(report['citation_metadata_gaps'])}))
