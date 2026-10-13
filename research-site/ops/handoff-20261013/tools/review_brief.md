# Semantic fact review (strict)

Repo root: C:\Users\Neo Pegasus\Documents\ChatGPT\078-kaori sample\artifacts\stock-coverage-audit-20261003\incoming\latest-audit\My-TW-Coverage (quote paths; Python `.venv/Scripts/python.exe -X utf8`).

You get a file with fact ids ({ticker}-AR-NN), one per line. Each fact is in research-site/data/company-facts/{ticker}.json (statement, period, page, excerpts, attribution). They passed a mechanical check (excerpts exist verbatim on the cited page; numbers in the statement appear in the excerpts — note: for flattened tables the number check is a substring match, so confirm table numbers yourself).

For each fact open the snapshot text at `source.text_path` (repo-relative, UTF-8, pages marked "[PDF PAGE n]") and read the cited page (and neighbours if a table spans pages). Verdict:
- ACCEPT: the statement says exactly what the report says — correct YEAR/column for every table number (visible from the table header), correct unit (仟元/千元/%/人), correct entity, correct attribution.
- REJECT if any of: wrong or unshown year/column mapping; a number from another row/cell (watch numbers run together in flattened tables); missing or wrong unit on a money amount; wrong entity; evaluative/self-promotional wording (成功、領先、知名、品質佳、具規模、步入常軌、已見成效…) not attributed as 公司年報自述; a list presented as complete when the report lists more; a customer/supplier rank not stated by the report; a code name turned into a real name; the report itself contradicts the number elsewhere; anything added that the report does not say.

Write one JSON per line to the output file named in your task: {"id":"…","verdict":"ACCEPT"|"REJECT","reason":"Traditional Chinese, one sentence; for REJECT state what is wrong and what the report says"}. Review every id. Do not edit repo files. No web. Final report in Traditional Chinese: counts and REJECT causes by category.
