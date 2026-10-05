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

URL = "https://mopsfin.twse.com.tw/compare/report"
LABELS = {
    "revenue": ("營業收入合計", "營業收入"),
    "gross_profit": ("營業毛利（毛損）淨額", "營業毛利（毛損）"),
    "operating_income": ("營業利益（損失）",),
    "net_income": ("母公司業主（淨利∕損）", "淨利（淨損）歸屬於母公司業主"),
}
ROW_NAMES = {
    "revenue": "Revenue",
    "gross_profit": "Gross Profit",
    "operating_income": "Operating Income",
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


def fetch_statement(ticker: str, company: str, period: str, retries: int = 4) -> str:
    pairs = [
        ("compareItem", "IncomeStatement"),
        ("ylabel", "新台幣仟元"),
        ("quarter", "true"),
        ("revenue", "true"),
        ("ys", period),
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
            if attempt + 1 < retries:
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
    for label in LABELS[metric]:
        if label in rows:
            return rows[label]
    return None


def parse_quarter_table(text: str):
    m = re.search(
        r"(^### 季度關鍵財務數據.*?\n)(\|.*?\n\|.*?\n(?:\|.*?\n)+)",
        text,
        flags=re.MULTILINE,
    )
    if not m:
        raise ValueError("quarterly table not found")
    lines = [line for line in m.group(2).splitlines() if line.startswith("|")]
    headers = [c.strip() for c in lines[0].strip("|").split("|")][1:]
    rows = {}
    order = []
    for line in lines[2:]:
        cells = [c.strip() for c in line.strip("|").split("|")]
        rows[cells[0]] = cells[1:]
        order.append(cells[0])
    return headers, rows, order, m


def render_table(headers, rows, order):
    first_width = 25
    out = ["| " + " " * first_width + " | " + " | ".join(headers) + " |"]
    out.append("|:" + "-" * first_width + "|" + "|".join("-" * (len(h) + 2) + ":" for h in headers) + "|")
    for label in order:
        out.append("| " + label.ljust(first_width) + " | " + " | ".join(rows[label]) + " |")
    return "\n".join(out) + "\n"


def patch_report(path: Path, values: dict[str, tuple[float, float]]) -> bool:
    text = path.read_text(encoding="utf-8")
    headers, rows, order, match = parse_quarter_table(text)
    if "2026-03-31" not in headers or "2026-06-30" not in headers:
        return False
    q1_idx = headers.index("2026-03-31")
    q2_idx = headers.index("2026-06-30")

    changed = False
    for metric, (q1_m, q2_single_m) in values.items():
        row = ROW_NAMES[metric]
        if row not in rows:
            continue
        new_q1 = f"{q1_m:.2f}"
        new_q2 = f"{q2_single_m:.2f}"
        if rows[row][q1_idx] != new_q1 or rows[row][q2_idx] != new_q2:
            rows[row][q1_idx] = new_q1
            rows[row][q2_idx] = new_q2
            changed = True

    def num(label: str, idx: int):
        try:
            return float(rows[label][idx].replace(",", ""))
        except Exception:
            return None

    for idx in (q1_idx, q2_idx):
        rev = num("Revenue", idx)
        for metric, margin_row in (
            ("gross_profit", "Gross Margin (%)"),
            ("operating_income", "Operating Margin (%)"),
            ("net_income", "Net Margin (%)"),
        ):
            value = num(ROW_NAMES[metric], idx)
            if rev not in (None, 0) and value is not None and margin_row in rows:
                new_margin = f"{value / rev * 100:.2f}"
                if rows[margin_row][idx] != new_margin:
                    rows[margin_row][idx] = new_margin
                    changed = True

    if not changed:
        return False
    new_table = render_table(headers, rows, order)
    path.write_text(text[:match.start(2)] + new_table + text[match.end(2):], encoding="utf-8")
    return True


def target_reports(root: Path):
    out = []
    for path in sorted((root / "Credit Services").glob("*.md")):
        m = re.match(r"^(\d+)_(.+)\.md$", path.name)
        if m:
            out.append((m.group(1), m.group(2), path))
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default="Pilot_Reports")
    ap.add_argument("--output", default="audit-v5/generated/credit-services-refresh.json")
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    results = []
    counts = Counter()
    for ticker, company, path in target_reports(Path(args.root)):
        try:
            q1 = statement_rows(fetch_statement(ticker, company, "20261"))
            q2 = statement_rows(fetch_statement(ticker, company, "20262"))
        except Exception as exc:
            results.append({
                "ticker": ticker, "company": company, "path": path.as_posix(),
                "status": "FETCH_FAILED", "error": f"{type(exc).__name__}: {exc}",
            })
            counts["FETCH_FAILED"] += 1
            continue

        values = {}
        missing = []
        evidence = {}
        for metric in ROW_NAMES:
            q1_raw = metric_value(q1, metric)
            q2_ytd_raw = metric_value(q2, metric)
            if q1_raw is None or q2_ytd_raw is None:
                missing.append(metric)
                continue
            q1_m = q1_raw / 1000.0
            q2_ytd_m = q2_ytd_raw / 1000.0
            q2_single_m = q2_ytd_m - q1_m
            values[metric] = (q1_m, q2_single_m)
            evidence[metric] = {
                "q1_million": q1_m,
                "q2_ytd_million": q2_ytd_m,
                "q2_single_million": q2_single_m,
            }

        if missing:
            status = "MOPS_VALUE_MISSING"
            counts[status] += 1
            applied = False
        elif args.apply:
            applied = patch_report(path, values)
            status = "PATCHED" if applied else "UNCHANGED"
            counts[status] += 1
        else:
            applied = False
            status = "READY"
            counts[status] += 1

        results.append({
            "ticker": ticker,
            "company": company,
            "path": path.as_posix(),
            "status": status,
            "missing_metrics": missing,
            "patch_applied": applied,
            "evidence": evidence,
        })
        time.sleep(0.2)

    payload = {
        "schema": "credit-services-refresh-1",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source": URL,
        "policy": "credit-services-current-period-mops",
        "target_count": len(results),
        "counts": dict(sorted(counts.items())),
        "results": results,
    }
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in payload.items() if k != "results"}, ensure_ascii=False, indent=2))
    return 0 if not counts["FETCH_FAILED"] and not counts["MOPS_VALUE_MISSING"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
