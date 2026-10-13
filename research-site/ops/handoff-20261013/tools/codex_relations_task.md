# Task for Codex: build the company-relations layer (workspace-write)

Repo root = current directory. Python: `.venv/Scripts/python.exe -X utf8`. You may ONLY create/modify:
- `research-site/scripts/relations/` (new folder: your scripts and tests)
- `research-site/data/relations/` (new folder: your outputs)
Do not touch any other file. No web access, no prior knowledge about companies: everything must come
from the repo data. Do not commit.

## Inputs
- `research-site/data/company-facts/{ticker}.json` (1,733 files; schema in
  `research-site/schemas/company-facts.schema.json`). Each fact has `id`, `field`, `statement`,
  `period`, `page`, `excerpts`, `attribution`, `verification.status`.
- `research-site/data/company-facts/_semantic-review.jsonl`: one JSON per line with `id` and
  `verdict` (`ACCEPT…` or `REJECT…`); several lines may exist per id — the LAST line wins.
- `research-site/catalog/release-scope-companies.csv`: ticker, company (short name), industry_folder.
- Legal names: the `legal_name` of every company-facts file.

## Usable facts
Only facts with `verification.status == "PASS"` and whose last review verdict is not REJECT.
Relevant fields: `major_customers`, `major_suppliers`, `group_structure`.

## Step 1 — counterparties (`data/relations/counterparties.jsonl`)
For every usable relevant fact write one line:
`{"fact_id", "ticker", "field", "counterparty", "counterparty_kind", "role", "period", "share_text", "amount_text"}`
- `counterparty`: the counterparty name EXACTLY as it appears in the statement (substring of the
  statement). If the statement names several, write one line per counterparty.
- `counterparty_kind`: `named` (a real organisation name), `code` (anonymous code such as 甲客戶,
  A公司, Z35, 客戶628 — keep it but it must never be resolved to a real company), or `none` (the
  fact says there is no ≥10% customer/supplier, or names no counterparty) — for `none` set
  counterparty to "".
- `role`: from the issuer's point of view — `customer`, `supplier`, `parent`, `subsidiary`,
  `affiliate`, `investee` (for group_structure use what the statement says; if unclear use `affiliate`).
- `period`: copy the fact's period. `share_text` / `amount_text`: the percentage / amount with unit
  exactly as written in the statement, or "".
Do this by reading the statements yourself (you may write helper scripts for the regular patterns,
but check the output). Never invent a name; never turn a code into a name.

## Step 2 — resolver script `scripts/relations/build_relations.py`
Deterministic, re-runnable. Reads counterparties.jsonl, asserts each `counterparty` is a substring
of its fact statement and each fact_id is usable, then resolves `named` counterparties to listed
tickers in our catalog by exact match against (a) legal names, (b) legal names with 股份有限公司 /
(股)公司 / 有限公司 suffix variants removed, (c) catalog short names — only when the match is
unique and unambiguous. Do NOT use fuzzy matching. Output:
- `data/relations/relations.csv` with columns
  `relation_id,ticker,company,role,counterparty,counterparty_kind,counterparty_ticker,counterparty_company,period,share_text,amount_text,fact_id,match_rule`
- `data/relations/summary.json`: counts by role/kind, number resolved to listed tickers, number of
  edges where both ends are listed, top 30 most-connected listed companies.
- `data/relations/unresolved_named.csv`: named counterparties not resolved (for later review).

## Step 3 — tests `scripts/relations/test_relations.py` (pytest-style, runnable with python -m pytest)
Cover: suffix stripping, no fuzzy matches, codes never resolved, ambiguous short names left
unresolved, substring assertion, REJECT/FAIL facts excluded (use small inline fixtures).

## Acceptance
Run the script and the tests; both must pass. Final message (Traditional Chinese): what you built,
counts from summary.json, and any doubtful cases.
