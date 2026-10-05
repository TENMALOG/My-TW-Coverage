# Audit v5 Status

Updated: 2026-10-07 11:04 UTC
Branch: `audit-v5`

## Semantic HIGH review

- HIGH issuers: **836**
- Raw HIGH signals: **1,410**
- Unique HIGH claims: **1,399**
- Author-reviewed: **331 / 1,399**
- Remaining author review: **1,068**
- Latest batch: **author-059** (7 claims)
- Independent reviews: **0**; author decisions are not final acceptance.

### Existing author decision counts

- `ACCEPTED`: **56**
- `PARTIALLY_SUPPORTED`: **212**
- `UNSUPPORTED`: **1**
- `PERIOD_UNRESOLVED`: **0**
- `SOURCE_UNAVAILABLE`: **3**
- `UNKNOWN_AFTER_RESEARCH`: **59**

## Latest claim batch

- `2327:objective_ranking_or_market_share:4bc2906c15245aae` — `PARTIALLY_SUPPORTED`; 國巨2025年報第77頁載「**國巨為全球鉭質電容第一大廠，市占率46％以上**」與「**本公司是世界最大的晶片電阻製造廠商**」；惟「晶片電阻34%」「MLCC 15%第三」「電感12%第三」未載。
- `2355:objective_ranking_or_market_share:e2751dcf4f662431` — `PARTIALLY_SUPPORTED`; 敬鵬111年報載「以**汽車板業務為主**」（汽車17次、PCB 82次）；惟「全球第四」0次、「市占」僅1次泛用語。
- `2355:objective_ranking_or_market_share:45cccbbebc446916` — `UNKNOWN_AFTER_RESEARCH`; 「Bosch」「Denso」「Continental」「Magna」「Delphi」「Visteon」皆0次，依具名客戶身分規則結為UNKNOWN。
- `2383:objective_ranking_or_market_share:d7e1c63f7e5f9a21`、`8cd3eedf1d33d1d5` — `UNKNOWN_AFTER_RESEARCH` ×2; 台光電2023年報文字層呈**亂碼**，僅子公司資料表可讀，「銅箔基板」僅見於子公司業務描述，「CCL」「載板」皆0次。
- `2393:objective_ranking_or_market_share:855bf0c8d0c3d854`、`feb61c76bb10402c` — `ACCEPTED` ×2; 億光2021年報第106頁載「**本公司目前為國內最大的LED專業封裝廠**」「照明元件、背光元件、手持裝置…車用元件及不可見光元件之**產值明顯超過台灣同業**」。
- 證據、期間、查閱日期與摘記記錄於 `semantic/author-059.json`（7 筆）。未修改發行人報告。
- Next pending claim by priority: `2402:objective_ranking_or_market_share:6eadc6e5bdc3ad83` (毅嘉).

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
