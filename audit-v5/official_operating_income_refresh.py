from __future__ import annotations

import argparse
import json
import re
import time
import urllib.parse
import urllib.request
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from official_financial_check import (
    SPECIALIZED_FINANCIAL_SECTORS,
    canonical_reports,
    field,
    load_official,
    parse_number,
    quarter_number,
    roc_year,
)

URL = "https://mopsfin.twse.com.tw/compare/data"


def request_metric(companies: list[tuple[str, str]], period: str, retries: int = 4) -> dict[str, Any]:
    year, quarter = period.split("Q")
    pairs = [
        ("compareItem", "OperatingIncome"),
        ("ylabel", "新台幣仟元"),
        ("quarter", "true"),
        ("revenue", "true"),
        ("ys", year),
        ("qnumber", quarter),
        ("bcodeAvg", "false"),
        ("companyAvg", "false"),
    ]
    pairs.extend(("companyId", f"{ticker} {company}") for ticker, company in companies)
    req = urllib.request.Request(
        URL,
        data=urllib.parse.urlencode(pairs).encode(),
        method="POST",
        headers={
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
            "Origin": "https://mopsfin.twse.com.tw",
            "Referer": "https://mopsfin.twse.com.tw/",
            "X-Requested-With": "XMLHttpRequest",
            "Accept": "application/json",
            "User-Agent": "My-TW-Coverage-audit-v5/1.0",
        },
    )
    last = None
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(req, timeout=90) as response:
                return json.load(response)
        except Exception as exc:
            last = exc
            time.sleep(1.0 + attempt * 1.5)
    raise last


def series_by_name(payload: dict[str, Any], period: str) -> dict[str, float]:
    periods = [str(x) for x in payload.get("xaxisList", [])]
    out: dict[str, float] = {}
    for series in payload.get("graphData", []):
        if not isinstance(series, dict):
            continue
        label = str(series.get("label", "")).strip()
        for point in series.get("data", []):
            if not isinstance(point, list) or len(point) < 2:
                continue
            idx, value = point[0], point[1]
            if isinstance(idx, int) and 0 <= idx < len(periods) and periods[idx] == period:
                n = parse_number(value)
                if label and n is not None:
                    out[label] = n / 1000.0
    return out


def replace_quarterly_cells(text: str, q1: float, q2: float) -> tuple[str, bool]:
    m = re.search(
        r"(^###\s+季度關鍵財務數據.*?$\n)([\s\S]*?)(?=^###\s+|\Z)",
        text,
        flags=re.MULTILINE,
    )
    if not m:
        return text, False

    lines = m.group(2).splitlines()
    table_idx = [i for i, line in enumerate(lines) if line.strip().startswith("|")]
    if len(table_idx) < 3:
        return text, False

    headers = [c.strip() for c in lines[table_idx[0]].strip().strip("|").split("|")]
    date_to_col = {d: i for i, d in enumerate(headers)}
    if "2026-03-31" not in date_to_col or "2026-06-30" not in date_to_col:
        return text, False

    revenue = {}
    row_indexes = {}
    for i in table_idx[2:]:
        cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
        if not cells:
            continue
        row_indexes[cells[0]] = i
        if cells[0] == "Revenue":
            for date in ("2026-03-31", "2026-06-30"):
                col = date_to_col[date]
                revenue[date] = parse_number(cells[col]) if col < len(cells) else None

    changed = False
    i = row_indexes.get("Operating Income")
    if i is not None:
        cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
        for date, value in {"2026-03-31": q1, "2026-06-30": q2}.items():
            col = date_to_col[date]
            if col < len(cells):
                cells[col] = f"{value:.2f}"
                changed = True
        lines[i] = "| " + " | ".join(cells) + " |"

    i = row_indexes.get("Operating Margin (%)")
    if i is not None:
        cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
        for date, op in {"2026-03-31": q1, "2026-06-30": q2}.items():
            rev = revenue.get(date)
            col = date_to_col[date]
            if rev not in (None, 0) and col < len(cells):
                cells[col] = f"{op / rev * 100:.2f}"
                changed = True
        lines[i] = "| " + " | ".join(cells) + " |"

    if not changed:
        return text, False
    return text[:m.start(2)] + "\n".join(lines) + text[m.end(2):], True


def chunks(items: list[Any], size: int) -> list[list[Any]]:
    return [items[i:i + size] for i in range(0, len(items), size)]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default="Pilot_Reports")
    ap.add_argument("--batch-size", type=int, default=20)
    ap.add_argument("--summary", default="audit-v5/generated/operating-income-refresh.json")
    args = ap.parse_args()

    reports = canonical_reports(Path(args.root))
    official, _, _ = load_official()
    official_by_code = {
        str(field(row, "code") or "").strip(): row
        for row in official
        if str(field(row, "code") or "").strip().isdigit()
    }

    targets = []
    for ticker, path in reports.items():
        row = official_by_code.get(ticker)
        if not row or path.parent.name in SPECIALIZED_FINANCIAL_SECTORS:
            continue
        if roc_year(field(row, "year")) != 2026 or quarter_number(field(row, "quarter")) != 2:
            continue
        targets.append((ticker, path.stem.split("_", 1)[1], path))

    results = []
    counts = Counter()
    for batch in chunks(targets, args.batch_size):
        request_companies = [(ticker, company) for ticker, company, _ in batch]
        try:
            q1_payload = request_metric(request_companies, "2026Q1")
            q2_payload = request_metric(request_companies, "2026Q2")
        except Exception as exc:
            for ticker, company, path in batch:
                results.append({
                    "ticker": ticker,
                    "company": company,
                    "path": path.as_posix(),
                    "status": "FETCH_FAILED",
                    "error": f"{type(exc).__name__}: {exc}",
                })
                counts["fetch_failed"] += 1
            continue

        q1_map = series_by_name(q1_payload, "2026Q1")
        q2_map = series_by_name(q2_payload, "2026Q2")

        for ticker, company, path in batch:
            q1 = q1_map.get(company)
            q2 = q2_map.get(company)
            if q1 is None or q2 is None:
                results.append({
                    "ticker": ticker,
                    "company": company,
                    "path": path.as_posix(),
                    "status": "MOPS_VALUE_MISSING",
                    "q1": q1,
                    "q2": q2,
                })
                counts["value_missing"] += 1
                continue

            text = path.read_text(encoding="utf-8")
            new_text, changed = replace_quarterly_cells(text, q1, q2)
            if changed:
                path.write_text(new_text, encoding="utf-8")
                counts["patched"] += 1
                status = "PATCHED"
            else:
                counts["unchanged_or_unpatchable"] += 1
                status = "UNCHANGED_OR_UNPATCHABLE"

            results.append({
                "ticker": ticker,
                "company": company,
                "path": path.as_posix(),
                "status": status,
                "official_q1_million": q1,
                "official_q2_million": q2,
            })
        time.sleep(0.15)

    payload = {
        "schema": "operating-income-refresh-1",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source": URL,
        "mapping": "MOPSFIN OperatingIncome -> MOPS 營業利益（損失）",
        "periods": ["2026Q1", "2026Q2"],
        "target_count": len(targets),
        "counts": dict(sorted(counts.items())),
        "results": results,
    }
    out = Path(args.summary)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in payload.items() if k != "results"}, ensure_ascii=False, indent=2))
    return 0 if counts["fetch_failed"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
