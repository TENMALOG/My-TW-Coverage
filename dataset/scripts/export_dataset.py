"""Export the verified research as a versioned dataset release for 股.tw and other consumers.

  python dataset/scripts/export_dataset.py --version 2026.10.0
      [--gu-tw-research "C:/Users/Neo Pegasus/Documents/codex-project/075-Stock-surf-rewrite/backend/data/research.json"]
      [--force]

Writes dataset/releases/{version}/ (companies, facts, statements, audits, financials, manifest,
LICENSE-NOTICE). A release folder is never rewritten unless --force is given. Only verified content
enters facts/statements: annual-report facts need verification PASS and no semantic-review REJECT;
statements are the adoptable sentences of the audited claims. Unknowns stay null.
The format is described in dataset/GU-TW-INTEGRATION-PLAN.md.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import subprocess
import unicodedata
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SITE = ROOT / 'research-site'
CR = ROOT / 'audit-v5/semantic/candidate-rerun'
GU_TW_RESEARCH = Path('C:/Users/Neo Pegasus/Documents/codex-project/075-Stock-surf-rewrite/backend/data/research.json')
SCHEMA_VERSION = '1.0'
ASSESSMENT_DATE = '2026-10-08'
OFFICIAL_HOSTS = ('mops.twse.com.tw', 'mopsov.twse.com.tw', 'doc.twse.com.tw', 'twse.com.tw', 'tpex.org.tw', '.gov.tw')
ATTRIBUTION = {'公司年報揭露': 'annual_report', '公司年報自述（未經獨立驗證的排名或評價）': 'self_description',
               '公司年報引述第三方資料': 'third_party'}
# our final result -> 股.tw research-evidence status (see the integration plan, section 3)
GU_TW_STATUS = {'REVISED_SUPPORTED': 'corrected', 'PARTIALLY_SUPPORTED': 'partial', 'UNSUPPORTED': 'not_supported',
                'PERIOD_UNRESOLVED': 'needs_period', 'UNKNOWN_AFTER_RESEARCH': 'unverified',
                'PRIMARY_REVIEW_FAILED': 'unverified'}


def sha256(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def jsonl(path):
    return [json.loads(l) for l in Path(path).read_text(encoding='utf-8').splitlines() if l.strip()]


def roc_date(s):
    """'68/07/07' -> '1979-07-07'; anything else -> None."""
    m = re.fullmatch(r'\s*(\d{2,3})/(\d{1,2})/(\d{1,2})\s*', s or '')
    if not m:
        return None
    return f'{int(m[1]) + 1911:04d}-{int(m[2]):02d}-{int(m[3]):02d}'


def official(url):
    host = re.sub(r'^https?://', '', url or '').split('/')[0].lower()
    return any(host == h or host.endswith(h) for h in OFFICIAL_HOSTS)


# ---------------------------------------------------------------- companies
def build_companies():
    catalog = list(csv.DictReader(open(SITE / 'catalog/release-scope-companies.csv', encoding='utf-8-sig')))
    names = {r['industry_folder']: r for r in csv.DictReader(open(SITE / 'data/industry-names.csv', encoding='utf-8-sig'))}
    basic = {r['ticker']: r for r in jsonl(SITE / 'data/basic-data.jsonl')} if (SITE / 'data/basic-data.jsonl').exists() else {}
    rows = []
    for c in catalog:
        b = basic.get(c['ticker'], {})
        twse, tpex = roc_date(b.get('twse_listed_roc')), roc_date(b.get('tpex_listed_roc'))
        ind = names.get(c['industry_folder'], {})
        rows.append({
            'ticker': c['ticker'],
            'name_in_original_project': c['company'],
            'legal_name': b.get('legal_name'),
            'name_en': (b.get('name_en') or '').strip() or None,
            'market': '上市' if twse else ('上櫃' if tpex else None),
            'listing_status': {'parsed': 'public', 'ceased_public_offering': 'ceased_public_offering'}.get(b.get('status'))
                              if b else None,
            'industry': {'folder': c['industry_folder'], 'slug': ind.get('slug'),
                         'name_zh': (ind.get('name_zh') or '').rstrip('?') or None,
                         'name_zh_needs_review': (ind.get('name_zh') or '').endswith('?'),
                         'mops_category': b.get('industry_mops')},
            'established': roc_date(b.get('established_roc')),
            'address': b.get('address'),
            'twse_listed': twse, 'tpex_listed': tpex,
            'source': ({'kind': 'mops_basic_data', **b['source']} if b.get('source') else None),
        })
    return rows


# ---------------------------------------------------------------- facts
def semantic_verdicts():
    path = SITE / 'data/company-facts/_semantic-review.jsonl'
    latest = {}
    if path.exists():
        for r in jsonl(path):
            latest[r['id']] = r
    return latest


def build_facts():
    review = semantic_verdicts()
    rows, skipped = [], {'mechanical_fail': 0, 'semantic_reject': 0, 'unverified': 0}
    for p in sorted((SITE / 'data/company-facts').glob('[0-9A-Z]*.json')):
        doc = json.loads(p.read_text(encoding='utf-8'))
        src = doc['source']
        for f in doc['facts']:
            v = f.get('verification') or {}
            if not v:
                skipped['unverified'] += 1; continue
            if v.get('status') != 'PASS':
                skipped['mechanical_fail'] += 1; continue
            sem = review.get(f['id'])
            if sem and sem['verdict'] == 'REJECT':
                skipped['semantic_reject'] += 1; continue
            rows.append({
                'id': f['id'], 'ticker': doc['ticker'], 'field': f['field'], 'statement': f['statement'],
                'period': f['period'] or None, 'attribution': ATTRIBUTION.get(f['attribution'], f['attribution']),
                'source': {'kind': 'annual_report', 'citation_url': src['citation_url'], 'fy': src['fy'],
                           'filename': src['filename'], 'page': f['page'], 'excerpts': f['excerpts'],
                           'text_sha256': src['text_sha256'], 'legal_name': doc['legal_name']},
                'verification': {'mechanical': 'PASS', 'mechanical_at': v.get('verified_at'),
                                 'semantic': 'ACCEPT' if sem else 'not_sampled',
                                 'semantic_at': sem['reviewed_at'] if sem else None},
            })
    return rows, skipped


# ---------------------------------------------------------------- statements and audits
def outcome_dates():
    """claim_id -> date the deciding adjudication was recorded (YYYY-MM-DD)."""
    dates = {}
    for res in CR.glob('revision-*/adjudication/results.jsonl'):
        for r in jsonl(res):
            if r.get('output') and r.get('recorded_at'):
                dates[r['claim_id']] = r['recorded_at'][:10]
    return dates


def plain(text):
    return unicodedata.normalize('NFC', (text or '').replace('**', '').replace('[[', '').replace(']]', '')).strip()


class GuTwBlocks:
    """Blocks of the 股.tw pinned research snapshot, with the ids and hashes its claimsFor() checks."""

    def __init__(self, path: Path):
        self.ok = path.exists()
        self.commit, self.by_code = None, {}
        if not self.ok:
            return
        data = json.loads(path.read_text(encoding='utf-8'))
        self.commit = data['metadata']['commit']
        for rep in data['reports']:
            blocks = []
            for section, items in rep['sections'].items():
                for i, b in enumerate(items, 1):
                    blocks.append({'blockId': f"{rep['code']}:{section}:{i}", 'sha256': sha256(b['text'].encode('utf-8')),
                                   'plain': plain(b['text'])})
            self.by_code[rep['code']] = blocks

    def target(self, code, original_text):
        if not self.ok:
            return None, 'gu_tw_snapshot_not_available'
        blocks = self.by_code.get(code)
        if not blocks:
            return None, 'report_not_in_gu_tw_snapshot'
        quote = plain(original_text).rstrip('。')
        for b in blocks:
            if quote and quote in b['plain']:
                return {'blockId': b['blockId'], 'sha256': b['sha256'], 'quote': quote}, None
        return None, 'quote_not_found_in_pinned_snapshot'


def build_statements_and_audits(gu):
    claims = list(csv.DictReader(open(SITE / 'catalog/release-scope-claims.csv', encoding='utf-8-sig')))
    sentences = {r['claim_id']: r for r in jsonl(SITE / 'data/verified-sentences.jsonl')}
    dates = outcome_dates()
    statements, audits = [], []
    for c in claims:
        cid = c['claim_id']
        s = sentences.get(cid)
        if s:
            statements.append({'id': cid, 'ticker': c['ticker'], 'text': s['text'],
                               'kind': 'original' if c['adoption_basis'] == '原句最終 ACCEPTED' else 'revised',
                               'period': s.get('period') or None, 'claim_type': c['claim_type'],
                               'citations': [{**x, 'official': official(x.get('url'))} for x in s['citations']],
                               'basis': s['basis']})
        if c['adoption_basis'] == '原句最終 ACCEPTED':
            outcome, status = 'original_accepted', 'verified'
        elif c['revision_status'] == '新句通過':
            outcome, status = 'revised_supported', 'corrected'
        elif c['revision_final_verdict']:
            outcome, status = c['revision_final_verdict'].lower(), GU_TW_STATUS.get(c['revision_final_verdict'], 'unverified')
        else:
            outcome, status = 'no_revision_proposal', 'unverified'
        reviewed = dates.get(c['revision_id']) if c['revision_id'] else None
        target, why = gu.target(c['ticker'], c['original_text'])
        verified = status in ('verified', 'corrected')
        gu_tw = None
        if target:
            cites = s['citations'] if s else []
            gu_tw = {'source_commit': gu.commit, 'target': target, 'status': status,
                     'text': s['text'] if s else None, 'scope': c['claim_type'],
                     'period': (s.get('period') if s else None) or None,
                     'reviewedAt': reviewed, 'verifiedAt': reviewed if verified else None,
                     'officialSources': [{'label': x.get('title'), 'url': x['url'], 'publishedOn': x.get('publication_date')}
                                         for x in cites if official(x.get('url'))]}
        audits.append({'claim_id': cid, 'ticker': c['ticker'], 'claim_type': c['claim_type'],
                       'original_text': c['original_text'], 'outcome': outcome,
                       'adopted_text': s['text'] if s else None,
                       'statement_id': cid if s else None, 'reviewed_at': reviewed,
                       'gu_tw': gu_tw, 'gu_tw_unmatched_reason': why})
    return statements, audits


# ---------------------------------------------------------------- financials
def build_financials():
    rows = []
    for r in json.loads((SITE / 'data/financials/fy2025-financials-all.json').read_text(encoding='utf-8')):
        for year, y in r['years'].items():
            rows.append({'ticker': r['ticker'], 'year': int(year), 'table_kind': y['table_kind'],
                         'unit': 'TWD thousand', 'items': y['items_k'],
                         'gross_margin_pct': y.get('gross_margin_pct'), 'operating_margin_pct': y.get('operating_margin_pct'),
                         'formula': r['formula'], 'source': {'kind': 'mops_t163sb04', **y['source']}})
    return rows


# ---------------------------------------------------------------- release
def write_jsonl(path, rows):
    data = ''.join(json.dumps(r, ensure_ascii=False, sort_keys=True) + '\n' for r in rows).encode('utf-8')
    path.write_bytes(data)
    return {'sha256': sha256(data), 'rows': len(rows), 'bytes': len(data)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--version', required=True)
    ap.add_argument('--gu-tw-research', default=str(GU_TW_RESEARCH))
    ap.add_argument('--force', action='store_true')
    a = ap.parse_args()
    if not re.fullmatch(r'\d{4}\.\d{2}\.\d+', a.version):
        raise SystemExit('version must look like 2026.10.0')
    out = ROOT / 'dataset/releases' / a.version
    if out.exists() and not a.force:
        raise SystemExit(f'{out} exists; releases are immutable (use a new version or --force for a draft)')
    out.mkdir(parents=True, exist_ok=True)

    gu = GuTwBlocks(Path(a.gu_tw_research))
    companies = build_companies()
    facts, skipped = build_facts()
    statements, audits = build_statements_and_audits(gu)
    financials = build_financials()
    known = {c['ticker'] for c in companies}
    for name, rows in (('facts', facts), ('statements', statements), ('audits', audits), ('financials', financials)):
        stray = {r['ticker'] for r in rows} - known
        if stray:
            raise SystemExit(f'{name}: tickers not in companies: {sorted(stray)[:5]}')

    files = {}
    for name, rows in (('companies', companies), ('facts', facts), ('statements', statements),
                       ('audits', audits), ('financials', financials)):
        files[f'{name}.jsonl'] = write_jsonl(out / f'{name}.jsonl', rows)
    lic = (ROOT / 'LICENSE').read_text(encoding='utf-8')
    notice = ('# 授權與來源聲明\n\n本資料集的查核起點為 Timeverse/My-TW-Coverage（MIT 授權）的公司報告；'
              '所有 facts 與 statements 均依公開資料重新查證。原專案授權全文如下。\n\n```\n' + lic + '\n```\n').encode('utf-8')
    (out / 'LICENSE-NOTICE.md').write_bytes(notice)
    files['LICENSE-NOTICE.md'] = {'sha256': sha256(notice), 'bytes': len(notice)}
    try:
        commit = subprocess.run(['git', '-C', str(ROOT), 'rev-parse', 'HEAD'], capture_output=True, text=True).stdout.strip() or None
        dirty = bool(subprocess.run(['git', '-C', str(ROOT), 'status', '--porcelain'], capture_output=True, text=True).stdout.strip())
    except OSError:
        commit, dirty = None, None
    matched = sum(1 for r in audits if r['gu_tw'])
    manifest = {
        'name': 'tw-verified-company-research', 'version': a.version, 'schema_version': SCHEMA_VERSION,
        'generated_at': datetime.now(timezone.utc).isoformat(timespec='seconds'),
        'assessment_date': ASSESSMENT_DATE, 'source_commit': commit, 'source_tree_dirty': dirty,
        'gu_tw_snapshot_commit': gu.commit,
        'counts': {'companies': len(companies), 'companies_with_facts': len({r['ticker'] for r in facts}),
                   'facts': len(facts), 'facts_excluded': skipped, 'statements': len(statements),
                   'audits': len(audits), 'audits_matched_to_gu_tw': matched, 'financial_rows': len(financials)},
        'files': files,
        'notes': ['facts: annual-report facts that passed mechanical verification and were not rejected in semantic review',
                  'statements: verified sentences adopted from the claim audit; kind=revised sentences are narrower than the original claim',
                  'audits: every audited claim, including those that did not pass; gu_tw is null when the original sentence is not found verbatim in the 股.tw pinned snapshot'],
    }
    (out / 'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=1), encoding='utf-8')
    print(json.dumps(manifest['counts'], ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
