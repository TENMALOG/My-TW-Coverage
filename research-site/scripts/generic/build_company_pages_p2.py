"""Generate the P2 section (研究完整版 P2: companies outside the original catalog), grouped by the official 證交所產業別.

Chairman 2026-10-26 (option A): a separate section grouped by the MOPS / TWSE industry classification; the companies
are not mapped into the 99 industry folders. The catalog CSVs and research-site/_quarto.yml are never touched.

Inputs (read-only):
  ops/full-coverage-p2/batches/b01..b13.json             the 608 P2 companies
  data/official-directory.json + its cached ISIN lists    market, industry code and its official name
  ops/full-coverage-p2/out/b*/financials.json             2024/2025 income-statement summaries
  data/company-facts/{ticker}.json + out/b*/review/final-adjudication.jsonl              annual-report facts
  data/company-facts-prospectus/{ticker}.json + prospectus/review/final-adjudication.jsonl  prospectus facts (rules v2)
A fact is rendered only when its mechanical verification is PASS and its final adjudication is ACCEPT
(and it is not in data/company-facts/_semantic-review.jsonl as REJECT).

Outputs: chapters/p2/index.qmd, chapters/p2/industry-{code}.qmd, chapters/p2/{ticker}.qmd,
_generated/p2-book-parts.json, _generated/_quarto-with-p2.yml (a copy of _quarto.yml with the P2 section inserted
before the company index) and _generated/p2-pages-build-log.jsonl.

  python research-site/scripts/generic/build_company_pages_p2.py [--tickers T ...] [--check]

--check (run by check_site.py) writes nothing: it regenerates every page in memory and fails when a page on disk
differs or research-site/_quarto.yml does not list exactly the generated P2 section.
"""
from __future__ import annotations

import argparse
import glob
import html
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

import build_company_pages_all as base
from industries import ROOT, SITE, md_escape, roc_year

P2 = SITE / 'ops/full-coverage-p2'
PROSPECTUS = P2 / 'prospectus'
OUTDIR = SITE / 'chapters/p2'
PARTS = SITE / '_generated/p2-book-parts.json'
QUARTO_COPY = SITE / '_generated/_quarto-with-p2.yml'
LOG = SITE / '_generated/p2-pages-build-log.jsonl'
GENERATOR = 'research-site/scripts/generic/build_company_pages_p2.py'
ASSESSMENT = '2026-10-26'
DIRECTORY = SITE / 'data/official-directory.json'
DIRECTORY_CACHE = ROOT / 'audit-v5/source-cache/research-site/official-directory'

# Companies without deployable facts and why (artifacts/full-coverage-p2-20261024/PROGRESS.md, 2026-10-26).
UNRESOLVED = {
    **{t: '年報文字層為亂碼（PyMuPDF、pdfminer、pdftotext 皆無法讀取），依規定不做 OCR'
       for t in ('4570', '6518', '6539', '6912', '7829')},
    **{t: '公開資訊觀測站上查無年報，正式版公開說明書為掃描影像、沒有文字層，依規定不做 OCR' for t in ('7913', '7950')},
    **{t: '公開資訊觀測站上查無年報，公開說明書只有稿本，依規定不採用'
       for t in ('7422', '7686', '7898', '7946', '7951', '7954', '7960')},
    **{t: '公開資訊觀測站上查無年報，公開說明書雖列為正式版，但封面或摘要頁載明為稿本，依規定不採用'
       for t in ('7918', '7927', '7930', '7932', '7934', '7935', '7936', '7942')},
}


def jsonl(path):
    p = Path(path)
    return [json.loads(l) for l in p.read_text(encoding='utf-8').splitlines() if l.strip()] if p.exists() else []


def p2_companies() -> list[dict]:
    rows = []
    for b in range(1, 14):
        rows += json.loads((P2 / 'batches' / f'b{b:02d}.json').read_text(encoding='utf-8'))
    return rows


