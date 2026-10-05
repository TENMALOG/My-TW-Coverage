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

Author-reviewed: **117 / 1,399** unique HIGH claims across batches `author-001` (8), `author-002` (1), `author-003` (1), `author-004` (2), `author-005` (1), `author-006` (1), `author-007` (1), `author-008` (1), `author-009` (1), `author-010` (1), `author-011` (2), `author-012` (1), `author-013` (3), `author-014` (2), `author-015` (2), `author-016` (3), `author-017` (6), `author-018` (7), `author-019` (8), `author-020` (8), `author-021` (10), `author-022` (8), `author-023` (7), `author-024` (9), `author-025` (7), `author-026` (8), and `author-027` (8).

- ACCEPTED by author: 31
- PARTIALLY_SUPPORTED: 70
- UNSUPPORTED: 1
- SOURCE_UNAVAILABLE: 3
- Other allowed author decisions: 12
- Remaining author queue: 1,282

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

## Author batch `author-016` — 2026-10-05

- Reviewed the next three unreviewed objective ranking/market-share claims in checkpoint order (如興 4414, 銘旺實 4432, 廣越 4438). Evidence came from directly downloaded and inspected issuer investor-conference decks, an annual report PDF and an official website; search snippets were discovery leads only.
- `4414:objective_ranking_or_market_share:cb90ae7e677cf480` — `PARTIALLY_SUPPORTED`. 如興民國114年法說會簡報第11頁標題「全球布局之牛仔褲專業製造商」，第8頁列示被收購公司「玖地製造有限公司及Tooku Holdings Limited」之商譽與客戶關係明細（收購溢價合計8,582,580仟元），支持牛仔褲製造商定位與玖地收購事實；惟第4頁自述為「全球前三牛仔成衣廠」，未支持「全球最大」；2024年全年銷量60,913仟件、2025年前三季42,932仟件，與 claim 所述1.2億件訂單／9,000萬件製造量及市佔10%／8% 不符。
- `4432:objective_ranking_or_market_share:5839812e308b4ea7` — `UNKNOWN_AFTER_RESEARCH`. 銘旺實113年度年報第87頁以代號揭露銷貨客戶：客戶甲占29.38%、客戶乙11.61%、客人丙11.05%、客戶丁10.96%，第98頁載「113年度大客戶佔比最大客戶超過29%」；231頁年報與官方網站均未出現 Under Armour。客戶身分未揭露，其占比亦與 claim 所述「約20%」不一致，既無法確認亦無證據否定，依政策以 UNKNOWN_AFTER_RESEARCH 結案。
- `4438:objective_ranking_or_market_share:05ea182e0e761907` — `PARTIALLY_SUPPORTED`. 廣越2025年11月官方法說會簡報第14頁載「成立於1995年」；惟第15頁標題為「廣越為全球前三大高端戶外機能服飾製造商」，第14頁自述「全球領先的高端機能服飾及羽絨衣製造商」，均未使用「最大」，故「全球最大高階羽絨外套製造商」不成立（2024年產品組合中羽絨夾克占34.53%）。
- Proposed wording for the two partial claims is recorded in `semantic/author-016.json`; no issuer report was modified. Independent review remains pending.
- 檢索紀錄：如興官網 `/data/qa/` 端點因 TLS 憑證信任問題無法下載（僅為檢索限制，未用以推論 claim）；銘旺實官網首次比對 Under Armour 時因未加字詞邊界而誤判，經逐一取出出現位置後確認為零命中，已改正。上述均未達 `local-recheck-queue.json` 應記錄之重大暫時性失敗門檻，佇列維持 **15** 筆。
- Author-reviewed total: **31 / 1,399**; remaining: **1,368**. Outcome counts: ACCEPTED 7, PARTIALLY_SUPPORTED 19, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 1. Next pending claim by priority: `8932:objective_ranking_or_market_share:39298f531ff2064c` (智通).

## Author batch `author-017` — 2026-10-05

