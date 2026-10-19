"""Generate one company page per catalog company (all industries) from verified data only.

Inputs (read-only):
  catalog/release-scope-companies.csv, catalog/release-scope-claims.csv,
  data/verified-sentences.jsonl, data/financials/fy2025-financials-all.json,
  data/company-facts/{ticker}.json (optional; only facts with verification.status == PASS are rendered)

Citation mechanism: Pandoc footnotes. Each rendered fact, sentence and the financial table carries a
footnote with source title, locator/page and URL. The 〔id〕 marker mechanism of the aerospace pages
(filters/refs.lua + data/aerospace-defense/ref-map.json + a CSL bibliography) is not reused: the filter
aborts on any marker missing from that hand-built map, and extending it would mean editing existing files
and shipping a ~5,000-entry bibliography to every page. Footnotes keep each page self-contained.

Identity gate for company-facts files: the file's ticker, the ticker inside source.filename and the
legal_name (must contain the catalog short name's characters in order) must all agree with the page;
otherwise the file is skipped, the reason is written into the page's 資料缺口 and into the build log.

  python research-site/scripts/generic/build_company_pages_all.py [--industry FOLDER ...] [--tickers T ...] [--include-aero]
"""
from __future__ import annotations

import argparse
import csv
import functools
import json
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from industries import (AERO_TICKERS, ASSESSMENT, FACTS_DIR, SITE, claims, companies, display_name,  # noqa: E402
                        fmt_k, fmt_pct, industry_names, load_financials, load_verified, md_escape, roc_year)

OUTDIR = SITE / 'chapters/companies'
LOG = SITE / '_generated/company-pages-build-log.jsonl'
GENERATOR = 'research-site/scripts/generic/build_company_pages_all.py'

SECTION_FIELDS = {
    'basic': ['established', 'headquarters', 'history', 'business_scope', 'group_structure', 'employees'],
    'products': ['products', 'revenue_mix', 'sales_regions', 'export_share', 'capacity_or_production', 'rd', 'outlook'],
    'market': ['major_customers', 'major_suppliers', 'raw_materials', 'market_position'],
}
SECTION_ZH = {'basic': '公司基本資料', 'products': '產品與營收結構', 'market': '客戶、供應商與市場地位'}
FIELD_ZH = {
    'established': '設立', 'headquarters': '總部', 'history': '沿革', 'business_scope': '營業範圍',
    'group_structure': '集團結構', 'employees': '員工', 'products': '主要產品', 'revenue_mix': '營收結構',
    'sales_regions': '銷售地區', 'export_share': '外銷比重', 'capacity_or_production': '產能與產量',
    'rd': '研究發展', 'outlook': '公司自述展望', 'major_customers': '主要客戶', 'major_suppliers': '主要供應商',
    'raw_materials': '主要原料', 'market_position': '市場地位',
}
GENERAL_ROWS = [  # (label, candidate item keys)
    ('營業收入', ('營業收入',)),
    ('營業毛利', ('營業毛利（毛損）淨額', '營業毛利（毛損）')),
    ('營業利益', ('營業利益（損失）',)),
    ('本期淨利', ('本期淨利（淨損）',)),
]
EPS_KEY = '基本每股盈餘（元）'
NOT_PASSED_PREFIX = '新句未通過'


# ---------------- identity ----------------

def page_name(row: dict, fin: dict | None) -> tuple[str, bool]:
    """Catalog short name, or the MOPS name when the catalog name is garbled (U+FFFD)."""
    name = row['company']
    if '�' in name and fin:
        for y in sorted(fin.get('years', {}), reverse=True):
            mops = fin['years'][y].get('mops_company_name')
            if mops and '�' not in mops:
                return mops, True
    return name, False


def _norm_short(name: str) -> str:
    s = re.sub(r'-?KY創?$|-創$', '', name.strip())
    return ''.join(ch for ch in s if ch not in '*＊ �-').lower()


def name_in_order(short: str, legal: str) -> bool:
    chars, legal = _norm_short(short), legal.replace('(方方土)', '堃').lower()
    if not chars:
        return False
    pos = 0
    for ch in chars:
        pos = legal.find(ch, pos)
        if pos < 0:
            return False
        pos += 1
    return True


