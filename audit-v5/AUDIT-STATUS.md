# Audit v5 Status

Updated: 2026-10-09 09:04 UTC
Branch: `audit-v5`

## Semantic HIGH review

- HIGH issuers: **836**
- Raw HIGH signals: **1,410**
- Unique HIGH claims: **1,399**
- Author-reviewed: **634 / 1,399**
- Remaining author review: **765**
- Latest batch: **author-105** (8 claims)
- Independent reviews: **0**; author decisions are not final acceptance.

### Existing author decision counts

- `ACCEPTED`: **77**
- `PARTIALLY_SUPPORTED`: **411**
- `UNSUPPORTED`: **1**
- `PERIOD_UNRESOLVED`: **0**
- `SOURCE_UNAVAILABLE`: **3**
- `UNKNOWN_AFTER_RESEARCH`: **142**

## Latest claim batch

- `8289:objective_ranking_or_market_share:f64fe0dc9d652473` — `PARTIALLY_SUPPORTED`；泰藝簡報「石英」2次、TCXO 5次、VCXO 3次、OCXO 2次、振盪器8次；惟「諧振器」「唯一」皆0次。
- `5484:objective_ranking_or_market_share:6db0feefd513243e`、`821685f1c25c5b71`、`ce6fd1fdc3f662bb` — `UNKNOWN_AFTER_RESEARCH` ×3；慧友官方下載端點回應 **HTTP 403**。
- `9917:objective_ranking_or_market_share:1cb9babd3bf0854f` — `PARTIALLY_SUPPORTED`；中保科文件載「**1977年11月**」與「與**日本最大的SECOM公司合資技術合作**」（保全390次、SECOM 14次）；惟「最大」14次之上下文為「最大宗整合系統」「美國最大消費性電子展」「全國最大安控教育訓練中心」「SECOM為我方最大股東之一」，**均非**「台灣最大保全集團」。
- `2351:objective_ranking_or_market_share:33136b7be916bb4a`、`f9a2de7507ee264c` — `PARTIALLY_SUPPORTED` ×2；順德簡報「導線架」3次、「功率」2次；惟「全球最大」「前五大」皆0次。
- `2455:objective_ranking_or_market_share:c7875bcac9220f55` — `PARTIALLY_SUPPORTED`；全新年報「砷化鎵」54次、「磊晶」29次、「IQE」3次；惟「全球最大」「領導」皆0次，且「IQE」3次係**同業列舉**（「IQE 等」「IQE、IET-KY」），未載超越之敘述。
- 證據、期間、查閱日期與摘記記錄於 `semantic/author-105.json`（8 筆）。未修改發行人報告。
- Next pending claim by priority: `2455:objective_ranking_or_market_share:0c9b77b516d1cc7d` (全新).

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
