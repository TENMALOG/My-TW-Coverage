"""Unit tests for the industry-generic generators.

  .venv/Scripts/python.exe -X utf8 -m unittest research-site/scripts/generic/test_generic.py -v
"""
from __future__ import annotations

import json
import re
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import industries as ind  # noqa: E402
import build_company_pages_all as pages  # noqa: E402
import build_industry_chapters as chapters  # noqa: E402
import build_verified_sentences as vs  # noqa: E402

BANNED = ('待補充', 'TBD', 'TODO', '待更新')
ROW = {'ticker': '9999', 'company': '測試電', 'industry_folder': 'Electronic Components'}


def facts_doc(ticker='9999', legal='測試電子股份有限公司', filename='2025_9999_20260520F04.pdf', facts=None):
    return {'ticker': ticker, 'company': '測試電', 'legal_name': legal,
            'source': {'citation_url': 'https://doc.twse.com.tw/example.pdf', 'fy': 2025, 'filename': filename,
                       'text_sha256': '0' * 64, 'text_path': 'x.txt'},
            'facts': facts if facts is not None else [
                {'id': '9999-AR-01', 'field': 'products', 'statement': '主要產品為被動元件。', 'period': '114年度（2025）',
                 'page': 12, 'excerpts': ['主要產品為被動元件'], 'attribution': '公司年報揭露',
                 'verification': {'status': 'PASS'}},
                {'id': '9999-AR-02', 'field': 'major_customers', 'statement': '這是一條未通過核對的事實。',
                 'period': '114年度（2025）', 'page': 30, 'excerpts': ['未通過'], 'attribution': '公司年報揭露',
                 'verification': {'status': 'FAIL'}},
                {'id': '9999-AR-03', 'field': 'employees', 'statement': '這是一條尚未核對的事實。',
                 'period': '114年度（2025）', 'page': 31, 'excerpts': ['尚未核對'], 'attribution': '公司年報揭露'},
            ]}


def bank_fin():
    items = {'利息淨收益': 1000, '營業費用': 400, '本期稅後淨利（淨損）': 500, '基本每股盈餘（元）': 1, '空項目': None}
    src = {'url': 'https://mopsov.twse.com.tw/mops/web/ajax_t163sb04', 'post': {'year': '114', 'season': '04', 'TYPEK': 'sii'},
           'captured_at': '2026-10-10T00:00:00'}
    return {'ticker': '9999', 'company': '測試電', 'basis': '合併綜合損益表彙總',
            'years': {'2025': {'mops_company_name': '測試電', 'table_kind': '銀行業', 'items_k': items,
                               'gross_margin_pct': None, 'operating_margin_pct': None, 'source': src}}}


SENTENCE = {'claim_id': '9999:x:1', 'ticker': '9999', 'company': '測試電', 'industry_folder': 'Electronic Components',
            'claim_type': '具名客戶／供應關係', 'text': '測試電供應[[Apple]]零件*。', 'basis': 'x', 'period': '2025',
            'citations': [{'url': 'https://news.example.com/a', 'title': '測試新聞', 'locator': '第3段',
                           'publication_date': '2025-01-01', 'support_excerpt': '原文', 'inspection_method': 'captured_content'},
                          {'url': 'claim-input://internal', 'title': '內部', 'locator': None, 'publication_date': None,
                           'support_excerpt': 'x', 'inspection_method': 'captured_content'}]}


def render(fin=None, sentences=(), facts_result=(None, [], 0, []), claims_=()):
    return pages.render_page(ROW, fin=fin, sentences=list(sentences), company_claims=list(claims_),
                             facts_result=facts_result, industry_zh='電子零組件', industry_slug='electronic-components')


