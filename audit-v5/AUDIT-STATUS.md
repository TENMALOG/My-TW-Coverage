# Audit v5 Status

Updated: 2026-10-12 08:04 UTC
Branch: `audit-v5`

## Semantic HIGH review

- HIGH issuers: **836**
- Raw HIGH signals: **1,410**
- Unique HIGH claims: **1,399**
- Author-reviewed: **951 / 1,399**
- Remaining author review: **448**
- Latest batch: **author-176** (6 claims)
- Independent reviews: **0**; author decisions are not final acceptance.

### Existing author decision counts

- `ACCEPTED`: **92**
- `PARTIALLY_SUPPORTED`: **622**
- `UNSUPPORTED`: **1**
- `PERIOD_UNRESOLVED`: **0**
- `SOURCE_UNAVAILABLE`: **3**
- `UNKNOWN_AFTER_RESEARCH`: **233**

## Latest claim batch

- `4541:material_named_relationship:2ab6d5fc7471158f` — `PARTIALLY_SUPPORTED`；晟田簡報「**漢翔」11 次、「Boeing」11 次、「Airbus」9 次、「GE」57 次、「起落架」7 次**、「SPP」4次、「MOOG」4次；惟「**三菱重工」0 次**、「75%」0次。
- `4541:material_named_relationship:df473dfcdc3e30d8` — `PARTIALLY_SUPPORTED`；「食品」3次、「10%」1次；惟「三菱重工」0次。
- `4541:material_named_relationship:bcf536822f52729b` — `PARTIALLY_SUPPORTED`；「漢翔」11次、「41%」1次、「Boeing」11次、「Airbus」9次**均有出現**，惟簡報文字層多為孤立詞組，**「41%」與「漢翔」之連結無法確認**。
- `4572:material_named_relationship:b06442b0f8987e25` — `PARTIALLY_SUPPORTED`；駐龍簡報「Boeing」6次、「認證」5次；惟「**三家」0 次、「全製程」0 次**。
- `4572:material_named_relationship:425087302d080000` — `PARTIALLY_SUPPORTED`；「**737」3 次、「777」3 次、「787」2 次**、「Spirit」6次、「Safran」4次；惟「漢翔」「Tier」皆0次。
- `8222:material_named_relationship:710cbe41e0f8945e` — `PARTIALLY_SUPPORTED`；寶一年報「**Safran」27 次、「Pratt」10 次、「Tier」11 次**、「MTU」2次；惟「**川崎」0 次、「GE Avio」0 次**、「波蘭」0次。
- 證據、期間、查閱日期與摘記記錄於 `semantic/author-176.json`（6 筆）。未修改發行人報告。
- Next pending claim by priority: `6508:export_concentration:d679e0352a3e6a29` (惠光).

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
