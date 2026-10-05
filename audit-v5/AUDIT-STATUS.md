# Audit v5 Status

Updated: 2026-10-05 14:08 UTC
Branch: `audit-v5`

## Semantic HIGH review

- HIGH issuers: **836**
- Raw HIGH signals: **1,410**
- Unique HIGH claims: **1,399**
- Author-reviewed: **20 / 1,399**
- Remaining author review: **1,379**
- Latest batch: **author-011** (2 claims)
- Independent reviews: **0**; author decisions are not final acceptance.

### Existing author decision counts

- `ACCEPTED`: **6**
- `PARTIALLY_SUPPORTED`: **10**
- `UNSUPPORTED`: **1**
- `PERIOD_UNRESOLVED`: **0**
- `SOURCE_UNAVAILABLE`: **3**
- `UNKNOWN_AFTER_RESEARCH`: **0**

## Latest claim batch

- `6757:objective_ranking_or_market_share:3c96889365c79805` — `PARTIALLY_SUPPORTED`; 台灣虎航114年度年報支持東北亞為主要客運營收區域、日本為客運營收占比最高市場、年輕客群、自由行/深度旅遊需求及日本二、三線城市航點；不支持把二、三線航點歸於東南亞，也未證明現行營運效率相對同業突出。
- `6757:objective_ranking_or_market_share:1cb894214a9355a5` — `ACCEPTED`; 年報載明20–39歲旅客占50.5%、主力客群平均年齡35.3歲，將航點規劃連結自由行需求，並稱日本為客運營收占比最高市場。
- 來源為台灣虎航官方資產網域上的114年度年報 PDF；證據、期間與摘記記錄於 `semantic/author-011.json`。未修改發行人報告。
- Next pending claim by priority: `4558:objective_ranking_or_market_share:e9efcd84b9b3989d`（寶緯）。

## Source access

The saved environment draft has `network_policy.type: unrestricted`; no configuration change was needed. Current-instance checks: Python 3.12 dependencies imported successfully, `git ls-remote origin HEAD` succeeded, and 長亨, TPEx, 台肥 and 華航 official pages returned HTTP 200. 台肥's annual report and company pages were inspectable; 華航's history and SkyTeam-anniversary announcement were inspectable. 興農 and CPC issuer pages returned HTTP 503; OCP official pages and the attempted USGS phosphate report returned HTTP 403. CAA pages were reachable but did not provide the attempted CPC airport-fuel supplier roster. MOPS' annual-report form loaded but the attempted 1712/ROC 113–114 query returned no viewable filing. A MOEA request timed out on a current retry. Earlier checks found the TWSE home page returned HTTP 503; a current TWSE OpenAPI retry did not return within the command window. No claim used search-result snippets as evidence.


## Transient retrieval failure handling

- Policy and append-only local recheck queue added; no local worker is implemented or run.
- Durable queue: **15 URL/failure entries**, all `LOCAL_RECHECK_PENDING`; **HTTP 500: 8**, **HTTP 503: 7**. These span 3 claims: 4558 (10 URLs), 1712 (3), and 2610 (2). The entries preserve Cloud observations and are idempotent by claim ID, normalized claim hash, exact URL, and failure signature.
- The currently unreviewed 4558 claim (`e9efcd84b9b3989d`) remains blocked on inspecting material official sources for its ranking/history qualifiers. The previous 1712 and 2610 author ledger decisions remain preserved unchanged; their `SOURCE_UNAVAILABLE` outcomes were recorded before this transient-failure policy and require a normal Codex Cloud semantic review if home-network retrieval later makes content inspectable. A home-network result alone cannot change those decisions.
- Relevant tests: `python -m unittest audit-v5/tests/test_semantic_local_recheck_queue.py` — 3 passed.
- No production files or author ledgers were changed.
