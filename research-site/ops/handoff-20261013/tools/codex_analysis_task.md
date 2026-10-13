# Task for Codex: draft the analysis section of one industry chapter (READ-ONLY run)

You get one JSON file with every verified annual-report fact for the listed companies of one
industry (fields: id, field, statement, period, attribution; plus company names and report year).
These facts are the ONLY allowed source. No web, no prior knowledge, no outside numbers, no
general industry knowledge, no forecasts of your own. You cannot write files: your FINAL MESSAGE is
the chapter section itself (Quarto Markdown body, Traditional Chinese), nothing else.

## Output format
Start with `## 產業分析 {.unnumbered}` and then these subsections (skip one only if no fact supports
it; never write filler):
1. `### 業務型態與產品` — what the companies in this industry actually do, grouped by business type.
2. `### 營收結構與市場分布` — revenue mix and sales regions / export share, with years.
3. `### 供應鏈：原料、供應商與客戶` — main raw materials and their sources, named or code-named
   suppliers/customers ≥10% with shares and years, customer concentration.
4. `### 市場地位` — market shares and positions, always with attribution (公司自述 vs 第三方).
5. `### 研發與人力` — R&D spending/staff and headcount with years and scope notes.
6. `### 發展計畫` — the companies' own stated plans, written as plans.
Length: about 150 Chinese characters per company in the industry, minimum 400, maximum 3,000.
For industries with many companies, describe groups and the most informative examples; you do not
have to mention every company.

## Citation rule (strict)
Every sentence must end with one or more markers 〔ID〕 using the fact ids it relies on, e.g.
`……占全年度銷貨淨額13.87%。〔2059-AR-11〕`. A sentence may only state what its cited facts say.
- Numbers, years, units, denominators and periods must be copied from the cited facts.
- Always name the company with its short name and ticker the first time, e.g. 川湖（2059）.
- Comparisons or aggregates ("三家公司均…", "比重最高者為…") are allowed only if every company
  involved is named and cited in that sentence, and the comparison uses the same period and unit.
- Self-descriptions (attribution 公司年報自述) must be written as 「（公司）於年報自述……」.
- Keep anonymous codes (甲客戶、A公司…) exactly; never guess a real name; never add ranks.
- Never mention individual persons. No wikilinks, no bold inside sentences, no tables.
- Different report years (e.g. FY2024 vs FY2025) must be stated explicitly when compared.
