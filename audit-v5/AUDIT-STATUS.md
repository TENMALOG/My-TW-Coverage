# Audit v5 Status

Updated: 2026-10-06 06:04 UTC
Branch: `audit-v5`

## Semantic HIGH review

- HIGH issuers: **836**
- Raw HIGH signals: **1,410**
- Unique HIGH claims: **1,399**
- Author-reviewed: **141 / 1,399**
- Remaining author review: **1,258**
- Latest batch: **author-030** (8 claims)
- Independent reviews: **0**; author decisions are not final acceptance.

### Existing author decision counts

- `ACCEPTED`: **37**
- `PARTIALLY_SUPPORTED`: **85**
- `UNSUPPORTED`: **1**
- `PERIOD_UNRESOLVED`: **0**
- `SOURCE_UNAVAILABLE`: **3**
- `UNKNOWN_AFTER_RESEARCH`: **15**

## Latest claim batch

- `2504:objective_ranking_or_market_share:271a4f0e71b4103a` — `ACCEPTED`; 國產2026法說會第2頁載「為臺灣預拌混凝土之龍頭企業」、「全台共有26個預拌廠」。
- `5546:objective_ranking_or_market_share:9e5e5a07bc534c70` — `PARTIALLY_SUPPORTED`; 永固集團介紹第6頁載重慶五個攪拌站、第13/17頁載重慶輕軌4/5/9/10號線「均指定由我司供應混凝土」；惟全份未載市占率或「領先」表述。
- `8424:objective_ranking_or_market_share:ac341368dc8f4238` — `PARTIALLY_SUPPORTED`; 惠普2025法說會第4頁載矽酸鈣板64%／纖維水泥板36%、第5頁載國產持股50.6%；惟未載「台灣最大」或任何市占率。
- `9930:objective_ranking_or_market_share:edbe1906dd3dcf78` — `ACCEPTED`; 中聯資源2026法說會第4頁載「國內規模最大爐石粉產銷業者…實踐循環經濟」，第24頁載獲環境部資源循環績優企業銀質獎。
- `2062:objective_ranking_or_market_share:a71bb7b3c16dfa04` — `PARTIALLY_SUPPORTED`; 橋椿簡報第4/5頁載其為裝飾設備鋅壓鑄零組件領導製造商、第11頁載「鋅的原料成本是銅的1/3」；惟六成以上市占係指客戶、非橋椿自身零組件市占。
- `2062:objective_ranking_or_market_share:95163601c6041a89` — `PARTIALLY_SUPPORTED`; 簡報第4/9頁載「客戶在北美及歐洲水龍頭市占率超過六成」；惟Kohler／Moen／American Standard／TOTO於簡報與110年報出現次數皆為0。
- `8930:objective_ranking_or_market_share:b7304d14590e5873` — `PARTIALLY_SUPPORTED`; 青鋼簡報第17頁沿革載「成立於1982年」、「第一家自動化生產」、「第一家上市櫃金屬建材」；惟官方為「第一家」而非claim之「唯一」。
- `8930:objective_ranking_or_market_share:0e49eeeb7dba1af5` — `UNKNOWN_AFTER_RESEARCH`; 青鋼簡報與官網簡介中「市佔」「市占」出現次數皆為0。
- 證據、期間、查閱日期與摘記記錄於 `semantic/author-030.json`。未修改發行人報告。
- Next pending claim by priority: `9924:objective_ranking_or_market_share:d29232b4aad5a82a` (福興).

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
