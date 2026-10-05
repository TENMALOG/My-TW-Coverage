# Audit v5 Status

Updated: 2026-10-09 15:04 UTC
Branch: `audit-v5`

## Semantic HIGH review

- HIGH issuers: **836**
- Raw HIGH signals: **1,410**
- Unique HIGH claims: **1,399**
- Author-reviewed: **668 / 1,399**
- Remaining author review: **731**
- Latest batch: **author-111** (5 claims)
- Independent reviews: **0**; author decisions are not final acceptance.

### Existing author decision counts

- `ACCEPTED`: **77**
- `PARTIALLY_SUPPORTED`: **435**
- `UNSUPPORTED`: **1**
- `PERIOD_UNRESOLVED`: **0**
- `SOURCE_UNAVAILABLE`: **3**
- `UNKNOWN_AFTER_RESEARCH`: **152**

## Latest claim batch

- `2408:objective_ranking_or_market_share:c4377f2679307d07` — `PARTIALLY_SUPPORTED`；南亞科年報「**DRAM」77 次**；惟「台灣最大」「第四大」皆0次。
- `2436:objective_ranking_or_market_share:57909ce03d931541` — `PARTIALLY_SUPPORTED`；偉詮電3Q25簡報「**USB PD」4 次**、「USB」17次、「電源管理」3次、筆電1次、充電器1次；惟「市佔」「遊戲機」皆0次。
- `2449:objective_ranking_or_market_share:fea783f1ad9c465a` — `PARTIALLY_SUPPORTED`；京元電113年報「**測試」108 次**、「封裝」36次、「預燒」7次、「burn-in」9次；惟「台灣最大」0次，且「獨立」137次多為「獨立董事」「IDM委外測試」。
- `2454:objective_ranking_or_market_share:f41e65769c42213b` — `PARTIALLY_SUPPORTED`；聯發科2025年報（**英文版**）「AI」944次、「5G」15次、「market share」7次；惟未見「5G手機晶片市占率位居全球前二」之專述。
- `2454:objective_ranking_or_market_share:5905335fb55488f0` — `PARTIALLY_SUPPORTED`；年報載「tape out of its flagship SoC using **TSMC's 2nm process**」（TSMC 7次、foundry 4次）；惟「**largest supplier」0 次**。
- 證據、期間、查閱日期與摘記記錄於 `semantic/author-111.json`（5 筆）。未修改發行人報告。
- Next pending claim by priority: `2458:objective_ranking_or_market_share:16cff6fcb439c815` (義隆).

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
