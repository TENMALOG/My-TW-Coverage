# Audit v5 Status

Updated: 2026-10-06 13:04 UTC
Branch: `audit-v5`

## Semantic HIGH review

- HIGH issuers: **836**
- Raw HIGH signals: **1,410**
- Unique HIGH claims: **1,399**
- Author-reviewed: **196 / 1,399**
- Remaining author review: **1,203**
- Latest batch: **author-037** (7 claims)
- Independent reviews: **0**; author decisions are not final acceptance.

### Existing author decision counts

- `ACCEPTED`: **41**
- `PARTIALLY_SUPPORTED`: **126**
- `UNSUPPORTED`: **1**
- `PERIOD_UNRESOLVED`: **0**
- `SOURCE_UNAVAILABLE`: **3**
- `UNKNOWN_AFTER_RESEARCH`: **25**

## Latest claim batch

- `3363:objective_ranking_or_market_share:26fa475a285812b8` — `PARTIALLY_SUPPORTED`; 上詮2025年報第72頁載ReLFACon光纖陣列元件FAU精準對位與封裝技術、第73頁二維光纖陣列精密對準共封裝技術、第68頁載長期目標為CPO光纖陣列元件主要供應商；惟「COUPE」與「獨家」皆0次，「台積電」2次均與CPO認證無關。
- `3491:objective_ranking_or_market_share:94f1a06238faac2a` — `PARTIALLY_SUPPORTED`; 昇達科2026簡報第3頁載1999年9月成立、產品為微波&毫米波元件及天線；惟「唯一」0次。
- `3491:objective_ranking_or_market_share:b1519b89f78df062` — `PARTIALLY_SUPPORTED`; 簡報第4頁低軌衛星主要客戶列Amazon Leo／SpaceX／AST SpaceMobile／Intellian；惟「最大客戶」官方僅1次且未具名，其發射時程（2025/4/28首批、6/13第二批）與Amazon Leo相符，無法確立SpaceX為最大客戶。
- `3491:objective_ranking_or_market_share:e76f95644dba4f6a` — `PARTIALLY_SUPPORTED`; 產品定位成立；「台灣唯一」未獲支持。
- `3558:objective_ranking_or_market_share:b07caacadd76de3a` — `UNKNOWN_AFTER_RESEARCH`; 神準2022簡報載OEM/ODM占92%，但未出現Cisco或Meraki，亦未具名任何客戶。
- `3596:objective_ranking_or_market_share:6e94f9bb077f0c5b`、`f3bf92f9c38ba724` — `PARTIALLY_SUPPORTED` ×2; 智易114年報第5/87頁支持IAD、PON、5G FWA、Wi-Fi 7產品線，第116頁載仁寶為法人董事暨大股東；惟「全球最大」0次。
- 證據、期間、查閱日期與摘記記錄於 `semantic/author-037.json`（7 筆）。未修改發行人報告。
- Next pending claim by priority: `3694:objective_ranking_or_market_share:411bb8cf29a1b2fb` (海華).

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
