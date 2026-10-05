# Audit v5 Status

Updated: 2026-10-06 02:04 UTC
Branch: `audit-v5`

## Semantic HIGH review

- HIGH issuers: **836**
- Raw HIGH signals: **1,410**
- Unique HIGH claims: **1,399**
- Author-reviewed: **109 / 1,399**
- Remaining author review: **1,290**
- Latest batch: **author-026** (8 claims)
- Independent reviews: **0**; author decisions are not final acceptance.

### Existing author decision counts

- `ACCEPTED`: **28**
- `PARTIALLY_SUPPORTED`: **67**
- `UNSUPPORTED`: **1**
- `PERIOD_UNRESOLVED`: **0**
- `SOURCE_UNAVAILABLE`: **3**
- `UNKNOWN_AFTER_RESEARCH`: **10**

## Latest claim batch

- `4581:objective_ranking_or_market_share:73abdc91543dcce2`、`51c1f3dd91ff6f70` — `PARTIALLY_SUPPORTED` ×2; 光隆精密2021法說會第6頁載承接 Cummins 引擎零件、第21/22頁載為 PACCAR 英國卡車廠提供 VA/VE 與樣件，支持兩家為客戶；惟未載最大客戶、北美柴油引擎龍頭，且 Daimler／Volvo／Traton 與市佔30%／20%／10% 均未見。
- `2834:objective_ranking_or_market_share:3e15299e9e29f33f` — `PARTIALLY_SUPPORTED`; 臺企銀2025年報第30頁載前身為1915年設立之臺灣無盡株式會社，110年度永續報告第4/29頁載「全國唯一之中小企業專業銀行」；惟「八大行庫之一」未獲查閱來源逐一列名。
- `2834:objective_ranking_or_market_share:f95bff030d5de303` — `PARTIALLY_SUPPORTED`; 2025年報第62/65頁主要股東名單列第一大股東為臺灣銀行16.21%、財政部直接持股2.08%（第4名），並註明財政部持有臺灣金控100%，故財政部為最終控制者而非直接最大股東。
- `2801:objective_ranking_or_market_share:3c8dac88a1c7f530` — `ACCEPTED`; 彰銀2024年報第80頁主要股東名單第1名為財政部（12.19%），第87頁載國內營業單位185家、海外7家分行含紐約／洛杉磯／東京／倫敦／香港／新加坡／馬尼拉。
- `2836:objective_ranking_or_market_share:8aa22fea75ecafb5` — `PARTIALLY_SUPPORTED`; 高雄銀2021 ESG報告第3頁載1982年由高雄市政府出資成立、第5頁載設立日期1982/1/13與出資99.994%、第12頁載主要控制股東高雄市政府持股43.13%；惟「唯一」未獲官方使用。
- `2845:objective_ranking_or_market_share:70d1f48d13bb0d55`、`f2164388106df7ee` — `UNKNOWN_AFTER_RESEARCH` ×2; 遠東銀2021永續報告（124頁）中 VASP／虛擬資產／虛擬通貨 出現次數皆為0，113年度年報端點僅回傳320 bytes。
- 證據、期間、查閱日期與摘記記錄於 `semantic/author-026.json`。未修改發行人報告。
- Next pending claim by priority: `2880:objective_ranking_or_market_share:bea17a5f1d280fb1` (華南金).

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
