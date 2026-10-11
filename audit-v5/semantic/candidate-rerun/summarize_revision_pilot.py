#!/usr/bin/env python3
"""Validate isolated revision records and deliver only source-reviewed new text."""
import hashlib
import json
from collections import Counter
from pathlib import Path
import run_final_adjudication as controller

ROOT = Path(__file__).resolve().parent/'revision-pilot-001'


def read(path):
    return [json.loads(x) for x in path.read_text().splitlines() if x.strip()] if path.exists() else []


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    queue = read(ROOT/'queue.jsonl'); manifest = json.loads((ROOT/'queue.manifest.json').read_text())
    if sha(ROOT/'queue.jsonl') != manifest['sha256'] or len(queue) != 30:
        raise ValueError('Frozen pilot queue mismatch')
    latest = {r['claim_id']: r for r in read(ROOT/'adjudication/results.jsonl')}
    primary = {r['claim_id']: r for r in read(ROOT/'adjudication/primary-source-review.jsonl')}
    issues = []; accepted = []; outcomes = []
    for filename, expected in manifest['inputs'].items():
        p = ROOT.parent/'delivery'/filename
        if sha(p) != expected:
            issues.append({'kind': 'parent_delivery_changed', 'file': filename})
    parent_accepted = ROOT.parent/'delivery/accepted-original-claims.jsonl'
    if sha(parent_accepted) != '2a8ae93d1ff113c0a0413461a6094b0b5ec35c2674914a201cd30cef806501db':
        issues.append({'kind': 'parent_original_acceptance_changed', 'file': str(parent_accepted)})
    for item in queue:
        cid = item['claim_id']; row = latest.get(cid)
        if not row:
            issues.append({'kind': 'missing_independent_review', 'claim_id': cid})
            outcomes.append({'claim_id': cid, 'parent_claim_id': item['parent_claim_id'], 'category': item['pilot_category'], 'verdict': 'PENDING', 'text': item['original_text']})
            continue
        local = []
        if row['original_claim'] != item or row.get('parent_original_acceptance_changed') is not False:
            local.append('Revision or parent identity differs from frozen queue')
        e = row['execution']
        for ref, h in [('prompt_path', 'prompt_sha256'), ('output_path', None), ('controller_version_path', 'controller_sha256')]:
            p = controller.BASE/e[ref]
            expected = row['output_sha256'] if h is None else e[h]
            if not p.is_file() or sha(p) != expected:
                local.append('Immutable execution artifact changed: '+ref)
        output = controller.BASE/e['output_path']
        if output.exists() and json.loads(output.read_text()) != row['adjudication']:
            local.append('Record differs from actual independent model output')
        repair = row.get('proof_capture_repair')
        if repair:
            for path_key, hash_key in [('parent_row_path', 'parent_row_sha256'), ('repair_code_path', 'repair_code_sha256')]:
                p = controller.BASE/repair[path_key]
                if not p.is_file() or sha(p)!=repair[hash_key]:
                    local.append('Capture repair binding changed: '+path_key)
            parent_path = controller.BASE/repair['parent_row_path']
            if parent_path.is_file():
                parent = json.loads(parent_path.read_text())
                if (parent['output_sha256'] != row['output_sha256'] or parent['execution'] != row['execution']
                        or parent['adjudication'] != row['adjudication'] or parent['original_claim'] != row['original_claim']
                        or repair['model_output_unchanged'] is not True or repair['new_model_execution'] is not False):
                    local.append('Capture repair changed independently judged text or execution')
        for field in ['claim_output_schema_snapshot', 'original_report_context_snapshot', 'revision_controller_snapshot']:
            binding = e[field]; p = controller.BASE/binding['path']
            if not p.is_file() or sha(p) != binding['sha256']:
                local.append('Execution snapshot changed: '+field)
        schema = json.loads((controller.BASE/e['claim_output_schema_snapshot']['path']).read_text())
        if any(schema['properties'][k].get('enum') != [item[k]] for k in ['claim_id', 'normalized_claim_hash']):
            local.append('Per-claim schema identity mismatch')
        report = controller.BASE/item['parent_report_context']['resolved_report_path']
        if sha(report) != item['parent_report_context']['report_sha256']:
            local.append('Parent report bytes changed')
        caps = {c['url']: c for c in row['source_captures']}
        for c in caps.values():
            if c.get('status') == 'captured':
                kinds = ['raw', 'text']
                if c.get('kind') == 'pdf_page_ocr':
                    kinds += ['image', 'observations', 'ocr_code', 'assembly_code']
                    if (c.get('capture_method') != 'macOS.Vision_VNRecognizeTextRequest' or
                            c.get('partial_document') is not True):
                        local.append('Invalid supplemental PDF OCR identity')
                for kind in kinds:
                    p = Path(c[kind+'_path'])
                    if not p.is_file() or sha(p) != c[kind+'_sha256']:
                        local.append('Captured source bytes changed: '+c['url'])
        reasons, _ = controller.acceptance_problems(row['adjudication'], e['runtime_selection'], capture_source=lambda url: caps.get(url, {'url': url, 'status': 'missing'}))
        local.extend(reasons)
        review = primary.get(cid)
        if review and review.get('source_image'):
            b = review['source_image']; p = controller.BASE/b['path']
            if not p.is_file() or sha(p)!=b['sha256']:
                local.append('Primary source image snapshot changed')
        if review and review['output_sha256'] == row['output_sha256'] and review['status']=='REVIEW_REQUIRED':
            local.append('Primary semantic review requires a fresh judgment: '+review['review_basis'])
        if row['model_verdict']=='ACCEPTED':
            if not review or review['output_sha256'] != row['output_sha256'] or review['status'] != 'PASS':
                local.append('Primary source review pending')
            elif 'context_snapshot' not in review:
                local.append('Primary placement review is not hash-bound')
            else:
                binding = review['context_snapshot']; p = controller.BASE/binding['path']
                if not p.is_file() or sha(p)!=binding['sha256']:
                    local.append('Primary placement review snapshot changed')
                if binding != e['original_report_context_snapshot']:
                    local.append('Primary placement differs from independently judged placement')
        if local:
            issues.append({'kind': 'revision_review_hold', 'claim_id': cid, 'reasons': sorted(set(local))})
        approved = row['model_verdict']=='ACCEPTED' and not local
        verdict = 'REVISED_SUPPORTED' if approved else 'PENDING_REVIEW' if local else row['verdict']
        outcomes.append({'claim_id': cid, 'parent_claim_id': item['parent_claim_id'], 'ticker': item['issuer_ticker'], 'company': item['issuer_company'],
            'category': item['pilot_category'], 'verdict': verdict, 'proposed_text': item['original_text'],
            'model_verdict': row['model_verdict'], 'output_sha256': row['output_sha256'],
            'rationale': row['adjudication']['rationale'], 'remaining_qualifiers': row['adjudication']['unresolved_qualifiers'],
            'alternative_text': row['adjudication']['revised_claim'], 'alternative_requires_new_review': bool(row['adjudication']['revised_claim']),
            'parent_original_acceptance_changed': False})
        if approved:
            accepted.append({'revision_id': cid, 'parent_claim_id': item['parent_claim_id'], 'verdict': 'REVISED_SUPPORTED',
                'text': item['original_text'], 'ticker': item['issuer_ticker'], 'company': item['issuer_company'],
                'target_section': item['proposed_target_section'], 'adjudication': row['adjudication'], 'source_captures': row['source_captures'],
                'execution': e, 'output_sha256': row['output_sha256'], 'primary_source_review': review,
                'parent_original_acceptance_changed': False, 'corpus_modified': False})
    d = ROOT/'delivery'; d.mkdir(exist_ok=True)
    for name, data in [('accepted-revisions.jsonl', accepted), ('pilot-outcomes.jsonl', outcomes)]:
        (d/name).write_text(''.join(json.dumps(x, ensure_ascii=False)+'\n' for x in data))
    summary = {'schema': 'revision-pilot-summary-1', 'generated_at': controller.now(), 'queue_count': 30,
        'reviewed': sum(x['claim_id'] in latest for x in queue), 'remaining_reviews': sum(x['claim_id'] not in latest for x in queue),
        'accepted_revisions': len(accepted), 'verdicts': dict(Counter(x['verdict'] for x in outcomes)),
        'blocking_issue_count': len(issues), 'adjudication_complete': not issues,
        'parent_original_ACCEPTED_count': len(read(parent_accepted)), 'parent_original_acceptance_changed': False,
        'assessment_date': manifest['assessment_date'], 'drafts_complete': False, 'complete': False}
    draft_path = d/'draft-manifest.json'
    draft_issues = []
    if draft_path.exists():
        draft = json.loads(draft_path.read_text())
        if draft['accepted_input_sha256'] != sha(d/'accepted-revisions.jsonl'):
            draft_issues.append('Drafts do not match the current accepted revision ledger')
        included = []
        for f in draft['files']:
            for field, expected in [('source_path', 'source_sha256'), ('draft_path', 'draft_sha256'), ('diff_path', 'diff_sha256')]:
                p = controller.BASE/f[field]
                if not p.is_file() or sha(p) != f[expected]:
                    draft_issues.append('Draft artifact changed: '+f[field])
            included.extend(f['revision_ids'])
            if f['financial_bytes_preserved'] is not True:
                draft_issues.append('Financial bytes changed: '+f['source_path'])
            from build_revision_drafts import financial
            source = controller.BASE/f['source_path']; copy = controller.BASE/f['draft_path']
            if source.is_file() and copy.is_file():
                if financial(source.read_bytes()) != financial(copy.read_bytes()):
                    draft_issues.append('Actual financial section bytes differ: '+f['source_path'])
                if controller.digest(financial(copy.read_bytes())) != f['financial_sha256']:
                    draft_issues.append('Financial section hash binding differs: '+f['source_path'])
        if sorted(included) != sorted(r['revision_id'] for r in accepted):
            draft_issues.append('Draft revision set differs from accepted revisions')
        draft_issues.extend(draft['issues'])
        summary['draft_count'] = draft['draft_count']
        summary['drafts_for_reviewed_revisions_complete'] = not draft_issues
        summary['drafts_complete'] = summary['adjudication_complete'] and not draft_issues
    else:
        draft_issues.append('Draft manifest not built')
    baseline_path = controller.BASE/'audit-v5/source-cache/candidate-rerun/operational-repair/20261008-finalization/baseline.json'
    baseline = json.loads(baseline_path.read_text())
    mismatches = [rel for rel, expected in baseline['protected_files'].items()
                  if not (controller.BASE/rel).is_file() or sha(controller.BASE/rel) != expected]
    summary['protected_integrity'] = {'checked_at': controller.now(), 'protected_count': len(baseline['protected_files']), 'mismatches': mismatches}
    if mismatches:
        issues.append({'kind': 'protected_file_changed', 'paths': mismatches})
    summary['draft_issues'] = draft_issues
    summary['blocking_issue_count'] = len(issues)+len(draft_issues)
    summary['complete'] = summary['adjudication_complete'] and summary['drafts_complete'] and not mismatches
    controller.write_json(d/'remaining-issues.json', issues); controller.write_json(d/'summary.json', summary)
    print(json.dumps(summary, ensure_ascii=False))


if __name__ == '__main__':
    main()
