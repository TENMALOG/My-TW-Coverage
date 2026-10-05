# Audit v5 Status

Updated: 2026-10-10 14:04 UTC
Branch: `audit-v5`

## Semantic HIGH review

- HIGH issuers: **836**
- Raw HIGH signals: **1,410**
- Unique HIGH claims: **1,399**
- Author-reviewed: **791 / 1,399**
- Remaining author review: **608**
- Latest batch: **author-134** (5 claims)
- Independent reviews: **0**; author decisions are not final acceptance.

### Existing author decision counts

- `ACCEPTED`: **86**
- `PARTIALLY_SUPPORTED`: **517**
- `UNSUPPORTED`: **1**
- `PERIOD_UNRESOLVED`: **0**
- `SOURCE_UNAVAILABLE`: **3**
- `UNKNOWN_AFTER_RESEARCH`: **184**

## Latest claim batch

- `4754:objective_ranking_or_market_share:a2cc9eca34a71824` — `PARTIALLY_SUPPORTED`；國碳科105年報「**防火」81 次**、「UL」4次、「FM」3次；惟「亞洲唯一」「唯一」「雙認證」皆0次。
- `4763:objective_ranking_or_market_share:86c143e3b1fdeacf` — `PARTIALLY_SUPPORTED`；材料-KY簡報「**絲束」25 次**並列同業「Celanese、Eastman、Solvay及Daicel」；惟「38%」「25%」「19%」「15%」未見，且「**2%」6 次為「27.2%」「71.12%」之子字串**。
- `4766:objective_ranking_or_market_share:37f70358d3db2a81` — `PARTIALLY_SUPPORTED`；南寶簡報逐字載「**我們是世界第一的運動鞋用接著劑**」（接著劑26次、鞋用6次）；惟「市佔」2次皆為目標敘述，「**50%」6 次皆非 Tier-1 品牌市佔**（2030減碳50%／工會比例50%）。
- `4772:objective_ranking_or_market_share:2d583dbd82c12ed3`、`3e71412bc838ad92` — `PARTIALLY_SUPPORTED` ×2；台特化文件「**半導體」30 次**；惟「中美晶」「大立光」「環球晶圓」「最大股東」「30%」皆0次。
- 證據、期間、查閱日期與摘記記錄於 `semantic/author-134.json`（5 筆）。未修改發行人報告。
- Next pending claim by priority: `6434:objective_ranking_or_market_share:4cdefa173c0d7b8e` (達輝光電).

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
