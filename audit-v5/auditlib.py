from __future__ import annotations

import hashlib
import json
import re
import sqlite3
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any, Iterable

REQUIRED_SECTIONS = ("業務簡介", "供應鏈位置", "主要客戶及供應商", "財務概況")
REQUIRED_METADATA = ("板塊", "產業", "市值", "企業價值")
PLACEHOLDER_PATTERNS = (
    r"待\s*AI\s*補充",
    r"待更新",
    r"待補",
    r"TODO",
    r"TBD",
    r"placeholder",
)
BANNED_GENERIC_WIKILINKS = {
    "大廠", "供應商", "客戶", "廠商", "原廠", "經銷商", "製造商", "業者", "企業", "公司"
}
HIGH_RISK_TERMS = (
    "最大", "第一", "唯一", "領先", "龍頭", "高毛利", "獲利引擎", "核心獲利", "主要獲利",
    "市占", "市佔", "主要客戶", "主要供應商", "打入", "出貨", "併購", "收購", "合併",
    "分割", "下市", "改名",
)
MEDIUM_RISK_TERMS = (
    "主要產品", "產能", "應用", "策略", "總部", "地址", "市場定位", "合作", "產品組合",
    "供應鏈", "出口", "外銷",
)

GEOGRAPHY_TERMS = (
    "美國", "中國", "日本", "韓國", "歐洲", "歐盟", "東南亞", "印度", "越南", "泰國", "墨西哥",
    "北美", "南美", "亞洲", "中東", "澳洲", "德國", "法國", "英國",
)

ATOMIC_STATUSES = {
    "PENDING_MACHINE", "AUTO_VERIFIED", "CARRY_FORWARD_ACCEPTED", "NEEDS_MODEL_REVIEW",
    "UNDER_REVIEW", "ACCEPTED", "PARTIALLY_SUPPORTED", "UNSUPPORTED", "METHOD_UNRESOLVED",
    "PERIOD_UNRESOLVED", "IDENTITY_UNRESOLVED", "UNRESOLVED_PDF", "SOURCE_UNAVAILABLE",
    "UNKNOWN_AFTER_RESEARCH", "REJECTED", "REVISION_REQUIRED", "BLOCKED",
}

DIMENSIONS = {
    "identity", "identity_history", "narrative", "supply_chain", "customers_suppliers",
    "financials", "valuation", "source_period_integrity",
}


