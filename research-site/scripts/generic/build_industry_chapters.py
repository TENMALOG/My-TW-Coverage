"""Generate one industry chapter per industry folder (except the hand-written Aerospace & Defense).

Content: scope, company table, revenue/margin statistics (一般業 tables only), named-relationship
sentences (claim_type 具名客戶／供應關係) with footnoted sources, 研究限制 counts.
A hand-written analysis chapters/industries/_analysis/{slug}.qmd is included after the introduction
when it exists; otherwise nothing is inserted.

  python research-site/scripts/generic/build_industry_chapters.py [--industry FOLDER ...]
"""
from __future__ import annotations

import argparse
import statistics
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from industries import (AERO_FOLDER, ASSESSMENT, FACTS_DIR, SITE, claims, companies, fmt_m,  # noqa: E402
                        fmt_pct, industry_names, load_financials, load_verified, md_escape, mops_industry,
                        ordered_industries)
from build_company_pages_all import Notes, industry_corrections, page_name, public_citations, sentence_note  # noqa: E402

OUTDIR = SITE / 'chapters/industries'
ANALYSIS = OUTDIR / '_analysis'
GENERATOR = 'research-site/scripts/generic/build_industry_chapters.py'
REL_TYPE = '具名客戶／供應關係'
NOT_PASSED_PREFIX = '新句未通過'


def general_2025(fin):
    y = (fin or {}).get('years', {}).get('2025')
    if y and y['table_kind'] == '一般業' and (y['items_k'].get('營業收入') or 0) > 0:
        return y
    return None


def fmt_num(v, digits=2):
    return f'{v:,.{digits}f}'


def stats_rows(fins_in: list[dict]) -> list[str]:
    revs = [general_2025(f)['items_k']['營業收入'] for f in fins_in if general_2025(f)]
    gms = [general_2025(f)['gross_margin_pct'] for f in fins_in
           if general_2025(f) and general_2025(f).get('gross_margin_pct') is not None]
    oms = [general_2025(f)['operating_margin_pct'] for f in fins_in
           if general_2025(f) and general_2025(f).get('operating_margin_pct') is not None]
    growth = []
    for f in fins_in:
        y5, y4 = general_2025(f), (f or {}).get('years', {}).get('2024')
        if y5 and y4 and y4['table_kind'] == '一般業' and (y4['items_k'].get('營業收入') or 0) > 0:
            growth.append((y5['items_k']['營業收入'] / y4['items_k']['營業收入'] - 1) * 100)
    if not revs:
        return []

    def q(xs):
        if len(xs) < 4:
            return '—', '—'
        qs = statistics.quantiles(xs, n=4, method='inclusive')
        return qs[0], qs[2]

    L = ['| 指標（2025 年度） | 家數 | 中位數 | 第 1 四分位數 | 第 3 四分位數 | 最小值 | 最大值 |',
         '|---|---:|---:|---:|---:|---:|---:|']
    q1, q3 = q([r / 1000 for r in revs])
    L.append(f'| 營業收入（百萬元） | {len(revs)} | {fmt_m(statistics.median(revs))} | '
             f'{q1 if q1 == "—" else fmt_num(q1, 0)} | {q3 if q3 == "—" else fmt_num(q3, 0)} | '
             f'{fmt_m(min(revs))} | {fmt_m(max(revs))} |')
    for label, xs in (('毛利率（%）', gms), ('營業利益率（%）', oms), ('營收年增率（%，2025 對 2024）', growth)):
        if xs:
            a, b = q(xs)
            L.append(f'| {label} | {len(xs)} | {fmt_num(statistics.median(xs))} | '
                     f'{a if a == "—" else fmt_num(a)} | {b if b == "—" else fmt_num(b)} | '
                     f'{fmt_num(min(xs))} | {fmt_num(max(xs))} |')
    L.append(f'\n合計營業收入 {fmt_m(sum(revs))} 百萬元（{len(revs)} 家加總）。')
    return L


