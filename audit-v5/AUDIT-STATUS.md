# Audit v5 Status

Updated: 2026-10-07 06:04 UTC
Branch: `audit-v5`

## Semantic HIGH review

- HIGH issuers: **836**
- Raw HIGH signals: **1,410**
- Unique HIGH claims: **1,399**
- Author-reviewed: **301 / 1,399**
- Remaining author review: **1,098**
- Latest batch: **author-054** (8 claims)
- Independent reviews: **0**; author decisions are not final acceptance.

### Existing author decision counts

- `ACCEPTED`: **53**
- `PARTIALLY_SUPPORTED`: **196**
- `UNSUPPORTED`: **1**
- `PERIOD_UNRESOLVED`: **0**
- `SOURCE_UNAVAILABLE`: **3**
- `UNKNOWN_AFTER_RESEARCH`: **48**

## Latest claim batch

- `5904:objective_ranking_or_market_share:1c808dde25b1f8c1` — `PARTIALLY_SUPPORTED`; 寶雅官方投資人專區載地址「台南市民族路三段74號」與主要經營業務（時尚美粧、內衣襪、生活日常用品）；惟未載「台灣最大」「連鎖」，官網財務報告下載失敗、MOPS年報端點回320 bytes。
- `2496:objective_ranking_or_market_share:f13fd59509def495` — `PARTIALLY_SUPPORTED`; 卓越113年報資料載集團旗下「陳立教育」之升學教學服務（陳立10次、高中6次）；惟「全國最大」與「40年」皆0次。
- `1537:objective_ranking_or_market_share:a9061697368a9c39` — `PARTIALLY_SUPPORTED`; 廣隆2022簡報載「KLB是**東南亞**產能最大的專業生產UPS電（池）」（範圍為東南亞而非claim之亞洲）；「LONG」「100國」皆0次。
- `1597:objective_ranking_or_market_share:00f892e251ed2b4f` — `PARTIALLY_SUPPORTED`; 直得114年報「半導體」32次、「醫療」10次、「自動化」64次；惟「最大」6處均為股東利益等語，非應用領域排序。
- `1617:objective_ranking_or_market_share:9fba43f07feab108` — `PARTIALLY_SUPPORTED`; 榮星2025簡報「漆包線」16次；惟「龍頭」「唯一」「最齊全」皆0次。
- `3078:objective_ranking_or_market_share:299b9d575f6c2dfd` — `PARTIALLY_SUPPORTED`; 僑威2022永續報告「電源」103次；惟「全球最大」「代工」「市佔」皆0次。
- `3092:objective_ranking_or_market_share:e36782398881d1ed` — `UNKNOWN_AFTER_RESEARCH`; 鴻碩官方年報路徑所下載PDF僅1,086字元且為網站頁尾文字，非公司文件。
- `3484:objective_ranking_or_market_share:e42a3a40cfbcace6` — `PARTIALLY_SUPPORTED`; 崧騰2020簡報「開關」9次、載高耐受性與防水防塵開關設計；惟「全球最大」「電動工具」「市佔」皆0次。
- 證據、期間、查閱日期與摘記記錄於 `semantic/author-054.json`（8 筆）。未修改發行人報告。
- Next pending claim by priority: `3484:objective_ranking_or_market_share:277360a2dcd0bf7c` (崧騰).

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
