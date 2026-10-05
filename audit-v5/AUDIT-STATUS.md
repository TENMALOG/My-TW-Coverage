# Audit v5 Status

Updated: 2026-10-06 08:04 UTC
Branch: `audit-v5`

## Semantic HIGH review

- HIGH issuers: **836**
- Raw HIGH signals: **1,410**
- Unique HIGH claims: **1,399**
- Author-reviewed: **156 / 1,399**
- Remaining author review: **1,243**
- Latest batch: **author-032** (8 claims)
- Independent reviews: **0**; author decisions are not final acceptance.

### Existing author decision counts

- `ACCEPTED`: **40**
- `PARTIALLY_SUPPORTED`: **95**
- `UNSUPPORTED`: **1**
- `PERIOD_UNRESOLVED`: **0**
- `SOURCE_UNAVAILABLE`: **3**
- `UNKNOWN_AFTER_RESEARCH`: **17**

## Latest claim batch

- `6593:objective_ranking_or_market_share:bcd8051088ba12eb`、`b3ba33d575c72e62`、`2b4e80914df0aac2` — `PARTIALLY_SUPPORTED` ×3; 台灣銘板2025簡報第2頁載 RFID 技術與二代悠遊晶片、第10頁載「掌握銀行及票證公司年度合約770萬張」，2017簡報第7頁載「★Mastercard 正式認可」、第17頁載「全球唯二之二代悠遊晶片合格供應商」；惟「台灣前四大發卡銀行」「市佔35%」「美國專利」「Visa」均未載。
- `6914:objective_ranking_or_market_share:e0e3a03b5e669446` — `ACCEPTED`; 阜爾運通2026法說會第18頁載「就目前主要停車管理公司案場分析，城市車旅目前已居於業界領導位置」。
- `8342:objective_ranking_or_market_share:acce089189cec438`、`a2f0330b12f64684` — `UNKNOWN_AFTER_RESEARCH` ×2; 益張2025簡報「北美」「市佔」「最大」皆為0次，107年報「北美」僅1次且屬市場環境描述、「市佔」「領導」為0。
- `2820:objective_ranking_or_market_share:4ea2d7d9b3fa5942` — `PARTIALLY_SUPPORTED`; 華票109年報第7頁載王道商業銀行持股28.36%為最大股東；惟「寶佳集團持股約17%」未載（寶佳僅出現2次且為董事經歷）。
- `2820:objective_ranking_or_market_share:7eeb0fcbdc78b0fb` — `ACCEPTED`; 同頁載「截至110年3月底王道商業銀行（持股28.36%）仍為華票最大股東」。
- 證據、期間、查閱日期與摘記記錄於 `semantic/author-032.json`。未修改發行人報告。
- Next pending claim by priority: `2855:objective_ranking_or_market_share:23dcc1ae4b2739ba` (統一證).

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