def render_chapter(folder: str, rows: list[dict], *, names: dict, fins: dict, verified: dict,
                   claim_rows: list[dict], analysis_dir: Path = ANALYSIS) -> str:
    info = names[folder]
    zh, slug = info['name_zh'], info['slug']
    notes = Notes()
    rows = sorted(rows, key=lambda r: r['ticker'])
    corrected = industry_corrections()
    n_in = sum(1 for r in rows if r['ticker'] in corrected)
    fin_mark = notes.add('公開資訊觀測站「合併綜合損益表彙總（t163sb04，第四季＝全年度）」，民國 113、114 年度；'
                         '單位新臺幣仟元，本章換算為百萬元（四捨五入）。<https://mopsov.twse.com.tw/mops/web/ajax_t163sb04>')
    L = [f'---\ntitle: "{zh}"\n---\n', f'<!-- 由 {GENERATOR} 產生；請勿手動修改。 -->\n',
         '## 研究範圍與資料截止 {.unnumbered}\n',
         f'本章涵蓋「{md_escape(zh)}」產業的 {len(rows)} 家上市櫃公司（原專案英文分類「{md_escape(folder)}」），資料截止日 {ASSESSMENT}。'
         + (f'其中 {n_in} 家的產業分類由本研究依年報更正後移入，於下表以＊標示，更正理由見各公司頁與原專案勘誤表。' if n_in else '')
         + 
         '本章及各公司研究頁只使用三類資料：公開資訊觀測站的綜合損益表彙總、經逐條查核通過的敘述，以及經逐字核對的年報事實；'
         '未通過查核的原報告敘述只計入研究限制，不列入正文。\n']
    if (analysis_dir / f'{slug}.qmd').exists():
        L += [f'{{{{< include _analysis/{slug}.qmd >}}}}', '']

    # company table
    L += ['## 公司一覽 {.unnumbered}\n',
          f'營業收入與毛利率取自 2025 年度綜合損益表彙總{fin_mark}；採銀行、保險、證券等其他報表格式的公司不列毛利率。'
          '「已驗證敘述」為經查核通過且有公開來源的敘述條數。\n',
          '| 代號 | 公司 | 2025 營業收入（百萬元） | 2025 毛利率 | 已驗證敘述 |', '|---|---|---:|---:|---:|']
    for r in rows:
        tk, fin = r['ticker'], fins.get(r['ticker'])
        name, _ = page_name(r, fin)
        y = general_2025(fin)
        rev = fmt_m(y['items_k']['營業收入']) if y else '—'
        gm = fmt_pct(y.get('gross_margin_pct')) if y else '—'
        n = sum(1 for s in verified.get(tk, []) if public_citations(s))
        star = '＊' if tk in corrected else ''
        mops = mops_industry(tk)[0] or '已停止公開發行'
        L.append(f'| {tk} | [{md_escape(name)}](../companies/{tk}.qmd){star} | {md_escape(mops)} | {rev} | {gm} | {n} |')
    L.append('')

    # statistics
    L.append('## 營收與獲利概況 {.unnumbered}\n')
    st = stats_rows([fins.get(r['ticker']) for r in rows])
    if st:
        L.append(f'下表只計入 2025 年度採一般業格式、且營業收入大於零的公司；各列家數可能不同。'
                 f'中位數與四分位數為本章計算的描述統計，不代表產業整體規模。{fin_mark}\n')
        L += st
    else:
        L.append('本產業沒有採一般業格式且有 2025 年度營業收入的公司，因此不計算營收與毛利統計。')
    L.append('')

    # named relationships
    rel = [(r, s) for r in rows for s in verified.get(r['ticker'], [])
           if s['claim_type'] == REL_TYPE and public_citations(s)]
    L.append('## 已驗證的具名客戶與供應關係 {.unnumbered}\n')
    if rel:
        L += ['| 公司 | 敘述 |', '|---|---|']
        for r, s in rel:
            name, _ = page_name(r, fins.get(r['ticker']))
            L.append(f'| [{r["ticker"]} {md_escape(name)}](../companies/{r["ticker"]}.qmd) | '
                     f'{md_escape(s["text"])}{notes.add(sentence_note(s))} |')
    else:
        L.append('本產業目前沒有經查核通過的具名客戶或供應關係敘述。')
    L.append('')

    # reviewed listed-company relation graph (scripts/generic/build_industry_relation_graphs.py)
    if (OUTDIR / '_relations' / f'{slug}.qmd').exists():
        L += ['## 上市櫃公司之間的年報關係 {.unnumbered}\n', f'{{{{< include _relations/{slug}.qmd >}}}}', '']

    # limitations
    tks = {r['ticker'] for r in rows}
    mine = [c for c in claim_rows if c['ticker'] in tks]
    passed = [c for c in mine if c['adoptable_text'].strip()]
    failed = [c for c in mine if c['revision_status'].startswith(NOT_PASSED_PREFIX)]
    with_fin = sum(1 for t in tks if fins.get(t) and fins[t].get('years'))
    general = sum(1 for t in tks if general_2025(fins.get(t)))
    with_sent = sum(1 for t in tks if any(public_citations(s) for s in verified.get(t, [])))
    facts_files = sum(1 for t in tks if (FACTS_DIR / f'{t}.json').exists())
    L += ['## 研究限制 {.unnumbered}\n',
          f'- 本產業 {len(rows)} 家公司中，{with_fin} 家有 2024 或 2025 年度財務彙總資料，'
          f'{general} 家有可計算毛利率的 2025 年度一般業資料。',
          f'- 原報告有 {len(mine)} 條敘述被選入查核，{len(passed)} 條有可採用的版本，{len(failed)} 條經兩輪查核仍未通過。',
          f'- {with_sent} 家公司至少有一條已驗證敘述；其餘公司的研究頁只有財務數字與資料缺口說明。',
          f'- {facts_files} 家公司已有年報事實檔；年報事實只採用逐字核對通過的條目。',
          '- 公司分類沿用原專案的英文產業資料夾，未依營收結構重新歸類；跨產業經營的公司只出現在一個產業。',
          '- 統計只描述本研究涵蓋的上市櫃公司，不含未上市櫃業者與海外同業。', '']
    if notes.items:
        L += notes.render() + ['']
    return '\n'.join(L)


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument('--industry', nargs='*', default=None)
    a = ap.parse_args(argv)
    names = industry_names()
    all_rows = companies()
    order = [f for f, _ in ordered_industries(all_rows)]
    if a.industry:
        unknown = set(a.industry) - set(order)
        if unknown:
            raise SystemExit(f'unknown industry folder(s): {sorted(unknown)}')
        order = [f for f in order if f in a.industry]
    fins, verified, claim_rows = load_financials(), load_verified(), claims()
    OUTDIR.mkdir(parents=True, exist_ok=True)
    written = 0
    for folder in order:
        if folder == AERO_FOLDER:
            continue
        rows = [r for r in all_rows if r['industry_folder'] == folder]
        text = render_chapter(folder, rows, names=names, fins=fins, verified=verified, claim_rows=claim_rows)
        (OUTDIR / f'{names[folder]["slug"]}.qmd').write_text(text, encoding='utf-8', newline='\n')
        written += 1
    print(f'industry chapters written {written} (Aerospace & Defense left to the hand-written chapter)')


if __name__ == '__main__':
    main()
