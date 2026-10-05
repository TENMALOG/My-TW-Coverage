from __future__ import annotations

import json
from pathlib import Path

from credit_services_refresh import parse_quarter_table, render_table

SUMMARY=Path("audit-v5/generated/official-financial-summary.json")


def num(raw):
    try:
        s=str(raw).strip().replace(",","")
        if not s or s in {"-","--","N/A"}:
            return None
        return float(s)
    except Exception:
        return None


def patch(path,official_ytd):
    text=path.read_text(encoding="utf-8")
    headers,rows,order,match=parse_quarter_table(text)
    q1i=headers.index("2026-03-31")
    q2i=headers.index("2026-06-30")
    q1=num(rows["Operating Income"][q1i])
    if q1 is None:
        raise RuntimeError("Q1 Operating Income missing: "+str(path))
    q2=official_ytd-q1
    rows["Operating Income"][q2i]=f"{q2:.2f}"
    rev=num(rows["Revenue"][q2i]) if "Revenue" in rows else None
    if rev not in (None,0) and "Operating Margin (%)" in rows:
        rows["Operating Margin (%)"][q2i]=f"{q2/rev*100:.2f}"
    table=render_table(headers,rows,order)
    path.write_text(text[:match.start(2)]+table+text[match.end(2):],encoding="utf-8")
    return {"q1":q1,"q2":q2,"official_ytd":official_ytd}


def main():
    summary=json.loads(SUMMARY.read_text(encoding="utf-8"))
    items=summary.get("source_definition_differences",[])
    results=[]
    for item in items:
        if item.get("metric")!="operating_income":
            raise RuntimeError("unexpected metric: "+str(item.get("metric")))
        values=patch(Path(item["path"]),float(item["official_value_million"]))
        results.append({"ticker":item["ticker"],"path":item["path"],**values})
    out={"schema":"source-definition-close-1","input_count":len(items),"patched_count":len(results),"method":"preserve Q1; Q2 = canonical MOPS Q2 YTD - Q1","results":results}
    Path("audit-v5/generated/source-definition-close.json").write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"input_count":len(items),"patched_count":len(results)},ensure_ascii=False))


if __name__=="__main__":
    main()
