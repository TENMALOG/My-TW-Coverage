from __future__ import annotations

import argparse
import json
import re
import time
import urllib.parse
import urllib.request
from collections import Counter
from pathlib import Path
from typing import Any

from bs4 import BeautifulSoup

MOPSFIN_REPORT = "https://mopsfin.twse.com.tw/compare/report"
METRIC_LABELS = {
    "revenue": ("營業收入合計", "營業收入"),
    "gross_profit": ("營業毛利（毛損）淨額", "營業毛利（毛損）"),
    "net_income": ("母公司業主（淨利∕損）", "母公司業主（淨利／損）"),
}
ROW_NAMES = {
    "revenue": "Revenue",
    "gross_profit": "Gross Profit",
    "net_income": "Net Income",
}


def parse_number(raw: str | None) -> float | None:
    if raw is None:
        return None
    s = raw.strip().replace(",", "")
    if not s or s in {"-", "--"}:
        return None
    if s.startswith("(") and s.endswith(")"):
        s = "-" + s[1:-1]
    try:
        return float(s)
    except ValueError:
        return None


def fetch_statement(company_id: str, period: str, retries: int = 4) -> str:
    pairs = [
        ("compareItem", "IncomeStatement"),
        ("ylabel", "新台幣仟元"),
        ("quarter", "true"),
        ("revenue", "true"),
        ("ys", period),
        ("qnumber", ""),
        ("bcodeAvg", "false"),
        ("companyAvg", "false"),
        ("companyId", company_id),
    ]
    body = urllib.parse.urlencode(pairs).encode()
    req = urllib.request.Request(
        MOPSFIN_REPORT,
        data=body,
        method="POST",
        headers={
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
            "Origin": "https://mopsfin.twse.com.tw",
            "Referer": "https://mopsfin.twse.com.tw/",
            "X-Requested-With": "XMLHttpRequest",
            "Accept": "text/html,*/*;q=0.8",
            "User-Agent": "My-TW-Coverage-audit-v5/1.0",
        },
    )
    last = None
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(req, timeout=60) as response:
                return response.read().decode("utf-8", errors="replace")
        except Exception as exc:
            last = exc
            time.sleep(1 + attempt)
    raise last


def statement_rows(raw: str) -> dict[str, float]:
    soup = BeautifulSoup(raw, "html.parser")
    tables = [t for t in soup.find_all("table") if not t.find_parent("table")]
    if len(tables) < 2:
        return {}
    label_rows = []
    value_rows = []
    for table, dest in ((tables[0], label_rows), (tables[1], value_rows)):
        for tr in table.find_all("tr"):
            if tr.find_parent("table") is not table:
                continue
            cells = [c.get_text(" ", strip=True) for c in tr.find_all(["th", "td"], recursive=False)]
            if cells:
                dest.append(cells)
    out: dict[str, float] = {}
    for idx, labels in enumerate(label_rows):
        if idx >= len(value_rows):
            break
        label = labels[0].strip() if labels else ""
        vals = value_rows[idx]
        value = parse_number(vals[0] if vals else None)
        if label and value is not None:
            out[label] = value
    return out


def metric_value(rows: dict[str, float], metric: str) -> float | None:
    for label in METRIC_LABELS[metric]:
        if label in rows:
            return rows[label]
    return None


def parse_quarter_table(text: str) -> tuple[list[str], dict[str, list[str]], list[str], re.Match[str]]:
    m = re.search(
        r"(^### 季度關鍵財務數據.*?\n)(\|.*?\n\|.*?\n(?:\|.*?\n)+)",
        text,
        flags=re.MULTILINE,
    )
    if not m:
        raise ValueError("quarterly table not found")
    lines = [line for line in m.group(2).splitlines() if line.startswith("|")]
    headers = [c.strip() for c in lines[0].strip("|").split("|")]
    rows: dict[str, list[str]] = {}
    order: list[str] = []
    for line in lines[2:]:
        cells = [c.strip() for c in line.strip("|").split("|")]
        if not cells:
            continue
        rows[cells[0]] = cells[1:]
        order.append(cells[0])
    return headers[1:], rows, order, m


def render_quarter_table(headers: list[str], rows: dict[str, list[str]], order: list[str]) -> str:
    first_width = 25
    out = ["| " + " " * first_width + " | " + " | ".join(headers) + " |"]
    out.append("|:" + "-" * first_width + "|" + "|".join("-" * (len(h) + 2) + ":" for h in headers) + "|")
    for label in order:
        out.append("| " + label.ljust(first_width) + " | " + " | ".join(rows[label]) + " |")
    return "\n".join(out) + "\n"


