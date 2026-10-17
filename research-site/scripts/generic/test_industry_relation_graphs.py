"""Focused tests for reviewed, listed-company industry graphs."""
from __future__ import annotations

import json
from collections import Counter, defaultdict

from build_industry_relation_graphs import (
    OUTPUT_DIR,
    ROLES,
    edge_flow,
    graph_layout,
    read_inputs,
    render_page,
    select_industry_edges,
    unique_edges,
)
from industries import industry_names


def row(role: str, relation_id: str = 'REL-TEST', company: str = '甲公司',
        other: str = '乙公司') -> dict[str, str]:
    return {
        'relation_id': relation_id, 'ticker': '1001', 'company': company,
        'role': role, 'counterparty': other, 'counterparty_kind': 'named',
        'counterparty_ticker': '1002', 'counterparty_company': other,
        'period': '2025', 'share_text': '12%', 'amount_text': '100',
        'fact_id': 'FACT-1', 'match_rule': 'test',
    }


def test_role_to_column_and_direction():
    expected = {
        'supplier': ('supply', '1002', '1001', True),
        'customer': ('customer', '1001', '1002', True),
        'parent': ('ownership', '1002', '1001', True),
        'subsidiary': ('ownership', '1001', '1002', True),
        'investee': ('ownership', '1001', '1002', True),
        'affiliate': ('affiliate', '1001', '1002', False),
    }
    assert set(ROLES) == set(expected)
    for role, flow in expected.items():
        assert edge_flow(row(role)) == flow
    assert graph_layout([row('supplier')], {'1001'})[0][0][2:4] == (
        ('1002', 'left'), ('1001', 'middle'))
    assert graph_layout([row('customer')], {'1001'})[0][0][2:4] == (
        ('1001', 'middle'), ('1002', 'right'))
    assert graph_layout([row('parent')], {'1001'})[0][0][2:4] == (
        ('1002', 'left'), ('1001', 'middle'))
    assert graph_layout([row('subsidiary')], {'1001'})[0][0][2:4] == (
        ('1001', 'middle'), ('1002', 'right'))


def test_counterparty_in_industry_reverses_side():
    supplier = row('supplier')
    assert select_industry_edges([supplier], {'1002'}) == [supplier]
    assert graph_layout([supplier], {'1002'})[0][0][2:4] == (
        ('1002', 'middle'), ('1001', 'right'))
    customer = row('customer')
    assert graph_layout([customer], {'1002'})[0][0][2:4] == (
        ('1001', 'left'), ('1002', 'middle'))
    parent = row('parent')
    assert graph_layout([parent], {'1002'})[0][0][2:4] == (
        ('1002', 'middle'), ('1001', 'right'))
    subsidiary = row('subsidiary')
    assert graph_layout([subsidiary], {'1002'})[0][0][2:4] == (
        ('1001', 'left'), ('1002', 'middle'))


def test_duplicate_relation_id_is_rendered_once():
    edge = row('supplier')
    selected = select_industry_edges([edge, dict(edge)], {'1001'})
    assert len(selected) == 1
    page = render_page(selected, {'1001'}, {'1001': '甲公司', '1002': '乙公司'}, '測試')
    assert page.count('data-relation-id="REL-TEST"') == 1
    assert page.count('FACT-1') == 2  # SVG tooltip and Markdown row


def test_html_escapes_names_and_keeps_full_name_in_title():
    issuer = '<甲 & "公司">很長很長的公司名稱'
    other = '<乙 & "公司">'
    edge = row('affiliate', company=issuer, other=other)
    page = render_page([edge], {'1001'}, {'1001': issuer, '1002': other}, '測試')
    svg = page.split('```{=html}\n', 1)[1].split('\n```', 1)[0]
    assert '&lt;甲 &amp; &quot;公司&quot;&gt;' in svg
    assert '&lt;乙 &amp; &quot;公司&quot;&gt;' in svg
    assert issuer not in svg
    assert '<title>&lt;甲 &amp; &quot;公司&quot;&gt;很長很長的公司名稱' in svg
    assert 'stroke-dasharray="6 4"' in svg
    assert 'href="../companies/1001.html"' in svg
    assert '](../companies/1002.qmd)' in page


def test_generated_files_cover_exactly_expected_slugs_and_counts():
    edges, companies = read_inputs()
    names = industry_names()
    tickers_by_industry = defaultdict(set)
    for ticker, company in companies.items():
        tickers_by_industry[company['industry_folder']].add(ticker)
    expected = {}
    for folder, tickers in tickers_by_industry.items():
        selected = select_industry_edges(edges, tickers)
        if selected:
            nodes = {ticker for edge in selected for ticker in
                     (edge['ticker'], edge['counterparty_ticker'])}
            expected[names[folder]['slug']] = {
                'edge_count': len(selected), 'node_count': len(nodes),
            }
    summary = json.loads((OUTPUT_DIR / '_summary.json').read_text(encoding='utf-8'))
    assert summary == expected
    assert {path.stem for path in OUTPUT_DIR.glob('*.qmd')} == set(expected)
    for slug, counts in expected.items():
        page = (OUTPUT_DIR / f'{slug}.qmd').read_text(encoding='utf-8')
        assert page.count('data-relation-id=') == counts['edge_count']
        assert page.count('\n| [') == counts['edge_count']
    assert len(unique_edges(edges)) == len({edge['relation_id'] for edge in edges})
    assert all(count == 1 for count in Counter(edge['relation_id'] for edge in edges).values())
