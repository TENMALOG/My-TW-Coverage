from __future__ import annotations

import json
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

URL = "https://mopsfin.twse.com.tw/compare/data"
COMPANIES = [
    "1304 台聚",
    "6776 展碁國際",
    "2412 中華電",
    "3290 東浦",
]
METRICS = {
    "OperatingRevenue": "營業收入",
    "GrossProfit": "營業毛利",
    "OperatingIncome": "營業利益",
    "NetProfit": "稅後純益",
}


def post_metric(metric: str):
    pairs = [
        ("compareItem", metric),
        ("ylabel", "新台幣仟元"),
        ("quarter", "true"),
        ("revenue", "true"),
        ("ys", "0"),
        ("qnumber", ""),
        ("bcodeAvg", "false"),
        ("companyAvg", "false"),
    ]
    pairs.extend(("companyId", company) for company in COMPANIES)
    body = urllib.parse.urlencode(pairs).encode()
    req = urllib.request.Request(
        URL,
        data=body,
        headers={
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
            "Origin": "https://mopsfin.twse.com.tw",
            "Referer": "https://mopsfin.twse.com.tw/",
            "X-Requested-With": "XMLHttpRequest",
            "Accept": "application/json, text/html;q=0.9, */*;q=0.8",
            "User-Agent": "My-TW-Coverage-audit-v5/1.0",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=60) as r:
        text = r.read().decode("utf-8", errors="replace")
        content_type = r.headers.get("content-type", "")
    return json.loads(text), content_type


def main():
    out = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source": URL,
        "companies": COMPANIES,
        "metrics": {},
    }
    for code, name in METRICS.items():
        try:
            payload, content_type = post_metric(code)
            periods = payload.get("xaxisList", [])
            rows = {}
            for series in payload.get("graphData", []):
                if not isinstance(series, dict):
                    continue
                label = str(series.get("label", ""))
                values = {}
                for point in series.get("data", []):
                    if not isinstance(point, list) or len(point) < 2:
                        continue
                    idx = point[0]
                    if isinstance(idx, int) and 0 <= idx < len(periods):
                        values[str(periods[idx])] = point[1]
                rows[label] = values
            out["metrics"][code] = {
                "name": name,
                "ok": True,
                "content_type": content_type,
                "periods": periods,
                "series": rows,
                "unit": payload.get("ylabel"),
                "year": payload.get("year"),
                "season": payload.get("season"),
                "checkedNameList": payload.get("checkedNameList"),
            }
        except Exception as exc:
            out["metrics"][code] = {
                "name": name,
                "ok": False,
                "error": f"{type(exc).__name__}: {exc}",
            }

    path = Path("audit-v5/generated/mopsfin-probe.json")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, ensure_ascii=False, indent=2))
    if not all(item.get("ok") for item in out["metrics"].values()):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