def filename_ticker(filename: str) -> str | None:
    """MOPS annual-report filenames look like '2025_2634_20260522F04.pdf' (year_ticker_date...)."""
    m = re.match(r'^\d{4}_([0-9]{4,6}[A-Z]?)_', filename or '') or re.search(r'_([0-9]{4,6}[A-Z]?)_', filename or '')
    return m.group(1) if m else None


def identity_problems(doc: dict, ticker: str, short: str) -> list[str]:
    probs = []
    if str(doc.get('ticker')) != ticker:
        probs.append(f'檔案內代號 {doc.get("ticker")} 與本頁代號 {ticker} 不符')
    ft = filename_ticker((doc.get('source') or {}).get('filename', ''))
    if ft != ticker:
        probs.append(f'年報檔名代號 {ft or "無法辨識"} 與本頁代號 {ticker} 不符')
    # verify_extraction.py already confirmed identity against the MOPS registered name for every fact;
    # that covers variant characters (臺/台、恆/恒), English legal names and renamed companies, which the
    # short-name heuristic below cannot.
    facts = doc.get('facts') or []
    verified = bool(facts) and all(((f.get('verification') or {}).get('checks') or {}).get('identity') for f in facts)
    if not verified and not name_in_order(short, doc.get('legal_name', '')):
        probs.append(f'年報公司全名「{doc.get("legal_name", "")}」與簡稱「{short}」對不上')
    return probs


def load_company_facts(ticker: str, short: str, facts_dir: Path = FACTS_DIR):
    """-> (doc or None, pass_facts, failed_count, gate_reasons)."""
    path = facts_dir / f'{ticker}.json'
    if not path.exists():
        return None, [], 0, []
    try:
        doc = json.loads(path.read_text(encoding='utf-8'))
    except (OSError, json.JSONDecodeError) as e:
        return None, [], 0, [f'年報事實檔無法讀取（{type(e).__name__}）']
    probs = identity_problems(doc, ticker, short)
    if probs:
        return None, [], 0, probs
    facts = doc.get('facts') or []
    rejected = semantic_rejects()
    ok = [f for f in facts if (f.get('verification') or {}).get('status') == 'PASS' and f.get('id') not in rejected]
    return doc, ok, len(facts) - len(ok), []


_REJECTS = None
_EDGES = None


def relation_edges() -> dict:
    global _EDGES
    if _EDGES is None:
        from company_relations import load_edges  # imported late: company_relations imports this module
        _EDGES = load_edges()
    return _EDGES


_RENAMES = None


@functools.lru_cache(maxsize=None)
def industry_corrections() -> dict:
    """{ticker: row} from data/industry-corrections.csv (classes corrected against the annual report)."""
    with open(SITE / 'data/industry-corrections.csv', encoding='utf-8-sig') as fh:
        return {r['ticker']: r for r in csv.DictReader(fh)}


def company_renames() -> dict:
    """Verified name history per ticker (data/company-renames.json, built by ops/renames/build_renames.py)."""
    global _RENAMES
    if _RENAMES is None:
        path = SITE / 'data/company-renames.json'
        _RENAMES = json.loads(path.read_text(encoding='utf-8')) if path.exists() else {}
    return _RENAMES


def rename_lines(doc: dict, renames: list[dict], notes) -> list[str]:
    out = []
    for r in renames:
        when = f'{md_escape(r["date_text"])}，' if r.get('date_text') else ''
        if r.get('former_name'):
            text = f'{when}由「{md_escape(r["former_name"])}」更名為「{md_escape(r["new_name"])}」'
        else:
            text = f'{when}更名為「{md_escape(r["new_name"])}」（年報未載更名前名稱）'
        if r.get('kind') == 'english':
            text += '（英文名稱）'
        src = doc['source']
        note = (f'{md_escape(doc["legal_name"])} {r["fy"]} 年度年報，第 {r["page"]} 頁'
                f'（{md_escape(src["filename"])}）。{url_md(r["source"])}')
        out.append(f'    - {text}{notes.add(note)}')
    return (['- **名稱沿革**：'] + out) if out else []


