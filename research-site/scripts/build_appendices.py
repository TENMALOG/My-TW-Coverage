"""Generate the evidence appendix (appendices/evidence.qmd) from the frozen and new records.

Sections: A adopted facts (with evidence markers → citations), B relations (anchor rel-Rxx),
C every selected claim of the industry with its latest status and reason (anchor co-<ticker>),
D company-level re-research of 2630/6753 report statements, E open issues.
Original report wording shown in C/D is labelled as unverified source text, never as fact.

  python research-site/scripts/build_appendices.py
"""
from __future__ import annotations

import csv
import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SITE = ROOT / 'research-site'
DATA = SITE / 'data/aerospace-defense'
CR = ROOT / 'audit-v5/semantic/candidate-rerun'
CRES = ROOT / 'audit-v5/source-cache/candidate-rerun/company-research-aero-001/companies'
ORDER = ['2634', '4541', '4546', '4572', '8222', '2645', '2630', '2208', '2644', '6753']
NAMES = {'2208': '台船', '2630': '亞航', '2634': '漢翔', '2644': '中信造船', '2645': '長榮航太', '4541': '晟田',
         '4546': '長亨', '4572': '駐龍', '6753': '龍德造船', '8222': '寶一'}
ZH = {'REVISED_SUPPORTED': '新句通過', 'PARTIALLY_SUPPORTED': '部分支持', 'UNSUPPORTED': '不支持', 'ACCEPTED': '原句通過',
      'PRIMARY_REVIEW_FAILED': '來源覆核未通過', 'PERIOD_UNRESOLVED': '期間未解決', 'UNKNOWN_AFTER_RESEARCH': '研究後仍未知',
      'PARTIAL': '部分支持（初查）', 'UNKNOWN': '未知（初查）'}

OPEN_ISSUES = [
    '中信造船有百分之百持股子公司，卻未出現在公開資訊觀測站的合併損益彙總中；本研究的財務數字取自其年報財務績效表，口徑待確認。',
    '亞航 114 年度年報對銳鳶二型全案完成時間有兩種記載（2025 年 8 月完成、2025 年 9 月驗結），本研究兩者並列。',
    '晟田 114 年度年報主要客戶表中，113 年度甲公司銷貨 583,728 千元除以銷貨淨額 1,416,505 千元約為 41.21%，與表列 42.20% 不一致。',
    '8 家公司以代號揭露最大客戶，本研究不推定代號身分；例如晟田「甲公司」是否為漢翔，現有可重現證據不足。',
    '長榮航太的 747 機體 MRO 市占、中信造船的海巡艦艇市占、燁鋒的「亞洲唯一」均屬公司自述，未取得獨立比較資料。',
    '公開資訊觀測站年報快照取自 2026-10-10；公司官網頁面的擷取日晚於評估基準日 2026-10-08，僅用於引述公司說法，不回推當日狀態。',
]


def jsonl(p):
    p = Path(p)
    return [json.loads(l) for l in p.read_text(encoding='utf-8').splitlines() if l.strip()] if p.exists() else []


def short(fid):
    return fid if not fid.startswith('revision') else 'revision:…' + fid.split(':')[-1][:8]


def esc(s):
    return (s or '').replace('[[', '').replace(']]', '').replace('|', '／').replace('\n', ' ')


