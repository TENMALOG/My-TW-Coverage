"""Build the errata (勘誤表) for the original project Pilot_Reports (Timeverse/My-TW-Coverage fork).

  python research-site/ops/errata/build_errata.py

Writes research-site/errata/:
  names.csv           company names in the original filenames that are wrong (mojibake, a split 堃, renamed companies)
  classification.csv  industry classes contradicted by the annual report (from data/industry-corrections.csv)
  claims.csv          high-risk sentences of the original reports that were checked against primary sources:
                      original text, verdict, the corrected sentence that passed review, period, evidence basis
  README.md           counts and how to read the tables
Every row is backed by a verified annual-report fact id or a recorded review verdict; nothing is inferred.
"""
import csv
import json
from collections import Counter
from pathlib import Path

SITE = Path(__file__).resolve().parents[2]
OUT = SITE / 'errata'

VERDICT_ZH = {
    'ACCEPTED': '原句通過', 'PARTIAL': '部分支持', 'PARTIALLY_SUPPORTED': '部分支持', 'UNSUPPORTED': '不支持',
    'UNKNOWN': '無法證實', 'UNKNOWN_AFTER_RESEARCH': '補查後仍無法證實', 'PERIOD_UNRESOLVED': '期間無法確定',
}
FINAL_ZH = {
    'REVISED_SUPPORTED': '更正句經一手資料證實', 'PARTIALLY_SUPPORTED': '更正句仍僅部分支持',
    'UNKNOWN_AFTER_RESEARCH': '補查後仍無法證實', 'PRIMARY_REVIEW_FAILED': '一手資料覆核未通過',
    'UNSUPPORTED': '不支持', '': '原句通過，無須更正',
}


def write(name, header, rows):
    with open(OUT / name, 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)
    return len(rows)


def names(cat):
    renames = json.loads((SITE / 'data/company-renames.json').read_text(encoding='utf-8'))
    rows = []
    for r in cat:
        orig = r['report_path'].rsplit('/', 1)[1][:-3].split('_', 1)[1]
        if orig == r['company']:
            continue
        hist = [x for x in renames.get(r['ticker'], []) if x.get('former_name')]
        if '�' in orig or any(ord(c) > 0xF000 for c in orig):
            kind, note = '檔名亂碼', '原檔名含亂碼字元（Big5 轉換時遺失「碁」「恒」等字）'
        elif '方土' in orig:
            kind, note = '缺字拆字', '「堃」不在 Big5 字集，公開資訊觀測站寫作「(方方土)」，原檔名將其拆開'
        else:
            kind = '已更名未更新'
            note = '；'.join(f"{x.get('date_text', '')}由「{x['former_name']}」更名為「{x.get('new_name', '')}」" for x in hist) \
                or '依 2025 年度財務資料，公司現行簡稱已不同於原檔名'
        rows.append([r['ticker'], orig, r['company'], kind, note])
    return write('names.csv', ['股票代號', '原專案名稱', '正確名稱', '錯誤類型', '說明與依據'], rows)


def classification():
    p = SITE / 'data/industry-corrections.csv'
    zh = {r['industry_folder']: r['name_zh'] for r in csv.DictReader(open(SITE / 'data/industry-names.csv', encoding='utf-8-sig'))}
    rows = [[r['ticker'], r['company'], f"{zh.get(r['original_folder'], '')}（{r['original_folder']}）",
             f"{zh.get(r['corrected_folder'], '')}（{r['corrected_folder']}）", r['reason'], r['facts'].replace(';', '、')]
            for r in csv.DictReader(open(p, encoding='utf-8-sig'))]
    return write('classification.csv', ['股票代號', '公司', '原專案分類', '更正分類', '理由', '依據的年報事實編號'], rows)


def claims():
    rows, stats = [], Counter()
    for r in csv.DictReader(open(SITE / 'catalog/release-scope-claims.csv', encoding='utf-8-sig')):
        v = VERDICT_ZH.get(r['parent_verdict'], r['parent_verdict'])
        fin = FINAL_ZH.get(r['revision_final_verdict'], r['revision_final_verdict'])
        stats[v] += 1
        corrected = r['adoptable_text'] if r['revision_final_verdict'] == 'REVISED_SUPPORTED' else ''
        rows.append([r['ticker'], r['company'], r['claim_type'], r['original_text'], v, corrected, fin,
                     r['period_note'], r['adoption_basis'], r['claim_id']])
    n = write('claims.csv', ['股票代號', '公司', '敘述類型', '原專案原句', '原句查核結果', '更正後敘述', '更正句結果',
                             '資料期間', '依據', '主張編號'], rows)
    return n, stats