def render_relations(ticker, edges, notes):
    from company_relations import render_relations as _render
    return _render(ticker, edges, notes)


def semantic_rejects():
    """Fact ids rejected by semantic review (latest verdict per id wins) — never rendered."""
    global _REJECTS
    if _REJECTS is None:
        latest = {}
        path = SITE / 'data/company-facts/_semantic-review.jsonl'
        if path.exists():
            for line in path.read_text(encoding='utf-8').splitlines():
                if line.strip():
                    r = json.loads(line)
                    latest[r['id']] = r['verdict']
        _REJECTS = {k for k, v in latest.items() if v == 'REJECT'}
    return _REJECTS


# ---------------- rendering ----------------

class Notes:
    """Pandoc footnote collector."""

    def __init__(self):
        self.items: list[str] = []

    def add(self, text: str) -> str:
        self.items.append(text)
        return f'[^n{len(self.items)}]'

    def render(self) -> list[str]:
        return [f'[^n{i}]: {t}' for i, t in enumerate(self.items, 1)]


def url_md(url: str) -> str:
    u = url.strip().replace(' ', '%20').replace('<', '%3C').replace('>', '%3E')
    return f'<{u}>'


def web_citation(c: dict) -> str:
    parts = [f'「{md_escape(c.get("title") or "未具標題的來源")}」']
    if c.get('publication_date'):
        parts.append(md_escape(str(c['publication_date'])))
    if c.get('locator'):
        parts.append(f'位置：{md_escape(str(c["locator"]))}')
    return '，'.join(parts) + f'。{url_md(c["url"])}'


def public_citations(sentence: dict) -> list[dict]:
    return [c for c in sentence.get('citations') or [] if (c.get('url') or '').startswith('http')]


def sentence_note(sentence: dict) -> str:
    """One footnote per sentence; citations of the same URL are merged (locators joined)."""
    merged: dict[str, dict] = {}
    for c in public_citations(sentence):
        m = merged.setdefault(c['url'], {**c, 'locators': []})
        if c.get('locator') and c['locator'] not in m['locators']:
            m['locators'].append(c['locator'])
    return '；'.join(web_citation({**m, 'locator': '／'.join(m['locators'])}) for m in merged.values())


def fact_note(doc: dict, fact: dict | None) -> str:
    src = doc['source']
    head = f'{md_escape(doc["legal_name"])} {src["fy"]} 年度（民國 {roc_year(src["fy"])} 年度）年報'
    if fact is None:
        return f'{head}（{md_escape(src["filename"])}）。{url_md(src["citation_url"])}'
    return (f'{head}，第 {fact["page"]} 頁（{md_escape(src["filename"])}）；期間：{md_escape(fact["period"])}。'
            f'{url_md(src["citation_url"])}')


def fin_source_note(fin: dict) -> str:
    bits = []
    for y in sorted(fin['years']):
        s = fin['years'][y].get('source') or {}
        post = s.get('post') or {}
        bits.append(f'{y} 年：民國 {post.get("year", roc_year(y))} 年第 {post.get("season", "04").lstrip("0")} 季'
                    f'（{post.get("TYPEK", "")}），擷取於 {str(s.get("captured_at", ""))[:10]}')
    url = next((fin['years'][y]['source']['url'] for y in fin['years'] if fin['years'][y].get('source')), '')
    return (f'公開資訊觀測站「{md_escape(fin["basis"])}」；' + '；'.join(bits) + '。單位：新臺幣仟元。'
            + (f'查詢端點 {url_md(url)}（需以表單參數查詢）' if url else ''))