def main():
    facts = jsonl(DATA / 'verified-facts.jsonl')
    rels = list(csv.DictReader(open(DATA / 'relations.csv', encoding='utf-8')))
    claims = [r for r in csv.DictReader(open(SITE / 'catalog/release-scope-claims.csv', encoding='utf-8-sig'))
              if r['industry_folder'] == 'Aerospace & Defense']
    # latest outcome per parent claim (pilot → aero-001 → aero-002; a pass is never overwritten)
    latest = {}
    for path, label in ((CR / 'revision-pilot-001/delivery/pilot-outcomes.jsonl', 'revision-pilot-001'),
                        (CR / 'revision-aero-001/delivery/outcomes.jsonl', 'revision-aero-001'),
                        (CR / 'revision-aero-002/delivery/outcomes.jsonl', 'revision-aero-002')):
        for o in jsonl(path):
            cur = latest.get(o['parent_claim_id'])
            if cur and cur['verdict'] == 'REVISED_SUPPORTED':
                continue
            latest[o['parent_claim_id']] = {**o, 'batch': label}
    psr = {}
    for b in ('revision-aero-001', 'revision-aero-002'):
        for r in jsonl(CR / b / 'adjudication/primary-source-review.jsonl'):
            psr[r['claim_id']] = r

    L = ['---\ntitle: "證據附錄"\n---\n', '<!-- 由 research-site/scripts/build_appendices.py 產生；請勿手動修改。 -->\n',
         '本附錄列出航太與國防章採用的全部事實與關係、本產業每一條被選入查核的原報告敘述及其結果，以及仍未解決的問題。'
         '評估基準日為 2026-10-08。標示「原報告敘述」的文字是查核對象，不代表本研究認定其為事實。\n']

    L.append('## 採用的事實 {#sec-ev-facts}\n')
    L += ['| 編號 | 公司 | 主題 | 內容 | 期間 | 來源 |', '|---|---|---|---|---|---|']
    for f in sorted(facts, key=lambda x: (ORDER.index(x['ticker']), x['fact_id'])):
        L.append(f'| {short(f["fact_id"])} | {NAMES[f["ticker"]]} | {f["topic"]} | {esc(f["text"])} | {esc(f["period"])[:40]} | 〔{short(f["fact_id"])}〕 |')
    L.append('')

    L.append('## 有證據的公司關係 {#sec-ev-relations}\n')
    L.append('「甲 → 乙：類型」讀作「甲是乙的（類型）」。\n')
    for r in rels:
        L.append(f'- []{{#rel-{r["relation_id"]}}}**{r["relation_id"]}**　{r["subject"]} → {r["object"]}：{r["relation_type"]}；'
                 f'範圍：{r["scope"]}；期間：{r["period"]}；資訊來源：{r["attribution"]}'
                 + (f'；註：{r["note"]}' if r['note'] else '') + f'〔{r["relation_id"]}〕')
    L.append('')

    L.append('## 選定主張的查核結果 {#sec-ev-claims}\n')
    L.append('原專案共有 17 條本產業敘述被選入查核。每條先由原報告抽出，再經原句重查或強模型裁定；'
             '其中 17 條都有修正版本，修正版本另行獨立驗證並經來源覆核。下表列出每條的最新結果。\n')
    by_tk = defaultdict(list)
    for c in claims:
        by_tk[c['ticker']].append(c)
    for tk in ORDER:
        if tk not in by_tk:
            continue
        L.append(f'### {tk} {NAMES[tk]} {{#co-{tk}}}\n')
        for c in by_tk[tk]:
            o = latest.get(c['claim_id'])
            L.append(f'- **原報告敘述**（{c["claim_type"]}；原句裁定：{ZH.get(c["parent_verdict"], c["parent_verdict"])}）：「{esc(c["original_text"])}」')
            if o is None:
                L.append('    - 尚無修正版本驗證。')
                continue
            L.append(f'    - **最新結果**：{ZH.get(o["verdict"], o["verdict"])}（{o["batch"]}）。驗證的修正版本：「{esc(o["proposed_text"])}」')
            review = psr.get(o['claim_id'])
            if review and review['status'] == 'FAIL':
                L.append(f'    - **來源覆核**：{esc(review["review_basis"])}')
            elif o['verdict'] != 'REVISED_SUPPORTED':
                L.append(f'    - **理由**：{esc(o["rationale"])}')
        L.append('')

    L.append('## 公司層級重新研究：亞航、龍德造船 {#sec-ev-companyresearch}\n')
    L.append('這兩家公司沒有被選入原查核範圍。本研究另就原報告的主要敘述做公司層級研究；'
             '以下為研究階段判定，只有經年報等原始資料獨立核對的內容才列入「採用的事實」。\n')
    for tk in ('2630', '6753'):
        finals = sorted((CRES / tk).glob('attempt-*/final.json'))
        if not finals:
            continue
        out = json.loads(finals[-1].read_text(encoding='utf-8'))
        L.append(f'### {tk} {NAMES[tk]} {{#co-{tk}}}\n')
        for st in out['statements']:
            L.append(f'- **{st["key"]}**（研究階段判定：{ZH.get(st["verdict"], st["verdict"])}）：{esc(st["rationale"])}')
        L.append('')

    L.append('## 未解決的問題 {#sec-ev-open}\n')
    for i in OPEN_ISSUES:
        L.append(f'- {i}')
    L.append('')
    (SITE / 'appendices/evidence.qmd').write_text('\n'.join(L), encoding='utf-8')
    print(f'facts {len(facts)}, relations {len(rels)}, claims {len(claims)}, outcomes matched {sum(1 for c in claims if c["claim_id"] in latest)}')


if __name__ == '__main__':
    main()
