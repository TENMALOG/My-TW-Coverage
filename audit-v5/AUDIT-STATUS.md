# Audit v5 Status

Updated: 2026-10-08 10:04 UTC
Branch: `audit-v5`

## Semantic HIGH review

- HIGH issuers: **836**
- Raw HIGH signals: **1,410**
- Unique HIGH claims: **1,399**
- Author-reviewed: **468 / 1,399**
- Remaining author review: **931**
- Latest batch: **author-082** (7 claims)
- Independent reviews: **0**; author decisions are not final acceptance.

### Existing author decision counts

- `ACCEPTED`: **70**
- `PARTIALLY_SUPPORTED`: **307**
- `UNSUPPORTED`: **1**
- `PERIOD_UNRESOLVED`: **0**
- `SOURCE_UNAVAILABLE`: **3**
- `UNKNOWN_AFTER_RESEARCH`: **87**

## Latest claim batch

- `6464:objective_ranking_or_market_share:7ee6bae723c03229` — `PARTIALLY_SUPPORTED`；台數科文件載其為「**有線電視多系統經營者（MSO）**」（有線電視9次、MSO 1次）；惟「中部最大」「30萬」「訂戶」皆0次。
- `6625:objective_ranking_or_market_share:2ffa2be8731ab449` — `UNKNOWN_AFTER_RESEARCH`；必應111年報**文字層為亂碼**（第1頁「΋΋΋ԃࡋ」），無法判讀。
- `8487:objective_ranking_or_market_share:14898f3649f7c437` — `ACCEPTED`；愛爾達文件載「**以「體育轉播」為核心的新媒體**」並標示「**全台第一家**」「打造**台灣No.1 運動轉播大平台**」（體育20次、轉播17次、新媒體8次）。
- `6952:objective_ranking_or_market_share:ea612b92d7bf70a2`、`9f37dbda4677cd61` — `PARTIALLY_SUPPORTED` ×2；大武山年報「大成」1次、「卜蜂」1次；惟「市占」2次均為該公司自身目標敘述（擴大市占率、提高洗選鮮蛋市占率），未載同業市占率數字。
- `8345:objective_ranking_or_market_share:c3e3bf688a893fdd`、`f78f0cd9a0168655` — `PARTIALLY_SUPPORTED` ×2；超秦114年營業報告書見「**屠宰**」2次與進口雞肉供需失衡敘述；惟「北台灣」「家禽」「電宰」「1985」「74年」皆0次。
- 證據、期間、查閱日期與摘記記錄於 `semantic/author-082.json`（7 筆）。未修改發行人報告。
- Next pending claim by priority: `2885:objective_ranking_or_market_share:3f642a85d15abc7f` (元大金).

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
