from __future__ import annotations

import json
import re
import time
from pathlib import Path

from credit_services_refresh import fetch_statement, statement_rows, metric_value

SUMMARY = Path("audit-v5/generated/official-financial-summary.json")
ROW_NAMES = {
    "revenue": "Revenue",
    "gross_profit": "Gross Profit",
    "operating_income": "Operating Income",
    "net_income": "Net Income",
}
MARGIN_ROWS = {
    "gross_profit": "Gross Margin (%)",
    "operating_income": "Operating Margin (%)",
    "net_income": "Net Margin (%)",
}
SEMIANNUAL_YTD_TICKERS = {"3659", "4546", "6618"}
ROW_ORDER = [
    "Revenue",
    "Gross Profit",
    "Gross Margin (%)",
    "Operating Income",
    "Operating Margin (%)",
    "Net Income",
    "Net Margin (%)",
]


def num(raw):
    if raw is None:
        return None
    s = str(raw).strip().replace(",", "")
    if not s or s in {"-", "--", "N/A", "None"}:
        return None
    try:
        return float(s)
    except ValueError:
        return None


def section_match(text: str):
    return re.search(
        r"(^###\s+季度關鍵財務數據.*?$\n)([\s\S]*?)(?=^###\s+|\Z)",
        text,
        flags=re.MULTILINE,
    )


def parse_existing_table(block: str):
    lines = [line for line in block.splitlines() if line.strip().startswith("|")]
    if len(lines) < 3:
        return [], {}, []
    headers = [c.strip() for c in lines[0].strip().strip("|").split("|")][1:]
    rows = {}
    order = []
    for line in lines[2:]:
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if not cells:
            continue
        label = cells[0]
        rows[label] = cells[1:]
        order.append(label)
    return headers, rows, order


def ensure_2026_columns(headers, rows):
    for date in ("2026-03-31", "2026-06-30"):
        if date not in headers:
            headers.insert(0, date)
            for label in list(rows):
                rows[label].insert(0, "-")
    return headers, rows


def ensure_core_rows(headers, rows, order):
    for label in ROW_ORDER:
        if label not in rows:
            rows[label] = ["-"] * len(headers)
            order.append(label)
        elif len(rows[label]) < len(headers):
            rows[label] += ["-"] * (len(headers) - len(rows[label]))
    return rows, order


def render_table(headers, rows, order):
    out = ["|                         | " + " | ".join(headers) + " |"]
    out.append("|:------------------------|" + "|".join("-" * (len(h) + 2) + ":" for h in headers) + "|")
    for label in order:
        vals = rows[label]
        if len(vals) < len(headers):
            vals = vals + ["-"] * (len(headers) - len(vals))
        out.append("| " + label.ljust(25) + " | " + " | ".join(vals[:len(headers)]) + " |")
    return "\n".join(out) + "\n"


def official_q1(ticker: str, company: str):
    raw = statement_rows(fetch_statement(ticker, company, "20261"))
    out = {}
    for metric in ROW_NAMES:
        value = metric_value(raw, metric)
        if value is not None:
            out[metric] = value / 1000.0
    return out


