# Audit v5 Status

Updated: 2026-10-08 12:04 UTC
Branch: `audit-v5`

## Semantic HIGH review

- HIGH issuers: **836**
- Raw HIGH signals: **1,410**
- Unique HIGH claims: **1,399**
- Author-reviewed: **482 / 1,399**
- Remaining author review: **917**
- Latest batch: **author-084** (6 claims)
- Independent reviews: **0**; author decisions are not final acceptance.

### Existing author decision counts

- `ACCEPTED`: **71**
- `PARTIALLY_SUPPORTED`: **320**
- `UNSUPPORTED`: **1**
- `PERIOD_UNRESOLVED`: **0**
- `SOURCE_UNAVAILABLE`: **3**
- `UNKNOWN_AFTER_RESEARCH`: **87**

## Latest claim batch

- `9910:objective_ranking_or_market_share:d6ba6478547062ad` — `PARTIALLY_SUPPORTED`；豐泰永續報告載其為「主要客戶 **Nike 最資深之製鞋合作夥伴**」；惟「85%」「六分之一」「氣墊」皆0次。
- `1558:objective_ranking_or_market_share:87cc034abe16d845` — `PARTIALLY_SUPPORTED`；伸興2022年報載同業／客戶群含「**SVP集團**、日本JANOME、日本BROTHER…」（SVP 2次）；惟「1968」「全球最大」皆0次，且「30%」4次為**獨董比率與持股分級**。
- `1558:objective_ranking_or_market_share:c93aec6e76435d1b`、`0fd3b72d834f9729` — `PARTIALLY_SUPPORTED` ×2；SVP集團之產業關聯成立；惟「最大客戶」「七成」與「全球市佔第一」皆0次。
- `1558:objective_ranking_or_market_share:01444720c98b05b0` — `PARTIALLY_SUPPORTED`；年報「越南」49次、「越南廠」3次；惟「全球最大」0次，且「90%」唯一命中為「**-46.90%**」財務變動比例。
- `1626:objective_ranking_or_market_share:2a014c4508c270a2` — `PARTIALLY_SUPPORTED`；艾美特2023簡報載「**Electric heater ranked #1**」與「**Household fan ranked as #2 in China**」；惟電風扇之排名範圍明確為**中國**而非claim所述之「全球」，「美的集團」與「No.1」未出現。
- 證據、期間、查閱日期與摘記記錄於 `semantic/author-084.json`（6 筆）。未修改發行人報告。
- Next pending claim by priority: `1810:objective_ranking_or_market_share:51ab5ce5d9716cb5` (和成).

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
