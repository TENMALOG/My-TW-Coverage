from pathlib import Path
import importlib.util
import tempfile

MODULE = Path(__file__).resolve().parents[1] / "credit_services_refresh.py"
spec = importlib.util.spec_from_file_location("credit_services_refresh", MODULE)
mod = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(mod)


def test_statement_rows_and_metric_mapping():
    html = """
    <table>
      <tr><td>營業收入合計</td></tr>
      <tr><td>營業毛利（毛損）淨額</td></tr>
      <tr><td>營業利益（損失）</td></tr>
      <tr><td>母公司業主（淨利∕損）</td></tr>
    </table>
    <table>
      <tr><td>1,000</td></tr>
      <tr><td>500</td></tr>
      <tr><td>200</td></tr>
      <tr><td>100</td></tr>
    </table>
    """
    rows = mod.statement_rows(html)
    assert mod.metric_value(rows, "revenue") == 1000.0
    assert mod.metric_value(rows, "gross_profit") == 500.0
    assert mod.metric_value(rows, "operating_income") == 200.0
    assert mod.metric_value(rows, "net_income") == 100.0


def test_patch_report_recomputes_margins():
    text = """### 季度關鍵財務數據 (近 4 季)
|                         | 2026-06-30 | 2026-03-31 | 2025-12-31 | 2025-09-30 |
|:------------------------|-----------:|-----------:|-----------:|-----------:|
| Revenue                 | 60.00 | 40.00 | 30.00 | 20.00 |
| Gross Profit            | 12.00 | 8.00 | 6.00 | 4.00 |
| Gross Margin (%)        | 20.00 | 20.00 | 20.00 | 20.00 |
| Operating Income        | 6.00 | 4.00 | 3.00 | 2.00 |
| Operating Margin (%)    | 10.00 | 10.00 | 10.00 | 10.00 |
| Net Income              | 3.00 | 2.00 | 1.50 | 1.00 |
| Net Margin (%)          | 5.00 | 5.00 | 5.00 | 5.00 |
"""
    with tempfile.TemporaryDirectory() as td:
        p = Path(td) / "5871_test.md"
        p.write_text(text, encoding="utf-8")
        changed = mod.patch_report(p, {
            "revenue": (100.0, 120.0),
            "gross_profit": (50.0, 60.0),
            "operating_income": (20.0, 24.0),
            "net_income": (10.0, 12.0),
        })
        assert changed
        out = p.read_text(encoding="utf-8")
        assert "120.00" in out
        assert "100.00" in out
        assert "50.00" in out
        assert "20.00" in out
        assert "10.00" in out


if __name__ == "__main__":
    test_statement_rows_and_metric_mapping()
    test_patch_report_recomputes_margins()
    print("credit services tests passed")
