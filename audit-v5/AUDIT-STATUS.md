# Audit v5 Status

Updated: 2026-10-14 16:04 UTC
Branch: `audit-v5`

## Semantic HIGH review

- HIGH issuers: **836**
- Raw HIGH signals: **1,410**
- Unique HIGH claims: **1,399**
- Author-reviewed: **1,180 / 1,399**
- Remaining author review: **219**
- Latest batch: **author-232** (6 claims)
- Independent reviews: **0**; author decisions are not final acceptance.

### Existing author decision counts

- `ACCEPTED`: **101**
- `PARTIALLY_SUPPORTED`: **739**
- `UNSUPPORTED`: **2**
- `PERIOD_UNRESOLVED`: **0**
- `SOURCE_UNAVAILABLE`: **3**
- `UNKNOWN_AFTER_RESEARCH`: **335**

## Latest claim batch

- `6116:profitability_assertion:fee901f6415a0400` — `PARTIALLY_SUPPORTED`；彩晶年報「**車載」42 次、「面板」185 次**；**惟「高毛利」1 次且係泛用敘述**。
- `6116:material_named_relationship:aba5c3b20e5397e2` — `UNKNOWN_AFTER_RESEARCH`；**「HP」1 次係地址「Hempstead HP2 4TZ」之子字串**，「**宏碁／Dell」皆 0 次**。
- `6155:material_named_relationship:7c03d4361ff42950` — `PARTIALLY_SUPPORTED`；鈞寶簡報「**電感」6 次、「5G」4 次**；**惟「LTCC／低溫共燒／陶瓷」皆 0 次**。
- `6158:material_named_relationship:abe99517d07e32de` — `PARTIALLY_SUPPORTED`；禾昌文件**逐字載**「軟板暨軟排線**連接器**、**液晶面板**及顯示器**連接器**」（連接器36次、液晶面板4次）；**惟具名客戶未獲支持**。
- `5474:material_named_relationship:8a46d7cd77b269e6` — `PARTIALLY_SUPPORTED`；聰泰ESG「**影像擷取」11 次、「AI」28 次**；**惟「歐美／人形」皆 0 次，且「機器人」1 次係產業協會名稱**。
- `5251:material_named_relationship:7a2e178397650de7` — `UNKNOWN_AFTER_RESEARCH`；天鉞電**未取得官方文件**（搜尋僅導向第三方資訊站，不予採用）。
- 證據記錄於 `semantic/author-232.json`（6 筆）。未修改發行人報告。帳目一致：唯一 claim 數 1,180 ＝ 條目總數 1,180。
- Next pending claim by priority: `5315:profitability_assertion:a8d38d9aef0affb8` (光聯).

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
