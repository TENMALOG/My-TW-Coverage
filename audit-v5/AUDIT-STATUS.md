# Audit v5 Status

Updated: 2026-10-15 00:04 UTC
Branch: `audit-v5`

## Semantic HIGH review

- HIGH issuers: **836**
- Raw HIGH signals: **1,410**
- Unique HIGH claims: **1,399**
- Author-reviewed: **1,228 / 1,399**
- Remaining author review: **171**
- Latest batch: **author-240** (6 claims)
- Independent reviews: **0**; author decisions are not final acceptance.

### Existing author decision counts

- `ACCEPTED`: **103**
- `PARTIALLY_SUPPORTED`: **762**
- `UNSUPPORTED`: **2**
- `PERIOD_UNRESOLVED`: **0**
- `SOURCE_UNAVAILABLE`: **3**
- `UNKNOWN_AFTER_RESEARCH`: **358**

## Latest claim batch

- `2404:material_named_relationship:c9fafe0c318e0dc0` — `PARTIALLY_SUPPORTED`；漢唐簡報「**台積電」15 次、「Micron」10 次、「新加坡」4 次**（ESG亦同）；**惟「ASML」0 次**。
- `5536:material_named_relationship:77eb22555b4e78ed` — `PARTIALLY_SUPPORTED`；聖暉年報**逐字載**「歷年來承攬**矽品、日月光、台積電**、台達電及台灣康寧等知名（廠商）」（台積電2次、日月光1次、**無塵室 42 次、機電 66 次**）；**惟「核心客戶」之排序性表述未見**。
- `9945:material_named_relationship:62688d7d62c26d93` — `UNKNOWN_AFTER_RESEARCH`；潤泰新簡報「**中鋼／鋼筋／供應商」皆 0 次**。
- `9906:material_named_relationship:62688d7d62c26d93` — `UNKNOWN_AFTER_RESEARCH`；未取得欣巴巴文件。**併同發現：本筆與 9945 之 normalized_claim_hash 完全相同——同一 claim 文本被掛在兩個 ticker 上**。
- `5263:aa07cffc342c44f5`、`9950:f674c7866ea25891` — `UNKNOWN_AFTER_RESEARCH` ×2；智崴與萬國通端點 **HTTP 404**。
- 證據記錄於 `semantic/author-240.json`（6 筆）。未修改發行人報告。帳目一致：唯一 claim 數 1,228 ＝ 條目總數 1,228。
- Next pending claim by priority: `1558:profitability_assertion:be4566041628db44` (伸興).

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
