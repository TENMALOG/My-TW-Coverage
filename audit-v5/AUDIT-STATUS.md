# Audit v5 Status

Updated: 2026-10-08 01:04 UTC
Branch: `audit-v5`

## Semantic HIGH review

- HIGH issuers: **836**
- Raw HIGH signals: **1,410**
- Unique HIGH claims: **1,399**
- Author-reviewed: **411 / 1,399**
- Remaining author review: **988**
- Latest batch: **author-073** (6 claims)
- Independent reviews: **0**; author decisions are not final acceptance.

### Existing author decision counts

- `ACCEPTED`: **66**
- `PARTIALLY_SUPPORTED`: **263**
- `UNSUPPORTED`: **1**
- `PERIOD_UNRESOLVED`: **0**
- `SOURCE_UNAVAILABLE`: **3**
- `UNKNOWN_AFTER_RESEARCH`: **78**

## Latest claim batch

- `6538:objective_ranking_or_market_share:84142ea1fb4928c3` — `PARTIALLY_SUPPORTED`; 倉和111年報載「**CF 系列**產品**3D 無網結網版**」「深耕太陽能網版印刷領域」（網版56次、無網結9次、太陽能24次、銀漿6次）；惟「全球唯一」「獨家」「首家」皆0次。
- `6673:objective_ranking_or_market_share:e881d11eadac0b96`、`5837eee3cc7c02e7` — `UNKNOWN_AFTER_RESEARCH` ×2；和詮官方年報端點回應 **HTTP 404**。
- `6698:objective_ranking_or_market_share:e3db967c354ef4c5` — `PARTIALLY_SUPPORTED`；旭暉年報載其為「**AMOLED面板關鍵製程用精密金屬遮罩**」（遮罩72次、OLED86次）；惟「40%」係「**AMOLED智慧型手機應用比重**」而非其市占率，且年報將「中國京東方、中國和輝、中國華星、中國維信諾」併列為下游代表公司而未區分是否已為客戶。
- `6732:objective_ranking_or_market_share:60bfec13a29befba` — `PARTIALLY_SUPPORTED`；昇佳簡報「環境光」7次、ALS 2次、PS 2次；惟「非蘋」「Android」「市佔」皆0次。
- `6863:objective_ranking_or_market_share:208c742c8478bb55` — `PARTIALLY_SUPPORTED`；永道公司文件「RFID」9次、「永豐餘」3次；惟「全球第二」「亞洲最大」「市佔」「25%」「50億」皆0次。
- 證據、期間、查閱日期與摘記記錄於 `semantic/author-073.json`（6 筆）。未修改發行人報告。
- Next pending claim by priority: `6962:objective_ranking_or_market_share:8a6e457c9cf41c59` (奕力-KY).

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