def site_page(n_names, n_cls, n_claims, stats):
    """appendices/errata.qmd: the readable errata on the site (tables for names and classes, CSV downloads)."""
    def table(name, link_col=1):
        rows = list(csv.reader(open(OUT / name, encoding='utf-8-sig')))
        head, body = rows[0], rows[1:]
        out = ['| ' + ' | '.join(head) + ' |', '|' + '---|' * len(head)]
        for r in body:
            cells = [c.replace('|', '／').replace('*', '＊') for c in r]   # literal text (md_escape would rewrite 「(方方土)」)
            cells[link_col] = f'[{cells[link_col]}](../chapters/companies/{r[0]}.qmd)'
            out.append('| ' + ' | '.join(cells) + ' |')
        return out

    L = ['---', 'title: "原專案勘誤表"', '---', '',
         f'<!-- 由 research-site/ops/errata/build_errata.py 產生；請勿手動修改。 -->', '',
         '本附錄列出原專案（Timeverse/My-TW-Coverage，MIT 授權）`Pilot_Reports` 公司報告中，經本研究以 2025 年度年報及'
         '一手資料核對後確認的錯誤。每一筆都附可回查的依據；完整資料可下載 CSV。', '',
         '| 類別 | 筆數 | 下載 |', '|---|---|---|',
         f'| 公司名稱錯誤（亂碼、缺字、已更名未更新） | {n_names} | [names.csv](../errata/names.csv) |',
         f'| 產業分類與年報主要業務不符 | {n_cls} | [classification.csv](../errata/classification.csv) |',
         f'| 高風險敘述逐句查核（原句與更正句） | {n_claims:,} | [claims.csv](../errata/claims.csv) |', '',
         '## 公司名稱 {#sec-errata-names}', ''] + table('names.csv', 2) + [
         '', '## 產業分類 {#sec-errata-classes}', '',
         '判定標準：年報明載的主要業務或最大營收部門明確不屬於原分類，且有明顯更貼切的分類才列入；兩個相鄰分類都說得通、'
         '業務橫跨多業或缺少營收占比者，一律維持原分類。依據欄為年報事實編號，可在各公司頁的註腳回查頁碼。', ''] + \
        table('classification.csv') + [
         '', '## 高風險敘述 {#sec-errata-claims}', '',
         '原報告中風險最高的敘述（排名或市占、客戶與供應商關係、沿革與組織變更等）逐句以一手資料重查，原句結果如下：', '',
         '| 原句查核結果 | 句數 |', '|---|---|'] + [f'| {k} | {v} |' for k, v in stats.most_common()] + [
         '', '「部分支持」表示原句有一部分與一手資料不符或無法證實（範圍、期間、排名說法等）。逐句的原句、更正句與依據見 '
         '[claims.csv](../errata/claims.csv)；更正句沒有通過證實者，原句不應引用。其餘未列入查核範圍的原句並不因此被視為正確。', '']
    (SITE / 'appendices/errata.qmd').write_text('\n'.join(L), encoding='utf-8', newline='\n')


def main():
    OUT.mkdir(exist_ok=True)
    cat = list(csv.DictReader(open(SITE / 'catalog/release-scope-companies.csv', encoding='utf-8-sig')))
    n_names = names(cat)
    n_cls = classification()
    n_claims, stats = claims()
    lines = [
        '# 原專案勘誤表',
        '',
        '對象：原專案 Timeverse/My-TW-Coverage（MIT 授權）的 `Pilot_Reports` 公司報告（1,733 家）。',
        '依據：各公司 2025 年度年報（公開資訊觀測站）及逐句查核紀錄；每一筆勘誤都附可回查的依據。',
        '',
        '| 表 | 內容 | 筆數 |',
        '|---|---|---|',
        f'| `names.csv` | 公司名稱錯誤（亂碼、缺字、已更名未更新） | {n_names} |',
        f'| `classification.csv` | 產業分類與年報主要業務不符 | {n_cls} |',
        f'| `claims.csv` | 高風險敘述（排名、市占、客戶、供應商、沿革等）逐句查核 | {n_claims} |',
        '',
        '## 高風險敘述的查核結果（原句）',
        '',
        '| 結果 | 句數 |',
        '|---|---|',
    ] + [f'| {k} | {v} |' for k, v in stats.most_common()] + [
        '',
        '「部分支持」表示原句有一部分與一手資料不符或無法證實（例如範圍、期間、排名說法），`更正後敘述` 欄是經一手資料證實的改寫；',
        '空白表示沒有通過證實的更正句，該原句不應引用。',
        '',
        '查核範圍說明：`claims.csv` 只涵蓋原報告中風險最高的敘述類型；其餘敘述未逐句比對，'
        '本專案改以年報重新整理每家公司的事實，不代表其餘原句皆正確。',
    ]
    (OUT / 'README.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
    site_page(n_names, n_cls, n_claims, stats)
    print(f'names {n_names}, classification {n_cls}, claims {n_claims}', dict(stats))


if __name__ == '__main__':
    main()
