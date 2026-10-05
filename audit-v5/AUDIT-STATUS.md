# Audit v5 Status

Updated: 2026-10-09 18:04 UTC
Branch: `audit-v5`

## Semantic HIGH review

- HIGH issuers: **836**
- Raw HIGH signals: **1,410**
- Unique HIGH claims: **1,399**
- Author-reviewed: **692 / 1,399**
- Remaining author review: **707**
- Latest batch: **author-114** (8 claims)
- Independent reviews: **0**; author decisions are not final acceptance.

### Existing author decision counts

- `ACCEPTED`: **80**
- `PARTIALLY_SUPPORTED`: **446**
- `UNSUPPORTED`: **1**
- `PERIOD_UNRESOLVED`: **0**
- `SOURCE_UNAVAILABLE`: **3**
- `UNKNOWN_AFTER_RESEARCH`: **162**

## Latest claim batch

- `3545:objective_ranking_or_market_share:3863a18a0b35d83b`、`b0c570c3eee08a0b` — `ACCEPTED` ×2；敦泰2024年報載「（本公司）**觸控IC** 年度出貨逾4億顆，成為**全球最大觸控IC 供應商**」，並見電容式15次、顯示驅動17次、指紋68次、TDDI 2次——**逐項對應**。
- `3567:objective_ranking_or_market_share:771daad65f7afad8` — `PARTIALLY_SUPPORTED`；逸昌112年報「類比」66次、「混合訊號」6次、「晶圓測試」16次、「100%」3次；惟「第一家」「雷射修整」「捲帶」皆0次。
- `3583:objective_ranking_or_market_share:d01d05af66a35f62` — `PARTIALLY_SUPPORTED`；辛耘2025年報「濕式」5次、「矽晶圓再生」2次；惟「16萬」「16nm」皆0次。
- `3583:objective_ranking_or_market_share:9f4f88d12436b18e` — `UNKNOWN_AFTER_RESEARCH`；年報「最大客戶」「19.37」皆0次，且「**台積電」9 次含「台積電採購副理」之人員經歷**與「製造商如台積電、三星和英特爾」之產業敘述。
- `3661:objective_ranking_or_market_share:3565731645cc816a` — `PARTIALLY_SUPPORTED`；世芯年報「ASIC」84次、「先進製程」4次、「台積電」3次；惟「**唯一」0 次**。
- `3680:objective_ranking_or_market_share:6827b5060d58507e`、`7bf17ffbe1bd9dda` — `PARTIALLY_SUPPORTED` ×2；家登文件「EUV」1次、「FOUP」4次；惟「ASML」「80%」「50%」皆0次（該檔文字擷取僅3,381字元）。
- 證據、期間、查閱日期與摘記記錄於 `semantic/author-114.json`（8 筆）。未修改發行人報告。
- Next pending claim by priority: `3680:objective_ranking_or_market_share:c865bf5112c73bab` (家登).

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
