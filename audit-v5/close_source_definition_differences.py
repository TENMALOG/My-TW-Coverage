from __future__ import annotations

import json
import re
from pathlib import Path

SUMMARY = Path("audit-v5/generated/official-financial-summary.json")


def num(raw):
    if raw is None:
        return None
    s = str(raw).strip().replace(",", "")
    if not s or s in {"-", "--", "N/A"}:
        return None
    try:
        return float(s)
    except ValueError:
        return None


def patch(path, official_ytd):
    text = path.read_text(encoding="utf-8")
    m = re.search(r"(^###\\s+季度關鍵財務數據.*?$\\n)([\\s\\S]*?)(?=^###\\s+|\\Z)", text, re.MULTILINE)
    if not m:
        raise RuntimeError("quarterly section missing: " + str(path))
    lines = m.group(2).splitlines()
    table = [i for i, line in enumerate(lines) if line.strip().startswith("|")]
    headers = [c.strip() for c in lines[table[0]].strip().strip("|").split("|")]
    cols = {v: i for i, v in enumerate(headers)}
    q1c, q2c = cols["2026-03-31"], cols["2026-06-30"]
    rows = {}
    idx = {}
    for i in table[2:]:
        cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
        if cells:
            rows[cells[0]] = cells
            idx[cells[0]] = i

    op = rows["Operating Income"]
    q1 = num(op[q1c])
    if q1 is None:
        raise RuntimeError("Q1 Operating Income missing: " + str(path))
    q2 = official_ytd - q1
    op[q2c] = f"{q2:.2f}"
    lines[idx["Operating Income"]] = "| " + " | ".join(op) + " |"

    if "Operating Margin (%)" in rows and "Revenue" in rows:
        rev = num(rows["Revenue"][q2c])
        if rev not in (None, 0):
            margin = rows["Operating Margin (%)"]
            margin[q2c] = f"{q2 / rev * 100:.2f}"
            lines[idx["Operating Margin (%)"]] = "| " + " | ".join(margin) + " |"

    path.write_text(text[:m.start(2)] + "\n".join(lines) + text[m.end(2):], encoding="utf-8")
    return {"q1": q1, "q2": q2, "official_ytd": official_ytd}


def main():
    summary = json.loads(SUMMARY.read_text(encoding="utf-8"))
    items = summary.get("source_definition_differences", [])
    results = []
    for item in items:
        if item.get("metric") != "operating_income":
            raise RuntimeError("unexpected source-definition metric: " + str(item.get("metric")))
        values = patch(Path(item["path"]), float(item["official_value_million"]))
        results.append({"ticker": item["ticker"], "path": item["path"], **values})
    out = {
        "schema": "source-definition-close-1",
        "input_count": len(items),
        "patched_count": len(results),
        "method": "preserve Q1; set Q2 single-quarter = canonical MOPS Q2 YTD - Q1",
        "results": results,
    }
    Path("audit-v5/generated/source-definition-close.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps({k: v for k, v in out.items() if k != "results"}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
