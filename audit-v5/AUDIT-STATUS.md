# Audit v5 Status

Updated: 2026-10-10 00:04 UTC
Branch: `audit-v5`

## Semantic HIGH review

- HIGH issuers: **836**
- Raw HIGH signals: **1,410**
- Unique HIGH claims: **1,399**
- Author-reviewed: **724 / 1,399**
- Remaining author review: **675**
- Latest batch: **author-120** (8 claims)
- Independent reviews: **0**; author decisions are not final acceptance.

### Existing author decision counts

- `ACCEPTED`: **80**
- `PARTIALLY_SUPPORTED`: **473**
- `UNSUPPORTED`: **1**
- `PERIOD_UNRESOLVED`: **0**
- `SOURCE_UNAVAILABLE`: **3**
- `UNKNOWN_AFTER_RESEARCH`: **167**

## Latest claim batch

- `6573:objective_ranking_or_market_share:0ab58d2ad0c9cdd6` — `PARTIALLY_SUPPORTED`；虹揚文件「太陽能」13次、「**旁路二極體」1 次**；惟「市佔」「工業電腦」「AI」「高功率」皆0次。
- `6679:objective_ranking_or_market_share:37679da783fb2682`、`7459dd76809acab4` — `PARTIALLY_SUPPORTED` ×2；鈺太文件「**MEMS」27 次、「麥克風」16 次**、「筆電」4次；惟「**市占」「龍頭」皆 0 次**（未載 55-60%）。
- `6789:objective_ranking_or_market_share:0b84bdb1ceb376d2`、`113f7291089fc909` — `PARTIALLY_SUPPORTED` ×2；采鈺議事手冊「彩色濾光」4次；惟「台積電」「CIS」「市占」「世界第一」皆0次。
- `8086:objective_ranking_or_market_share:afb154ac23e8d0ac`、`f979a0ca4a7bc6dd`、`2b8e68c61d000145` — `PARTIALLY_SUPPORTED` ×3；宏捷科**民國97年度財務報告**「**Skyworks」7 次**、「砷化鎵」2次；惟「最大客戶」「56%」「第二大」「晶圓代工」「24」皆0次（**非近期文件**）。
- 證據、期間、查閱日期與摘記記錄於 `semantic/author-120.json`（8 筆）。未修改發行人報告。
- Next pending claim by priority: `8086:objective_ranking_or_market_share:195cb9f67a470584` (宏捷科).

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
