# Audit v5 Status

Updated: 2026-10-05 16:34 UTC
Branch: `audit-v5`

## Semantic HIGH review

- HIGH issuers: **836**
- Raw HIGH signals: **1,410**
- Unique HIGH claims: **1,399**
- Author-reviewed: **31 / 1,399**
- Remaining author review: **1,368**
- Latest batch: **author-016** (3 claims)
- Independent reviews: **0**; author decisions are not final acceptance.

### Existing author decision counts

- `ACCEPTED`: **7**
- `PARTIALLY_SUPPORTED`: **19**
- `UNSUPPORTED`: **1**
- `PERIOD_UNRESOLVED`: **0**
- `SOURCE_UNAVAILABLE`: **3**
- `UNKNOWN_AFTER_RESEARCH`: **1**

## Latest claim batch

- `4414:objective_ranking_or_market_share:cb90ae7e677cf480` — `PARTIALLY_SUPPORTED`; 如興民國114年法說會簡報第11頁標題「全球布局之牛仔褲專業製造商」、第8頁列示被收購公司「玖地製造有限公司及Tooku Holdings Limited」明細，支持牛仔褲製造商定位與玖地收購；惟第4頁自述為「全球前三牛仔成衣廠」而非最大，且2024年全年銷量60,913仟件與 claim 的1.2億件訂單／9,000萬件製造量不符，故「全球最大」及所述數字不成立。
- `4432:objective_ranking_or_market_share:5839812e308b4ea7` — `UNKNOWN_AFTER_RESEARCH`; 銘旺實113年度年報第87頁以代號揭露最大客戶（客戶甲）占銷貨淨額29.38%，與 claim 所述「約20%」不符，且231頁年報與官方網站均未出現 Under Armour；既不能確認亦無證據否定，依政策以 UNKNOWN_AFTER_RESEARCH 結案。
- `4438:objective_ranking_or_market_share:05ea182e0e761907` — `PARTIALLY_SUPPORTED`; 廣越2025年11月官方法說會簡報第14頁「成立於1995年」支持成立時間；惟第15頁自述「全球前三大高端戶外機能服飾製造商」，未使用「最大」，故「全球最大高階羽絨外套製造商」不成立。
- 證據、期間、查閱日期與摘記記錄於 `semantic/author-016.json`。未修改發行人報告。
- Next pending claim by priority: `8932:objective_ranking_or_market_share:39298f531ff2064c` (智通).

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
