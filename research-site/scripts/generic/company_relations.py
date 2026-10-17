"""Load reviewed listed-company relations and render a cited company-page table."""
from __future__ import annotations

import csv
import json
import re
from collections import defaultdict
from pathlib import Path

from build_company_pages_all import fact_note


SITE = Path(__file__).resolve().parents[2]
EDGES_CSV = SITE / 'data/relations/listed_edges.csv'
FACTS_DIR = SITE / 'data/company-facts'

INVERSE_ROLE = {
    'customer': 'supplier',
    'supplier': 'customer',
    'parent': 'subsidiary',
    'subsidiary': 'parent',
    'investee': 'investor',
    'affiliate': 'affiliate',
}
ROLE_LABEL = {
    'customer': '客戶',
    'supplier': '供應商',
    'parent': '母公司',
    'subsidiary': '子公司',
    'investee': '被投資公司',
    'investor': '投資方',
    'affiliate': '關係企業',
}
ROLE_ORDER = {role: i for i, role in enumerate(ROLE_LABEL)}


def load_edges(path: Path = EDGES_CSV) -> dict[str, list[dict]]:
    """Index every reviewed edge from both listed companies' viewpoints."""
    by_company: dict[str, list[dict]] = defaultdict(list)
    seen: dict[str, set[tuple[str, str, str, str]]] = defaultdict(set)
    with Path(path).open(encoding='utf-8-sig', newline='') as source:
        for row in csv.DictReader(source):
            issuer_ticker = row['ticker'].strip()
            other_ticker = row['counterparty_ticker'].strip()
            role = row['role'].strip()
            if role not in INVERSE_ROLE:
                raise ValueError(f'Unknown relation role: {role}')
            for page_ticker, page_role, peer_ticker, peer_name in (
                (issuer_ticker, role, other_ticker, row['counterparty_company']),
                (other_ticker, INVERSE_ROLE[role], issuer_ticker, row['company']),
            ):
                key = (peer_ticker, page_role, row['period'], row['fact_id'])
                if key in seen[page_ticker]:
                    continue
                seen[page_ticker].add(key)
                by_company[page_ticker].append({
                    'ticker': page_ticker,
                    'other_ticker': peer_ticker,
                    'other_company': peer_name,
                    'role': page_role,
                    'period': row['period'],
                    'share_text': row['share_text'],
                    'amount_text': row['amount_text'],
                    'fact_id': row['fact_id'],
                    'issuer_ticker': issuer_ticker,
                    'issuer_company': row['company'],
                })
    return dict(by_company)


def _cell(value: object) -> str:
    return str(value or '').replace('|', r'\|').replace('\n', ' ')


def _period_key(period: str) -> tuple[int, str]:
    # ROC years are usually three digits; some rows use a Gregorian year only.
    years = [int(year) for year in re.findall(r'(?<!\d)(?:1\d{2}|20\d{2})(?=\s*年|\s*年度|\s*[）)])', period)]
    return (max((year - 1911 if year > 1911 else year for year in years), default=-1), period)


def render_relations(
    ticker: str, edges: list[dict], notes, facts_dir: Path = FACTS_DIR
) -> list[str]:
    """Render the relations section; add one source footnote for each table row."""
    if not edges:
        return []

    lines = [
        '## 與其他上市櫃公司的往來關係 {.unnumbered}',
        '',
        '本節只列年報明載、且經逐筆審查的上市櫃公司之間關係；不代表完整供應鏈。',
        '',
        '| 對象 | 關係 | 期間 | 占比／金額 | 資料來源 |',
        '|---|---|---|---|---|',
    ]
    documents: dict[str, tuple[dict, dict[str, dict]]] = {}
    ordered = sorted(edges, key=lambda edge: _period_key(edge['period']), reverse=True)
    ordered.sort(key=lambda edge: ROLE_ORDER[edge['role']])
    for edge in ordered:
        issuer = edge['issuer_ticker']
        if issuer not in documents:
            doc = json.loads((Path(facts_dir) / f'{issuer}.json').read_text(encoding='utf-8'))
            documents[issuer] = doc, {fact['id']: fact for fact in doc['facts']}
        doc, facts = documents[issuer]
        fact_id = edge['fact_id']
        if fact_id not in facts:
            raise ValueError(f'Missing fact {fact_id} for issuer {issuer}')
        marker = notes.add(fact_note(doc, facts[fact_id]))
        peer_ticker = edge['other_ticker']
        peer = f'[{_cell(peer_ticker)} {_cell(edge["other_company"])}](../companies/{peer_ticker}.qmd)'
        amount = '；'.join(_cell(value) for value in (edge['share_text'], edge['amount_text']) if value)
        cells = (peer, ROLE_LABEL[edge['role']], _cell(edge['period']), amount,
                 f'{_cell(edge["issuer_company"])}{marker}')
        lines.append('| ' + ' | '.join(cells) + ' |')
    return lines
