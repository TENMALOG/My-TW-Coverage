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

Author-reviewed: **28 / 1,399** unique HIGH claims across batches `author-001` (8), `author-002` (1), `author-003` (1), `author-004` (2), `author-005` (1), `author-006` (1), `author-007` (1), `author-008` (1), `author-009` (1), `author-010` (1), `author-011` (2), `author-012` (1), `author-013` (3), `author-014` (2), and `author-015` (2).

- ACCEPTED by author: 7
- PARTIALLY_SUPPORTED: 17
- UNSUPPORTED: 1
- SOURCE_UNAVAILABLE: 3
- Other allowed author decisions: 0
- Remaining author queue: 1,371

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

## Author batch `author-005` — 2026-10-05

- Reviewed 1 previously unreviewed HIGH claim at claim level: `1722:objective_ranking_or_market_share:991de260b51083b7`.
- Decision: `PARTIALLY_SUPPORTED`. 台肥官網支持其持有土地約 170 公頃及南港開發方式；114 年度年報列出 C2、C3 案件，但查閱來源未支持「台北市最大地主」、3.58 萬坪或 150 億／逾 100 億元等排名與金額。
- Evidence URL、標題、來源層級、期間、查閱日期、evidence note 與 proposed wording 記錄於 `semantic/author-005.json`；未修改發行人報告。
- Author-reviewed total: 13 / 1,399; remaining author queue: 1,386. 獨立複核仍待處理。

## Author batch `author-006` — 2026-10-05

- Reviewed 1 previously unreviewed HIGH claim at claim level: `1722:objective_ranking_or_market_share:584c29afa2ffa73c`.
- Decision: `PARTIALLY_SUPPORTED`. 台肥官網支持其百分之百投資台灣海洋深層水股份有限公司，以及花蓮深層海水園區取水、瓶裝水與濃縮液產線；查閱的官方頁面未支持「亞洲最大」排名，且所列子公司名稱不同於原句。
- Evidence URL、標題、來源層級、期間、查閱日期、evidence note 與 proposed wording 記錄於 `semantic/author-006.json`；未修改發行人報告。
- Author-reviewed total: 14 / 1,399; remaining author queue: 1,385. 獨立複核仍待處理。

## Author batch `author-007` — 2026-10-05

- Reviewed 1 previously unreviewed HIGH claim at claim level: `1722:objective_ranking_or_market_share:7cd11cc6ee9fc2c7`.
- Decision: `SOURCE_UNAVAILABLE`. OCP Group 官網多個頁面回應 HTTP 403；USGS 官方磷礦摘要 PDF 端點也回應 HTTP 403，因此無法檢視能支持公司層級全球最大出口商排名的正式來源。
- 存取結果僅記錄來源限制，不代表排名為真或為假；完整來源 URL、標題欄位、來源層級、期間與證據摘記記錄於 `semantic/author-007.json`。
- Author-reviewed total: 15 / 1,399; remaining author queue: 1,384. 獨立複核仍待處理。

## Author batch `author-008` — 2026-10-05

- Reviewed 1 previously unreviewed HIGH claim at claim level: `1722:objective_ranking_or_market_share:fd708de33a7d0e86`.
- Decision: `PARTIALLY_SUPPORTED`. 台肥官網支持「農友牌」品牌，114 年度年報將農會列為肥料下游參與者；查閱來源未明確支持全台各級農會系統為最大經銷通路。
- Evidence URL、標題、來源層級、期間、查閱日期、evidence note 與 proposed wording 記錄於 `semantic/author-008.json`；未修改發行人報告。
- Author-reviewed total: 16 / 1,399; remaining author queue: 1,383. 獨立複核仍待處理。

## Author batch `author-009` — 2026-10-05

- Reviewed 1 previously unreviewed HIGH claim at claim level: `2610:objective_ranking_or_market_share:a74fba6da2dc6742`.
- Decision: `PARTIALLY_SUPPORTED`. 華航沿革支持 1959 年創立，官方新聞稿支持 2011 年加入天合聯盟；查閱頁面未明確支持台灣「最悠久」或「規模最大」的比較排名。
- Evidence URL、標題、來源層級、期間、查閱日期、evidence note 與 proposed wording 記錄於 `semantic/author-009.json`；未修改發行人報告。
- Author-reviewed total: 17 / 1,399; remaining author queue: 1,382. 獨立複核仍待處理。

