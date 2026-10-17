# QA audit of facts accepted only by the Codex second-pass review

Repo root: the folder that contains `research-site/`. Use `.venv/Scripts/python.exe -X utf8` (read-only) to read files.

Input: one id file `research-site/ops/qa-audit3/ids_NN.txt` (one fact id per line). Each fact lives in
`research-site/data/company-facts/{ticker}.json` (ticker = part before `-AR-`), with `statement`, `field`,
`period`, `attribution`, `excerpts`, `page`, and the annual-report text path in the document meta. Open the
cited page (and the next page when a table continues) and check that the statement is exactly supported.

REJECT when any of these holds, otherwise ACCEPT:
- a number, year, unit, currency or column is wrong or taken from another row / year column;
- a percentage names no denominator (the report's own label 營業比重 / 營收比重 counts as named: share of
  operating revenue) or names a denominator different from the table's;
- a table row number or code (A客戶, 甲, 第1列) is presented as a rank or as a real name;
- the scope is changed: consolidated vs parent-only, a subsidiary's figure presented as the company's,
  an employee count implying a scope the table does not state, a partial sentence that narrows or widens
  the business scope;
- the statement adds an inference, ranking or evaluation the report does not make, or presents the
  company's self-assessment as fact (attribution must then be 公司年報自述（未經獨立驗證的排名或評價）);
- the fact names a natural person;
- a revenue-mix or sales-region figure carries no year.

Write `research-site/ops/qa-audit3/out_NN.jsonl`: one line per id, same order as the id file:

    {"id": "...", "verdict": "ACCEPT"|"REJECT", "reason": "..."}

`reason` is short Traditional Chinese; for REJECT say exactly what is wrong. Do not modify any other repo
file; helper scripts go in `research-site/ops/qa-audit3/` with prefix `qaNN_`.
