# Adjudication brief: decide and fix flagged facts

Repo root: C:\Users\Neo Pegasus\Documents\ChatGPT\078-kaori sample\artifacts\stock-coverage-audit-20261003\incoming\latest-audit\My-TW-Coverage

Your input JSON (list) has items `{id, reviewer_reason, source}`. For each id (`{ticker}-AR-NN`) open
`research-site/data/company-facts/{ticker}.json`, read the fact (statement, period, page, excerpts,
attribution) and the report text at `source.text_path` on the cited page (and page+1). Rules:
`research-site/ops/handoff-20261013/tools/review_rules_v3.md`. No web, no prior knowledge.

Decide one action per id:
- `KEEP` — the reviewer was wrong; the statement is correct as written.
- `FIX` — give `new_statement`: a corrected Traditional Chinese sentence that says only what the
  report says. Typical fixes: name the denominator without adding new figures (占銷售地區表合計、
  占全年度銷貨淨額、占營業收入淨額、占該表合計); add 「（員工人數表未載明為母公司或合併範圍）」;
  add 「（原文未載幣別）」 or remove an invented currency; mark self-descriptions 「公司於年報自述…」;
  remove a rank that is only a table row number (「列於主要客戶表」 instead of 「排名第1」 —
  keep a rank only if the report's TEXT states it, e.g. 「第一大客戶」 written in a sentence or a
  table column literally titled 排名/名次); remove person names; add 「等」 to incomplete lists;
  narrow an over-broad scope. Every number in new_statement must appear in the fact's excerpts
  (you may also drop numbers). If the fix needs a number from a different row/column/page that is
  not in the excerpts, choose DROP instead. Set `new_attribution` only when attribution must change
  (allowed values: 公司年報揭露, 公司年報自述（未經獨立驗證的排名或評價）, 公司年報引述第三方資料).
- `DROP` — cannot be fixed from its excerpts (wrong column/year, report contradicts itself on the
  same item, year not shown for year-specific data, only the 「其他」 row, person-only counterparty).

Write your output file as JSON Lines, one per input id in the same order:
`{"id": ..., "action": "KEEP"|"FIX"|"DROP", "new_statement": "...", "new_attribution": "...", "reason": "<short Traditional Chinese>"}`
(new_statement / new_attribution only for FIX, may be omitted otherwise). Do not edit any repo
file. Helper files only with the given prefix next to your output. Reply in Traditional Chinese with
counts per action.
