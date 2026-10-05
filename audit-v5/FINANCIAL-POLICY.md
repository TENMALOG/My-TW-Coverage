# Financial Audit Policy

Version: `financial-2-current-approved`

## Principle

Do not spend model reasoning confirming arithmetic equality. Financial exact matches are deterministic; accounting-definition ambiguity is not.

## AUTO_VERIFIED prerequisites

A financial cell may be auto-verified only when all are established:

- issuer identity match
- reporting period match
- annual/quarterly context match
- consolidated/individual scope match
- currency match
- unit normalization match
- unambiguous account/tag mapping
- approved rounding/tolerance rule
- original and official values compare equal within policy

If any prerequisite is missing, do not auto-pass.

## Differences

A numeric mismatch becomes `NEEDS_MODEL_REVIEW` or a more specific unresolved state. The original and official value, exact source context and calculation must be retained.

## Global method questions

Questions such as which net-income concept to use, CAPEX definition, operating-income adjustments or FCF formula are corpus-level policy questions. They must be decided once and versioned here rather than re-litigated independently for every issuer.

Until approved, affected cells remain `METHOD_UNRESOLVED`.

## Approved current-period mappings

For general-industry issuers, the current-period canonical mappings are approved:

- Revenue -> MOPS/TWSE `營業收入`
- Gross Profit -> MOPS/TWSE `營業毛利（毛損）`
- Operating Income -> MOPS `營業利益（損失）` / Mopsfin `OperatingIncome`
- Net Income -> MOPS `母公司業主（淨利∕損）` / TWSE `淨利（淨損）歸屬於母公司業主`

Mopsfin metric-series values are single-quarter values. TWSE/TPEx OpenAPI income-statement values are year-to-date for Q1-Q3. The two forms must reconcile after summing the single-quarter series.

CAPEX and other cash-flow concepts remain outside this phase.


## Official cross-check phase 1

The GitHub-native v5 baseline uses the TWSE official OpenAPI current-period income-statement snapshot as an independent cross-check for general-industry issuers. When available, the public-company dataset is preferred; listed/OTC general-industry feeds are fallback sources.

Phase 1 validates only concepts that can be reproduced from the official snapshot and current repository tables:

- Revenue
- Gross Profit
- Operating Income
- Net Income

For Q1-Q3, official income-statement values are cumulative year-to-date. v5 therefore sums the repository's single-quarter values for the same year through the official quarter before comparison. For Q4, the annual table is used directly.

Official OpenAPI values are reported in thousand TWD and normalized to million TWD before comparison.

A mismatch is `FINANCIAL_DIFFERENCE`, not an automatic correction. Net-income differences may represent a scope/attribution definition difference and require method review.

Phase 1 does not claim official verification of Selling & Marketing, R&D, G&A, operating/investing/financing cash flow or CAPEX. Historical full-statement verification remains a later MOPS/XBRL phase.


### Current source precedence clarification

The listed-company `t187ap06_L_ci` and OTC `mopsfin_t187ap06_O_ci` feeds are the primary current-period market sources. The `t187ap06_X_ci` public-company feed is supplemental only because it is not the full listed+OTC universe.

For Net Income, v5 first attempts the official concept "淨利（淨損）歸屬於母公司業主" to better align with the repository/Yahoo common-stockholder convention; total-period profit/loss is retained only as a fallback. Any remaining attribution mismatch stays a method issue rather than being silently accepted.


### Difference triage

A current-period mismatch is not automatically a factual error.

- Revenue, Gross Profit and parent-attributable Net Income mismatches remain `FINANCIAL_DIFFERENCE` when the issuer uses the general-industry schema.
- Operating Income maps canonically to official `營業利益（損失）`; general-industry mismatches are factual differences rather than method gaps.
- Reports in banking, capital markets, credit services, financial conglomerates, insurance and related financial-service sectors use `METHOD_UNRESOLVED` under the general-industry checker until specialized schemas are implemented.

This prevents a broad accounting-definition mismatch from being misreported as hundreds of issuer-level factual errors.


## Operating Income legacy-source disposition

The corpus-level accounting mapping is now closed for general-industry current-period Operating Income:

Operating Income -> MOPS 營業利益（損失） / Mopsfin OperatingIncome

When the legacy repository value sourced from Yahoo/yfinance differs from this approved official concept, v5 records SOURCE_DEFINITION_DIFFERENCE with reason legacy-yfinance-operating-income-vs-canonical-mops.

This is not an issuer-by-issuer accounting-method ambiguity and must not consume semantic-review capacity. Specialized financial-sector schemas remain METHOD_UNRESOLVED until their own mappings are approved.
