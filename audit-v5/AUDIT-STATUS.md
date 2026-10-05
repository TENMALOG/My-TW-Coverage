# Audit v5 Status

Updated: 2026-10-09 12:04 UTC
Branch: `audit-v5`

## Semantic HIGH review

- HIGH issuers: **836**
- Raw HIGH signals: **1,410**
- Unique HIGH claims: **1,399**
- Author-reviewed: **655 / 1,399**
- Remaining author review: **744**
- Latest batch: **author-108** (8 claims)
- Independent reviews: **0**; author decisions are not final acceptance.

### Existing author decision counts

- `ACCEPTED`: **77**
- `PARTIALLY_SUPPORTED`: **424**
- `UNSUPPORTED`: **1**
- `PERIOD_UNRESOLVED`: **0**
- `SOURCE_UNAVAILABLE`: **3**
- `UNKNOWN_AFTER_RESEARCH`: **150**

## Latest claim batch

- `5483:objective_ranking_or_market_share:330863256f88c588` — `PARTIALLY_SUPPORTED`；中美晶110年報「矽晶圓」53次；惟「3-12吋」「台灣最大」皆0次。
- `6147:objective_ranking_or_market_share:b5110c677f121bef`、`55e95765fe157fbc`、`6bdc058d1011e062` — `PARTIALLY_SUPPORTED` ×3；頎邦110年報「**驅動IC」8 次**、「**凸塊」13 次**、「COF」5次、「COG」5次；惟「全球最大」「南茂」皆0次，且「**50%」9 次為「削減50%」「50%提升至75%」「25.50%」**等，非市占率。
- `6261:objective_ranking_or_market_share:37228631f06f5ce4` — `UNKNOWN_AFTER_RESEARCH`；久元年報「**晶元」0 次**（客戶108次、光電36次均為通稱），「最大客戶」「占營收」皆0次。
- `6532:objective_ranking_or_market_share:9f3fc56944fd9568` — `PARTIALLY_SUPPORTED`；瑞耘113年報「**OEM」4 次**、「晶圓旋乾」3次、「SRD」2次；惟「應用材料」「Applied Materials」皆0次（「Applied」2次之一為**學術期刊名**）。
- `6532:objective_ranking_or_market_share:7e0ba7530f386152` — `UNKNOWN_AFTER_RESEARCH`；年報「應用材料」「台積電」「日月光」「最大客戶」「六成」皆0次。
- `6533:objective_ranking_or_market_share:de4c47986928bfbe` — `UNKNOWN_AFTER_RESEARCH`；所取得文件為**股東常會議事手冊**（非年報），「Meta」「MTIA」「聯發科」「聯詠」「Renesas」皆0次。
- 證據、期間、查閱日期與摘記記錄於 `semantic/author-108.json`（8 筆）。未修改發行人報告。
- Next pending claim by priority: `6830:objective_ranking_or_market_share:f1578b23f3b713fe` (汎銓).

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
