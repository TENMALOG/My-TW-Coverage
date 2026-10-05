# Audit v5 Status

Updated: 2026-10-08 04:04 UTC
Branch: `audit-v5`

## Semantic HIGH review

- HIGH issuers: **836**
- Raw HIGH signals: **1,410**
- Unique HIGH claims: **1,399**
- Author-reviewed: **428 / 1,399**
- Remaining author review: **971**
- Latest batch: **author-076** (5 claims)
- Independent reviews: **0**; author decisions are not final acceptance.

### Existing author decision counts

- `ACCEPTED`: **67**
- `PARTIALLY_SUPPORTED`: **279**
- `UNSUPPORTED`: **1**
- `PERIOD_UNRESOLVED`: **0**
- `SOURCE_UNAVAILABLE`: **3**
- `UNKNOWN_AFTER_RESEARCH`: **78**

## Latest claim batch

- `8215:objective_ranking_or_market_share:e396f3af21b11405` — `PARTIALLY_SUPPORTED`; 明基材2022年報載合資設立達尼特材料科技從事「**鋰電池用隔離膜**產品製造銷售」（隔離膜6次、捲對捲2次、塗佈3次、電動車8次、儲能6次）；惟「台灣唯一」0次。
- `8240:objective_ranking_or_market_share:ad10cdcb6cd24cc2` — `ACCEPTED`; 華宏2021年報載「**光學膜片最大專業製造裁切廠**，各項產品皆具有高的市場佔有率」，產品線含偏光板、擴散膜、增亮膜、導光板、量子點（7次）、防爆膜（6次）、觸控面板（4次）。
- `3687:objective_ranking_or_market_share:cae577f91575490d` — `PARTIALLY_SUPPORTED`; 綠界115年報載「**維持第三方支付市場龍頭地位**」（第三方支付26次）；惟「市佔率極高」「數十萬」「藍新」「LINE Pay」皆0次。
- `5478:objective_ranking_or_market_share:ce91f88d8082e000`、`66491f95bfe4f0d6` — `PARTIALLY_SUPPORTED` ×2; 智冠簡報載「★**台港澳市佔率最高 60%** ★合作產品2,400+ ★市佔第一」；惟官方範圍為「**台港澳**」而claim表述為「**台灣**」，且「四大便利商店」「東南亞」未載。
- 證據、期間、查閱日期與摘記記錄於 `semantic/author-076.json`（5 筆）。未修改發行人報告。
- Next pending claim by priority: `6473:objective_ranking_or_market_share:b29d00af5856229f` (美賣).

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
