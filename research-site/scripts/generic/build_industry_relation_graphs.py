"""Build one reviewed, listed-company relation graph per involved industry.

Run from the repository root with:
    .venv/Scripts/python.exe -X utf8 research-site/scripts/generic/build_industry_relation_graphs.py
"""
from __future__ import annotations

import csv
import html
import json
from collections import Counter, defaultdict
from pathlib import Path

from industries import industry_names, md_escape


ROOT = Path(__file__).resolve().parents[3]
SITE = ROOT / "research-site"
EDGES_CSV = SITE / "data/relations/listed_edges.csv"
COMPANIES_CSV = SITE / "catalog/release-scope-companies.csv"
OUTPUT_DIR = SITE / "chapters/industries/_relations"

# Roles are stated from the annual-report issuer's point of view. The tuple is
# (legend category, Traditional Chinese role, direction of the economic link).
ROLES = {
    "supplier": ("supply", "供應商", "counterparty_to_issuer"),
    "customer": ("customer", "客戶", "issuer_to_counterparty"),
    "parent": ("ownership", "母公司", "counterparty_to_issuer"),
    "subsidiary": ("ownership", "子公司", "issuer_to_counterparty"),
    "investee": ("ownership", "被投資公司", "issuer_to_counterparty"),
    "affiliate": ("affiliate", "關係企業", "undirected"),
}
COLORS = {
    "supply": ("供應", "#b45309"),
    "customer": ("客戶", "#2563eb"),
    "ownership": ("股權", "#7c3aed"),
    "affiliate": ("關係企業", "#64748b"),
}
X = {"left": 190, "middle": 750, "right": 1310}
BOX_W = {"left": 250, "middle": 250, "right": 250}
WIDTH = 1500


def read_inputs() -> tuple[list[dict[str, str]], dict[str, dict[str, str]]]:
    with EDGES_CSV.open(encoding="utf-8-sig", newline="") as fh:
        edges = list(csv.DictReader(fh))
    with COMPANIES_CSV.open(encoding="utf-8-sig", newline="") as fh:
        companies = {row["ticker"]: row for row in csv.DictReader(fh)}
    return edges, companies


def unique_edges(edges: list[dict[str, str]]) -> list[dict[str, str]]:
    """A relation ID is a single publishable fact, even if supplied twice."""
    seen = set()
    result = []
    for edge in edges:
        relation_id = edge["relation_id"]
        if relation_id not in seen:
            result.append(edge)
            seen.add(relation_id)
    return result


def edge_flow(edge: dict[str, str]) -> tuple[str, str, str, bool]:
    """Return category, source ticker, target ticker, and whether it is directed."""
    category, _, direction = ROLES[edge["role"]]
    issuer, other = edge["ticker"], edge["counterparty_ticker"]
    if direction == "counterparty_to_issuer":
        return category, other, issuer, True
    if direction == "issuer_to_counterparty":
        return category, issuer, other, True
    return category, issuer, other, False


def select_industry_edges(
    edges: list[dict[str, str]], industry_tickers: set[str]
) -> list[dict[str, str]]:
    return unique_edges([
        edge for edge in edges
        if edge["ticker"] in industry_tickers
        or edge["counterparty_ticker"] in industry_tickers
    ])


def node_key(ticker: str, other: str, industry_tickers: set[str], directed: bool,
             source: str, target: str) -> tuple[str, str]:
    if ticker in industry_tickers:
        return (ticker, "middle")
    if not directed:
        return (ticker, "left")
    return (ticker, "left" if ticker == source else "right")


def graph_layout(edges: list[dict[str, str]], industry_tickers: set[str]):
    """Place local companies in the middle and external companies by flow."""
    columns: dict[str, set[tuple[str, str]]] = {side: set() for side in X}
    placements = []
    for edge in edges:
        category, source, target, directed = edge_flow(edge)
        issuer, other = edge["ticker"], edge["counterparty_ticker"]
        source_key = node_key(source, target, industry_tickers, directed, source, target)
        target_key = node_key(target, source, industry_tickers, directed, source, target)
        # Affiliates are undirected; put an outside company left of this industry.
        if not directed and issuer not in industry_tickers and other in industry_tickers:
            source_key, target_key = target_key, source_key
        columns[source_key[1]].add(source_key)
        columns[target_key[1]].add(target_key)
        placements.append((edge, category, source_key, target_key, directed))

    middle = sorted(columns["middle"])
    middle_rank = {key: rank for rank, key in enumerate(middle)}
    neighbors: dict[tuple[str, str], list[int]] = defaultdict(list)
    for _, _, source_key, target_key, _ in placements:
        if source_key[1] == "middle" and target_key[1] != "middle":
            neighbors[target_key].append(middle_rank[source_key])
        if target_key[1] == "middle" and source_key[1] != "middle":
            neighbors[source_key].append(middle_rank[target_key])

    ordered = {"middle": middle}
    for side in ("left", "right"):
        ordered[side] = sorted(
            columns[side],
            key=lambda key: (sum(neighbors[key]) / len(neighbors[key]) if neighbors[key]
                             else len(middle), key[0]),
        )
    height = max(260, 125 + max(map(len, ordered.values())) * 38)
    positions = {}
    for side, keys in ordered.items():
        for index, key in enumerate(keys):
            y = 75 + (height - 160) * (index + 0.5) / len(keys)
            positions[key] = (X[side], round(y, 2))
    return placements, positions, height


