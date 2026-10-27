# Extra review rules (v4, 2026-10-24) — apply on top of review_brief.md

v4 = v3 unchanged, plus the lessons of the P1 full-coverage pilot (371 facts, 16 companies). v3 stays
as the record for earlier reviews; use v4 for all new reviews.

## Carried over from v3
- A fact may cite a table header on `page` and rows continuing on `page`+1: ACCEPT only if the rows belong to that same table and year columns. The first excerpt must be on `page`; later excerpts may start on `page`+1.
- Year labels printed with doubled characters, spaced digits, Western years or Chinese numerals count as visible. A year-specific number (revenue mix, sales region, customer/supplier share, R&D, headcount…) whose year is not visible in the excerpts → REJECT.
- A market share / rank stated by the company without a year counts as as-of-the-report self-description: ACCEPT if attributed as 公司年報自述 and the statement does not invent a year. A share published by a third party for a specific year needs that year.
- `period` 「截至N年度年報刊印日」 means "as stated in that annual report"; ACCEPT it only for non-year-specific content.
- A customer/supplier fact whose only content is the 「其他」 row → REJECT.
- Employee counts must not imply a scope the table does not state.
- A market share the company computed itself must be attributed as 公司年報自述; only a share published by the named institution itself may be 引述第三方資料.
- Evaluative words (成功、領先、高品質、知名、最佳、龍頭…) must be attributed as 公司年報自述.
- A rank such as 「第一大」 is allowed only if the report's text states it.
- Percentages must make their denominator clear.
- If the report gives two different figures for the same item, REJECT a statement using either without noting the conflict.

## New in v4 (each was a real miss in the pilot)
1. **Money without currency or unit → REJECT**, even when the statement says 「原文未載幣別」. An amount the reader cannot interpret is not publishable.
2. **The statement must not say more than its excerpts.** If the excerpt says 「研發藍圖已涵蓋」 the statement may not say 「產品涵蓋」; support found elsewhere in the report does not rescue the fact — REJECT.
3. **Scope must survive.** If the report limits a figure (one production line, one customer's orders, one region, a subsidiary), the statement must keep that limit (e.g. capacity of a contract filling line ≠ company capacity) — otherwise REJECT.
4. **Related parties must be named as such.** When the report marks a customer/supplier as 關係人／關係企業／母公司, the statement must say so — otherwise REJECT.
5. **Suspicious glyphs.** If the statement contains a character flagged by `scan_glyphs.py` (or one you recognise as a PDF text-layer error, e.g. 「強雊」 for 強韌, simplified 「孙」), check the page image context (English names, other mentions). If the true characters cannot be established from the report itself → REJECT; never correct a name from outside knowledge.
6. **Copying a registration list is not describing the business.** A 營業項目／營業範圍 list that does not match the report's own main products must not be presented as the company's products — REJECT unless the statement says it is the registered business scope list and does not imply it is the main business.
7. **A table total that does not exist cannot be a denominator.** 「占…合計」 requires a 合計 row (or the report's own stated total) — otherwise REJECT.
8. **Table title vs report text.** If a table title conflicts with the report's own text for the same period (e.g. 「四價」 title vs 2025 switch to trivalent), a statement repeating the title → REJECT.

## Reason quality (enforced)
- Every verdict needs a specific reason naming what was checked: the year column, the unit, the row, the page. Reasons such as 「年報原文與陳述一致」 alone are not acceptable; the batch is returned for re-review.

## Second review (new process)
- After the first reviewer, a second, independent reviewer re-checks: every REJECT/FIX, and a random 15 % of ACCEPTs (seeded, reproducible: `select_second_review.py`).
- Disagreements go to the general manager (Claude main session) for the final verdict, recorded in `final-adjudication.jsonl` with the reason.
- If the second reviewer overturns more than 5 % of the sampled ACCEPTs in a batch, the whole batch is re-reviewed.
