# Task for Codex: company-page relations section module (workspace-write)

Repo root = current directory. Python: `.venv/Scripts/python.exe -X utf8`. You may ONLY create:
- `research-site/scripts/generic/company_relations.py`
- `research-site/scripts/generic/test_company_relations.py`
Do not modify any existing file. No web access. Do not commit.

## Inputs
- `research-site/data/relations/listed_edges.csv` (read with `utf-8-sig`): reviewed edges between
  listed companies. `ticker`/`company` = issuer whose annual report states the relation; `role`
  is from the ISSUER's view (customer = counterparty buys from issuer; supplier = counterparty
  sells to issuer; parent = counterparty is issuer's parent; subsidiary / investee = counterparty is
  owned by issuer; affiliate). Other columns: counterparty_ticker, counterparty_company, period,
  share_text, amount_text, fact_id.
- `research-site/data/company-facts/{ticker}.json`: facts by id (to build source footnotes).
- Existing helpers to IMPORT (do not edit): `research-site/scripts/generic/build_company_pages_all.py`
  provides `fact_note(doc, fact)` (footnote text for a fact) and class `Notes` (`add(text)` returns
  a footnote marker like `[^n3]`).

## Build
`company_relations.py` must expose:
- `load_edges(path=...) -> dict[str, list[dict]]`: for every listed company, the edges where it is
  the issuer AND the edges where it is the counterparty. For the latter, convert the role to the
  page company's point of view: customer↔supplier swap; parent↔subsidiary swap; investee becomes
  `investor`; affiliate stays. Keep the original fact_id and the issuer (whose report states it).
  Deduplicate identical (other company, role, period, fact_id).
- `render_relations(ticker: str, edges: list[dict], notes, facts_dir=...) -> list[str]`: Markdown
  lines for a section `## 與其他上市櫃公司的往來關係 {.unnumbered}` with one intro sentence
  (「本節只列年報明載、且經逐筆審查的上市櫃公司之間關係；不代表完整供應鏈。」), then a table:
  對象（link `../companies/{ticker}.qmd`，顯示「代號 簡稱」）| 關係（中文：客戶、供應商、母公司、
  子公司、被投資公司、投資方、關係企業）| 期間 | 占比／金額 | 資料來源（the issuer's name + a
  footnote via `notes.add(fact_note(doc, fact))` for the fact_id). Order: customers, suppliers,
  ownership, affiliates; within each by period desc. Return [] when there are no edges.
  Escape `|` in cells.

## Tests (`python -m pytest`)
Role inversion, dedup, empty case, table row count, footnote added per row, link format.

## Acceptance
Run the tests; they pass. Final message (Traditional Chinese): API summary and counts (companies
with ≥1 relation, total rows).
