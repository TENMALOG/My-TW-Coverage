from pathlib import Path
import importlib.util
import tempfile
import unittest

MODULE_PATH = Path(__file__).resolve().parents[1] / "official_financial_check.py"
spec = importlib.util.spec_from_file_location("official_financial_check", MODULE_PATH)
mod = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(mod)


class OfficialFinancialCheckTests(unittest.TestCase):
    def test_parse_number(self):
        self.assertEqual(mod.parse_number("1,234"), 1234.0)
        self.assertEqual(mod.parse_number("(123)"), -123.0)
        self.assertIsNone(mod.parse_number("-"))

    def test_roc_year_and_quarter(self):
        self.assertEqual(mod.roc_year("115"), 2026)
        self.assertEqual(mod.quarter_number("2"), 2)
        self.assertEqual(mod.quarter_number("Q3"), 3)

    def test_repo_quarterly_ytd_sum(self):
        text = """### 季度關鍵財務數據 (近 4 季)
| | 2026-06-30 | 2026-03-31 | 2025-12-31 |
|---|---:|---:|---:|
| Revenue | 20.00 | 10.00 | 9.00 |
| Gross Profit | 8.00 | 4.00 | 3.00 |
| Operating Income | 3.00 | 1.00 | 0.50 |
| Net Income | 2.00 | 1.00 | 0.25 |
"""
        value, basis = mod.repo_metric_value(text, "revenue", 2026, 2)
        self.assertEqual(value, 30.0)
        self.assertEqual(basis, "quarterly-ytd")

    def test_repo_annual_q4(self):
        text = """### 年度關鍵財務數據 (近 3 年)
| | 2025-12-31 | 2024-12-31 |
|---|---:|---:|
| Revenue | 100.00 | 90.00 |
| Gross Profit | 20.00 | 18.00 |
| Operating Income | 10.00 | 9.00 |
| Net Income | 8.00 | 7.00 |
"""
        value, basis = mod.repo_metric_value(text, "revenue", 2025, 4)
        self.assertEqual(value, 100.0)
        self.assertEqual(basis, "annual")


if __name__ == "__main__":
    unittest.main()
