# Audit v5 Status

Independent-review update: 2026-10-06T01:17:15.066958Z
Branch: `audit-v5`

## Current independent-review checkpoint

- Author-reviewed: **1,399 / 1,399**; original author records preserved.
- Independently reviewed: **120 / 1,399**; unreviewed: **1279**.
- Author ACCEPTED coverage: **111 / 111**; remaining: **0**.
- Reviewer decisions: `{'PARTIALLY_SUPPORTED': 76, 'ACCEPTED': 22, 'UNSUPPORTED': 1, 'PERIOD_UNRESOLVED': 20, 'UNKNOWN_AFTER_RESEARCH': 1}`.
- Final states: `{'ESCALATED_REVIEW_DISAGREEMENT': 97, 'PARTIALLY_SUPPORTED': 2, 'ACCEPTED': 21}`.
- Final ACCEPTED: **21**, within recorded period and scope.
- Pending resolution: **1376** including **97** awaiting adjudication.
- Author ACCEPTED summary: [INDEPENDENT-REVIEW-ACCEPTED.md](INDEPENDENT-REVIEW-ACCEPTED.md); component amendment events: **1**.
- Latest batch: `semantic/reviewer-006.json`; report: [INDEPENDENT-REVIEW-006.md](INDEPENDENT-REVIEW-006.md).
- Original 1,399 author final_state / independent_review values remain null. Original reports and Cloud failure queue unchanged.
- PDF/HTML raw sources remain in ignored local caches; separate verified source package required for paper publication.

## Preserved author-status snapshot

The following is the prior author snapshot. Its reported 2026-10-16 timestamp is future-dated relative to this review on 2026-10-06 and has not been independently verified. Its zero-review count is historical, not the current reviewer checkpoint. No historical acquisition dates have been reconstructed.

# Audit v5 Status

Updated: 2026-10-16 02:04 UTC
Branch: `audit-v5`

## Semantic HIGH review

- HIGH issuers: **836**
- Raw HIGH signals: **1,410**
- Unique HIGH claims: **1,399**
- Author-reviewed: **1,399 / 1,399**
- Remaining author review: **0**
- Latest batch: **author-266** (16 claims)
- Independent reviews: **0**; author decisions are not final acceptance.

### Existing author decision counts

- `ACCEPTED`: **111**
- `PARTIALLY_SUPPORTED`: **833**
- `UNSUPPORTED`: **2**
- `PERIOD_UNRESOLVED`: **0**
- `SOURCE_UNAVAILABLE`: **3**
- `UNKNOWN_AFTER_RESEARCH`: **450**

## Latest claim batch

- 🟢 `9926:material_named_relationship:9ee2a3f7848520f1`、`73633ab28e6947bb` — **`ACCEPTED` ×2**；新海年報**逐字載**「**註：本公司氣源由台灣中油公司獨家供應。**」（**中油 21 次、獨家 3 次、天然氣 176 次**）。
- `9908:material_named_relationship:9ee2a3f7848520f1`、`73633ab28e6947bb` — `PARTIALLY_SUPPORTED` ×2；大台北年報載「**中油**氣源成本」「**中油**公司**供應**之天然氣」（**中油 21 次、天然氣 142 次**）；**惟「獨家」0 次**。
- `9931:material_named_relationship:9ee2a3f7848520f1`、`73633ab28e6947bb` — `PARTIALLY_SUPPORTED` ×2；欣高文件載「本公司自**中油**公司接氣」（**中油 13 次**）；**惟「獨家」0 次**。
- `8908:material_named_relationship:9ee2a3f7848520f1`、`73633ab28e6947bb` — `UNKNOWN_AFTER_RESEARCH` ×2；欣雄簡報「**中油／CPC／獨家」皆 0 次**。
- `8917:material_named_relationship:9ee2a3f7848520f1`、`73633ab28e6947bb`、`9918:material_named_relationship:9ee2a3f7848520f1`、`73633ab28e6947bb` — `UNKNOWN_AFTER_RESEARCH` ×4；欣泰與欣天然未取得可檢視之官方文件。
- `5604:identity_changing_event:b3e57d29547603cf` — `PARTIALLY_SUPPORTED`；中連誠簡報「**中連誠」4 次、「不動產」17 次、「租賃」12 次**；**惟「更名／2021」皆 0 次**。
- `8087:identity_changing_event:edf6dae43adbf07e` — `PARTIALLY_SUPPORTED`；麗升文件「**華鎂鑫」31 次、「麗升」129 次**；**惟「更名」1 次之上下文為「股票之更名過戶」（語意歸屬錯置）**。
- `6624:material_named_relationship:9427141aad3f581c` — `PARTIALLY_SUPPORTED`；萬年清ESG「**廢水」92 次**；**惟「半導體／封裝／台積電」皆 0 次**。
- `8476:material_named_relationship:1f56f40e7746d7f1` — `PARTIALLY_SUPPORTED`；台境簡報載「案例-**中油**污染土處理場址」（**污染 11 次、整治 14 次**）；**惟「台電」0 次**。
- 證據記錄於 `semantic/author-266.json`（**16 筆**）。未修改發行人報告。帳目一致：唯一 claim 數 1,399 ＝ 條目總數 1,399。
- ✅ **作者審核階段完成：1,399 / 1,399（100.00%）。待辦之作者 claim 為 0 筆；後續為獨立複核階段（`final_state` 仍為 null，全帳本 1,399 筆皆為 null）。**
- **帳本一致鍵驗證**：唯一 claim 數 1,399 ＝ 條目總數 1,399；缺 `normalized_claim_hash` 者 **0**、與佇列不符者 **0**。**（2026-10-16 補齊 `author-001` 之欄位缺口，未更動任何判定。）**

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
