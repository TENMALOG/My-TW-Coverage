# Audit v5 Status

Updated: 2026-10-05 13:04 UTC
Branch: `audit-v5`

## Semantic HIGH review

- HIGH issuers: **836**
- Raw HIGH signals: **1,410**
- Unique HIGH claims: **1,399**
- Author-reviewed: **9 / 1,399**
- Remaining author review: **1,390**
- Latest batch: **author-002** (1 claim)
- Independent reviews: **0**; author decisions are not final acceptance.

### Existing author decision counts

- `ACCEPTED`: **5**
- `PARTIALLY_SUPPORTED`: **3**
- `UNSUPPORTED`: **1**
- `PERIOD_UNRESOLVED`: **0**
- `SOURCE_UNAVAILABLE`: **0**
- `UNKNOWN_AFTER_RESEARCH`: **0**

## Latest claim batch

- Decision: `PARTIALLY_SUPPORTED`
- Claim: `2645:objective_ranking_or_market_share:acb07c2f05995949`
- Proposed wording is in `semantic/author-002.json`; no issuer report was changed.
- Next pending claim in priority order: `4546:objective_ranking_or_market_share:db06b1cb4d0d13e1` (長亨).

## Source access

The environment's unrestricted egress was retested. EGAT company pages, the TPEx site, MOEA, and AIDC responded with HTTP 200. The TWSE home page returned HTTP 503. MOPS returned HTTP 200 but its body was a security-denial page, so no MOPS filing content was inspected. The TWSE company-directory OpenAPI returned official data, though the download was slow.
