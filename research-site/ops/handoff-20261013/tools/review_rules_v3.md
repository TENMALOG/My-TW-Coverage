# Extra review rules (v3) — apply on top of review_brief.md

- A fact may cite a table header on `page` and rows continuing on `page`+1: ACCEPT only if the rows belong to that same table and year columns. The first excerpt must be on `page`; later excerpts may start on `page`+1.
- Year labels printed with doubled characters, spaced digits, Western years or Chinese numerals count as visible. A year-specific number (revenue mix, sales region, customer/supplier share, R&D, headcount…) whose year is not visible in the excerpts → REJECT.
- A market share / rank stated by the company without a year (e.g. 「目前市占約20%」) counts as as-of-the-report self-description: ACCEPT if attributed as 公司年報自述 and the statement does not invent a year. A share published by a third party for a specific year needs that year.
- `period` 「截至N年度年報刊印日」 means "as stated in that annual report"; ACCEPT it only for non-year-specific content (descriptions, cumulative/as-of figures, plans).
- A customer/supplier fact whose only content is the 「其他」 row → REJECT.
- Employee counts must not imply a scope the table does not state.
- A market share the company computed itself (even from official or third-party statistics) must be attributed as 公司年報自述; only a share published by the named institution itself may be 引述第三方資料.
- Evaluative words (成功、領先、高品質、知名、最佳、龍頭…) must be attributed as 公司年報自述.
- A rank such as 「第一大」 is allowed only if the report's text states it.
- Percentages must make their denominator clear (e.g. 占銷貨淨額、占銷售地區表合計).
- If the report gives two different figures for the same item, REJECT a statement using either without noting the conflict.
- Write a specific reason for every verdict (not one generic sentence).
