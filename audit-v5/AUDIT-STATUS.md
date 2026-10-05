# Audit v5 Status

Updated: 2026-10-06 09:04 UTC
Branch: `audit-v5`

## Semantic HIGH review

- HIGH issuers: **836**
- Raw HIGH signals: **1,410**
- Unique HIGH claims: **1,399**
- Author-reviewed: **164 / 1,399**
- Remaining author review: **1,235**
- Latest batch: **author-033** (8 claims)
- Independent reviews: **0**; author decisions are not final acceptance.

### Existing author decision counts

- `ACCEPTED`: **40**
- `PARTIALLY_SUPPORTED`: **103**
- `UNSUPPORTED`: **1**
- `PERIOD_UNRESOLVED`: **0**
- `SOURCE_UNAVAILABLE`: **3**
- `UNKNOWN_AFTER_RESEARCH`: **17**

## Latest claim batch

- `2855:objective_ranking_or_market_share:23dcc1ae4b2739ba` — `PARTIALLY_SUPPORTED`; 統一證111年報第324/87頁載「證券經紀市佔率為2.82%，市佔排名為國內本土券商中第11名」（非前十），另載單點平均市佔率0.09%在前十大本土券商第5名；第101頁載電子下單108年為79.37%。
- `2889:objective_ranking_or_market_share:9f8aba6960121ca6` — `PARTIALLY_SUPPORTED`; 國票金永續報告第15/17頁載2002年3月26日由國際票券、協和證券及大東綜合證券設立；惟「唯一以票券業務為核心」之「唯一」未獲支持。
- `6005:objective_ranking_or_market_share:083b365bd1c581fa` — `PARTIALLY_SUPPORTED`; 群益證簡報第16頁經紀市佔3.71%排名9（2025）、第22頁3.53%排名8（2026年1-2月），與「約4%」相符；惟官方排名為第8～9名而非「第六」。
- `6005:objective_ranking_or_market_share:5130bfc55573a836` — `PARTIALLY_SUPPORTED`; 市占約4%相符；惟據點數與客戶結構未載。
- `6023:objective_ranking_or_market_share:cec62e122390ab9a` — `PARTIALLY_SUPPORTED`; 元大期113年報第9頁載期貨經紀市占22.62%、客戶保證金占全市場32.89%「市場存量第一」、稅後淨利21.67億「位居14家專營期貨商之首」；惟資本額與淨值「第一」未載。
- `6026:objective_ranking_or_market_share:f276a5441599570d` — `PARTIALLY_SUPPORTED`; 福邦證113年報第89頁載「以投資銀行業務為核心…聚焦耕耘中型及中小企業客戶」；惟「中小型企業的全方位策略夥伴」字樣未出現。
- `1313:objective_ranking_or_market_share:f7e881e9038a20ac` — `PARTIALLY_SUPPORTED`; 聯成2025簡報第5/7頁載「全球最大苯酐及可塑劑製造商」；惟「大中華區30%」出自2020簡報，2025簡報第17頁載中國大陸可塑劑市占約23%。
- `1313:objective_ranking_or_market_share:440a3c16130704da` — `PARTIALLY_SUPPORTED`; 全球最大成立；惟「龍頭」（0次）、「一站式垂直海運物流競爭壁壘」與集團隸屬陳述未獲支持。
- 證據、期間、查閱日期與摘記記錄於 `semantic/author-033.json`。未修改發行人報告。
- Next pending claim by priority: `1326:objective_ranking_or_market_share:9a1e08d41d3aa67e` (台化).

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
