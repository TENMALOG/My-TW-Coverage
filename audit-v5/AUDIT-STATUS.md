# Audit v5 Status

Updated: 2026-10-05 23:04 UTC
Branch: `audit-v5`

## Semantic HIGH review

- HIGH issuers: **836**
- Raw HIGH signals: **1,410**
- Unique HIGH claims: **1,399**
- Author-reviewed: **85 / 1,399**
- Remaining author review: **1,314**
- Latest batch: **author-023** (7 claims)
- Independent reviews: **0**; author decisions are not final acceptance.

### Existing author decision counts

- `ACCEPTED`: **26**
- `PARTIALLY_SUPPORTED`: **51**
- `UNSUPPORTED`: **1**
- `PERIOD_UNRESOLVED`: **0**
- `SOURCE_UNAVAILABLE`: **3**
- `UNKNOWN_AFTER_RESEARCH`: **4**

## Latest claim batch

- `2235:objective_ranking_or_market_share:2f804dd9a0a390da` — `PARTIALLY_SUPPORTED`; 謚源103年上櫃公開說明書載與堤維西自89年合作、北美銷售獨家委由堤維西、再由其美國子公司 GENERA 銷售予 General Parts Inc／LKQ／Amazon Services，第一大客戶堤維西占營收78.80%／77.44%；惟官方文件未出現 NAPA。
- `2235:objective_ranking_or_market_share:f11191fc5107144b` — `ACCEPTED`; 同一公開說明書載「美國最大汽車維修通路商LKQ Corp.」，LKQ FY2025 10-K 亦載其北美部門營運北美最大替代性零件配送網路。
- `2239:objective_ranking_or_market_share:f6f576305c25bdeb`、`95f5fff739fc9085` — `ACCEPTED` ×2; 英利公開發行說明書載一汽大眾為最大客戶（銷售占比80.24%→73.16%）、北京奔馳與上汽大眾列名主要客戶，並載「一汽大眾AUDI所有系列的儀錶板骨架皆為本集團生產」。
- `2239:objective_ranking_or_market_share:1f382b871069e7dc`、`8d3dc1316d4155c8`、`f1b8e1134f6bc9d1` — `PARTIALLY_SUPPORTED` ×3; 說明書與2017法說會簡報支持 SymaLITE 專利授權與歐洲產線、首家國產化廠；惟均未載「亞洲唯一產線」「全球僅5條」，亦未將 Audi 與底盤護板連結。
- 證據、期間、查閱日期與摘記記錄於 `semantic/author-023.json`。未修改發行人報告。
- Next pending claim by priority: `2245:objective_ranking_or_market_share:7ade1b140810fe09` (詠勝昌).

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
