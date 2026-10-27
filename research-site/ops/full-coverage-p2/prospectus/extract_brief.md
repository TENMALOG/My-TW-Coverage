# Task: extract verified facts from a Taiwan PROSPECTUS (公開說明書) — prospectus rules v2

You work in the repo root (current directory). You may read files and run read-only Python
(`.venv/Scripts/python.exe -X utf8 -c "..."`). You CANNOT write files unless your task says so.
If you cannot write files, your deliverable is your FINAL MESSAGE: ONE JSON object and nothing else
(no prose, no code fences):

    {"<ticker>": <company-facts document>, "<ticker>": ..., "_notes": "<Traditional Chinese notes>"}

## Read first and follow every rule
1. `research-site/ops/full-coverage-p2/prospectus/RULES-v2.md` (this route's rules).
2. `research-site/schemas/company-facts-prospectus.schema.json` — every document must validate against it.
3. `research-site/prompts/extract-company-facts.md`, `research-site/ops/handoff-20261013/tools/extract_rules_v2.md`
   and `research-site/ops/handoff-20261013/tools/review_rules_v4.md` (reviewers use v4 plus
   `prospectus/review_addendum.md`). Wherever these say 年報 / annual report, read 公開說明書 / prospectus.

## Steps per ticker
1. Read `research-site/ops/full-coverage-p2/prospectus/sources/{ticker}.json` only to copy `legal_name` and the seven
   `source` fields unchanged.
2. Read the FULL prospectus text at `source.text_path` (pages marked `[PDF PAGE n]`). Work through the
   公司概況 and 營運概況 chapters page by page.
3. Write 15–25 facts, ids `{ticker}-PS-01`, `-02`, ...; `company` = the short name given in the task.
   attribution: 公司公開說明書揭露 / 公司公開說明書自述（未經獨立驗證的排名或評價） / 公司公開說明書引述第三方資料.
4. NEVER use: securities underwriter (承銷商/推薦證券商) evaluation opinions or 總評, lawyer or CPA opinions,
   financial forecasts (財務預測), offering / use-of-proceeds projections, third-party opinions in 特別記載事項.
   If you cannot tell whether a passage is the company's own statement or the underwriter's evaluation, skip it.
5. Every table number needs its year/period from the table header in `period` and in the statement.
   Prospectuses mix 113年度, 114年度 and 115年第一季 — never mix columns. Skip numbers whose period is not shown.
   Purely numeric ROC dates (115.03.31, 114/12) are skipped, never rewritten.
6. Self-check with Python before answering: each excerpt is an exact substring of the text (copy
   programmatically; never strip spaces or NFKC-normalize); the first excerpt is on `page`, the others on
   `page` or `page+1`; every excerpt ≥ 4 characters; every number in the statement appears in an excerpt.

## Hard rules
- Money needs currency and unit; keep scope limits; name related parties; a registered business-scope list
  is not the main products; no 占合計 without a total row; skip figures the prospectus contradicts elsewhere;
  skip names with suspicious glyphs; never turn a code name (甲公司、A客戶) into a real name; never add a rank.
- A region row nested under 外銷 (亞洲、歐洲、其他地區…) must say 外銷 in the statement; a parenthetical scope note
  must name the right table (研究發展人員表 is not 員工人數表). Both were frequent reviewer rejects/borderlines.
- Never output names of individual persons.
- Professional Traditional Chinese; no web search, no prior knowledge.
- Identity: the ticker and short name in the task are ground truth; if the prospectus is for another
  company, skip it and say so in `_notes`.
- Do not write the `verification` field.
