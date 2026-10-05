# Audit v5 Status

Updated: 2026-10-08 05:04 UTC
Branch: `audit-v5`

## Semantic HIGH review

- HIGH issuers: **836**
- Raw HIGH signals: **1,410**
- Unique HIGH claims: **1,399**
- Author-reviewed: **435 / 1,399**
- Remaining author review: **964**
- Latest batch: **author-077** (7 claims)
- Independent reviews: **0**; author decisions are not final acceptance.

### Existing author decision counts

- `ACCEPTED`: **67**
- `PARTIALLY_SUPPORTED`: **283**
- `UNSUPPORTED`: **1**
- `PERIOD_UNRESOLVED`: **0**
- `SOURCE_UNAVAILABLE`: **3**
- `UNKNOWN_AFTER_RESEARCH`: **81**

## Latest claim batch

- `6473:objective_ranking_or_market_share:b29d00af5856229f` — `UNKNOWN_AFTER_RESEARCH`；美賣（興櫃）未查得可下載之年報或法人說明會端點，僅見官網平台介紹與櫃買中心基本資料頁。
- `1603:objective_ranking_or_market_share:12171e5a5dfe2650`、`fe4b64c156172c36` — `UNKNOWN_AFTER_RESEARCH` ×2；華電2025簡報（英文）含客戶訂單表（台電花東供電區處／超耐熱鋼心鋁線），惟「第一銅」「華新麗華」「銅」「鋁錠」「Copper」「Supplier」皆0次。
- `2347:objective_ranking_or_market_share:8fff79b3fa219000` — `PARTIALLY_SUPPORTED`；聯強2024年報載「**亞太地區主要城市建立數十座智能化的運籌服務中心**」與多品牌採購；惟「亞太第一大」「第一大」皆0次，「440」唯一命中為「440.4」、「30,000」4次均為**酬金級距**。
- `3010:objective_ranking_or_market_share:23e0e98b40b54555` — `PARTIALLY_SUPPORTED`；華立111年報載材料涵蓋半導體35次、綠能14次、工程塑膠5次、PCB 1次、面板1次；惟「高科技材料通路」0次，且「最大」2次為「穩定性最大化」「發揮最大工作潛能」等**非市場地位**用語。
- `3033:objective_ranking_or_market_share:54d8ccbbd3d4f3e1`、`720516a156c7c28d` — `PARTIALLY_SUPPORTED` ×2；威健2021永續報告載「代理之電子零組件包括例如：**AMD**、…、**Infineon**、…、**Microchip**、…、**NXP**、…」（Vishay 6次）；惟「最大代理線」未載（「最大」5次為獎項與泛用語），「CPU」「GPU」皆0次。
- 證據、期間、查閱日期與摘記記錄於 `semantic/author-077.json`（7 筆）。未修改發行人報告。
- Next pending claim by priority: `2450:objective_ranking_or_market_share:d4c4eba514df929a` (神腦).

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
