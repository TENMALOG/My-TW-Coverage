# Audit v5 Status

Updated: 2026-10-07 08:04 UTC
Branch: `audit-v5`

## Semantic HIGH review

- HIGH issuers: **836**
- Raw HIGH signals: **1,410**
- Unique HIGH claims: **1,399**
- Author-reviewed: **312 / 1,399**
- Remaining author review: **1,087**
- Latest batch: **author-056** (7 claims)
- Independent reviews: **0**; author decisions are not final acceptance.

### Existing author decision counts

- `ACCEPTED`: **54**
- `PARTIALLY_SUPPORTED`: **203**
- `UNSUPPORTED`: **1**
- `PERIOD_UNRESOLVED`: **0**
- `SOURCE_UNAVAILABLE`: **3**
- `UNKNOWN_AFTER_RESEARCH`: **51**

## Latest claim batch

- `5227:objective_ranking_or_market_share:46ed0624b8da23c3` — `PARTIALLY_SUPPORTED`; 立凱簡報載「將在美國、歐洲、澳洲和印度授權生產」與其LFP材料地位；惟「ICL」「4億」「補貼」「首座」皆0次。
- `6121:objective_ranking_or_market_share:6289cc549c3bc5c6` — `ACCEPTED`; 新普2023永續報告載「全球筆電(NB)電池組的**市佔持續維持全球第一**」「每年提供超過兩億個電池組」「市場上**每三個筆記型電腦中，就有一個為新普科技製造**」。
- `6290:objective_ranking_or_market_share:19c3d40cace1a46e` — `UNKNOWN_AFTER_RESEARCH`; 良維2020簡報載其為全球電源線及連接線領導廠商；惟「Amazon」「Microsoft」「Lenovo」「ChargePoint」「最大客戶」皆0次，未具名任何客戶。
- `6409:objective_ranking_or_market_share:5d7e6075ec84567f` — `PARTIALLY_SUPPORTED`; 旭隼2025簡報載「**100% ODM in UPS**」；惟「全球最大」「largest」「台積電」皆0次。
- `6558:objective_ranking_or_market_share:7f263d7df2605e0b` — `PARTIALLY_SUPPORTED`; 興能高2024永續報告載產品應用於藍牙耳機、無線健康穿戴裝置（藍牙耳機3次）；惟「市佔」「12%」皆0次。
- `6788:objective_ranking_or_market_share:4cdbfeafed0be581`、`e15a4230aec4e97e` — `UNKNOWN_AFTER_RESEARCH` ×2; 華景電2025簡報載晶圓製程AMC防治設備與製程節點（90nm–2nm）及「優質客戶群」標題，惟「台積電」「TSMC」「聯電」「旺宏」「Micron」「中芯」「最大」皆0次，客戶名稱未見於文字層。
- 證據、期間、查閱日期與摘記記錄於 `semantic/author-056.json`（7 筆）。未修改發行人報告。
- 本批次起明確採用一致性規則：claim 實質內容**全為具名客戶身分**且官方文件未具名任何客戶 → `UNKNOWN_AFTER_RESEARCH`；claim **混合可查證之業務描述與不可查證之客戶／排名** → `PARTIALLY_SUPPORTED`。
- Next pending claim by priority: `6940:objective_ranking_or_market_share:a339a04db47953d6` (格斯科技).

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