## Author batch `author-010` — 2026-10-05

- Reviewed 1 previously unreviewed HIGH claim at claim level: `2610:objective_ranking_or_market_share:e790282c63b01303`.
- Decision: `SOURCE_UNAVAILABLE`. 台灣中油官網及業務頁回應 HTTP 503；可讀的民航局業者申辦與機場資料頁沒有航油供應商名冊或唯一供應商聲明。
- 存取結果只記錄來源限制，不代表中油是否為唯一供應商；完整 URL、標題、來源層級、期間與 evidence note 記錄於 `semantic/author-010.json`。
- Author-reviewed total: 18 / 1,399; remaining author queue: 1,381. 獨立複核仍待處理。


## Author batch `author-011` — 2026-10-05

- Reviewed 2 previously unreviewed HIGH claims for 台灣虎航 from its directly opened 114年度年報 PDF, hosted on the issuer's official asset domain.
- `6757:objective_ranking_or_market_share:3c96889365c79805` — `PARTIALLY_SUPPORTED`. The annual report supports Northeast Asia as the main passenger-revenue region, Japan as the highest passenger-revenue market, youth targeting, free-independent/deep-tourism demand, and Japanese second/third-tier city routes. It does not support describing those second/third-tier routes as Southeast Asian or current operations as outstanding in efficiency; the stated 11.2% per-seat cost reduction is a future A321neo plan.
- `6757:objective_ranking_or_market_share:1cb894214a9355a5` — `ACCEPTED`. The report identifies young customers (ages 20–39 are 50.5% of passengers; core customer average age 35.3), ties route planning to free-independent travel demand, and explicitly calls Japan the market with the highest passenger-revenue share. The ranking is supported on the report's stated revenue measure.
- Evidence and rationale are recorded in `semantic/author-011.json`; no issuer report was changed. Independent review remains pending.
- Author-reviewed total: 20 / 1,399; remaining author queue: 1,379. Next pending claim by priority: `4558:objective_ranking_or_market_share:e9efcd84b9b3989d` (寶緯).


## Transient retrieval failure policy checkpoint — 2026-10-05

Added an append-only, idempotent machine-readable queue at `semantic/local-recheck-queue.json` and the retrieval-failure rules in `SEMANTIC-REVIEW-POLICY.md`. HTTP 500–504 and equivalent connection failures are retrieval observations, not proof of source unavailability, IP blocking, absent evidence, or an unsupported claim. A future residential-network observation may establish availability only; it cannot overwrite Cloud history or make a semantic decision. No local worker was implemented or run.

The queue contains 15 URL/failure entries across 3 claims: HTTP 500 × 8 and HTTP 503 × 7. The reviewed 4558 claim has 10 affected official URLs in the availability queue. An inspected TPEx profile supports establishment in 1989 and aluminum-extrusion products, so history is supported; the ranking qualifier remains unsupported by inspected evidence. Existing author results for 1712 and 2610 (both previously `SOURCE_UNAVAILABLE`) remain unchanged; the new policy does not rewrite completed ledgers. If later content becomes inspectable, Codex Cloud must perform the semantic review under the normal process.

Current author-reviewed total is **21 / 1,399** (remaining **1,378**); outcomes are ACCEPTED 6, PARTIALLY_SUPPORTED 11, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 0. Relevant recheck queue tests passed: 3. The next claim in the existing author checkpoint order is `6175:objective_ranking_or_market_share:6b1aff5b9f087151` (normalized hash `6b1aff5b9f0871512323ef9e85860901e331e9c2c6ff20e008ab013b740c37ef`).


## Author batch `author-012` — 2026-10-05

- Reviewed the next unreviewed HIGH claim: `4558:objective_ranking_or_market_share:e9efcd84b9b3989d` (normalized hash `e9efcd84b9b3989da3693064b31fa64589ab4acb800e4007bcfe1dd0e3e4b661`).
- Decision: `PARTIALLY_SUPPORTED`. A directly inspected TPEx company-profile PDF states 宝緯 was established on 1989-03-09 and produces aluminum-extrusion products, supporting the product and 30+ year history portions. It contains no comparative ranking evidence for “one of Taiwan's largest.” The issuer and MOPS HTTP 500/503 observations did not determine the verdict.
- Proposed text and the TPEx PDF citation are recorded in `semantic/author-012.json`; no issuer report was modified. Its 10 failed official URLs remain in the availability-only local recheck queue; the recorded Cloud observations were preserved.
- Author-reviewed total: **21 / 1,399**; remaining: **1,378**. Outcome counts: ACCEPTED 6, PARTIALLY_SUPPORTED 11, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 0. Independent review remains pending.

