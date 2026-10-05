# Audit v5 Status

Updated: 2026-10-07 13:04 UTC
Branch: `audit-v5`

## Semantic HIGH review

- HIGH issuers: **836**
- Raw HIGH signals: **1,410**
- Unique HIGH claims: **1,399**
- Author-reviewed: **341 / 1,399**
- Remaining author review: **1,058**
- Latest batch: **author-061** (3 claims)
- Independent reviews: **0**; author decisions are not final acceptance.

### Existing author decision counts

- `ACCEPTED`: **59**
- `PARTIALLY_SUPPORTED`: **214**
- `UNSUPPORTED`: **1**
- `PERIOD_UNRESOLVED`: **0**
- `SOURCE_UNAVAILABLE`: **3**
- `UNKNOWN_AFTER_RESEARCH`: **64**

## Latest claim batch

- `3037:objective_ranking_or_market_share:2416d3deb1742a86` — `PARTIALLY_SUPPORTED`; 欣興105年報「載板」27次、「PCB」34次、「聯電」1次；惟「全球最大」0次。
- `3037:objective_ranking_or_market_share:9b2f00b9af8d44c3` — `PARTIALLY_SUPPORTED`; IC載板業務與2026Q2簡報之「ABF」1次；惟「ABF」於105年報0次、「Ibiden」0次、「18%」未載。
- `3049:objective_ranking_or_market_share:6538e9d4932d6c19` — `ACCEPTED`; 精金年報載「瀚宇彩晶投資本公司」「正式為本公司**最大股東**」「**於98年6月16日董監事改選後，對本公司具控制力**」，並載觸控與彩色濾光片業務（觸控82次、彩色濾光片5次）。
- **新增產出：`semantic/unknown-followup.json`（UNKNOWN 追蹤清單）** — 彙整全部 `UNKNOWN_AFTER_RESEARCH` 之 HIGH claim，共 **64 筆**，含 claim_id、ticker、公司、claim 原文、所屬批次、失敗分類（failure_signature）、已嘗試來源網址與建議替代路徑。失敗分類統計：mops_non_document 24、non_document_response 22、http_404 21、no_official_endpoint_found 21、image_only_or_tiny_text 7、http_403 5、client_rendered_only 4、connection_failure 3、garbled_text_layer 3、download_timeout 2、other_unclassified 30（同一筆可屬多類）。
- 證據、期間、查閱日期與摘記記錄於 `semantic/author-061.json`（3 筆）。未修改發行人報告。
- Next pending claim by priority: `3060:objective_ranking_or_market_share:56574c45f5224560` (銘異).

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
