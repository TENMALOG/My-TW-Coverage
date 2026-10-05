# Audit v5 Status

Updated: 2026-10-15 02:04 UTC
Branch: `audit-v5`

## Semantic HIGH review

- HIGH issuers: **836**
- Raw HIGH signals: **1,410**
- Unique HIGH claims: **1,399**
- Author-reviewed: **1,241 / 1,399**
- Remaining author review: **158**
- Latest batch: **author-242** (6 claims)
- Independent reviews: **0**; author decisions are not final acceptance.

### Existing author decision counts

- `ACCEPTED`: **103**
- `PARTIALLY_SUPPORTED`: **767**
- `UNSUPPORTED`: **2**
- `PERIOD_UNRESOLVED`: **0**
- `SOURCE_UNAVAILABLE`: **3**
- `UNKNOWN_AFTER_RESEARCH`: **366**

## Latest claim batch

- `2816:identity_changing_event:00fd24fba693ef88` — `PARTIALLY_SUPPORTED`；旺旺保年報**逐字載**「一、**設立日期：民國52 年2 月20 日**」與「同時通過公司**更名**為『**旺旺友聯產物**』」（**民國52年＝1963年**）；**惟「98年」1 次之上下文實為「98年金融危機」，並非2009年旺旺入主**（「2009」0次）。
- `6616:material_named_relationship:ef25aff8ea336307` — `PARTIALLY_SUPPORTED`；特昇手冊載「開發新的**寢室家具**系列」「拆裝式家具（**RTA**）」「針對**美洲**及網購市場」；**惟「OEM／五件式／臥室／木製」皆 0 次**。
- `6807:material_named_relationship:de5168ab462b6ac1` — `UNKNOWN_AFTER_RESEARCH`；峰源年報「**Williams-Sonoma／Costco／好市多」皆 0 次**。
- `6536:material_named_relationship:b33368d8bd4f0fc9` — `UNKNOWN_AFTER_RESEARCH`；碩豐文件為**個體財務報告**，「**Tigre／水晶老虎／海參崴」皆 0 次**。
- `6629:a2257218a3ef35d5`、`2881:eaafe360917c05ea` — `UNKNOWN_AFTER_RESEARCH` ×2；泰金-KY與富邦金端點 **HTTP 404**。
- 證據記錄於 `semantic/author-242.json`（6 筆）。未修改發行人報告。帳目一致：唯一 claim 數 1,241 ＝ 條目總數 1,241。
- Next pending claim by priority: `5859:identity_changing_event:3146527b074efe1a` (遠壽).

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
