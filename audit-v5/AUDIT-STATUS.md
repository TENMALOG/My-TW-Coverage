# Audit v5 Status

Updated: 2026-10-10 01:04 UTC
Branch: `audit-v5`

## Semantic HIGH review

- HIGH issuers: **836**
- Raw HIGH signals: **1,410**
- Unique HIGH claims: **1,399**
- Author-reviewed: **732 / 1,399**
- Remaining author review: **667**
- Latest batch: **author-121** (8 claims)
- Independent reviews: **0**; author decisions are not final acceptance.

### Existing author decision counts

- `ACCEPTED`: **83**
- `PARTIALLY_SUPPORTED`: **476**
- `UNSUPPORTED`: **1**
- `PERIOD_UNRESOLVED`: **0**
- `SOURCE_UNAVAILABLE`: **3**
- `UNKNOWN_AFTER_RESEARCH`: **169**

## Latest claim batch

- `8086:objective_ranking_or_market_share:195cb9f67a470584` — `UNKNOWN_AFTER_RESEARCH`；該 claim 為**第三人（穩懋）之市場地位**，宏捷科議事錄「穩懋」「全球最大」「代工」皆0次，且穩懋官方網域先前遭 TLS 憑證失敗（author-112）。
- `8131:objective_ranking_or_market_share:5930424229e429b1` — `ACCEPTED`；福懋科110年報載「**南亞科技股份有限公司持股比例達32% 成為本公司最大股東**，**福懋興業股份有限公司持股比例降為30.68%**」＋台塑集團關聯圖——**逐字對應**。
- `8131:objective_ranking_or_market_share:478f771b0c4ced7b` — `PARTIALLY_SUPPORTED`；32%／最大股東逐字支持；惟「最大客戶」0次。
- `8131:objective_ranking_or_market_share:468108abf2d6a30b` — `PARTIALLY_SUPPORTED`；第一大股東成立；惟「占營收50%」未獲支持（「50%」1次為員工年齡別統計）。
- `8162:objective_ranking_or_market_share:53be25f984132f29`、`e32635bf5c906e45` — `ACCEPTED` ×2；微矽簡報載「深耕半導體產業超過**38年**」與「為國內**電源管理IC、MOSFET、氮化鎵(GaN)晶圓測試服務的最大供應商**」——**逐字對應**。
- `8261:objective_ranking_or_market_share:49acbcc2abe7bd34` — `PARTIALLY_SUPPORTED`；「MOSFET」1次；惟「6吋」「DMOS」「第一家」皆0次。
- `8299:objective_ranking_or_market_share:cd78eed6eeac704c` — `UNKNOWN_AFTER_RESEARCH`；群聯官方年報端點**連線中斷**。
- 證據、期間、查閱日期與摘記記錄於 `semantic/author-121.json`（8 筆）。未修改發行人報告。
- Next pending claim by priority: `3570:objective_ranking_or_market_share:35138bf9d920ff85` (大塚).

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
