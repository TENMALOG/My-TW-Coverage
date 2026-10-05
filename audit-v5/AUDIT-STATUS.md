# Audit v5 Status

Updated: 2026-10-08 15:04 UTC
Branch: `audit-v5`

## Semantic HIGH review

- HIGH issuers: **836**
- Raw HIGH signals: **1,410**
- Unique HIGH claims: **1,399**
- Author-reviewed: **504 / 1,399**
- Remaining author review: **895**
- Latest batch: **author-087** (6 claims)
- Independent reviews: **0**; author decisions are not final acceptance.

### Existing author decision counts

- `ACCEPTED`: **71**
- `PARTIALLY_SUPPORTED`: **334**
- `UNSUPPORTED`: **1**
- `PERIOD_UNRESOLVED`: **0**
- `SOURCE_UNAVAILABLE`: **3**
- `UNKNOWN_AFTER_RESEARCH`: **95**

## Latest claim batch

- `9935:objective_ranking_or_market_share:edace39a5abeffd8` — `UNKNOWN_AFTER_RESEARCH`；慶豐富2018簡報「Walmart」「沃爾瑪」皆0次（窗簾11次）。
- `1732:objective_ranking_or_market_share:481aee35491d420d` — `PARTIALLY_SUPPORTED`；毛寶2020 CSR報告載「冷洗精」3次之產品線敘述；惟「白鷺」「市佔」皆0次。
- `6504:objective_ranking_or_market_share:a9d7ea309cd8da26` — `PARTIALLY_SUPPORTED`；南六年報載「2023年**全球不織布銷售排名，本公司係列於第23名**」（在「全球前40大」範圍內）與「水針不織布」（水針35次、不織布153次）；惟「**亞洲水針不織布供應龍頭**」未獲支持（年報用語為「亞洲地區**重要的**不織布大廠」；「龍頭」1次實為「**水龍頭**」），「1972」0次。
- `6504:objective_ranking_or_market_share:dad592a04c1ad087`、`b60ee696040661e2` — `PARTIALLY_SUPPORTED` ×2；南六年報載下游生技產品含「柔濕巾、面膜、乳液」；惟「**蘭韻**」「**康乃馨**」「**化妝棉**」皆0次。
- `9919:objective_ranking_or_market_share:2affdfaaf7479723` — `PARTIALLY_SUPPORTED`；康那香2026簡報「不織布」24次；惟「1968」「衛生用品」「全球前40」皆0次。
- 證據、期間、查閱日期與摘記記錄於 `semantic/author-087.json`（6 筆）。未修改發行人報告。
- Next pending claim by priority: `6671:objective_ranking_or_market_share:1c6728d636eea59e` (三能-KY).

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
