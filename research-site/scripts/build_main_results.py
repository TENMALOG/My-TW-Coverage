"""Generate chapters/main/results.qmd; every number is read from frozen or batch summaries.

  python research-site/scripts/build_main_results.py
"""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SITE = ROOT / 'research-site'
CR = ROOT / 'audit-v5/semantic/candidate-rerun'


def load(p):
    return json.loads(Path(p).read_text(encoding='utf-8'))


def jsonl(p):
    return [json.loads(l) for l in Path(p).read_text(encoding='utf-8').splitlines() if l.strip()]


def n(x):
    return f'{x:,}'


def main():
    cat = load(SITE / 'catalog/catalog-manifest.json')['totals']
    st = load(CR / 'delivery/summary.json')
    pilot = load(CR / 'revision-pilot-001/delivery/summary.json')
    a1 = load(CR / 'revision-aero-001/delivery/summary.json')
    a2 = load(CR / 'revision-aero-002/delivery/summary.json')
    rerun = st['candidate_rerun']['verdicts']
    so, sc = st['strong_adjudication']['original']['verdicts'], st['strong_adjudication']['candidate']['verdicts']
    strong = Counter(so) + Counter(sc)
    # aerospace parents: passed if any revision for the parent passed
    passed_parents, all_parents = set(), set()
    for path in (CR / 'revision-pilot-001/delivery/pilot-outcomes.jsonl', CR / 'revision-aero-001/delivery/outcomes.jsonl',
                 CR / 'revision-aero-002/delivery/outcomes.jsonl'):
        for o in jsonl(path):
            if o['ticker'] in {'2208', '2630', '2634', '2644', '2645', '4541', '4546', '4572', '6753', '8222'}:
                all_parents.add(o['parent_claim_id'])
                if o['verdict'] == 'REVISED_SUPPORTED':
                    passed_parents.add(o['parent_claim_id'])
    zh = {'PARTIAL': '部分支持', 'UNKNOWN': '未知', 'CANDIDATE_ACCEPTED': '候選通過', 'ACCEPTED': '原句通過',
          'PARTIALLY_SUPPORTED': '部分支持', 'PERIOD_UNRESOLVED': '期間未解決', 'UNKNOWN_AFTER_RESEARCH': '研究後仍未知',
          'UNSUPPORTED': '不支持', 'REVISED_SUPPORTED': '新句通過', 'PRIMARY_REVIEW_FAILED': '來源覆核未通過'}

    def table(d):
        rows = ['| 結果 | 條數 |', '|---|---:|'] + [f'| {zh.get(k, k)} | {n(v)} |' for k, v in sorted(d.items(), key=lambda kv: -kv[1])]
        return '\n'.join(rows) + f'\n| **合計** | **{n(sum(d.values()))}** |\n'

    md = f'''---
title: "研究結果"
---

<!-- 由 research-site/scripts/build_main_results.py 產生；數字取自 catalog-manifest.json 與各批次 delivery/summary.json。 -->

## 查核覆蓋範圍 {{#sec-r-coverage}}

原專案 {n(cat["reports"])} 份公司報告分布在 {cat["industry_folders"]} 個產業資料夾。本研究選入查核的敘述共 {n(cat["claims_in_scope"])} 條，涵蓋 {n(cat["companies_with_claims"])} 家公司；其餘 {n(cat["reports"] - cat["companies_with_claims"])} 家公司沒有選入查核的敘述。

## 第一階段：原句重查 {{#sec-r-stage1}}

{n(st["candidate_rerun"]["requested"])} 條原本判定為部分支持或未知的敘述，經逐條重查後結果如下。「候選通過」只代表進入下一階段，不是最終接受。

{table(rerun)}
## 第二階段：原句最終裁定 {{#sec-r-stage2}}

原本判定通過的 {st["strong_adjudication"]["original"]["reviewed"]} 條，加上第一階段的 {st["strong_adjudication"]["candidate"]["reviewed"]} 條候選，共 {st["strong_adjudication"]["original"]["reviewed"] + st["strong_adjudication"]["candidate"]["reviewed"]} 條，由較強的模型重新裁定：

{table(dict(strong))}
原本判定通過的 {st["strong_adjudication"]["original"]["reviewed"]} 條中，最終只有 {so.get("ACCEPTED", 0)} 條的完整原句獲得支持。

## 第三階段：修正句獨立驗證 {{#sec-r-stage3}}

前兩階段共產生 {n(st["rewrite_proposals"])} 個修正版本，對應 {n(cat["revision_parents"])} 條原敘述。到目前為止已驗證三批：

| 批次 | 範圍 | 驗證數 | 新句通過 | 其他結果 |
|---|---|---:|---:|---|
| revision-pilot-001 | 六類風險各 5 條 | {pilot["reviewed"]} | {pilot["accepted_revisions"]} | {"、".join(f"{zh.get(k, k)} {v}" for k, v in pilot["verdicts"].items() if k != "REVISED_SUPPORTED")} |
| revision-aero-001 | 航太與國防全部待驗修正句 | {a1["reviewed"]} | {a1["verdicts"].get("REVISED_SUPPORTED", 0)} | {"、".join(f"{zh.get(k, k)} {v}" for k, v in a1["verdicts"].items() if k != "REVISED_SUPPORTED")} |
| revision-aero-002 | 上一批提出的較窄替代句 | {a2["reviewed"]} | {a2["verdicts"].get("REVISED_SUPPORTED", 0)} | {"、".join(f"{zh.get(k, k)} {v}" for k, v in a2["verdicts"].items() if k != "REVISED_SUPPORTED")} |

新句通過與原句通過分開計算：前者是改寫後的文字在其明示的範圍內成立，不代表原報告的原句正確。

在航太與國防產業，{len(all_parents)} 條被選入查核的原敘述中，有 {len(passed_parents)} 條至少有一個修正版本通過。試批次是依風險類別選樣，航太批次則是單一產業的全部敘述，兩者的通過比例都不能推論到全部 {n(cat["revision_parents"])} 條。

## 示範產業 {{#sec-r-demo}}

航太與國防產業的研究結果見產業專章與 10 家公司研究頁。該章所有事實都來自[證據附錄](../../appendices/evidence.qmd)列出的已驗證事實、年報數據與關係紀錄。
'''
    out = SITE / 'chapters/main/results.qmd'
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(md, encoding='utf-8')
    print('aero parents', len(all_parents), 'passed', len(passed_parents))


if __name__ == '__main__':
    main()
