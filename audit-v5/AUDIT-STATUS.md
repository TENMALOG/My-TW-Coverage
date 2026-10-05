# Audit v5 Status

Updated: 2026-10-10 03:04 UTC
Branch: `audit-v5`

## Semantic HIGH review

- HIGH issuers: **836**
- Raw HIGH signals: **1,410**
- Unique HIGH claims: **1,399**
- Author-reviewed: **744 / 1,399**
- Remaining author review: **655**
- Latest batch: **author-123** (8 claims)
- Independent reviews: **0**; author decisions are not final acceptance.

### Existing author decision counts

- `ACCEPTED`: **83**
- `PARTIALLY_SUPPORTED`: **483**
- `UNSUPPORTED`: **1**
- `PERIOD_UNRESOLVED`: **0**
- `SOURCE_UNAVAILABLE`: **3**
- `UNKNOWN_AFTER_RESEARCH`: **174**

## Latest claim batch

- `5202:objective_ranking_or_market_share:0a310a8ce7f2645f` — `UNKNOWN_AFTER_RESEARCH`；所取得力新文件為**永續報告書**，「第一金」「富邦金」皆0次。
- `5403:objective_ranking_or_market_share:5c94bad17f7166b3`、`e50a246d694f5936`、`6ea45e064b9f4141` — `UNKNOWN_AFTER_RESEARCH` ×3；中菲官方網域 **DNS 解析失敗**（兩度嘗試）。
- `6231:objective_ranking_or_market_share:1da870e8d9816ee5` — `PARTIALLY_SUPPORTED`；系微簡介「**BIOS」5 次、「Intel」8 次、「AMD」3 次、「Snapdragon」1 次**；惟「AI PC」「市佔」皆0次。
- `6590:objective_ranking_or_market_share:b5dc93a1541f6920` — `PARTIALLY_SUPPORTED`；普鴻簡報「**資安」10 次、「支付」3 次**、「票交」1次；惟「跨行」「清算」「市佔」皆0次。
- `6738:objective_ranking_or_market_share:16908d8f6cf3d1a7` — `PARTIALLY_SUPPORTED`；鼎恒年報「**超過95%高續約率**」✓；惟「**1,300」3 次皆為財務數字**（17,300／51,300／11,300），「**緯創」1 次為「緯創軟體董事李紹唐」之個人職稱**，「遠雄」0次。
- `6738:objective_ranking_or_market_share:7d16cd36e6e8ebf5` — `PARTIALLY_SUPPORTED`；「Azure」9次；惟「唯一」為「台灣區唯一合作夥伴**代表**」（活動身分），「創新合作夥伴」0次。
- 證據、期間、查閱日期與摘記記錄於 `semantic/author-123.json`（8 筆）。未修改發行人報告。
- Next pending claim by priority: `6902:objective_ranking_or_market_share:f2d0f66b5bcf6aed` (GOGOLOOK).

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