## Author batch `author-013` — 2026-10-05

- Reviewed the next three unreviewed objective ranking/market-share claims, all for 立敦 (6175), following the documented priority order (objective ranking/market-share before material named relationships). All evidence came from directly downloaded and inspected official issuer disclosures and official/government pages; search snippets were discovery leads only.
- `6175:objective_ranking_or_market_share:6b1aff5b9f087151` (normalized hash `6b1aff5b9f0871512323ef9e85860901e331e9c2c6ff20e008ab013b740c37ef`) — `PARTIALLY_SUPPORTED`. 立敦113年度合併財務報告第13頁載明「立隆電子工業股份有限公司為本公司之母公司」，第76頁主要股東資訊列示立隆持股 29.04%（113.12.31）；立隆115年上半年合併財務報告第15頁列示民國114年投資比例由 29.21% 變動為 29.13%，並確認立隆自投資之日起為立敦單一最大股東，故「母公司為立隆電子，持股約 30%」可接受。惟「台灣車用電容市佔逾七成」不獲查閱之權威來源支持：立隆114年度年報正式的「市場占有率」段落僅稱其為台灣營收最高的鋁質電解電容器廠商、在台灣鋁電解電容產業居領先位置、依 Paumanok 2024年報告為2024年全球前十大鋁電廠商，未載明車用電容市占率；2026年第一季法說會所述汽車電子營收佔比36%與中央社所述2024年約33%均為營收結構占比，並非市占率。
- `6175:objective_ranking_or_market_share:0a838c414def37cd` — `ACCEPTED`. 日本ケミコン官方「事業概要」頁自述「アルミ電解コンデンサで世界トップシェア」並為「アルミ電解コンデンサの トップメーカー」；日本厚生労働省所屬ハローワーク2026年6月10日事業所文件獨立載明「主力製品のアルミ電解コンデンサは世界シェアナンバーワンです」。
- `6175:objective_ranking_or_market_share:08043f1f1f8247cf` — `PARTIALLY_SUPPORTED`. 領導廠商與下游主要電容廠之地位獲上述兩項來源支持；「全球市佔約 20%」之具體數值未獲權威來源確認（次級產業文章僅提供三家日商合計逾 40% 之敘述，依政策不得用以認定數值）。
- Proposed wording for the two partial claims is recorded in `semantic/author-013.json`; no issuer report was modified. Independent review remains pending; none of these author decisions is final acceptance.
- 檢索過程中僅遇兩次非關鍵取回異常：一個推測性的 liton.com.tw 舊版 PDF 網址回應 HTTP 500、一個舊版 MOPS 網址回應 404；兩者皆非本 claim 所需來源，未影響任何判定，故未達 `semantic/local-recheck-queue.json` 應記錄之重大失敗門檻。佇列維持 **15** 筆 `LOCAL_RECHECK_PENDING`（HTTP 500 × 8、HTTP 503 × 7），先前 Cloud 觀測未被覆寫。
- Author-reviewed total: **24 / 1,399**; remaining: **1,375**. Outcome counts: ACCEPTED 7, PARTIALLY_SUPPORTED 13, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 0. Next pending claim by priority: `8942:objective_ranking_or_market_share:271aa5af591a1811` (森鉅).

## Author batch `author-014` — 2026-10-05