def fin_table(fin: dict, notes: Notes) -> list[str]:
    years = ['2024', '2025']
    have = {y: fin['years'].get(y) for y in years}
    kinds = {v['table_kind'] for v in have.values() if v}
    mark = notes.add(fin_source_note(fin))
    L = []
    if kinds == {'一般業'}:
        L += ['| 項目 | 2024 | 2025 |', '|---|---:|---:|']
        for label, keys in GENERAL_ROWS:
            cells = []
            for y in years:
                v = have[y]
                val = next((v['items_k'][k] for k in keys if v and v['items_k'].get(k) is not None), None)
                cells.append('—' if val is None else fmt_k(val))
            L.append(f'| {label}（仟元） | {cells[0]} | {cells[1]} |')
        L.append(f'| 毛利率 | {fmt_pct(have["2024"] and have["2024"].get("gross_margin_pct"))} | '
                 f'{fmt_pct(have["2025"] and have["2025"].get("gross_margin_pct"))} |')
        L.append(f'| 營業利益率 | {fmt_pct(have["2024"] and have["2024"].get("operating_margin_pct"))} | '
                 f'{fmt_pct(have["2025"] and have["2025"].get("operating_margin_pct"))} |')
        L += ['', f'金額單位為新臺幣仟元，取自公開資訊觀測站綜合損益表彙總（第四季＝全年度）；'
                  f'毛利率與營業利益率＝該項目 ÷ 營業收入 × 100，四捨五入至小數第二位。{mark}']
    else:
        kind_txt = '、'.join(sorted(kinds))
        keys = []
        for y in years:
            if have[y]:
                keys += [k for k, v in have[y]['items_k'].items() if v is not None and k != EPS_KEY and k not in keys]
        L += ['| 項目（仟元） | 2024 | 2025 |', '|---|---:|---:|']
        for k in keys:
            cells = []
            for y in years:
                v = have[y]['items_k'].get(k) if have[y] else None
                cells.append('—' if v is None else fmt_k(v))
            L.append(f'| {md_escape(k)} | {cells[0]} | {cells[1]} |')
        L += ['', f'本公司綜合損益表採「{md_escape(kind_txt)}」格式，沒有一般業的營業收入與營業毛利欄位，'
                  f'因此不計算毛利率，改列報表上有數值的項目。金額單位為新臺幣仟元。{mark}']
    missing = [y for y in years if not have[y]]
    if missing:
        L.append(f'\n{"、".join(missing)} 年度在公開資訊觀測站彙總表中查無本公司資料，以「—」表示。')
    return L


def render_facts(doc, facts, fields, notes: Notes) -> list[str]:
    L = []
    for field in fields:
        for f in [x for x in facts if x.get('field') == field]:
            attr = f.get('attribution', '')
            tag = '' if attr == '公司年報揭露' else f'（{md_escape(attr)}）'
            L.append(f'- **{FIELD_ZH[field]}**：{md_escape(f["statement"])}{tag}{notes.add(fact_note(doc, f))}')
    return L


