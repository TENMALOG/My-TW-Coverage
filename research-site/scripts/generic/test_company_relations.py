"""Tests for the reviewed listed-company relations section."""
from __future__ import annotations

import csv
import io
import json
import sys
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parent))

from build_company_pages_all import Notes  # noqa: E402
from company_relations import load_edges, render_relations  # noqa: E402


def _edge(role='customer', fact_id='1001-AR-01', period='114年度（2025）'):
    return {
        'ticker': '1001', 'company': '甲公司', 'role': role,
        'counterparty_ticker': '1002', 'counterparty_company': '乙公司',
        'period': period, 'share_text': '12%', 'amount_text': '100元',
        'fact_id': fact_id,
    }


def _load(rows):
    out = io.StringIO()
    writer = csv.DictWriter(out, fieldnames=list(_edge()))
    writer.writeheader()
    writer.writerows(rows)
    with patch.object(Path, 'open', return_value=io.StringIO(out.getvalue())):
        return load_edges(Path('edges.csv'))


def _facts(fact_ids=('1001-AR-01',)):
    doc = {
        'ticker': '1001', 'legal_name': '甲公司股份有限公司',
        'source': {'fy': 2025, 'filename': '2025_1001_report.pdf',
                   'citation_url': 'https://example.test/report.pdf'},
        'facts': [{'id': fact_id, 'page': 8, 'period': '114年度（2025）'}
                  for fact_id in fact_ids],
    }
    return patch.object(Path, 'read_text', return_value=json.dumps(doc, ensure_ascii=False))


def test_role_inversion_and_issuer_preserved():
    inverse = {
        'customer': 'supplier', 'supplier': 'customer',
        'parent': 'subsidiary', 'subsidiary': 'parent',
        'investee': 'investor', 'affiliate': 'affiliate',
    }
    rows = [_edge(role=role, fact_id=f'1001-AR-{i:02d}')
            for i, role in enumerate(inverse, 1)]
    indexed = _load(rows)
    assert {edge['role'] for edge in indexed['1001']} == set(inverse)
    assert [edge['role'] for edge in indexed['1002']] == list(inverse.values())
    assert all(edge['issuer_ticker'] == '1001' and edge['issuer_company'] == '甲公司'
               for edge in indexed['1002'])
    assert all(edge['other_ticker'] == '1001' for edge in indexed['1002'])


def test_dedup_uses_other_role_period_and_fact():
    rows = [_edge(), _edge(), _edge(period='113年度（2024）'),
            _edge(fact_id='1001-AR-02')]
    indexed = _load(rows)
    assert len(indexed['1001']) == len(indexed['1002']) == 3


def test_empty_section_adds_no_note():
    notes = Notes()
    assert render_relations('1001', [], notes) == []
    assert notes.items == []


def test_table_rows_footnotes_links_and_escaping():
    rows = [_edge(), _edge(role='supplier', fact_id='1001-AR-02',
                          period='113年度（2024）')]
    rows[0]['counterparty_company'] = '乙|公司'
    rows[0]['amount_text'] = '100|元'
    indexed = _load(rows)
    notes = Notes()
    with _facts(('1001-AR-01', '1001-AR-02')):
        lines = render_relations('1001', indexed['1001'], notes)
    table_rows = [line for line in lines if line.startswith('| [')]
    assert len(table_rows) == 2
    assert len(notes.items) == 2
    assert '[1002 乙\\|公司](../companies/1002.qmd)' in table_rows[0]
    assert '100\\|元' in table_rows[0]
    assert '[^n1]' in table_rows[0] and '[^n2]' in table_rows[1]
    assert all('example.test/report.pdf' in note for note in notes.items)
    assert lines[0] == '## 與其他上市櫃公司的往來關係 {.unnumbered}'


def test_customer_precedes_supplier_and_period_descends():
    rows = [_edge(role='supplier', fact_id='1001-AR-01'),
            _edge(role='customer', fact_id='1001-AR-02', period='113年度（2024）'),
            _edge(role='customer', fact_id='1001-AR-03')]
    indexed = _load(rows)
    with _facts(('1001-AR-01', '1001-AR-02', '1001-AR-03')):
        lines = render_relations('1001', indexed['1001'], Notes())
    table_rows = [line for line in lines if line.startswith('| [')]
    assert ['114年度' in table_rows[0], '113年度' in table_rows[1]] == [True, True]
    assert '| 客戶 |' in table_rows[0] and '| 客戶 |' in table_rows[1]
    assert '| 供應商 |' in table_rows[2]