def industry_names_official(directory: dict) -> tuple[dict, dict]:
    """({code: name}, {ticker: name for ISIN-only rows}) from the cached TWSE ISIN lists: each code takes the industry
    name the ISIN list shows for the companies the basic data files under that code (one name per code is asserted)."""
    seen: dict[str, set] = defaultdict(set)
    isin_only = {}
    for key in ('isin_2', 'isin_4'):
        meta = json.loads((DIRECTORY_CACHE / f'{key}.json').read_text(encoding='utf-8'))
        text = (ROOT / meta['raw_path']).read_bytes().decode('big5hkscs', errors='replace')
        for row in re.findall(r'<tr>(.*?)</tr>', text, re.S):
            cells = [html.unescape(re.sub(r'<[^>]+>', '', c)).strip() for c in re.findall(r'<td[^>]*>(.*?)</td>', row, re.S)]
            if len(cells) < 5 or not cells[4]:
                continue
            tk = cells[0].replace('　', ' ').split(' ')[0].strip()
            d = directory.get(tk)
            if not d:
                continue
            if d.get('industry_code'):
                seen[d['industry_code']].add(cells[4])
            elif d.get('source', '').startswith('isin'):
                isin_only[tk] = cells[4]
    clash = {k: v for k, v in seen.items() if len(v) > 1}
    if clash:
        raise SystemExit(f'industry code maps to several ISIN names: {clash}')
    return {k: next(iter(v)) for k, v in seen.items()}, isin_only


def load_financials() -> dict:
    out = {}
    for f in sorted(glob.glob(str(P2 / 'out/b*/financials.json'))):
        for r in json.loads(Path(f).read_text(encoding='utf-8')):
            if r.get('years'):
                out[r['ticker']] = r
    return out


def accepted_ids() -> set:
    ids = set()
    files = glob.glob(str(P2 / 'out/b*/review/final-adjudication.jsonl')) + [str(PROSPECTUS / 'review/final-adjudication.jsonl')]
    for f in files:
        ids |= {r['id'] for r in jsonl(f) if r['final'] == 'ACCEPT'}
    return ids


def load_facts(ticker: str, short: str, accepted: set):
    """-> (doc or None, kind 'annual'|'prospectus'|None, shown facts, withheld count, gate reasons)."""
    for kind, folder in (('annual', SITE / 'data/company-facts'), ('prospectus', SITE / 'data/company-facts-prospectus')):
        path = folder / f'{ticker}.json'
        if not path.exists():
            continue
        doc = json.loads(path.read_text(encoding='utf-8'))
        if not doc.get('facts'):
            continue
        probs = base.identity_problems(doc, ticker, short)
        if probs:
            return None, kind, [], 0, probs
        rejected = base.semantic_rejects()
        ok = [f for f in doc['facts'] if (f.get('verification') or {}).get('status') == 'PASS'
              and f['id'] in accepted and f['id'] not in rejected]
        return doc, kind, ok, len(doc['facts']) - len(ok), []
    return None, None, [], 0, []


def source_label(doc: dict, kind: str) -> str:
    """Chairman 2026-10-26: 「資料來源：公開說明書（YYYY 年 M 月，{doc_label}）」 for prospectus facts."""
    s = doc['source']
    if kind == 'prospectus':
        y, m = s['filed_month'].split('-')
        return f'公開說明書（{y} 年 {int(m)} 月，{md_escape(s["doc_label"])}）'
    return f'{s["fy"]} 年度（民國 {roc_year(s["fy"])} 年度）年報'


def fact_note(doc: dict, kind: str, fact: dict | None) -> str:
    s = doc['source']
    head = f'{md_escape(doc["legal_name"])} {source_label(doc, kind)}'
    if fact is None:
        return f'{head}（{md_escape(s["filename"])}）。{base.url_md(s["citation_url"])}'
    return (f'{head}，第 {fact["page"]} 頁（{md_escape(s["filename"])}）；期間：{md_escape(fact["period"])}。'
            f'{base.url_md(s["citation_url"])}')


def render_facts(doc, kind, facts, fields, notes) -> list[str]:
    plain = '公司公開說明書揭露' if kind == 'prospectus' else '公司年報揭露'
    L = []
    for field in fields:
        for f in [x for x in facts if x.get('field') == field]:
            attr = f.get('attribution', '')
            tag = '' if attr == plain else f'（{md_escape(attr)}）'
            L.append(f'- **{base.FIELD_ZH[field]}**：{md_escape(f["statement"])}{tag}{notes.add(fact_note(doc, kind, f))}')
    return L