def render_page(row: dict, *, fin: dict | None, sentences: list[dict], company_claims: list[dict],
                facts_result: tuple, industry_zh: str, industry_slug: str) -> tuple[str, dict]:
    tk = row['ticker']
    name, from_mops = page_name(row, fin)
    doc, facts, failed_facts, gate = facts_result
    notes = Notes()
    shown = [s for s in sentences if public_citations(s)]
    no_public = len(sentences) - len(shown)
    title = f'{tk} {name}'.replace('"', '\\"')
    subtitle = doc['legal_name'].replace('"', '\\"') if doc else ''
    L = [f'---\ntitle: "{title}"\n' + (f'subtitle: "{subtitle}"\n' if doc else '') + '---\n',
         f'<!-- 由 {GENERATOR} 產生；請勿手動修改。 -->\n',
         f'本頁整理{md_escape(name)}（股票代號 {tk}，[{md_escape(industry_zh)}](../industries/{industry_slug}.qmd)）'
         f'已通過查核的公開資料，資料截止日 {ASSESSMENT}；未通過查核的原報告敘述只計入資料缺口，不列入正文。\n']
    gaps = []
    if from_mops:
        gaps.append(f'原專案目錄中的公司簡稱有亂碼，本頁改用公開資訊觀測站財務彙總表上的公司名稱「{md_escape(name)}」。')

    # 1. basic data
    L.append('## 公司基本資料 {.unnumbered}\n')
    L.append(f'- **股票代號**：{tk}')
    fix = industry_corrections().get(tk)
    if fix:   # the original project's class contradicts the annual report: show both, cite the evidence
        orig = fix['original_folder']
        orig_zh = industry_names().get(orig, {}).get('name_zh', orig)
        ev = ''.join(notes.add(fact_note(doc, f)) for f in (doc or {}).get('facts', []) if f['id'] in fix['facts'].split(';'))
        L.append(f'- **產業分類**：{md_escape(industry_zh)}（依年報更正；原專案歸為{md_escape(orig_zh)}／{md_escape(orig)}。'
                 f'{md_escape(fix["reason"])}）{ev}')
    else:
        L.append(f'- **產業分類**：{md_escape(industry_zh)}（原專案分類 {md_escape(row["industry_folder"])}）')
    if doc:
        L.append(f'- **公司全名**：{md_escape(doc["legal_name"])}'
                 f'{notes.add(fact_note(doc, None))}')
        L += rename_lines(doc, company_renames().get(tk, []), notes)
    basic =render_facts(doc, facts, SECTION_FIELDS['basic'], notes) if doc else []
    L += basic + ['']

    # 2. products
    L.append('## 產品與營收結構 {.unnumbered}\n')
    prod = render_facts(doc, facts, SECTION_FIELDS['products'], notes) if doc else []
    L += prod if prod else ['目前沒有已驗證的產品或營收結構資料。']
    L.append('')

    # 3. financials
    L.append('## 財務摘要 {.unnumbered}\n')
    if fin and fin.get('years'):
        L += fin_table(fin, notes)
    else:
        L.append('公開資訊觀測站 2024、2025 年度綜合損益表彙總中查無本公司資料，本頁不列財務數字。')
        gaps.append('2024、2025 年度財務數字缺漏。')
    L.append('')

    # 4. customers / suppliers / market + verified sentences
    L.append('## 客戶、供應商與市場地位 {.unnumbered}\n')
    market = render_facts(doc, facts, SECTION_FIELDS['market'], notes) if doc else []
    L += market
    if shown:
        if market:
            L.append('')
        L.append('以下敘述經逐條查核並有公開來源支持：\n')
        for s in shown:
            period = f'（期間：{md_escape(s["period"])}）' if s.get('period') and len(s['period']) <= 20 else ''
            L.append(f'- {md_escape(s["text"])}{period}{notes.add(sentence_note(s))}')
    if not market and not shown:
        L.append('目前沒有已驗證的客戶、供應商或市場地位資料。')
    L.append('')

    # 4b. reviewed relations with other listed companies (data/relations/listed_edges.csv)
    rel = render_relations(tk, relation_edges().get(tk, []), notes)
    if rel:
        L += rel + ['']

    # 5. gaps
    not_passed = [c for c in company_claims if c['revision_status'].startswith(NOT_PASSED_PREFIX)]
    no_text = [c for c in company_claims if not c['adoptable_text'].strip() and not c['revision_status'].startswith(NOT_PASSED_PREFIX)]
    missing_sections = []
    if not basic:
        missing_sections.append('公司基本資料（年報事實）')
    if not prod:
        missing_sections.append('產品與營收結構')
    if not market and not shown:
        missing_sections.append('客戶、供應商與市場地位')
    L.append('## 資料缺口 {.unnumbered}\n')
    if company_claims:
        L.append(f'- 原報告共有 {len(company_claims)} 條敘述被選入查核，其中 {len(sentences)} 條有可採用的版本；'
                 f'{len(not_passed)} 條經兩輪查核仍未通過，內容不列入本頁。')
        if no_text:
            L.append(f'- {len(no_text)} 條敘述沒有可採用的修正版本，內容不列入本頁。')
    else:
        L.append('- 原查核範圍沒有選入本公司的敘述。')
    if no_public:
        L.append(f'- {no_public} 條已通過的敘述只有內部比對資料、沒有可公開連結的來源，因此不列入本頁。')
    if doc is None and not gate:
        L.append('- 尚無經驗證的年報事實檔。')
    for g in gate:
        L.append(f'- 年報事實檔未通過身分核對，整份未採用：{md_escape(g)}。')
    if failed_facts:
        L.append(f'- 年報事實檔中有 {failed_facts} 條事實未通過逐字核對，不列入本頁。')
    if missing_sections:
        L.append(f'- 缺少已驗證內容的段落：{"、".join(missing_sections)}。')
    for g in gaps:
        L.append(f'- {g}')
    L.append('')

    # 6. sources (each once)
    L.append('## 資料來源 {.unnumbered}\n')
    srcs: dict[str, str] = {}
    if doc:
        src = doc['source']
        srcs[src['citation_url']] = f'{md_escape(doc["legal_name"])} {src["fy"]} 年度年報（公開資訊觀測站，{md_escape(src["filename"])}）'
    if fin and fin.get('years'):
        for y in sorted(fin['years']):
            s = fin['years'][y].get('source') or {}
            if s.get('url'):
                srcs.setdefault(s['url'], '公開資訊觀測站 綜合損益表彙總（t163sb04）')
    for s in shown:
        for c in public_citations(s):
            srcs.setdefault(c['url'], md_escape(c.get('title') or c['url']))
    if srcs:
        for url, label in srcs.items():
            L.append(f'- {label}：{url_md(url)}')
    else:
        L.append('本頁沒有可列出的外部來源。')
    L.append('')
    if notes.items:
        L += notes.render() + ['']
    stats = {'ticker': tk, 'company': name, 'financials': bool(fin and fin.get('years')),
             'verified_sentences': len(shown), 'pass_facts': len(facts), 'facts_rejected': bool(gate),
             'gate_reasons': gate}
    return '\n'.join(L), stats


