# Audit v5 Status

Updated: 2026-10-06 12:04 UTC
Branch: `audit-v5`

## Semantic HIGH review

- HIGH issuers: **836**
- Raw HIGH signals: **1,410**
- Unique HIGH claims: **1,399**
- Author-reviewed: **189 / 1,399**
- Remaining author review: **1,210**
- Latest batch: **author-036** (9 claims)
- Independent reviews: **0**; author decisions are not final acceptance.

### Existing author decision counts

- `ACCEPTED`: **41**
- `PARTIALLY_SUPPORTED`: **120**
- `UNSUPPORTED`: **1**
- `PERIOD_UNRESOLVED`: **0**
- `SOURCE_UNAVAILABLE`: **3**
- `UNKNOWN_AFTER_RESEARCH`: **24**

## Latest claim batch

- `2345:objective_ranking_or_market_share:45533474be4d6591` — `PARTIALLY_SUPPORTED`; 智邦2016年報第4頁載參與OCP、第44頁「第一家通過OCP認證的10G交換器」；惟「白牌」出現0次、49%市占未載（第44頁數字為Gartner市場環境資料）。
- `3047:objective_ranking_or_market_share:8d08849b1db7901e`、`ccd9decfc4baa78c`、`6665972999a4ae24` — `UNKNOWN_AFTER_RESEARCH` ×3; 訊舟官網年報2014/2013皆404、MOPS年報端點回320 bytes、簡報端點404；康全電訊法說會404、年報端點320 bytes，未取得任何可檢視官方文件。
- `3163:objective_ranking_or_market_share:f4538d7b4e0ae3de`、`db69c04b1b9da86f` — `PARTIALLY_SUPPORTED` ×2; 波若威2020公開說明書第36/37頁支持WDM／PLC分光器／光纖連接器OEM/ODM；「台灣最大」「CPO」皆0次（第43頁5.18%為其占台灣光電產業產值比率）。
- `3209:objective_ranking_or_market_share:375fbb618f362445` — `PARTIALLY_SUPPORTED`; 全科111年報第8頁沿革載2003年取得Broadcom代理權、並取得Cypress代理權；惟年報載Cypress係與Infineon業務整合（非Broadcom併購），「5G」「Wi-Fi」「資料中心」皆0次。
- `3221:objective_ranking_or_market_share:1c545b7df1052ede`、`9bfb232098e92952` — `PARTIALLY_SUPPORTED` ×2; 台嘉碩2026簡報第4頁載6'/4'晶圓微影與MLCSP封裝、第5頁完整頻率元件產品線、第10/11頁應用含TPMS／Keyless／GNSS與400G-1.6T Smart NIC；惟「唯一」「台灣最大」「全球非手機用SAW市占領先」與Motorola沿革未載。
- 證據、期間、查閱日期與摘記記錄於 `semantic/author-036.json`（9 筆）。未修改發行人報告。
- Next pending claim by priority: `3363:objective_ranking_or_market_share:26fa475a285812b8` (上詮).

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
