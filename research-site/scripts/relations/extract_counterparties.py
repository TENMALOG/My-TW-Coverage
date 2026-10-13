"""Extract literal counterparties; keep anonymous labels anonymous."""

from __future__ import annotations

import csv
import json
import re
from collections import Counter

from build_relations import CATALOG, DATA, FACTS, load_facts, name_index

SHARE = re.compile(r"(?:\d+(?:\.\d+)?\s*%|百分之[零一二三四五六七八九十百\d]+)")
AMOUNT = re.compile(r"(?:新[臺台]幣|美金|美元|人民幣)?\s*\d[\d,]*(?:\.\d+)?\s*(?:仟元|千元|佰萬元|百萬元|億元|萬元|元|億美元|萬美元)")
CODE = re.compile(r"(?:[A-ZＡ-ＺＩ][A-ZＡ-Ｚ0-9０-９#\- ]{0,8}|[#＃]?[A-ZＡ-Ｚ]?[0-9０-９]{3,8}|[甲乙丙丁戊己庚辛壬癸⼄])(?:\s*(?:公司|客戶|供應商|廠商))?|(?:客戶|供應商|廠商)\s*[A-ZＡ-Ｚ甲乙丙丁]")
NO_NAME = re.compile(r"未有|並無|皆無|均無|無超過|無任一|不適用|無需揭露|未達|無主要|無特定|載明為[「『]?無|列示為[「『]?無")
SPLIT = re.compile(r"(?:、|，|,|及|以及|與|和|等)")
STOP = re.compile(r"(?:進貨|銷貨|採購|供貨|交易|之關係|金額|占全|為主|，|。|；|（年報|\(年報)")
PATTERNS = [
    re.compile(r"(?:向|對)(?P<name>[^，。；]{1,75}?)(?:進貨|銷貨|採購|供貨|交易)"),
    re.compile(r"(?:供應商|客戶|廠商)(?P<name>[^，。；]{1,75}?)(?:進貨|銷貨|採購|供貨|交易|金額|占)"),
    re.compile(r"(?:供應商|客戶|廠商)(?:為|包括|有)(?P<name>[^，。；]{1,85})(?:[，。；]|$)"),
    re.compile(r"(?:子公司|母公司|關係企業|轉投資公司|投資於)(?P<name>[^，。；]{2,85})(?:[，。；]|$)"),
    re.compile(r"(?:供應商|廠商|客戶)(?:表)?(?:列示|列有|列為|名稱欄載為)[「『]?(?P<name>[^，。；「」『』]{2,55})(?:[，。；]|$)"),
    re.compile(r"(?:隸屬|對)(?P<name>[^，。；]{2,50}?)(?:集團|之投資)") ,
]
LEGAL_SUFFIX = re.compile(r"(?:股份有限公司|[（(]股[）)]公司|有限公司|Co\.,? Ltd\.?|Inc\.?|Corporation|Corp\.?|Limited|Ltd\.?)")
REJECT_FRAGMENTS = {"公司", "本公司", "合併公司", "年報", "供應商", "客戶", "廠商", "主要", "其他", "無", "不適用"}
BAD_WORDS = re.compile(r"資料|年報|表列|表中|代號|編號|匿名|未揭露|進貨|銷貨|金額|年度|原文|關係|之|的|於|持續|負責|製造|業務|比例|占|比率|列名|列示|稱|皆|單一|所用|商品|服務")


def kind_for(name: str, statement: str) -> str:
    pos = statement.find(name)
    local = statement[max(0, pos - 12):pos + len(name) + 12]
    if re.search(r"代號|編號|匿名|未揭露|某客戶|某供應商|某廠商|以代稱", local) and re.search(r"[A-Za-zＡ-Ｚ甲乙丙丁戊己庚辛壬癸#＃]|\d{3,}", name):
        return "code"
    if re.search(r"\d{3,}", name) and not LEGAL_SUFFIX.search(name):
        return "code"
    if re.fullmatch(r"(?:客戶|供應商|廠商)\s*[A-ZＡ-Ｚ甲乙丙丁戊己庚辛壬癸⼄]", name):
        return "code"
    if re.fullmatch(r"[A-ZＡ-Ｚ甲乙丙丁戊己庚辛壬癸⼄](?:\s*(?:公司|客戶|供應商|廠商))?", name):
        return "code"
    if re.fullmatch(r"[A-ZＡ-Ｚ甲乙丙丁戊己庚辛壬癸⼄]\s*集團", name):
        return "code"
    return "named"


