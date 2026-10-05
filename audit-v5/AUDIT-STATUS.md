# Audit v5 Status

Updated: 2026-10-05 13:14 UTC
Branch: `audit-v5`

## Semantic HIGH review

- HIGH issuers: **836**
- Raw HIGH signals: **1,410**
- Unique HIGH claims: **1,399**
- Author-reviewed: **10 / 1,399**
- Remaining author review: **1,389**
- Latest batch: **author-003** (1 claim)
- Independent reviews: **0**; author decisions are not final acceptance.

### Existing author decision counts

- `ACCEPTED`: **5**
- `PARTIALLY_SUPPORTED`: **4**
- `UNSUPPORTED`: **1**
- `PERIOD_UNRESOLVED`: **0**
- `SOURCE_UNAVAILABLE`: **0**
- `UNKNOWN_AFTER_RESEARCH`: **0**

## Latest claim batch

- Decision: `PARTIALLY_SUPPORTED`
- Claim: `4546:objective_ranking_or_market_share:db06b1cb4d0d13e1`
- Decision: `PARTIALLY_SUPPORTED`; 長亨官網支持 100% 外銷與多項產品全球市占第一，但查閱頁未支持 Safran／GE Aerospace 為主要客戶。
- Proposed wording is in `semantic/author-003.json`; no issuer report was changed.
- Next pending claim in priority order: `1712:objective_ranking_or_market_share:ababe1bd116826cb` (興農).

## Source access

The saved environment draft has `network_policy.type: unrestricted`; no configuration change was needed. Current-instance checks: Python 3.12 dependencies imported successfully, `git ls-remote origin HEAD` succeeded, and the 長亨 issuer page and TPEx home page returned HTTP 200. The MOEA request timed out on this retest. Earlier checks found the TWSE home page returned HTTP 503 and MOPS returned a security-denial page despite HTTP 200; no MOPS filing content was inspected.