def normalize_text(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    lines = [re.sub(r"[ \t]+", " ", line).strip() for line in text.split("\n")]
    return "\n".join(line for line in lines if line).strip()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def json_hash(value: Any) -> str:
    payload = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return sha256_text(payload)


@dataclass(frozen=True)
class BindingFingerprint:
    normalized_claim_hash: str
    source_raw_hash: str
    source_text_hash: str
    evidence_span_hash: str
    period_binding: str
    issuer_binding: str
    policy_binding: str

    @classmethod
    def from_dict(cls, value: dict[str, str]) -> "BindingFingerprint":
        return cls(**{k: value.get(k, "") for k in cls.__dataclass_fields__})


def carry_forward_eligible(previous: BindingFingerprint, current: BindingFingerprint) -> bool:
    return previous == current


@dataclass
class Check:
    code: str
    status: str
    message: str
    severity: str = "info"
    details: dict[str, Any] | None = None

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class ReportScan:
    path: str
    ticker: str | None
    company: str | None
    content_hash: str
    risk_class: str
    risk_reasons: list[str]
    checks: list[Check]

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        data["checks"] = [c.to_dict() for c in self.checks]
        return data


def _parse_sections(text: str) -> dict[str, str]:
    matches = list(re.finditer(r"^##\s+(.+?)\s*$", text, flags=re.MULTILINE))
    out: dict[str, str] = {}
    for i, match in enumerate(matches):
        start = match.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        out[match.group(1).strip()] = text[start:end].strip()
    return out


def _section_body(sections: dict[str, str], required: str) -> str | None:
    if required in sections:
        return sections[required]
    matches = [body for heading, body in sections.items() if heading.startswith(required)]
    if len(matches) == 1:
        return matches[0]
    return None


def _filename_identity(path: Path) -> tuple[str | None, str | None]:
    match = re.match(r"^(\d{4,6})_(.+)\.md$", path.name)
    if not match:
        return None, None
    return match.group(1), match.group(2)


def _normalize_identity_label(raw: str) -> str:
    raw = re.sub(r"\[\[([^\]]+)\]\]", r"\1", raw)
    raw = raw.replace("*", "")
    raw = re.sub(r"\s+", " ", raw).strip()
    return raw


def _title_identity(text: str) -> tuple[str | None, str | None]:
    heading = re.search(r"^#\s*(.+?)\s*$", text, flags=re.MULTILINE)
    if not heading:
        return None, None
    raw_heading = heading.group(1).strip()
    if "{" in raw_heading or "}" in raw_heading or "file.replace" in raw_heading:
        return None, None
    match = re.fullmatch(r"(\d{4,6})\s*(?:-|_)\s*(.+?)", raw_heading)
    if not match:
        return None, None
    ticker = match.group(1)
    company = _normalize_identity_label(match.group(2))
    return ticker, company


def _narrative_risk_text(text: str) -> str:
    """Return only narrative sections that can contain semantic business claims."""
    sections = _parse_sections(text)
    bodies = []
    for name in ("業務簡介", "供應鏈位置", "主要客戶及供應商"):
        body = _section_body(sections, name)
        if body:
            bodies.append(body)
    return "\n".join(bodies)


def _claim_lines(text: str) -> list[str]:
    """Split narrative text into claim-like lines/sentences, excluding labels/tables/metadata."""
    claims: list[str] = []
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or line.startswith("|"):
            continue
        line = re.sub(r"^[-*+]\s+", "", line)
        # Remove a leading bold label (e.g. **主要客戶:**), but keep any factual tail.
        line = re.sub(r"^\*\*[^*]+:\*\*\s*", "", line)
        if not line:
            continue
        for part in re.split(r"(?<=[。；！？!?])\s*", line):
            part = part.strip()
            if part:
                claims.append(part)
    return claims


def _has_named_entity(claim: str) -> bool:
    # Wikilinks are the project's strongest deterministic proxy for named entities.
    return bool(re.search(r"\[\[[^\]]+\]\]", claim))


def risk_signals(text: str) -> list[dict[str, str]]:
    """Extract calibrated semantic risk signals from narrative claims."""
    signals: list[dict[str, str]] = []
    for claim in _claim_lines(text):
        normalized = re.sub(r"\s+", " ", claim).strip()

        # Ranking / market-position assertions.
        if re.search(r"(?:全球|世界|台灣|國內|亞洲|業界|市場)?(?:最大|第一|唯一|領先|龍頭)", normalized) or re.search(r"市[占佔](?:率)?", normalized):
            signals.append({"level": "HIGH", "type": "ranking_or_market_share", "claim": normalized})
            continue

        # Profitability / earnings-contribution assertions.
        if re.search(r"(?:高毛利|獲利引擎|核心獲利|主要獲利|主要獲利來源|成長引擎)", normalized):
            signals.append({"level": "HIGH", "type": "profitability_assertion", "claim": normalized})
            continue

        # Material corporate-history events.
        if re.search(r"(?:併購|收購|合併|分割|下市|改名|更名)", normalized):
            signals.append({"level": "HIGH", "type": "corporate_event", "claim": normalized})
            continue

        # Named customer/supplier/commercial relationships. A relationship word alone
        # is not enough; require a named entity in the same claim.
        relation = re.search(
            r"(?:主要客戶|主要供應商|客戶包括|客戶為|供應商包括|供應商為|"
            r"向.+採購|採購自|供應(?:給|予|商)?|出貨(?:給|予|至)?|打入.+供應鏈|"
            r"成為.+供應商|Design[- ]?in)",
            normalized,
            flags=re.IGNORECASE,
        )
        if relation and _has_named_entity(normalized):
            signals.append({"level": "HIGH", "type": "named_commercial_relationship", "claim": normalized})
            continue

        # Export assertions become HIGH only when a concrete geography or percentage is asserted.
        if re.search(r"(?:出口|外銷)", normalized):
            if any(term in normalized for term in GEOGRAPHY_TERMS) or re.search(r"\d+(?:\.\d+)?\s*%", normalized):
                signals.append({"level": "HIGH", "type": "specific_export_assertion", "claim": normalized})
            else:
                signals.append({"level": "MEDIUM", "type": "generic_export", "claim": normalized})
            continue

        # General dynamic business assertions remain MEDIUM.
        medium_patterns = (
            r"主要產品", r"產能", r"應用", r"策略", r"總部", r"地址",
            r"市場定位", r"合作", r"產品組合", r"供應鏈",
        )
        if any(re.search(p, normalized) for p in medium_patterns):
            signals.append({"level": "MEDIUM", "type": "dynamic_business_claim", "claim": normalized})

    return signals


def classify_risk(text: str, extra_reasons: Iterable[str] = ()) -> tuple[str, list[str]]:
    reasons = list(extra_reasons)
    signals = risk_signals(text)
    high = [s for s in signals if s["level"] == "HIGH"]
    medium = [s for s in signals if s["level"] == "MEDIUM"]

    reasons.extend(f'high-signal:{s["type"]}' for s in high)
    reasons.extend(f'medium-signal:{s["type"]}' for s in medium)

    if high or any(
        r.startswith("identity-")
        or r.startswith("financial-")
        or r.startswith("structure-missing:")
        for r in reasons
    ):
        return "HIGH", sorted(set(reasons))
    if medium or reasons:
        return "MEDIUM", sorted(set(reasons))
    return "LOW", []


def scan_report(path: Path) -> ReportScan:
    text = path.read_text(encoding="utf-8")
    normalized = normalize_text(text)
    checks: list[Check] = []
    risk_reasons: list[str] = []

    file_ticker, file_company = _filename_identity(path)
    title_ticker, title_company = _title_identity(text)

    if not file_ticker:
        checks.append(Check("identity.filename", "IDENTITY_UNRESOLVED", "檔名不是 XXXX_公司名.md 格式", "error"))
        risk_reasons.append("identity-filename-invalid")
    else:
        checks.append(Check("identity.filename", "AUTO_VERIFIED", "檔名格式可解析"))

    if not title_ticker:
        checks.append(Check("identity.title", "IDENTITY_UNRESOLVED", "標題無法解析 ticker/company", "error"))
        risk_reasons.append("identity-title-invalid")
    elif file_ticker and (file_ticker != title_ticker or file_company != title_company):
        checks.append(Check(
            "identity.filename_title_match", "IDENTITY_UNRESOLVED", "檔名與標題身份不一致", "error",
            {"filename": [file_ticker, file_company], "title": [title_ticker, title_company]},
        ))
        risk_reasons.append("identity-filename-title-conflict")
    else:
        checks.append(Check("identity.filename_title_match", "AUTO_VERIFIED", "檔名與標題身份一致"))

    section_headings = re.findall(r"^##\s+(.+?)\s*$", text, flags=re.MULTILINE)
    duplicate_headings = sorted({h for h in section_headings if section_headings.count(h) > 1})
    if duplicate_headings:
        checks.append(Check(
            "structure.duplicate_section_heading",
            "REVISION_REQUIRED",
            "偵測到重複的二級章節標題",
            "warning",
            {"headings": duplicate_headings},
        ))
        risk_reasons.append("duplicate-section-heading")
    else:
        checks.append(Check("structure.duplicate_section_heading", "AUTO_VERIFIED", "二級章節標題無重複"))

    sections = _parse_sections(text)
    for section in REQUIRED_SECTIONS:
        body = _section_body(sections, section)
        if body is not None and body.strip():
            checks.append(Check(f"structure.section.{section}", "AUTO_VERIFIED", f"存在必要章節：{section}"))
        else:
            checks.append(Check(f"structure.section.{section}", "BLOCKED", f"缺少必要章節：{section}", "error"))
            risk_reasons.append(f"structure-missing:{section}")

    business = _section_body(sections, "業務簡介") or ""
    for field in REQUIRED_METADATA:
        match = re.search(rf"^\*\*{re.escape(field)}:\*\*\s*(.+?)\s*$", business, flags=re.MULTILINE)
        if match and match.group(1).strip() and "待" not in match.group(1):
            checks.append(Check(f"metadata.{field}", "AUTO_VERIFIED", f"metadata 已填：{field}"))
        else:
            checks.append(Check(f"metadata.{field}", "NEEDS_MODEL_REVIEW", f"metadata 缺失或不可用：{field}", "warning"))
            risk_reasons.append(f"metadata-missing:{field}")

    for pattern in PLACEHOLDER_PATTERNS:
        if re.search(pattern, text, flags=re.IGNORECASE):
            checks.append(Check("content.placeholder", "REVISION_REQUIRED", f"偵測到 placeholder：{pattern}", "warning"))
            risk_reasons.append("placeholder")

    wikilinks = re.findall(r"\[\[([^\]]+)\]\]", text)
    bad_generic = sorted({w.strip() for w in wikilinks if w.strip() in BANNED_GENERIC_WIKILINKS})
    if bad_generic:
        checks.append(Check("wikilink.generic", "REVISION_REQUIRED", "存在禁止的泛稱 wikilink", "warning", {"values": bad_generic}))
        risk_reasons.append("generic-wikilink")
    else:
        checks.append(Check("wikilink.generic", "AUTO_VERIFIED", "未偵測到禁止的泛稱 wikilink"))

    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", text) if len(normalize_text(p)) >= 80]
    seen: dict[str, int] = {}
    duplicates: list[str] = []
    for p in paragraphs:
        h = sha256_text(normalize_text(p))
        if h in seen:
            duplicates.append(h)
        seen[h] = seen.get(h, 0) + 1
    if duplicates:
        checks.append(Check("content.duplicate_paragraph", "NEEDS_MODEL_REVIEW", "偵測到完全重複的長段落", "warning", {"hashes": sorted(set(duplicates))}))
        risk_reasons.append("duplicate-paragraph")

    risk_input = _narrative_risk_text(text)
    risk_class, risk_reasons = classify_risk(risk_input, risk_reasons)
    return ReportScan(
        path=str(path), ticker=file_ticker or title_ticker, company=file_company or title_company,
        content_hash=sha256_text(normalized), risk_class=risk_class,
        risk_reasons=risk_reasons, checks=checks,
    )


def financial_auto_verify(*, issuer_match: bool, period_match: bool, statement_scope_match: bool,
                          currency_match: bool, unit_match: bool, mapping_unambiguous: bool,
                          original_value: float | None, official_value: float | None,
                          tolerance: float = 0.005) -> str:
    prerequisites = (
        issuer_match, period_match, statement_scope_match, currency_match, unit_match, mapping_unambiguous,
        original_value is not None, official_value is not None,
    )
    if not all(prerequisites):
        return "METHOD_UNRESOLVED"
    if abs(float(original_value) - float(official_value)) <= tolerance:
        return "AUTO_VERIFIED"
    return "NEEDS_MODEL_REVIEW"


def init_db(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(path) as conn:
        conn.executescript(
            """
            PRAGMA journal_mode=WAL;
            CREATE TABLE IF NOT EXISTS meta (key TEXT PRIMARY KEY, value TEXT NOT NULL);
            CREATE TABLE IF NOT EXISTS issuers (
                issuer_id TEXT PRIMARY KEY,
                ticker TEXT,
                company TEXT,
                overall_state TEXT NOT NULL DEFAULT 'NEEDS_REVIEW',
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            );
            CREATE TABLE IF NOT EXISTS atomic_items (
                item_id TEXT PRIMARY KEY,
                issuer_id TEXT NOT NULL,
                dimension TEXT NOT NULL,
                status TEXT NOT NULL,
                risk_class TEXT NOT NULL,
                normalized_claim_hash TEXT,
                source_raw_hash TEXT,
                source_text_hash TEXT,
                evidence_span_hash TEXT,
                period_binding TEXT,
                issuer_binding TEXT,
                policy_binding TEXT,
                carry_forward_from TEXT,
                origin_engine TEXT,
                origin_item_id TEXT,
                payload_json TEXT NOT NULL DEFAULT '{}',
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (issuer_id) REFERENCES issuers(issuer_id)
            );
            CREATE TABLE IF NOT EXISTS events (
                event_id INTEGER PRIMARY KEY AUTOINCREMENT,
                issuer_id TEXT,
                item_id TEXT,
                event_type TEXT NOT NULL,
                actor_session TEXT,
                model TEXT,
                effort TEXT,
                payload_json TEXT NOT NULL DEFAULT '{}',
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            );
            CREATE TABLE IF NOT EXISTS migrations (
                migration_id TEXT PRIMARY KEY,
                source_engine TEXT NOT NULL,
                target_engine TEXT NOT NULL,
                source_manifest_hash TEXT NOT NULL,
                status TEXT NOT NULL,
                counts_json TEXT NOT NULL,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            );
            """
        )
        conn.execute("INSERT OR REPLACE INTO meta(key,value) VALUES('engine','audit-engine-v5')")
        conn.execute("INSERT OR REPLACE INTO meta(key,value) VALUES('protocol','1.2.0-draft')")


def validate_v4_export(payload: dict[str, Any]) -> dict[str, Any]:
    manifest = payload.get("manifest")
    items = payload.get("items")
    errors: list[str] = []
    if not isinstance(manifest, dict):
        errors.append("manifest missing")
    if not isinstance(items, list):
        errors.append("items missing")
        items = []
    ids: set[str] = set()
    duplicate_ids: list[str] = []
    for item in items:
        item_id = str(item.get("item_id", ""))
        if not item_id:
            errors.append("item without item_id")
            continue
        if item_id in ids:
            duplicate_ids.append(item_id)
        ids.add(item_id)
        for required in ("issuer_id", "status", "origin_engine"):
            if not item.get(required):
                errors.append(f"{item_id}: missing {required}")
    if duplicate_ids:
        errors.append(f"duplicate item ids: {sorted(set(duplicate_ids))[:10]}")
    return {
        "ok": not errors,
        "errors": errors,
        "item_count": len(items),
        "unique_item_count": len(ids),
        "manifest_hash": json_hash(manifest) if isinstance(manifest, dict) else None,
    }