- Reviewed the next six unreviewed objective ranking/market-share claims in checkpoint order (智通 8932 ×2, 和泰車 2207 ×4). Evidence came from directly downloaded and inspected official issuer disclosures: 智通 2024永續報告書與2024年法說會簡報, YKK《This is YKK 2025》統合報告書, 和泰汽車 Annual Report 2025 與2025年第4季法說會簡報.
- `8932:objective_ranking_or_market_share:39298f531ff2064c` — `PARTIALLY_SUPPORTED`. 智通2024永續報告書第17頁載公司原名宏大拉鏈、創立於1978年，並載2023年6月中文名稱變更為智通科創；第18與21頁載MAX產品線（尼龍、塑鋼、金屬、隱形拉鍊及配件）與客戶群（Wal-Mart、Target、JCPenney、MACYS、Kohl's 等）。惟官方一貫敘述為「兩大核心事業體」（MAX拉鍊與GLN軟體），非「三大事業體」；「Toyota等60餘家汽車品牌」不獲支持（官方為「近60個國際大型品牌認證」，涵蓋成衣箱包，文件中未出現 Toyota）；更名時點官方為2023年6月，非 claim 所述9月。
- `8932:objective_ranking_or_market_share:2c4e8e723b5b77d9` — `PARTIALLY_SUPPORTED`. YKK《This is YKK 2025》第11頁載2014年獲 Porter Prize 之「global leader in zippers」，第58頁載業務遍及70國、拉鍊年產能逾300萬公里、FY2024淨銷售4,331億日圓，支持其日本企業與全球拉鏈領導地位；惟全報告未揭露全球市占率百分比，「市佔約35%」未獲確立。
- `2207:objective_ranking_or_market_share:12f16578b4009931` — `ACCEPTED`. 和泰年報第112頁載多年持續位居汽車產業市場領先；第87頁載其為 Toyota 在台 exclusive distributor；第132頁載與 TMC（TOYOTA/LEXUS）及 Hino Motors 之代理合約；第14頁載2025年三品牌合計登錄逾16萬台、市佔38.6%（近16年最高），TOYOTA 30.1%。法說會第15頁載「蟬聯台灣車市冠軍24年」。「約40%」與官方38.6%相當。
- `2207:objective_ranking_or_market_share:ea263c42d696e282` — `ACCEPTED`. 年報第121頁主要原料供應表將 TOYOTA 與 HINO 之國內供應商均列為 Kuozui Motors, Ltd.，且未列其他國內製造商；第132頁 Product Sales Agreement 載國瑞提供授權製造車輛、零件與配件供和泰在台銷售；第139頁載 TMC 與國瑞負責產品製造與研發。
- `2207:objective_ranking_or_market_share:41ac99c4757c51d2` — `ACCEPTED`. 與 ea263c42d696e282 同源證據之供應鏈條目表述，支持「國瑞汽車 — Toyota/Hino 台灣唯一組裝廠」。
- `2207:objective_ranking_or_market_share:f0cf847d4e06fec3` — `PARTIALLY_SUPPORTED`. 官方揭露之2025年38.6%係 TOYOTA、LEXUS、HINO 三品牌合計口徑；TOYOTA 單一品牌30.1%、LEXUS 於豪華車市場28.0%、HINO 與 TOYOTA 商用車37.6%。claim 以「Toyota、Lexus 品牌」為範圍與官方三品牌合計口徑不符，故僅部分成立。
- Proposed wording is recorded for the partial claims in `semantic/author-017.json`; no issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆 `LOCAL_RECHECK_PENDING`（HTTP 500 × 8、HTTP 503 × 7），Cloud 觀測未被覆寫。
- Author-reviewed total: **37 / 1,399**; remaining: **1,362**. Outcome counts: ACCEPTED 10, PARTIALLY_SUPPORTED 22, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 1. Next pending claim by priority: `2206:objective_ranking_or_market_share:2206926921111339` (三陽工業).

## Author batch `author-018` — 2026-10-05

- Reviewed the next seven unreviewed objective ranking/market-share claims in checkpoint order (三陽工業 2206 ×3, 東陽 1319 ×4). Evidence came from directly downloaded and inspected official disclosures: 三陽 2026 QIC CEO Week 簡報與2022 ESG 永續報告書、東陽 2020/2021/2022 永續報告書、LKQ Corporation FY2025 與 FY2024 Form 10-K（SEC EDGAR）及 LKQ 官方 Keystone 品牌頁。
- `2206:objective_ranking_or_market_share:2206926921111339` — `PARTIALLY_SUPPORTED`. 簡報第3頁標題「台灣摩托車與汽車製造的領導者」，第4頁載業務橫跨摩托車與汽車、機車部門在台生產自有品牌SYM、汽車部門生產並引進現代汽車產品，第3頁載新竹廠30萬輛機車與2萬輛汽車產能，支持雙製造能力；惟「台灣唯一」未獲官方陳述。
- `2206:objective_ranking_or_market_share:63ed0282b9ad9374` — `ACCEPTED`. 簡報第4頁載2025年三陽自有品牌摩托車占台灣市場44.3%的份額、2022年5月重返台灣機車品牌第一名；第15頁載外銷版圖橫跨中國、東協、東北亞、歐洲及美洲，並明載「三陽也幫義大利品牌Lambretta 以及法國品牌Peugeot 等代工生產」；ESG報告另載SYM共85個外銷國家。
- `2206:objective_ranking_or_market_share:f1d0e04eae11fc9f` — `PARTIALLY_SUPPORTED`. 簡報第4頁載汽車部門「生產以及引進韓國現代汽車的產品進入台灣市場」，ESG報告載三陽與HYUNDAI策略聯盟、以生產技術提供國產HYUNDAI汽車並透過直接管理之子公司提供銷售與維修；惟官方未以「獨家總代理」描述三陽本身，且第17頁載2025年現代汽車台灣市占率4.55%（排名第5、非豪華乘用品牌第三名），未見「市佔率屢創新高」之陳述。
- `1319:objective_ranking_or_market_share:92d37f3eb1beade9` — `PARTIALLY_SUPPORTED`. 東陽2022永續報告第31頁載其為「全球最大的汽車塑膠AM供應廠」及「全球AM鈑金供應龍頭」，第54頁載其為AM市場最大製造供應商與台灣汽車塑膠件最大OEM供應商，第62頁載客戶遍及五大洲超過200個國家、2,300個客戶；惟2020、2021、2022三份報告書均未出現「70%」或「35%」之市占率數字，兩個百分比未獲確立。
- `1319:objective_ranking_or_market_share:2a6fc80138e4eb21` — `PARTIALLY_SUPPORTED`. LKQ FY2025 Form 10-K 載其北美部門營運北美最大的替代性車輛零件與配件配送網路，LKQ 官方品牌頁載 Keystone 為其子公司與美國最大售後零件供應商，支持 LKQ／Keystone 之通路地位；惟東陽2020至2022年報告書中 LKQ、Keystone 與 State Farm 出現次數均為0，東陽特定經銷夥伴關係與保險公司效應未獲支持。
- `1319:objective_ranking_or_market_share:40b14c614d7aad1a` 與 `4f8e5c27889374aa` — `ACCEPTED`. 同一事實之兩處條目表述，由 LKQ 10-K 與官方品牌頁支持。
- Proposed wording is recorded for the partial claims in `semantic/author-018.json`; no issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆 `LOCAL_RECHECK_PENDING`（HTTP 500 × 8、HTTP 503 × 7），Cloud 觀測未被覆寫。
- Author-reviewed total: **44 / 1,399**; remaining: **1,355**. Outcome counts: ACCEPTED 13, PARTIALLY_SUPPORTED 26, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 1. Next pending claim by priority: `2237:objective_ranking_or_market_share:ee7593a1bc4fa73e` (華德動能).

