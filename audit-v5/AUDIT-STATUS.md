# Audit v5 Status

Updated: 2026-10-06 22:04 UTC
Branch: `audit-v5`

## Semantic HIGH review

- HIGH issuers: **836**
- Raw HIGH signals: **1,410**
- Unique HIGH claims: **1,399**
- Author-reviewed: **254 / 1,399**
- Remaining author review: **1,145**
- Latest batch: **author-046** (5 claims)
- Independent reviews: **0**; author decisions are not final acceptance.

### Existing author decision counts

- `ACCEPTED`: **53**
- `PARTIALLY_SUPPORTED`: **161**
- `UNSUPPORTED`: **1**
- `PERIOD_UNRESOLVED`: **0**
- `SOURCE_UNAVAILABLE`: **3**
- `UNKNOWN_AFTER_RESEARCH`: **36**

## Latest claim batch

- `6166:objective_ranking_or_market_share:b3a2e1a025feff65` — `PARTIALLY_SUPPORTED`; 凌華108年報載「COM Express, SMARC, Qseven」與ROS（5次）；惟「友達」「鴻海」「法博」皆0次（該年報早於相關事件）。
- `6188:objective_ranking_or_market_share:22cd3f0905111079` — `PARTIALLY_SUPPORTED`; 廣明官方股東資料載廣達電腦為法人董事代表人；惟「客戶」「最大」「Toyota」「晶圓」皆0次。
- `6206:objective_ranking_or_market_share:11dce486dbff428d` — `PARTIALLY_SUPPORTED`; 飛捷2025簡報第5頁載零售、餐飲、醫療與工業自動化領域及POS/自助服務/嵌入式電腦；惟「市佔」0次。
- `6228:objective_ranking_or_market_share:5c4944216c7b1727` — `PARTIALLY_SUPPORTED`; 全譜年報與簡報載底片掃描器產品；惟「Kodak」「柯達」「Olympus」皆0次，且年報第60頁市佔率表（螢光與化學光成像系統）載全譜推估市佔率**<1%**，同頁底片掃瞄器段落未載市占。
- `6277:objective_ranking_or_market_share:7c8c5bb9d85cb3ea` — `PARTIALLY_SUPPORTED`; 宏正93年報「KVM」52次；惟「全球最大」0次，且該文件為2004年版本。
- 證據、期間、查閱日期與摘記記錄於 `semantic/author-046.json`（5 筆）。未修改發行人報告。
- Next pending claim by priority: `6485:objective_ranking_or_market_share:5969e1c71ddb6ef2` (點序).

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
