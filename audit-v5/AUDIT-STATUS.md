# Audit v5 Status

Updated: 2026-10-15 22:34 UTC
Branch: `audit-v5`

## Semantic HIGH review

- HIGH issuers: **836**
- Raw HIGH signals: **1,410**
- Unique HIGH claims: **1,399**
- Author-reviewed: **1,363 / 1,399**
- Remaining author review: **36**
- Latest batch: **author-262** (5 claims)
- Independent reviews: **0**; author decisions are not final acceptance.

### Existing author decision counts

- `ACCEPTED`: **106**
- `PARTIALLY_SUPPORTED`: **818**
- `UNSUPPORTED`: **2**
- `PERIOD_UNRESOLVED`: **0**
- `SOURCE_UNAVAILABLE`: **3**
- `UNKNOWN_AFTER_RESEARCH`: **434**

## Latest claim batch

- `4904:material_named_relationship:82d2b1e647aca322` — `PARTIALLY_SUPPORTED`；遠傳2024英文版年報載「Joined the **Ericsson** Global Product Take-Back Program and recycle…wastes from **base stations**」（**Ericsson 7 次、5G 117 次、base station 20 次**）；**惟「主要供應商」之排序性表述未見**。
- `5016:material_named_relationship:f7cc475a704a35de` — `PARTIALLY_SUPPORTED`；松和簡報「**電梯」1 次、「鋼索」1 次**；**惟「崇友／永大」皆 0 次**。
- `1307:material_named_relationship:4eb0c68975ca904a` — `PARTIALLY_SUPPORTED`；三芳簡報「**Nike／Adidas／Puma 各 2 次**」；**惟「New Balance／Hoka／On Running／指定供應商」皆 0 次**。
- `1307:material_named_relationship:572938d0d688e798` — `UNKNOWN_AFTER_RESEARCH`；三芳簡報「**座椅／門飾／皮革／Tier 1／MIH」皆 0 次**。
- `2221:export_concentration:abc1d459bf42c9b4` — `UNKNOWN_AFTER_RESEARCH`；大甲端點 **HTTP 404**。
- ⚠️ **本批次之帳目更正**：`5009:profitability_assertion:b8037559961325d8` 原已於 `author-261` 判定（UNKNOWN，端點404）。為維持「每一 claim 於帳本中僅有一個判定」，**已將該筆自本批次移除，並把其所據之新證據（榮剛2024法說會簡報）與新評估以 `amendment` 之形式併入 author-261 之對應條目**（原判定不予更動）；本批次並加入 `corrections` 記錄。
- 證據記錄於 `semantic/author-262.json`（**5 筆**）。未修改發行人報告。帳目一致：唯一 claim 數 1,363 ＝ 條目總數 1,363。**覆蓋率 97.43%**。
- Next pending claim by priority: `1341:export_concentration:68cf7713a01f37cf` (富林-KY).

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
