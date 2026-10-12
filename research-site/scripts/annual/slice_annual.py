"""Slice MOPS annual-report text snapshots into the sections used for fact extraction.

Read-only on the annual-report cache. Output: research-site/data/annual-slices/{ticker}.json
"""
import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
CACHE = ROOT / "audit-v5" / "source-cache" / "research-site" / "mops-annual"
OUT_DIR = ROOT / "research-site" / "data" / "annual-slices"
WINDOW = 6000
PAGE_RE = re.compile(r"\[PDF PAGE (\d+)\]")
WS_RE = re.compile(r"\s+")


def norm(s):
    """NFKC + remove all whitespace (used for matching only)."""
    return WS_RE.sub("", unicodedata.normalize("NFKC", s))


def split_pages(text):
    """List of (page_no, start_offset, end_offset) of each page body (marker excluded)."""
    marks = list(PAGE_RE.finditer(text))
    pages = []
    for i, m in enumerate(marks):
        end = marks[i + 1].start() if i + 1 < len(marks) else len(text)
        pages.append((int(m.group(1)), m.end(), end))
    return pages


def page_texts(text):
    return {p: text[s:e] for p, s, e in split_pages(text)}


def is_garbled(text):
    body = PAGE_RE.sub("", text)
    chars = [c for c in body if not c.isspace()]
    if len(chars) < 200:
        return True
    cjk = sum(1 for c in chars if "一" <= c <= "鿿")
    bad = sum(1 for c in chars if c == "�" or "" <= c <= "" or c == "\x00")
    return cjk / len(chars) < 0.15 or bad / len(chars) > 0.3


# ---------------------------------------------------------------- sections
SECTIONS = {
    "company_profile": ["設立日期", "公司沿革", "公司簡介", "公司之沿革", "沿革",
                        "歷史沿革"],
    "business_scope": ["業務內容", "業務範圍", "所營業務之主要內容", "所營業務", "營業範圍", "公司業務"],
    "revenue_mix": ["營業比重", "營業項目之比重", "營業收入比重", "營收比重", "業務比重", "營業比例"],
    "products": ["主要商品", "主要產品", "主要服務", "主要營業項目", "產品項目", "商品項目", "服務項目", "公司目前之商品"],
    "sales_regions": ["銷售地區", "主要銷售地", "內外銷", "外銷比重", "市場分析", "銷售區域", "內銷", "外銷"],
    "market_position": ["市場占有率", "市場佔有率", "市占率", "市佔率", "市場地位", "市場占有"],
    "raw_materials": ["主要原料", "原料之供應", "原物料", "原料供應", "主要材料", "原材料"],
    "major_customers_suppliers": [
        "百分之十以上", "百分之十以上之進", "百分之十以上之供應商", "百分之十以上之銷",
        "占進(銷)貨總額", "占進貨總額", "占銷貨總額", "占進銷貨總額", "10%以上之客戶", "10%以上之供應商",
        "主要進貨廠商", "主要銷貨客戶", "主要進銷貨客戶", "主要供應商", "主要客戶", "主要銷貨對象", "主要進貨對象",
    ],
    "production_sales": ["生產量值", "銷售量值", "產銷量值", "產量與產值", "產能產量", "產銷情形", "產量值"],
    "employees": ["從業員工", "員工人數", "從業人員", "員工資料"],
}
# Everything except company_profile lives in the 營運概況 chapter; search starts there when found.
AFTER_OPS = set(SECTIONS) - {"company_profile"}
# Short/ambiguous keywords: usable only as (very short) headings, never as keyword-window fallback.
WEAK = {"沿革", "內銷", "外銷", "市場分析", "所營業務", "公司業務", "主要客戶", "主要服務"}

LEADER_RE = re.compile(r"(?:\.{4,}|…{2,}|·{4,}|．{4,}|・{4,}|-{6,}|_{6,})")
TOC_LINE_RE = re.compile(r"(?:\.{3,}|…{2,}|·{3,}|．{3,}|・{3,})\s*\d+\s*$|\S\s{2,}\d{1,3}\s*$")
NUM_PREFIX_RE = re.compile(
    r"^(?:[（(]?[一二三四五六七八九十壹貳參叁肆伍陸柒捌玖拾]+[)）]?[、.．]?|[（(]\d+[)）]|\d+[、.．)]|[a-zA-Z][、.．)])")
