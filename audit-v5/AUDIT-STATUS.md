# Audit v5 Status

Updated: 2026-10-10 05:04 UTC
Branch: `audit-v5`

## Semantic HIGH review

- HIGH issuers: **836**
- Raw HIGH signals: **1,410**
- Unique HIGH claims: **1,399**
- Author-reviewed: **754 / 1,399**
- Remaining author review: **645**
- Latest batch: **author-125** (5 claims)
- Independent reviews: **0**; author decisions are not final acceptance.

### Existing author decision counts

- `ACCEPTED`: **83**
- `PARTIALLY_SUPPORTED`: **489**
- `UNSUPPORTED`: **1**
- `PERIOD_UNRESOLVED`: **0**
- `SOURCE_UNAVAILABLE`: **3**
- `UNKNOWN_AFTER_RESEARCH`: **178**

## Latest claim batch

- `6462:objective_ranking_or_market_share:d15da7bf0a3e513d` — `UNKNOWN_AFTER_RESEARCH`；神盾議事手冊「指紋」25次，惟「三星」「Samsung」「起亞」「KIA」「CSP」「IP驗證」皆0次，且「市占」2次皆為**目標敘述**。
- `6690:objective_ranking_or_market_share:2ca855b26577abb8` — `PARTIALLY_SUPPORTED`；安碁文件「**宏碁」92 次**、「SOC」61次、「委外」3次；惟「台灣最大」0次，「領導」2次為「領導能力」與「技術領導廠商」。
- `6690:objective_ranking_or_market_share:e280e76cce489447` — `UNKNOWN_AFTER_RESEARCH`；「市佔」「六成」「45%」「40%」皆0次；「**300」20 次多為財務數字**（300,000／300,500 仟元）。
- `6763:objective_ranking_or_market_share:66e5afa9447c9ff4` — `PARTIALLY_SUPPORTED`；綠界年報「第三方支付」26次、「信用卡」37次；惟「市占」1次為目標敘述，「**最大」8 次多為泛用語**（最大的潛能／最大限度／最大值）。
- `6878:objective_ranking_or_market_share:ac1050bc146ee810` — `PARTIALLY_SUPPORTED`；歐付寶議事手冊「電子支付」19次、「專營」4次；惟「綠界」「第一家」「執照」「2015」皆0次。
- 證據、期間、查閱日期與摘記記錄於 `semantic/author-125.json`（5 筆）。未修改發行人報告。
- Next pending claim by priority: `6925:objective_ranking_or_market_share:f4539b5294dcb0a4` (意藍).

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
