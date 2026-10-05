# Audit v5 Status

Updated: 2026-10-06 04:04 UTC
Branch: `audit-v5`

## Semantic HIGH review

- HIGH issuers: **836**
- Raw HIGH signals: **1,410**
- Unique HIGH claims: **1,399**
- Author-reviewed: **125 / 1,399**
- Remaining author review: **1,274**
- Latest batch: **author-028** (8 claims)
- Independent reviews: **0**; author decisions are not final acceptance.

### Existing author decision counts

- `ACCEPTED`: **34**
- `PARTIALLY_SUPPORTED`: **75**
- `UNSUPPORTED`: **1**
- `PERIOD_UNRESOLVED`: **0**
- `SOURCE_UNAVAILABLE`: **3**
- `UNKNOWN_AFTER_RESEARCH`: **12**

## Latest claim batch

- `2892:objective_ranking_or_market_share:ed08854a9f3fb74e` — `PARTIALLY_SUPPORTED`; 第一金現增公開說明書第3/11頁載設立日期「民國92年1月2日」→ 2003年成立成立；惟「歷史最悠久的泛公股金控之一」未獲查閱來源比較。
- `2892:objective_ranking_or_market_share:76b816df512daafe` — `PARTIALLY_SUPPORTED`; 公開說明書支持第一銀行為核心子公司（占金控收益93.98%）；惟「1899」於查閱文件中出現0次，CSR報告載全台188個營運據點與33處海外營運點（與claim的182／31不同）。
- `2892:objective_ranking_or_market_share:ca7ce41d34befae1` — `PARTIALLY_SUPPORTED`; 公開說明書子公司摘要表列第一金證券、第一金證券投資信託、第一金人壽；惟明台產物保險不在現行子公司表內（第33頁註2顯示其於民國92年曾為股份轉換對象）。
- `2892:objective_ranking_or_market_share:88dd8b6be75d5904` — `PARTIALLY_SUPPORTED`; 中小企業放款獲CSR報告「市占連續第八年居國銀首位」支持；惟「房貸」「進出口」出現0次，「財富管理」僅見於董事經歷。
- `2892:objective_ranking_or_market_share:e8187bb231e1e142`、`3f5488a25cf9016f`、`2f5c3c2bb8f9797b` — `ACCEPTED` ×3; 公開說明書子公司摘要表列第一金證券（經紀）、第一金證券投資信託（投信／基金管理）、第一金人壽保險（壽險）。
- `2897:objective_ranking_or_market_share:de51a64a7f203960` — `PARTIALLY_SUPPORTED`; 王道銀行官方文件載其2017年改制後為「全台第一家原生數位銀行」、2017年取得B型企業認證並於2021／2025重新認證；惟未主張其為「首家取得B型企業認證之上市銀行」（官方載其為當時臺灣第21家B型企業）。
- 證據、期間、查閱日期與摘記記錄於 `semantic/author-028.json`。未修改發行人報告。
- Next pending claim by priority: `5880:objective_ranking_or_market_share:a7669e207f28c0b5` (合庫金).

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