def patch_report(path: Path, replacements: dict[str, tuple[float, float]]) -> bool:
    text = path.read_text(encoding="utf-8")
    headers, rows, order, match = parse_quarter_table(text)
    try:
        q2_idx = headers.index("2026-06-30")
        q1_idx = headers.index("2026-03-31")
    except ValueError:
        return False

    changed = False
    for metric, (q1_m, q2_single_m) in replacements.items():
        row_name = ROW_NAMES[metric]
        if row_name not in rows:
            continue
        rows[row_name][q1_idx] = f"{q1_m:.2f}"
        rows[row_name][q2_idx] = f"{q2_single_m:.2f}"
        changed = True

    def num(label: str, idx: int) -> float | None:
        try:
            return float(rows[label][idx].replace(",", ""))
        except Exception:
            return None

    for idx in (q1_idx, q2_idx):
        rev = num("Revenue", idx)
        gp = num("Gross Profit", idx)
        op = num("Operating Income", idx)
        ni = num("Net Income", idx)
        if rev not in (None, 0):
            if gp is not None and "Gross Margin (%)" in rows:
                rows["Gross Margin (%)"][idx] = f"{gp / rev * 100:.2f}"
            if op is not None and "Operating Margin (%)" in rows:
                rows["Operating Margin (%)"][idx] = f"{op / rev * 100:.2f}"
            if ni is not None and "Net Margin (%)" in rows:
                rows["Net Margin (%)"][idx] = f"{ni / rev * 100:.2f}"

    if not changed:
        return False

    new_table = render_quarter_table(headers, rows, order)
    new_text = text[:match.start(2)] + new_table + text[match.end(2):]
    path.write_text(new_text, encoding="utf-8")
    return True


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--summary", default="audit-v5/generated/official-financial-summary.json")
    ap.add_argument("--output", default="audit-v5/generated/financial-difference-resolution.json")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--tolerance-million", type=float, default=0.02)
    args = ap.parse_args()

    source = json.loads(Path(args.summary).read_text(encoding="utf-8"))
    targets = [d for d in source.get("differences", []) if d.get("metric") != "operating_income"]
    grouped: dict[str, list[dict[str, Any]]] = {}
    for item in targets:
        grouped.setdefault(item["ticker"], []).append(item)

    results = []
    patch_plan: dict[str, dict[str, tuple[float, float]]] = {}
    counters = Counter()

    for ticker, items in grouped.items():
        company = items[0]["company"]
        company_id = f"{ticker} {company}"
        try:
            q1_rows = statement_rows(fetch_statement(company_id, "20261"))
            q2_rows = statement_rows(fetch_statement(company_id, "20262"))
            time.sleep(0.2)
        except Exception as exc:
            for item in items:
                results.append({**item, "disposition": "UNKNOWN", "resolution_reason": f"mopsfin-fetch:{type(exc).__name__}:{exc}"})
                counters["UNKNOWN"] += 1
            continue

        for item in items:
            metric = item["metric"]
            q1_raw = metric_value(q1_rows, metric)
            q2_ytd_raw = metric_value(q2_rows, metric)
            if q1_raw is None or q2_ytd_raw is None:
                disposition = "UNKNOWN"
                counters[disposition] += 1
                results.append({
                    **item,
                    "disposition": disposition,
                    "resolution_reason": "mopsfin-row-unavailable",
                })
                continue

            q1_m = q1_raw / 1000.0
            q2_ytd_m = q2_ytd_raw / 1000.0
            q2_single_m = q2_ytd_m - q1_m
            official = float(item["official_value_million"])
            tol = max(args.tolerance_million, abs(official) * 0.00005)
            official_agrees = abs(q2_ytd_m - official) <= tol

            if official_agrees:
                disposition = "REPO_WRONG_CONFIRMED_OFFICIAL"
                reason = "twse/tpex-openapi-and-mopsfin-statement-agree"
                patch_plan.setdefault(item["path"], {})[metric] = (q1_m, q2_single_m)
            else:
                disposition = "SOURCE_SCOPE_DIFFERENCE"
                reason = "official-sources-disagree-on-q2-ytd"
            counters[disposition] += 1
            results.append({
                **item,
                "mopsfin_q1_million": q1_m,
                "mopsfin_q2_ytd_million": q2_ytd_m,
                "mopsfin_q2_single_million": q2_single_m,
                "openapi_vs_mopsfin_difference_million": q2_ytd_m - official,
                "disposition": disposition,
                "resolution_reason": reason,
            })

    patched_files = []
    if args.apply:
        for raw_path, replacements in patch_plan.items():
            path = Path(raw_path)
            if patch_report(path, replacements):
                patched_files.append(raw_path)

    payload = {
        "schema": "financial-difference-resolution-1",
        "input_difference_count": len(targets),
        "ticker_count": len(grouped),
        "disposition_counts": dict(sorted(counters.items())),
        "apply": args.apply,
        "patched_file_count": len(patched_files),
        "patched_files": sorted(patched_files),
        "results": results,
    }
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "input_difference_count": payload["input_difference_count"],
        "disposition_counts": payload["disposition_counts"],
        "patched_file_count": payload["patched_file_count"],
        "output": str(out),
    }, ensure_ascii=False, indent=2))
    return 0 if not counters.get("UNKNOWN") else 1


if __name__ == "__main__":
    raise SystemExit(main())
