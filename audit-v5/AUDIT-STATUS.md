# Audit v5 Status

Updated: 2026-10-08 06:04 UTC
Branch: `audit-v5`

## Semantic HIGH review

- HIGH issuers: **836**
- Raw HIGH signals: **1,410**
- Unique HIGH claims: **1,399**
- Author-reviewed: **441 / 1,399**
- Remaining author review: **958**
- Latest batch: **author-078** (6 claims)
- Independent reviews: **0**; author decisions are not final acceptance.

### Existing author decision counts

- `ACCEPTED`: **68**
- `PARTIALLY_SUPPORTED`: **286**
- `UNSUPPORTED`: **1**
- `PERIOD_UNRESOLVED`: **0**
- `SOURCE_UNAVAILABLE`: **3**
- `UNKNOWN_AFTER_RESEARCH`: **83**

## Latest claim batch

- `2450:objective_ranking_or_market_share:d4c4eba514df929a` — `ACCEPTED`; 神腦106年報載「**創立於1979年**，為**全台行動手持裝置最大通路商**」「全台數位滙流裝置最大之通路商」與「（中華電信）成為神腦**最大股東**」（中華電信16次）。
- `3048:objective_ranking_or_market_share:e7578b46e213723c`、`144af8e9daef4625` — `UNKNOWN_AFTER_RESEARCH` ×2；就益登(3048)所取得之 zenitron.com.tw 檔案經檢視確認其為「**2023永續報告書**」且目錄載「關於**增你強**」，屬另一公司文件，故不予採用；未取得3048可檢視之正式文件。
- `3312:objective_ranking_or_market_share:ef9a168379d5a594`、`30b39681faeb2489` — `PARTIALLY_SUPPORTED` ×2；弘憶110年報載「**代理並銷售瑞昱半導體科技(股)公司電子零組件產品**」（瑞昱39次）；惟「最大代理線」「最大供應商」未載，「7成」「營收佔比」0次，而「70%」2次實為**員工福利精算折現率0.70%**。
- `3702:objective_ranking_or_market_share:bbfe49daa140f2f0` — `PARTIALLY_SUPPORTED`；大聯大2022年報載「**全球第二、亞太區第一大的半導體零組件通路商**，總部位於臺（北）」（全球第二3次、2005 6次）；惟claim之「全球最大…之一」與官方「全球第二」用語不同，且「8,806」於2022年報中0次。
- 證據、期間、查閱日期與摘記記錄於 `semantic/author-078.json`（6 筆）。未修改發行人報告。
- Next pending claim by priority: `3360:objective_ranking_or_market_share:1e5c4a342b962d2f` (尚立).

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
