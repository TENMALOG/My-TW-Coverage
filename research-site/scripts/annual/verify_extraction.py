"""Verify extracted company facts against the annual-report text snapshot.

Reads research-site/data/company-facts/{ticker}.json, validates it against
research-site/schemas/company-facts.schema.json, runs deterministic checks on every fact and writes back
only each fact's `verification` object.
"""
import argparse
import datetime
import hashlib
import json
import re
import sys
from decimal import Decimal, InvalidOperation
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from slice_annual import ROOT, identity_confirmed, norm, split_pages  # noqa: E402

FACTS_DIR = ROOT / "research-site" / "data" / "company-facts"
SCHEMA_PATH = ROOT / "research-site" / "schemas" / "company-facts.schema.json"
CHECKS = ["source_hash", "excerpt_found", "page_match", "numbers_supported", "identity"]
CHECK_LABEL = {
    "source_hash": "來源檔雜湊不符",
    "excerpt_found": "引文不在快照中",
    "page_match": "引文不在標示頁面",
    "numbers_supported": "數字未被引文支持",
    "identity": "公司身分不符",
}


# ------------------------------------------------------------------ mini JSON Schema validator
def validate(inst, schema, path="$"):
    """Validate the JSON Schema subset used by company-facts.schema.json. Returns a list of errors."""
    errs = []
    t = schema.get("type")
    pytypes = {"object": dict, "array": list, "string": str, "integer": int, "number": (int, float), "boolean": bool}
    if t:
        ok = isinstance(inst, pytypes[t]) and not (t in ("integer", "number") and isinstance(inst, bool))
        if not ok:
            return [f"{path}: 應為 {t}"]
    if "enum" in schema and inst not in schema["enum"]:
        errs.append(f"{path}: 值不在允許清單內 ({inst!r})")
    if isinstance(inst, str):
        if "pattern" in schema and not re.search(schema["pattern"], inst):
            errs.append(f"{path}: 不符合格式 {schema['pattern']}")
        if "minLength" in schema and len(inst) < schema["minLength"]:
            errs.append(f"{path}: 長度小於 {schema['minLength']}")
    if isinstance(inst, (int, float)) and not isinstance(inst, bool):
        if "minimum" in schema and inst < schema["minimum"]:
            errs.append(f"{path}: 小於最小值 {schema['minimum']}")
    if isinstance(inst, dict):
        for r in schema.get("required", []):
            if r not in inst:
                errs.append(f"{path}: 缺少欄位 {r}")
        props = schema.get("properties", {})
        ap = schema.get("additionalProperties", True)
        for k, v in inst.items():
            if k in props:
                errs += validate(v, props[k], f"{path}.{k}")
            elif ap is False:
                errs.append(f"{path}: 不允許的欄位 {k}")
            elif isinstance(ap, dict):
                errs += validate(v, ap, f"{path}.{k}")
    if isinstance(inst, list):
        if "minItems" in schema and len(inst) < schema["minItems"]:
            errs.append(f"{path}: 項目數少於 {schema['minItems']}")
        if "items" in schema:
            for i, v in enumerate(inst):
                errs += validate(v, schema["items"], f"{path}[{i}]")
    return errs


# ------------------------------------------------------------------ number handling
NUM_RE = re.compile(r"\d[\d,]*(?:\.\d+)?")


def _dec(tok):
    try:
        return Decimal(tok.replace(",", "")).normalize()
    except InvalidOperation:
        return None


def numbers_in(text):
    """Set of Decimal values of all numbers in text (NFKC, thousands separators removed)."""
    import unicodedata
    t = unicodedata.normalize("NFKC", text)
    out = set()
    for m in NUM_RE.finditer(t):
        d = _dec(m.group(0))
        if d is not None:
            out.add(d)
    return out


def check_numbers(statement, period, excerpts):
    """Return list of statement numbers NOT supported by the excerpts."""
    import unicodedata
    st = unicodedata.normalize("NFKC", statement)
    period_nums = numbers_in(period)
    exc_nums = set()
    for e in excerpts:
        exc_nums |= numbers_in(e)
    # ROC <-> calendar equivalents of every excerpt number
    equiv = set(exc_nums)
    for d in exc_nums:
        equiv.add(d + 1911)
        equiv.add(d - 1911)
    missing = []
    for m in NUM_RE.finditer(st):
        tok = m.group(0)
        d = _dec(tok)
        if d is None:
            continue
        before = st[max(0, m.start() - 1):m.start()]
        after = st[m.end():m.end() + 1]
        # list ordinals such as "(1)" / "1、" / "1." at the start of a clause
        if "," not in tok and "." not in tok and d < 100:
            if (before in ("(", "（") and after in (")", "）")) or (
                    after in ("、", ".") and (m.start() == 0 or before in " ；;，。")):
                continue
        # digits inside a code name such as "B15" or "A1" are part of the label, not a quantity;
        # the whole code must still appear in the excerpts
        if before.isascii() and before.isalpha():
            flat = "".join(re.sub(r"\s+", "", unicodedata.normalize("NFKC", e)) for e in excerpts)
            if (before + tok) in flat:
                continue
        if d in period_nums:
            continue
        if d in equiv:
            continue
        if _in_flattened(tok, excerpts):
            continue
        missing.append(tok)
    return missing


