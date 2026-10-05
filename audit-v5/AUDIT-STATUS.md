# Audit v5 Status

Updated: 2026-10-14 23:04 UTC
Branch: `audit-v5`

## Semantic HIGH review

- HIGH issuers: **836**
- Raw HIGH signals: **1,410**
- Unique HIGH claims: **1,399**
- Author-reviewed: **1,222 / 1,399**
- Remaining author review: **177**
- Latest batch: **author-239** (6 claims)
- Independent reviews: **0**; author decisions are not final acceptance.

### Existing author decision counts

- `ACCEPTED`: **103**
- `PARTIALLY_SUPPORTED`: **760**
- `UNSUPPORTED`: **2**
- `PERIOD_UNRESOLVED`: **0**
- `SOURCE_UNAVAILABLE`: **3**
- `UNKNOWN_AFTER_RESEARCH`: **354**

## Latest claim batch

- `2354:material_named_relationship:8d538674a3923948` — `PARTIALLY_SUPPORTED`；鴻準年報載「【消費性電子產品(**遊戲機**)系統**組裝**】」（**遊戲機 34 次、組裝 17 次**）；**惟「任天堂／Nintendo／Switch／Apple」皆 0 次**。
- `6150:material_named_relationship:0112c8a5be3447d0` — `PARTIALLY_SUPPORTED`；撼訊簡報「**AMD」8 次、「顯示卡」2 次**；**惟「全球／前列」與「主要供應商之一」未獲支持**。
- `1472:identity_changing_event:ead6a8ddf3696763` — `PARTIALLY_SUPPORTED`；三洋實業簡報「**營造」6 次、「甲級」2 次、「更名」1 次**；**惟「上騰／政府標案」皆 0 次**。
- `3528:profitability_assertion:90c59cc187b13900` — `UNKNOWN_AFTER_RESEARCH`；安馳簡報為**英文版**，「**工業／國防／醫療／測試／利基」皆 0 次**。
- `6473:447f7733d52280f2`、`6908:fd2c6df51c194b44` — `UNKNOWN_AFTER_RESEARCH` ×2；美賣與宏碁遊戲端點 **HTTP 404**。
- ⚠️ 附帶發現：`6908` 之 **company 欄位在來源佇列中為亂碼（「宏�砦C戲」）**，本審核以 ticker 為準並已標示該來源資料編碼瑕疵。
- 證據記錄於 `semantic/author-239.json`（6 筆）。未修改發行人報告。帳目一致：唯一 claim 數 1,222 ＝ 條目總數 1,222。
- Next pending claim by priority: `2404:material_named_relationship:c9fafe0c318e0dc0` (漢唐).

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
