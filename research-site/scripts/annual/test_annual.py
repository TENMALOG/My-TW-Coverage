"""Unit tests for slice_annual.py and verify_extraction.py (synthetic texts only, plus one optional live test).

Run: .venv/Scripts/python.exe -X utf8 -m unittest research-site/scripts/annual/test_annual.py
"""
import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import slice_annual as S  # noqa: E402
import verify_extraction as V  # noqa: E402

DOT = "." * 60

SYNTH = (
    "\n[PDF PAGE 1]\n測試實業股份有限公司 \n114 年度年報 \n"
    "\n[PDF PAGE 2]\n目 錄 \n壹、致股東報告書 " + DOT + " 1 \n貳、公司治理報告 " + DOT + " 4 \n"
    "肆、營運概況 " + DOT + " 10 \n一、業務內容 " + DOT + " 10 \n營業比重 " + DOT + " 11 \n"
    "主要原料之供應狀況 " + DOT + " 12 \n最近二年度占進(銷)貨總額百分之十以上之客戶 " + DOT + " 13 \n"
    "\n[PDF PAGE 3]\n壹、致股東報告書 \n本公司營運穩健。\n"
    "\n[PDF PAGE 4]\n肆、營運概況 \n一、業務內容 \n(一)業務範圍 \n本公司從事電子零件製造。 \n"
    "2、主要產品之營業比重 \n電子零件 1,234,567 仟元 85.5 % \n其他 14.5 % \n"
    "\n[PDF PAGE 5]\n(三)主要原料之供應狀況 \n銅材來自國內供應商。 \n"
    "(四)最近二年度任一年度中曾占進(銷)貨總額百分之十以上之客戶名稱 \n甲客戶 銷貨 500,000 仟元 \n"
    "\n[PDF PAGE 6]\n三、從業員工 \n員工 100 人 \n"
)


class SliceTests(unittest.TestCase):
    def test_norm_nfkc_and_whitespace(self):
        self.assertEqual(S.norm("營 業　比重（％）"), "營業比重(%)")

    def test_page_detection(self):
        pages = S.split_pages(SYNTH)
        self.assertEqual([p for p, _s, _e in pages], [1, 2, 3, 4, 5, 6])
        pt = S.page_texts(SYNTH)
        self.assertIn("目 錄", pt[2])
        self.assertIn("電子零件製造", pt[4])

    def test_toc_pages_detected(self):
        self.assertEqual(S.toc_pages(SYNTH), {2})

    def test_toc_skipped_and_real_heading_used(self):
        garbled, legal, secs = S.slice_text(SYNTH * 1)
        self.assertFalse(garbled)
        by = {s["name"]: s for s in secs}
        self.assertEqual(by["business_scope"]["start_page"], 4)
        self.assertEqual(by["business_scope"]["confidence"], "heading")
        self.assertEqual(by["revenue_mix"]["start_page"], 4)
        self.assertEqual(by["raw_materials"]["start_page"], 5)
        self.assertEqual(by["major_customers_suppliers"]["start_page"], 5)
        self.assertEqual(by["employees"]["start_page"], 6)
        for s in secs:
            self.assertNotEqual(s["start_page"], 2, s["name"])
            self.assertNotIn("....", s["text"][:40])

    def test_window_keeps_original_text_and_markers(self):
        _g, _l, secs = S.slice_text(SYNTH)
        by = {s["name"]: s for s in secs}
        self.assertIn("[PDF PAGE 5]", by["business_scope"]["text"])
        self.assertIn("1,234,567 仟元 85.5 %", by["revenue_mix"]["text"])  # un-normalised spacing preserved
        self.assertEqual(by["business_scope"]["end_page"], 6)
        self.assertLessEqual(len(by["business_scope"]["text"]), 6000)

    def test_legal_name(self):
        self.assertEqual(S.find_legal_name(SYNTH), "測試實業股份有限公司")

    def test_keyword_confidence_for_sentence_hit(self):
        text = ("\n[PDF PAGE 1]\n某某股份有限公司\n"
                "\n[PDF PAGE 2]\n肆、營運概況\n本公司於國內市場佔有率約百分之三十，為業界前三大廠商之一，並持續擴充產能。\n")
        _g, _l, secs = S.slice_text(text + "填充" * 300)
        by = {s["name"]: s for s in secs}
        self.assertEqual(by["market_position"]["confidence"], "keyword")

    def test_garbled_detection(self):
        garbled_text = "\n[PDF PAGE 1]\n" + ("abcd1234 " * 200)
        self.assertTrue(S.is_garbled(garbled_text))
        replacement = "\n[PDF PAGE 1]\n" + ("���中" * 200)
        self.assertTrue(S.is_garbled(replacement))
        self.assertFalse(S.is_garbled(SYNTH + "中文內容" * 100))
        g, legal, secs = S.slice_text(garbled_text)
        self.assertTrue(g)
        self.assertEqual(secs, [])


