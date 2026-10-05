# Audit v5 Status

Updated: 2026-10-09 11:04 UTC
Branch: `audit-v5`

## Semantic HIGH review

- HIGH issuers: **836**
- Raw HIGH signals: **1,410**
- Unique HIGH claims: **1,399**
- Author-reviewed: **647 / 1,399**
- Remaining author review: **752**
- Latest batch: **author-107** (8 claims)
- Independent reviews: **0**; author decisions are not final acceptance.

### Existing author decision counts

- `ACCEPTED`: **77**
- `PARTIALLY_SUPPORTED`: **419**
- `UNSUPPORTED`: **1**
- `PERIOD_UNRESOLVED`: **0**
- `SOURCE_UNAVAILABLE`: **3**
- `UNKNOWN_AFTER_RESEARCH`: **147**

## Latest claim batch

- `3189:objective_ranking_or_market_share:d30c008603686d3a` — `UNKNOWN_AFTER_RESEARCH`；景碩官方年報端點（114與112年度）皆回應 **HTTP 401**。
- `3413:objective_ranking_or_market_share:ebe2223d339ab310` — `UNKNOWN_AFTER_RESEARCH`；京鼎MOPS簡報端點回應 **HTTP 404**。
- `3551:objective_ranking_or_market_share:21c365ea8b4c5152` — `UNKNOWN_AFTER_RESEARCH`；世禾2025簡報「台積電」0次（營收5次、清洗3次），「最大」2次為泛用語。
- `3563:objective_ranking_or_market_share:678d0af119707979` — `UNKNOWN_AFTER_RESEARCH`；牧德官方簡報端點**連線中斷**。
- `5222:objective_ranking_or_market_share:dbde28318bead583` — `PARTIALLY_SUPPORTED`；全訊114年報載「本公司自**1998年成立**以來」與「**化合物半導體**…（氮化鎵10次）」；惟「唯一」0次。
- `5222:objective_ranking_or_market_share:ac86f330feeaa01a` — `PARTIALLY_SUPPORTED`；年報「**雷達」32 次、「飛彈」4 次**（國防應用成立）；惟「最大客戶」「8成」皆0次。
- `5272:objective_ranking_or_market_share:5a22c41a58004d2c` — `UNKNOWN_AFTER_RESEARCH`；笙科102年報**文字層僅擷取3,559字元**，SRD／LNB／聯笙／RF IC 皆0次。
- `5483:objective_ranking_or_market_share:f9ec0490463350f9` — `PARTIALLY_SUPPORTED`；中美晶110年報「矽晶圓」53次、「太陽能」139次、「藍寶石」6次；惟「3吋」「12吋」「台灣最大」皆0次（「最大」7次為泛用語）。
- 證據、期間、查閱日期與摘記記錄於 `semantic/author-107.json`（8 筆）。未修改發行人報告。
- Next pending claim by priority: `5483:objective_ranking_or_market_share:330863256f88c588` (中美晶).

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