## Author batch `author-019` — 2026-10-05

- Reviewed the next eight unreviewed objective ranking/market-share claims in checkpoint order (華德動能 2237, 台翰 1336 ×2, 廣華-KY 1338 ×2, 昭輝 1339 ×2, 正道 1506). Evidence came from directly downloaded and inspected official disclosures: 華德動能投資人簡報、台翰113年度年報、廣華控股2025年公司簡介、昭輝2020/2024/2026法人說明會簡報、正道工業官方NASA技術頁與107年度年報、LKQ FY2025 Form 10-K 與官方 Keystone 品牌頁。
- `2237:objective_ranking_or_market_share:ee7593a1bc4fa73e` — `PARTIALLY_SUPPORTED`. 官方簡報第5頁載2011年台灣第一輛電動巴士上路、2019年首家取得電動巴士自主設計開發資格、2024年首輛市區公車電動化方案出口日本東京；惟「國內市佔率約30%」、「累計逾500輛」、「台灣首家通過認證之純電動巴士廠商」均未見於簡報（官方僅載台灣APTS市佔率超過80%）。
- `1336:objective_ranking_or_market_share:cee272854eaffb62` 與 `fe2d9e60f44aa914` — `ACCEPTED`. 台翰113年度年報主要股東名單列宣德科技22,599,000股、29.12%為最大股東；第10頁揭露宣德科技之主要股東為香港商聯滔電子有限公司（24.59%），而香港商聯滔電子之主要股東為立訊精密工業股份有限公司（100%），支持最大股東與最終母公司之認定。
- `1338:objective_ranking_or_market_share:666e6bac07f9b5a5` 與 `043acc8984fdcb88` — `ACCEPTED`. 廣華控股2025年官方簡報第15頁載2024年客戶結構日系46%、中國28%、歐美25%、其他1%；日系明細含東風日產／日本日產與東風本田／廣汽本田，日系營收百分比為日產34%、豐田6%、本田5%、SUBARU1%，日產為最大單一品牌。
- `1339:objective_ranking_or_market_share:375175af06d90a6f` — `UNKNOWN_AFTER_RESEARCH`. 昭輝2026年8月、2024年12月與2020年7月三個版本官方簡報均未出現 LKQ、Keystone、CAPA、N Group 或客戶集中度文字；公開資訊觀測站108至113年度年報端點均回應 HTTP 200 但內容僅320 bytes，未能檢視年報。三項具體陳述無法確認亦無證據否定。
- `1339:objective_ranking_or_market_share:8c262157716b38f8` — `PARTIALLY_SUPPORTED`. LKQ FY2025 Form 10-K 載其北美部門營運北美最大替代性車輛零件配送網路，官方品牌頁載 Keystone 為 LKQ 子公司與美國最大售後零件供應商；惟括號中「合計佔營收50%+」為昭輝客戶集中度，未獲其官方來源支持。
- `1506:objective_ranking_or_market_share:b7bdbc426ed03c94` — `PARTIALLY_SUPPORTED`. 正道官方「NASA高性能鋁合金活塞」頁載其取得NASA授權、為全球唯一有量產實績的專業NASA活塞生產廠商、每年製造NASA鋁合金活塞超過20萬個；惟同頁明載鍛造版本係「近期…延伸開發第一顆NASA鍛造鋁合金活塞」，年產20萬顆係對應其鑄造經驗，claim 將鑄造量產與鍛造混為一談。
- Proposed wording is recorded for the partial claims in `semantic/author-019.json`; no issuer report was modified. Independent review remains pending.
- 來源檢索限制：昭輝年報端點連續六個年度皆回傳非文件內容；此為檢索限制之紀錄，未用以推論 claim 真偽，亦未達 `local-recheck-queue.json` 之重大暫時性失敗門檻。佇列維持 **15** 筆。
- Author-reviewed total: **52 / 1,399**; remaining: **1,347**. Outcome counts: ACCEPTED 17, PARTIALLY_SUPPORTED 29, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 2. Next pending claim by priority: `1521:objective_ranking_or_market_share:b0344d1922014380` (大億).

## Author batch `author-020` — 2026-10-05

