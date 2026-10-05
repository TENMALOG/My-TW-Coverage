from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from auditlib import BindingFingerprint, carry_forward_eligible, init_db, scan_report, validate_v4_export


def command_scan(args: argparse.Namespace) -> int:
    root = Path(args.root)
    if not root.exists():
        print(f"root not found: {root}", file=sys.stderr)
        return 2
    paths = sorted(root.rglob("*.md"))
    if args.ticker:
        paths = [p for p in paths if p.name.startswith(f"{args.ticker}_")]
    results = [scan_report(p).to_dict() for p in paths]
    payload = {
        "engine": "audit-engine-v5",
        "mode": "deterministic-machine-gate",
        "report_count": len(results),
        "results": results,
    }
    text = json.dumps(payload, ensure_ascii=False, indent=2)
    if args.output:
        out = Path(args.output)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(text + "\n", encoding="utf-8")
        print(out)
    else:
        print(text)
    return 0


def command_init(args: argparse.Namespace) -> int:
    path = Path(args.db)
    init_db(path)
    print(path)
    return 0


def command_carry_forward(args: argparse.Namespace) -> int:
    before = json.loads(Path(args.previous).read_text(encoding="utf-8"))
    after = json.loads(Path(args.current).read_text(encoding="utf-8"))
    prev = BindingFingerprint.from_dict(before)
    cur = BindingFingerprint.from_dict(after)
    result = {"eligible": carry_forward_eligible(prev, cur), "previous": before, "current": after}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["eligible"] else 1


def command_validate_export(args: argparse.Namespace) -> int:
    payload = json.loads(Path(args.path).read_text(encoding="utf-8"))
    result = validate_v4_export(payload)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["ok"] else 1


def command_regression_1304(args: argparse.Namespace) -> int:
    fixture = json.loads(Path(args.fixture).read_text(encoding="utf-8"))
    expected = fixture["expected_v4"]
    invariants = fixture["v5_invariants"]
    failures = []
    if expected.get("narrative_claims") != 30:
        failures.append("expected narrative claim count changed")
    if expected.get("financial_cells") != 98:
        failures.append("expected financial cell count changed")
    if expected.get("financial_exact") != 66:
        failures.append("expected exact financial count changed")
    if expected.get("financial_differences") != 11:
        failures.append("expected financial difference count changed")
    if expected.get("financial_method_gaps") != 21:
        failures.append("expected financial method-gap count changed")
    if expected.get("valuation_cells") != 8:
        failures.append("expected valuation cell count changed")
    required = {"preserve_v4", "do_not_auto_pass_differences", "do_not_auto_pass_method_gaps", "reuse_sources"}
    if not required.issubset(set(invariants)):
        failures.append("required v5 invariants missing")
    result = {"ok": not failures, "failures": failures, "fixture": str(args.fixture)}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["ok"] else 1


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="My-TW-Coverage audit-engine-v5 control CLI")
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("init", help="initialize the local v5 SQLite state database")
    p.add_argument("--db", default="audit-v5/work/audit-v5.sqlite")
    p.set_defaults(func=command_init)

    p = sub.add_parser("scan", help="run deterministic machine gate over report markdown")
    p.add_argument("--root", default="Pilot_Reports")
    p.add_argument("--ticker")
    p.add_argument("--output")
    p.set_defaults(func=command_scan)

    p = sub.add_parser("carry-forward", help="compare two binding fingerprints")
    p.add_argument("--previous", required=True)
    p.add_argument("--current", required=True)
    p.set_defaults(func=command_carry_forward)

    p = sub.add_parser("validate-v4-export", help="validate a normalized read-only v4 export before migration")
    p.add_argument("path")
    p.set_defaults(func=command_validate_export)

    p = sub.add_parser("regression-1304", help="validate the locked 1304 regression contract")
    p.add_argument("--fixture", default="audit-v5/fixtures/1304-regression.json")
    p.set_defaults(func=command_regression_1304)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
