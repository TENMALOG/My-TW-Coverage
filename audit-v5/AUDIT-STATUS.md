# Audit v5 Status

Updated: 2026-10-09 17:04 UTC
Branch: `audit-v5`

## Semantic HIGH review

- HIGH issuers: **836**
- Raw HIGH signals: **1,410**
- Unique HIGH claims: **1,399**
- Author-reviewed: **684 / 1,399**
- Remaining author review: **715**
- Latest batch: **author-113** (8 claims)
- Independent reviews: **0**; author decisions are not final acceptance.

### Existing author decision counts

- `ACCEPTED`: **78**
- `PARTIALLY_SUPPORTED`: **441**
- `UNSUPPORTED`: **1**
- `PERIOD_UNRESOLVED`: **0**
- `SOURCE_UNAVAILABLE`: **3**
- `UNKNOWN_AFTER_RESEARCH`: **161**

## Latest claim batch

- `3141:objective_ranking_or_market_share:65a03ef2f2732bd5`、`76eab7724d46fd0c` — `UNKNOWN_AFTER_RESEARCH` ×2；晶宏2022年報「**元太」0 次**、「最大客戶」0次；「**E Ink」1 次係「E Ink Spectra 3100**」之**技術規格名稱**；「母公司」158次多為財務報表用語。
- `3227:objective_ranking_or_market_share:9484acc8041462d9` — `UNKNOWN_AFTER_RESEARCH`；原相官方年報端點所取得檔案**僅111 bytes**（PDF解析回應 no objects found），顯非 PDF。
- `3264:objective_ranking_or_market_share:60de4d8a051579fe`、`067c7811d5d64930` — `UNKNOWN_AFTER_RESEARCH` ×2；欣銓111年報**文字層呈現亂碼**（與台光電／上洋／必應／峰源同型），車用／測試／MCU／市占皆0次。
- `3443:objective_ranking_or_market_share:0e18f8dc0286575f` — `UNKNOWN_AFTER_RESEARCH`；所取得者為「**2022 創意電子氣候相關財務揭露報告書**」（TCFD），「台積電」「最大股東」皆0次。
- `3527:objective_ranking_or_market_share:8eb795fd7f9d812e` — `PARTIALLY_SUPPORTED`；聚積議事手冊載「為**全球第一大顯示屏LED 驅動IC 廠**」（LED 45次、Mini 6次、Micro 3次）；惟「物聯網精準行銷系統」未見。
- `3527:objective_ranking_or_market_share:39a26c1aea2cd59c` — `ACCEPTED`；議事手冊載「為**全球第一大顯示屏LED 驅動IC 廠**」——逐項對應。
- 證據、期間、查閱日期與摘記記錄於 `semantic/author-113.json`（8 筆）。未修改發行人報告。
- Next pending claim by priority: `3545:objective_ranking_or_market_share:3863a18a0b35d83b` (敦泰).

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