- Reviewed the next eight unreviewed objective ranking/market-share claims in checkpoint order (大億 1521, 堤維西 1522 ×2, 耿鼎 1524 ×3, 江申 1525 ×2). Evidence came from directly downloaded and inspected official disclosures: 大億 112/114年度年報、堤維西2023永續報告書與2026法說會簡報、耿鼎111/112年度年報與2025公司簡報、江申115年股東會年報與2019企業社會責任報告書。
- `1521:objective_ranking_or_market_share:b0344d1922014380` — `PARTIALLY_SUPPORTED`. 大億114年度年報第57頁載「2.市場佔有率：國內約為80%」，112年度年報第71頁載「國內為80%」，且公司以OEM客戶為主要合作對象，支持其為台灣OEM車燈市場領先者；惟 claim 所述「72%」與官方約80%不符，應以官方數字為準。
- `1522:objective_ranking_or_market_share:c39cb97e670a83a1` — `PARTIALLY_SUPPORTED`. 堤維西2023永續報告第22頁載其為「全球領先OEM車廠及AM售服市場的夥伴與供應商之一」、以TYC品牌行銷全球130多個國家；惟「北美AM車燈市場市佔約12%」與「位居全球前五大」均未見於官方報告與2026法說會簡報（報告中唯一12%為荷蘭外銷占營收約12%）。
- `1522:objective_ranking_or_market_share:9f7b131fa64ec7b2` — `PARTIALLY_SUPPORTED`. 官方簡報僅載TYC自建之加州總部與五個北美發貨倉，未具名 LKQ 等經銷商，亦未載12%市佔；經銷關係與市占數字均未獲確立。
- `1524:objective_ranking_or_market_share:37a66df6e8c59992`、`3fdf0568b0589c62`、`7bfdfa0fb2fba733` — `PARTIALLY_SUPPORTED` ×3. 耿鼎112年度年報第9頁載民國105年獲「LKQ 供應商評估獎」（LKQ 為客戶）、第57頁載其為「北美地區最主要的汽車售後服務(AM)鈑金件供應商之一」；惟第59頁銷貨客戶表以代號揭露（112年度最大客戶為客戶A、占銷貨淨額24.66%），未具名 LKQ，「市佔近40%」亦無官方依據（相關40.6%為耿鼎自身銷售區域結構）。
- `1525:objective_ranking_or_market_share:fd492ed31d1ccf47`、`67775914202401b9` — `PARTIALLY_SUPPORTED` ×2. 江申2019企業社會責任報告第10頁載其「為國內目前最大商用車車架生產公司」、產品涵蓋商用車3.5噸~35噸及巴士底盤；115年股東會年報公司沿革載車架供應國瑞汽車公司與中華汽車公司、第59頁載「車架屬寡占產品」；惟年報未載車架市占100%（唯一占有率數字為木床市場90%）。
- Proposed wording is recorded for the partial claims in `semantic/author-020.json`; no issuer report was modified. Independent review remains pending.
- 方法註記：本批次首次發現需以「市場佔有率」等變體字串檢索，先前以「市佔／市占」檢索大億年報得到零命中，改用「佔有率」後取得官方80%之數字；後續批次將以多變體檢索，避免漏檢。
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。
- Author-reviewed total: **60 / 1,399**; remaining: **1,339**. Outcome counts: ACCEPTED 17, PARTIALLY_SUPPORTED 37, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 2. Next pending claim by priority: `1533:objective_ranking_or_market_share:7a6d45cabd1f1a81` (車王電).

## Author batch `author-021` — 2026-10-05

- Reviewed the next ten unreviewed objective ranking/market-share claims in checkpoint order (車王電 1533, 和大 1536 ×3, 巧新 1563, 正新 2105, 建大 2106, 鑫永銓 2114 ×3). Evidence came from directly downloaded and inspected official disclosures: 車王電112年度年報、和大114年度年報與2026法說會簡報、德國 IHK Weltmarktführer OTTO FUCHS 條目、正新2022永續報告書與2025Q4法說會簡報、建大2022永續報告書、鑫永銓2024法說會簡報。
- `1533:objective_ranking_or_market_share:7a6d45cabd1f1a81` — `PARTIALLY_SUPPORTED`. 車王電112年度年報第184頁載設立於民國71年7月19日、主要營業項目為汽車用引擎傳動控制系統（電子點火器、電壓調整器及整流器），支持逾41年與引擎電子零組件業務；惟年報未使用「唯一」描述其地位，亦無市場結構證據支持台灣唯一。
- `1536:objective_ranking_or_market_share:0a8bd467b7db2e7b` — `ACCEPTED`. 和大2026法說會簡報第2頁標題「TAIWAN TOP 1 GEAR MAKER」，113年度年報第62頁載「更為國內汽車齒輪產業第一把交椅」，114年度年報第67頁載其為台灣第一家外銷國外OEM之（齒輪軸類）上市公司。
- `1536:objective_ranking_or_market_share:cce96a49ba94ccaf` 與 `fd8ac95e7e36addc` — `PARTIALLY_SUPPORTED`. 和大114年度年報第71頁以代號揭露第一大銷貨客戶（甲公司）占銷貨淨額113年度43.94%、114年度51.19%，高度集中之事實成立；惟全份年報無 BorgWarner 字樣（客戶一律以代號表示），且「約40%」低於官方43.94%／51.19%。油泵齒輪與扭力轉換系統零組件之產品別則獲年報支持。
- `1563:objective_ranking_or_market_share:a0f33eff27b93300` — `ACCEPTED`. 德國工商會（IHK）「世界市場領導者」名錄之 OTTO FUCHS KG 條目明載「We are the world market leader in forged wheels, chassis parts and synchronizer rings for the automotive industry」，產品欄首位為 Forged wheels，總部位於德國 Meinerzhagen。
- `2105:objective_ranking_or_market_share:daa2ec046bdc0d7f` — `PARTIALLY_SUPPORTED`. 正新2022永續報告第8頁載「正新為華人地區最大的輪胎專業製造公司，營業額持續維持台灣第一」、外銷比73%、行銷逾180國；惟永續報告與2025Q4法說會簡報均未載全球輪胎廠排名，「全球前十大」未獲確立。
- `2106:objective_ranking_or_market_share:0bd79cfdcec25a2d` — `ACCEPTED`. 建大2022永續報告第12頁載「以自有品牌KENDA 行銷全球，現已成為台灣第2大、全球第26大的輪胎廠」。
- `2114:objective_ranking_or_market_share:1bcf873b591901ce`、`83a4decf054d606c`、`7279073e1958fd1e` — `ACCEPTED` ×3. 鑫永銓2024法說會簡報第22頁載其開發製造之橡皮壩「已成功打入日本市場，目前為日本第一大進口製造廠」，並載橡皮壩屬水利應用（含小水力發電、國內多項水利工程實績）。
- Proposed wording is recorded for the partial claims in `semantic/author-021.json`; no issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。
- Author-reviewed total: **70 / 1,399**; remaining: **1,329**. Outcome counts: ACCEPTED 23, PARTIALLY_SUPPORTED 41, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 2. Next pending claim by priority: `2115:objective_ranking_or_market_share:62d5c63efe920f40` (六暉-KY).

