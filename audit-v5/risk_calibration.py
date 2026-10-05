from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

from auditlib import _narrative_risk_text, risk_signals, scan_report


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default="Pilot_Reports")
    ap.add_argument("--output", default="audit-v5/generated/risk-calibration.json")
    args = ap.parse_args()

    counts = Counter()
    signal_counts = Counter()
    high_signal_counts = Counter()
    samples = defaultdict(list)
    high_reports = []
    medium_reports = []
    low_reports = []

    for path in sorted(Path(args.root).rglob("*.md")):
        scan = scan_report(path)
        counts[scan.risk_class] += 1
        text = path.read_text(encoding="utf-8")
        signals = risk_signals(_narrative_risk_text(text))
        for signal in signals:
            key = f'{signal["level"]}:{signal["type"]}'
            signal_counts[key] += 1
            if signal["level"] == "HIGH":
                high_signal_counts[signal["type"]] += 1
            if len(samples[key]) < 12:
                samples[key].append({
                    "ticker": scan.ticker,
                    "company": scan.company,
                    "path": path.as_posix(),
                    "claim": signal["claim"][:500],
                })

        entry = {
            "ticker": scan.ticker,
            "company": scan.company,
            "path": path.as_posix(),
            "reasons": scan.risk_reasons,
        }
        if scan.risk_class == "HIGH":
            high_reports.append(entry)
        elif scan.risk_class == "MEDIUM":
            medium_reports.append(entry)
        else:
            low_reports.append(entry)

    payload = {
        "schema": "risk-calibration-2",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "method": "claim-level semantic signals over narrative sections only",
        "issuer_counts": dict(sorted(counts.items())),
        "high_share": round(counts["HIGH"] / max(sum(counts.values()), 1), 6),
        "signal_counts": dict(sorted(signal_counts.items())),
        "high_signal_counts": dict(sorted(high_signal_counts.items())),
        "samples": dict(samples),
        "high_reports": high_reports,
        "medium_report_count": len(medium_reports),
        "low_report_count": len(low_reports),
        "calibration_invariants": [
            "headings, metadata and financial tables cannot create semantic HIGH",
            "generic export alone is MEDIUM",
            "generic supply-chain language alone is MEDIUM",
            "named customer/supplier relations are HIGH only when a named entity is present in the same claim",
            "ranking/market-share, profitability and corporate-event assertions remain HIGH"
        ]
    }

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "issuer_counts": payload["issuer_counts"],
        "high_share": payload["high_share"],
        "high_signal_counts": payload["high_signal_counts"],
        "output": str(out),
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
