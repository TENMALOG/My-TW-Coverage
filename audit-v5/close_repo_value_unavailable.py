from __future__ import annotations

import json
import time
from pathlib import Path

from credit_services_refresh import fetch_statement, statement_rows, metric_value, parse_quarter_table, render_table

SUMMARY = Path("audit-v5/generated/official-financial-summary.json")
ROW_NAMES = {"revenue":"Revenue","gross_profit":"Gross Profit","operating_income":"Operating Income","net_income":"Net Income"}
MARGINS = {"gross_profit":"Gross Margin (%)","operating_income":"Operating Margin (%)","net_income":"Net Margin (%)"}


def num(raw):
    try:
        s=str(raw).strip().replace(",","")
        if not s or s in {"-","--","N/A"}:
            return None
        return float(s)
    except Exception:
        return None


def patch_file(path, items, q1_rows):
    text=path.read_text(encoding="utf-8")
    headers,rows,order,match=parse_quarter_table(text)
    q1i=headers.index("2026-03-31")
    q2i=headers.index("2026-06-30")
    changes=[]
    failures=[]
    for item in items:
        metric=item["metric"]
        row=ROW_NAMES[metric]
        if row not in rows:
            failures.append({"metric":metric,"reason":"row_missing"})
            continue
        q1=num(rows[row][q1i])
        q2=num(rows[row][q2i])
        ytd=float(item["official_value_million"])
        if q1 is None and q2 is None:
            raw=metric_value(q1_rows,metric) if q1_rows else None
            if raw is None:
                failures.append({"metric":metric,"reason":"official_q1_missing"})
                continue
            q1=raw/1000.0
            q2=ytd-q1
            method="MOPS_Q1_PLUS_OFFICIAL_Q2_YTD_RESIDUAL"
        elif q1 is None:
            q1=ytd-q2
            method="OFFICIAL_YTD_MINUS_EXISTING_Q2"
        elif q2 is None:
            q2=ytd-q1
            method="OFFICIAL_YTD_MINUS_EXISTING_Q1"
        else:
            failures.append({"metric":metric,"reason":"checker_missing_but_cells_present"})
            continue
        rows[row][q1i]=f"{q1:.2f}"
        rows[row][q2i]=f"{q2:.2f}"
        changes.append({"metric":metric,"q1":q1,"q2":q2,"official_ytd":ytd,"method":method})

    for i in (q1i,q2i):
        revenue=num(rows["Revenue"][i]) if "Revenue" in rows else None
        if revenue in (None,0):
            continue
        for metric,margin_row in MARGINS.items():
            value_row=ROW_NAMES[metric]
            if value_row in rows and margin_row in rows:
                value=num(rows[value_row][i])
                if value is not None:
                    rows[margin_row][i]=f"{value/revenue*100:.2f}"

    if changes:
        table=render_table(headers,rows,order)
        path.write_text(text[:match.start(2)]+table+text[match.end(2):],encoding="utf-8")
    return changes,failures


def main():
    summary=json.loads(SUMMARY.read_text(encoding="utf-8"))
    targets=summary.get("repo_value_unavailable",[])
    grouped={}
    for item in targets:
        grouped.setdefault(item["path"],[]).append(item)
    results=[]
    failure_count=0
    patched_count=0
    for path_s,items in sorted(grouped.items()):
        need_q1=any("[1, 2]" in str(x.get("repo_basis")) for x in items)
        q1_rows={}
        fetch_error=None
        if need_q1:
            first=items[0]
            try:
                q1_rows=statement_rows(fetch_statement(first["ticker"],first["company"],"20261"))
            except Exception as exc:
                fetch_error=f"{type(exc).__name__}: {exc}"
        if fetch_error:
            changes=[]
            failures=[{"metric":"*","reason":"q1_fetch_failed","error":fetch_error}]
        else:
            changes,failures=patch_file(Path(path_s),items,q1_rows)
        patched_count+=len(changes)
        failure_count+=len(failures)
        results.append({"path":path_s,"ticker":items[0]["ticker"],"company":items[0]["company"],"changes":changes,"failures":failures})
        time.sleep(0.15)
    out={"schema":"repo-value-unavailable-close-1","input_count":len(targets),"patched_count":patched_count,"failure_count":failure_count,"results":results}
    Path("audit-v5/generated/repo-value-unavailable-close.json").write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"input_count":len(targets),"patched_count":patched_count,"failure_count":failure_count},ensure_ascii=False,indent=2))
    raise SystemExit(0 if failure_count==0 else 2)


if __name__=="__main__":
    main()
