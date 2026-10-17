"""Small behavioral fixtures for the strict relation resolver."""

import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent))
from build_relations import build, load_facts, name_index, resolve, strip_suffix
from extract_counterparties import extract, kind_for


def test_suffix_stripping():
    assert strip_suffix("甲股份有限公司") == "甲"
    assert strip_suffix("甲(股)公司") == "甲"
    assert strip_suffix("甲（股）公司") == "甲"
    assert strip_suffix("甲有限公司") == "甲"
    assert strip_suffix("甲企業") == "甲企業"


def test_no_fuzzy_codes_and_ambiguous_short_names():
    companies = {
        "1001": {"legal_name": "福星股份有限公司"},
        "1002": {"legal_name": "甲控股有限公司"},
        "1003": {"legal_name": "乙控股有限公司"},
    }
    rows = [
        {"ticker": "1001", "company": "福星"},
        {"ticker": "1002", "company": "共名"},
        {"ticker": "1003", "company": "共名"},
    ]
    indexes = name_index(companies, rows)
    catalog = {row["ticker"]: row["company"] for row in rows}
    assert resolve("福星", "named", indexes, catalog) == ("1001", "福星", "legal_name_suffix")
    assert resolve("福興", "named", indexes, catalog) == ("", "", "")
    assert resolve("福星", "code", indexes, catalog) == ("", "", "")
    assert resolve("共名", "named", indexes, catalog) == ("", "", "ambiguous_catalog_short_name")


def test_anonymous_labels_and_named_brand():
    assert kind_for("A客戶", "114年度A客戶（年報代號）銷貨。") == "code"
    assert kind_for("KOSE", "主要客戶包括KOSE及花王。") == "named"
    fact = {"field": "major_customers", "statement": "主要客戶包括KOSE、花王。"}
    assert ("KOSE", "named", "customer") in extract(fact, ["花王"])


def fixtures():
    source = [
        {"id": "1001-AR-01", "field": "major_customers", "statement": "向福星銷貨。", "period": "114", "verification": {"status": "PASS"}},
        {"id": "1001-AR-02", "field": "major_customers", "statement": "向甲銷貨。", "period": "114", "verification": {"status": "PASS"}},
        {"id": "1001-AR-03", "field": "major_customers", "statement": "向乙銷貨。", "period": "114", "verification": {"status": "FAIL"}},
    ]
    document = json.dumps({"ticker": "1001", "company": "福星", "legal_name": "福星股份有限公司", "facts": source}, ensure_ascii=False)
    reviews = '\n'.join([
        json.dumps({"id": "1001-AR-02", "verdict": "ACCEPT"}),
        json.dumps({"id": "1001-AR-02", "verdict": "REJECT"}),
    ]) + '\n'

    class FakeFile:
        def __init__(self, name):
            self.name = name

        def __truediv__(self, name):
            return FakeFile(name)

        def exists(self):
            return self.name == "_semantic-review.jsonl"

        def read_text(self, **_kwargs):
            return reviews if self.name == "_semantic-review.jsonl" else document

        def glob(self, _pattern):
            return [FakeFile("1001.json")]

    return FakeFile("facts")


def test_reject_and_fail_excluded():
    facts_dir = fixtures()
    facts, _ = load_facts(facts_dir)
    assert set(facts) == {"1001-AR-01"}


def test_substring_assertion(monkeypatch, tmp_path):
    import build_relations

    facts_dir = fixtures()
    record = {"fact_id": "1001-AR-01", "ticker": "1001", "field": "major_customers", "counterparty": "不存在", "counterparty_kind": "named", "role": "customer", "period": "114", "share_text": "", "amount_text": ""}
    class FakeCounterparty:
        def read_text(self, **_kwargs):
            return json.dumps(record, ensure_ascii=False) + "\n"

    class FakeCatalog:
        def open(self, **_kwargs):
            from io import StringIO
            return StringIO("ticker,company\n1001,福星\n")

    # a counterparty that is no longer in the (reviewed) statement is skipped, never published
    build(FakeCounterparty(), facts_dir, FakeCatalog(), tmp_path)
    assert len((tmp_path / "relations.csv").read_text(encoding="utf-8-sig").strip().splitlines()) == 1
