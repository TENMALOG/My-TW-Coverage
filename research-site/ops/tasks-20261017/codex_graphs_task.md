# Task for Codex: per-industry relation graphs (workspace-write)

Repo root = current directory. Python: `.venv/Scripts/python.exe -X utf8`. You may ONLY create:
- `research-site/scripts/generic/build_industry_relation_graphs.py`
- `research-site/scripts/generic/test_industry_relation_graphs.py`
- files under `research-site/chapters/industries/_relations/` (generated output)
Do not modify any existing file. No web access. Do not commit.

## Inputs
- `research-site/data/relations/listed_edges.csv` — reviewed, publishable edges between listed
  companies. Columns: relation_id, ticker, company (the issuer whose annual report states it), role
  (from the ISSUER's point of view: customer = counterparty buys from issuer; supplier =
  counterparty sells to issuer; parent / subsidiary / investee / affiliate), counterparty,
  counterparty_kind, counterparty_ticker, counterparty_company, period, share_text, amount_text,
  fact_id, match_rule. Read with encoding `utf-8-sig`.
- `research-site/catalog/release-scope-companies.csv` — ticker, company, industry_folder.
- Industry slugs and Chinese names: `research-site/scripts/generic/industries.py`
  (`industry_names()` → {folder: {slug, name_zh, ...}}).
- Style reference (read only): `research-site/scripts/build_relation_graph.py` (aerospace graph).

## Output
For every industry folder that has at least one edge where the issuer OR the counterparty belongs
to that industry, write `research-site/chapters/industries/_relations/{slug}.qmd` containing:
1. A short Traditional Chinese lead sentence: number of edges and companies shown, and that the
   graph only shows relations between listed companies that annual reports state and that were
   reviewed one by one; it is not a complete supply chain.
2. An HTML-only inline SVG (same wrapper pattern as build_relation_graph.py:
   `::: {.content-visible when-format="html"}` + ```` ```{=html} ```` block; for other formats a
   one-line note). Three columns: left = upstream of this industry's companies (suppliers to them,
   parents/shareholders), middle = this industry's companies involved, right = downstream
   (customers, subsidiaries, investees). Affiliates: draw between the two nodes with a dashed line.
   Edge colour by type (supply, customer, ownership, affiliate) with a legend. Every node of a
   listed company links to `../companies/{ticker}.html`; every edge has a `<title>` tooltip
   「A → B：關係｜period｜share_text｜依據 fact_id」. Long names truncated with full name in title.
   Must render readably for industries with up to ~150 edges (grow height; horizontal scroll ok).
3. A compact Markdown table (also for PDF) listing every edge: 公司, 關係, 對象, 期間, 占比/金額,
   依據（fact_id）. Company names link to their pages (`../companies/{ticker}.qmd`).
Also write `research-site/chapters/industries/_relations/_summary.json` with edge and node counts
per slug.

## Tests (`python -m pytest`)
Role → column mapping, an edge whose counterparty is in the industry appears with correct
direction, no duplicate edges, output file per expected slug, HTML escaping of names.

## Acceptance
Run the script and the tests; both pass. Final message (Traditional Chinese): what was built, counts.
