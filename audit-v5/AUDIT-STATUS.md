# Audit v5 Status

Updated: 2026-10-11 03:04 UTC
Branch: `audit-v5`

## Semantic HIGH review

- HIGH issuers: **836**
- Raw HIGH signals: **1,410**
- Unique HIGH claims: **1,399**
- Author-reviewed: **846 / 1,399**
- Remaining author review: **553**
- Latest batch: **author-147** (5 claims)
- Independent reviews: **0**; author decisions are not final acceptance.

### Existing author decision counts

- `ACCEPTED`: **87**
- `PARTIALLY_SUPPORTED`: **552**
- `UNSUPPORTED`: **1**
- `PERIOD_UNRESOLVED`: **0**
- `SOURCE_UNAVAILABLE`: **3**
- `UNKNOWN_AFTER_RESEARCH`: **203**

## Latest claim batch

- `6982:objective_ranking_or_market_share:6ce0f1f566a2483c` — `PARTIALLY_SUPPORTED`；大井簡報「**加壓」10 次、「馬達」6 次**；惟「龍頭」「六成」「市佔」「住宅」皆0次，且「60%」2次上下文不足。
- `6982:objective_ranking_or_market_share:d789441c0ced0dea` — `PARTIALLY_SUPPORTED`；同上；「市佔 60%+」未獲支持。
- `7795:objective_ranking_or_market_share:1fece52690003c4d` — `PARTIALLY_SUPPORTED`；長廣年報「**載板」68 次、「壓膜」68 次、「長興」88 次**、「真空」49次、「ABF」35次；惟「95%」「市佔」皆0次。
- `7795:objective_ranking_or_market_share:b856cd136904fdc5` — `PARTIALLY_SUPPORTED`；ABF 載板真空壓膜機業務成立；惟「95%」「醫療」「推桿」皆0次。
- `7795:objective_ranking_or_market_share:c8947ab48156fadc` — `UNKNOWN_AFTER_RESEARCH`；年報「**欣興」「南亞電路板」皆 0 次**。
- 證據、期間、查閱日期與摘記記錄於 `semantic/author-147.json`（5 筆）。未修改發行人報告。
- Next pending claim by priority: `8996:objective_ranking_or_market_share:49ffb2ed084de05d` (高力).

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
