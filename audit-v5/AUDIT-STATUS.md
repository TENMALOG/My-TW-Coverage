# Audit v5 Status

Updated: 2026-10-08 18:04 UTC
Branch: `audit-v5`

## Semantic HIGH review

- HIGH issuers: **836**
- Raw HIGH signals: **1,410**
- Unique HIGH claims: **1,399**
- Author-reviewed: **527 / 1,399**
- Remaining author review: **872**
- Latest batch: **author-090** (7 claims)
- Independent reviews: **0**; author decisions are not final acceptance.

### Existing author decision counts

- `ACCEPTED`: **73**
- `PARTIALLY_SUPPORTED`: **347**
- `UNSUPPORTED`: **1**
- `PERIOD_UNRESOLVED`: **0**
- `SOURCE_UNAVAILABLE`: **3**
- `UNKNOWN_AFTER_RESEARCH`: **103**

## Latest claim batch

- `7765:objective_ranking_or_market_share:ca7dd7afc3bd6233`、`5ea2c57aff387b29` — `PARTIALLY_SUPPORTED` ×2；中華資安年報載「**本公司之母公司為中華電信股份有限公司**」（中華電信3次）；惟「ISP」「寬頻」「5G」「骨幹」「通路」皆0次。
- `2882:objective_ranking_or_market_share:bdb9b99f8967d1f7` — `PARTIALLY_SUPPORTED`；國泰金文件載「**臺灣最大金融控股公司之一**，總資產 NT$12.8兆元」；惟官方含「**之一**」、「資產規模最大」0次、「霖園集團核心」未載。
- `2882:objective_ranking_or_market_share:a2ee540a3626fa41` — `PARTIALLY_SUPPORTED`；文件載「**國泰人壽成立於1962年，為臺灣最大人壽保險公司**」；惟「最大機構投資者之一」未載。
- `2882:objective_ranking_or_market_share:cadef22332fa1adf` — `PARTIALLY_SUPPORTED`；文件載「國泰世華銀行 **CUBE卡**…**流通卡數近600萬張**…成為**國內最大宗的銀行卡**」；惟「房貸」0次、「財富管理」13次未載市占率、「發卡」0次。
- `2882:objective_ranking_or_market_share:214bbde45faed47f` — `PARTIALLY_SUPPORTED`；文件載子公司含國泰證券（54次）與國泰投信（43次）且「皆具產業領導地位」；惟「ETF」31次未以「最大ETF發行商」表述。
- `2883:objective_ranking_or_market_share:7060f1b3248b8161` — `UNKNOWN_AFTER_RESEARCH`；所取得檔案經確認**屬凱基期貨**之2024永續報告書（目錄載「關於凱基期貨」），非凱基金控文件。
- 證據、期間、查閱日期與摘記記錄於 `semantic/author-090.json`（7 筆）。未修改發行人報告。
- Next pending claim by priority: `2852:objective_ranking_or_market_share:4a5ef4fd4fdcb9d2` (第一保).

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
