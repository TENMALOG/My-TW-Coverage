# Audit v5 Status

Updated: 2026-10-07 02:04 UTC
Branch: `audit-v5`

## Semantic HIGH review

- HIGH issuers: **836**
- Raw HIGH signals: **1,410**
- Unique HIGH claims: **1,399**
- Author-reviewed: **277 / 1,399**
- Remaining author review: **1,122**
- Latest batch: **author-050** (8 claims)
- Independent reviews: **0**; author decisions are not final acceptance.

### Existing author decision counts

- `ACCEPTED`: **53**
- `PARTIALLY_SUPPORTED`: **175**
- `UNSUPPORTED`: **1**
- `PERIOD_UNRESOLVED`: **0**
- `SOURCE_UNAVAILABLE`: **3**
- `UNKNOWN_AFTER_RESEARCH`: **45**

## Latest claim batch

- `2371:objective_ranking_or_market_share:7c1b7458bb352b9a` — `PARTIALLY_SUPPORTED`; 大同113年報「台電」33次（電網強韌計畫、345KV特高壓電纜、變電所統包工程）；惟「國內最大客戶」0次、「中東」0次。
- `2614:objective_ranking_or_market_share:fc653f741714d04d` — `PARTIALLY_SUPPORTED`; 東森109年報載台灣最大網路媒體、comScore觸及率逾85%、新聞類網站第一名；惟「衛星電視頻道」未獲支持（「衛星」4次均為法規名稱與物流衛星倉）。
- `5288:objective_ranking_or_market_share:e2b6169ea8b47d06`、`e03e47ad2fe08132`、`26d23c8673c73aeb` — `PARTIALLY_SUPPORTED` ×3; 豐祥簡報載2006年越南Exedy合資與2012年供應Polaris；惟 Honda／Yamaha／Ducati／Harley 皆0次、「最大客戶」未載、業務別營收比重未載。
- `6754:objective_ranking_or_market_share:97bcd095ad4b455e` — `PARTIALLY_SUPPORTED`; 匯僑簡報「精品」6次（國際精品名牌、Cartier杭州、台北101精品櫃位、深耕30餘年）；惟 LVMH／Kering／Richemont 與「市佔」皆0次。
- `4749:objective_ranking_or_market_share:b6aa8390164f3bc1`、`8a41f0ce8cef58b5` — `PARTIALLY_SUPPORTED` ×2; 新應材簡報載先進製程光阻與DUV光阻劑、晶圓代工客戶；惟「最大客戶」0次，且「79%」實為**半導體應用材料占營收比重**、「79.6%」為**2024年台灣占銷售區域比重**，均非單一客戶占比。
- 證據、期間、查閱日期與摘記記錄於 `semantic/author-050.json`（8 筆）。未修改發行人報告。
- Next pending claim by priority: `5225:objective_ranking_or_market_share:9878893f3dc16044` (東科-KY).

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
