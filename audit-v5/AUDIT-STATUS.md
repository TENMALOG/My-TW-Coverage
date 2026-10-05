# Audit v5 Status

Updated: 2026-10-08 21:04 UTC
Branch: `audit-v5`

## Semantic HIGH review

- HIGH issuers: **836**
- Raw HIGH signals: **1,410**
- Unique HIGH claims: **1,399**
- Author-reviewed: **548 / 1,399**
- Remaining author review: **851**
- Latest batch: **author-093** (8 claims)
- Independent reviews: **0**; author decisions are not final acceptance.

### Existing author decision counts

- `ACCEPTED`: **75**
- `PARTIALLY_SUPPORTED`: **360**
- `UNSUPPORTED`: **1**
- `PERIOD_UNRESOLVED`: **0**
- `SOURCE_UNAVAILABLE`: **3**
- `UNKNOWN_AFTER_RESEARCH`: **109**

## Latest claim batch

- `2636:objective_ranking_or_market_share:b0e48b98528244b3` — `UNKNOWN_AFTER_RESEARCH`；台驊官方財務專區為文件索引，未提供可下載年報或簡報。
- `2642:objective_ranking_or_market_share:6cfd9d7f082d8b12` — `PARTIALLY_SUPPORTED`；宅配通財報載「汽車路線貨運及宅配等專業物流配送服務」與「**東元電機股份有限公司持有本公司**」（東元15次）；惟「第一家」「戶對戶」「日本通運」皆0次。
- `5287:objective_ranking_or_market_share:b429f32154c5e076` — `PARTIALLY_SUPPORTED`；數字年報載591（85次）、8591（35次）等平台組合；惟「高市佔率」之概括表述未見（「市占」0次）。
- `5287:objective_ranking_or_market_share:ee2db393fbb7a072` — `PARTIALLY_SUPPORTED`；591之平台存在與業務成立；惟「**台灣最大**房屋租售媒合平台」未獲支持（文件中以「最大」描述者為**8591**與**小雞上工**，非591）。
- `5287:objective_ranking_or_market_share:bd1a0819aadbeb8c` — `ACCEPTED`；年報載「**8591 寶物交易網：臺灣最大的線上遊戲虛擬寶物交易平台**」——逐字對應。
- `8454:objective_ranking_or_market_share:831fc9adc6fce229`、`8562fb574e9c1bc9`、`faf0013285a9ca12` — `PARTIALLY_SUPPORTED` ×3；富邦媒2024年報（**英文版**）載「**leading e-commerce player**」與「leading the **No. 1 e-commerce brand**」（e-commerce 35次、B2C 9次）；惟「突破千億」未見，且中文關鍵字於英文文件中均0次（須改以英文比對）。
- 證據、期間、查閱日期與摘記記錄於 `semantic/author-093.json`（8 筆）。未修改發行人報告。
- Next pending claim by priority: `1432:objective_ranking_or_market_share:308460c572bff85d` (大魯閣).

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
