from __future__ import annotations

import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--root", default="Pilot_Reports")
    p.add_argument("--git-sha", required=True)
    p.add_argument("--branch", default="audit-v5")
    p.add_argument("--output", default="audit-v5/generated/github-baseline.json")
    args = p.parse_args()

    root = Path(args.root)
    reports = []
    ticker_map = {}
    company_map = {}
    sector_counts = {}
    for path in sorted(root.rglob("*.md")):
        rel = path.as_posix()
        m = re.match(r"^Pilot_Reports/([^/]+)/(\d{4,6})_(.+)\.md$", rel)
        if not m:
            continue
        sector, ticker, company = m.groups()
        item = {
            "path": rel,
            "sector": sector,
            "ticker": ticker,
            "company": company,
            "sha256": sha256_file(path),
            "size": path.stat().st_size,
        }
        reports.append(item)
        ticker_map.setdefault(ticker, []).append(rel)
        company_map.setdefault(company, []).append(rel)
        sector_counts[sector] = sector_counts.get(sector, 0) + 1

    duplicates = {
        "ticker": {k: v for k, v in ticker_map.items() if len(v) > 1},
        "company": {k: v for k, v in company_map.items() if len(v) > 1},
    }
    manifest = {
        "schema": "github-baseline-1",
        "engine": "audit-engine-v5",
        "source": "TENMALOG/My-TW-Coverage",
        "branch": args.branch,
        "source_parent_sha": args.git_sha,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "report_count": len(reports),
        "sector_count": len(sector_counts),
        "sector_counts": dict(sorted(sector_counts.items())),
        "duplicate_tickers": duplicates["ticker"],
        "duplicate_companies": duplicates["company"],
        "reports": reports,
    }
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "report_count": manifest["report_count"],
        "sector_count": manifest["sector_count"],
        "duplicate_ticker_count": len(duplicates["ticker"]),
        "duplicate_company_count": len(duplicates["company"]),
        "output": str(out),
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
