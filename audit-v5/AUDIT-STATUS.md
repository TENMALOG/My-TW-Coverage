# Audit v5 Status

Updated: 2026-10-14 15:04 UTC
Branch: `audit-v5`

## Semantic HIGH review

- HIGH issuers: **836**
- Raw HIGH signals: **1,410**
- Unique HIGH claims: **1,399**
- Author-reviewed: **1,174 / 1,399**
- Remaining author review: **225**
- Latest batch: **author-231** (4 claims)
- Independent reviews: **0**; author decisions are not final acceptance.

### Existing author decision counts

- `ACCEPTED`: **101**
- `PARTIALLY_SUPPORTED`: **735**
- `UNSUPPORTED`: **2**
- `PERIOD_UNRESOLVED`: **0**
- `SOURCE_UNAVAILABLE`: **3**
- `UNKNOWN_AFTER_RESEARCH`: **333**

## Latest claim batch

- 🟢 `3624:material_named_relationship:ac1a104f423eebd9` — **`ACCEPTED`**；光頡ESG**逐字載**「（符）合 **IATF16949、AEC-Q200**、ISO13485」與「更由**歐美車廠供應鏈 Tier 1** 親自到廠做 **VDA 6.3** 過程稽核，且獲得客戶評級 **A** 的肯定」——**逐項對應**。
- `3717:material_named_relationship:e3d253a6e990043a` — `PARTIALLY_SUPPORTED`；聯嘉年報載「2022 年 microprism 應用在 **Magna MY24 DT 尾燈**」（Tier 1 6次）；**惟「Hella」0 次**。
- `3717:material_named_relationship:91a5266bf0300df3` — `PARTIALLY_SUPPORTED`；年報載「客戶包含 Ford、FCA、**Tesla**、BMW、TOYOTA、GM」與「美國電動車大廠 **Tesla** 的**供應鏈**」（Tesla 8次、尾燈12次、Model 3 2次）；**惟「Model Y」與「主要供應商」未獲支持**。
- `3426:control_acquisition:a589bf991e484ce3` — `UNKNOWN_AFTER_RESEARCH`；台興簡報為**電磁閥事業介紹**，「**松川／晶技／收購／溢價」皆 0 次**；**且「48」係來自「2.48」之子字串（子字串假陽性）**。
- 證據記錄於 `semantic/author-231.json`（4 筆）。未修改發行人報告。帳目一致：唯一 claim 數 1,174 ＝ 條目總數 1,174。
- Next pending claim by priority: `5251:material_named_relationship:7a2e178397650de7` (天鉞電).

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