# ---------------- driver ----------------

def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument('--industry', nargs='*', default=None)
    ap.add_argument('--tickers', nargs='*', default=None)
    ap.add_argument('--include-aero', action='store_true')
    a = ap.parse_args(argv)
    names = industry_names()
    rows = companies()
    if a.industry:
        unknown = set(a.industry) - {r['industry_folder'] for r in rows}
        if unknown:
            raise SystemExit(f'unknown industry folder(s): {sorted(unknown)}')
        rows = [r for r in rows if r['industry_folder'] in a.industry]
    if a.tickers:
        rows = [r for r in rows if r['ticker'] in a.tickers]
    fins = load_financials()
    verified = load_verified()
    by_tk_claims: dict[str, list] = {}
    for c in claims():
        by_tk_claims.setdefault(c['ticker'], []).append(c)
    OUTDIR.mkdir(parents=True, exist_ok=True)
    LOG.parent.mkdir(parents=True, exist_ok=True)
    cnt, log = Counter(), []
    for r in rows:
        tk = r['ticker']
        if tk in AERO_TICKERS and not a.include_aero:
            cnt['skipped_aero'] += 1
            continue
        fin = fins.get(tk)
        name, _ = page_name(r, fin)
        facts_result = load_company_facts(tk, name)
        ind = names[r['industry_folder']]
        text, st = render_page(r, fin=fin, sentences=verified.get(tk, []), company_claims=by_tk_claims.get(tk, []),
                               facts_result=facts_result, industry_zh=ind['name_zh'], industry_slug=ind['slug'])
        (OUTDIR / f'{tk}.qmd').write_text(text, encoding='utf-8', newline='\n')
        cnt['written'] += 1
        cnt['with_financials'] += st['financials']
        cnt['with_verified_sentence'] += st['verified_sentences'] > 0
        cnt['with_pass_facts'] += st['pass_facts'] > 0
        cnt['identity_mismatch_skipped'] += st['facts_rejected']
        if st['facts_rejected']:
            log.append({'ticker': tk, 'company': name, 'event': 'company_facts_rejected', 'reasons': st['gate_reasons']})
    with open(LOG, 'w', encoding='utf-8', newline='\n') as fh:
        for e in log:
            fh.write(json.dumps(e, ensure_ascii=False) + '\n')
    facts_files = len(list(FACTS_DIR.glob('*.json'))) if FACTS_DIR.exists() else 0
    print(f'pages written {cnt["written"]}; with financials {cnt["with_financials"]}; '
          f'with >=1 verified sentence {cnt["with_verified_sentence"]}; with PASS annual-report facts {cnt["with_pass_facts"]}; '
          f'company-facts files present {facts_files}; identity mismatches skipped {cnt["identity_mismatch_skipped"]}; '
          f'aerospace pages left untouched {cnt["skipped_aero"]}; log {LOG}')
    return cnt


if __name__ == '__main__':
    main()
