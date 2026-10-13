# Annual-report fact extraction from the FULL report (new companies)

Repo root: C:\Users\Neo Pegasus\Documents\ChatGPT\078-kaori sample\artifacts\stock-coverage-audit-20261003\incoming\latest-audit\My-TW-Coverage (quote paths; Python `.venv/Scripts/python.exe -X utf8`). Use only your own helper folder `<scratchpad>/work-<BATCH>/` (<scratchpad> = the folder of this brief).

1. Read `research-site/prompts/extract-company-facts.md` and `research-site/schemas/company-facts.schema.json` and follow every rule (verbatim excerpts, page, numbers, units, years visible in excerpts with the table header as its own excerpt, scope/denominator for shares and market sizes, self-description vs third-party attribution, anonymous code names, tense of plans, skip anything the report contradicts elsewhere).
2. For each ticker: read `research-site/data/annual-slices/{ticker}.json` only to copy `legal_name` and the five `source` fields (citation_url, fy, filename, text_sha256, text_path) unchanged. If the slice is `garbled`, skip the ticker. Then read the FULL report text at `text_path` (pages marked "[PDF PAGE n]"): 營運概況 (業務內容, 營業比重, 主要商品, 產業概況, 技術及研發, 長短期業務發展計畫, 市場分析, 銷售地區, 市場占有率, 主要原料之供應狀況, 最近二年度占進(銷)貨百分之十以上客戶/供應商, 生產量值, 銷售量值, 從業員工) and 公司簡介/沿革 if present.
3. Write `research-site/data/company-facts/{ticker}.json` with up to 25 facts, ids `{ticker}-AR-01`, `-02`, ...; `company` = the short name given in your task.
4. Self-check before writing with a small script: excerpt found in the full text and on `page` (or continuing onto page+1), every number in the statement present in an excerpt. Do not run verify_extraction.py; do not edit other files; no web; no prior knowledge.
5. Final report in Traditional Chinese: `ticker 公司 facts數` per company (or `跳過（原因）`), plus anything notable.
