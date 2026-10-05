# Audit v5 Status

Updated: 2026-10-05 17:04 UTC
Branch: `audit-v5`

## Semantic HIGH review

- HIGH issuers: **836**
- Raw HIGH signals: **1,410**
- Unique HIGH claims: **1,399**
- Author-reviewed: **37 / 1,399**
- Remaining author review: **1,362**
- Latest batch: **author-017** (6 claims)
- Independent reviews: **0**; author decisions are not final acceptance.

### Existing author decision counts

- `ACCEPTED`: **10**
- `PARTIALLY_SUPPORTED`: **22**
- `UNSUPPORTED`: **1**
- `PERIOD_UNRESOLVED`: **0**
- `SOURCE_UNAVAILABLE`: **3**
- `UNKNOWN_AFTER_RESEARCH`: **1**

## Latest claim batch

- `8932:objective_ranking_or_market_share:39298f531ff2064c` — `PARTIALLY_SUPPORTED`; 智通2024永續報告書第17頁載「創立於西元1978年」及2023年6月更名、第21頁列客戶 Wal-Mart／Target／JCPenney／MACYS／Kohl's，支持成立、MAX拉鍊產品與零售客戶；惟「三大事業體」官方稱「兩大核心事業體」、「Toyota等60餘家汽車品牌」官方所述為「近60個國際大型品牌認證」（涵蓋成衣箱包，未出現 Toyota），故該部分不成立。
- `8932:objective_ranking_or_market_share:2c4e8e723b5b77d9` — `PARTIALLY_SUPPORTED`; YKK 官方統合報告書《This is YKK 2025》第11頁載2014年獲 Porter Prize 之「global leader in zippers」、第58頁載業務遍及70國與拉鍊年產能逾300萬公里，支持其日本企業與全球領導地位；惟全篇未揭露全球市占率，「市佔約35%」未獲確立。
- `2207:objective_ranking_or_market_share:12f16578b4009931` — `ACCEPTED`; 和泰年報第112頁載多年位居汽車產業市場領先、法說會第15頁載「蟬聯台灣車市冠軍24年」，第5頁載「總代理：TOYOTA、LEXUS、HINO」，第10頁載2025年三品牌合計市佔38.6%（近16年最高），與「約40%」相當。
- `2207:objective_ranking_or_market_share:ea263c42d696e282` — `ACCEPTED`; 和泰年報第121頁主要原料供應表將 TOYOTA 與 HINO 之國內供應商均列為 Kuozui Motors（唯一國內製造商），第132頁產品銷售合約載國瑞提供授權製造車輛供在台銷售。
- `2207:objective_ranking_or_market_share:41ac99c4757c51d2` — `ACCEPTED`; 與 ea263c42d696e282 同源證據（年報第121、132頁），支持「國瑞汽車 — Toyota/Hino 台灣唯一組裝廠」。
- `2207:objective_ranking_or_market_share:f0cf847d4e06fec3` — `PARTIALLY_SUPPORTED`; 官方揭露之38.6%係 TOYOTA＋LEXUS＋HINO 三品牌合計口徑，TOYOTA 單一品牌為30.1%、LEXUS 為豪華車市場28.0%；claim 以「Toyota、Lexus」為範圍與官方口徑不符。
- 證據、期間、查閱日期與摘記記錄於 `semantic/author-017.json`。未修改發行人報告。
- Next pending claim by priority: `2206:objective_ranking_or_market_share:2206926921111339` (三陽工業).

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
