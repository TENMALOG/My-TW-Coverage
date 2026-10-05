# Audit v5 Status

Updated: 2026-10-12 03:04 UTC
Branch: `audit-v5`

## Semantic HIGH review

- HIGH issuers: **836**
- Raw HIGH signals: **1,410**
- Unique HIGH claims: **1,399**
- Author-reviewed: **930 / 1,399**
- Remaining author review: **469**
- Latest batch: **author-171** (6 claims)
- Independent reviews: **0**; author decisions are not final acceptance.

### Existing author decision counts

- `ACCEPTED`: **91**
- `PARTIALLY_SUPPORTED`: **608**
- `UNSUPPORTED`: **1**
- `PERIOD_UNRESOLVED`: **0**
- `SOURCE_UNAVAILABLE`: **3**
- `UNKNOWN_AFTER_RESEARCH`: **227**

## Latest claim batch

- `6977:objective_ranking_or_market_share:578892ccae2b59f4` — `PARTIALLY_SUPPORTED`；聯純資料「**超純水」6 次、「水處理」6 次**；惟「日月光」「矽品」「超豐」「供應鏈」皆0次。
- `6806:objective_ranking_or_market_share:8a5ced4ccef9e61c` — `PARTIALLY_SUPPORTED`；森崴文件「**離岸風電」19 次、「統包」6 次、「EPC」3 次**、「正崴」2次；惟「最大」1次係「太陽能設置量成長幅度最大」，「本土」1次係國產化政策。
- `6869:objective_ranking_or_market_share:e69c35c8ab2af08d` — `PARTIALLY_SUPPORTED`；雲豹年報「**天能綠電」12 次**（取得售電業執照、協助玉山金控綠電轉供）；惟「10億」「160億」「880億」「338%」皆0次，「最大」係指太陽能電廠。
- `6869:objective_ranking_or_market_share:7e2d1e75d0b3577d` — `PARTIALLY_SUPPORTED`；天能綠電售電平台成立；惟「最大民間綠電售電平台」未獲支持。
- `6994:objective_ranking_or_market_share:2ce556a2bce652ca`、`4a494708c5380bf7` — `UNKNOWN_AFTER_RESEARCH` ×2；所取得檔案為**兆聯實業（6944）年報**（「富威」0次），**屬另一法人**，且部分文字層為亂碼。
- 證據、期間、查閱日期與摘記記錄於 `semantic/author-171.json`（6 筆）。未修改發行人報告。
- Next pending claim by priority: `6803:objective_ranking_or_market_share:d6b824ac14940918` (崑鼎).

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