## Author batch `author-022` — 2026-10-05

- Reviewed the next eight unreviewed objective ranking/market-share claims in checkpoint order (六暉-KY 2115 ×2, 劍麟 2228 ×3, 為升 2231 ×3). Evidence came from directly downloaded and inspected official issuer presentations: 六暉 2024年法說會簡報、劍麟 2013年上市前業績發表會簡報、為升 2024年法說會簡報。
- `2115:objective_ranking_or_market_share:62d5c63efe920f40` — `PARTIALLY_SUPPORTED`. 六暉官方簡報第23頁標語「全球產量第一 台灣氣門嘴領導品牌」，第3頁載氣嘴占產品80%、月產能7,000萬支、LUHAI成立於1980年；惟全份簡報未載全球市占率，「約10%」未獲確立。
- `2115:objective_ranking_or_market_share:ce0e7e4bf82e336c` — `PARTIALLY_SUPPORTED`. 簡報第5頁「Global Locations」列台灣彰化田中、中國廈門廈暉與崑山陸暉、印尼PT. LUHAI，支持 claim 之生產基地範圍；惟「印尼二輪內胎市佔60%」未見於簡報或任何查閱來源。
- `2228:objective_ranking_or_market_share:82e3738fa7cb1ef3`、`78fc8e4a85f351e4`、`53a88eea8833176f` — `PARTIALLY_SUPPORTED` ×3. 劍麟2013年上市前簡報第5、8、9、12頁支持其核心產品為汽車安全氣囊充氣器殼體與預縮式安全帶零件，第16頁載其配合 Autoliv 之預縮式安全帶產品；惟官方簡報未使用「隱形冠軍」定位、未出現 ZF 或均勝電子，亦未載「全球市佔逾90%」。
- `2231:objective_ranking_or_market_share:be355493562a87fb` — `PARTIALLY_SUPPORTED`. 為升2024年官方簡報第6頁載其自1979年起專注汽車感測器（含輪胎壓力監測感測器）、自2015年起進入毫米波雷達研發與生產（4D成像雷達、MRR、SRR等）；惟「台灣汽車電子龍頭」與「TPMS AM 市佔約90%」均未見於官方簡報。
- `2231:objective_ranking_or_market_share:f1eaea15e5afaa59` 與 `53dc6e668cc52c45` — `UNKNOWN_AFTER_RESEARCH` ×2. 為升官方簡報全篇未具名任何客戶，未出現 SMP（Standard Motor Products）或 Wells，亦未載北美 TPMS AM 90% 市占率；客戶身分與市占數字既不能確認亦無證據否定。
- Proposed wording is recorded for the partial claims in `semantic/author-022.json`; no issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。
- Author-reviewed total: **78 / 1,399**; remaining: **1,321**. Outcome counts: ACCEPTED 23, PARTIALLY_SUPPORTED 47, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 4. Next pending claim by priority: `2235:objective_ranking_or_market_share:2f804dd9a0a390da` (謚源).

## Author batch `author-023` — 2026-10-05

