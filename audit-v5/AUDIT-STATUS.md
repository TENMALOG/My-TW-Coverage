# Audit v5 Status

Updated: 2026-10-06 18:04 UTC
Branch: `audit-v5`

## Semantic HIGH review

- HIGH issuers: **836**
- Raw HIGH signals: **1,410**
- Unique HIGH claims: **1,399**
- Author-reviewed: **233 / 1,399**
- Remaining author review: **1,166**
- Latest batch: **author-042** (7 claims)
- Independent reviews: **0**; author decisions are not final acceptance.

### Existing author decision counts

- `ACCEPTED`: **48**
- `PARTIALLY_SUPPORTED`: **147**
- `UNSUPPORTED`: **1**
- `PERIOD_UNRESOLVED`: **0**
- `SOURCE_UNAVAILABLE`: **3**
- `UNKNOWN_AFTER_RESEARCH`: **34**

## Latest claim batch

- `2356:objective_ranking_or_market_share:ed253454231d412c` — `PARTIALLY_SUPPORTED`; 英業達50週年特刊第35/42頁載2002年康柏被惠普併購後ODM關係延續、「繼續成為HP核心供應商」；惟未載HP為最大筆電代工客戶或客戶占比。
- `2364:objective_ranking_or_market_share:1a5a7e549dde1f07` — `PARTIALLY_SUPPORTED`; 倫飛112年報第9/62頁載軍規電腦ODM/OEM與自有品牌Durabook、持續投入軍工規強固型筆電；惟「2000年第一台」未載。
- `2365:objective_ranking_or_market_share:694d960ffe356728` — `PARTIALLY_SUPPORTED`; 昆盈103年報與111年報告載滑鼠產品與Genius品牌（滑鼠17/8次）；惟「1985」「先驅」「第一支」皆0次。
- `2382:objective_ranking_or_market_share:e26e1066260b8298` — `PARTIALLY_SUPPORTED`; 廣達文件載註冊地址桃園市龜山區、第90頁「筆電出貨4,240萬台、市佔約26%、為全球筆記型電腦代工廠之龍頭」；惟「1988」0次。
- `2382:objective_ranking_or_market_share:c8e56ca69d86acd4` — `ACCEPTED`; 同頁明載其為全球筆記型電腦代工廠之龍頭。
- `2382:objective_ranking_or_market_share:846efe9d83aac395`、`beca552fa505ce2a` — `PARTIALLY_SUPPORTED` ×2; QCT為雲端事業部門並供應大型資料中心獲支持；惟「全球前50大資料中心市佔逾五成」未載。
- 證據、期間、查閱日期與摘記記錄於 `semantic/author-042.json`（7 筆）。未修改發行人報告。
- Next pending claim by priority: `2385:objective_ranking_or_market_share:22c3e7f8c90b61ca` (群光).

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
