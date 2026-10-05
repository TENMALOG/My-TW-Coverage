# Audit v5 Status

Updated: 2026-10-14 17:04 UTC
Branch: `audit-v5`

## Semantic HIGH review

- HIGH issuers: **836**
- Raw HIGH signals: **1,410**
- Unique HIGH claims: **1,399**
- Author-reviewed: **1,186 / 1,399**
- Remaining author review: **213**
- Latest batch: **author-233** (6 claims)
- Independent reviews: **0**; author decisions are not final acceptance.

### Existing author decision counts

- `ACCEPTED`: **101**
- `PARTIALLY_SUPPORTED`: **744**
- `UNSUPPORTED`: **2**
- `PERIOD_UNRESOLVED`: **0**
- `SOURCE_UNAVAILABLE`: **3**
- `UNKNOWN_AFTER_RESEARCH`: **336**

## Latest claim batch

- `5315:profitability_assertion:a8d38d9aef0affb8` — `PARTIALLY_SUPPORTED`；光聯年報「**車載」4 次、「利基」3 次**；**惟「Porsche／高毛利」皆 0 次**。
- `5328:material_named_relationship:6e569e23de500446` — `PARTIALLY_SUPPORTED`；華容手冊「**電容」11 次、「電動車」1 次**並載「綠色新能源配套用**電容器**」；**惟「充電樁／中國車廠」皆 0 次**。
- ⚠️ `5345:profitability_assertion:a313145adca2eb03` — `PARTIALLY_SUPPORTED`；**馥鴻（5345）現已為「馥鴻建設」（FullHome）**，其2025年法說會內容為**建設事業**（「**電源**」與「**科技**」各僅1次），**與 claim 所述之「智慧電源控制技術」方向不同**——**已標示此業務變更供複核者優先檢視**。
- `6114:material_named_relationship:95a80caca976facc` — `UNKNOWN_AFTER_RESEARCH`；所取得檔案僅 **2,753 bytes**（**無文字層**）。
- `6205:profitability_assertion:3622ea1b4a869dfe` — `PARTIALLY_SUPPORTED`；詮欣簡報載「**車用**高速傳輸技術」「以高速高頻技術突破 **Tier 1 車用客戶供應鏈**」（車用4次、PC 8次、轉型1次）。
- `6207:material_named_relationship:500ab024118bcd98` — `PARTIALLY_SUPPORTED`；雷科簡報載「**COWOS 設備**」「**CoWoS CT**」（CoWoS 4次、量測3次）；**惟「台積電／雷射切割」皆 0 次**。
- 證據記錄於 `semantic/author-233.json`（6 筆）。未修改發行人報告。帳目一致：唯一 claim 數 1,186 ＝ 條目總數 1,186。
- Next pending claim by priority: `6210:material_named_relationship:735bde0845d750f2` (慶生).

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
