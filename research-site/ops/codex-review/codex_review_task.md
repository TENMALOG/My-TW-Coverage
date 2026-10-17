# Task for Codex: second-opinion semantic review of verified annual-report facts (READ-ONLY)

Repo root = current directory. You may read files and run read-only Python
(`.venv/Scripts/python.exe -X utf8 -c "..."`). You cannot write files. Your FINAL MESSAGE must be
JSON Lines only — one line per fact id in your id file, same order, nothing else:

    {"id": "2059-AR-11", "verdict": "ACCEPT", "reason": "<short Traditional Chinese reason>"}
    {"id": "2059-AR-12", "verdict": "REJECT", "reason": "<what exactly is wrong>"}

## What to do
1. Read the review rules: `research-site/ops/handoff-20261013/tools/review_brief.md` and
   `research-site/ops/handoff-20261013/tools/review_rules_v3.md` (ignore their instructions about
   output files and helper files; you return JSON Lines instead).
2. For each id (format `{ticker}-AR-NN`): open `research-site/data/company-facts/{ticker}.json`, find
   the fact, open the report text at `source.text_path`, read the cited page (and page+1), and judge
   the MEANING: the statement must say only what the report says on that page — correct entity,
   number, year/column, unit, denominator, scope (合併/個體, 範圍未載明), attribution (公司自述 vs
   第三方), no added ranks/evaluations/causality, codes not turned into names, no person names,
   no two conflicting figures for the same item in the report left unmentioned.
   A mechanical check already confirmed that excerpts exist on the page and digits appear in them.
3. ACCEPT only if you checked the page. When in doubt, REJECT with the precise reason.
No web, no prior knowledge.