def patch_report(path: Path, items, q1_official, ticker: str):
    text = path.read_text(encoding="utf-8")
    match = section_match(text)
    if not match:
        raise RuntimeError("quarterly section not found")

    headers, rows, order = parse_existing_table(match.group(2))

    if ticker in SEMIANNUAL_YTD_TICKERS:
        if "2026-06-30" not in headers:
            headers.insert(0, "2026-06-30")
            for label in list(rows):
                rows[label].insert(0, "-")
        rows, order = ensure_core_rows(headers, rows, order)
        q2i = headers.index("2026-06-30")
        changes = []
        failures = []
        for item in items:
            metric = item["metric"]
            row_name = ROW_NAMES[metric]
            official_ytd = float(item["official_value_million"])
            rows[row_name][q2i] = f"{official_ytd:.2f}"
            changes.append({
                "metric": metric,
                "h1_ytd_million": official_ytd,
                "method": "OFFICIAL_H1_YTD_DIRECT",
            })

        revenue = num(rows["Revenue"][q2i])
        if revenue not in (None, 0):
            for metric, margin_row in MARGIN_ROWS.items():
                value = num(rows[ROW_NAMES[metric]][q2i])
                if value is not None:
                    rows[margin_row][q2i] = f"{value / revenue * 100:.2f}"

        if changes:
            new_block = render_table(headers, rows, order)
            path.write_text(text[:match.start(2)] + new_block + text[match.end(2):], encoding="utf-8")
        return changes, failures

    headers, rows = ensure_2026_columns(headers, rows)
    rows, order = ensure_core_rows(headers, rows, order)

    q1i = headers.index("2026-03-31")
    q2i = headers.index("2026-06-30")
    changes = []
    failures = []

    for item in items:
        metric = item["metric"]
        row_name = ROW_NAMES[metric]
        official_ytd = float(item["official_value_million"])
        q1 = num(rows[row_name][q1i])
        q2 = num(rows[row_name][q2i])

        if q1 is None and q2 is None:
            q1 = q1_official.get(metric)
            if q1 is None:
                failures.append({"metric": metric, "reason": "official_q1_unavailable"})
                continue
            q2 = official_ytd - q1
            method = "MOPS_Q1_PLUS_OFFICIAL_Q2_YTD_RESIDUAL"
        elif q1 is None:
            q1 = official_ytd - q2
            method = "OFFICIAL_YTD_MINUS_EXISTING_Q2"
        elif q2 is None:
            q2 = official_ytd - q1
            method = "OFFICIAL_YTD_MINUS_EXISTING_Q1"
        else:
            failures.append({"metric": metric, "reason": "checker_missing_but_both_cells_present"})
            continue

        rows[row_name][q1i] = f"{q1:.2f}"
        rows[row_name][q2i] = f"{q2:.2f}"
        changes.append({
            "metric": metric,
            "q1_million": q1,
            "q2_single_million": q2,
            "official_q2_ytd_million": official_ytd,
            "method": method,
        })

    for idx in (q1i, q2i):
        revenue = num(rows["Revenue"][idx])
        if revenue in (None, 0):
            continue
        for metric, margin_row in MARGIN_ROWS.items():
            value = num(rows[ROW_NAMES[metric]][idx])
            if value is not None:
                rows[margin_row][idx] = f"{value / revenue * 100:.2f}"

    if changes:
        new_block = render_table(headers, rows, order)
        path.write_text(text[:match.start(2)] + new_block + text[match.end(2):], encoding="utf-8")
    return changes, failures


def main():
    summary = json.loads(SUMMARY.read_text(encoding="utf-8"))
    targets = summary.get("repo_value_unavailable", [])
    grouped = {}
    for item in targets:
        grouped.setdefault(item["path"], []).append(item)

    results = []
    patched_items = 0
    failures_total = 0

    for path_s, items in sorted(grouped.items()):
        first = items[0]
        try:
            q1 = {} if first["ticker"] in SEMIANNUAL_YTD_TICKERS else official_q1(first["ticker"], first["company"])
            changes, failures = patch_report(Path(path_s), items, q1, first["ticker"])
        except Exception as exc:
            changes = []
            failures = [{"metric": "*", "reason": "exception", "error": f"{type(exc).__name__}: {exc}"}]

        patched_items += len(changes)
        failures_total += len(failures)
        results.append({
            "ticker": first["ticker"],
            "company": first["company"],
            "path": path_s,
            "target_count": len(items),
            "changes": changes,
            "failures": failures,
        })
        time.sleep(0.15)

    out = {
        "schema": "repo-value-unavailable-close-2",
        "input_count": len(targets),
        "patched_count": patched_items,
        "failure_count": failures_total,
        "results": results,
    }
    Path("audit-v5/generated/repo-value-unavailable-close.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps({k: v for k, v in out.items() if k != "results"}, ensure_ascii=False, indent=2))
    if failures_total:
        print(json.dumps(
            [{"ticker": r["ticker"], "company": r["company"], "path": r["path"], "failures": r["failures"]} for r in results if r["failures"]],
            ensure_ascii=False,
            indent=2,
        ))
    raise SystemExit(0 if failures_total == 0 else 2)


if __name__ == "__main__":
    main()
