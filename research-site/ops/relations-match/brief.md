# Brief: match named counterparties to listed companies (review-grade)

Repo root: C:\Users\Neo Pegasus\Documents\ChatGPT\078-kaori sample\artifacts\stock-coverage-audit-20261003\incoming\latest-audit\My-TW-Coverage

Input: a JSON list of relations whose counterparty is a NAME that exact matching could not resolve.
Each item: relation_id, ticker/company (the issuer whose annual report states it), role (issuer's
view: customer, supplier, parent, subsidiary, investee, affiliate), counterparty (text taken from
the statement), fact_id, statement (the verified fact sentence).

Reference list of listed companies: `research-site/catalog/release-scope-companies.csv` (ticker,
company short name) and the `legal_name` in `research-site/data/company-facts/{ticker}.json`
(you may grep these files). No web, no prior knowledge.

For each item output one JSON line:
`{"relation_id", "fact_id", "counterparty", "verdict", "counterparty_ticker", "role", "reason"}`
- `MATCH` — the statement clearly names exactly that listed company (legal-name variants such as
  臺/台, 股份有限公司 / (股)公司 omitted, or the catalog short name used for that company in this
  context). counterparty_ticker = its ticker; role = correct role from the ISSUER's view (fix it if
  the input role is wrong). The counterparty must not be the issuer itself.
- `NOT_LISTED` — a real organisation, but not one of our listed companies (foreign firms, private
  firms, government bodies, subsidiaries/branches/overseas entities of a listed company such as
  「台塑河靜」「台灣三星」— these are NOT the listed parent).
- `BAD_NAME` — the text is not an organisation name (generic word, product, region, truncated
  fragment, code name, group name like 「XX集團」).
When in doubt between MATCH and anything else, do not MATCH.

Write JSON Lines to the given output file, one per input item in the same order. Helper files only
with the given prefix in research-site/ops/relations-match/. Do not modify other files. Reply in
Traditional Chinese with counts per verdict.
