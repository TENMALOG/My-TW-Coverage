# Audit v5 Status

Updated: 2026-10-09 00:04 UTC
Branch: `audit-v5`

## Semantic HIGH review

- HIGH issuers: **836**
- Raw HIGH signals: **1,410**
- Unique HIGH claims: **1,399**
- Author-reviewed: **572 / 1,399**
- Remaining author review: **827**
- Latest batch: **author-096** (8 claims)
- Independent reviews: **0**; author decisions are not final acceptance.

### Existing author decision counts

- `ACCEPTED`: **76**
- `PARTIALLY_SUPPORTED`: **372**
- `UNSUPPORTED`: **1**
- `PERIOD_UNRESOLVED`: **0**
- `SOURCE_UNAVAILABLE`: **3**
- `UNKNOWN_AFTER_RESEARCH`: **120**

## Latest claim batch

- `6655:objective_ranking_or_market_share:0f29d3a1cca9dfcd` — `ACCEPTED`；科定簡報載「生產總部：**嘉義縣大林鎮大埔美園區五路10號**」與「2. **業界唯一，產銷一條龍垂直整合**」——兩項逐項對應。
- `6655:objective_ranking_or_market_share:055a6afbd23947d4`、`ccaa6c4b5d8549e4` — `UNKNOWN_AFTER_RESEARCH` ×2；簡報「大日本印刷」「DNP」「ECO」「PP」「EB」「食品級」皆0次。
- `8444:objective_ranking_or_market_share:1ba76f09f75f204f` — `PARTIALLY_SUPPORTED`；綠河簡報「塑合板」37次、「泰國」4次；惟「亞洲最大」1次之上下文為「（燃）煤發電廠(南韓也是**亞洲最大**木質顆（粒）)」之**產業敘述**，非該公司地位。
- `2603:objective_ranking_or_market_share:c49229ece3415b49` — `PARTIALLY_SUPPORTED`；長榮簡報載「**7th 全球船隊運能排名**」「船隊運能市佔率 5.8%」→ 全球前十大成立；惟「1968」「台灣最大」皆0次。
- `2637:objective_ranking_or_market_share:c179a03f49adb48f` — `UNKNOWN_AFTER_RESEARCH`；慧洋2025年報端點回應 **HTTP 404**。
- `8367:objective_ranking_or_market_share:654fe06c1da29251`、`50a32e6e94716675` — `UNKNOWN_AFTER_RESEARCH` ×2；建新簡報檔案**僅690 bytes**（擷取1字元），顯非完整文件。
- 證據、期間、查閱日期與摘記記錄於 `semantic/author-096.json`（8 筆）。未修改發行人報告。
- Next pending claim by priority: `1343:objective_ranking_or_market_share:f0a65b719a264687` (旭東環保).

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
