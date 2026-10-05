# Financial Phase 1 Report

Status: **MAPPING + EXCEPTION RESOLUTION COMPLETE**

Date: 2026-10-05  
Corpus: 1,733 issuer reports  
Official current-period matched issuers: 1,584

## Scope

Phase 1 covers current-period general-industry income-statement concepts only:

- Revenue
- Gross Profit
- Operating Income
- Net Income

It does not yet close historical periods, CAPEX/cash-flow definitions, specialized banking/insurance/capital-markets schemas, or valuation methodology.

## Corpus-level accounting mapping

The following mappings are approved:

| Repository field | Canonical official concept |
|---|---|
| Revenue | MOPS/TWSE 營業收入 |
| Gross Profit | MOPS/TWSE 營業毛利（毛損） |
| Operating Income | MOPS 營業利益（損失） / Mopsfin OperatingIncome |
| Net Income | MOPS 母公司業主（淨利∕損） / TWSE 歸屬母公司業主淨利 |

Mopsfin metric-series values are single-quarter values. TWSE/TPEx OpenAPI income-statement values are year-to-date for Q1-Q3. Comparisons must normalize these period bases before evaluation.

## Former 1,029 METHOD_UNRESOLVED items

The 1,029 population was mostly one global mapping issue, not 1,029 separate issuer investigations.

After approving the mapping:

- 1,019 legacy Yahoo/yfinance Operating Income mismatches -> `SOURCE_DEFINITION_DIFFERENCE`
- 10 specialized-financial-schema items -> remain `METHOD_UNRESOLVED`

This closes the general-industry Operating Income accounting-definition question at corpus level.

## 26 true current-period differences

The remaining non-Operating-Income differences were:

- Revenue: 5
- Gross Profit: 13
- Net Income: 8
- Total: 26

They affected 20 issuer reports.

Each was checked against both:

1. TWSE/TPEx official OpenAPI current-period data; and
2. MOPSFIN official income-statement pages for 2026Q1 and 2026Q2.

Result:

- `REPO_WRONG_CONFIRMED_OFFICIAL`: 26
- `SOURCE_SCOPE_DIFFERENCE`: 0
- `UNKNOWN`: 0

All 26 were repaired in the repository. Q1 and Q2 single-quarter values were reconstructed from official Q1 and Q2 YTD statement data where needed, and dependent margins were recalculated.

## Post-repair official check

After the 26 repairs:

- AUTO_VERIFIED: 5,134
- FINANCIAL_DIFFERENCE: **0**
- SOURCE_DEFINITION_DIFFERENCE: 1,019
- METHOD_UNRESOLVED: 10
- REPO_VALUE_UNAVAILABLE: 44

The 1,019 SOURCE_DEFINITION_DIFFERENCE items are known legacy-source differences, not unresolved accounting mappings and not candidates for 1,019 independent semantic investigations.

## Remaining financial work outside Phase 1

- specialized financial-sector schemas;
- 44 current-period repository values unavailable for deterministic comparison;
- 129 official Net Income values absent in the general OpenAPI feed;
- historical MOPS/XBRL verification;
- cash-flow/CAPEX definitions;
- valuation reproducibility.

These are separate later phases and do not reopen the completed general-industry current-period mapping or the 26 resolved exceptions.


## Final closure

The two residual Phase 1 categories have now been closed:

- `SOURCE_DEFINITION_DIFFERENCE`: 38 -> **0**
- `REPO_VALUE_UNAVAILABLE`: 44 -> **0**

For the 38 legacy Operating Income residuals, the repository now preserves Q1 and derives Q2 single-quarter Operating Income from the approved official H1/YTD MOPS value.

For 33 of the 44 missing-value items, Q1/Q2 values were reconstructed from official MOPS Q1 plus official H1/YTD evidence or from an existing quarter plus the official H1/YTD total.

The final 11 items belonged to 3659 百辰, 4546 長亨 and 6618 永虹先進. These are handled as 2026H1 semiannual/YTD issuers rather than inventing an unavailable Q1/Q2 split. Their 2026-06-30 cells are stored and checked directly as official H1/YTD values.

Final deterministic current-period result:

- comparison cells: **6,207**
- AUTO_VERIFIED: **6,207**
- FINANCIAL_DIFFERENCE: **0**
- METHOD_UNRESOLVED: **0**
- SOURCE_DEFINITION_DIFFERENCE: **0**
- REPO_VALUE_UNAVAILABLE: **0**

Official Net Income is absent from the general current-period feed for 129 matched issuers; those cells are outside the 6,207 comparable-cell denominator and are not falsely counted as verified.