- Reviewed the next two unreviewed objective ranking/market-share claims, both for 森鉅 (8942), following the documented priority order. Evidence came from directly downloaded and inspected issuer annual reports, official product documents and a U.S. SEC Form 10-K; search snippets were discovery leads only.
- `8942:objective_ranking_or_market_share:271aa5af591a1811` — `PARTIALLY_SUPPORTED`. 森鉅112年度年報（第71頁）正式「市場占有率」段落載明「本公司ALCOPLA 在室內板及室外板市場占有率約略為50%，北美市場廂式掛車市占率約60%」，直接支持約60%於112年度之表述；官方產品文件載明 G-BOND 鍍鋅鋼複合板與 A-BOND 高強度鋁塑複合板，並自述為「北美規模最大的金屬複合板生產商」。惟官方文件之範圍為北美最大／美國第一（2017年簡報另以「成為世界第一的卡車複合板材供應商」自我期許），未支持「全球…龍頭」；且最新114年度年報同一段落已更新為「北美市場廂式掛車市占率約50%」，60%並非現行數字。
- `8942:objective_ranking_or_market_share:96c34e1e0641bb89` — `PARTIALLY_SUPPORTED`. Wabash National FY2023 Form 10-K「Competitive Strengths」段落自述為拖車之「leading provider」及「one of the market leaders」，支持其為北美主要／領先拖車製造商；惟該正式申報未使用「最大」之最高級表述，亦未揭露可據以認定其為北美最大之市占數據。
- Proposed wording for both partial claims is recorded in `semantic/author-014.json`; no issuer report was modified. Independent review remains pending.
- 查證過程中 SEC EDGAR 之 HTML 端點以「Undeclared Automated Tool」回應 HTTP 403；該限制僅為檢索觀測，未用以推論 claim 真偽，已改以同一申報文件之 PDF 版本完成檢視，故未新增 `local-recheck-queue.json` 項目。佇列維持 **15** 筆。
- Author-reviewed total: **26 / 1,399**; remaining: **1,373**. Outcome counts: ACCEPTED 7, PARTIALLY_SUPPORTED 15, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 0. Next pending claim by priority: `1476:objective_ranking_or_market_share:f6132ace76c9ad00` (儒鴻).

## Author batch `author-015` — 2026-10-05

- Reviewed the next two unreviewed objective ranking/market-share claims (儒鴻 1476 and 聚陽 1477), following the documented priority order. Evidence came from directly downloaded and inspected official issuer annual reports, investor-conference decks and an official MOPS-hosted company profile; search snippets were discovery leads only.
- `1476:objective_ranking_or_market_share:f6132ace76c9ad00` — `PARTIALLY_SUPPORTED`. 儒鴻民國115年第二季法人說明會簡報第11頁「嚴格品質控制／國際認證」具名列示 Bluesign、ISO 14001、NIKE、ADIDAS，支持 NIKE 與儒鴻之國際品牌合作關係；惟114年度年報第112頁將最大客戶匿名為代號「A」（113年度14.12%、114年度16.44%、115年度截至前一季18.63%），全篇未出現 NIKE，且法人說明會簡報未揭露客戶營收占比或排名，故「最大客戶」此一最高級主張未獲查閱之權威來源確立。
- `1477:objective_ranking_or_market_share:7c3598761946783e` — `PARTIALLY_SUPPORTED`. 聚陽存放於公開資訊觀測站之民國114年官方公司簡介，第5頁「生產基地」列示 Vietnam、Indonesia、Cambodia、China、Philippines（另列 El Salvador、Bangladesh），第11頁全球網絡以產能揭示各國占比（2024年印尼40%、越南41%、柬埔寨15%、中國2%、菲律賓2%），直接支持 claim 所列五個生產基地；惟官方簡報自我定位為「亞太地區著名的全流程整合成衣製造商」，未作台灣境內排名陳述，故「台灣最大成衣 OEM/ODM 廠之一」未獲確立（同一族群中儒鴻2024年度營收37,989,751千元高於聚陽35,524百萬台幣）。
- Proposed wording for both partial claims is recorded in `semantic/author-015.json`; no issuer report was modified. Independent review remains pending.
- 檢索限制：嘗試以公開資訊觀測站年報端點取得聚陽112、113年度年報時，端點回傳 HTTP 200 但內容僅 320 bytes（非文件內容），故未取得該兩年度年報；此為檢索限制之紀錄，未用以推論 claim 真偽，亦未達 `local-recheck-queue.json` 應記錄之重大暫時性失敗門檻。佇列維持 **15** 筆。
- Author-reviewed total: **28 / 1,399**; remaining: **1,371**. Outcome counts: ACCEPTED 7, PARTIALLY_SUPPORTED 17, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 0. Next pending claim by priority: `4414:objective_ranking_or_market_share:cb90ae7e677cf480` (如興).



