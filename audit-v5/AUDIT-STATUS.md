# Audit v5 Status

Updated: 2026-10-06 05:04 UTC
Branch: `audit-v5`

## Semantic HIGH review

- HIGH issuers: **836**
- Raw HIGH signals: **1,410**
- Unique HIGH claims: **1,399**
- Author-reviewed: **133 / 1,399**
- Remaining author review: **1,266**
- Latest batch: **author-029** (8 claims)
- Independent reviews: **0**; author decisions are not final acceptance.

### Existing author decision counts

- `ACCEPTED`: **35**
- `PARTIALLY_SUPPORTED`: **80**
- `UNSUPPORTED`: **1**
- `PERIOD_UNRESOLVED`: **0**
- `SOURCE_UNAVAILABLE`: **3**
- `UNKNOWN_AFTER_RESEARCH`: **14**

## Latest claim batch

- `5880:objective_ranking_or_market_share:a7669e207f28c0b5`、`0f3b5a58ad55e774` — `UNKNOWN_AFTER_RESEARCH` ×2; 合庫金官網投資人路徑未提供可下載年報或股東結構文件，立法院公聽會報告全文未含股東結構表，未能取得主要股東名單與中小企業放款市占資料。
- `1101:objective_ranking_or_market_share:70c0cf57f148a361` — `ACCEPTED`; 台泥官方簡報第3頁時間軸載「1946 • 國營台灣水泥成立」「第一家股票上市公司(1962年)」，標題為「從水泥產業到綠色環境工程公司」。
- `1101:objective_ranking_or_market_share:1d1eb04d19b03299` — `PARTIALLY_SUPPORTED`; 簡報載2018年「全球化佈局歐亞非」、2024 ESG年鑑載「跨五大洲13市場」、年鑑第498頁載「土耳其最大水泥公司 OYAK」；惟「台泥國際」出現0次。
- `1104:objective_ranking_or_market_share:9a15f087597b0139` — `PARTIALLY_SUPPORTED`; 環泥2025法說會第6頁支持水泥／混凝土／石膏板為主要產品（13%營收）；惟石膏板市占率與「全台第一約90%」全份未載。
- `1109:objective_ranking_or_market_share:7c6d8b2d2057eb58`、`5fd4ab936a526e30` — `PARTIALLY_SUPPORTED` ×2; 信大簡報第6/7/8/9頁支持江蘇信寧新型建材為大陸子公司、以南京為主要市場；惟官方載「占南京市區域市場約17%左右」，與claim的15%不同。
- `1802:objective_ranking_or_market_share:75e14cf20248f928` — `PARTIALLY_SUPPORTED`; 台玻2019 CSR第13頁載「1964年8月25日 台玻成立於1964年」及三大產品線；惟「國內最大」「名列前茅」等字樣全份出現0次。
- 證據、期間、查閱日期與摘記記錄於 `semantic/author-029.json`。未修改發行人報告。
- Next pending claim by priority: `2504:objective_ranking_or_market_share:271a4f0e71b4103a` (國產).

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
