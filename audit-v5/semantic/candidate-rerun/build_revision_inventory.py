#!/usr/bin/env python3
"""Freeze a provenance-bound revision inventory and a diverse 30-claim pilot."""
import hashlib
import json
import re
from collections import Counter
from pathlib import Path
import run_final_adjudication as source

ROOT = Path(__file__).resolve().parent / 'revision-pilot-001'
INPUT = source.ROOT.parent / 'delivery'

PILOT = {
    '排名': ['2208:objective_ranking_or_market_share:ccf06f0f4586432a', '2634:objective_ranking_or_market_share:00ab32673453e00d', '6175:objective_ranking_or_market_share:0a838c414def37cd', '2603:objective_ranking_or_market_share:c49229ece3415b49', '6869:objective_ranking_or_market_share:7e2d1e75d0b3577d'],
    '市占與分母': ['2207:objective_ranking_or_market_share:12f16578b4009931', '2890:objective_ranking_or_market_share:2ec04a9365b56c0f', '6951:objective_ranking_or_market_share:f85c202bfd3023a7', '9938:objective_ranking_or_market_share:75e89fb7124e96b1', '8415:objective_ranking_or_market_share:016f3d5d3ac36d27'],
    '客戶與歷史合作': ['4414:material_named_relationship:d5be7e550754288b', '6750:objective_ranking_or_market_share:40044574fe259065', '1464:material_named_relationship:d334c64365468203', '2329:material_named_relationship:19240fe9ac740634', '6805:material_named_relationship:c29ff8e8534503e0'],
    '供應商與獨家限定': ['2208:material_named_relationship:d3108d0f5a3afd74', '2330:material_named_relationship:d4821272fa108886', '2646:material_named_relationship:2da1bdd0a02eaff8', '9908:material_named_relationship:9ee2a3f7848520f1', '9926:material_named_relationship:9ee2a3f7848520f1'],
    '沿革與組織變更': ['1101:objective_ranking_or_market_share:70c0cf57f148a361', '3652:identity_changing_event:59acbb960f3cd20b', '3056:identity_changing_event:42ce16aac106b895', '3611:identity_changing_event:9235ca41b694fe7a', '8927:identity_changing_event:0ed472edc9669c94'],
    '期間與數值口徑': ['5007:export_concentration:0ee2200a2af138a8', '2481:export_concentration:3941f289bb5c6d99', '3455:material_named_relationship:82a4ffc86eb92f92', '5278:profitability_assertion:24a745be10d45843', '6908:export_concentration:fd2c6df51c194b44'],
}


def rows(path):
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def encode(value):
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':'))+'\n').encode()


def freeze(path, raw):
    if path.exists() and path.read_bytes() != raw:
        raise ValueError('Frozen artifact differs: '+str(path))
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(raw)


def edits(original, proposed, context):
    changes = []
    for qualifier in ['唯一', '獨家', '最大', '第一', '主要', '全球', '全台', '市占', '市佔', '控股', '母公司']:
        if qualifier in original and qualifier not in proposed:
            changes.append({'term': qualifier, 'change': '原限定詞未保留，須按修正句範圍另審'})
    if re.search(r'(?:19|20)\d{2}', proposed):
        changes.append({'term': '期間', 'change': '修正句明列日期或年度，不能轉為未限定當期'})
    if any('主要' in h['text'] for o in context.get('occurrences', []) for h in o['headings']):
        changes.append({'term': '原段落主要關係', 'change': '試批次另置業務與歷史資料段，原主要關係限定不自動繼承'})
    return changes


