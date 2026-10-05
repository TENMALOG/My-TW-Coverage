# Audit v5 Status

Updated: 2026-10-09 07:04 UTC
Branch: `audit-v5`

## Semantic HIGH review

- HIGH issuers: **836**
- Raw HIGH signals: **1,410**
- Unique HIGH claims: **1,399**
- Author-reviewed: **618 / 1,399**
- Remaining author review: **781**
- Latest batch: **author-103** (7 claims)
- Independent reviews: **0**; author decisions are not final acceptance.

### Existing author decision counts

- `ACCEPTED`: **77**
- `PARTIALLY_SUPPORTED`: **401**
- `UNSUPPORTED`: **1**
- `PERIOD_UNRESOLVED`: **0**
- `SOURCE_UNAVAILABLE`: **3**
- `UNKNOWN_AFTER_RESEARCH`: **136**

## Latest claim batch

- `2923:objective_ranking_or_market_share:2deccd89094eaab3` — `PARTIALLY_SUPPORTED`；鼎固文件「日月光」59次（母子集團關係）；惟「全球最大」「封測」皆0次。
- `3489:objective_ranking_or_market_share:6f1e5cdcedde4c99` — `PARTIALLY_SUPPORTED`；森寶2025簡報「森碁」2次、「營造」3次、「100%」2次；惟「一條龍」「垂直整合」皆0次。
- `9940:objective_ranking_or_market_share:103ba9aa17da7009` — `PARTIALLY_SUPPORTED`；信義2025簡報載「2024年10月店數為**464家直營分店**」；惟「1987」「最大」皆0次，且claim之「超過500間」**與官方所載464家不符**。
- `8478:objective_ranking_or_market_share:1d158029ffa49cb9` — `PARTIALLY_SUPPORTED`；東哥2026簡報之來源身分成立；惟「亞洲最大」「全球第三」「Ocean」皆0次。
- `8478:objective_ranking_or_market_share:28a1bcd15fe9985b`、`803bb81e8eda9129` — `UNKNOWN_AFTER_RESEARCH` ×2；簡報「MarineMax」0次，且「50%」5次分別為「產能+50%」「回購率50%+」等，**非經銷商營收占比**。
- `2360:objective_ranking_or_market_share:1e49821a8cff17a7` — `PARTIALLY_SUPPORTED`；致茂114年報「量測」44次、「自動化測試」6次；惟「亞洲最大」「1984」皆0次（**封面頁文字層亂碼**）。
- 證據、期間、查閱日期與摘記記錄於 `semantic/author-103.json`（7 筆）。未修改發行人報告。
- Next pending claim by priority: `2423:objective_ranking_or_market_share:89e017344f0a4685` (固緯).

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
