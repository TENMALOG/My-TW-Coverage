# Audit v5 Status

Updated: 2026-10-08 19:04 UTC
Branch: `audit-v5`

## Semantic HIGH review

- HIGH issuers: **836**
- Raw HIGH signals: **1,410**
- Unique HIGH claims: **1,399**
- Author-reviewed: **535 / 1,399**
- Remaining author review: **864**
- Latest batch: **author-091** (8 claims)
- Independent reviews: **0**; author decisions are not final acceptance.

### Existing author decision counts

- `ACCEPTED`: **74**
- `PARTIALLY_SUPPORTED`: **351**
- `UNSUPPORTED`: **1**
- `PERIOD_UNRESOLVED`: **0**
- `SOURCE_UNAVAILABLE`: **3**
- `UNKNOWN_AFTER_RESEARCH`: **106**

## Latest claim batch

- `2852:objective_ranking_or_market_share:4a5ef4fd4fdcb9d2` — `PARTIALLY_SUPPORTED`；第一保2025簡報載「**設立日期 1962年**」與股東結構（個人57.14%、金融機構1.15%）；惟「第一金」0次，「與第一金控無直接股權隸屬關係」未獲來源陳述。
- `2852:objective_ranking_or_market_share:a9cea9f32089f2c8`、`0ed2489ebb872b77`、`d1acd16b4de6e7eb` — `UNKNOWN_AFTER_RESEARCH` ×3；簡報「第一銀行」「銀保」「銀行保險」「車商」「保險經紀人」皆0次。
- `2852:objective_ranking_or_market_share:fb910ccfdc42b585` — `PARTIALLY_SUPPORTED`；簡報業務概況呈現簽單保費與業務結構（汽車任意險48.94%、火災保險20.00%等）；惟職能區分敘述未見。
- `2851:objective_ranking_or_market_share:f4428cbe7406c75a` — `ACCEPTED`；中再保50周年特刊載「**民國57年10月31日正式成立**」「於**民國91年**…自此本公司**轉換為民營公司**」「**長榮集團為本公司之最大股東，持股比率為58.68%**」——三項逐項對應（特刊以西元1968／2002檢索均0次）。
- `2851:objective_ranking_or_market_share:5019a1f91c5268c9` — `PARTIALLY_SUPPORTED`；特刊載「為**國內唯一的本土專業再保險公司**」；惟「寡占」「市占」皆0次。
- `2851:objective_ranking_or_market_share:31637d692bd9234c` — `PARTIALLY_SUPPORTED`；特刊載財產再保險與人身再保險業務發展；惟「市占」0次，且「18.8」「19.4」之上下文為**未標示名稱之數字表格**。
- 證據、期間、查閱日期與摘記記錄於 `semantic/author-091.json`（8 筆）。未修改發行人報告。
- Next pending claim by priority: `5878:objective_ranking_or_market_share:ac33ab82c59a8a20` (台名).

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
