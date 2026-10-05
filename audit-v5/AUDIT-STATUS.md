# Audit v5 Status

Updated: 2026-10-14 08:34 UTC
Branch: `audit-v5`

## Semantic HIGH review

- HIGH issuers: **836**
- Raw HIGH signals: **1,410**
- Unique HIGH claims: **1,399**
- Author-reviewed: **1,141 / 1,399**
- Remaining author review: **258**
- Latest batch: **author-224** (1 new claim; 4 re-reviews recorded as amendments in author-223)
- Independent reviews: **0**; author decisions are not final acceptance.

### Existing author decision counts

- `ACCEPTED`: **100**
- `PARTIALLY_SUPPORTED`: **715**
- `UNSUPPORTED`: **2**
- `PERIOD_UNRESOLVED`: **0**
- `SOURCE_UNAVAILABLE`: **3**
- `UNKNOWN_AFTER_RESEARCH`: **321**

## Latest claim batch

- 🟢 `3338:material_named_relationship:f05e7d30c8a03bef` — **`ACCEPTED`**；泰碩113年度年報載「供應完整 **NVIDIA/AMD/Intel** CPU 與 GPU 之高效運算伺服器」（「**散熱」125 次、「液冷」19 次、「AI 伺服器」8 次、「NVIDIA」2 次**）——**逐項對應**。
- 🟢 `3481:material_named_relationship:1a7976baa56b151f` — **`ACCEPTED`**；群創114年度年報載「隨著子公司 **CarUX** 民國一一四年底完成對 **Pioneer** 的收購」（「**CarUX」26 次、「Pioneer」46 次、「雙軌」2 次、「More than Panel」3 次**）——**逐項對應**。
- `3338:d8fd097329e5101b` — `PARTIALLY_SUPPORTED`；年報載「F. **CDU**、Manifold 研究開發」（CDU 2次）；**惟「CDM」與「LCM」皆 0 次**。
- `3338:f2a716d3ac6b0cbc` — `PARTIALLY_SUPPORTED`；年報載「緊密配合 Intel、AMD、**NVIDIA** 等晶片大廠開發時程」；**惟「RVL」0 次**。
- `3455:material_named_relationship:82a4ffc86eb92f92` — `PARTIALLY_SUPPORTED`；由田簡報載「1. **CoWoS** RDL AOI Series」與「**OSAT**」（FOPLP 2次、先進封裝2次）；**惟「半導體營收比重顯著」未載**。
- ⚠️ **記帳更正**：本輪原重複審查 4 筆已於 author-223 結案之 claim（3338 ×3、3481）。**為維持「每個 claim_id 僅一筆判定」，該 4 筆之複審結果已移入 author-223 作為 `amendment`（保留原判定），author-224 僅保留真正新增之 1 筆。** 現況：**唯一 claim 數 1,141 ＝ 條目總數 1,141（一致）**。
- 證據、期間、查閱日期與摘記記錄於 `semantic/author-223.json`（9 筆，其中 4 筆經 amendment）與 `semantic/author-224.json`（1 筆）。未修改發行人報告。
- Next pending claim by priority: `3426:control_acquisition:a589bf991e484ce3` (台興).

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