- Reviewed the next seven unreviewed objective ranking/market-share claims in checkpoint order (謚源 2235 ×2, 英利-KY 2239 ×5). Evidence came from directly downloaded and inspected official disclosures: 謚源實業申請上櫃公開說明書（民國103年）、開曼英利工業股票公開發行說明書（初次上市用）與2017年法人說明會簡報、LKQ Corporation FY2025 Form 10-K。
- `2235:objective_ranking_or_market_share:2f804dd9a0a390da` — `PARTIALLY_SUPPORTED`. 謚源公開說明書第41頁前後載其與堤維西自民國89年簽訂合作協議、產品於北美之銷售獨家委由堤維西負責、再由堤維西出貨給其美國子公司 GENERA 公司銷售予當地通路業者「包括 General Parts Inc、LKQ Corporation 及 Amazon Services」，第一大客戶堤維西占其營收78.80%／77.44%；惟全篇未出現 NAPA，claim 括號中之「(NAPA)」未獲支持。
- `2235:objective_ranking_or_market_share:f11191fc5107144b` — `ACCEPTED`. 同一公開說明書以「美國最大汽車維修通路商LKQ Corp.」描述 LKQ；LKQ 自身 FY2025 Form 10-K 亦載其北美部門營運北美最大的替代性車輛零件與配件配送網路。
- `2239:objective_ranking_or_market_share:f6f576305c25bdeb` 與 `95f5fff739fc9085` — `ACCEPTED`. 英利公開說明書第131、136頁載其對一汽大眾之銷售占比達80.24%／81.16%／78.73%／73.16% 並明載「最大客戶一汽大眾」；第120、124頁列北京奔馳與上海（上汽）大眾；第67頁載「一汽大眾AUDI所有系列的儀錶板骨架皆為本集團生產」。
- `2239:objective_ranking_or_market_share:1f382b871069e7dc`、`8d3dc1316d4155c8`、`f1b8e1134f6bc9d1` — `PARTIALLY_SUPPORTED`. 公開說明書第17頁前後載其與 Quadrant Composites AG 簽訂專利授權契約而可生產 SymaLITE、為「首家SYMALITE輕質材料車底護板及全鋁合金儀錶板骨架產品國產化廠」，2017年法說會簡報亦載自歐洲引進完整產線；惟兩份官方文件均未載「亞洲唯一產線」或「全球僅5條」，且未將 Audi 與底盤護板連結（官方之 Audi 關聯為儀錶板骨架）。
- Proposed wording is recorded for the partial claims in `semantic/author-023.json`; no issuer report was modified. Independent review remains pending.
- 來源性質註記：謚源民國103年上櫃申請之公開說明書（全文以「本公司」自述）由承銷體系之凱基證券網域取得，內容屬發行人正式申報文件，故採為來源；其內含對堤維西營運與訴訟之詳細評估，已按事實摘記。本批次未新增來源取得失敗，`local-recheck-queue.json` 維持 **15** 筆。
- Author-reviewed total: **85 / 1,399**; remaining: **1,314**. Outcome counts: ACCEPTED 26, PARTIALLY_SUPPORTED 51, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 4. Next pending claim by priority: `2245:objective_ranking_or_market_share:7ade1b140810fe09` (詠勝昌).

## Author batch `author-024` — 2026-10-05

- Reviewed the next nine unreviewed objective ranking/market-share claims in checkpoint order (詠勝昌 2245 ×3, 湧盛 2249, 歐特明 2256 ×3, 精確 3162 ×2). Evidence came from directly downloaded and inspected official disclosures: 詠勝昌115年第2季合併財務報告、湧盛2020年業績發表會簡報、歐特明114年度年報、精確公司簡介及2025營運展望。
- `2245:objective_ranking_or_market_share:7ade1b140810fe09`、`03b9308fa26ebeb9`、`9d1fc3aba637d71d` — `UNKNOWN_AFTER_RESEARCH` ×3. 詠勝昌115年第2季合併財務報告（38頁）僅載信用風險管理政策（「對主要客戶予以評等」），未具名任何客戶；Standard Motor、Federal-Mogul、BERU、Tenneco、BorgWarner 出現次數均為0。發行人官網 nwwmfg.com 之 TLS 連線失敗，未取得年報或公開說明書。三家客戶關係與 SMP 之最大經銷商身分均未獲確立。
- `2249:objective_ranking_or_market_share:f3cb005c6c4a4f6c` — `PARTIALLY_SUPPORTED`. 湧盛2020年官方簡報第5頁載主要產品為汽車空調壓縮機與熱交換器，第6頁載2012年起生產製造汽車空調壓縮機、2013年取得日本 SINLIN AUTOMOTIVE 95%股權，第31頁載2019年營收21.3億元；惟簡報未載「台灣最大」或「出口量逾95%」（其自身區域銷售為美洲56%、歐洲31%、亞洲12%）。2026年9月法說會簡報下載成功但為掃描影像，無法擷取文字。
- `2256:objective_ranking_or_market_share:922429090abb9e1a`、`904acb0030df90b3`、`8d2c0b8f1fbe9b0c` — `PARTIALLY_SUPPORTED` ×3. 歐特明114年度年報第5頁載「本公司自104年承接納智捷及小鵬汽車量產案後，即投入全車360度視覺AI感知技術」，支持小鵬汽車為客戶；惟第70頁銷貨客戶揭露以代號表示（「A 客戶」114年度占10.50%），未具名小鵬為最大客戶，亦未載「歷史營收占比逾80%」或「目標降至50%」。
- `3162:objective_ranking_or_market_share:41c8c84e28a3f1c3` 與 `ef970bc4a035c623` — `PARTIALLY_SUPPORTED`. 精確2025年官方簡報第22頁列主要客戶「蜂巢能源(吉利)」、第24及26頁列「億緯鋰能」；惟第7頁將「寧德時代」列於「客戶認證中」，顯示其並非現有客戶，故「寧德時代（最大）」不成立。
- Proposed wording is recorded for the partial claims in `semantic/author-024.json`; no issuer report was modified. Independent review remains pending.
- 來源檢索限制：詠勝昌官網 TLS 憑證失敗、湧盛2026法說會簡報為掃描影像；二者均為檢索限制之紀錄，未用以推論 claim 真偽，亦未達 `local-recheck-queue.json` 之門檻。佇列維持 **15** 筆。
- Author-reviewed total: **94 / 1,399**; remaining: **1,305**. Outcome counts: ACCEPTED 26, PARTIALLY_SUPPORTED 57, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 7. Next pending claim by priority: `3552:objective_ranking_or_market_share:e17dab0717bd3ebb` (同致).

## Author batch `author-025` — 2026-10-06

