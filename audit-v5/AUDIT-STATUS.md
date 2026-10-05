# Audit v5 Status

Updated: 2026-10-09 08:04 UTC
Branch: `audit-v5`

## Semantic HIGH review

- HIGH issuers: **836**
- Raw HIGH signals: **1,410**
- Unique HIGH claims: **1,399**
- Author-reviewed: **626 / 1,399**
- Remaining author review: **773**
- Latest batch: **author-104** (8 claims)
- Independent reviews: **0**; author decisions are not final acceptance.

### Existing author decision counts

- `ACCEPTED`: **77**
- `PARTIALLY_SUPPORTED`: **406**
- `UNSUPPORTED`: **1**
- `PERIOD_UNRESOLVED`: **0**
- `SOURCE_UNAVAILABLE`: **3**
- `UNKNOWN_AFTER_RESEARCH`: **139**

## Latest claim batch

- `2423:objective_ranking_or_market_share:89e017344f0a4685`、`ac4c5aacc850ead3`、`598bd6f5b3e719aa` — `UNKNOWN_AFTER_RESEARCH` ×3；固緯三個端點均失敗（gwinstek.co.uk 與 gwinstek.de 之113年報端點皆 **SSL/TLS 憑證信任失敗**；MOPS t100 端點**僅320 bytes**）。
- `3030:objective_ranking_or_market_share:0bce561f06e3e4e6` — `PARTIALLY_SUPPORTED`；德律107年報「**AOI」58 次、「自動光學」12 次**；惟「台灣最大」「國內最大」「名列前茅」皆0次，且「市佔」2次係**營運目標**敘述。
- `3587:objective_ranking_or_market_share:d51886a6ad107637`、`807d8b6094e488c5` — `PARTIALLY_SUPPORTED` ×2；閎康簡報（英文版）載「**Kumamoto (MA)**」「Japan – National Project (Rapidus)」（Kumamoto 4次、Japan 9次）；惟「**TSMC」0 次**、「largest customer」0 次。
- `6516:objective_ranking_or_market_share:ee30bf28283d37f0` — `PARTIALLY_SUPPORTED`；勤崴議事錄「電子地圖」1次；惟「七成」「Google」「市佔」皆0次。
- `8289:objective_ranking_or_market_share:3e8264bf27a8e71f` — `PARTIALLY_SUPPORTED`；泰藝簡報「OCXO」2次、「衛星」4次、「5G」2次；惟「唯一」「恆溫」皆0次。
- 證據、期間、查閱日期與摘記記錄於 `semantic/author-104.json`（8 筆）。未修改發行人報告。
- Next pending claim by priority: `8289:objective_ranking_or_market_share:f64fe0dc9d652473` (泰藝).

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
