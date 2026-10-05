# Audit v5 Status

Updated: 2026-10-06 03:04 UTC
Branch: `audit-v5`

## Semantic HIGH review

- HIGH issuers: **836**
- Raw HIGH signals: **1,410**
- Unique HIGH claims: **1,399**
- Author-reviewed: **117 / 1,399**
- Remaining author review: **1,282**
- Latest batch: **author-027** (8 claims)
- Independent reviews: **0**; author decisions are not final acceptance.

### Existing author decision counts

- `ACCEPTED`: **31**
- `PARTIALLY_SUPPORTED`: **70**
- `UNSUPPORTED`: **1**
- `PERIOD_UNRESOLVED`: **0**
- `SOURCE_UNAVAILABLE`: **3**
- `UNKNOWN_AFTER_RESEARCH`: **12**

## Latest claim batch

- `2880:objective_ranking_or_market_share:bea17a5f1d280fb1` — `ACCEPTED`; 華南金2022永續報告第22頁載「為臺灣第一家成立之金融控股公司。於2001年12月19日，由華南商業銀行及永昌綜合證券以股權轉換方式設立」。
- `2880:objective_ranking_or_market_share:a7669e207f28c0b5` — `ACCEPTED`; 同報告第24頁股東結構載「本公司最大股東為臺灣銀行（持股占比21.23%）」，臺灣銀行為財政部100%持有，故財政部透過臺灣銀行間接為最大股東之敘述與官方揭露一致。
- `2886:objective_ranking_or_market_share:a7669e207f28c0b5` — `PARTIALLY_SUPPORTED`; 兆豐金112年報第73頁主要股東名單第1名為財政部8.20%、臺灣銀行僅第5名2.62%，故財政部為直接最大股東，「透過臺灣銀行間接」之機制描述不符。
- `2886:objective_ranking_or_market_share:6bbc731aba29c26b` — `PARTIALLY_SUPPORTED`; 中央銀行新聞稿標題「兆豐銀行續任『外幣結算平台』美元清算銀行」支持其清算銀行地位，兆豐金112年報載「維持聯貸市場優勢地位」支持聯貸優勢；惟新聞稿內文未擷取到，「台灣唯一」未獲確認。
- `2890:objective_ranking_or_market_share:2ec04a9365b56c0f` — `ACCEPTED`; 永豐金2022公司簡介第4頁「2022年3月底太陽能設備融資市占維持第一(25.5%)」。
- `2890:objective_ranking_or_market_share:298eb00d61c6591a`、`92485629cda4cfea` — `UNKNOWN_AFTER_RESEARCH` ×2; 永豐金2022公司簡介中「上櫃」出現0次、無據點數，Amret與柬埔寨亦為0次（事件發生於該文件之後）。
- `2892:objective_ranking_or_market_share:a7669e207f28c0b5` — `PARTIALLY_SUPPORTED`; 第一金現增公開說明書第57頁主要股東名單第1名財政部13.35%、臺灣銀行第2名7.72%，故財政部為直接最大股東，「透過臺灣銀行間接」不符（基準日民國104年）。
- 證據、期間、查閱日期與摘記記錄於 `semantic/author-027.json`。未修改發行人報告。
- Next pending claim by priority: `2892:objective_ranking_or_market_share:ed08854a9f3fb74e` (第一金).

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
