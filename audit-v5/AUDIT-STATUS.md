# Audit v5 Status

Updated: 2026-10-08 08:04 UTC
Branch: `audit-v5`

## Semantic HIGH review

- HIGH issuers: **836**
- Raw HIGH signals: **1,410**
- Unique HIGH claims: **1,399**
- Author-reviewed: **454 / 1,399**
- Remaining author review: **945**
- Latest batch: **author-080** (6 claims)
- Independent reviews: **0**; author decisions are not final acceptance.

### Existing author decision counts

- `ACCEPTED`: **69**
- `PARTIALLY_SUPPORTED`: **295**
- `UNSUPPORTED`: **1**
- `PERIOD_UNRESOLVED`: **0**
- `SOURCE_UNAVAILABLE`: **3**
- `UNKNOWN_AFTER_RESEARCH`: **86**

## Latest claim batch

- `6776:objective_ranking_or_market_share:59f0a1faacffbf5e` — `PARTIALLY_SUPPORTED`；展碁文件載「2020年9月取得**代理銷售 Adobe 產品**」「**代理 Adobe 全系列產品**」（軟體50次、授權10次）；惟「最大」8次為「**LG 在台最大品牌代理商**」等，未見「台灣最大軟體通路商」。
- `8070:objective_ranking_or_market_share:13e7c6a3959a27bd` — `PARTIALLY_SUPPORTED`；同長華年報，代理住友培科封膠樹脂成立（住友7次、封膠19次）；惟「67%」3次為**董事出席率**與法人股東持股比例，非國內市占率。
- `2072:objective_ranking_or_market_share:033b7b8eb52cfe3b` — `PARTIALLY_SUPPORTED`；世紀鋼2025簡報載「**世紀風電**」「**世紀風電-台北港**」「**水下基礎**基樁Section製造」（水下基礎17次、世紀風電4次）；惟「本土」「量能最大」皆0次。
- `6691:objective_ranking_or_market_share:4a06f569d516bc7a`、`d5272625e216200f` — `UNKNOWN_AFTER_RESEARCH` ×2；洋基工程2026簡報「台積電」「ASML」「最大客戶」皆0次，且「40%」2次之上下文為「**0.40%**」。
- `6750:objective_ranking_or_market_share:40044574fe259065` — `UNKNOWN_AFTER_RESEARCH`；泰創工程未查得可下載之年報或法說會端點，僅官網服務與案例頁。
- 證據、期間、查閱日期與摘記記錄於 `semantic/author-080.json`（6 筆）。未修改發行人報告。
- Next pending claim by priority: `6873:objective_ranking_or_market_share:8e8bea538366ff4d` (泓德能源).

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
