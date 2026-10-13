# Extra extraction rules (v2) — apply on top of extract_full_brief.md

- Keep anonymous code names exactly as printed; never guess real names; never add a rank (「第一大」) the text does not state.
- Every year must be visible in the excerpts: add the table header as its own excerpt. For descriptive facts with no year use period 「截至{ROC}年度年報刊印日」 (ROC = fy − 1911).
- A revenue-mix, sales-region, customer/supplier or headcount table with no year label is year-specific data without a year — skip it.
- If a table header is on one page and rows continue on the next, set `page` to the header page; the first excerpt must be on `page`.
- Employee counts: state the scope only if the table states it, otherwise add 「（員工人數表未載明為母公司或合併範圍）」.
- Never output a customer/supplier fact whose only content is the 「其他」 row.
- Lists must end with 「等」 unless the list is complete.
- Evaluative words (成功、領先、知名、高品質、最佳、龍頭…) only as 「公司於年報自述…」 with attribution 公司年報自述.
- A market share the company computed itself (even from official or third-party statistics) is 公司年報自述; name the source of the denominator. Only a share published by the named institution is 引述第三方資料.
- Percentages must name their denominator (e.g. 占銷貨淨額、占銷售地區表合計). 「營業比重」 is self-explanatory.
- Money amounts must carry the unit as printed; if the report omits the currency write 「（原文未載幣別）」.
- If the report gives two different figures for the same item, output neither.
- Never add a denominator, inference or interpretation the report does not state.
- If a table's numbers run together so that the split is ambiguous (e.g. 「968890」), skip it.
