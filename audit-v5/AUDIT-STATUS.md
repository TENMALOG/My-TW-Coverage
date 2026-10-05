# Audit v5 Status

Updated: 2026-10-15 04:04 UTC
Branch: `audit-v5`

## Semantic HIGH review

- HIGH issuers: **836**
- Raw HIGH signals: **1,410**
- Unique HIGH claims: **1,399**
- Author-reviewed: **1,254 / 1,399**
- Remaining author review: **145**
- Latest batch: **author-244** (6 claims)
- Independent reviews: **0**; author decisions are not final acceptance.

### Existing author decision counts

- `ACCEPTED`: **103**
- `PARTIALLY_SUPPORTED`: **774**
- `UNSUPPORTED`: **2**
- `PERIOD_UNRESOLVED`: **0**
- `SOURCE_UNAVAILABLE`: **3**
- `UNKNOWN_AFTER_RESEARCH`: **372**

## Latest claim batch

- `8924:material_named_relationship:737bd19f1360d702` — `PARTIALLY_SUPPORTED`；大田年報載「是高爾夫及自行車國際知名品牌的重要供應商」（**高爾夫 250 次、自行車 114 次、Callaway 1 次**）；**惟「TaylorMade」0 次**。
- `8938:material_named_relationship:7f702e5df65e7ef6` — `PARTIALLY_SUPPORTED`；明安年報載「高爾夫球頭…**碳纖維**布、**自行車碳纖維**零組件…複合材料之專業製造公司」（**碳纖維 53 次、自行車 31 次**）；**惟「Toray／東麗／碳纖維紗」皆 0 次**。
- `2724:identity_changing_event:f0208bc4004081cd` — `PARTIALLY_SUPPORTED`；藝舍簡報「**立信」13 次、「賴運興」1 次、「建設」2 次**；**惟「入主」與「更名／2023」皆 0 次**。
- `6655:material_named_relationship:44b32eca6d1374f8`、`e43d28680738ba3b` — `PARTIALLY_SUPPORTED` ×2；科定簡報「**FSC」1 次**；**惟「原木／木皮／北美／歐洲」皆 0 次**（**該簡報為英文版**）。
- `8933:export_concentration:d68998658367f462` — `UNKNOWN_AFTER_RESEARCH`；愛地雅端點 **HTTP 404**。
- 證據記錄於 `semantic/author-244.json`（6 筆）。未修改發行人報告。帳目一致：唯一 claim 數 1,254 ＝ 條目總數 1,254。
- Next pending claim by priority: `5608:material_named_relationship:1a2dfe39ec2a2efd` (四維航).

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