OPS_RE = re.compile(r"^(?:[壹貳參叁肆伍陸柒捌玖拾一二三四五六七八九十]+[、.．]?)?營運概況")
SENT_END_RE = re.compile(r"[。，,；;：:]$")


def toc_pages(text):
    """Pages that are a table of contents (many leader / trailing page-number lines)."""
    res = set()
    for p, s, e in split_pages(text):
        body = text[s:e]
        lines = body.splitlines()
        leader = sum(1 for ln in lines if TOC_LINE_RE.search(ln.strip()) or LEADER_RE.search(ln))
        if leader >= 5 or (p <= 15 and "目錄" in norm(body[:400]) and leader >= 2):
            res.add(p)
    return res


def build_lines(text):
    """[(page, offset, raw_line, norm_line)] in document order."""
    out = []
    for p, s, e in split_pages(text):
        off = s
        for raw in text[s:e].split("\n"):
            out.append((p, off, raw, norm(raw)))
            off += len(raw) + 1
    return out


def find_ops_index(lines, tocs):
    """Index of the first non-TOC 營運概況 chapter heading, else None."""
    for i, (p, _o, _r, n) in enumerate(lines):
        if p in tocs or len(n) > 30 or LEADER_RE.search(n):
            continue
        if OPS_RE.match(n):
            return i
    return None


KEYWORD_ONLY = set()
NO_KEYWORD_MODE = {"company_profile"}  # 設立/沿革 keywords hit too many unrelated sentences; heading only
HEAD_BAD_RE = re.compile(r"[，,。；;]")


def match_line(lines, i, keywords, name=""):
    """Return (kind, keyword) for line i; kind is 'heading', 'keyword' or None.

    A heading is a short, punctuation-free line whose (numbering-stripped) text starts with the keyword.
    A keyword hit is any line containing the keyword (also when it wraps onto the next line)."""
    p, _o, _raw, n = lines[i]
    if not n:
        return None, None
    nxt = lines[i + 1][3] if i + 1 < len(lines) and lines[i + 1][0] == p else ""
    joined = n + nxt
    stripped_n = NUM_PREFIX_RE.sub("", n, count=1)
    stripped_j = NUM_PREFIX_RE.sub("", joined, count=1)
    headingish = len(n) <= (20 if name in NO_KEYWORD_MODE else 70) and not HEAD_BAD_RE.search(n)
    if headingish:
        for kw in keywords:
            if kw in KEYWORD_ONLY:
                continue
            k = norm(kw)
            pos = stripped_j.find(k)
            limit = 30 if stripped_n != n else 5
            if 0 <= pos <= limit and (pos < len(stripped_n)):  # keyword begins on this line
                if kw in WEAK and len(stripped_n) > 14:
                    continue
                return "heading", kw
    for kw in keywords:
        if name not in NO_KEYWORD_MODE and kw not in WEAK and norm(kw) in joined:
            return "keyword", kw
    return None, None


def locate(lines, tocs, name, ops_idx):
    kws = SECTIONS[name]
    start, stop = 0, len(lines)
    if ops_idx is not None:
        if name in AFTER_OPS:
            start = ops_idx
    best_kw = None
    for i in range(start, stop):
        if lines[i][0] in tocs or re.search(r"企業名稱|關係企業|被投資公司", lines[i][3]):
            continue
        kind, kw = match_line(lines, i, kws, name)
        if kind == "heading":
            return i, "heading", kw
        if kind == "keyword" and best_kw is None:
            best_kw = (i, "keyword", kw)
    return best_kw if best_kw else (None, None, None)


def make_window(text, lines, i):
    off = lines[i][1]
    win = text[off:off + WINDOW]
    start_page = lines[i][0]
    end_page = start_page
    for m in PAGE_RE.finditer(win):
        end_page = int(m.group(1))
    return win, start_page, end_page