def main():
    summary = json.loads((INPUT/'summary.json').read_text())
    if not summary['complete']:
        raise ValueError('Original adjudication must finish first')
    parents = {r['claim_id']: r for r in rows(INPUT/'consolidated-status.jsonl')}
    finals = {r['claim_id']: r for r in rows(source.ROOT/'results.jsonl')}
    proposals_path = INPUT/'revised-claim-proposals.jsonl'
    grouped = {}
    for number, proposal in enumerate(rows(proposals_path), 1):
        cid = proposal['claim_id']
        key = re.sub(r'\s+', '', proposal['proposed_text'])
        record = {'proposal_ordinal': number, 'proposal': proposal, 'proposal_record_sha256': source.digest(encode(proposal))}
        grouped.setdefault(cid, {}).setdefault(key, []).append(record)
    inventory = []
    for cid, variants in grouped.items():
        parent = parents[cid]; claim = parent['claim']
        context = source.report_context(claim)
        candidates = [r for group in variants.values() for r in group]
        best = sorted(candidates, key=lambda r: (r['proposal']['stage'] != 'sol_proposal', r['proposal_ordinal']))[0]
        prop = best['proposal']; text = prop['proposed_text']
        if prop['stage'] == 'sol_proposal':
            evidence = [e for a in finals[cid]['adjudication']['atomic_claims'] for e in a['evidence']]
        else:
            evidence = json.loads((source.BASE/prop['evidence_manifest']).read_text()).get('sources', [])
        leads = list({s['url']: {'url': s['url'], 'title': s.get('title'), 'locator': s.get('locator')} for s in evidence if s.get('url')}.values())
        flags = []
        if claim['issuer_ticker'] != Path(context['resolved_report_path']).name.split('_', 1)[0]:
            flags.append('ticker_filename_mismatch')
        if not leads:
            flags.append('no_source_leads')
        inventory.append({'parent_claim_id': cid, 'parent_claim': claim, 'parent_effective_verdict': parent['verdict'],
            'parent_original_accepted': parent['final_ACCEPTED'], 'preferred_stage': prop['stage'],
            'preferred_proposal': text, 'preferred_proposal_sha256': source.digest(text.encode()),
            'preferred_proposal_record_sha256': best['proposal_record_sha256'],
            'proposal_variants': [{'normalized_text': k, 'records': v} for k, v in variants.items()],
            'variant_count': len(variants), 'source_leads': leads, 'report_context': context,
            'qualifier_changes': edits(claim['original_text'], text, context), 'routing_flags': flags,
            'priority': 1 if prop['stage'] == 'sol_proposal' else 2,
            'revision_support_verified': False, 'corpus_modified': False})
    inventory.sort(key=lambda r: (r['priority'], bool(r['routing_flags']), r['parent_claim']['issuer_ticker'], r['parent_claim_id']))
    freeze(ROOT/'inventory.jsonl', b''.join(encode(r) for r in inventory))
    by_id = {r['parent_claim_id']: r for r in inventory}
    pilot = []
    for category, cids in PILOT.items():
        for cid in cids:
            item = by_id[cid]; parent = item['parent_claim']
            if item['preferred_stage'] != 'sol_proposal' or item['routing_flags']:
                raise ValueError('Selected pilot does not meet routing contract: '+cid)
            ph = item['preferred_proposal_sha256']
            pilot.append({'claim_id': 'revision:'+source.digest(cid.encode())[:20]+':'+ph[:16],
                'normalized_claim_hash': ph, 'issuer_ticker': parent['issuer_ticker'], 'issuer_company': parent['issuer_company'],
                'original_text': item['preferred_proposal'], 'report_path': item['report_context']['resolved_report_path'],
                'cohort': 'revision_pilot', 'parent_claim_id': cid, 'parent_claim': parent,
                'source_leads': item['source_leads'], 'pilot_category': category,
                'proposed_target_section': '業務與歷史資料', 'qualifier_changes': item['qualifier_changes'],
                'proposal_binding': {'input_path': str(proposals_path.relative_to(source.BASE)), 'input_sha256': source.digest(proposals_path.read_bytes()),
                    'record_sha256': item['preferred_proposal_record_sha256'], 'proposed_text_sha256': ph},
                'parent_output_sha256': finals[cid]['output_sha256'], 'parent_report_context': item['report_context'],
                'assessment_date': '2026-10-08'})
    if len(pilot) != 30 or len({r['claim_id'] for r in pilot}) != 30:
        raise ValueError('Pilot must contain exactly 30 independent revisions')
    raw = b''.join(encode(r) for r in pilot)
    freeze(ROOT/'queue.jsonl', raw)
    manifest = {'schema': 'revision-pilot-queue-1', 'count': len(pilot), 'sha256': source.digest(raw),
        'assessment_date': '2026-10-08', 'categories': dict(Counter(r['pilot_category'] for r in pilot)),
        'company_count': len({r['issuer_ticker'] for r in pilot}), 'original_acceptance_authority': False,
        'inputs': {f: source.digest((INPUT/f).read_bytes()) for f in ['summary.json', 'consolidated-status.jsonl', 'revised-claim-proposals.jsonl']}}
    freeze(ROOT/'queue.manifest.json', encode(manifest))
    freeze(ROOT/'inventory.summary.json', encode({'proposal_rows': sum(len(v) for x in grouped.values() for v in x.values()),
        'parent_claim_count': len(inventory), 'unique_text_variants': sum(len(v) for v in grouped.values()),
        'preferred_stages': dict(Counter(x['preferred_stage'] for x in inventory)),
        'routing_flags': dict(Counter(f for x in inventory for f in x['routing_flags'])),
        'pilot': manifest}))
    print(json.dumps({'inventory': len(inventory), 'proposal_rows': 1491, 'pilot': manifest}, ensure_ascii=False))


if __name__ == '__main__':
    main()