def clean_piece(piece: str, statement: str) -> str:
    piece = piece.strip(" \t\n「」『』：:")
    piece = re.sub(r"^.*者為", "", piece)
    piece = re.sub(r"^(?:主要|供應商|客戶|廠商|分別為|為|係|包括|有|與|對|向)", "", piece)
    piece = STOP.split(piece, 1)[0].strip(" \t\n「」『』：:")
    piece = re.sub(r"^(?:\d{2,3}年度|\d{4}年度|第\d+名)", "", piece).strip()
    piece = re.sub(r"(?:\d{2,3}年度|\d{4}年度|於\d{2,3}年度)$", "", piece).strip()
    legal_match = LEGAL_SUFFIX.search(piece)
    if legal_match and re.search(r"\d|股權|持股|比例", piece[legal_match.end():]):
        piece = piece[:legal_match.end()]
    if re.search(r"^(?:年報|資料|表|名單|名稱|最近|個別|同一|單一|其|之|本|發行人|全年度|數字|原文|截至|金額|比率|對象)", piece):
        return ""
    if re.fullmatch(r"[\W\d_]+", piece) or len(piece) < 2 and piece not in "甲乙丙丁ABCDEF":
        return ""
    if BAD_WORDS.search(piece) and not LEGAL_SUFFIX.search(piece):
        return ""
    if piece.endswith("客戶") and re.search(r"產品|食品|化妝品|藥妝|機油|日化|業", piece):
        return ""
    return piece if piece and piece in statement and piece not in REJECT_FRAGMENTS else ""