def _svg_path(start: tuple[float, float], end: tuple[float, float],
              start_side: str, end_side: str, offset: float) -> str:
    x1, y1 = start
    x2, y2 = end
    if start_side == end_side == "middle":
        bend = max(75, 100 + abs(y2 - y1) * 0.16 + offset)
        return (f"M{x1 + 127:.1f},{y1:.1f} C{x1 + 127 + bend:.1f},{y1:.1f} "
                f"{x2 + 127 + bend:.1f},{y2:.1f} {x2 + 127:.1f},{y2:.1f}")
    # Affiliate lines may point from a middle node to the left without arrows.
    if x1 <= x2:
        a, b = x1 + 127, x2 - 127
    else:
        a, b = x1 - 127, x2 + 127
    control = (a + b) / 2
    return (f"M{a:.1f},{y1:.1f} C{control:.1f},{y1 + offset:.1f} "
            f"{control:.1f},{y2 + offset:.1f} {b:.1f},{y2:.1f}")


def _label(name: str, limit: int = 17) -> str:
    return name if len(name) <= limit else name[:limit - 1] + "…"


def render_svg(edges: list[dict[str, str]], industry_tickers: set[str],
               company_names: dict[str, str], title: str) -> str:
    placements, positions, height = graph_layout(edges, industry_tickers)
    svg = [
        f'<svg viewBox="0 0 {WIDTH} {height}" role="img" aria-labelledby="relgraph-title" '
        'style="width:100%;height:auto;font-family:inherit;font-size:14px">',
        f'<title id="relgraph-title">{html.escape(title)}：上市公司關係圖</title>',
        '<defs>',
    ]
    for category, (_, color) in COLORS.items():
        if category != "affiliate":
            svg.append(
                f'<marker id="arrow-{category}" viewBox="0 0 10 10" refX="9" refY="5" '
                f'markerWidth="6" markerHeight="6" orient="auto-start-reverse">'
                f'<path d="M0 0 L10 5 L0 10 Z" fill="{color}"/></marker>'
            )
    svg.append('</defs>')
    for side, heading in (("left", "上游：供應商、母公司"),
                          ("middle", "本產業公司"),
                          ("right", "下游：客戶、子公司、被投資公司")):
        svg.append(f'<text x="{X[side]}" y="32" text-anchor="middle" '
                   f'font-size="18" font-weight="bold">{heading}</text>')

    # Spread repeated issuer/counterparty facts so each SVG path stays inspectable.
    group_sizes = Counter((source_key, target_key) for _, _, source_key, target_key, _ in placements)
    group_index: Counter = Counter()
    for edge, category, source_key, target_key, directed in placements:
        pair = (source_key, target_key)
        offset = (group_index[pair] - (group_sizes[pair] - 1) / 2) * 12
        group_index[pair] += 1
        path = _svg_path(positions[source_key], positions[target_key],
                         source_key[1], target_key[1], offset)
        color = COLORS[category][1]
        marker = f' marker-end="url(#arrow-{category})"' if directed else ''
        dash = ' stroke-dasharray="6 4"' if category == "affiliate" else ''
        source_name = company_names[source_key[0]]
        target_name = company_names[target_key[0]]
        role_name = ROLES[edge["role"]][1]
        tooltip = (f'{source_name} → {target_name}：{role_name}｜'
                   f'{edge["period"] or "—"}｜{edge["share_text"] or "—"}｜'
                   f'依據 {edge["fact_id"]}')
        svg.append(
            f'<path data-relation-id="{html.escape(edge["relation_id"], quote=True)}" '
            f'd="{path}" fill="none" stroke="{color}" stroke-width="2.3" '
            f'opacity="0.72"{marker}{dash}><title>{html.escape(tooltip)}</title></path>'
        )

    for (ticker, side), (x, y) in sorted(positions.items(), key=lambda item: (item[0][1], item[1][1])):
        name = company_names[ticker]
        fill, stroke = ("#eef2ff", "#4f46e5") if side == "middle" else ("#f8fafc", "#94a3b8")
        svg.append(
            f'<a href="../companies/{html.escape(ticker, quote=True)}.html">'
            f'<title>{html.escape(name)}（{html.escape(ticker)}）</title>'
            f'<rect x="{x - BOX_W[side] / 2:.1f}" y="{y - 14:.1f}" '
            f'width="{BOX_W[side]}" height="28" rx="5" fill="{fill}" stroke="{stroke}"/>'
            f'<text x="{x}" y="{y + 5:.1f}" text-anchor="middle">'
            f'{html.escape(_label(name))}（{html.escape(ticker)}）</text></a>'
        )
    legend_y = height - 24
    for index, (category, (label, color)) in enumerate(COLORS.items()):
        legend_x = 35 + index * 225
        dash = ' stroke-dasharray="6 4"' if category == "affiliate" else ''
        svg.append(f'<line x1="{legend_x}" y1="{legend_y}" x2="{legend_x + 35}" '
                   f'y2="{legend_y}" stroke="{color}" stroke-width="3"{dash}/>'
                   f'<text x="{legend_x + 43}" y="{legend_y + 5}">{label}</text>')
    svg.append('</svg>')
    return '\n'.join(svg)


