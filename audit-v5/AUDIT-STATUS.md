# Audit v5 Status

Updated: 2026-10-06 19:04 UTC
Branch: `audit-v5`

## Semantic HIGH review

- HIGH issuers: **836**
- Raw HIGH signals: **1,410**
- Unique HIGH claims: **1,399**
- Author-reviewed: **241 / 1,399**
- Remaining author review: **1,158**
- Latest batch: **author-043** (8 claims)
- Independent reviews: **0**; author decisions are not final acceptance.

### Existing author decision counts

- `ACCEPTED`: **53**
- `PARTIALLY_SUPPORTED`: **150**
- `UNSUPPORTED`: **1**
- `PERIOD_UNRESOLVED`: **0**
- `SOURCE_UNAVAILABLE`: **3**
- `UNKNOWN_AFTER_RESEARCH`: **34**

## Latest claim batch

- `2385:objective_ranking_or_market_share:22c3e7f8c90b61ca` — `PARTIALLY_SUPPORTED`; 群光2025年報載「自72年2月22日成立」（1983）、總部新北三重、第63/64頁「NB鍵盤、影像模組以及電源供應器產品都是全球市佔率第一」與「均居全球龍頭」；惟「連續多年」0次。
- `2385:objective_ranking_or_market_share:abe9e706555f9c9d`、`bdefdbbe34f7abee`、`57a3aa507e64e4f6` — `ACCEPTED` ×3; 同頁支持筆電鍵盤全球第一與影像模組全球市佔第一，第56頁產品線含桌機鍵盤、滑鼠、數位攝影機與相機模組，第62頁載IPcam應用、文中「行車紀錄」6次與LED ADB車燈開發。
- `2387:objective_ranking_or_market_share:fc8df196f3e558dc`、`e5e02db27813e6d2` — `ACCEPTED` ×2; 精元2024永續報告第27頁載「創立於1975年」、「目前為世界第一大筆記型電腦鍵盤製造商」，第30頁沿革載台中市電腦商業同業公會參與紀錄。
- `2395:objective_ranking_or_market_share:46485c9c097dd36f`、`9566784397e27fb6` — `PARTIALLY_SUPPORTED` ×2; 研華113年報多處論述工業電腦（19次）與相關產品獲獎；惟「全球最大」出現0次。
- 證據、期間、查閱日期與摘記記錄於 `semantic/author-043.json`（8 筆）。未修改發行人報告。
- Next pending claim by priority: `3005:objective_ranking_or_market_share:a3b2b980edcf8e31` (神基).

## Source access

The saved environment draft has `network_policy.type: unrestricted`; no configuration change was needed. Current-instance checks: Python 3.12 dependencies imported successfully, `git ls-remote origin HEAD` succeeded, and 長亨, TPEx, 台肥 and 華航 official pages returned HTTP 200. 台肥's annual report and company pages were inspectable; 華航's history and SkyTeam-anniversary announcement were inspectable. 興農 and CPC issuer pages returned HTTP 503; OCP official pages and the attempted USGS phosphate report returned HTTP 403. CAA pages were reachable but did not provide the attempted CPC airport-fuel supplier roster. MOPS' annual-report form loaded but the attempted 1712/ROC 113–114 query returned no viewable filing. A MOEA request timed out on a current retry. Earlier checks found the TWSE home page returned HTTP 503; a current TWSE OpenAPI retry did not return within the command window. No claim used search-result snippets as evidence.


## Transient retrieval failure handling

- Policy and append-only local recheck queue added; no local worker is implemented or run.
- Durable queue: **15 URL/failure entries**, all `LOCAL_RECHECK_PENDING`; **HTTP 500: 8**, **HTTP 503: 7**. These span 3 claims: 4558 (10 URLs), 1712 (3), and 2610 (2). The entries preserve Cloud observations and are idempotent by claim ID, normalized claim hash, exact URL, and failure signature.
- Claim 4558 (`e9efcd84b9b3989d`) is now `PARTIALLY_SUPPORTED`: the inspected TPEx profile supports its 1989 establishment and aluminum-extrusion products; the “one of Taiwan’s largest” qualifier remains unsupported by the inspected evidence. The previous 1712 and 2610 author ledger decisions remain preserved unchanged; their `SOURCE_UNAVAILABLE` outcomes were recorded before this transient-failure policy and require a normal Codex Cloud semantic review if content later becomes inspectable. A home-network result alone cannot change those decisions.
- Relevant tests: `python -m unittest audit-v5/tests/test_semantic_local_recheck_queue.py` — 3 passed.
- No production files or author ledgers were changed.

## Semantic worker throughput

- Worker configuration: **author concurrency 4**, **reviewer concurrency 4**, default batch size **4**. The worker also accepts `SEMANTIC_AUTHOR_CONCURRENCY` / `SEMANTIC_REVIEWER_CONCURRENCY` and matching CLI flags.
- State, status, and batch JSON now use coordinator-only atomic replace writes. The GitHub Actions concurrency group continues to serialize separate workflow runs.
- Latest verification: **37/37 tests passed** across `audit-v5/tests`; Python syntax check passed. A bounded live API batch was not run because `OPENAI_API_KEY` is absent in this environment.
- Mocked 8-claim timing (50 ms per call): sequential baseline **0.802s**; author pool 4 + reviewer pool 4 **0.209s**; author/reviewer mean call times **0.051s / 0.050s**; errors **0**, rate limits **0**. This validates pool behavior only and does not predict API throughput.


### Latest author batch

- `4558:objective_ranking_or_market_share:e9efcd84b9b3989d` — `PARTIALLY_SUPPORTED`; a directly inspected TPEx company profile supports establishment on 1989-03-09 and aluminum-extrusion production, but supplies no evidence for the Taiwan-largest ranking. The issuer/MOPS transient failures were not treated as semantic evidence. Details: `semantic/author-012.json`.
- The 10 BaoWei URL failures remain `LOCAL_RECHECK_PENDING` for availability observation; the semantic review is no longer blocked because TPEx independently supports the historical/product portions.