def _dedupe_glyphs(name):
    """Some PDFs print each glyph three times (富富富世世世...); collapse when the whole string does."""
    if len(name) >= 6 and len(name) % 3 == 0 and all(name[i] == name[i + 1] == name[i + 2] for i in range(0, len(name), 3)):
        return name[::3]
    return name


def find_legal_name(text):
    pages = [(p, s, e) for p, s, e in split_pages(text) if p <= 4]
    cand = []
    for _p, s, e in pages:
        for raw in text[s:e].splitlines():
            n = norm(raw)
            st = raw.strip()
            if n.endswith("股份有限公司") and 5 <= len(n) <= 40 and not re.search(r"[：:，,。]", n):
                cand.append(_dedupe_glyphs(WS_RE.sub("", raw)))
            elif (re.search(r"(?:Co\.,?\s?Ltd\.?|Limited|Inc\.?|Corporation|Holdings?)$", st)
                  and 8 <= len(st) <= 70 and re.match(r"^[A-Za-z0-9&.,'\- ()]+$", st)):
                cand.append(WS_RE.sub(" ", st))
    if cand:
        return cand[0]
    # cover is an image: use the most frequent "XX股份有限公司" in the first 60 pages
    cnt = {}
    first = {}
    pat = re.compile(r"(?:^|[：:（(])([一-鿿][一-鿿A-Za-z0-9\-－]{1,18}股份有限公司)")
    for p, s, e in split_pages(text):
        if p > 60:
            break
        for raw in text[s:e].splitlines():
            for m in pat.finditer(WS_RE.sub("", raw)):
                nm = m.group(1)
                cnt[nm] = cnt.get(nm, 0) + 1
                first.setdefault(nm, len(first))
    cnt = {k: v for k, v in cnt.items() if not re.search(r"證券|會計師|股務|代理", k)}
    if cnt:
        return max(cnt, key=lambda k: (cnt[k], -first[k]))
    head = "".join(text[s:e] for _p, s, e in pages)
    m = re.search(r"([A-Z][A-Za-z0-9&.,\- ]{3,60}(?:Co\.,? ?Ltd\.?|Limited|Inc\.))", head)
    return m.group(1).strip() if m else ""


def slice_text(text):
    """Return (garbled, legal_name, sections)."""
    if is_garbled(text):
        return True, "", []
    tocs = toc_pages(text)
    lines = build_lines(text)
    ops_idx = find_ops_index(lines, tocs)
    sections = []
    for name in SECTIONS:
        i, kind, kw = locate(lines, tocs, name, ops_idx)
        if i is None:
            continue
        win, sp, ep = make_window(text, lines, i)
        found = lines[i][2].strip()
        sections.append({
            "name": name,
            "heading_found": found if kind == "heading" else f"{found} [keyword:{kw}]",
            "start_page": sp,
            "end_page": ep,
            "text": win,
            "confidence": kind,
        })
    return False, find_legal_name(text), sections


def latest_reports(cache=CACHE, tickers=None):
    best = {}
    for f in sorted(cache.glob("*_F04.json")):
        try:
            meta = json.loads(f.read_text(encoding="utf-8"))
        except Exception:
            continue
        if meta.get("status") != "captured":
            continue
        t = str(meta.get("ticker"))
        if tickers and t not in tickers:
            continue
        if t not in best or int(meta.get("fy", 0)) > int(best[t].get("fy", 0)):
            best[t] = meta
    return best


_VARIANTS = str.maketrans({"臺": "台", "晧": "皓"})


def name_forms(name):
    """Normalised spellings of a legal name as it may appear in a report: 股份有限公司 written as
    (股)公司, and common variant characters (臺/台, 晧/皓) unified."""
    base = norm(name).translate(_VARIANTS)
    forms = {base}
    # foreign-incorporated (KY) companies: the domicile prefix differs between MOPS and reports
    core = re.sub(r"^(英屬開曼群島商|英屬維京群島商|英屬蓋曼群島商|開曼群島商|開曼|百慕達商|薩摩亞商|香港商|新加坡商|美商|日商)", "", base)
    if len(core) >= 4:
        forms.add(core)
    for f in list(forms):
        if f.endswith("股份有限公司"):
            forms.add(f[: -len("股份有限公司")] + "(股)公司")
    return forms


