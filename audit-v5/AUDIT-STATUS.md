# Audit v5 Status

Updated: 2026-10-05 20:04 UTC
Branch: `audit-v5`

## Semantic HIGH review

- HIGH issuers: **836**
- Raw HIGH signals: **1,410**
- Unique HIGH claims: **1,399**
- Author-reviewed: **60 / 1,399**
- Remaining author review: **1,339**
- Latest batch: **author-020** (8 claims)
- Independent reviews: **0**; author decisions are not final acceptance.

### Existing author decision counts

- `ACCEPTED`: **17**
- `PARTIALLY_SUPPORTED`: **37**
- `UNSUPPORTED`: **1**
- `PERIOD_UNRESOLVED`: **0**
- `SOURCE_UNAVAILABLE`: **3**
- `UNKNOWN_AFTER_RESEARCH`: **2**

## Latest claim batch

- `1521:objective_ranking_or_market_share:b0344d1922014380` — `PARTIALLY_SUPPORTED`; 大億114年度年報第57頁「市場佔有率：國內約為80%」、112年度年報第71頁「國內為80%」，支持OEM車燈龍頭與高市占；惟 claim 所述「72%」與官方80%不符。
- `1522:objective_ranking_or_market_share:c39cb97e670a83a1` — `PARTIALLY_SUPPORTED`; 堤維西2023永續報告第22頁載其為「全球領先OEM車廠及AM售服市場的夥伴與供應商之一」、TYC品牌行銷全球130多國；惟「北美AM車燈市佔約12%」與「全球前五大」均未見於官方來源。
- `1522:objective_ranking_or_market_share:9f7b131fa64ec7b2` — `PARTIALLY_SUPPORTED`; 官方簡報僅載TYC自建北美發貨倉，未具名 LKQ 等經銷商，亦無12%市佔數字。
- `1524:objective_ranking_or_market_share:37a66df6e8c59992`、`3fdf0568b0589c62`、`7bfdfa0fb2fba733` — `PARTIALLY_SUPPORTED` ×3; 耿鼎112年度年報第9頁載105年獲 LKQ 供應商評估獎（LKQ為客戶），第57頁載其為北美AM鈑金件最主要供應商之一；惟第59頁銷貨客戶表以代號揭露（最大客戶為客戶A、24.66%），未具名 LKQ，且無「市佔近40%」（相關40.6%為耿鼎自身北美銷售占比）。
- `1525:objective_ranking_or_market_share:fd492ed31d1ccf47`、`67775914202401b9` — `PARTIALLY_SUPPORTED` ×2; 江申2019 CSR第10頁載其為「國內目前最大商用車車架生產公司」、涵蓋3.5噸~35噸及巴士底盤，年報公司沿革載車架供應國瑞與中華；惟年報僅載車架「屬寡占產品」、木床市場占有率90%，無車架市占100%。
- 證據、期間、查閱日期與摘記記錄於 `semantic/author-020.json`。未修改發行人報告。
- Next pending claim by priority: `1533:objective_ranking_or_market_share:7a6d45cabd1f1a81` (車王電).

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
