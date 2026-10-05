# Audit v5 Status

Updated: 2026-10-06 10:04 UTC
Branch: `audit-v5`

## Semantic HIGH review

- HIGH issuers: **836**
- Raw HIGH signals: **1,410**
- Unique HIGH claims: **1,399**
- Author-reviewed: **172 / 1,399**
- Remaining author review: **1,227**
- Latest batch: **author-034** (8 claims)
- Independent reviews: **0**; author decisions are not final acceptance.

### Existing author decision counts

- `ACCEPTED`: **40**
- `PARTIALLY_SUPPORTED`: **110**
- `UNSUPPORTED`: **1**
- `PERIOD_UNRESOLVED`: **0**
- `SOURCE_UNAVAILABLE`: **3**
- `UNKNOWN_AFTER_RESEARCH`: **18**

## Latest claim batch

- `1326:objective_ranking_or_market_share:9a1e08d41d3aa67e` — `PARTIALLY_SUPPORTED`; 台化2017法說會第4頁載「全球第2大SM」、「全球第3大ABS／苯酚」、「全球第7大芳香烴／PTA／PC」，第5頁沿革支持尼龍／嫘縈／PS／ABS／PP／PC 垂直整合；惟官方未以「台灣最大」描述該四項產品。
- `1326:objective_ranking_or_market_share:f1c330ef2220ac46` — `PARTIALLY_SUPPORTED`; 全球排名支持其領先地位；惟「台塑集團四大核心旗艦成員」與「全台產能最大」字樣未載。
- `1326:objective_ranking_or_market_share:ab200ad4f1ede1d8` — `UNKNOWN_AFTER_RESEARCH`; 台化簡報第6頁僅列投資架構，全份未載原料供應來源或台塑化為其供料中心。
- `1708:objective_ranking_or_market_share:1769e438bc571e76` — `PARTIALLY_SUPPORTED`; 東鹼2025英文年報載主要產品線 Potassium sulfate 與 Soda ash，並列 Liquid calcium chloride、Hydrochloric Acid、Baking Soda；惟「the only」出現0次，「唯一」未獲支持。
- `1714:objective_ranking_or_market_share:849ab16abec60b83` — `PARTIALLY_SUPPORTED`; 和桐110年報第10頁載「作為世界界面活性劑原料工業的龍頭企業」；惟「亞洲最大」0次、正烷屬烴「龍頭」未載。
- `1714:objective_ranking_or_market_share:adfae1c40f1b5b8e` — `PARTIALLY_SUPPORTED`; 年報載「主要生產原料－煤油均係向台灣中油股份有限公司購入」；惟「純苯」出現0次。
- `1714:objective_ranking_or_market_share:1ec145cda72231d8` — `PARTIALLY_SUPPORTED`; 兩岸 LAB/NP 佈局 supported；「全亞洲產量最大」「絕對規模經濟與定價優勢」未載。
- `1714:objective_ranking_or_market_share:54021868aa7d2922` — `PARTIALLY_SUPPORTED`; 年報第21頁載「供給下游清潔劑產品製造商如P&G、Unilever等」；惟花王／獅王0次、市佔數字未載。
- 證據、期間、查閱日期與摘記記錄於 `semantic/author-034.json`。未修改發行人報告。
- Next pending claim by priority: `1723:objective_ranking_or_market_share:b3cf265f3bf03e83` (中碳).

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
