from __future__ import annotations

import argparse
import json
import re
import urllib.error
import urllib.request
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

MARKET_SOURCES = [
    ("twse-listed-general", "https://openapi.twse.com.tw/v1/opendata/t187ap06_L_ci"),
    ("tpex-otc-general", "https://www.tpex.org.tw/openapi/v1/mopsfin_t187ap06_O_ci"),
]
SUPPLEMENTAL_SOURCE = (
    "twse-public-general",
    "https://openapi.twse.com.tw/v1/opendata/t187ap06_X_ci",
)

FIELD_ALIASES = {
    "code": ("公司代號", "SecuritiesCompanyCode"),
    "name": ("公司名稱", "CompanyName"),
    "year": ("年度", "Year"),
    "quarter": ("季別", "Quarter", "Season"),
    "revenue": ("營業收入", "Revenue"),
    "gross_profit": ("營業毛利（毛損）", "營業毛利(毛損)", "GrossProfitLoss"),
    "operating_income": ("營業利益（損失）", "營業利益(損失)", "OperatingIncomeLoss"),
    "net_income": (
        "淨利（淨損）歸屬於母公司業主",
        "淨利(淨損)歸屬於母公司業主",
        "本期淨利（淨損）",
        "本期淨利(淨損)",
        "本期稅後淨利（淨損）",
        "ProfitLossAttributableToOwnersOfParent",
        "ProfitLoss",
    ),
}

REPO_ROWS = {
    "revenue": "Revenue",
    "gross_profit": "Gross Profit",
    "operating_income": "Operating Income",
    "net_income": "Net Income",
}

SPECIALIZED_FINANCIAL_SECTORS = {
    "Asset Management",
    "Banks",
    "Banks - Regional",
    "Capital Markets",
    "Credit Services",
    "Financial Conglomerates",
    "Insurance - Diversified",
    "Insurance - Life",
    "Insurance - Property & Casualty",
    "Insurance - Reinsurance",
    "Insurance Brokers",
}


def fetch_json(url: str, timeout: int = 60) -> tuple[list[dict[str, Any]] | None, dict[str, Any]]:
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "My-TW-Coverage-audit-v5/1.0", "Accept": "application/json"},
    )
    meta = {"url": url, "ok": False, "error": None, "row_count": 0}
    try:
        with urllib.request.urlopen(req, timeout=timeout) as response:
            data = json.load(response)
        if not isinstance(data, list):
            raise ValueError("expected JSON array")
        meta["ok"] = True
        meta["row_count"] = len(data)
        return data, meta
    except Exception as exc:
        meta["error"] = f"{type(exc).__name__}: {exc}"
        return None, meta


def field(row: dict[str, Any], key: str) -> Any:
    for alias in FIELD_ALIASES[key]:
        if alias in row:
            return row[alias]
    return None


def parse_number(value: Any) -> float | None:
    if value is None:
        return None
    raw = str(value).strip().replace(",", "")
    if raw in {"", "-", "--", "N/A", "nan", "None"}:
        return None
    if raw.startswith("(") and raw.endswith(")"):
        raw = "-" + raw[1:-1]
    raw = raw.replace("%", "")
    try:
        return float(raw)
    except ValueError:
        return None


def roc_year(value: Any) -> int | None:
    n = parse_number(value)
    if n is None:
        return None
    y = int(n)
    return y + 1911 if y < 1911 else y


def quarter_number(value: Any) -> int | None:
    if value is None:
        return None
    m = re.search(r"[1-4]", str(value))
    return int(m.group(0)) if m else None


def parse_markdown_table(section: str) -> dict[str, dict[str, float | None]]:
    lines = [line.strip() for line in section.splitlines() if line.strip().startswith("|")]
    if len(lines) < 3:
        return {}
    headers = [c.strip() for c in lines[0].strip("|").split("|")]
    if len(headers) < 2:
        return {}
    dates = headers[1:]
    out: dict[str, dict[str, float | None]] = {}
    for line in lines[2:]:
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 2:
            continue
        label = cells[0]
        out[label] = {}
        for date, raw in zip(dates, cells[1:]):
            out[label][date] = parse_number(raw)
    return out


