# Audit v5 Status

Updated: 2026-10-07 09:04 UTC
Branch: `audit-v5`

## Semantic HIGH review

- HIGH issuers: **836**
- Raw HIGH signals: **1,410**
- Unique HIGH claims: **1,399**
- Author-reviewed: **317 / 1,399**
- Remaining author review: **1,082**
- Latest batch: **author-057** (5 claims)
- Independent reviews: **0**; author decisions are not final acceptance.

### Existing author decision counts

- `ACCEPTED`: **54**
- `PARTIALLY_SUPPORTED`: **207**
- `UNSUPPORTED`: **1**
- `PERIOD_UNRESOLVED`: **0**
- `SOURCE_UNAVAILABLE`: **3**
- `UNKNOWN_AFTER_RESEARCH`: **52**

## Latest claim batch

- `6940:objective_ranking_or_market_share:a339a04db47953d6` — `PARTIALLY_SUPPORTED`; 格斯2025簡報以「鈦酸鋰」「LTO」「NCM」為主軸（LTO 18次、鈦酸鋰7次、NCM 9次、「LTO電池代工合約」）；惟「台灣唯一」0次。
- `6940:objective_ranking_or_market_share:6cfe81e246b74e61` — `PARTIALLY_SUPPORTED`; 簡報載「安裝地點：**中油**嘉義綠能所加油站」；惟「最大客戶」0次、未載標案規模或客戶占比。
- `7750:objective_ranking_or_market_share:f2879969d03c99dd` — `PARTIALLY_SUPPORTED`; 新代2026簡報載「CNC 控制器」「AI賦能智慧控制器」（CNC 8次、控制器11次）；惟「市佔」「逾20%」「FANUC」「Siemens」「亞洲領先」皆0次（「第三」係「第三個五年計劃」）。
- `8038:objective_ranking_or_market_share:d89476319d794d57` — `UNKNOWN_AFTER_RESEARCH`; 長園科2023簡報載鋰鐵電池與UPS/儲能電池模組、半導體產業儲能系統（鋰鐵32次、UPS 16次、儲能33次）；惟「台積電」「最大客戶」皆0次，依具名客戶身分規則結為UNKNOWN。
- `1582:objective_ranking_or_market_share:948268fc83d4768f` — `PARTIALLY_SUPPORTED`; 信錦2022議事錄載營收主要來自顯示器樞紐、專利逾140項多與液晶監視器底座相關、「監視器軸承暨底座的**領導地位**」；惟「全球最大」「市佔」「Hinge」皆0次。
- 證據、期間、查閱日期與摘記記錄於 `semantic/author-057.json`（5 筆）。未修改發行人報告。
- Next pending claim by priority: `2308:objective_ranking_or_market_share:102dbd9ad2f63ed0` (台達電).

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
