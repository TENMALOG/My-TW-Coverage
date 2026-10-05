# Audit v5 Status

Updated: 2026-10-06 15:04 UTC
Branch: `audit-v5`

## Semantic HIGH review

- HIGH issuers: **836**
- Raw HIGH signals: **1,410**
- Unique HIGH claims: **1,399**
- Author-reviewed: **210 / 1,399**
- Remaining author review: **1,189**
- Latest batch: **author-039** (6 claims)
- Independent reviews: **0**; author decisions are not final acceptance.

### Existing author decision counts

- `ACCEPTED`: **44**
- `PARTIALLY_SUPPORTED`: **135**
- `UNSUPPORTED`: **1**
- `PERIOD_UNRESOLVED`: **0**
- `SOURCE_UNAVAILABLE`: **3**
- `UNKNOWN_AFTER_RESEARCH`: **27**

## Latest claim batch

- `6216:objective_ranking_or_market_share:35cb5307cb38ee31` — `PARTIALLY_SUPPORTED`; 居易2025永續報告第54頁載「歐洲是居易的主要市場」、第11頁載自有品牌 Vigor 與9次英國 PC PRO 最佳年度路由器品牌；惟全份未載市占率數字，亦未就德國／荷蘭提出量化陳述。
- `6220:objective_ranking_or_market_share:08b79d0e2afacd31` — `ACCEPTED`; 岳豐2020簡報第4頁載2006年購併Prime Wire、2016年收購Monoprice，第7/20頁載垂直整合，第10/15/21頁載Monoprice電商平台拓展B2B/B2C。
- `6245:objective_ranking_or_market_share:658825ba3e219605`、`01e6d42e67b49976` — `PARTIALLY_SUPPORTED` ×2; 立端2025資料第57頁載網路安全業務成長、2020 CSR第18頁載其與全球主要網路安全公司合作；惟「全球最大」0次、市占逾四成與北美約五成未載。
- `6245:objective_ranking_or_market_share:58a28527f37f9002` — `ACCEPTED`; 2020 CSR第6/18頁載2020年11月私募9億元可轉債由台達電全數認購；2025資料第47頁前十大股東表第1名台達電子18.34%（第2名7.38%）。
- `6416:objective_ranking_or_market_share:a6c6b74e700a6d31` — `PARTIALLY_SUPPORTED`; 瑞祺2026簡報第6頁載「硬體供應商模式」特徵、第11/13頁網路安全占66%、第12頁美洲占57%；惟「白牌」「OEM」出現0次，未具名客戶。
- 證據、期間、查閱日期與摘記記錄於 `semantic/author-039.json`（6 筆）。未修改發行人報告。
- Next pending claim by priority: `6417:objective_ranking_or_market_share:f2fcac08e268dad2` (韋僑).

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