def extract_section(text: str, heading_prefix: str) -> str:
    m = re.search(
        rf"^###\s+{re.escape(heading_prefix)}.*?$([\s\S]*?)(?=^###\s+|\Z)",
        text,
        flags=re.MULTILINE,
    )
    return m.group(1) if m else ""


def quarter_of_date(date_str: str) -> tuple[int, int] | None:
    m = re.match(r"(\d{4})-(\d{2})-(\d{2})", date_str)
    if not m:
        return None
    y, month = int(m.group(1)), int(m.group(2))
    q = {3: 1, 6: 2, 9: 3, 12: 4}.get(month)
    return (y, q) if q else None


def repo_metric_value(text: str, metric: str, year: int, quarter: int) -> tuple[float | None, str]:
    row_name = REPO_ROWS[metric]
    if quarter == 4:
        annual = parse_markdown_table(extract_section(text, "年度關鍵財務數據"))
        row = annual.get(row_name, {})
        for date, value in row.items():
            yq = quarter_of_date(date)
            if yq == (year, 4):
                return value, "annual"
        return None, "annual"

    quarterly = parse_markdown_table(extract_section(text, "季度關鍵財務數據"))
    row = quarterly.get(row_name, {})
    selected = []
    for date, value in row.items():
        yq = quarter_of_date(date)
        if yq and yq[0] == year and yq[1] <= quarter and value is not None:
            selected.append((yq[1], value))
    expected = set(range(1, quarter + 1))
    present = {q for q, _ in selected}
    if present != expected:
        return None, f"quarterly-ytd-missing:{sorted(expected - present)}"
    return sum(v for _, v in selected), "quarterly-ytd"


def canonical_reports(root: Path) -> dict[str, Path]:
    result: dict[str, Path] = {}
    for path in root.rglob("*.md"):
        m = re.match(r"^(\d{4,6})_(.+)\.md$", path.name)
        if not m:
            continue
        ticker = m.group(1)
        if ticker in result:
            raise RuntimeError(f"duplicate canonical ticker files: {ticker}")
        result[ticker] = path
    return result


