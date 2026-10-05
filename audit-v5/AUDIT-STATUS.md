# Audit v5 Status

Updated: 2026-10-07 23:04 UTC
Branch: `audit-v5`

## Semantic HIGH review

- HIGH issuers: **836**
- Raw HIGH signals: **1,410**
- Unique HIGH claims: **1,399**
- Author-reviewed: **400 / 1,399**
- Remaining author review: **999**
- Latest batch: **author-071** (6 claims)
- Independent reviews: **0**; author decisions are not final acceptance.

### Existing author decision counts

- `ACCEPTED`: **66**
- `PARTIALLY_SUPPORTED`: **256**
- `UNSUPPORTED`: **1**
- `PERIOD_UNRESOLVED`: **0**
- `SOURCE_UNAVAILABLE`: **3**
- `UNKNOWN_AFTER_RESEARCH`: **74**

## Latest claim batch

- `6165:objective_ranking_or_market_share:b2f8d9c3fcc1a02a` — `PARTIALLY_SUPPORTED`; 浪凡議事手冊載「網路直播業務-浪Live」「以直播事業為核心」（直播22次）；惟「第一家」「AI」皆0次。
- `6174:objective_ranking_or_market_share:d7e2f404f69ba714` — `PARTIALLY_SUPPORTED`; 安碁2025簡報地區別銷售為台灣22%、美國24%、大陸36%、歐洲15%→「銷售遍及兩岸、歐美」成立；惟產品別分析係依 OSC & XTAL 而非終端應用，「車用」「工業控制」「網通」「五成」皆0次。
- `6176:objective_ranking_or_market_share:98d2560ecfdbae12` — `UNKNOWN_AFTER_RESEARCH`; 瑞儀年報「Apple」「最大客戶」皆0次，依具名客戶身分規則結為UNKNOWN。
- `6207:objective_ranking_or_market_share:5b5191cdf2afd95c` — `PARTIALLY_SUPPORTED`; 雷科文件載雷射修整機製造並載「SMT設備、被動元件產業生產設備等佔約60%以上」；惟該60%係**產品別營收占比**，非雷射修整機全球市占率。
- `6224:objective_ranking_or_market_share:163934390430b572` — `PARTIALLY_SUPPORTED`; 聚鼎2022簡報大事記載「SMD Mass Production for **ASUS customer**」「Design-Win the **Top 3 global cell phone company**」；惟「Littelfuse」「shareholder」「largest」皆0次。
- `6449:objective_ranking_or_market_share:4466a7526d81896b` — `ACCEPTED`; 鈺邦112年報載「**largest supplier of coiled solid-state capacitors in the world with a leading position in the solid-state capacitor industry**」，主要股東表列 TAI-TECH ADVANCED ELECTRONICS 28.11%，關係人交易列有 Walsin Technology。
- 證據、期間、查閱日期與摘記記錄於 `semantic/author-071.json`（6 筆）。未修改發行人報告。
- 里程碑：已審 **400 / 1,399（28.6%）**。
- Next pending claim by priority: `6196:objective_ranking_or_market_share:c712b83c2829b483` (帆宣).

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