def name_in_text(name, text_norm_variant):
    """text_norm_variant = norm(text).translate(_VARIANTS)."""
    return any(f in text_norm_variant for f in name_forms(name))


def identity_confirmed(registered, short_name, ticker, filename, text):
    """Return the basis on which the report is confirmed to belong to the company, or None.
    Either the registered legal name appears in the report, or (cover printed as an image) the
    MOPS filename carries the ticker and the short name appears at least 3 times in the text."""
    tv = norm(text).translate(_VARIANTS)
    if registered and name_in_text(registered, tv):
        return "registered_name_in_text"
    if f"_{ticker}_" in filename and short_name:
        # trading-name suffixes such as -KY, -創, * are not part of the name used in the report
        short = re.sub(r"(-KY創?|-創|\*)+$", "", norm(short_name).translate(_VARIANTS), flags=re.I)
        if len(short) >= 2 and tv.count(short) >= 3:
            return "filename_ticker_and_short_name"
    return None


_REGISTERED = None


def registered_name(ticker):
    """MOPS 公司基本資料 name for the ticker (research-site/data/basic-data.jsonl), if downloaded."""
    global _REGISTERED
    if _REGISTERED is None:
        _REGISTERED = {}
        path = ROOT / "research-site/data/basic-data.jsonl"
        if path.exists():
            for line in path.read_text(encoding="utf-8").splitlines():
                if line.strip():
                    r = json.loads(line)
                    if r.get("legal_name"):
                        _REGISTERED[r["ticker"]] = r["legal_name"]
    return _REGISTERED.get(ticker)


def process(meta):
    text = (ROOT / meta["text_path"]).read_text(encoding="utf-8")
    garbled, legal, sections = slice_text(text)
    # the cover heuristic is unreliable when the cover is an image; prefer the MOPS-registered
    # name whenever it actually appears in this report's text
    reg = registered_name(meta["ticker"])
    name_source = "cover_heuristic"
    if reg and name_in_text(reg, norm(text).translate(_VARIANTS)):
        legal, name_source = reg, "mops_registered_in_text"
    elif reg:
        name_source = "cover_heuristic_registered_name_not_in_text"
    return {
        "ticker": meta["ticker"], "fy": meta["fy"], "filename": meta["filename"],
        "citation_url": meta["citation_url"], "text_sha256": meta["text_sha256"],
        "text_path": meta["text_path"], "legal_name": legal, "legal_name_source": name_source,
        "garbled": garbled, "sections": sections,
    }


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--tickers", nargs="*")
    ap.add_argument("--out", default=str(OUT_DIR))
    a = ap.parse_args(argv)
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    reports = latest_reports(tickers=set(a.tickers) if a.tickers else None)
    n = garb = 0
    stats = {k: {"heading": 0, "keyword": 0, "missing": 0} for k in SECTIONS}
    nolegal = []
    for t in sorted(reports):
        try:
            res = process(reports[t])
        except FileNotFoundError:
            print(f"skip {t}: text file missing", file=sys.stderr)
            continue
        (out / f"{t}.json").write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
        n += 1
        if res["garbled"]:
            garb += 1
            continue
        if not res["legal_name"]:
            nolegal.append(t)
        got = {s["name"]: s["confidence"] for s in res["sections"]}
        for k in SECTIONS:
            stats[k][got.get(k, "missing")] += 1
    print(f"reports: {n}  garbled: {garb}  no legal_name: {len(nolegal)} {nolegal}")
    ng = max(n - garb, 1)
    for k, v in stats.items():
        hit = (v["heading"] + v["keyword"]) / ng * 100
        print(f"{k:28s} heading={v['heading']:3d} keyword={v['keyword']:3d} missing={v['missing']:3d}  hit={hit:.0f}%")


if __name__ == "__main__":
    main()