def render_table(edges: list[dict[str, str]]) -> str:
    lines = ['| 公司 | 關係 | 對象 | 期間 | 占比/金額 | 依據（fact_id） |',
             '| --- | --- | --- | --- | --- | --- |']
    for edge in edges:
        issuer = f'[{md_escape(edge["company"])}](../companies/{edge["ticker"]}.qmd)'
        other = (f'[{md_escape(edge["counterparty_company"])}]'
                 f'(../companies/{edge["counterparty_ticker"]}.qmd)')
        share_amount = '；'.join(md_escape(x) for x in
                                (edge['share_text'], edge['amount_text']) if x) or '—'
        lines.append('| ' + ' | '.join((issuer, ROLES[edge['role']][1], other,
                                        md_escape(edge['period']) or '—', share_amount,
                                        md_escape(edge['fact_id']))) + ' |')
    return '\n'.join(lines)


def render_page(edges: list[dict[str, str]], industry_tickers: set[str],
                company_names: dict[str, str], industry_name: str) -> str:
    nodes = {ticker for edge in edges for ticker in
             (edge['ticker'], edge['counterparty_ticker'])}
    lead = (f'{industry_name}關係圖顯示 {len(edges)} 筆關係、{len(nodes)} 家公司。'
            '僅收錄年報載明、逐筆審核的上市公司間關係，並非完整供應鏈。')
    svg = render_svg(edges, industry_tickers, company_names, industry_name)
    return (f'{lead}\n\n'
            '::: {.content-visible when-format="html"}\n'
            '```{=html}\n'
            '<div class="relgraph" style="overflow-x:auto"><div style="min-width:1400px">\n'
            f'{svg}\n</div></div>\n'
            '```\n:::\n\n'
            '::: {.content-visible unless-format="html"}\n'
            '（關係圖僅提供於網站版；完整關係清單如下。）\n'
            ':::\n\n'
            f'{render_table(edges)}\n')


def build() -> dict[str, dict[str, int]]:
    all_edges, companies = read_inputs()
    names = industry_names()
    company_names = {ticker: row['company'] for ticker, row in companies.items()}
    tickers_by_industry: dict[str, set[str]] = defaultdict(set)
    for ticker, row in companies.items():
        tickers_by_industry[row['industry_folder']].add(ticker)
    unknown_roles = {edge['role'] for edge in all_edges} - ROLES.keys()
    if unknown_roles:
        raise ValueError(f'Unknown relation roles: {sorted(unknown_roles)}')
    missing_tickers = {ticker for edge in all_edges for ticker in
                       (edge['ticker'], edge['counterparty_ticker'])} - companies.keys()
    if missing_tickers:
        raise ValueError(f'Relation tickers absent from catalog: {sorted(missing_tickers)}')

    summary = {}
    pages = {}
    for folder, industry_tickers in sorted(tickers_by_industry.items()):
        edges = select_industry_edges(all_edges, industry_tickers)
        if not edges:
            continue
        slug = names[folder]['slug']
        nodes = {ticker for edge in edges for ticker in
                 (edge['ticker'], edge['counterparty_ticker'])}
        summary[slug] = {'edge_count': len(edges), 'node_count': len(nodes)}
        pages[slug] = render_page(edges, industry_tickers, company_names,
                                  names[folder]['name_zh'])
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for slug, page in sorted(pages.items()):
        (OUTPUT_DIR / f'{slug}.qmd').write_text(page, encoding='utf-8')
    (OUTPUT_DIR / '_summary.json').write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    return summary


if __name__ == '__main__':
    result = build()
    print(f'{len(result)} industries, {sum(item["edge_count"] for item in result.values())} '
          f'industry-edge appearances, {len(unique_edges(read_inputs()[0]))} unique relations')
