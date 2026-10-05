# Audit v5 Status

Updated: 2026-10-05 13:43 UTC
Branch: `audit-v5`

## Semantic HIGH review

- HIGH issuers: **836**
- Raw HIGH signals: **1,410**
- Unique HIGH claims: **1,399**
- Author-reviewed: **15 / 1,399**
- Remaining author review: **1,384**
- Latest batch: **author-007** (1 claim)
- Independent reviews: **0**; author decisions are not final acceptance.

### Existing author decision counts

- `ACCEPTED`: **5**
- `PARTIALLY_SUPPORTED`: **7**
- `UNSUPPORTED`: **1**
- `PERIOD_UNRESOLVED`: **0**
- `SOURCE_UNAVAILABLE`: **2**
- `UNKNOWN_AFTER_RESEARCH`: **0**

## Latest claim batch

- Decision: `PARTIALLY_SUPPORTED`
- `1712:objective_ranking_or_market_share:ababe1bd116826cb` — `SOURCE_UNAVAILABLE`; issuer site returned HTTP 503 and MOPS produced no viewable filing for the attempted years.
- `1722:objective_ranking_or_market_share:82710f0ae62b4476` — `PARTIALLY_SUPPORTED`; annual report supports largest domestic fertilizer producer/supplier and shareholder records support MOA 24.07%, but the inspected report does not state 70% market share.
- `1722:objective_ranking_or_market_share:991de260b51083b7` — `PARTIALLY_SUPPORTED`; official sources support about 170 hectares of land and C2/C3 project existence, not the claimed city ranking or project amounts.
- `1722:objective_ranking_or_market_share:584c29afa2ffa73c` — `PARTIALLY_SUPPORTED`; official sources support the wholly owned Taiwan Ocean Deep Water subsidiary and Hualien production facilities, but not the Asia-largest ranking.
- `1722:objective_ranking_or_market_share:7cd11cc6ee9fc2c7` — `SOURCE_UNAVAILABLE`; OCP official pages and the attempted USGS report returned HTTP 403, so no company-level ranking evidence was inspectable.
- Proposed wording from partial claims is recorded in their author ledgers; no issuer report was changed.
- Next pending claim in priority order: `1722:objective_ranking_or_market_share:fd708de33a7d0e86` (台肥).

## Source access

The saved environment draft has `network_policy.type: unrestricted`; no configuration change was needed. Current-instance checks: Python 3.12 dependencies imported successfully, `git ls-remote origin HEAD` succeeded, and 長亨, TPEx and 台肥 official pages returned HTTP 200. 台肥's annual report, real-estate, subsidiary and Hualien deep-water park pages were inspectable. 興農's issuer site returned HTTP 503; OCP official pages and the attempted USGS phosphate report returned HTTP 403. MOPS' annual-report form loaded but the attempted 1712/ROC 113–114 query returned no viewable filing. A MOEA request timed out on a current retry. Earlier checks found the TWSE home page returned HTTP 503 and MOPS' main host returned a security-denial route; no claim used search-result snippets as evidence.
