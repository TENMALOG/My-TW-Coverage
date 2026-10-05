# Audit v5 Status

Updated: 2026-10-07 16:04 UTC
Branch: `audit-v5`

## Semantic HIGH review

- HIGH issuers: **836**
- Raw HIGH signals: **1,410**
- Unique HIGH claims: **1,399**
- Author-reviewed: **358 / 1,399**
- Remaining author review: **1,041**
- Latest batch: **author-064** (6 claims)
- Independent reviews: **0**; author decisions are not final acceptance.

### Existing author decision counts

- `ACCEPTED`: **64**
- `PARTIALLY_SUPPORTED`: **225**
- `UNSUPPORTED`: **1**
- `PERIOD_UNRESOLVED`: **0**
- `SOURCE_UNAVAILABLE`: **3**
- `UNKNOWN_AFTER_RESEARCH`: **65**

## Latest claim batch

- `3441:objective_ranking_or_market_share:8b98c062556b5eb7` — `UNKNOWN_AFTER_RESEARCH`; 聯一光官方109與107年度年報端點均以「連接意外關閉」失敗，未取得可檢視文件。
- `3455:objective_ranking_or_market_share:9dab2c22ab03c4f4` — `PARTIALLY_SUPPORTED`; 由田2025簡報「檢測」82次、「PCB」9次、「LCD」5次；惟市占敘述為泛用語，未載數字或排名。
- `3455:objective_ranking_or_market_share:7453775b6f91a65d` — `ACCEPTED`; 同簡報明載「**IC 載板 AVI 設備，連續（年數未擷取）年佔有率全球第一**」，並列先進封裝多面檢測設備等產品（半導體23次、封裝10次）。
- `3645:objective_ranking_or_market_share:b5c3e6a0efaa2e89` — `PARTIALLY_SUPPORTED`; 達邁109年報載其為「**台灣第一家**投入生產聚醯亞胺薄膜的廠商」及「全球生產PI薄膜**領導廠商之一**」；惟「台灣最大」與「前四」皆0次。
- `3653:objective_ranking_or_market_share:32b1017f613092df`、`be2f7c2dfae707bf` — `PARTIALLY_SUPPORTED` ×2; 健策官方文件載均熱片產品說明、市場狀況與「伺服器ILM扣件產品說明」；惟「市佔」「台灣最大」「Vapor」皆0次。
- 證據、期間、查閱日期與摘記記錄於 `semantic/author-064.json`（6 筆）。未修改發行人報告。
- Next pending claim by priority: `3481:objective_ranking_or_market_share:44f9e638883c3468` (群創).

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
