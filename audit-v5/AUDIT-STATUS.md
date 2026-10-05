# Audit v5 Status

Updated: 2026-10-08 23:04 UTC
Branch: `audit-v5`

## Semantic HIGH review

- HIGH issuers: **836**
- Raw HIGH signals: **1,410**
- Unique HIGH claims: **1,399**
- Author-reviewed: **564 / 1,399**
- Remaining author review: **835**
- Latest batch: **author-095** (8 claims)
- Independent reviews: **0**; author decisions are not final acceptance.

### Existing author decision counts

- `ACCEPTED`: **75**
- `PARTIALLY_SUPPORTED`: **370**
- `UNSUPPORTED`: **1**
- `PERIOD_UNRESOLVED`: **0**
- `SOURCE_UNAVAILABLE`: **3**
- `UNKNOWN_AFTER_RESEARCH`: **115**

## Latest claim batch

- `6670:objective_ranking_or_market_share:0b9c48bd7d884e3f` — `PARTIALLY_SUPPORTED`；復盛2022永續報告載「為**全球最大之高爾夫球桿頭生產據點**」與「復盛應用身為**全球最大之高爾夫球桿頭製造商**」（全球最大2次、桿頭24次）；惟「五成」「市占」皆0次，且「50%」1次係**供應商季度考核之D類佔比**。
- `8467:objective_ranking_or_market_share:48dd1d22ba83c457` — `PARTIALLY_SUPPORTED`；波力111年報載「A公司是目前**全球最大曲棍球品牌**」與「**全球市占率自2005年8%穩定成長至50%**」，並具名「與主要客戶 **Bauer Hockey** 合作逾十年」；惟官方為「成長**至**50%」而非「超過50%」，且未以「高階」界定。
- `8467:objective_ranking_or_market_share:9a6071b2054ff71b`、`5b5b16a8a12e4d56` — `PARTIALLY_SUPPORTED` ×2；代工關係與「頭盔」2次成立；惟「**最大客戶**」0次（官方僅稱「主要客戶」）。
- `9914:objective_ranking_or_market_share:6f51a2c9276ae36b`、`f9ee3f3ed9072675` — `PARTIALLY_SUPPORTED` ×2；美利達2025簡報載「**歐洲是主要市場**」（歐洲4次）；惟「**最大市場**」0次。
- `9921:objective_ranking_or_market_share:53af3876a9921e62`、`c46e30a478d1a6f2` — `UNKNOWN_AFTER_RESEARCH` ×2；巨大三個官方端點（109年報、112年報、MOPS 2024簡報）**均回應HTTP 404**。
- 證據、期間、查閱日期與摘記記錄於 `semantic/author-095.json`（8 筆）。未修改發行人報告。
- Next pending claim by priority: `6655:objective_ranking_or_market_share:0f29d3a1cca9dfcd` (科定).

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
