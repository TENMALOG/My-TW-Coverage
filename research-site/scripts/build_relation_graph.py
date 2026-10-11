"""Draw the evidence-backed relation graph (relations.csv) as an inline SVG partial.

Layout: three columns — upstream (suppliers, licensors, parents, partners) | the 10 covered
companies grouped by sub-sector | downstream (customers, contracting agencies, OEMs).
Every edge is a link to its row in the evidence appendix and carries a <title> tooltip.
Output: chapters/industries/_relations-graph.qmd (HTML-only raw block).

  python research-site/scripts/build_relation_graph.py
"""
from __future__ import annotations

import csv
import html
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SITE = ROOT / 'research-site'
REL = SITE / 'data/aerospace-defense/relations.csv'
OUT = SITE / 'chapters/industries/_relations-graph.qmd'

CENTER = [('航空製造', ['漢翔', '晟田', '長亨', '駐龍', '寶一']),
          ('航空器維修', ['長榮航太', '亞航']),
          ('造船', ['台船', '中信造船', '龍德造船'])]
COVERED = {c for _, cs in CENTER for c in cs}
# relation → (category, which side the counterparty sits on)
UPSTREAM_TYPES = ('供應商', '母公司', '授權', '技術支援', '專案分工')
COLORS = {'客戶與契約': '#2563eb', '供應': '#d97706', '合作與授權': '#6b7280', '股權': '#7c3aed'}


def classify(r):
    s, o, t = r['subject'], r['object'], r['relation_type']
    if s in COVERED and o in COVERED:
        return '供應', s, o, 'mid'
    if s not in COVERED:  # counterparty is subject
        if t.startswith('客戶'):
            return '客戶與契約', o, s, 'down'
        if '母公司' in t:
            return '股權', o, s, 'up'
        if t.startswith('供應商'):
            return '供應', o, s, 'up'
        return '合作與授權', o, s, 'up'
    # covered company is subject; licences/partnerships first (「授權維修中心」 also contains 維修)
    if '授權' in t or '技術支援' in t or '專案分工' in t:
        return '合作與授權', s, o, 'up'
    if t.startswith('供應商') or t.startswith('合格供應商') or '建造' in t or '維修' in t or '受託' in t or '商維' in t:
        return '客戶與契約', s, o, 'down'
    return '合作與授權', s, o, 'down'


def main():
    rows = list(csv.DictReader(open(REL, encoding='utf-8')))
    edges = [(r, *classify(r)) for r in rows]
    up, down = [], []
    for r, cat, comp, other, side in edges:
        if side == 'up' and other not in up:
            up.append(other)
        if side == 'down' and other not in down:
            down.append(other)
    W, row_h, top = 1000, 30, 40
    xL, xC, xR = 140, 500, 860
    pos = {}
    for i, n in enumerate(up):
        pos[n] = (xL, top + 20 + i * row_h * 1.6)
    y = top + 20
    groups = []
    for g, cs in CENTER:
        groups.append((g, y))
        y += 22
        for c in cs:
            pos[c] = (xC, y); y += row_h
        y += 14
    for i, n in enumerate(down):
        pos[n] = (xR, top + 20 + i * row_h)
    H = int(max(y, top + 20 + len(down) * row_h, top + 20 + len(up) * row_h * 1.6) + 40)

    S = [f'<svg viewBox="0 0 {W} {H}" role="img" aria-labelledby="relgraph-title" '
         f'style="width:100%;height:auto;font-family:inherit;font-size:13px">',
         '<title id="relgraph-title">航太與國防產業有證據的公司關係圖</title>',
         f'<text x="{xL}" y="22" text-anchor="middle" font-weight="bold">上游：供應、授權、股權</text>',
         f'<text x="{xC}" y="22" text-anchor="middle" font-weight="bold">本章公司</text>',
         f'<text x="{xR}" y="22" text-anchor="middle" font-weight="bold">下游：客戶、發包機關、原廠</text>']
    for r, cat, comp, other, side in edges:
        if side == 'mid':
            (x1, y1), (x2, y2) = pos[r['subject']], pos[r['object']]
            path = f'M{x1 + 60},{y1} C{x1 + 140},{y1} {x2 + 140},{y2} {x2 + 60},{y2}'
        elif side == 'up':
            (x1, y1), (x2, y2) = pos[other], pos[comp]
            path = f'M{x1 + 100},{y1} C{x1 + 200},{y1} {x2 - 200},{y2} {x2 - 60},{y2}'
        else:
            (x1, y1), (x2, y2) = pos[comp], pos[other]
            path = f'M{x1 + 60},{y1} C{x1 + 200},{y1} {x2 - 200},{y2} {x2 - 100},{y2}'
        dash = ' stroke-dasharray="5 4"' if cat == '合作與授權' else ''
        tip = html.escape(f'{r["subject"]} → {r["object"]}：{r["relation_type"]}｜{r["scope"]}｜{r["period"]}｜{r["attribution"]}〔{r["relation_id"]}〕')
        S.append(f'<a href="../../appendices/evidence.html#rel-{r["relation_id"]}"><path d="{path}" fill="none" '
                 f'stroke="{COLORS[cat]}" stroke-width="2.2" opacity="0.8"{dash}><title>{tip}</title></path></a>')
    for g, gy in groups:
        S.append(f'<text x="{xC}" y="{gy + 4}" text-anchor="middle" fill="#6b7280" font-size="12">{html.escape(g)}</text>')
    for n, (x, y) in pos.items():
        covered = n in COVERED
        w = 120 if covered else (200 if x != xC else 120)
        S.append(f'<rect x="{x - w / 2}" y="{y - 11}" width="{w}" height="22" rx="5" '
                 f'fill="{"#eef2ff" if covered else "#f9fafb"}" stroke="{"#4f46e5" if covered else "#d1d5db"}"/>')
        label = n if len(n) <= 18 else n[:17] + '…'
        S.append(f'<text x="{x}" y="{y + 4}" text-anchor="middle"><title>{html.escape(n)}</title>{html.escape(label)}</text>')
    lx = 20
    for cat, col in COLORS.items():
        dash = ' stroke-dasharray="5 4"' if cat == '合作與授權' else ''
        S.append(f'<line x1="{lx}" y1="{H - 16}" x2="{lx + 30}" y2="{H - 16}" stroke="{col}" stroke-width="2.5"{dash}/>'
                 f'<text x="{lx + 36}" y="{H - 12}">{cat}</text>')
        lx += 150
    S.append('</svg>')
    OUT.write_text('<!-- 由 scripts/build_relation_graph.py 產生 -->\n\n::: {.content-visible when-format="html"}\n```{=html}\n'
                   + '<div class="relgraph" style="overflow-x:auto"><div style="min-width:760px">'
                   + '\n'.join(S) + '</div></div>\n```\n:::\n\n::: {.content-visible unless-format="html"}\n'
                   '（互動關係圖僅提供於網站版；關係清單見證據附錄。）\n:::\n', encoding='utf-8')
    print(f'{len(edges)} edges, {len(up)} upstream, {len(down)} downstream nodes -> {OUT.relative_to(ROOT).as_posix()}')


if __name__ == '__main__':
    main()
