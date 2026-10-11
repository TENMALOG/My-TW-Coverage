#!/usr/bin/env python3
"""Write a readable review and draft index from validated pilot outputs."""
import json
from collections import Counter, defaultdict
from pathlib import Path
import run_final_adjudication as controller

ROOT = Path(__file__).resolve().parent/'revision-pilot-001'


def read(path):
    return [json.loads(x) for x in path.read_text().splitlines() if x.strip()]


def main():
    summary = json.loads((ROOT/'delivery/summary.json').read_text())
    queue = {x['claim_id']: x for x in read(ROOT/'queue.jsonl')}
    accepted = {x['revision_id']: x for x in read(ROOT/'delivery/accepted-revisions.jsonl')}
    draft = json.loads((ROOT/'delivery/draft-manifest.json').read_text())
    drafts = {cid: f for f in draft['files'] for cid in f['revision_ids']}
    grouped = defaultdict(list)
    for row in read(ROOT/'delivery/pilot-outcomes.jsonl'):
        grouped[row['category']].append(row)
    lines = ['# 修正句試批次審查結果', '',
        f"本批次範圍為 30 筆修正提案、29 家公司。已完成模型研究 {summary['reviewed']} 筆；其中 {summary['accepted_revisions']} 筆修正句通過來源複核，尚有 {summary['remaining_reviews']} 筆未取得模型結果。", '',
        '評估基準日：2026-10-08。原文最終 ACCEPTED 仍為 28 筆；新修正句通過不改變父 claim。', '',
        f"批次完成：{'是' if summary['complete'] else '否'}。草稿數：{draft['draft_count']}。", '',
        '草稿保留其餘原報告內容，但本批次僅驗證所列修正句。原始報告未覆寫，財務概況逐 byte 保留。', '',
        '6908 原檔名與標題已有名稱亂碼；本索引依來源列為「宏碁遊戲」，連結保留實際檔名。', '',
        '## 各類結果', '', '| 類別 | 結果 |', '|---|---|']
    for cat, rows in grouped.items():
        counts = Counter(r['verdict'] for r in rows)
        lines.append('| '+cat+' | '+'、'.join(k+' '+str(v) for k,v in counts.items())+' |')
    lines += ['', '## 逐筆修正與草稿', '']
    for cat, rows in grouped.items():
        lines += ['### '+cat, '']
        for row in rows:
            cid = row['claim_id']; item = queue[cid]
            company = '宏碁遊戲' if item['issuer_ticker']=='6908' else item['issuer_company']
            lines += ['#### '+item['issuer_ticker']+' '+company, '',
                '**結果：** '+row['verdict'], '',
                '**提案：** '+item['original_text'], '']
            if cid in accepted:
                lines += ['**來源複核：** '+accepted[cid]['primary_source_review']['review_basis'], '']
                if cid in drafts:
                    f = drafts[cid]
                    lines += ['[報告草稿](<'+str(controller.BASE/f['draft_path'])+'>) · [修改差異](<'+str(controller.BASE/f['diff_path'])+'>)', '']
            elif row.get('rationale'):
                lines += ['**保留問題：** '+row['rationale'], '']
                if row.get('alternative_text'):
                    lines += ['**待另案複核的替代句：** '+row['alternative_text'], '',
                              '替代句尚未独立通過，未採入草稿。', '']
            else:
                lines += ['尚未取得可驗證的獨立模型結果。', '']
    lines += ['## 產物與完整性', '',
        '[修正登記表](<'+str(ROOT/'delivery/change-register.jsonl')+'>) · '+
        '[完整判決](<'+str(ROOT/'delivery/pilot-outcomes.jsonl')+'>) · '+
        '[待處理問題](<'+str(ROOT/'delivery/remaining-issues.json')+'>)', '',
        f"保護檔案檢查：{summary['protected_integrity']['protected_count']} 個檔案，異動 {len(summary['protected_integrity']['mismatches'])} 個。", '',
        '本批次結果用於決定下一輪修正句複核方式；其餘全量提案仍須獨立驗證，不自動採用。', '']
    output = ROOT/'delivery/review-summary.md'
    output.write_text('\n'.join(lines).replace('尚未独立','尚未獨立'), encoding='utf-8')
    print(output)


if __name__=='__main__':
    main()
