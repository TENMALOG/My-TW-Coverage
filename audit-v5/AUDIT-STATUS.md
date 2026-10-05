# Audit v5 Status

Updated: 2026-10-08 00:04 UTC
Branch: `audit-v5`

## Semantic HIGH review

- HIGH issuers: **836**
- Raw HIGH signals: **1,410**
- Unique HIGH claims: **1,399**
- Author-reviewed: **405 / 1,399**
- Remaining author review: **994**
- Latest batch: **author-072** (5 claims)
- Independent reviews: **0**; author decisions are not final acceptance.

### Existing author decision counts

- `ACCEPTED`: **66**
- `PARTIALLY_SUPPORTED`: **259**
- `UNSUPPORTED`: **1**
- `PERIOD_UNRESOLVED`: **0**
- `SOURCE_UNAVAILABLE`: **3**
- `UNKNOWN_AFTER_RESEARCH`: **76**

## Latest claim batch

- `6196:objective_ranking_or_market_share:c712b83c2829b483` — `PARTIALLY_SUPPORTED`; 帆宣文件載「榮獲**台積電15廠A/B**」「台積電2022年【**優良承攬商**】」「2022 日月光」（半導體33次、顯示器7次）；惟「最大客戶」「鴻海」皆0次。
- `6230:objective_ranking_or_market_share:d3934452c5eec0ad` — `PARTIALLY_SUPPORTED`; 尼得科超眾2025簡報載「主營業務: 散熱模組、散熱片、熱導管及微均熱板」「10W NB至10kW AI Server」；惟「市佔」「45%」「霸主」皆0次，且「30%」唯一命中為**Nidec 持股86.30%**之一部分。
- `6474:objective_ranking_or_market_share:e1e8b7bc5f77c89b` — `PARTIALLY_SUPPORTED`; 華豫寧簡報載「2019成立**WAFERLOCK**子公司暨併購利滙」與電子鎖／門禁／IoT業務；惟「市佔超過五成」之「50%」係**銷售漏斗示意圖階段**，且未載 IoT 營收占比25%。
- `6512:objective_ranking_or_market_share:52216fcbf3c5cfac`、`2876e98579307c73` — `UNKNOWN_AFTER_RESEARCH` ×2；**發現 ticker-公司身分不符**：claim 所述業務主體為「南俊」（伺服器滑軌、美超微、NVIDIA GB200），而查得之官方文件主體為**南俊國際（股票代號 6584）**（簡報首頁載「南俊國際股份有限公司（6584TW）」「全球鋼珠導軌的專家」），本 claim 隊列紀錄卻掛載於 ticker **6512**（啟發電）。已依專案規則第2條記錄，待 author 端覆核。
- 證據、期間、查閱日期與摘記記錄於 `semantic/author-072.json`（5 筆）。未修改發行人報告。
- Next pending claim by priority: `6538:objective_ranking_or_market_share:84142ea1fb4928c3` (倉和).

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
