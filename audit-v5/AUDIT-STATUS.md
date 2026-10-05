# Audit v5 Status

Updated: 2026-10-06 16:04 UTC
Branch: `audit-v5`

## Semantic HIGH review

- HIGH issuers: **836**
- Raw HIGH signals: **1,410**
- Unique HIGH claims: **1,399**
- Author-reviewed: **218 / 1,399**
- Remaining author review: **1,181**
- Latest batch: **author-040** (8 claims)
- Independent reviews: **0**; author decisions are not final acceptance.

### Existing author decision counts

- `ACCEPTED`: **46**
- `PARTIALLY_SUPPORTED`: **139**
- `UNSUPPORTED`: **1**
- `PERIOD_UNRESOLVED`: **0**
- `SOURCE_UNAVAILABLE`: **3**
- `UNKNOWN_AFTER_RESEARCH`: **29**

## Latest claim batch

- `6417:objective_ranking_or_market_share:f2fcac08e268dad2` — `PARTIALLY_SUPPORTED`; 韋僑2021簡報第17頁載「美洲占比最高，係醫療客戶對RFID」、第5頁載全球首家取得ISO 13485；惟「2025年」與「美國子公司」皆未出現於該簡報。
- `6638:objective_ranking_or_market_share:a10e7dbfbe350734` — `PARTIALLY_SUPPORTED`; 沅聖113年報載112及113年度第一大銷貨客戶占總銷售額僅13%及12%，且「Ring」「Amazon」「門鈴」皆0次。
- `6715:objective_ranking_or_market_share:f73e500d5e922beb` — `PARTIALLY_SUPPORTED`; 嘉基2018簡報第5頁載多項Thunderbolt 3產品獲Intel認證；惟「Thunderbolt 4/5」「唯一授權原始開發者」未載。
- `7812:objective_ranking_or_market_share:e6cb42dfad1770b6` — `UNKNOWN_AFTER_RESEARCH`; 稜研2025簡報「毫米波」39次，惟「印度」與「全球最大」皆0次。
- `8045:objective_ranking_or_market_share:6295b64544ea58b8` — `PARTIALLY_SUPPORTED`; 2017簡報第4頁載「台灣第一大寬頻放大器」；惟「成立於1992」與新北市地址未載。
- `8045:objective_ranking_or_market_share:b159b59617de6cf8` — `ACCEPTED`; 年報第5頁與2017簡報第4頁載「亞洲唯一通過北美主要MSO認證HFC研製商」、ACI自有品牌。
- `8045:objective_ranking_or_market_share:a101d657fc95e240` — `ACCEPTED`; 年報第66頁銷售地區表載112年度美洲占93.10%（111年76.50%）；2017簡報第8頁載「通過Comcast認證」、第16頁載逾100個系統使用ACI產品。
- `8089:objective_ranking_or_market_share:cee0f405aeaab0db` — `UNKNOWN_AFTER_RESEARCH`; 康全電訊年報端點回320 bytes、法說會端點404，未取得可檢視文件。
- 證據、期間、查閱日期與摘記記錄於 `semantic/author-040.json`（8 筆）。未修改發行人報告。
- Next pending claim by priority: `2301:objective_ranking_or_market_share:253cd0fbdf268d3a` (光寶科).

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
