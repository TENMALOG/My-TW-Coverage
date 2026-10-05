# Audit v5 Status

Updated: 2026-10-07 15:04 UTC
Branch: `audit-v5`

## Semantic HIGH review

- HIGH issuers: **836**
- Raw HIGH signals: **1,410**
- Unique HIGH claims: **1,399**
- Author-reviewed: **352 / 1,399**
- Remaining author review: **1,047**
- Latest batch: **author-063** (6 claims)
- Independent reviews: **0**; author decisions are not final acceptance.

### Existing author decision counts

- `ACCEPTED`: **63**
- `PARTIALLY_SUPPORTED`: **221**
- `UNSUPPORTED`: **1**
- `PERIOD_UNRESOLVED`: **0**
- `SOURCE_UNAVAILABLE`: **3**
- `UNKNOWN_AFTER_RESEARCH`: **64**

## Latest claim batch

- `3152:objective_ranking_or_market_share:57faf7aa307b7942` — `PARTIALLY_SUPPORTED`; 璟德議事錄載「**璟德為國內首家專注於高頻整合元件與模組的設計及製造公司**」與 LTCC 天線模組開發；惟「台灣最大」0次（官方為「國內首家」，指時間非規模）、「全球前三大」0次。
- `3217:objective_ranking_or_market_share:2f5f1672a80405d9` — `PARTIALLY_SUPPORTED`; 優群簡報載「DDR4/5 SO-DIMM 系列…**市占No.1**」；惟「50%」1次係「2020年起DDR與M.2在全球筆電市占率超越50%」（規格滲透率，非其自身市占）。
- `3305:objective_ranking_or_market_share:e2ce4b02cefa7379` — `PARTIALLY_SUPPORTED`; 昇貿簡報載銲錫製品之生產銷售與越南、馬來西亞子公司；惟「台灣第一」「全球前三」「千住」「Alpha」皆0次。
- `3311:objective_ranking_or_market_share:50321d8ad4f59f0e` — `PARTIALLY_SUPPORTED`; 閎暉簡報「穿戴」2次；惟「手機」「按鍵」「車用」「全球最大」「轉型」皆0次。
- `3362:objective_ranking_or_market_share:0d1f1f055061087b`、`0734bd9829977ceb` — `PARTIALLY_SUPPORTED` ×2; 先進光股東會手冊「鏡頭」28次；惟「NB」「筆電」「市佔」「70%」「龍頭」皆0次。
- 證據、期間、查閱日期與摘記記錄於 `semantic/author-063.json`（6 筆）。未修改發行人報告。
- 里程碑：已審 **352 / 1,399（25.2%）**，突破四分之一。
- Next pending claim by priority: `3441:objective_ranking_or_market_share:8b98c062556b5eb7` (聯一光).

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
