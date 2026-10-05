# Audit v5 Status

Updated: 2026-10-07 04:04 UTC
Branch: `audit-v5`

## Semantic HIGH review

- HIGH issuers: **836**
- Raw HIGH signals: **1,410**
- Unique HIGH claims: **1,399**
- Author-reviewed: **289 / 1,399**
- Remaining author review: **1,110**
- Latest batch: **author-052** (8 claims)
- Independent reviews: **0**; author decisions are not final acceptance.

### Existing author decision counts

- `ACCEPTED`: **53**
- `PARTIALLY_SUPPORTED`: **185**
- `UNSUPPORTED`: **1**
- `PERIOD_UNRESOLVED`: **0**
- `SOURCE_UNAVAILABLE`: **3**
- `UNKNOWN_AFTER_RESEARCH`: **47**

## Latest claim batch

- `6225:objective_ranking_or_market_share:328bec4589432b52` — `PARTIALLY_SUPPORTED`; 天瀚111年報沿革載美/德/上海 AIPTEK 行銷公司，及「2000年04月推出**全球第一台3合1筆式數位視訊相機**」；惟「HyperPen」0次。
- `6728:objective_ranking_or_market_share:d66093d3d854cbc7` — `UNKNOWN_AFTER_RESEARCH`; 上洋114年報文字層為亂碼無法判讀，「AQUA」「Huebsch」「總代理」等皆0次。
- `2009:objective_ranking_or_market_share:40ef15d8963c4f66`、`99c95bc4f4f81779` — `PARTIALLY_SUPPORTED` ×2; 第一銅112年報第75/77頁載其為台灣銅片製造廠、台灣全部合金總銷售量約占**30%**、黃銅12次與磷青銅7次；惟「白銅」0次。
- `5871:objective_ranking_or_market_share:5462990384cd01df` — `PARTIALLY_SUPPORTED`; 第10頁「穩居台灣租賃業領先地位」、「中租迪和」29次、海外布局含中國大陸與東協7國；惟未以「最大」自稱。
- `5871:objective_ranking_or_market_share:0d13f2e2c5782586` — `PARTIALLY_SUPPORTED`; 業務項目與中小企業客群獲支持；惟「市佔率」0次、「裕融」「和潤」皆0次。
- `5871:objective_ranking_or_market_share:87162f778667a426` — `UNKNOWN_AFTER_RESEARCH`; 110年報中「zingala」「銀角」皆0次，未載BNPL平台。
- `5871:objective_ranking_or_market_share:8a01608f52e45045` — `PARTIALLY_SUPPORTED`; 第5/66頁載2018年裝置容量全台第一、2021年底2,655座電廠、發電總容量**918.22MW**、全民電廠平台；惟「2024年底超過1.5GW」未載。
- 證據、期間、查閱日期與摘記記錄於 `semantic/author-052.json`（8 筆）。未修改發行人報告。
- Next pending claim by priority: `6592:objective_ranking_or_market_share:2860da8fae309c7a` (和潤企業).

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