class TestSlugs(unittest.TestCase):
    def test_slug_examples(self):
        self.assertEqual(ind.slugify('Electronic Components'), 'electronic-components')
        self.assertEqual(ind.slugify('Aerospace & Defense'), 'aerospace-defense')
        self.assertEqual(ind.slugify('Real Estate - Development'), 'real-estate-development')
        self.assertEqual(ind.slugify('Furnishings, Fixtures & Appliances'), 'furnishings-fixtures-appliances')

    def test_slugs_unique_stable_and_cover_catalog(self):
        names = ind.industry_names()
        folders = {r['industry_folder'] for r in ind.companies()}
        self.assertEqual(set(names), folders)
        slugs = [v['slug'] for v in names.values()]
        self.assertEqual(len(slugs), len(set(slugs)))
        for f, v in names.items():
            self.assertEqual(v['slug'], ind.slugify(f))
            self.assertRegex(v['slug'], r'^[a-z0-9]+(-[a-z0-9]+)*$')
            self.assertTrue(v['name_zh'] and not v['name_zh'].endswith('?'))

    def test_order_by_count(self):
        order = ind.ordered_industries()
        self.assertEqual(order[0][0], 'Electronic Components')
        self.assertEqual([n for _, n in order], sorted((n for _, n in order), reverse=True))