def _in_flattened(tok, excerpts):
    """Fallback for table text flattened by PDF extraction, where adjacent cells run together
    ("聲學元件類1,933,81160.61%") or digits are spaced ("1 1 4 年度") or dates use dots ("70.9.05").
    Numbers with >=3 digits (or a decimal point) may match as a substring of the excerpt with
    whitespace and thousands separators removed; shorter integers must equal a whole digit run."""
    import unicodedata
    flat = "".join(re.sub(r"\s+", "", unicodedata.normalize("NFKC", e)) for e in excerpts)
    digits = tok.replace(",", "")
    if "." in digits or len(digits) >= 3:
        return digits in flat.replace(",", "")
    runs = []
    for group in re.findall(r"\d+(?:\.\d+)*", flat.replace(",", "")):
        if group.count(".") == 1:
            continue  # a decimal such as 12.5 never supports the integer 12
        runs.extend(group.split("."))  # dotted dates such as 70.9.05 split into parts
    if any(int(r) == int(digits) for r in runs if len(r) <= 3):
        return True
    # a thousands-grouped amount ends after its last 3-digit group, so in "272,12624%" the cell
    # after 272,126 is 24; only digits directly followed by "%" count, so the split is unambiguous
    rest = re.sub(r"\d{1,3}(?:,\d{3})+", "|", flat)
    return any(int(m) == int(digits) for m in re.findall(r"(?<![\d.])(\d{1,3})%", rest))


# ------------------------------------------------------------------ text checks
def excerpt_in_text(excerpt, norm_text):
    return norm(excerpt) in norm_text


def page_norms(text):
    return {p: norm(text[s:e]) for p, s, e in split_pages(text)}


def excerpt_on_page(excerpt, page, pnorm):
    """Excerpt must start on `page` and may continue onto page+1."""
    ne = norm(excerpt)
    cur = pnorm.get(page)
    if cur is None:
        return False
    both = cur + pnorm.get(page + 1, "")
    idx = both.find(ne)
    while idx != -1:
        if idx < len(cur) or not cur:
            return True
        idx = both.find(ne, idx + 1)
    return False


def fact_pages_ok(excerpts, page, pnorm):
    """First excerpt must start on `page`; later excerpts (e.g. a table header on `page` and its rows
    continued on the next page) may start on `page` or `page`+1."""
    return [excerpt_on_page(e, page, pnorm) or (i > 0 and excerpt_on_page(e, page + 1, pnorm))
            for i, e in enumerate(excerpts)]


def registered_names():
    """{ticker: 公司名稱} from MOPS 公司基本資料 snapshots (fetch_basic_data.py), if present; the TWSE/TPEx
    official directory fills tickers outside that catalog (same order as slice_annual.registered_name)."""
    path = ROOT / "research-site/data/basic-data.jsonl"
    out = {}
    directory = ROOT / "research-site/data/official-directory.json"
    if directory.exists():
        for r in json.loads(directory.read_text(encoding="utf-8"))["companies"]:
            if r.get("legal_name"):
                out[r["ticker"]] = r["legal_name"]
    if path.exists():
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.strip():
                r = json.loads(line)
                if r.get("legal_name"):
                    out[r["ticker"]] = r["legal_name"]
    return out


REGISTERED = None


def identity_ok(legal_name, ticker, filename, text, short_name=None):
    """Name check passes if the legal name is on the first 3 pages; otherwise (cover printed as an
    image, abbreviated or variant spelling) the legal name must equal the MOPS-registered name for
    this ticker and the report must be confirmed by slice_annual.identity_confirmed()."""
    global REGISTERED
    pn = page_norms(text)
    head = "".join(v for p, v in sorted(pn.items()) if p <= 3)
    name_ok = bool(legal_name) and norm(legal_name) in head
    if not name_ok and legal_name:
        if REGISTERED is None:
            REGISTERED = registered_names()
        reg = REGISTERED.get(ticker)
        if reg:
            name_ok = (norm(reg) == norm(legal_name)
                       and identity_confirmed(reg, short_name, ticker, filename, text) is not None)
        else:
            # no current MOPS registration (e.g. ceased public offering): the filename ticker plus
            # the short name used throughout the report must confirm identity
            name_ok = identity_confirmed(None, short_name, ticker, filename, text) == "filename_ticker_and_short_name"
    if not name_ok:
        # a manual confirmation made by reading the rendered report (e.g. image-only cover) — bound to
        # this exact report file and legal name, so it cannot carry over to another report
        conf = manual_confirmations().get(ticker)
        name_ok = bool(conf) and conf["filename"] == filename and norm(conf["legal_name"]) == norm(legal_name or "")
    fn_ok = f"_{ticker}_" in filename
    return name_ok, fn_ok


