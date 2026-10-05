# Audit v5 Status

Updated: 2026-10-05 19:04 UTC
Branch: `audit-v5`

## Semantic HIGH review

- HIGH issuers: **836**
- Raw HIGH signals: **1,410**
- Unique HIGH claims: **1,399**
- Author-reviewed: **52 / 1,399**
- Remaining author review: **1,347**
- Latest batch: **author-019** (8 claims)
- Independent reviews: **0**; author decisions are not final acceptance.

### Existing author decision counts

- `ACCEPTED`: **17**
- `PARTIALLY_SUPPORTED`: **29**
- `UNSUPPORTED`: **1**
- `PERIOD_UNRESOLVED`: **0**
- `SOURCE_UNAVAILABLE`: **3**
- `UNKNOWN_AFTER_RESEARCH`: **2**

## Latest claim batch

- `2237:objective_ranking_or_market_share:ee7593a1bc4fa73e` — `PARTIALLY_SUPPORTED`; 華德動能官方簡報第5頁載2011年台灣第一輛電動巴士上路、2019年首家取得電動巴士自主設計開發資格，支持領導與首創地位；惟簡報未載「市佔率約30%」「累計逾500輛」「首家通過認證」等文字（僅載台灣APTS市佔超過80%）。
- `1336:objective_ranking_or_market_share:cee272854eaffb62`、`fe2d9e60f44aa914` — `ACCEPTED` ×2; 台翰113年度年報主要股東名單列宣德科技29.12%為最大股東，第10頁股權鏈載宣德→香港商聯滔電子(24.59%)→立訊精密工業(100%)，支持最終母公司為立訊精密。
- `1338:objective_ranking_or_market_share:666e6bac07f9b5a5`、`043acc8984fdcb88` — `ACCEPTED` ×2; 廣華控股2025官方簡報第15頁載2024年客戶結構日系46%、中國28%、歐美25%，其中日產34%為最大單一品牌、本田5%。
- `1339:objective_ranking_or_market_share:375175af06d90a6f` — `UNKNOWN_AFTER_RESEARCH`; 昭輝2020／2024／2026三版官方簡報均無 LKQ、CAPA 或客戶集中度文字，年報端點108–113年度皆回應320 bytes非文件內容，無法確立亦無證據否定。
- `1339:objective_ranking_or_market_share:8c262157716b38f8` — `PARTIALLY_SUPPORTED`; LKQ FY2025 10-K 與官方品牌頁支持「LKQ／Keystone 為北美最大 AM 通路」；惟括號中「合計佔營收50%+」為昭輝特有財務結構，未獲其官方來源支持。
- `1506:objective_ranking_or_market_share:b7bdbc426ed03c94` — `PARTIALLY_SUPPORTED`; 正道官方NASA技術頁載取得NASA授權、全球唯一有量產實績之專業NASA活塞廠、年產逾20萬顆，均獲支持；惟官方明載鍛造版本係「延伸開發第一顆」，20萬顆屬NASA鋁合金活塞（鑄造），claim 將鑄造量產與鍛造混為一談。
- 證據、期間、查閱日期與摘記記錄於 `semantic/author-019.json`。未修改發行人報告。
- Next pending claim by priority: `1521:objective_ranking_or_market_share:b0344d1922014380` (大億).

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