class TestIdentityGate(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.dir = Path(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def write(self, doc, tk='9999'):
        (self.dir / f'{tk}.json').write_text(json.dumps(doc, ensure_ascii=False), encoding='utf-8')

    def test_matching_file_accepted(self):
        self.write(facts_doc())
        doc, ok, failed, gate = pages.load_company_facts('9999', '測試電', self.dir)
        self.assertIsNotNone(doc)
        self.assertEqual(gate, [])
        self.assertEqual([f['id'] for f in ok], ['9999-AR-01'])
        self.assertEqual(failed, 2)

    def test_wrong_company_rejected(self):
        self.write(facts_doc(legal='另一家光學股份有限公司', filename='2025_1234_20260520F04.pdf'))
        doc, ok, failed, gate = pages.load_company_facts('9999', '測試電', self.dir)
        self.assertIsNone(doc)
        self.assertEqual(ok, [])
        self.assertTrue(gate)
        text, st = render(facts_result=(doc, ok, failed, gate))
        self.assertIn('身分核對', text)
        self.assertNotIn('另一家光學', text.split('## 資料缺口')[0])
        self.assertNotIn('被動元件', text)
        self.assertTrue(st['facts_rejected'])

    def test_wrong_name_same_ticker_rejected(self):
        self.write(facts_doc(legal='另一家光學股份有限公司'))
        self.assertTrue(pages.load_company_facts('9999', '測試電', self.dir)[3])

    def test_wrong_filename_ticker_rejected(self):
        self.write(facts_doc(filename='2025_1234_20260520F04.pdf'))
        self.assertTrue(pages.load_company_facts('9999', '測試電', self.dir)[3])

    def test_name_in_order(self):
        self.assertTrue(pages.name_in_order('台積電', '台灣積體電路製造股份有限公司'))
        self.assertTrue(pages.name_in_order('貿聯-KY', 'BizLink Holding Inc. 貿聯控股'))
        self.assertFalse(pages.name_in_order('積台', '台灣積體電路製造股份有限公司'))

    def test_missing_dir(self):
        self.assertEqual(pages.load_company_facts('9999', '測試電', self.dir / 'nope'), (None, [], 0, []))


class TestRendering(unittest.TestCase):
    def test_only_pass_facts_rendered(self):
        doc = facts_doc()
        ok = [f for f in doc['facts'] if (f.get('verification') or {}).get('status') == 'PASS']
        text, st = render(facts_result=(doc, ok, 2, []))
        self.assertIn('主要產品為被動元件', text)
        self.assertNotIn('未通過核對的事實', text)
        self.assertNotIn('尚未核對的事實', text)
        self.assertIn('2 條事實未通過逐字核對', text)
        self.assertIn('第 12 頁', text)
        self.assertEqual(st['pass_facts'], 1)

    def test_page_without_anything_has_gaps(self):
        text, st = render()
        for h in ('公司基本資料', '產品與營收結構', '財務摘要', '客戶、供應商與市場地位', '資料缺口', '資料來源'):
            self.assertIn(f'## {h}', text)
        self.assertIn('查無本公司資料', text)
        self.assertIn('缺少已驗證內容的段落', text)
        self.assertIn('原查核範圍沒有選入本公司的敘述', text)
        for b in BANNED:
            self.assertNotIn(b, text)
        self.assertNotIn('〔', text)
        self.assertFalse(st['financials'])

    def test_non_general_financial_table(self):
        text, st = render(fin=bank_fin())
        self.assertIn('| 利息淨收益 | — | 1,000 |', text)
        self.assertIn('銀行業', text)
        self.assertNotIn('毛利率 |', text)
        self.assertNotIn('基本每股盈餘', text)
        self.assertNotIn('空項目', text)
        self.assertIn('2024 年度在公開資訊觀測站彙總表中查無本公司資料', text)
        self.assertTrue(st['financials'])

    def test_verified_sentence_citations(self):
        text, st = render(sentences=[SENTENCE])
        body, notes_part = text.split('## 資料來源')
        line = next(l for l in body.splitlines() if '測試電供應' in l)
        self.assertIn('Apple', line)
        self.assertNotIn('[[', line)
        self.assertIn(r'零件\*', line)
        mark = re.search(r'\[\^(n\d+)\]$', line).group(1)
        note = next(l for l in notes_part.splitlines() if l.startswith(f'[^{mark}]:'))
        self.assertIn('測試新聞', note)
        self.assertIn('第3段', note)
        self.assertIn('<https://news.example.com/a>', note)
        self.assertNotIn('claim-input', text)
        self.assertEqual(st['verified_sentences'], 1)

    def test_sentence_without_public_source_not_rendered(self):
        s = dict(SENTENCE, citations=[SENTENCE['citations'][1]])
        text, st = render(sentences=[s])
        self.assertNotIn('測試電供應', text)
        self.assertEqual(st['verified_sentences'], 0)

    def test_md_escape(self):
        self.assertEqual(ind.md_escape('A [[B]] $5 @x 〔y〕'), r'A B \$5 \@x （y）')


class TestVerifiedSentences(unittest.TestCase):
    def test_built_file_matches_publishable_claims(self):
        if not ind.VERIFIED.exists():
            self.skipTest('verified-sentences.jsonl not built yet')
        rows = ind.jsonl(ind.VERIFIED)
        pub = [c for c in ind.claims() if c['adoptable_text'].strip()]
        self.assertEqual(len(rows), len(pub))
        for r in rows:
            self.assertTrue(r['citations'])
            sigs = [json.dumps(c, sort_keys=True, ensure_ascii=False) for c in r['citations']]
            self.assertEqual(len(sigs), len(set(sigs)))

    def test_batch_parse(self):
        self.assertEqual(vs.batch_of('新句 REVISED_SUPPORTED（第1輪，revision-batch-008，revision:a:b）'), 'revision-batch-008')
        self.assertEqual(vs.batch_of('x（第2輪，revision-orig-alt-001，revision:a:b）'), 'revision-orig-alt-001')


class TestIndustryChapter(unittest.TestCase):
    def test_chapter_render(self):
        names = ind.industry_names()
        fin = bank_fin()
        gen = json.loads(json.dumps(fin))
        gen['ticker'] = '9998'
        gen['years']['2025'].update(table_kind='一般業', gross_margin_pct=20.0, operating_margin_pct=5.0,
                                    items_k={'營業收入': 2000000})
        rows = [ROW, dict(ROW, ticker='9998', company='測試二')]
        with tempfile.TemporaryDirectory() as d:
            text = chapters.render_chapter('Electronic Components', rows, names=names, fins={'9999': fin, '9998': gen},
                                           verified={'9999': [SENTENCE]}, claim_rows=[], analysis_dir=Path(d))
            self.assertNotIn('include _analysis', text)
            (Path(d) / 'electronic-components.qmd').write_text('x', encoding='utf-8')
            text2 = chapters.render_chapter('Electronic Components', rows, names=names, fins={'9999': fin, '9998': gen},
                                            verified={}, claim_rows=[], analysis_dir=Path(d))
            self.assertIn('{{< include _analysis/electronic-components.qmd >}}', text2)
        self.assertIn('[測試電](../companies/9999.qmd)', text)
        self.assertIn('| 9998 | [測試二](../companies/9998.qmd) | 2,000 | 20.00% | 0 |', text)
        self.assertIn('具名客戶與供應關係', text)
        self.assertIn('測試新聞', text)
        for b in BANNED:
            self.assertNotIn(b, text)


if __name__ == '__main__':
    unittest.main()
