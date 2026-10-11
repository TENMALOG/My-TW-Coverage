"""Generate T2 company research pages for the aerospace & defense chapter.

Only verified content is rendered: verified-facts.jsonl, fy2025-metrics.json,
fy2025-financials.json and relations.csv. Claims that did not pass are summarised as
gaps (counts + status) and linked to the evidence appendix; their wording is not reproduced.
Identity gate: the filename ticker/company, the MOPS annual-report filename ticker and the
full legal name in the annual-report text must all agree, otherwise the build stops.

  python research-site/scripts/build_company_pages.py
"""
from __future__ import annotations

import csv
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SITE = ROOT / 'research-site'
DATA = SITE / 'data/aerospace-defense'
CR = ROOT / 'audit-v5/semantic/candidate-rerun'
MOPS = ROOT / 'audit-v5/source-cache/research-site/mops-annual'
OUTDIR = SITE / 'chapters/companies'
ASSESSMENT = '2026-10-08'

COMPANIES = {
    '2208': ('台船', '台灣國際造船股份有限公司', '造船'),
    '2630': ('亞航', '亞洲航空股份有限公司', '航空器維修'),
    '2634': ('漢翔', '漢翔航空工業股份有限公司', '航空製造'),
    '2644': ('中信造船', '中信造船股份有限公司', '造船'),
    '2645': ('長榮航太', '長榮航太科技股份有限公司', '航空器維修'),
    '4541': ('晟田', '晟田科技工業股份有限公司', '航空製造'),
    '4546': ('長亨', '長亨精密股份有限公司', '航空製造'),
    '4572': ('駐龍', '駐龍精密機械股份有限公司', '航空製造'),
    '6753': ('龍德造船', '龍德造船工業股份有限公司', '造船'),
    '8222': ('寶一', '寶一科技股份有限公司', '航空製造'),
}
TOPIC_ORDER = ['業務與產品', '營收結構', '客戶', '供應商', '重大合約', '集團與轉投資', '沿革', '其他', '業務與歷史資料']
STATUS_ZH = {'REVISED_SUPPORTED': '新句通過', 'PARTIALLY_SUPPORTED': '部分支持', 'UNSUPPORTED': '不支持',
             'PRIMARY_REVIEW_FAILED': '來源覆核未通過', 'PERIOD_UNRESOLVED': '期間未解決',
             'UNKNOWN_AFTER_RESEARCH': '研究後仍未知', 'ACCEPTED': '原句通過'}


def jsonl(p):
    return [json.loads(l) for l in Path(p).read_text(encoding='utf-8').splitlines() if l.strip()]


def identity_gate(tk, short, full):
    report = list((ROOT / 'Pilot_Reports').glob(f'*/{tk}_*.md'))
    if len(report) != 1 or report[0].stem.split('_', 1)[1] != short:
        sys.exit(f'{tk}: report filename does not match {short}: {report}')
    meta = json.loads((MOPS / f'{tk}_2025_F04.json').read_text(encoding='utf-8'))
    if f'_{tk}_' not in meta['filename']:
        sys.exit(f'{tk}: MOPS filename mismatch {meta["filename"]}')
    text = re.sub(r'\s+', '', (ROOT / meta['text_path']).read_text(encoding='utf-8'))
    if full not in text:
        sys.exit(f'{tk}: legal name {full} not found in annual report')
    return report[0], meta


def claim_status():
    """Final status per parent claim id for this industry (latest batch wins)."""
    status = {}
    for line in csv.DictReader(open(SITE / 'catalog/release-scope-claims.csv', encoding='utf-8-sig')):
        if line['industry_folder'] == 'Aerospace & Defense':
            status[line['claim_id']] = {'ticker': line['ticker'], 'type': line['claim_type'],
                                        'status': 'ACCEPTED' if line['adoption_basis'] == '原句最終 ACCEPTED' else line['parent_verdict']}
    for r in jsonl(CR / 'revision-pilot-001/delivery/pilot-outcomes.jsonl'):
        if r['parent_claim_id'] in status:
            status[r['parent_claim_id']]['status'] = r['verdict']
    for batch in ('revision-aero-001', 'revision-aero-002'):
        for r in jsonl(CR / batch / 'delivery/outcomes.jsonl'):
            cur = status[r['parent_claim_id']]
            if cur['status'] != 'REVISED_SUPPORTED':
                cur['status'] = r['verdict']
    return status


