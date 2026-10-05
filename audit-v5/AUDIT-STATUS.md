# Audit v5 Status

Updated: 2026-10-05 18:04 UTC
Branch: `audit-v5`

## Semantic HIGH review

- HIGH issuers: **836**
- Raw HIGH signals: **1,410**
- Unique HIGH claims: **1,399**
- Author-reviewed: **44 / 1,399**
- Remaining author review: **1,355**
- Latest batch: **author-018** (7 claims)
- Independent reviews: **0**; author decisions are not final acceptance.

### Existing author decision counts

- `ACCEPTED`: **13**
- `PARTIALLY_SUPPORTED`: **26**
- `UNSUPPORTED`: **1**
- `PERIOD_UNRESOLVED`: **0**
- `SOURCE_UNAVAILABLE`: **3**
- `UNKNOWN_AFTER_RESEARCH`: **1**

## Latest claim batch

- `2206:objective_ranking_or_market_share:2206926921111339` — `PARTIALLY_SUPPORTED`; 三陽2026法人說明會簡報第3頁「台灣摩托車與汽車製造的領導者」、第4頁載業務橫跨摩托車與汽車且新竹廠同時具機車30萬輛與汽車2萬輛產能，支持雙製造能力；惟「台灣唯一」未獲官方陳述。
- `2206:objective_ranking_or_market_share:63ed0282b9ad9374` — `ACCEPTED`; 簡報第4頁載2025年自有品牌摩托車占台灣市場44.3%、2022年5月重返台灣機車品牌第一名；第15頁載外銷版圖橫跨中國／東協／東北亞／歐洲／美洲，並明載為 Lambretta、Peugeot 代工。
- `2206:objective_ranking_or_market_share:f1d0e04eae11fc9f` — `PARTIALLY_SUPPORTED`; 簡報第4頁載汽車部門生產及引進現代汽車產品、ESG報告載與 HYUNDAI 策略聯盟，支持在台生產；惟官方未以「獨家總代理」描述三陽本身，且第17頁載2025年現代汽車市占率4.55%（第5名），不支持「市佔率屢創新高」。
- `1319:objective_ranking_or_market_share:92d37f3eb1beade9` — `PARTIALLY_SUPPORTED`; 東陽2022永續報告第31頁「全球最大的汽車塑膠AM供應廠」、第54頁「全球AM鈑金供應龍頭」、第62頁「逾200個國家、2,300個客戶」均獲支持；惟2020／2021／2022三份報告書均無「70%」「35%」市占數字。
- `1319:objective_ranking_or_market_share:2a6fc80138e4eb21` — `PARTIALLY_SUPPORTED`; LKQ FY2025 Form 10-K 載其北美部門為北美最大替代性車輛零件配送網路、Keystone 為 LKQ 子公司，支持 LKQ／Keystone 之通路地位；惟東陽三份報告書中 LKQ／Keystone／State Farm 出現次數皆為 0，東陽特定合作關係與 State Farm 效應未獲支持。
- `1319:objective_ranking_or_market_share:40b14c614d7aad1a`、`4f8e5c27889374aa` — `ACCEPTED` ×2; LKQ 10-K 及官方品牌頁明載其為北美最大替代性車輛零件配送網路、Keystone 為其子公司與美國最大售後零件供應商。
- 證據、期間、查閱日期與摘記記錄於 `semantic/author-018.json`。未修改發行人報告。
- Next pending claim by priority: `2237:objective_ranking_or_market_share:ee7593a1bc4fa73e` (華德動能).

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
