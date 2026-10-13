# Task for Codex: extract verified facts from Taiwan annual reports (READ-ONLY run)

You work in the repo root (current directory). You may read files and run read-only Python
(`.venv/Scripts/python.exe -X utf8 -c "..."`). You CANNOT write files. Your deliverable is your
FINAL MESSAGE, which must be ONE JSON object and nothing else (no prose, no code fences):

    {"<ticker>": <company-facts document>, "<ticker>": ..., "_notes": "<Traditional Chinese notes>"}

Each company-facts document must validate against `research-site/schemas/company-facts.schema.json`.

## Steps
1. Read `research-site/prompts/extract-company-facts.md` and
   `research-site/schemas/company-facts.schema.json`; follow every rule.
2. Read the two rule files that sit next to this task file: `extract_full_brief.md` (ignore its
   instructions about writing files and helper folders: you output JSON instead) and
   `extract_rules_v2.md`.
3. For each ticker in the batch: read `research-site/data/annual-slices/{ticker}.json` only to copy
   `legal_name` and the five `source` fields (citation_url, fy, filename, text_sha256, text_path)
   unchanged. Then read the FULL report text at `text_path` (pages marked `[PDF PAGE n]`) and
   extract up to 25 facts, ids `{ticker}-AR-01`, `-02`, ... `company` = the short name given below.
4. Self-check with Python before answering: each excerpt is an exact substring of the report text
   (original characters, punctuation and whitespace; never strip spaces, never NFKC-normalize;
   copy excerpts programmatically from the text), the first excerpt is on `page`, the others on
   `page` or `page+1`, every excerpt is at least 4 characters, every number in the statement
   appears in an excerpt.

## Hard rules (in addition to the rule files)
- Never add a rank (第N、列於表第N) the report's text does not state.
- Never output names of individual persons, even masked ones.
- Percentages must name their denominator. A revenue-mix / sales-region percentage with no year
  shown must be skipped.
- Statements in professional Traditional Chinese. No web search, no prior knowledge.
- Ticker identity: the filename/short name below is ground truth; if the report is for another
  company, skip that ticker and say so in `_notes`.

## Depth requirement (important)
Aim for 15–25 facts per company — a thin answer is a failed answer. Cover every item the report
supports: business scope and main products; revenue mix by product/segment with year; sales by
region with year; market share / market position (with attribution and denominator); main raw
materials and their supply; each named or code-named customer and supplier ≥10% with year,
amount, unit and share; employee counts with year; R&D expense and R&D staff; short- and
long-term business plans (as plans); establishment date, headquarters and group structure if
stated. One fact per table row/item. Work through the 營運概況 chapter page by page.
