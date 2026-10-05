# Audit v5 Status

Updated: 2026-10-15 23:04 UTC
Branch: `audit-v5`

## Semantic HIGH review

- HIGH issuers: **836**
- Raw HIGH signals: **1,410**
- Unique HIGH claims: **1,399**
- Author-reviewed: **1,371 / 1,399**
- Remaining author review: **28**
- Latest batch: **author-263** (8 claims)
- Independent reviews: **0**; author decisions are not final acceptance.

### Existing author decision counts

- `ACCEPTED`: **107**
- `PARTIALLY_SUPPORTED`: **822**
- `UNSUPPORTED`: **2**
- `PERIOD_UNRESOLVED`: **0**
- `SOURCE_UNAVAILABLE`: **3**
- `UNKNOWN_AFTER_RESEARCH`: **437**

## Latest claim batch

- 🟢 `4401:material_named_relationship:eb6a0ffaf7aac537` — **`ACCEPTED`**；東隆興簡報**逐字載**「(**POY or FDY**)」（**POY 1 次、FDY 1 次**）。
- `1341:export_concentration:68cf7713a01f37cf` — `PARTIALLY_SUPPORTED`；富林-KY簡報「**海防」8 次、「同奈」7 次、「越南」11 次、「內銷」1 次、外銷 2 次**；**惟「47%」之唯一上下文為「6.47%」——第 8 次子字串誤配**，且「東亞／亞洲」皆 0 次。
- `4401:material_named_relationship:fd1449426537e15a` — `PARTIALLY_SUPPORTED`；簡報**逐字載**客戶名單「Lululemon, Athleta, Fabletics, Alo, **Under Armour**, Vuori」「Lululemon, **Nike**, Dunning Golf, Helly Hansen」（**Lululemon 2、Nike 2、Adidas 1、Under Armour 1**）；**惟「核心供應商」0 次**。
- `4401:material_named_relationship:a0a73bc8e5775706` — `PARTIALLY_SUPPORTED`；**惟「Design-in」0 次**。
- `1444:material_named_relationship:5130f7ebb83abc71` — `PARTIALLY_SUPPORTED`；力麗年報「**Ecoya」2 次、「機能性」4 次**；**惟「原液染色／Apple」皆 0 次**。
- `1464:d334c64365468203` — `UNKNOWN_AFTER_RESEARCH`；得力簡報「**Under Armour／Adidas／Uniqlo」皆 0 次**（簡報僅2,120字元）。
- `1439:d6f665a3737f770e` — `UNKNOWN_AFTER_RESEARCH`；雋揚端點 **HTTP 404**。
- `1463:3409b6c7188c9f77` — `UNKNOWN_AFTER_RESEARCH`；未取得強盛新文件。
- 證據記錄於 `semantic/author-263.json`（8 筆）。未修改發行人報告。帳目一致：唯一 claim 數 1,371 ＝ 條目總數 1,371。**覆蓋率 98.00%**。
- Next pending claim by priority: `4406:material_named_relationship:95003ef6de91feba` (新昕纖).

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
