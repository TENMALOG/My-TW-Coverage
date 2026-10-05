# Audit v5 Status

Updated: 2026-10-05 21:04 UTC
Branch: `audit-v5`

## Semantic HIGH review

- HIGH issuers: **836**
- Raw HIGH signals: **1,410**
- Unique HIGH claims: **1,399**
- Author-reviewed: **70 / 1,399**
- Remaining author review: **1,329**
- Latest batch: **author-021** (10 claims)
- Independent reviews: **0**; author decisions are not final acceptance.

### Existing author decision counts

- `ACCEPTED`: **23**
- `PARTIALLY_SUPPORTED`: **41**
- `UNSUPPORTED`: **1**
- `PERIOD_UNRESOLVED`: **0**
- `SOURCE_UNAVAILABLE`: **3**
- `UNKNOWN_AFTER_RESEARCH`: **2**

## Latest claim batch

- `1533:objective_ranking_or_market_share:7a6d45cabd1f1a81` — `PARTIALLY_SUPPORTED`; 車王電112年度年報第184頁載設立於民國71年、主要業務為汽車引擎傳動控制系統（電子點火器、電壓調整器及整流器），支持逾41年與引擎零組件業務；惟年報未以「唯一」描述其地位。
- `1536:objective_ranking_or_market_share:0a8bd467b7db2e7b` — `ACCEPTED`; 和大2026法說會簡報標題「TAIWAN TOP 1 GEAR MAKER」，113年度年報載其為「國內汽車齒輪產業第一把交椅」。
- `1536:objective_ranking_or_market_share:cce96a49ba94ccaf`、`fd8ac95e7e36addc` — `PARTIALLY_SUPPORTED` ×2; 和大114年度年報第71頁以代號揭露第一大銷貨客戶（甲公司）占銷貨淨額113年度43.94%、114年度51.19%；惟全篇無 BorgWarner 字樣，且「約40%」低於官方數字。
- `1563:objective_ranking_or_market_share:a0f33eff27b93300` — `ACCEPTED`; 德國 IHK「世界市場領導者」名錄 OTTO FUCHS 條目載其為汽車鍛造輪圈、底盤零件及同步環之世界市場領導者（產品欄首位為 Forged wheels，總部 Meinerzhagen）。
- `2105:objective_ranking_or_market_share:daa2ec046bdc0d7f` — `PARTIALLY_SUPPORTED`; 正新2022永續報告第8頁載「華人地區最大的輪胎專業製造公司，營業額持續維持台灣第一」；惟永續報告與2025Q4法說會簡報均未載全球輪胎廠排名。
- `2106:objective_ranking_or_market_share:0bd79cfdcec25a2d` — `ACCEPTED`; 建大2022永續報告第12頁載「以自有品牌KENDA行銷全球，現已成為台灣第2大、全球第26大的輪胎廠」。
- `2114:objective_ranking_or_market_share:1bcf873b591901ce`、`83a4decf054d606c`、`7279073e1958fd1e` — `ACCEPTED` ×3; 鑫永銓2024法說會第22頁載其橡皮壩「已成功打入日本市場，目前為日本第一大進口製造廠」。
- 證據、期間、查閱日期與摘記記錄於 `semantic/author-021.json`。未修改發行人報告。
- Next pending claim by priority: `2115:objective_ranking_or_market_share:62d5c63efe920f40` (六暉-KY).

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
