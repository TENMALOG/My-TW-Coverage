# Review brief: industry analysis drafts (sentence by sentence)

Repo root: C:\Users\Neo Pegasus\Documents\ChatGPT\078-kaori sample\artifacts\stock-coverage-audit-20261003\incoming\latest-audit\My-TW-Coverage

For each slug in your list:
- Draft: `research-site/data/industry-analysis/{slug}.md`. Every sentence ends with markers 〔ID〕.
- Facts: `<scratchpad>/ind_facts/{slug}.json` (the only allowed evidence; look up each cited id).
  A mechanical check already confirmed that cited ids exist and that every digit appears in the
  cited facts. Your job is the MEANING.

For every sentence check, using only the cited facts:
1. Everything the sentence says is stated by the cited facts (entity, number, year/period, unit,
   denominator, scope such as 合併/個體, attribution). No added interpretation, causality,
   trend, ranking, "最高/最大/主要/集中/顯示" unless a cited fact says it, and no comparison across
   different periods or units without saying so.
2. A company-self-description is presented as the company's own claim (「於年報自述」).
3. Anonymous codes are kept; no person names; no facts about a company that cites another
   company's fact id.
4. Aggregates ("三家公司均…") name and cite every company involved.

Write ONLY the problem sentences to your output JSONL, one line each:
`{"slug": "...", "sentence": "<the first 30 characters of the sentence exactly as in the draft>", "problem": "<short reason>", "fix": "<a corrected sentence that keeps the same markers and uses only the cited facts, or \"DELETE\">"}`
If a draft has no problems, write `{"slug": "...", "sentence": "", "problem": "NONE", "fix": ""}`.
Do not edit the draft files. Prefix helper files with the given prefix. Reply in Traditional
Chinese with the number of problem sentences per slug.
