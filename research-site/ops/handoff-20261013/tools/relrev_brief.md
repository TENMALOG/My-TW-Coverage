# Review brief: listed-company relation edges

Each line of your input JSONL is one relation edge derived from an annual-report fact:
`ticker/company` (the issuer whose annual report it is), `role` (from the issuer's point of view:
customer, supplier, parent, subsidiary, affiliate, investee), `counterparty` (text taken from the
statement), `counterparty_ticker/company` (the listed company it was matched to), `match_rule`,
and `statement` (the verified fact sentence). Use ONLY the statement and the repo catalog
`research-site/catalog/release-scope-companies.csv` (plus `legal_name` in
`research-site/data/company-facts/{ticker}.json`). No web, no prior knowledge.

For every edge decide:
- `ACCEPT` — the statement really names this counterparty, the role is right, and the matched
  listed company is unambiguously the same entity (exact legal name, or a short name that in this
  context clearly refers to that listed company, e.g. 中鋼 → 中國鋼鐵).
- `FIX_ROLE|<correct role>` — counterparty and match right, role wrong.
- `REJECT|<reason>` — wrong counterparty text, a code name, the issuer itself, a non-company,
  a subsidiary/foreign entity with a similar name but not the listed company (e.g. 鴻海 vs
  鴻海精密工業(越南)), or the match is ambiguous.

Output one JSON per line to the output file you are given:
`{"relation_id": ..., "verdict": "ACCEPT" | "FIX_ROLE|supplier" | "REJECT|reason"}` — one line
per input line, same order. Prefix helper files with the given prefix. Reply in Traditional
Chinese with counts per verdict and the reject reasons.