def extract(fact: dict, known_names: list[str]) -> list[tuple[str, str]]:
    statement = fact["statement"]
    field = fact["field"]
    names: list[str] = []
    # Literal catalog and legal names provide the safest candidates. Prefer longer spans.
    generic_short = {"第一大", "數字", "銷售", "均無", "明係", "世界", "中華", "Ltd."}
    for name in known_names:
        if name in generic_short:
            continue
        if len(name) >= 2 and name in statement and not any(name in found for found in names):
            names.append(name)
    # Explicit report codes take priority over surrounding generic descriptions.
    for match in re.finditer(r"(?:代號|編號)\s*[「『（(]?\s*([#＃]?[A-ZＡ-Ｚ甲乙丙丁⼄]?[A-ZＡ-Ｚ0-9０-９#＃]{0,9})", statement):
        value = match.group(1)
        if value and (re.search(r"[A-ZＡ-Ｚ甲乙丙丁⼄#＃0-9０-９]", value)) and value not in names:
            names.append(value)
    for match in re.finditer(r"([A-Za-zＡ-Ｚ甲乙丙丁戊己庚辛壬癸⼄]{1,8})[（(](?:年報)?代號[）)]", statement):
        value = match.group(1)
        if value not in names:
            names.append(value)
    for match in re.finditer(r"匿名[^，。；]{0,15}?[「『]([^」』]{1,20})[」』]", statement):
        value = match.group(1).strip()
        if value and value not in names:
            names.append(value)
    for match in re.finditer(r"\b([A-ZＡ-Ｚ甲乙丙丁⼄][A-ZＡ-Ｚ0-9０-９]{0,5}(?:公司|客戶|供應商|廠商))(?=[（(]?年報|[（(]?代號|[（(]?匿名|\s*\d{2,3}年度)", statement):
        value = match.group(1)
        if value not in names:
            names.append(value)
    if field in {"major_customers", "major_suppliers"}:
        for match in re.finditer(r"(?<![A-Za-z])([A-ZＡ-Ｚ甲乙丙丁戊己庚辛壬癸⼄][A-ZＡ-Ｚ0-9０-９]{0,9}\s*(?:公司|客戶|供應商|廠商|集團)|(?:客戶|供應商|廠商)\s*[A-ZＡ-Ｚ甲乙丙丁戊己庚辛壬癸⼄][A-ZＡ-Ｚ0-9０-９]{0,9})", statement):
            value = match.group(1).strip()
            if value not in names and (re.search(r"代號|匿名|代稱|某客戶|某供應商|某廠商", statement) or re.search(r"[甲乙丙丁戊己庚辛壬癸⼄]", value)):
                names.append(value)
        for match in re.finditer(r"\b([A-ZＡ-Ｚ]{2,8}[0-9０-９]{2,8})\b", statement):
            value = match.group(1)
            if value not in names and re.search(r"代號|匿名|編號", statement):
                names.append(value)
        for match in re.finditer(r"([A-ZＡ-Ｚ][A-ZＡ-Ｚ0-9０-９]{4,12})[（(](?:年報)?代號[）)]", statement):
            value = match.group(1)
            if value not in names:
                names.append(value)
        for match in re.finditer(r"([A-ZＡ-Ｚ甲乙丙丁戊己庚辛壬癸⼄]\s*集團)", statement):
            value = match.group(1)
            if value not in names:
                names.append(value)
        for match in re.finditer(r"(?<![A-Za-z])([A-ZＡ-Ｚ甲乙丙丁戊己庚辛壬癸⼄]\s*(?:公司|客戶|供應商|廠商)|(?:客戶|供應商|廠商|進貨對象)\s*[A-ZＡ-Ｚ甲乙丙丁戊己庚辛壬癸⼄])", statement):
            value = match.group(1).strip()
            if value not in names:
                names.append(value)
        for match in re.finditer(r"[「『]([A-ZＡ-Ｚ][A-ZＡ-Ｚ0-9０-９-]{2,12})[」』]", statement):
            value = match.group(1)
            if value not in names and re.search(r"代號|匿名", statement):
                names.append(value)
        if not names and field == "major_customers":
            for match in re.finditer(r"([A-Z][A-Za-z ]{2,25})(?=、|皆為|等長期合作)", statement):
                value = match.group(1).strip()
                if value and value not in names:
                    names.append(value)
    for pattern in PATTERNS:
        for match in pattern.finditer(statement):
            raw = match.group("name")
            for piece in SPLIT.split(raw):
                value = clean_piece(piece, statement)
                if not value or value in names or any(value in existing for existing in names):
                    continue
                if re.match(r"^(?:\d+年度|\d+年|\d+月|\d+%|全年度|年度|最近|合併|單一|個別|國內|國外)", value):
                    continue
                names.append(value)
    # An anonymous label often sits in parentheses after a generic noun.
    for match in re.finditer(r"(?:代號|編號|某客戶|某供應商|某廠商)[^，。；]{0,12}?[（(「『]([A-ZＡ-Ｚ#＃0-9０-９甲乙丙丁⼄][^）)」』]{0,14})[）)」』]", statement):
        value = match.group(1).strip()
        if value and value not in names and not any(value in existing for existing in names):
            names.append(value)
    if not names and not NO_NAME.search(statement) and field == "group_structure":
        for match in re.finditer(r"(?:子公司|母公司|關係企業|轉投資公司|持有)([^，。；]{2,60})", statement):
            value = clean_piece(match.group(1), statement)
            if value and not re.search(r"^(?:約|逾|\d|於|在|之|其)", value):
                names.append(value)
    if not names and field in {"major_customers", "major_suppliers"}:
        action = "銷貨" if field == "major_customers" else "進貨"
        for match in re.finditer(r"(?:\d{2,3}年度|\d{4}年度|向|對|客戶|供應商|廠商)\s*([A-Za-z\u3400-\u9fff][^，。；]{1,60}?)" + action, statement):
            raw = match.group(1).strip()
            raw = re.split(r"(?:金額|占|[（(]年報|[（(]原文)", raw)[0].strip()
            value = clean_piece(raw, statement)
            if value:
                names.append(value)
    if not names and field in {"major_customers", "major_suppliers"}:
        for match in re.finditer(r"(?:表列示|表列|供應商|廠商|客戶|者為|表之)([\u3400-\u9fffA-Za-z][\u3400-\u9fffA-Za-z0-9（）() ]{1,45}?)(?=，|進貨|銷貨|[（(]年報代號)", statement):
            value = clean_piece(match.group(1), statement)
            if value:
                names.append(value)
        for match in re.finditer(r"表之(.{2,60}?)(?:進貨|銷貨)金額", statement):
            value = clean_piece(match.group(1), statement)
            if value:
                names.append(value)
    if not names and field in {"major_customers", "major_suppliers"}:
        for match in re.finditer(r"(?:^|[，、。]|\d{2,3}年度)([A-Za-z\u3400-\u9fff][A-Za-z\u3400-\u9fff0-9 （）().,'-]{2,55}?)(?:於\d{2,3}年度|\d{2,3}年度)?(?:的|之)?(?:進貨金額|銷貨金額|銷貨淨額|合併金額)", statement):
            value = clean_piece(match.group(1), statement)
            if value:
                names.append(value)
    if not names and field == "group_structure":
        for match in re.finditer(r"(?:子公司|母公司|控股公司)([A-Za-z\u3400-\u9fff][A-Za-z\u3400-\u9fff0-9 （）().,'-]{2,70}?)(?:[，。；]|\d+\.?\d*%|之|以|負責|所|$)", statement):
            value = clean_piece(match.group(1), statement)
            if value:
                names.append(value)
    if not names and field in {"major_customers", "major_suppliers"}:
        action = "銷貨" if field == "major_customers" else "進貨"
        for match in re.finditer(r"([A-Za-z\u3400-\u9fff][A-Za-z\u3400-\u9fff0-9（）()&.' -]{1,45}?)(?:於\d{2,3}年度)?(?:之|的)?" + action + r"(?:金額|淨額)", statement):
            raw = match.group(1)
            raw = re.split(r"(?:\d{2,3}年度|\d{4}年度|年報|表列|列示|向|對|供應商|廠商|客戶)", raw)[-1].strip()
            value = clean_piece(raw, statement)
            if value:
                names.append(value)
    result = []
    for name in names:
        if not name or name not in statement:
            continue
        if name in {"第一大", "數字", "銷售", "均無", "明係", "某供應商", "某客戶", "某廠商", "Ltd."}:
            continue
        if re.search(r"仟元|千元|萬元|億元|並無|本集團|全年度|百分之|\d+%", name):
            continue
        if len(name) > 40 and not LEGAL_SUFFIX.search(name):
            continue
        if kind_for(name, statement) == "code" and any(name != other and name in other and kind_for(other, statement) == "code" for other in names):
            continue
        if field == "group_structure":
            window = statement[max(0, statement.find(name) - 24):statement.find(name)]
            role = "parent" if re.search("母公司|母集團|控制公司|隸屬", window) else "subsidiary" if "子公司" in window else "investee" if re.search("轉投資|投資於|持有", window) or "之投資" in statement[statement.find(name):statement.find(name)+len(name)+6] else "affiliate"
        else:
            role = "customer" if field == "major_customers" else "supplier"
        result.append((name, kind_for(name, statement), role))
    return result or [("", "none", "customer" if field == "major_customers" else "supplier" if field == "major_suppliers" else "affiliate")]


