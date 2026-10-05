# Audit v5 Status

Updated: 2026-10-08 02:04 UTC
Branch: `audit-v5`

## Semantic HIGH review

- HIGH issuers: **836**
- Raw HIGH signals: **1,410**
- Unique HIGH claims: **1,399**
- Author-reviewed: **416 / 1,399**
- Remaining author review: **983**
- Latest batch: **author-074** (5 claims)
- Independent reviews: **0**; author decisions are not final acceptance.

### Existing author decision counts

- `ACCEPTED`: **66**
- `PARTIALLY_SUPPORTED`: **268**
- `UNSUPPORTED`: **1**
- `PERIOD_UNRESOLVED`: **0**
- `SOURCE_UNAVAILABLE`: **3**
- `UNKNOWN_AFTER_RESEARCH`: **78**

## Latest claim batch

- `6962:objective_ranking_or_market_share:8a6e457c9cf41c59` — `PARTIALLY_SUPPORTED`; 奕力2024及2026簡報載「車用／工控／平板／穿戴TDDI」（TDDI 19次、9次）；惟「市佔」「第二」「聯詠」皆0次。
- `8039:objective_ranking_or_market_share:0708d00d3969d082` — `PARTIALLY_SUPPORTED`; 台虹114年股東會文件中「銅箔」1次；「全球前三大」「大中華」「FCCL」「市佔」皆0次（該文件非完整年報）。
- `8046:objective_ranking_or_market_share:b6b6b05ab39bd5c8` — `PARTIALLY_SUPPORTED`; 南電113年報載「積極切入**AI 伺服器**供應鏈」、多項「**ABF載板**」擴建案、應用含「高效能運算晶片(HPC)」「5G交換器晶片」與「ASIC」（載板67次、ABF 16次）；惟「GPU」「CPU」皆0次。
- `8069:objective_ranking_or_market_share:2ea0db4264ee1d7d` — `PARTIALLY_SUPPORTED`; 元太文件載「**在全球擁有極高的市占率，全球主要電子閱讀器品牌供應商都使用元太科技生產的 EPD**」（電子紙360次、專利55次）；惟「九成」「龍頭」「Amazon」「Kindle」皆0次。
- `8069:objective_ranking_or_market_share:5f18abcc84d8634a` — `PARTIALLY_SUPPORTED`; 元太文件載「**樂天Kobo**」為其電子紙生態圈夥伴（Kobo 2次）；惟「Amazon」「Kindle」與「全球最大」皆0次。
- 證據、期間、查閱日期與摘記記錄於 `semantic/author-074.json`（5 筆）。未修改發行人報告。
- Next pending claim by priority: `8074:objective_ranking_or_market_share:0d087bffe38bc6c8` (鉅橡).

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
