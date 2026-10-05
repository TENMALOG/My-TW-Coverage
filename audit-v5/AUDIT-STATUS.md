# Audit v5 Status

Updated: 2026-10-08 17:04 UTC
Branch: `audit-v5`

## Semantic HIGH review

- HIGH issuers: **836**
- Raw HIGH signals: **1,410**
- Unique HIGH claims: **1,399**
- Author-reviewed: **520 / 1,399**
- Remaining author review: **879**
- Latest batch: **author-089** (8 claims)
- Independent reviews: **0**; author decisions are not final acceptance.

### Existing author decision counts

- `ACCEPTED`: **73**
- `PARTIALLY_SUPPORTED`: **341**
- `UNSUPPORTED`: **1**
- `PERIOD_UNRESOLVED`: **0**
- `SOURCE_UNAVAILABLE`: **3**
- `UNKNOWN_AFTER_RESEARCH`: **102**

## Latest claim batch

- `6192:objective_ranking_or_market_share:d0ce09fbc459509c` — `PARTIALLY_SUPPORTED`；年報載 Emerson 為程控「**領導廠商**」；惟「全球最大」「獨家」皆0次，且主要供應商含 ABB、Honeywell、Yokogawa、Siemens。
- `8374:objective_ranking_or_market_share:3152a46dc54ea3c8` — `PARTIALLY_SUPPORTED`；羅昇110年報載「本公司屬**自動化機電零組件代理商暨技術服務業者**」（自動化66次、代理48次）；惟「1984」「最大」皆0次。
- `3158:objective_ranking_or_market_share:6f3b16014ede3133` — `UNKNOWN_AFTER_RESEARCH`；嘉實未查得官方年報或法說會端點。
- `6214:objective_ranking_or_market_share:efede12ca151ffcc` — `UNKNOWN_AFTER_RESEARCH`；精誠官方年報端點所下載之兩份檔案**均僅5,574 bytes**（擷取各僅1字元），顯非完整文件。
- `6221:objective_ranking_or_market_share:03dcbb306517351e` — `UNKNOWN_AFTER_RESEARCH`；晉泰2023簡報「精誠」「三成」「最大股東」皆0次。
- `6614:objective_ranking_or_market_share:a2228d1fc670af08` — `PARTIALLY_SUPPORTED`；資拓宏宇114年報「市場占有率」段載「行政院轄下43機關切入41個（涵蓋率**95%**）」「38間本國銀行切入其中35間，涵蓋率**逾90%**」（與claim之「服務逾90%台灣本土銀行」相符）；惟官方用語為「**涵蓋率**」而非市佔率（「市佔」0次），且「30億」0次。
- `6906:objective_ranking_or_market_share:662269e93948f5e3`、`d7f499644ed091ed` — `ACCEPTED` ×2；現觀科112年報載「取得**中東地區最大電信業者 STC** CovMo™合作合約」與「中東地區的**最大電信業者 STC 集團**」（STC 4次、中東5次、最大電信4次）。
- 證據、期間、查閱日期與摘記記錄於 `semantic/author-089.json`（8 筆）。未修改發行人報告。
- Next pending claim by priority: `7765:objective_ranking_or_market_share:ca7dd7afc3bd6233` (中華資安).

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