def main() -> None:
    facts, companies = load_facts()
    with CATALOG.open(encoding="utf-8-sig", newline="") as handle:
        catalog = list(csv.DictReader(handle))
    indexes = name_index(companies, catalog)
    known_names = sorted({name for rule in indexes.values() for name in rule if name}, key=lambda name: (-len(name), name))
    records = []
    for fact_id, (ticker, fact) in sorted(facts.items()):
        statement = fact["statement"]
        shares = SHARE.findall(statement)
        amounts = AMOUNT.findall(statement)
        extracted = [(name, kind, role) for name, kind, role in extract(fact, known_names)
                     if not name or name not in {companies[ticker]["legal_name"], companies[ticker]["company"]}]
        if not extracted:
            extracted = [("", "none", "customer" if fact["field"] == "major_customers" else "supplier" if fact["field"] == "major_suppliers" else "affiliate")]
        for name, kind, role in extracted:
            records.append({"fact_id": fact_id, "ticker": ticker, "field": fact["field"],
                            "counterparty": name, "counterparty_kind": kind, "role": role,
                            "period": fact["period"], "share_text": shares[0] if shares else "",
                            "amount_text": amounts[0].strip() if amounts else ""})
    DATA.mkdir(parents=True, exist_ok=True)
    (DATA / "counterparties.jsonl").write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in records), encoding="utf-8")
    print(len(facts), len(records), Counter(r["counterparty_kind"] for r in records))


if __name__ == "__main__":
    main()
