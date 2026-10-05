# Audit v5 Status

Updated: 2026-10-09 06:04 UTC
Branch: `audit-v5`

## Semantic HIGH review

- HIGH issuers: **836**
- Raw HIGH signals: **1,410**
- Unique HIGH claims: **1,399**
- Author-reviewed: **611 / 1,399**
- Remaining author review: **788**
- Latest batch: **author-102** (6 claims)
- Independent reviews: **0**; author decisions are not final acceptance.

### Existing author decision counts

- `ACCEPTED`: **77**
- `PARTIALLY_SUPPORTED`: **396**
- `UNSUPPORTED`: **1**
- `PERIOD_UNRESOLVED`: **0**
- `SOURCE_UNAVAILABLE`: **3**
- `UNKNOWN_AFTER_RESEARCH`: **134**

## Latest claim batch

- `5292:objective_ranking_or_market_share:b7b5d29e96b2972f` — `PARTIALLY_SUPPORTED`；華懋2024簡報載「**VOCs污染防治系統**」「高科技**VOCs淨化設備**」（VOCs 6次、轉輪5次）；惟「沸石」「市佔」「黃光」皆0次。
- `1808:objective_ranking_or_market_share:ee0f0ac169c03e89` — `PARTIALLY_SUPPORTED`；潤隆簡報「完工」3次、「2025」3次；惟「最大」「交屋」皆0次。
- `2539:objective_ranking_or_market_share:0660a4ba59fb2fd6` — `PARTIALLY_SUPPORTED`；櫻花建2024簡報（**英文版**）「Taichung」18次；惟「1988」「largest」「Baujia」皆0次，且簡報載董事長為「**Mr. Chen, Shin-Ying**」，與claim所述**林家宏**不同。
- `2542:objective_ranking_or_market_share:ca12741b0453c297`、`ed6d035d3884b395` — `PARTIALLY_SUPPORTED` ×2；興富發113年報「曹淵博」18次；惟「1980」「民營建商」「全台最大」皆0次——**年報中「全球最大」係指其合作對象「全球最大連鎖酒店萬豪集團」，非興富發自身**。
- `2542:objective_ranking_or_market_share:c259dca2ad8e1373` — `PARTIALLY_SUPPORTED`；年報「**齊裕營造**」11次（集團子公司）成立；惟「地下室」0次，「全國地下室挖掘量最大」未獲支持。
- 證據、期間、查閱日期與摘記記錄於 `semantic/author-102.json`（6 筆）。未修改發行人報告。
- Next pending claim by priority: `2923:objective_ranking_or_market_share:2deccd89094eaab3` (鼎固-KY).

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
