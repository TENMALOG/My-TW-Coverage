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

from bs4 import BeautifulSoup

from official_financial_check import parse_number

URL = "https://mopsfin.twse.com.tw/compare/report"

LABELS = {
    "revenue": ("營業收入合計", "營業收入"),
    "gross_profit": ("營業毛利（毛損）淨額", "營業毛利（毛損）"),
    "operating_income": ("營業利益（損失）",),
    "net_income": ("母公司業主（淨利∕損）", "淨利（淨損）歸屬於母公司業主"),
}


def fetch_statement(ticker: str, company: str, period_code: str, retries: int = 4) -> str:
    pairs = [
        ("compareItem", "IncomeStatement"),
        ("ylabel", "新台幣仟元"),
        ("quarter", "true"),
        ("revenue", "true"),
        ("ys", period_code),
        ("qnumber", ""),
        ("bcodeAvg", "false"),
        ("companyAvg", "false"),
        ("companyId", f"{ticker} {company}"),
    ]
    req = urllib.request.Request(
        URL,
        data=urllib.parse.urlencode(pairs).encode(),
        method="POST",
        headers={
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
            "Origin": "https://mopsfin.twse.com.tw",
            "Referer": "https://mopsfin.twse.com.tw/",
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": "My-TW-Coverage-audit-v5/1.0",
        },
    )
    last = None
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(req, timeout=90) as response:
                return response.read().decode("utf-8", errors="replace")
        except Exception as exc:
            last = exc
            time.sleep(1.0 + attempt * 1.5)
    raise last


def tables(raw: str) -> list[list[list[str]]]:
    soup = BeautifulSoup(raw, "html.parser")
    out = []
    for table in [t for t in soup.find_all("table") if not t.find_parent("table")]:
        rows = []
        for tr in table.find_all("tr"):
            if tr.find_parent("table") is not table:
                continue
            cells = [c.get_text(" ", strip=True) for c in tr.find_all(["th", "td"], recursive=False)]
            if cells:
                rows.append(cells)
        out.append(rows)
    return out


def metric_candidates(raw: str, metric: str) -> list[float]:
    ts = tables(raw)
    if len(ts) < 2:
        return []
    labels = ts[0]
    values = ts[1]
    wanted = LABELS[metric]
    out = []
    for ri, row in enumerate(labels):
        label = " ".join(row).strip()
        if not any(w in label for w in wanted) or ri >= len(values):
            continue
        for cell in values[ri]:
            n = parse_number(cell)
            if n is not None:
                out.append(n / 1000.0)
    return out


def choose_closest(candidates: list[float], official_million: float) -> float | None:
    if not candidates:
        return None
    return min(candidates, key=lambda v: abs(v - official_million))


def replace_metric_cells(text: str, metric: str, q1: float, q2: float) -> tuple[str, bool]:
    labels = {
        "revenue": "Revenue",
        "gross_profit": "Gross Profit",
        "operating_income": "Operating Income",
        "net_income": "Net Income",
    }
    row_label = labels[metric]
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

    changed = False
    for i in table_idx[2:]:
        cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
        if not cells or cells[0] != row_label:
            continue
        for date, value in {"2026-03-31": q1, "2026-06-30": q2}.items():
            col = date_to_col[date]
            if col < len(cells):
                cells[col] = f"{value:.2f}"
                changed = True
        lines[i] = "| " + " | ".join(cells) + " |"

    margin_label = {
        "gross_profit": "Gross Margin (%)",
        "operating_income": "Operating Margin (%)",
        "net_income": "Net Margin (%)",
    }.get(metric)
    if changed and margin_label:
        revenue_row = None
        margin_row = None
        for i in table_idx[2:]:
            cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
            if cells and cells[0] == "Revenue":
                revenue_row = cells
            if cells and cells[0] == margin_label:
                margin_row = (i, cells)

        if revenue_row and margin_row:
            i, cells = margin_row
            for date, value in {"2026-03-31": q1, "2026-06-30": q2}.items():
                col = date_to_col[date]
                rev = parse_number(revenue_row[col]) if col < len(revenue_row) else None
                if rev not in (None, 0) and col < len(cells):
                    cells[col] = f"{value / rev * 100:.2f}"
            lines[i] = "| " + " | ".join(cells) + " |"

    if not changed:
        return text, False
    return text[:m.start(2)] + "\n".join(lines) + text[m.end(2):], True


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", default="audit-v5/generated/official-financial-summary.json")
    ap.add_argument("--output", default="audit-v5/generated/financial-difference-resolution.json")
    args = ap.parse_args()

    source = json.loads(Path(args.input).read_text(encoding="utf-8"))
    differences = source.get("differences") or source.get("top_differences", [])
    by_ticker = {}
    for item in differences:
        by_ticker.setdefault(item["ticker"], []).append(item)

    rows = []
    counts = Counter()

    for ticker, items in sorted(by_ticker.items()):
        company = items[0]["company"]
        path = Path(items[0]["path"])
        try:
            q1_raw = fetch_statement(ticker, company, "20261")
            q2_raw = fetch_statement(ticker, company, "20262")
        except Exception as exc:
            for item in items:
                rows.append({**item, "disposition": "UNKNOWN", "error": f"{type(exc).__name__}: {exc}"})
                counts["unknown"] += 1
            continue

        text = path.read_text(encoding="utf-8")
        patched_any = False

        for item in items:
            metric = item["metric"]
            official = float(item["official_value_million"])
            q2_ytd = choose_closest(metric_candidates(q2_raw, metric), official)
            q1_ytd = choose_closest(metric_candidates(q1_raw, metric), official)
            tolerance = max(0.02, abs(official) * 0.00005)

            if q2_ytd is None or abs(q2_ytd - official) > tolerance:
                disposition = "OFFICIAL_SOURCE_CONFLICT"
                counts["official_source_conflict"] += 1
                q2_single = None
                patch_applied = False
            elif q1_ytd is None:
                disposition = "UNKNOWN"
                counts["unknown"] += 1
                q2_single = None
                patch_applied = False
            else:
                disposition = "REPO_WRONG"
                counts["repo_wrong"] += 1
                q2_single = q2_ytd - q1_ytd
                text, changed = replace_metric_cells(text, metric, q1_ytd, q2_single)
                patched_any = patched_any or changed
                patch_applied = changed

            rows.append({
                **item,
                "mops_q1_ytd_million": q1_ytd,
                "mops_q2_ytd_million": q2_ytd,
                "mops_q2_single_million": q2_single,
                "disposition": disposition,
                "patch_applied": patch_applied,
            })

        if patched_any:
            path.write_text(text, encoding="utf-8")
        time.sleep(0.15)

    payload = {
        "schema": "financial-difference-resolution-1",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source": URL,
        "input_difference_count": len(differences),
        "counts": dict(sorted(counts.items())),
        "resolutions": rows,
    }

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in payload.items() if k != "resolutions"}, ensure_ascii=False, indent=2))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