- Reviewed the next seven unreviewed objective ranking/market-share claims in checkpoint order (同致 3552 ×2, 江興鍛 4528 ×3, 至興 4535, 永新-KY 4557). Evidence came from directly downloaded and inspected official disclosures: 同致2025年法說會簡報、江興鍛壓111年度年報、至興精機2016/2017公司簡介、永新控股2025年法說會簡報。
- `3552:objective_ranking_or_market_share:e17dab0717bd3ebb` — `PARTIALLY_SUPPORTED`. 同致2025年官方簡報第5頁載其為 tier-one supplier 並直接供應汽車品牌商，第9頁產品別營收中 Autonomous Parking Sensing 66%＋Autonomous Parking Controls 22%（合計88%），支持停車感測為其核心業務；惟簡報未載「亞洲最大、全球第三大」、未出現 Bosch 或 Valeo、未載48家OEM或50國。
- `3552:objective_ranking_or_market_share:1a523bd0dd0f352b` — `UNKNOWN_AFTER_RESEARCH`. 同致官方簡報全篇未出現 Bosch，亦未提供停車感測器市場之任何排名或市占資料，無法確立「Bosch — 全球第一」於該特定市場之地位。
- `4528:objective_ranking_or_market_share:d7d5512cdbb52739`、`c57c2e43e2aaf637`、`efa3b52c128a97ee` — `PARTIALLY_SUPPORTED` ×3. 江興鍛111年度年報第12頁公司沿革載其2500TON熱鍛生產線「順利生產廣州NTN鍛件」，支持 NTN 為其客戶；惟第142頁重要客戶資訊以代號揭露（111年度甲公司25%、乙公司13%、丙公司12%），最大客戶未具名；Dana、AAM、和大、中華台亞於全份年報出現次數均為0。
- `4535:objective_ranking_or_market_share:bb205423e2687dc7` — `PARTIALLY_SUPPORTED`. 至興2016年官方簡介第30頁明載「至興精機為國內精密沖壓製造業第一大廠」、機車碟煞盤國內市佔率70%，支持「台灣最大精密沖壓零組件製造商」；惟「隸屬全興集團（東陽集團）」未獲支持——簡報中「全興」四處皆為地址之「全興工業區」，「東陽」出現次數為0。
- `4557:objective_ranking_or_market_share:c1b4ac853233bb38` — `ACCEPTED`. 永新2025年官方簡報第3頁明載「The largest aftermarket supplier of brake assemblies in North America」，第18頁產品別營收列 Brake master cylinder 24.93%、Brake wheel cylinder 17.05%，第29頁載其正強化煞車卡鉗產能、推廣 EPB 卡鉗與 brake pads（iBooster、來令片），對應 claim 之拓展方向。
- Proposed wording is recorded for the partial claims in `semantic/author-025.json`; no issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。
- Author-reviewed total: **101 / 1,399**; remaining: **1,298**. Outcome counts: ACCEPTED 27, PARTIALLY_SUPPORTED 62, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 8. Next pending claim by priority: `4581:objective_ranking_or_market_share:73abdc91543dcce2` (光隆精密-KY).

## Author batch `author-026` — 2026-10-06

- Reviewed the next eight unreviewed objective ranking/market-share claims in checkpoint order (光隆精密-KY 4581 ×2, 臺企銀 2834 ×2, 彰銀 2801, 高雄銀 2836, 遠東銀 2845 ×2). Evidence came from directly downloaded and inspected official disclosures: 光隆精密2021年法說會簡報、臺企銀2025年報與110年度永續報告書（及立法院泛公股公聽會報告）、彰化銀行2024年報、高雄銀行2021年ESG報告、遠東銀行2021年永續報告書。
- `4581:objective_ranking_or_market_share:73abdc91543dcce2` 與 `51c1f3dd91ff6f70` — `PARTIALLY_SUPPORTED`. 光隆官方簡報第6頁載福州精工承接 Cummins 引擎零件、第21及22頁載為 PACCAR 英國卡車廠提供 VA/VE 與快速樣件，支持 Cummins、PACCAR 為客戶；惟簡報未載最大客戶、未使用「北美柴油引擎龍頭」，Daimler、Volvo、Traton 出現次數均為0，亦無30%／20%／10%之卡車 OEM 市占數字。
- `2834:objective_ranking_or_market_share:3e15299e9e29f33f` — `PARTIALLY_SUPPORTED`. 臺企銀2025年報第30頁公司沿革載前身為1915年設立之「臺灣無盡株式會社」及「大正無盡株式會社」；110年度永續報告第4、29、72頁三度載其為「全國唯一之中小企業專業銀行」。惟「八大行庫之一」未獲查閱來源逐一列名（立法院泛公股公聽會報告僅概括提及「八大行庫」）。
- `2834:objective_ranking_or_market_share:f95bff030d5de303` — `PARTIALLY_SUPPORTED`. 臺企銀2025年報第62及65頁主要股東名單（2026年2月28日）依序為臺灣銀行16.21%、行政院國家發展基金管理會5.87%、臺灣土地銀行2.29%、財政部2.08%，並註明「財政部持有其母公司臺灣金控股權（100%）」。故財政部為最終控制者，但直接最大股東為臺灣銀行。
- `2801:objective_ranking_or_market_share:3c8dac88a1c7f530` — `ACCEPTED`. 彰銀2024年報第80頁主要股東名單第1名為財政部（1,366,316,484股、12.19%）；第87頁載國內營業單位185家、海外據點7家分行、1家出張所及1家辦事處，涵蓋紐約、洛杉磯、東京、倫敦、香港、新加坡、馬尼拉等主要金融中心。
- `2836:objective_ranking_or_market_share:8aa22fea75ecafb5` — `PARTIALLY_SUPPORTED`. 高雄銀2021年ESG報告第3頁載「本行係於1982年由高雄市政府出資成立之地方政府政策型公營銀行」，第5頁載設立日期1982年1月13日、由高雄市政府出資99.994%，第12頁載「本行之主要控制股東為高雄市政府，持有本行股份43.13%」；惟報告未使用「全台唯一由地方政府主導」之表述。
- `2845:objective_ranking_or_market_share:70d1f48d13bb0d55` 與 `f2164388106df7ee` — `UNKNOWN_AFTER_RESEARCH`. 遠東銀2021年永續報告書（124頁）中 VASP、虛擬資產、虛擬通貨 出現次數均為0，「信託」僅出現於員工持股信託；公開資訊觀測站113年度年報端點回應 HTTP 200 但內容僅320 bytes，未能檢視。VASP 信託金流業務與九成市占均未獲確立。
- Proposed wording is recorded for the partial claims in `semantic/author-026.json`; no issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。
- Author-reviewed total: **109 / 1,399**; remaining: **1,290**. Outcome counts: ACCEPTED 28, PARTIALLY_SUPPORTED 67, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 10. Next pending claim by priority: `2880:objective_ranking_or_market_share:bea17a5f1d280fb1` (華南金).

