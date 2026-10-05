# Audit v5 Status

Updated: 2026-10-05 12:42 UTC  
Branch: `audit-v5`

## Semantic HIGH review

- HIGH issuers: **836**
- Raw HIGH signals: **1,410**
- Unique HIGH claims: **1,399**
- Author-reviewed: **8 / 1,399**
- Remaining author review: **1,391**
- New claim reviews in this execution: **0**
- Independent reviews: **0**; author decisions are not final acceptance.

### Existing author decision counts

- `ACCEPTED`: **5**
- `PARTIALLY_SUPPORTED`: **2**
- `UNSUPPORTED`: **1**
- `PERIOD_UNRESOLVED`: **0**
- `SOURCE_UNAVAILABLE`: **0**
- `UNKNOWN_AFTER_RESEARCH`: **0**

## Current blocker

The first claim-level research attempt could not proceed because the restricted egress proxy returned HTTP CONNECT 403 for official-source hosts tested: `www.aidc.com.tw`, `www.twse.com.tw`, `www.moea.gov.tw`, and `www.mops.twse.com.tw`. No live web-search tool is available in this environment. These failed connectivity probes are not claim evidence, so no claim received a decision and no `SOURCE_UNAVAILABLE` result was recorded.

Next pending claim in priority order: `2645:objective_ranking_or_market_share:acb07c2f05995949` (長榮航太; normalized claim hash `acb07c2f05995949a72a6d0c190e016489fc3dc71f58f1f9990154e19b09035c`).

Resume after a usable route to inspect official exchange, government, and issuer sources is available. Search-result snippets alone cannot close claims.
