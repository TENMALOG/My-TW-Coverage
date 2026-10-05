# Semantic HIGH Verification Report

Status: **IN PROGRESS**
Date: 2026-10-05
Branch: `audit-v5`

## Queue normalization

- Calibrated HIGH issuers: 836
- Raw HIGH signals: 1,410
- Unique HIGH claims after stable claim-level deduplication: 1,399
- Duplicate signal instances removed from semantic workload: 11

Signal mix (unique claims): objective ranking/market share 941; material named relationship 317; profitability 67; identity-changing event 42; export concentration 27; control acquisition 5.

## Author review progress

Author-reviewed: **12 / 1,399** unique HIGH claims across batches `author-001` (8), `author-002` (1), `author-003` (1), and `author-004` (2).

- ACCEPTED by author: 5
- PARTIALLY_SUPPORTED: 5
- UNSUPPORTED: 1
- SOURCE_UNAVAILABLE: 1
- Other allowed author decisions: 0
- Remaining author queue: 1,387

Notable correction: the report claim that Green Jade is Asia's largest is contradicted by current official CDWE material, which describes it as the largest Taiwan-flagged vessel and Asia's second-largest wind-power engineering vessel. Proposed repair is recorded in `semantic/author-001.json`.

Other partial findings: AIDC evidence supports 燁鋒 as an aerospace raw-material/aluminum supplier but not the exact 'Asia's only' ranking; inspected evidence supports China Steel as a plate supplier to Jong Shyn but not yet the qualifier 'major'.

## Independent review

Final HIGH acceptance remains pending independent reviewer separation. An attempted GitHub Models reviewer was not used because GitHub Models inference was retired on 2026-07-30. The retired endpoint returned plain `OK` rather than model inference. The automatic reviewer workflow has therefore been disabled instead of fabricating reviewer results.

Until a genuinely independent model/session is available, author decisions remain author decisions; `final_state` must not be promoted to final ACCEPTED solely from this ledger.

## Next execution order

Continue author verification claim-by-claim, prioritizing objective ranking/market-share assertions, then material named relationships, profitability assertions, identity-changing events, export concentration and control acquisitions. Reuse inspected authoritative evidence only when issuer, claim, period and qualifier all match.

## Execution checkpoint — 2026-10-05 12:42 UTC

- No new claims were reviewed in this execution; no claim decisions or evidence records were added.
- Existing author ledger remains 8 reviewed claims; author queue remains 1,391 claims.
- Next pending claim by the required priority order: `2645:objective_ranking_or_market_share:acb07c2f05995949` (長榮航太; normalized hash `acb07c2f05995949a72a6d0c190e016489fc3dc71f58f1f9990154e19b09035c`).
- Research stopped before the first batch because HTTPS requests to official-source hosts `www.aidc.com.tw`, `www.twse.com.tw`, `www.moea.gov.tw`, and `www.mops.twse.com.tw` were rejected by the environment egress proxy with `CONNECT tunnel failed, response 403`. These connectivity probes are not evidence about any claim.
- No claim was assigned `SOURCE_UNAVAILABLE`; target-specific authoritative source pages were not inspectable. Resume only after a live official-source research route is available. Search snippets alone remain insufficient under policy.

## Author batch `author-002` — 2026-10-05

- Reviewed 1 previously unreviewed HIGH claim at claim level: `2645:objective_ranking_or_market_share:acb07c2f05995949`.
- Decision: `PARTIALLY_SUPPORTED`. EGAT's current official profile supports service to more than 40 airlines; its maintenance page lists B747-400/B747-8 and more than 2,500 major airframe maintenance jobs. Inspected pages do not assert the “world's largest” ranking or support every aircraft type and expansion statement in the original claim.
- Proposed wording is recorded in `semantic/author-002.json`; the issuer report was not edited.
- Author-reviewed total: 9 / 1,399; remaining author queue: 1,390. Independent review remains pending.
- The unrestricted egress retest allowed direct access to the EGAT pages, TPEx, MOEA and AIDC. The TWSE home page returned 503; MOPS returned a security-denial page despite HTTP 200. The TWSE company-directory OpenAPI returned data but was slow to download.

## Author batch `author-003` — 2026-10-05

- Reviewed 1 previously unreviewed HIGH claim at claim level: `4546:objective_ranking_or_market_share:db06b1cb4d0d13e1` (normalized hash `db06b1cb4d0d13e1697ff1cc445e8970d8fa60b545a2207c31dd027eb5cbe193`).
- Decision: `PARTIALLY_SUPPORTED`. 長亨官網明確聲稱產品均 100% 外銷歐美大廠，並列出多項全球市占第一的引擎零組件；查閱頁面未支持 Safran 與 GE Aerospace 為主要客戶。
- Evidence URL、標題、來源層級、期間、查閱日期與證據摘記，以及 proposed wording，均記錄於 `semantic/author-003.json`。未修改發行人報告。
- Author-reviewed total: 10 / 1,399; remaining author queue: 1,389. 獨立複核仍待處理。
- 當次直接來源連線測試中，長亨官網與 TPEx 回應 HTTP 200；MOEA 請求逾時。這些連線結果不是 claim evidence。

## Author batch `author-004` — 2026-10-05

- Reviewed 2 previously unreviewed HIGH claims at claim level: `1712:objective_ranking_or_market_share:ababe1bd116826cb` and `1722:objective_ranking_or_market_share:82710f0ae62b4476`.
- `1712` decision: `SOURCE_UNAVAILABLE`. 興農官網直接請求回應 HTTP 503；MOPS 年報查詢沒有返回可檢視的公司文件。此結果只表示本次無法取得來源，不代表 claim 為真或為假。
- `1722` decision: `PARTIALLY_SUPPORTED`. 台肥 114 年度年報明確稱其為國內最大肥料生產、供應者；官網名單支持農業部於 2026-03-29 持股 24.07% 並列最大股東，但年報未明確支持國內市占約 70%。
- 完整 evidence 與 proposed wording 記錄於 `semantic/author-004.json`；沒有修改發行人報告。
- Author-reviewed total: 12 / 1,399; remaining author queue: 1,387. 獨立複核仍待處理。
- 本次已直接開啟台肥官網並下載、檢視 114 年度年報 PDF；興農與 MOPS 公司年報內容仍無法檢視。