## Author batch `author-027` — 2026-10-06

- Reviewed the next eight unreviewed objective ranking/market-share claims in checkpoint order (華南金 2880 ×2, 兆豐金 2886 ×2, 永豐金 2890 ×3, 第一金 2892). Evidence came from directly downloaded and inspected official disclosures: 華南金控2022永續報告書、中央銀行新聞稿、兆豐金控112年年報、永豐金控公司簡介、第一金控現金增資公開說明書。
- `2880:objective_ranking_or_market_share:bea17a5f1d280fb1` — `ACCEPTED`. 華南金2022年永續報告第22頁明載「華南金融控股股份有限公司…為臺灣第一家成立之金融控股公司。於2001年12月19日，由華南商業銀行及永昌綜合證券以股權轉換方式設立」。
- `2880:objective_ranking_or_market_share:a7669e207f28c0b5` — `ACCEPTED`. 同報告第24頁「股東結構」載「本公司最大股東為臺灣銀行（持股占比21.23%）」，而臺灣銀行為財政部100%持有之公營銀行，故「財政部透過臺灣銀行間接為最大股東」於華南金確實成立。
- `2886:objective_ranking_or_market_share:a7669e207f28c0b5` — `PARTIALLY_SUPPORTED`. 兆豐金112年年報第73頁主要股東名單第1名為財政部（8.20%），臺灣銀行列第5名（2.62%）；財政部為直接第一大股東，「透過臺灣銀行間接」之機制描述與官方揭露不符。
- `2886:objective_ranking_or_market_share:6bbc731aba29c26b` — `PARTIALLY_SUPPORTED`. 中央銀行官方新聞稿標題為「兆豐銀行續任『外幣結算平台』美元清算銀行」，支持其為央行外幣結算平台之美元清算銀行；兆豐金112年年報企業金融業務敘述亦以「維持聯貸市場優勢地位，持續發展國際化商機」為策略，支持大型企業跨國聯貸之優勢地位。惟「台灣唯一」一詞未獲確認——該新聞稿頁面主體為網站導覽文字，未擷取到內文。
- `2890:objective_ranking_or_market_share:2ec04a9365b56c0f` — `ACCEPTED`. 永豐金控官方公司簡介第4頁載「2022年3月底太陽能設備融資市占維持第一(25.5%)」，與 claim 之「全台第一（近三成）」相符。
- `2890:objective_ranking_or_market_share:298eb00d61c6591a` 與 `92485629cda4cfea` — `UNKNOWN_AFTER_RESEARCH`. 該簡報中「上櫃」出現次數為0、未載營業據點數；Amret 與柬埔寨出現次數亦為0（該收購事件發生於2025年，晚於本簡報）；本批次未取得其他可檢視之發行人官方來源以確認。
- `2892:objective_ranking_or_market_share:a7669e207f28c0b5` — `PARTIALLY_SUPPORTED`. 第一金現金增資公開說明書第57頁主要股東名單列財政部13.35%為第1名、臺灣銀行7.72%為第2名，第36頁載主要大股東（財政部及臺灣銀行）合計21.07%；故財政部為直接第一大股東，「透過臺灣銀行間接」不符（並註記該股東結構基準日為民國104年，屬歷史資料）。
- 本批次另附方法修正：撰寫 2886 聯貸敘述之 rationale 時，初稿誤稱年報未載聯貸優勢，經複查年報企業金融敘述後已即時更正為「支持聯貸市場優勢地位」，並保留「唯一」未確認之缺口。
- Proposed wording is recorded for the partial claims in `semantic/author-027.json`; no issuer report was modified. Independent review remains pending.
- 來源檢索限制：華南金官網 hnfhc.com.tw 三個 PDF 連結（含年報與永續報告）均連線逾時，改由公開資訊觀測站端點取得其111年度報告文件；此為檢索限制之紀錄，未用以推論 claim 真偽。佇列維持 **15** 筆。
- Author-reviewed total: **117 / 1,399**; remaining: **1,282**. Outcome counts: ACCEPTED 31, PARTIALLY_SUPPORTED 70, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 12. Next pending claim by priority: `2892:objective_ranking_or_market_share:ed08854a9f3fb74e` (第一金).