class VerifyTests(unittest.TestCase):
    def test_excerpt_whitespace_and_fullwidth(self):
        nt = S.norm("本公司  營業比重　為 85.5％ ，主要產品")
        self.assertTrue(V.excerpt_in_text("營業比重為85.5%", nt))
        self.assertTrue(V.excerpt_in_text("85.5 ％，主要", nt))
        self.assertFalse(V.excerpt_in_text("營業比重為85.6%", nt))

    def test_numbers_positive(self):
        ex = ["電子零件 1,234,567 仟元 85.5 %"]
        self.assertEqual(V.check_numbers("電子零件營收 1234567 仟元，占 85.5%", "114年度（2025）", ex), [])
        self.assertEqual(V.check_numbers("營收 1,234,567 仟元", "114年度（2025）", ex), [])

    def test_numbers_negative(self):
        ex = ["電子零件 1,234,567 仟元 85.5 %"]
        self.assertEqual(V.check_numbers("占 86.5%", "114年度（2025）", ex), ["86.5"])
        # 12 must not be accepted merely because it is a prefix of 12.5
        self.assertEqual(V.check_numbers("占 12%", "x", ["比重 12.5 %"]), ["12"])

    def test_numbers_flattened_table(self):
        # adjacent table cells run together in the PDF text layer
        ex = ["聲學元件類1,933,81160.61%"]
        self.assertEqual(V.check_numbers("營收為1,933,811仟元，占比60.61%。", "114年度", ex), [])
        # spaced digits and dotted dates
        self.assertEqual(V.check_numbers("114年度員工191人", "x", ["年度 1 1 4 年度 合計 191"]), [])
        self.assertEqual(V.check_numbers("設立日期為民國70年9月5日", "x", ["設立 70.9.05"]), [])
        # a number absent from the run is still caught
        self.assertEqual(V.check_numbers("營收為2,000,000仟元", "x", ex), ["2,000,000"])

    def test_numbers_period_and_roc_year(self):
        ex = ["民國 114 年度營收 500 仟元"]
        self.assertEqual(V.check_numbers("2025 年度營收 500 仟元", "114年度（2025）", ex), [])
        self.assertEqual(V.check_numbers("2025 年度營收 500 仟元", "x", ex), [])  # ROC+1911 equivalence
        self.assertEqual(V.check_numbers("114 年度營收 500 仟元", "x", ["2025 年度營收 500 仟元"]), [])
        self.assertEqual(V.check_numbers("2024 年營收 500 仟元", "x", ex), ["2024"])

    def test_numbers_ignore_list_ordinals(self):
        self.assertEqual(V.check_numbers("(1) 主要產品為電子零件", "x", ["主要產品為電子零件"]), [])
        self.assertEqual(V.check_numbers("1、主要產品為電子零件", "x", ["主要產品為電子零件"]), [])

    def test_page_match_across_page_break(self):
        text = "\n[PDF PAGE 1]\n封面\n\n[PDF PAGE 2]\n本公司主要產品為電\n\n[PDF PAGE 3]\n子零件及其他\n\n[PDF PAGE 4]\n結尾"
        pn = V.page_norms(text)
        self.assertTrue(V.excerpt_on_page("主要產品為電子零件", 2, pn))   # starts on 2, continues to 3
        self.assertFalse(V.excerpt_on_page("主要產品為電子零件", 3, pn))  # starts on 2, not on 3
        self.assertFalse(V.excerpt_on_page("子零件及其他", 1, pn))
        self.assertTrue(V.excerpt_on_page("子零件及其他", 3, pn))
        self.assertFalse(V.excerpt_on_page("結尾", 2, pn))

    def test_identity(self):
        text = "\n[PDF PAGE 1]\n測試實業 股份有限公司\n\n[PDF PAGE 5]\n其他公司股份有限公司"
        self.assertEqual(V.identity_ok("測試實業股份有限公司", "1234", "2025_1234_x_F04.pdf", text), (True, True))
        self.assertEqual(V.identity_ok("其他公司股份有限公司", "1234", "2025_1234_x_F04.pdf", text), (False, True))
        self.assertEqual(V.identity_ok("測試實業股份有限公司", "1235", "2025_1234_x_F04.pdf", text), (True, False))

    def test_schema_validator(self):
        schema = json.loads(V.SCHEMA_PATH.read_text(encoding="utf-8"))
        good = {
            "ticker": "1234", "company": "測試", "legal_name": "測試實業股份有限公司",
            "source": {"citation_url": "u", "fy": 2025, "filename": "f", "text_sha256": "0" * 64, "text_path": "p"},
            "facts": [{"id": "1234-AR-01", "field": "products", "statement": "s", "period": "p", "page": 4,
                       "excerpts": ["電子零件製造"], "attribution": "公司年報揭露"}],
        }
        self.assertEqual(V.validate(good, schema), [])
        bad = json.loads(json.dumps(good))
        bad["facts"][0]["field"] = "unknown"
        bad["facts"][0]["page"] = 0
        bad["facts"][0]["excerpts"] = []
        bad["facts"][0]["extra"] = 1
        bad["ticker"] = "x"
        self.assertGreaterEqual(len(V.validate(bad, schema)), 5)


class LiveCacheTest(unittest.TestCase):
    def test_cached_tickers(self):
        reps = S.latest_reports(tickers={"2208", "1582", "9926"})
        if not reps:
            self.skipTest("cache has none of 2208/1582/9926")
        for t, meta in reps.items():
            if not (S.ROOT / meta["text_path"]).exists():
                continue
            res = S.process(meta)
            self.assertFalse(res["garbled"], t)
            self.assertTrue(res["legal_name"].endswith("公司"), t)
            names = {s["name"] for s in res["sections"]}
            for need in ("business_scope", "revenue_mix", "sales_regions", "major_customers_suppliers"):
                self.assertIn(need, names, f"{t} {need}")
            for s in res["sections"]:
                self.assertNotIn("........", s["text"][:200], f"{t} {s['name']} looks like TOC")


if __name__ == "__main__":
    unittest.main()
