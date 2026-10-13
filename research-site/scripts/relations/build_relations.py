"""Build conservative, reproducible company relations from reviewed annual-report facts."""

from __future__ import annotations

import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FACTS = ROOT / "data/company-facts"
DATA = ROOT / "data/relations"
CATALOG = ROOT / "catalog/release-scope-companies.csv"
FIELDS = {"major_customers", "major_suppliers", "group_structure"}
SUFFIXES = ("股份有限公司", "(股)公司", "（股）公司", "有限公司")
COLUMNS = ("relation_id", "ticker", "company", "role", "counterparty", "counterparty_kind", "counterparty_ticker", "counterparty_company", "period", "share_text", "amount_text", "fact_id", "match_rule")


def strip_suffix(name: str) -> str:
    for suffix in SUFFIXES:
        if name.endswith(suffix):
            return name[: -len(suffix)]
    return name


def load_facts(facts_dir: Path = FACTS) -> tuple[dict, dict]:
    reviews = {}
    review_file = facts_dir / "_semantic-review.jsonl"
    if review_file.exists():
        for line in review_file.read_text(encoding="utf-8").splitlines():
            if line.strip():
                record = json.loads(line)
                reviews[record["id"]] = record["verdict"]
    facts, companies = {}, {}
    for path in sorted(facts_dir.glob("*.json")):
        document = json.loads(path.read_text(encoding="utf-8"))
        companies[document["ticker"]] = document
        for fact in document["facts"]:
            if (fact["field"] in FIELDS and fact.get("verification", {}).get("status") == "PASS"
                    and reviews.get(fact["id"]) != "REJECT"):
                facts[fact["id"]] = (document["ticker"], fact)
    return facts, companies


def name_index(companies: dict, catalog_rows: list[dict]) -> dict[str, list[tuple[str, str]]]:
    indexes = {rule: defaultdict(set) for rule in ("legal_name", "legal_name_suffix", "catalog_short_name")}
    catalog = {row["ticker"]: row["company"] for row in catalog_rows}
    for ticker, doc in companies.items():
        if ticker not in catalog:
            continue
        legal = doc["legal_name"]
        indexes["legal_name"][legal].add(ticker)
        short_legal = strip_suffix(legal)
        if short_legal != legal:
            indexes["legal_name_suffix"][short_legal].add(ticker)
        indexes["catalog_short_name"][catalog[ticker]].add(ticker)
    return indexes


def resolve(name: str, kind: str, indexes: dict, catalog: dict) -> tuple[str, str, str]:
    if kind != "named" or not name:
        return "", "", ""
    for rule in ("legal_name", "legal_name_suffix", "catalog_short_name"):
        candidates = indexes[rule].get(name, set())
        if len(candidates) == 1:
            ticker = next(iter(candidates))
            return ticker, catalog[ticker], rule
        if len(candidates) > 1:
            return "", "", "ambiguous_" + rule
    return "", "", ""


def build(counterparty_path: Path = DATA / "counterparties.jsonl", facts_dir: Path = FACTS,
          catalog_path: Path = CATALOG, output_dir: Path = DATA) -> dict:
    facts, companies = load_facts(facts_dir)
    with catalog_path.open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    catalog = {row["ticker"]: row["company"] for row in rows}
    indexes = name_index(companies, rows)
    relations = []
    seen = set()
    for line in counterparty_path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        entry = json.loads(line)
        fact_id = entry["fact_id"]
        assert fact_id in facts, f"Unusable fact: {fact_id}"
        ticker, fact = facts[fact_id]
        assert entry["ticker"] == ticker and entry["field"] == fact["field"]
        assert entry["period"] == fact["period"]
        assert entry["counterparty"] in fact["statement"], f"Not a statement substring: {fact_id}"
        assert entry["counterparty_kind"] in {"named", "code", "none"}
        assert entry["role"] in {"customer", "supplier", "parent", "subsidiary", "affiliate", "investee"}
        assert (entry["counterparty"] == "") == (entry["counterparty_kind"] == "none")
        key = (fact_id, entry["counterparty"], entry["role"])
        assert key not in seen, f"Duplicate counterparty: {key}"
        seen.add(key)
        target, target_company, rule = resolve(entry["counterparty"], entry["counterparty_kind"], indexes, catalog)
        if target == ticker:  # the issuer itself (e.g. 冠德 → 冠德建設) is not a relation to another company
            target, target_company, rule = "", "", "self_reference"
        relations.append({
            "relation_id": f"REL-{len(relations)+1:06d}", "ticker": ticker,
            "company": catalog.get(ticker, companies[ticker]["company"]),
            "role": entry["role"], "counterparty": entry["counterparty"],
            "counterparty_kind": entry["counterparty_kind"],
            "counterparty_ticker": target, "counterparty_company": target_company,
            "period": entry["period"], "share_text": entry["share_text"],
            "amount_text": entry["amount_text"], "fact_id": fact_id, "match_rule": rule,
        })
    assert set(facts) == {row["fact_id"] for row in relations}, "Counterparties must cover every usable relevant fact"
    output_dir.mkdir(parents=True, exist_ok=True)
    for filename, data in (("relations.csv", relations), ("unresolved_named.csv", [r for r in relations if r["counterparty_kind"] == "named" and not r["counterparty_ticker"]])):
        with (output_dir / filename).open("w", encoding="utf-8-sig", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=COLUMNS)
            writer.writeheader()
            writer.writerows(data)
    connections = Counter()
    for row in relations:
        if row["ticker"] in catalog:
            connections[row["ticker"]] += 1
        if row["counterparty_ticker"]:
            connections[row["counterparty_ticker"]] += 1
    summary = {
        "facts": len(facts), "relations": len(relations),
        "by_role": dict(sorted(Counter(r["role"] for r in relations).items())),
        "by_kind": dict(sorted(Counter(r["counterparty_kind"] for r in relations).items())),
        "resolved_to_listed_tickers": sum(bool(r["counterparty_ticker"]) for r in relations),
        "edges_both_listed": sum(r["ticker"] in catalog and bool(r["counterparty_ticker"]) for r in relations),
        "top_30_most_connected_listed_companies": [
            {"ticker": ticker, "company": catalog[ticker], "edges": count}
            for ticker, count in sorted(connections.items(), key=lambda item: (-item[1], item[0]))[:30]
        ],
    }
    (output_dir / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return summary


if __name__ == "__main__":
    print(json.dumps(build(), ensure_ascii=False, indent=2))
