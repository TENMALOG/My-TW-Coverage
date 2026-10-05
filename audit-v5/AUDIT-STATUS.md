# Audit v5 Status

Updated: 2026-10-07 19:04 UTC
Branch: `audit-v5`

## Semantic HIGH review

- HIGH issuers: **836**
- Raw HIGH signals: **1,410**
- Unique HIGH claims: **1,399**
- Author-reviewed: **378 / 1,399**
- Remaining author review: **1,021**
- Latest batch: **author-067** (7 claims)
- Independent reviews: **0**; author decisions are not final acceptance.

### Existing author decision counts

- `ACCEPTED`: **64**
- `PARTIALLY_SUPPORTED`: **239**
- `UNSUPPORTED`: **1**
- `PERIOD_UNRESOLVED`: **0**
- `SOURCE_UNAVAILABLE`: **3**
- `UNKNOWN_AFTER_RESEARCH`: **71**

## Latest claim batch

- `4939:objective_ranking_or_market_share:2a2e5d7a4b653457` — `PARTIALLY_SUPPORTED`; 亞電108年報「手機」49次、「穿戴」20次、「FPC」39次、「軟板」67次、「覆蓋膜」65次；惟「最大宗」0次、「車用」僅2次且未載電池模組FPC。
- `4958:objective_ranking_or_market_share:e9718e647cdf6213`、`40a491b3e2ad9593` — `UNKNOWN_AFTER_RESEARCH` ×2; 臻鼎官方新聞稿PDF僅3字元（影像排版），且查得之topco-global年報經確認為他公司文件（臻鼎／4958／ZDT皆0次）。
- `4960:objective_ranking_or_market_share:d14cd3d4febf570b` — `PARTIALLY_SUPPORTED`; 誠美材文件註記載「**群創光電(股)公司及代表人劉昭賢於109年5月6日辭任**」（群創僅1次），未載其為客戶或最大出海口。
- `5228:objective_ranking_or_market_share:b96cf4a86eed0538` — `PARTIALLY_SUPPORTED`; 鈺鎧2022簡報載車用17次、醫療14次、網通3次；惟「Cochlear」「全球最大」皆0次（簡報用語為「電子耳朵」）。
- `5228:objective_ranking_or_market_share:bc677a4369a50038`、`95ce91a2dd332b21` — `UNKNOWN_AFTER_RESEARCH` ×2; 同上，客戶名未載，依具名客戶身分規則結為UNKNOWN。
- 證據、期間、查閱日期與摘記記錄於 `semantic/author-067.json`（7 筆）。未修改發行人報告。
- Next pending claim by priority: `5243:objective_ranking_or_market_share:7d90a20a437364ad` (乙盛-KY).

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
