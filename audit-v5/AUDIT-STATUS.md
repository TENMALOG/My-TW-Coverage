# Audit v5 Status

Updated: 2026-10-08 07:04 UTC
Branch: `audit-v5`

## Semantic HIGH review

- HIGH issuers: **836**
- Raw HIGH signals: **1,410**
- Unique HIGH claims: **1,399**
- Author-reviewed: **448 / 1,399**
- Remaining author review: **951**
- Latest batch: **author-079** (7 claims)
- Independent reviews: **0**; author decisions are not final acceptance.

### Existing author decision counts

- `ACCEPTED`: **69**
- `PARTIALLY_SUPPORTED`: **292**
- `UNSUPPORTED`: **1**
- `PERIOD_UNRESOLVED`: **0**
- `SOURCE_UNAVAILABLE`: **3**
- `UNKNOWN_AFTER_RESEARCH`: **83**

## Latest claim batch

- `3360:objective_ranking_or_market_share:1e5c4a342b962d2f` — `PARTIALLY_SUPPORTED`；深圳證券交易所公開文件載「發行人向**尚立（香港）**採購的 **CMOS 圖像傳感器**價格係由影石創新與**日本索尼（Sony）**…協商確定…並直接與日本索尼（Sony）的**代理（商）**」，支持其處於 Sony CIS 供應／代理環節；惟「最大供應商」未載（本件為第三人之公開文件）。
- `3483:objective_ranking_or_market_share:eb582bc6e017b55f` — `ACCEPTED`；力致2025簡報「我們的優勢」載「**筆電風扇市佔率最高**」（散熱10次、風扇7次）。
- `3702:objective_ranking_or_market_share:c5f8ff6dd3f3b9ef` — `PARTIALLY_SUPPORTED`；大聯大2022年報「世平」35次、「WPI」18次；惟「最大子公司」0次。
- `5434:objective_ranking_or_market_share:a062e5f5b5b17bbb` — `PARTIALLY_SUPPORTED`；崇越113年報光阻15次、矽晶圓14次、先進製程12次；惟「最大客戶」0次。
- `6227:objective_ranking_or_market_share:43389475739d47d9` — `PARTIALLY_SUPPORTED`；茂綸年報Macnica 22次、代理106次、NVIDIA 4次、Renesas 4次；惟「日本第一大」0次。
- `8070:objective_ranking_or_market_share:db178e56e65db8b1`、`ab0adc7ddd6d83f3` — `PARTIALLY_SUPPORTED` ×2；長華2018年報載「整併日商住友導線架業務…成為**全球第三大導線架廠**」（導線架46次、封膠19次、住友7次、EMC 2次）；惟「51%」為**員工高中學歷比率**、「28%」為「8,028%」之子字串、「33%」為持股4.33%、「67%」為**董事出席率**，均非市場或營收數字；「市佔」5次均指台灣半導體產業整體。
- 證據、期間、查閱日期與摘記記錄於 `semantic/author-079.json`（7 筆）。未修改發行人報告。
- Next pending claim by priority: `6776:objective_ranking_or_market_share:59f0a1faacffbf5e` (展碁國際).

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
