# Audit v5 Status

Updated: 2026-10-08 16:04 UTC
Branch: `audit-v5`

## Semantic HIGH review

- HIGH issuers: **836**
- Raw HIGH signals: **1,410**
- Unique HIGH claims: **1,399**
- Author-reviewed: **512 / 1,399**
- Remaining author review: **887**
- Latest batch: **author-088** (8 claims)
- Independent reviews: **0**; author decisions are not final acceptance.

### Existing author decision counts

- `ACCEPTED`: **71**
- `PARTIALLY_SUPPORTED`: **338**
- `UNSUPPORTED`: **1**
- `PERIOD_UNRESOLVED`: **0**
- `SOURCE_UNAVAILABLE`: **3**
- `UNKNOWN_AFTER_RESEARCH`: **99**

## Latest claim batch

- `6671:objective_ranking_or_market_share:1c6728d636eea59e` — `PARTIALLY_SUPPORTED`；三能年報載營運模式「係以**自有品牌**之銷售為（主）」（SANNENG 18次、烘焙353次、烤模10次）；惟「UNOPAN」0次，且「市佔」1次係「提升線上銷售**市佔率**」之**營運目標**。
- `8929:objective_ranking_or_market_share:9995e14a016110bb` — `PARTIALLY_SUPPORTED`；富堡文件載成人紙尿褲25次、看護墊4次、復健褲2次、安安1次；惟「市佔」「Ancare」皆0次。
- `2373:objective_ranking_or_market_share:3dc2f728f9ba57e4` — `UNKNOWN_AFTER_RESEARCH`；震旦行官方年報、106.pdf 與2025永續報告書端點**均回應HTTP 404**。
- `6192:objective_ranking_or_market_share:7b550e9b311db4ef`、`3a45ecd2ce0afe92` — `PARTIALLY_SUPPORTED` ×2；巨路111年報載「主要與國際程控**領導品牌 Emerson** 合作，與其**共同開發大中華**」（Emerson 4次、程控108次、代理43次）；惟「**獨家**」0次（且主要供應商含ABB、Honeywell、Yokogawa、Siemens）、「**最大**程控原廠」未載（官方用語為「領導廠商」）、「台積電」0次。
- `6192:objective_ranking_or_market_share:9d3d9e091d15025a`、`29dfc8d397ce595b`、`7b53b3873666c020` — `UNKNOWN_AFTER_RESEARCH` ×3；「台積電」「三成」皆0次，且「30%」8次均為**淨值比率**。
- 證據、期間、查閱日期與摘記記錄於 `semantic/author-088.json`（8 筆）。未修改發行人報告。
- Next pending claim by priority: `6192:objective_ranking_or_market_share:d0ce09fbc459509c` (巨路).

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