_MANUAL = None


def manual_confirmations():
    global _MANUAL
    if _MANUAL is None:
        _MANUAL = {}
        path = ROOT / "research-site/data/company-facts/_identity-confirmations.jsonl"
        if path.exists():
            for line in path.read_text(encoding="utf-8").splitlines():
                if line.strip():
                    r = json.loads(line)
                    _MANUAL[r["ticker"]] = r
    return _MANUAL


def verify_doc(doc, text_cache=None, now=None):
    """Mutates doc: fills each fact's verification. Returns (n_pass, n_fail, fail_by_check)."""
    now = now or datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
    src = doc["source"]
    notes_doc = []
    text = None
    sha_ok = False
    tp = ROOT / src["text_path"]
    if tp.exists():
        raw = tp.read_bytes()
        sha_ok = hashlib.sha256(raw).hexdigest() == src["text_sha256"]
        text = raw.decode("utf-8")
    else:
        notes_doc.append(f"找不到快照檔 {src['text_path']}")
    ntext = norm(text) if text else ""
    pnorm = page_norms(text) if text else {}
    name_ok, fn_ok = identity_ok(doc["legal_name"], doc["ticker"], src["filename"], text or "", doc.get("company"))
    passed = failed = 0
    by_check = {c: 0 for c in CHECKS}
    for f in doc["facts"]:
        notes = list(notes_doc)
        checks = {}
        checks["source_hash"] = sha_ok
        if text and not sha_ok:
            notes.append("來源檔雜湊與 text_sha256 不一致")
        found = [excerpt_in_text(e, ntext) for e in f["excerpts"]]
        checks["excerpt_found"] = bool(text) and all(found)
        for e, ok in zip(f["excerpts"], found):
            if text and not ok:
                notes.append(f"引文在快照中找不到：{e[:30]}…")
        pm = fact_pages_ok(f["excerpts"], f["page"], pnorm)
        checks["page_match"] = bool(text) and all(pm)
        for e, ok in zip(f["excerpts"], pm):
            if text and not ok:
                notes.append(f"引文不在第 {f['page']} 頁（或下一頁起始處）：{e[:30]}…")
        miss = check_numbers(f["statement"], f["period"], f["excerpts"])
        checks["numbers_supported"] = not miss
        if miss:
            notes.append("陳述中的數字未出現在引文：" + "、".join(miss))
        checks["identity"] = name_ok and fn_ok
        if not name_ok:
            notes.append("法定名稱未出現在年報前 3 頁，且與公開資訊觀測站登記名稱不符或未出現在內文")
        if not fn_ok:
            notes.append("來源檔名中的股票代號與 ticker 不一致")
        ok = all(checks.values())
        f["verification"] = {
            "status": "PASS" if ok else "FAIL",
            "checks": checks,
            "notes": notes,
            "verified_at": now,
        }
        if ok:
            passed += 1
        else:
            failed += 1
            for c, v in checks.items():
                if not v:
                    by_check[c] += 1
    return passed, failed, by_check


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--tickers", nargs="*")
    ap.add_argument("--dir", default=str(FACTS_DIR))
    a = ap.parse_args(argv)
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    d = Path(a.dir)
    files = sorted(d.glob("*.json"))
    if a.tickers:
        files = [f for f in files if f.stem in set(a.tickers)]
    tot = {"files": 0, "facts": 0, "PASS": 0, "FAIL": 0, "schema_errors": 0}
    byc = {c: 0 for c in CHECKS}
    for f in files:
        doc = json.loads(f.read_text(encoding="utf-8"))
        errs = validate(doc, schema)
        if errs:
            tot["schema_errors"] += 1
            print(f"{f.name}: schema 驗證失敗，未寫回", file=sys.stderr)
            for e in errs[:10]:
                print("  -", e, file=sys.stderr)
            continue
        p, q, bc = verify_doc(doc)
        f.write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        tot["files"] += 1
        tot["facts"] += p + q
        tot["PASS"] += p
        tot["FAIL"] += q
        for c in CHECKS:
            byc[c] += bc[c]
    print(f"files={tot['files']} facts={tot['facts']} PASS={tot['PASS']} FAIL={tot['FAIL']} schema_errors={tot['schema_errors']}")
    for c in CHECKS:
        print(f"  FAIL {c}: {byc[c]}")


if __name__ == "__main__":
    main()