def pct(v):
    return f'{int(v)}' if float(v).is_integer() else f'{v:.2f}'


def research_statements(tk):
    """Report statements re-checked in company-research-aero-001 (research-stage verdicts)."""
    finals = sorted((ROOT / 'audit-v5/source-cache/candidate-rerun/company-research-aero-001/companies' / tk).glob('attempt-*/final.json'))
    if not finals:
        return []
    return json.loads(finals[-1].read_text(encoding='utf-8'))['statements']


def fmt_m(k):
    """仟元 → 百萬元, conventional half-up rounding (Python's round() is half-to-even)."""
    from decimal import ROUND_HALF_UP, Decimal
    return f'{(Decimal(k) / 1000).quantize(Decimal(1), rounding=ROUND_HALF_UP):,}'


def cite(fact):
    c = fact['citations'][0] if fact['citations'] else {}
    loc = c.get('locator', '')
    return f"〔{fact['fact_id'] if not fact['fact_id'].startswith('revision') else 'revision:…' + fact['fact_id'].split(':')[-1][:8]}〕"


def main():
    facts = defaultdict(list)
    for f in jsonl(DATA / 'verified-facts.jsonl'):
        facts[f['ticker']].append(f)
    metrics = {r['ticker']: r for r in json.loads((DATA / 'fy2025-metrics.json').read_text(encoding='utf-8'))}
    fins = {r['ticker']: r for r in json.loads((DATA / 'fy2025-financials.json').read_text(encoding='utf-8'))}
    rels = list(csv.DictReader(open(DATA / 'relations.csv', encoding='utf-8')))
    status = claim_status()
    OUTDIR.mkdir(parents=True, exist_ok=True)
    written = []
    for tk, (short, full, seg) in COMPANIES.items():
        report, meta = identity_gate(tk, short, full)
        m, fin = metrics[tk], fins[tk]
        L = [f'---\ntitle: "{tk} {short}"\nsubtitle: "{full}"\n---\n',
             f'<!-- 由 research-site/scripts/build_company_pages.py 產生；請勿手動修改。 -->\n',
             '## 研究範圍 {.unnumbered}\n',
             f'- **公司**：{full}（股票代號 {tk}），本研究歸入「{seg}」次領域。',
             f'- **資料截止**：主要依據 2025 年度年報（{meta["filename"]}），查核評估基準日 {ASSESSMENT}。',
             '- **研究深度**：T2 深入研究頁。本頁只列已驗證的事實與年報數據；未通過查核的原報告敘述不列入正文。\n']
        # financial summary
        L += ['## 營收與財務摘要 {.unnumbered}\n',
              '| 項目 | 2024 | 2025 |', '|---|---:|---:|',
              f'| 營業收入（百萬元） | {fmt_m(fin["revenue_2024_k"])} | {fmt_m(fin["revenue_2025_k"])} |',
              f'| 毛利率 | {fin["gross_margin_2024_pct"]:.2f}% | {fin["gross_margin_2025_pct"]:.2f}% |',
              f'| 營業利益率 | {fin["operating_margin_2024_pct"]:.2f}% | {fin["operating_margin_2025_pct"]:.2f}% |',
              f'| 最大客戶占比（2025） | — | {pct(m["top_customer_share_pct"])}%（{m["top_customer"]}） |\n',
              f'口徑：{fin["basis"]}。最大客戶占比取自年報主要銷貨客戶表（第 {m["customer_table_page"]} 頁）。〔metric:{tk}；fin:{tk}〕\n']
        # facts by topic
        by_topic = defaultdict(list)
        for f in facts.get(tk, []):
            by_topic[f['topic']].append(f)
        L.append('## 已驗證事實 {.unnumbered}\n')
        if not by_topic:
            L.append('本公司目前沒有逐條驗證的事實；請參考上方年報數據與下方資料缺口。\n')
        for topic in TOPIC_ORDER:
            if topic not in by_topic:
                continue
            L.append(f'### {topic if topic != "業務與歷史資料" else "查核後採用的敘述"} {{.unnumbered}}\n')
            for f in by_topic[topic]:
                L.append(f'- {f["text"]}{cite(f)}')
            L.append('')
        # relations
        mine = [r for r in rels if short in (r['subject'], r['object']) or r['subject'].startswith(short) or r['object'].startswith(short)]
        L.append('## 有證據的公司關係 {.unnumbered}\n')
        if mine:
            L.append('表中「甲 → 乙：類型」讀作「甲是乙的（類型）」，例如「中鋼 → 台船：供應商」表示中鋼是台船的供應商。\n')
            L += ['| 關係 | 範圍 | 期間 | 資訊來源 |', '|---|---|---|---|']
            for r in mine:
                L.append(f'| {r["subject"]} → {r["object"]}：{r["relation_type"]} | {r["scope"]} | {r["period"]} | {r["attribution"]}〔{r["relation_id"]}〕 |')
            L.append('')
        else:
            L.append('目前沒有可列入的具名關係。\n')
        # gaps
        mine_claims = [v for v in status.values() if v['ticker'] == tk]
        open_claims = [v for v in mine_claims if v['status'] not in ('REVISED_SUPPORTED', 'ACCEPTED')]
        L.append('## 資料缺口與未通過的原報告敘述 {.unnumbered}\n')
        if mine_claims:
            L.append(f'原報告共有 {len(mine_claims)} 條敘述被選入查核，其中 {len(mine_claims) - len(open_claims)} 條已有通過的版本，'
                     f'{len(open_claims)} 條尚未通過。')
        else:
            L.append('原查核範圍沒有選入本公司的敘述。')
        if open_claims:
            cnt = Counter((v['type'], STATUS_ZH.get(v['status'], v['status'])) for v in open_claims)
            L += ['', '| 敘述類型 | 查核結果 | 條數 |', '|---|---|---:|']
            for (typ, st), n in sorted(cnt.items()):
                L.append(f'| {typ} | {st} | {n} |')
            L.append('')
            L.append(f'未通過的敘述沒有寫入本頁正文，逐條裁定與理由見[證據附錄](../../appendices/evidence.qmd#co-{tk})。\n')
        else:
            L.append('')
        stmts = research_statements(tk)
        if stmts:
            cnt = Counter({**STATUS_ZH, 'ACCEPTED': '可支持'}.get(x['verdict'], x['verdict']) for x in stmts)
            L.append(f'另外，本研究對原報告的 {len(stmts)} 條主要敘述做了公司層級的重新研究（研究階段判定）：'
                     + '、'.join(f'{k} {v} 條' for k, v in cnt.items())
                     + '。只有經年報等原始資料獨立核對的內容，才列入上方「已驗證事實」。\n')
        if m['top_customer_named'] is False:
            L.append(f'- 年報以代號揭露最大客戶（{m["top_customer"]}），本研究不推定其身分。')
        if 'basis' in fin and '待確認' in fin['basis']:
            L.append('- 財務數字的合併或個體口徑待確認。')
        L.append('')
        # sources
        L.append('## 主要來源 {.unnumbered}\n')
        srcs = {}
        srcs[meta['citation_url']] = f'{full} 2025 年度年報（公開資訊觀測站，{meta["filename"]}）'
        for f in facts.get(tk, []):
            for c in f['citations']:
                srcs.setdefault(c['url'], c.get('title') or c['url'])
        for url, title in srcs.items():
            L.append(f'- [{title}]({url})')
        L.append('')
        out = OUTDIR / f'{tk}.qmd'
        out.write_text('\n'.join(L), encoding='utf-8')
        written.append(out)
        print(tk, short, 'facts', len(facts.get(tk, [])), 'relations', len(mine), 'claims', len(mine_claims), 'open', len(open_claims))
    print(f'{len(written)} pages written')


if __name__ == '__main__':
    main()
