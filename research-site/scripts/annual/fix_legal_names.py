"""Replace a company-facts file's legal_name with the MOPS-registered name when that name appears
in the cited annual report; leave it unchanged (and report it) otherwise.

  python research-site/scripts/annual/fix_legal_names.py [--tickers ...]

Only the legal_name field is touched; facts are not changed. Every change is appended to
research-site/data/company-facts/_legal-name-fixes.jsonl. Run verify_extraction.py afterwards.
"""
from __future__ import annotations

import argparse
import datetime
import json

from slice_annual import ROOT, identity_confirmed, registered_name

FACTS = ROOT / "research-site/data/company-facts"
LOG = FACTS / "_legal-name-fixes.jsonl"


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--tickers", nargs="*"); a = ap.parse_args()
    files = [FACTS / f"{t}.json" for t in a.tickers] if a.tickers else sorted(FACTS.glob("[0-9]*.json"))
    changed = unchanged = unresolved = 0
    for path in files:
        if not path.exists():
            continue
        doc = json.loads(path.read_text(encoding="utf-8"))
        reg = registered_name(doc["ticker"])
        text = (ROOT / doc["source"]["text_path"]).read_text(encoding="utf-8")
        basis = identity_confirmed(reg, doc.get("company"), doc["ticker"], doc["source"]["filename"], text)
        if not reg or not basis:
            unresolved += 1
            print(doc["ticker"], "unresolved:", "no registered name" if not reg else "report not confirmed as this company", reg)
            continue
        if doc["legal_name"] == reg:
            unchanged += 1
            continue
        old = doc["legal_name"]
        doc["legal_name"] = reg
        path.write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
        with open(LOG, "a", encoding="utf-8") as f:
            f.write(json.dumps({"ticker": doc["ticker"], "old": old, "new": reg, "identity_basis": basis,
                                "at": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")},
                               ensure_ascii=False) + "\n")
        changed += 1
        print(doc["ticker"], f"{old} -> {reg}")
    print(f"changed {changed}, already correct {unchanged}, unresolved {unresolved}")


if __name__ == "__main__":
    main()