def load_official() -> tuple[list[dict[str, Any]], list[dict[str, Any]], str]:
    combined: list[dict[str, Any]] = []
    metas: list[dict[str, Any]] = []
    seen_codes: set[str] = set()

    for name, url in MARKET_SOURCES:
        data, meta = fetch_json(url)
        meta["name"] = name
        metas.append(meta)
        if not data:
            continue
        for row in data:
            code = str(field(row, "code") or "").strip()
            if code:
                seen_codes.add(code)
            combined.append(row)

    # Supplemental public-company feed is not a substitute for listed/OTC feeds.
    # It only fills codes absent from the two market snapshots.
    sname, surl = SUPPLEMENTAL_SOURCE
    supplemental, smeta = fetch_json(surl)
    smeta["name"] = sname
    metas.append(smeta)
    if supplemental:
        for row in supplemental:
            code = str(field(row, "code") or "").strip()
            if code and code not in seen_codes:
                combined.append(row)
                seen_codes.add(code)

    ok_markets = [m["name"] for m in metas if m.get("ok") and m.get("name") in {x[0] for x in MARKET_SOURCES}]
    mode = "+".join(ok_markets) if ok_markets else "supplemental-only"
    return combined, metas, mode


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default="Pilot_Reports")
    ap.add_argument("--summary", default="audit-v5/generated/official-financial-summary.json")
    ap.add_argument("--details", default="audit-v5/work/official-financial-details.json")
    ap.add_argument("--tolerance-million", type=float, default=0.02)
    args = ap.parse_args()

    official, source_meta, source_mode = load_official()
    now = datetime.now(timezone.utc).isoformat()
    if not official:
        payload = {
            "schema": "official-financial-summary-1",
            "generated_at": now,
            "source_ok": False,
            "source_mode": source_mode,
            "sources": source_meta,
            "error": "No official income-statement rows could be fetched.",
        }
        out = Path(args.summary)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return 2

    reports = canonical_reports(Path(args.root))
    details = []
    ticker_results: dict[str, list[dict[str, Any]]] = {}
    field_names = sorted({k for row in official[:50] for k in row.keys()})
    official_by_code = {}
    for row in official:
        code = str(field(row, "code") or "").strip()
        if code and code.isdigit():
            official_by_code[code] = row

    counters = Counter()
    metric_counters = Counter()
    period_counter = Counter()
    period_unresolved_examples: list[dict[str, Any]] = []

    for ticker, path in reports.items():
        row = official_by_code.get(ticker)
        if not row:
            counters["no_official_row"] += 1
            continue
        year = roc_year(field(row, "year"))
        quarter = quarter_number(field(row, "quarter"))
        if not year or not quarter:
            counters["official_period_unresolved"] += 1
            if len(period_unresolved_examples) < 30:
                period_unresolved_examples.append({
                    "ticker": ticker,
                    "path": path.as_posix(),
                    "raw_year": field(row, "year"),
                    "raw_quarter": field(row, "quarter"),
                    "available_keys": sorted(row.keys()),
                })
            continue

        period_counter[f"{year}Q{quarter}"] += 1
        text = path.read_text(encoding="utf-8")
        ticker_items = []
        for metric in REPO_ROWS:
            official_raw = parse_number(field(row, metric))
            if official_raw is None:
                metric_counters[f"{metric}:official_missing"] += 1
                continue
            official_m = official_raw / 1000.0
            repo_value, repo_basis = repo_metric_value(text, metric, year, quarter)
            sector = path.parent.name
            reason = None
            if repo_value is None:
                status = "REPO_VALUE_UNAVAILABLE"
                metric_counters[f"{metric}:repo_missing"] += 1
                diff = None
            else:
                diff = repo_value - official_m
                tolerance = max(args.tolerance_million, abs(official_m) * 0.00005)
                if abs(diff) <= tolerance:
                    status = "AUTO_VERIFIED"
                    metric_counters[f"{metric}:verified"] += 1
                elif sector in SPECIALIZED_FINANCIAL_SECTORS:
                    status = "METHOD_UNRESOLVED"
                    reason = "specialized-financial-sector"
                    metric_counters[f"{metric}:method_unresolved"] += 1
                else:
                    status = "FINANCIAL_DIFFERENCE"
                    metric_counters[f"{metric}:difference"] += 1
            item = {
                "ticker": ticker,
                "company": path.stem.split("_", 1)[1] if "_" in path.stem else "",
                "path": path.as_posix(),
                "period": f"{year}Q{quarter}",
                "metric": metric,
                "repo_basis": repo_basis,
                "repo_value_million": repo_value,
                "official_value_million": official_m,
                "difference_million": diff,
                "status": status,
                "reason": reason,
            }
            details.append(item)
            ticker_items.append(item)
        if ticker_items:
            ticker_results[ticker] = ticker_items
            counters["matched_tickers"] += 1

    status_counts = Counter(d["status"] for d in details)
    summary = {
        "schema": "official-financial-summary-1",
        "generated_at": now,
        "source_ok": True,
        "source_mode": source_mode,
        "sources": source_meta,
        "official_row_count": len(official),
        "official_unique_company_count": len(official_by_code),
        "repo_report_count": len(reports),
        "matched_ticker_count": counters["matched_tickers"],
        "no_official_row_count": counters["no_official_row"],
        "official_period_unresolved_count": counters["official_period_unresolved"],
        "official_period_unresolved_examples": period_unresolved_examples,
        "period_counts": dict(sorted(period_counter.items())),
        "comparison_count": len(details),
        "status_counts": dict(sorted(status_counts.items())),
        "metric_counts": dict(sorted(metric_counters.items())),
        "official_field_names_sample": field_names,
        "top_differences": sorted(
            [d for d in details if d["status"] == "FINANCIAL_DIFFERENCE" and d["difference_million"] is not None],
            key=lambda d: abs(d["difference_million"]),
            reverse=True,
        )[:50],
        "coverage_note": (
            "Phase 1 validates current-period general-industry income-statement concepts only: "
            "revenue, gross profit, operating income and net income. Cash-flow/CAPEX and historical "
            "periods still require MOPS/XBRL coverage."
        ),
    }

    summary_path = Path(args.summary)
    details_path = Path(args.details)
    summary_path.parent.mkdir(parents=True, exist_ok=True)
    details_path.parent.mkdir(parents=True, exist_ok=True)
    summary_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    details_path.write_text(json.dumps({"summary": summary, "comparisons": details}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
