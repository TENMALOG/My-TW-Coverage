from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from auditlib import BindingFingerprint, carry_forward_eligible, financial_auto_verify, scan_report


GOOD_REPORT = """# 1304 - 台聚

## 業務簡介
**板塊:** Basic Materials
**產業:** Specialty Chemicals
**市值:** 15,495 百萬台幣
**企業價值:** 43,396 百萬台幣

台聚成立於 1965 年。

## 供應鏈位置
上游為原料供應，下游為加工應用。

## 主要客戶及供應商
尚未在本測試宣告特定客戶。

## 財務概況 (單位: 百萬台幣, 只有 Margin 為 %)
| 項目 | 2025 |
|---|---:|
| 營業收入 | 44168.00 |
"""


class AuditV5Tests(unittest.TestCase):
    def test_scan_accepts_original_plain_title_and_financial_suffix(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "1304_台聚.md"
            path.write_text(GOOD_REPORT, encoding="utf-8")
            result = scan_report(path)
            states = {c.code: c.status for c in result.checks}
            self.assertEqual(states["identity.filename_title_match"], "AUTO_VERIFIED")
            self.assertEqual(states["structure.section.財務概況"], "AUTO_VERIFIED")

    def test_scan_accepts_underscore_title(self):
        report = GOOD_REPORT.replace("# 1304 - 台聚", "# 1304_台聚")
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "1304_台聚.md"
            path.write_text(report, encoding="utf-8")
            result = scan_report(path)
            states = {c.code: c.status for c in result.checks}
            self.assertEqual(states["identity.filename_title_match"], "AUTO_VERIFIED")

    def test_scan_normalizes_inline_wikilinks_and_footnote_markers(self):
        report = GOOD_REPORT.replace("# 1304 - 台聚", "# 1304 - [[台]]聚*")
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "1304_台聚.md"
            path.write_text(report, encoding="utf-8")
            result = scan_report(path)
            states = {c.code: c.status for c in result.checks}
            self.assertEqual(states["identity.filename_title_match"], "AUTO_VERIFIED")

    def test_scan_rejects_template_placeholder_title(self):
        report = GOOD_REPORT.replace("# 1304 - 台聚", "# {file.replace('.md', '')}")
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "1304_台聚.md"
            path.write_text(report, encoding="utf-8")
            result = scan_report(path)
            states = {c.code: c.status for c in result.checks}
            self.assertEqual(states["identity.title"], "IDENTITY_UNRESOLVED")


    def test_generic_section_language_does_not_force_high(self):
        text = """一般供應鏈位置說明，出口為公司業務之一。"""
        level, reasons = __import__("auditlib").classify_risk(text)
        self.assertNotEqual(level, "HIGH")

    def test_named_customer_relationship_is_high(self):
        text = """主要客戶包括 [[Apple]] 與 [[NVIDIA]]。"""
        level, reasons = __import__("auditlib").classify_risk(text)
        self.assertEqual(level, "HIGH")
        self.assertIn("high-signal:named_commercial_relationship", reasons)

    def test_ranking_assertion_is_high(self):
        text = """公司為台灣最大玻璃製造商。"""
        level, reasons = __import__("auditlib").classify_risk(text)
        self.assertEqual(level, "HIGH")
        self.assertIn("high-signal:ranking_or_market_share", reasons)

    def test_specific_export_is_high_but_generic_export_is_medium(self):
        mod = __import__("auditlib")
        high, _ = mod.classify_risk("產品主要出口美國與日本。")
        medium, _ = mod.classify_risk("產品以出口為主。")
        self.assertEqual(high, "HIGH")
        self.assertEqual(medium, "MEDIUM")

    def test_financial_section_keywords_do_not_affect_report_risk(self):
        report = GOOD_REPORT.replace(
            "| 營業收入 | 44168.00 |",
            "| 營業收入 | 44168.00 |\n\n合併財務資料僅供測試。"
        )
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "1304_台聚.md"
            path.write_text(report, encoding="utf-8")
            result = scan_report(path)
            self.assertNotIn("high-impact-term:合併", result.risk_reasons)

    def test_financial_exact_auto_verifies(self):
        status = financial_auto_verify(
            issuer_match=True, period_match=True, statement_scope_match=True,
            currency_match=True, unit_match=True, mapping_unambiguous=True,
            original_value=44168.00, official_value=44168.00,
        )
        self.assertEqual(status, "AUTO_VERIFIED")

    def test_financial_difference_does_not_auto_pass(self):
        status = financial_auto_verify(
            issuer_match=True, period_match=True, statement_scope_match=True,
            currency_match=True, unit_match=True, mapping_unambiguous=True,
            original_value=-2650.09, official_value=-2651.63,
        )
        self.assertEqual(status, "NEEDS_MODEL_REVIEW")

    def test_method_gap_does_not_auto_pass(self):
        status = financial_auto_verify(
            issuer_match=True, period_match=True, statement_scope_match=True,
            currency_match=True, unit_match=True, mapping_unambiguous=False,
            original_value=-2790.96, official_value=-6405.28,
        )
        self.assertEqual(status, "METHOD_UNRESOLVED")

    def test_carry_forward_requires_all_bindings_equal(self):
        data = dict(
            normalized_claim_hash="a", source_raw_hash="b", source_text_hash="c",
            evidence_span_hash="d", period_binding="2025", issuer_binding="1304",
            policy_binding="narrative-1",
        )
        a = BindingFingerprint(**data)
        b = BindingFingerprint(**data)
        self.assertTrue(carry_forward_eligible(a, b))
        changed = BindingFingerprint(**{**data, "source_text_hash": "changed"})
        self.assertFalse(carry_forward_eligible(a, changed))


if __name__ == "__main__":
    unittest.main()