def render_page(row, d, ind_code, ind_name, fin, facts_result) -> tuple[str, dict]:
    tk, name = row['ticker'], row['company']
    doc, kind, facts, withheld, gate = facts_result
    notes = base.Notes()
    title = f'{tk} {name}'.replace('"', '\\"')
    legal = (doc or {}).get('legal_name') or d.get('legal_name') or ''
    subtitle = legal.replace('"', '\\"')
    L = [f'---\ntitle: "{title}"\n' + (f'subtitle: "{subtitle}"\n' if legal else '') + '---\n',
         f'<!-- 由 {GENERATOR} 產生；請勿手動修改。 -->\n',
         f'本頁整理{md_escape(name)}（股票代號 {tk}，{md_escape(d["market"])}，證交所產業別'
         f'[{md_escape(ind_name)}](industry-{ind_code}.qmd)）經機械核對與兩輪語意審查通過的公開資料，資料截止日 {ASSESSMENT}。'
         f'未通過審查的內容不列入正文，只在資料缺口中計數。\n']
    if doc:
        L.append(f'::: {{.callout-note appearance="minimal"}}\n資料來源：{source_label(doc, kind)}'
                 + ('。本公司在公開資訊觀測站上尚無年報，本頁事實取自公司申報的公開說明書（正式版），不是年報。' if kind == 'prospectus' else '。')
                 + '\n:::\n')
    dir_note = notes.add(f'臺灣證券交易所、證券櫃檯買賣中心公司基本資料與 ISIN 清單（official-directory，資料日 '
                         f'{json.loads(DIRECTORY.read_text(encoding="utf-8"))["as_of"]}）。')
    # 1. basic data
    L.append('## 公司基本資料 {.unnumbered}\n')
    L.append(f'- **股票代號**：{tk}')
    L.append(f'- **市場別**：{md_escape(d["market"])}{dir_note}')
    L.append(f'- **證交所產業別**：{md_escape(ind_name)}')
    if doc:
        L.append(f'- **公司全名**：{md_escape(doc["legal_name"])}{notes.add(fact_note(doc, kind, None))}')
    elif d.get('legal_name'):
        L.append(f'- **公司全名**：{md_escape(d["legal_name"])}')
    basic = render_facts(doc, kind, facts, base.SECTION_FIELDS['basic'], notes) if doc else []
    L += basic + ['']
    # 2. products
    L.append('## 產品與營收結構 {.unnumbered}\n')
    prod = render_facts(doc, kind, facts, base.SECTION_FIELDS['products'], notes) if doc else []
    L += prod if prod else ['目前沒有已驗證的產品或營收結構資料。']
    L.append('')
    # 3. financials
    L.append('## 財務摘要 {.unnumbered}\n')
    gaps = []
    if fin and fin.get('years'):
        L += base.fin_table(fin, notes)
    else:
        L.append('公開資訊觀測站 2024、2025 年度綜合損益表彙總中查無本公司資料，本頁不列財務數字。')
        gaps.append('2024、2025 年度財務數字缺漏。')
    L.append('')
    # 4. customers / suppliers / market
    L.append('## 客戶、供應商與市場地位 {.unnumbered}\n')
    market = render_facts(doc, kind, facts, base.SECTION_FIELDS['market'], notes) if doc else []
    L += market if market else ['目前沒有已驗證的客戶、供應商或市場地位資料。']
    L.append('')
    # 5. gaps
    L.append('## 資料缺口 {.unnumbered}\n')
    if tk in UNRESOLVED:
        L.append(f'- 本公司沒有可採用的事實來源：{UNRESOLVED[tk]}。')
    elif doc is None and not gate:
        L.append('- 尚無經驗證的年報或公開說明書事實。')
    for g in gate:
        L.append(f'- 事實檔未通過身分核對，整份未採用：{md_escape(g)}。')
    if withheld:
        L.append(f'- 事實檔中有 {withheld} 條事實未通過機械核對或兩輪語意審查，內容不列入本頁。')
    missing = [s for s, ok in (('公司基本資料（事實）', basic), ('產品與營收結構', prod), ('客戶、供應商與市場地位', market)) if not ok]
    if missing:
        L.append(f'- 缺少已驗證內容的段落：{"、".join(missing)}。')
    L += [f'- {g}' for g in gaps]
    if L[-1] == '## 資料缺口 {.unnumbered}\n':
        L.append('- 無。')
    L.append('')
    # 6. sources
    L.append('## 資料來源 {.unnumbered}\n')
    srcs = {}
    if doc:
        s = doc['source']
        srcs[s['citation_url']] = f'{md_escape(doc["legal_name"])} {source_label(doc, kind)}（公開資訊觀測站，{md_escape(s["filename"])}）'
    if fin and fin.get('years'):
        for y in sorted(fin['years']):
            u = (fin['years'][y].get('source') or {}).get('url')
            if u:
                srcs.setdefault(u, '公開資訊觀測站 綜合損益表彙總（t163sb04）')
    L += [f'- {label}：{base.url_md(u)}' for u, label in srcs.items()] or ['本頁沒有可列出的外部來源。']
    L.append('')
    if notes.items:
        L += notes.render() + ['']
    stats = {'ticker': tk, 'company': name, 'industry_code': ind_code, 'source_kind': kind if doc else None,
             'facts_shown': len(facts), 'facts_withheld': withheld, 'financials': bool(fin and fin.get('years')),
             'gate_reasons': gate, 'unresolved': UNRESOLVED.get(tk)}
    return '\n'.join(L), stats


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument('--tickers', nargs='*', default=None)
    ap.add_argument('--check', action='store_true', help='compare with the files on disk instead of writing')
    a = ap.parse_args(argv)
    differ = []

    def emit(path: Path, text: str):
        if a.check:
            if not path.exists() or path.read_text(encoding='utf-8') != text:
                differ.append(path.relative_to(SITE).as_posix())
        else:
            path.write_text(text, encoding='utf-8', newline='\n')
    directory = {c['ticker']: c for c in json.loads(DIRECTORY.read_text(encoding='utf-8'))['companies']}
    code_names, isin_only = industry_names_official(directory)
    rows = p2_companies()
    assert len(rows) == len({r['ticker'] for r in rows}) == 608, len(rows)
    fins, accepted = load_financials(), accepted_ids()
    OUTDIR.mkdir(parents=True, exist_ok=True)
    by_name = {v: k for k, v in code_names.items()}
    by_ind, stats_all = defaultdict(list), []
    for r in rows:
        tk = r['ticker']
        d = directory[tk]
        code = d.get('industry_code') or ''
        name = code_names.get(code) or isin_only.get(tk) or (f'產業代碼 {code}（官方資料未載名稱）' if code else '未分類')
        if not code:   # ISIN-only rows carry the industry name but no code: file them under that name's code
            code = by_name.get(name, 'unclassified')
        r = {**r, 'company': r.get('company') or d['short_name']}
        by_ind[(code, name)].append(r)
        if a.tickers and tk not in a.tickers:
            continue
        facts_result = load_facts(tk, r['company'], accepted)
        text, st = render_page(r, d, code, name, fins.get(tk), facts_result)
        emit(OUTDIR / f'{tk}.qmd', text)
        stats_all.append(st)
    stats = {s['ticker']: s for s in stats_all}
    if a.tickers:
        print(f'pages written {len(stats_all)} (partial run; index pages not rewritten)')
        return stats_all
    # industry pages, section index and book parts (largest industry first, as the main book does)
    order = sorted(by_ind.items(), key=lambda kv: (-len(kv[1]), kv[0][0]))
    parts = []
    for (code, name), members in order:
        members = sorted(members, key=lambda x: x['ticker'])
        n_ok = sum(1 for m in members if stats[m['ticker']]['facts_shown'])
        L = [f'---\ntitle: "新增公司：{name}"\n---\n', f'<!-- 由 {GENERATOR} 產生；請勿手動修改。 -->\n',
             f'證交所產業別「{md_escape(name)}」中，原研究目錄以外的 {len(members)} 家公司；其中 {n_ok} 家有經兩輪審查通過的事實。'
             '產業別取自臺灣證券交易所、證券櫃檯買賣中心的公司基本資料，本研究未另行判斷。\n',
             '| 代號 | 公司 | 市場別 | 事實來源 | 已通過事實 |', '|---|---|---|---|---:|']
        for m in members:
            s = stats[m['ticker']]
            src = {'annual': '年報', 'prospectus': '公開說明書', None: '—'}[s['source_kind']]
            L.append(f'| {m["ticker"]} | [{md_escape(m["company"])}]({m["ticker"]}.qmd) | {md_escape(directory[m["ticker"]]["market"])} '
                     f'| {src} | {s["facts_shown"]} |')
        emit(OUTDIR / f'industry-{code}.qmd', '\n'.join(L) + '\n')
        parts.append({'title': f'新增公司：{name}',
                      'chapters': [f'chapters/p2/industry-{code}.qmd'] + [f'chapters/p2/{m["ticker"]}.qmd' for m in members]})
    c = Counter(s['source_kind'] for s in stats_all)
    with_facts = sum(1 for s in stats_all if s['facts_shown'])
    idx = [f'---\ntitle: "新增公司（研究完整版 P2）"\n---\n', f'<!-- 由 {GENERATOR} 產生；請勿手動修改。 -->\n',
           f'本篇收錄原研究目錄以外的 {len(rows)} 家上市、上櫃、興櫃公司，依證交所產業別分組，共 {len(order)} 類。'
           f'事實取自公開資訊觀測站的年報；查無年報的新登錄興櫃公司，改用正式版公開說明書（頁面上會標明）。'
           f'每則事實都經過逐字與數字的機械核對，以及兩輪語意審查，資料截止日 {ASSESSMENT}。\n',
           f'- 有已通過事實的公司：{with_facts} 家（年報 {sum(1 for s in stats_all if s["facts_shown"] and s["source_kind"] == "annual")} 家、'
           f'公開說明書 {sum(1 for s in stats_all if s["facts_shown"] and s["source_kind"] == "prospectus")} 家）。',
           f'- 沒有可採用事實來源的公司：{len(rows) - with_facts} 家（原因列在各公司頁的資料缺口）。',
           f'- 有 2024／2025 年度財務摘要的公司：{sum(1 for s in stats_all if s["financials"])} 家。', '',
           '| 證交所產業別 | 公司數 | 有已通過事實 |', '|---|---:|---:|']
    for (code, name), members in order:
        idx.append(f'| [{md_escape(name)}](industry-{code}.qmd) | {len(members)} | '
                   f'{sum(1 for m in members if stats[m["ticker"]]["facts_shown"])} |')
    emit(OUTDIR / 'index.qmd', '\n'.join(idx) + '\n')
    # copy of research-site/_quarto.yml with the P2 section (re)inserted before the company index; since the
    # chairman's approval (2026-10-27) _quarto.yml itself carries the section, so in --check mode the two must match
    q = (SITE / '_quarto.yml').read_text(encoding='utf-8').splitlines()
    at = q.index('    - index-companies.qmd')
    start = q.index('    - chapters/p2/index.qmd') if '    - chapters/p2/index.qmd' in q else at
    block = ['    - chapters/p2/index.qmd']
    for p in parts:
        block += [f'    - part: "{p["title"]}"', '      chapters:'] + [f'        - {c}' for c in p['chapters']]
    merged = '\n'.join(q[:start] + block + q[at:]) + '\n'
    if a.check:
        if (SITE / '_quarto.yml').read_text(encoding='utf-8') != merged:
            differ.append('_quarto.yml (P2 section)')
        print(f'P2 pages regenerated in memory: {len(stats_all) + len(order) + 1}; differing from disk: {len(differ)} {differ[:5]}')
        if differ:
            raise SystemExit(1)
        return stats_all
    PARTS.write_text(json.dumps({'intro': 'chapters/p2/index.qmd', 'parts': parts}, ensure_ascii=False, indent=1),
                     encoding='utf-8')
    QUARTO_COPY.write_text(merged, encoding='utf-8', newline='\n')
    with open(LOG, 'w', encoding='utf-8', newline='\n') as fh:
        for s in stats_all:
            fh.write(json.dumps(s, ensure_ascii=False) + '\n')
    print(f'pages {len(stats_all)}; with shown facts {with_facts} (sources {dict(c)}); '
          f'facts shown {sum(s["facts_shown"] for s in stats_all)}; withheld {sum(s["facts_withheld"] for s in stats_all)}; '
          f'with financials {sum(1 for s in stats_all if s["financials"])}; identity-gated {sum(1 for s in stats_all if s["gate_reasons"])}; '
          f'industries {len(order)}; parts -> {PARTS}')
    return stats_all


if __name__ == '__main__':
    main()
