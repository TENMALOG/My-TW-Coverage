# Audit v5 Status

Updated: 2026-10-07 12:04 UTC
Branch: `audit-v5`

## Semantic HIGH review

- HIGH issuers: **836**
- Raw HIGH signals: **1,410**
- Unique HIGH claims: **1,399**
- Author-reviewed: **338 / 1,399**
- Remaining author review: **1,061**
- Latest batch: **author-060** (7 claims)
- Independent reviews: **0**; author decisions are not final acceptance.

### Existing author decision counts

- `ACCEPTED`: **58**
- `PARTIALLY_SUPPORTED`: **212**
- `UNSUPPORTED`: **1**
- `PERIOD_UNRESOLVED`: **0**
- `SOURCE_UNAVAILABLE`: **3**
- `UNKNOWN_AFTER_RESEARCH`: **64**

## Latest claim batch

- `2402:objective_ranking_or_market_share:6eadc6e5bdc3ad83` — `UNKNOWN_AFTER_RESEARCH`; 毅嘉官網根網址HTTP 200，惟年報路徑（http/https）與股東資訊頁均回404，未取得可檢視文件。
- `2486:objective_ranking_or_market_share:e7b17a5349873c82`、`7243ef589ba0d390` — `ACCEPTED` ×2; 一詮2023永續報告第15頁載「**光電產業LED可見光及不可見光導線架的全球市佔率已經排名世界第一**」，並列主要產品含 LED 導線架、IC 導線架、陶瓷基板、均熱片（半導體）。
- `3008:objective_ranking_or_market_share:851df492397be9dc` — `UNKNOWN_AFTER_RESEARCH`; 大立光2013年報「Apple」「Samsung」「小米」「OPPO」「vivo」與「最大客戶」皆0次（客戶27次均為通稱），依客戶身分規則結為UNKNOWN（該版本亦非近期）。
- `3017:objective_ranking_or_market_share:f76fbbb6956b1040` — `UNKNOWN_AFTER_RESEARCH`; 未查得奇鋐官方網域可檢視PDF端點，所取得者均為券商與第三方媒體。
- `3036:objective_ranking_or_market_share:48c69f1daccb8476`、`8a0838b5f670f054` — `UNKNOWN_AFTER_RESEARCH` ×2; 文曄官方簡報端點連續兩次（含420秒逾時）下載失敗。
- 證據、期間、查閱日期與摘記記錄於 `semantic/author-060.json`（7 筆）。未修改發行人報告。
- 註記：本批次新增5筆 UNKNOWN，使 UNKNOWN 累計達64筆（佔已審338筆之18.9%），成因均為官方來源不可取得（404／逾時／未查得端點）。
- Next pending claim by priority: `3037:objective_ranking_or_market_share:2416d3deb1742a86` (欣興).

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
