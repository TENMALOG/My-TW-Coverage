# Audit v5 Status

Updated: 2026-10-09 03:04 UTC
Branch: `audit-v5`

## Semantic HIGH review

- HIGH issuers: **836**
- Raw HIGH signals: **1,410**
- Unique HIGH claims: **1,399**
- Author-reviewed: **591 / 1,399**
- Remaining author review: **808**
- Latest batch: **author-099** (8 claims)
- Independent reviews: **0**; author decisions are not final acceptance.

### Existing author decision counts

- `ACCEPTED`: **76**
- `PARTIALLY_SUPPORTED`: **381**
- `UNSUPPORTED`: **1**
- `PERIOD_UNRESOLVED`: **0**
- `SOURCE_UNAVAILABLE`: **3**
- `UNKNOWN_AFTER_RESEARCH`: **130**

## Latest claim batch

- `6505:objective_ranking_or_market_share:7f3ac62fdb7f42ab` — `PARTIALLY_SUPPORTED`；台塑化112年報載「為**國內唯一之民營石油煉製業者**」，並見六輕13次、麥寮20次；惟「1992」0次（年報以民國年表述）。
- `6505:objective_ranking_or_market_share:e384f6967f7009fd`、`e2932b76fb13de47` — `PARTIALLY_SUPPORTED` ×2；油品與石化事業敘述成立；惟「62%」「54萬」「600座」「24%」「313萬」「最大石化」皆0次，「69%」3次含「15.69%」財務比率而未以市占率表述。
- `7610:objective_ranking_or_market_share:66f0a1d3b55f8053` — `PARTIALLY_SUPPORTED`；聯友114年報載「為**國內唯一**以二次硬質合金物料…**再製生產鎢酸（鈉）**」與「台灣首家也是唯一」；惟「全球最大」0次（**範圍由國內放大為全球**），且「2,500」1次係產業**每年消耗量**（2,000-2,500噸）而非出口量。
- `7610:objective_ranking_or_market_share:8dc2d0884b44a2f2`、`f09b19c3cba50f22`、`0e82075cdeab2da0` — `UNKNOWN_AFTER_RESEARCH` ×3；年報「台積電」「Apple」「Tesla」「Alconix」「合格供應」皆0次。
- `9927:objective_ranking_or_market_share:55726d612dd2b764` — `PARTIALLY_SUPPORTED`；泰銘簡報「鉛合金」1次；惟「亞洲最大」「85%」「市佔」「提煉」皆0次（簡報僅2,338字元、2012年版）。
- 證據、期間、查閱日期與摘記記錄於 `semantic/author-099.json`（8 筆）。未修改發行人報告。
- Next pending claim by priority: `9927:objective_ranking_or_market_share:d1bcdef3b01aa98b` (泰銘).

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
