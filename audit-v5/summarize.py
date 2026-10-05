from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--baseline", required=True)
    ap.add_argument("--scan", required=True)
    ap.add_argument("--financial", required=True)
    ap.add_argument("--readme", default="README.md")
    ap.add_argument("--output", default="audit-v5/generated/audit-summary.json")
    args = ap.parse_args()

    baseline = json.loads(Path(args.baseline).read_text(encoding="utf-8"))
    scan = json.loads(Path(args.scan).read_text(encoding="utf-8"))
    financial = json.loads(Path(args.financial).read_text(encoding="utf-8"))

    risk = Counter()
    statuses = Counter()
    severities = Counter()
    blocked_reports = 0
    unresolved_identity = 0
    for report in scan.get("results", []):
        risk[report.get("risk_class", "UNKNOWN")] += 1
        report_blocked = False
        report_identity = False
        for check in report.get("checks", []):
            statuses[check.get("status", "UNKNOWN")] += 1
            severities[check.get("severity", "info")] += 1
            if check.get("status") == "BLOCKED":
                report_blocked = True
            if check.get("status") == "IDENTITY_UNRESOLVED":
                report_identity = True
        blocked_reports += int(report_blocked)
        unresolved_identity += int(report_identity)

    readme_text = Path(args.readme).read_text(encoding="utf-8") if Path(args.readme).exists() else ""
    declared_reports = None
    declared_sectors = None
    m = re.search(r"covering \*\*(\d[\d,]*) Taiwan-listed companies\*\*", readme_text)
    if m:
        declared_reports = int(m.group(1).replace(",", ""))
    m = re.search(r"across \*\*(\d+) industry sectors\*\*", readme_text)
    if m:
        declared_sectors = int(m.group(1))

    warnings = []
    if declared_reports is not None and declared_reports != baseline.get("report_count"):
        warnings.append(
            f"README declares {declared_reports} companies but repository contains "
            f"{baseline.get('report_count')} report files"
        )
    if declared_sectors is not None and declared_sectors != baseline.get("sector_count"):
        warnings.append(
            f"README declares {declared_sectors} sectors but repository contains "
            f"{baseline.get('sector_count')} sector directories"
        )
    if baseline.get("duplicate_tickers"):
        warnings.append("duplicate ticker report files detected")
    if unresolved_identity:
        warnings.append(
            f"{unresolved_identity} reports have filename/title identity mismatch or unresolved identity"
        )
    if blocked_reports:
        warnings.append(f"{blocked_reports} reports are structurally blocked by deterministic checks")
    if not financial.get("ok"):
        warnings.append("financial refresh did not complete cleanly")

    payload = {
        "schema": "audit-summary-1",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "baseline_source_parent_sha": baseline.get("source_parent_sha"),
        "report_count": baseline.get("report_count"),
        "sector_count": baseline.get("sector_count"),
        "risk_counts": dict(sorted(risk.items())),
        "atomic_status_counts": dict(sorted(statuses.items())),
        "severity_counts": dict(sorted(severities.items())),
        "blocked_report_count": blocked_reports,
        "identity_unresolved_report_count": unresolved_identity,
        "financial_refresh": financial,
        "readme_declared_report_count": declared_reports,
        "readme_declared_sector_count": declared_sectors,
        "warnings": warnings,
        "semantic_validation_complete": False,
        "note": (
            "Machine-verifiable coverage is summarized here. HIGH/MEDIUM narrative claims remain "
            "subject to semantic/source review unless separately accepted."
        ),
    }
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
