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

Author-reviewed: **423 / 1,399** unique HIGH claims across batches `author-001` (8), `author-002` (1), `author-003` (1), `author-004` (2), `author-005` (1), `author-006` (1), `author-007` (1), `author-008` (1), `author-009` (1), `author-010` (1), `author-011` (2), `author-012` (1), `author-013` (3), `author-014` (2), `author-015` (2), `author-016` (3), `author-017` (6), `author-018` (7), `author-019` (8), `author-020` (8), `author-021` (10), `author-022` (8), `author-023` (7), `author-024` (9), `author-025` (7), `author-026` (8), `author-027` (8), `author-028` (8), `author-029` (8), `author-030` (8), `author-031` (7), `author-032` (8), `author-033` (8), `author-034` (8), `author-035` (8), `author-036` (9), `author-037` (7), `author-038` (8), `author-039` (6), `author-040` (8), `author-041` (8), `author-042` (7), `author-043` (8), `author-044` (4), `author-045` (4), `author-046` (5), `author-047` (5), `author-048` (6), `author-049` (4), `author-050` (8), `author-051` (4), `author-052` (8), `author-053` (4), `author-054` (8), `author-055` (4), `author-056` (7), `author-057` (5), `author-058` (7), `author-059` (7), `author-060` (7), `author-061` (3), `author-062` (5), `author-063` (6), `author-064` (6), `author-065` (6), `author-066` (7), `author-067` (7), `author-068` (6), `author-069` (4), `author-070` (6), `author-071` (6), `author-072` (5), `author-073` (6), `author-074` (5), and `author-075` (7).

- ACCEPTED by author: 66
- PARTIALLY_SUPPORTED: 275
- UNSUPPORTED: 1
- SOURCE_UNAVAILABLE: 3
- Other allowed author decisions: 78
- Remaining author queue: 976

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

## Author batch `author-028` — 2026-10-06

- Reviewed the next eight unreviewed objective ranking/market-share claims in checkpoint order (第一金 2892 ×7, 王道銀行 2897). Evidence came from directly downloaded and inspected official disclosures: 第一金控現金增資公開說明書（104年）與106年度企業社會責任報告書、王道銀行B型企業認證文件與2025永續報告書。
- `2892:objective_ranking_or_market_share:ed08854a9f3fb74e` — `PARTIALLY_SUPPORTED`. 公開說明書第3及11頁明載「設立日期：92年1月2日」（2003年）與上市日期，支持成立年度；惟「為台灣歷史最悠久的泛公股金控之一」之排名性敘述未獲查閱來源比較。
- `2892:objective_ranking_or_market_share:76b816df512daafe` — `PARTIALLY_SUPPORTED`. 公開說明書列第一銀行為主要子公司、占金控收益93.98%；惟「1899」於公開說明書與CSR報告中出現次數均為0，CSR報告第25頁載全臺188個營運據點、第3頁載33處海外營運點，與 claim 之182家分行／31家海外分支機構不符。
- `2892:objective_ranking_or_market_share:ca7ce41d34befae1` — `PARTIALLY_SUPPORTED`. 公開說明書第6頁子公司摘要表列第一金證券、第一金證券投資信託、第一金人壽保險；惟明台產物保險不在該表內，第33頁註2僅載其於民國92年7月31日曾為股份轉換對象，即設立初期曾納入而後已不在子公司之列。
- `2892:objective_ranking_or_market_share:88dd8b6be75d5904` — `PARTIALLY_SUPPORTED`. 第一銀行「中小企業放款」獲CSR報告支持（市占連續第八年居國銀首位）；「房貸」「進出口」出現次數為0，「財富管理」僅見於董事個人經歷。
- `2892:objective_ranking_or_market_share:e8187bb231e1e142`、`3f5488a25cf9016f`、`2f5c3c2bb8f9797b` — `ACCEPTED`. 公開說明書子公司摘要表分別列第一金證券（經紀）、第一金證券投資信託（投信／基金管理）、第一金人壽保險（壽險），三者之子公司身分與業務類別均獲支持。
- `2897:objective_ranking_or_market_share:de51a64a7f203960` — `PARTIALLY_SUPPORTED`. 王道銀行官方B型企業認證文件第13及19頁載其2017年1月改制為王道商業銀行、成為「全台第一家原生數位銀行」，2025永續報告第36及134頁亦同；官方文件載其2017年取得B型企業認證並於2021、2025年重新認證。惟「全台首家獲得B型企業認證的上市銀行」中之「首家」未獲支持——永續報告第39頁載其為「當時臺灣第21家B型企業」。
- Proposed wording is recorded for the partial claims in `semantic/author-028.json`; no issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。
- Author-reviewed total: **125 / 1,399**; remaining: **1,274**. Outcome counts: ACCEPTED 34, PARTIALLY_SUPPORTED 75, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 12. Next pending claim by priority: `5880:objective_ranking_or_market_share:a7669e207f28c0b5` (合庫金).

## Author batch `author-029` — 2026-10-06

- Reviewed the next eight unreviewed objective ranking/market-share claims in checkpoint order (合庫金 5880 ×2, 台泥 1101 ×2, 環泥 1104, 信大 1109 ×2, 台玻 1802). Evidence came from directly downloaded and inspected official disclosures: 台泥官方簡報（刊於臺灣證券交易所公司治理中心）與2024企業ESG年鑑、環球水泥2025下半年度法說會簡報、信大水泥法人說明會簡報、台玻2019企業社會責任報告書、合庫金官方網站。
- `5880:objective_ranking_or_market_share:a7669e207f28c0b5` 與 `0f3b5a58ad55e774` — `UNKNOWN_AFTER_RESEARCH`. 合庫金官網首頁與投資人路徑回應 HTTP 200 但內容為前端框架、未含可下載之年報或股東結構文件；立法院泛公股金融機構公聽會報告（115年8月）全文檢索未含「廣義公股」「財政部直接持股」等表格文字。故主要股東名單與中小企業放款市占均未獲確立。
- `1101:objective_ranking_or_market_share:70c0cf57f148a361` — `ACCEPTED`. 台泥官方簡報第3頁時間軸載「1946 • 日本浅野水泥株式会社(前身) • 國營台灣水泥成立」、「1954 • 台灣水泥民營化」、「• 第一家股票上市公司(1962年)」，且該頁標題為「從水泥產業到綠色環境工程公司」，三項敘述均獲支持。
- `1101:objective_ranking_or_market_share:1d1eb04d19b03299` — `PARTIALLY_SUPPORTED`. 簡報第3頁載2018年「全球化佈局歐亞非」，2024企業ESG年鑑第485頁載台泥2024年完成歐洲低碳水泥交割、成為「跨五大洲13市場」之集團；年鑑第498頁明載其與「土耳其最大水泥公司 OYAK 成立子公司」。惟「台泥國際」出現次數為0，該子公司名稱未獲確認。
- `1104:objective_ranking_or_market_share:9a15f087597b0139` — `PARTIALLY_SUPPORTED`. 環泥2025年法說會第6頁產品別營收列混凝土67%、水泥20%、石膏板13%，支持主要產品；惟全份簡報未載石膏板市占率或「全台第一約90%」，亦未使用「深耕南台灣」表述（第8頁混凝土地區占比為台南34%、高雄40%、屏東8%）。
- `1109:objective_ranking_or_market_share:7c6d8b2d2057eb58` 與 `5fd4ab936a526e30` — `PARTIALLY_SUPPORTED`. 信大簡報第6至9頁載大陸子公司江蘇信寧新型建材（南京市浦口區）、以南京市江北江南等為主要目標市場、並為江蘇省A級水泥企業；惟第9頁官方市占為「占南京市區域市場約17%左右」，與 claim 之15%不同。
- `1802:objective_ranking_or_market_share:75e14cf20248f928` — `PARTIALLY_SUPPORTED`. 台玻2019年CSR報告第13頁載「1964年8月25日」、「台玻成立於1964年」，並列平板玻璃、玻璃纖維、玻璃器皿等主要產品與多家生產子公司；惟「國內最大」「台灣最大」「龍頭」「名列前茅」於全份報告出現次數均為0。
- Proposed wording is recorded for the partial claims in `semantic/author-029.json`; no issuer report was modified. Independent review remains pending.
- 方法備註：台泥之公司沿革與上市地位於其自身ESG年鑑章節中未載明，改由刊載於臺灣證券交易所公司治理中心之發行人簡報取得，屬發行人自製文件，來源等級與 MOPS 簡報相同。
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。
- Author-reviewed total: **133 / 1,399**; remaining: **1,266**. Outcome counts: ACCEPTED 35, PARTIALLY_SUPPORTED 80, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 14. Next pending claim by priority: `2504:objective_ranking_or_market_share:271a4f0e71b4103a` (國產).

## Author batch `author-030` — 2026-10-06

- Reviewed the next eight unreviewed objective ranking/market-share claims in checkpoint order (國產 2504, 永固-KY 5546, 惠普 8424, 中聯資源 9930, 橋椿 2062 ×2, 青鋼 8930 ×2). Evidence came from directly downloaded and inspected official disclosures: 國產建材法人說明會簡報、永固集團介紹、惠普法人說明會簡報、中聯資源法人說明會簡報、橋椿公司簡報與110年度年報、青鋼法人說明會簡報與官網公司簡介。
- `2504:objective_ranking_or_market_share:271a4f0e71b4103a` — `ACCEPTED`. 國產2026年法說會第2頁公司簡介明載「為臺灣預拌混凝土之龍頭企業」、「全台共有26個預拌廠」，支持其為台灣預拌混凝土龍頭；官方未另載市占百分比，claim 之後段與「龍頭」為同義之市場地位敘述。
- `5546:objective_ranking_or_market_share:9e5e5a07bc534c70` — `PARTIALLY_SUPPORTED`. 永固集團介紹第5頁載主要商品為預拌商品混凝土、第6頁載重慶五個攪拌站、第13及17頁載重慶軌道交通線網覆蓋主城九區且在建輕軌4/5/9/10號線「均指定由我司供應混凝土」；惟全份文件未載市占率數字或市場排名，亦未以「領先」描述其市占。
- `8424:objective_ranking_or_market_share:ac341368dc8f4238` — `PARTIALLY_SUPPORTED`. 惠普2025年法說會第4頁載主要產品為矽酸鈣板（64%）與纖維水泥板（36%），第5頁載國產建材實業持股50.6%；惟全份簡報未載「台灣最大矽酸鈣板製造商」或任何市占率。
- `9930:objective_ranking_or_market_share:edbe1906dd3dcf78` — `ACCEPTED`. 中聯資源2026年法說會第4頁明載「國內規模最大爐石粉產銷業者，供應下游預拌混凝土、營造與公共工程…實踐循環經濟」，另一份簡報第4頁亦載「高爐水泥事業：國內規模最大爐石粉產銷業者」；第24頁載其獲環境部「資源循環績優企業遴選-銀質獎」。
- `2062:objective_ranking_or_market_share:a71bb7b3c16dfa04` — `PARTIALLY_SUPPORTED`. 橋椿公司簡報第4及5頁載其為「全球廚房衛浴產業中，裝飾設備鋅壓鑄零組件領導製造商」，第11頁載「鋅的原料成本是銅的1/3」；惟簡報所述六成以上市占係指「客戶」在北美與歐洲水龍頭市場之市占，並非橋椿在零組件市場之占有率，故「極高市佔率」未獲支持。
- `2062:objective_ranking_or_market_share:95163601c6041a89` — `PARTIALLY_SUPPORTED`. 簡報第4頁載「這些客戶在北美與歐洲市場的市占率達六成以上」、第9頁重述「我們的客戶在北美及歐洲水龍頭市占率超過六成」，支持市占比例之核心事實；惟 Kohler、科勒、Moen、摩恩、American Standard、美標、TOTO 於該簡報與110年度年報之出現次數均為0，四大客戶之具名未獲支持。
- `8930:objective_ranking_or_market_share:b7304d14590e5873` — `PARTIALLY_SUPPORTED`. 青鋼2025年12月法說會第17頁企業沿革載「成立於1982年」、「40年」，並標示「第一家自動化生產」與「第一家上市櫃金屬建材」；發行人官網公司簡介中「台南」出現5次，與總部所在地相符。惟官方用語為「第一家上市櫃金屬建材」（最早掛牌），與 claim 之「唯一掛牌上市」屬不同強度之限定。
- `8930:objective_ranking_or_market_share:0e49eeeb7dba1af5` — `UNKNOWN_AFTER_RESEARCH`. 「主力產品市佔率長年達20%~40%」未獲確立：查閱之簡報與官網簡介中「市佔」「市占」出現次數均為0；簡報中之20、40等數字均屬財務報表科目或沿革年數，與市占率無關。
- Proposed wording is recorded for the partial claims in `semantic/author-030.json`; no issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。
- Author-reviewed total: **141 / 1,399**; remaining: **1,258**. Outcome counts: ACCEPTED 37, PARTIALLY_SUPPORTED 85, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 15. Next pending claim by priority: `9924:objective_ranking_or_market_share:d29232b4aad5a82a` (福興).

## Author batch `author-031` — 2026-10-06

- Reviewed the next seven unreviewed objective ranking/market-share claims in checkpoint order (福興 9924 ×2, 三商電 2427 ×3, 互盛 2433, 上福 6128). Evidence came from directly downloaded and inspected official disclosures: 福興114年度年報、三商電公司簡介與2017年法人說明會簡報、互盛2016年法人說明會簡報、上福全球科技2018企業社會責任報告書。
- `9924:objective_ranking_or_market_share:d29232b4aad5a82a` — `PARTIALLY_SUPPORTED`. 福興114年度年報支持總部位於高雄（高雄市岡山區本洲里育才路88號）與其高級門鎖／防火門鎖／智慧門鎖產品線；惟「1957」「全球最大」「領導廠商」於全份年報之出現次數均為0。
- `9924:objective_ranking_or_market_share:e6f8af7f9168315b` — `PARTIALLY_SUPPORTED`. 年報第76頁載「內銷、外銷金額各約佔總營業額7%、93%；外銷部分以北美市場佔75%為最大宗」，支持其北美與全球銷售；惟「約佔美國終端市佔20%」未獲任何官方數字支持。
- `2427:objective_ranking_or_market_share:1e603cc94ccc2dc1` — `PARTIALLY_SUPPORTED`. 三商電公司簡介第27頁載「存提款機市佔第一」與「循環功能的自動櫃員機，在台的市占率更超過七成，穩居市場第一」；惟「超過五成」之整體 ATM 市占未載，且 NCR 與 Diebold 於文件中出現次數均為0（官方載明代理品牌為飛利浦、IBM、西門子、Omron、Hitachi）。
- `2427:objective_ranking_or_market_share:626114d027f188f8` 與 `1d56a8bd2f1d7f51` — `PARTIALLY_SUPPORTED`. 客戶涵蓋銀行、郵局等獲簡介支持；惟「ATM 市佔過半」之整體數字未載，2017年法說會簡報以「銀行A、銀行B、銀行C」代號示意客戶，且「外幣兌換機」「智慧繳費機」未見於官方文件。
- `2433:objective_ranking_or_market_share:326ac8fb4b455e88` — `PARTIALLY_SUPPORTED`. 互盛2016年法說會第6頁沿革載「Acquired agency right for RICOH printers」，支持 Ricoh 代理關係；惟全份簡報未使用「最大」「長期」「獨家」「唯一」描述該關係，產品線亦不含視訊設備。
- `6128:objective_ranking_or_market_share:f350aa9fa22fba0f` — `ACCEPTED`. 上福全球科技2018年CSR報告第6頁明載「國內唯一具備碳粉匣及OPC (Organic Photo-Conductor)感光鼓精密齒輪研發設計能力的廠商」，並載其為事務機器空碳粉匣、配件及感光鼓精密齒輪之領導廠商之一；第30至32頁載其自行研發生產該等零件（含德國 ARBURG 射出成形機17台）。
- Proposed wording is recorded for the partial claims in `semantic/author-031.json`; no issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。
- Author-reviewed total: **148 / 1,399**; remaining: **1,251**. Outcome counts: ACCEPTED 38, PARTIALLY_SUPPORTED 91, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 15. Next pending claim by priority: `6593:objective_ranking_or_market_share:bcd8051088ba12eb` (台灣銘板).

## Author batch `author-032` — 2026-10-06

- Reviewed the next eight unreviewed objective ranking/market-share claims in checkpoint order (台灣銘板 6593 ×3, 阜爾運通 6914, 益張 8342 ×2, 華票 2820 ×2). Evidence came from directly downloaded and inspected official disclosures: 台灣銘板2025與2017年官方簡報、阜爾運通2026年法人說明會簡報、益張實業2025年法人說明會簡報與107年度年報、中華票券109年度年報。
- `6593:objective_ranking_or_market_share:bcd8051088ba12eb` 與其兩個條目 `b3ba33d575c72e62`、`2b4e80914df0aac2` — `PARTIALLY_SUPPORTED`. 台灣銘板2025年簡報第2頁載其開發 RFID 無線射頻識別技術與二代悠遊晶片、提供 IC 晶片錄寫等個人化服務，第10頁載「掌握銀行及票證公司年度合約770萬張」；2017年簡報第7頁載「★Mastercard 正式認可」、第17頁載其為「全球唯二之二代悠遊晶片合格供應商」。惟「台灣前四大發卡銀行」「市佔率高達35%」「獲美國專利」及 Visa 認證均未獲查閱文件支持。
- `6914:objective_ranking_or_market_share:e0e3a03b5e669446` — `ACCEPTED`. 阜爾運通2026年官方簡報第18頁載「城市車旅普客二四」，並明載「就目前主要停車管理公司案場分析，城市車旅目前已居於業界領導位置」，與 claim 之市占最高／領導地位敘述一致。
- `8342:objective_ranking_or_market_share:acce089189cec438` 與 `a2f0330b12f64684` — `UNKNOWN_AFTER_RESEARCH`. 益張2025年官方簡報中「北美」「市佔」「市占」「最大」出現次數均為0，僅載金屬展示架與商店／超市展示設備；107年度年報中「北美」僅出現1次且係描述全球金屬製品市場之集中區域，「市佔」「領導」為0。「北美最大商業耗材設備商」既無官方亦無第三方權威來源可確認或否證。
- `2820:objective_ranking_or_market_share:4ea2d7d9b3fa5942` — `PARTIALLY_SUPPORTED`. 華票109年度年報第7頁載行政院開發基金出售持股後台灣工業銀行（後改制為王道商業銀行）成為最大股東，並載「截至110年3月底王道商業銀行（持股28.36%）仍為華票最（大股東）」；惟「第二大股東為寶佳集團（持股約17%）」未獲支持——年報中「寶佳」僅出現2次且均為董事會成員經歷，未載其持股比例。
- `2820:objective_ranking_or_market_share:7eeb0fcbdc78b0fb` — `ACCEPTED`. 同頁年報內容直接支持「王道銀行（持股約28%）— 最大股東」。
- Proposed wording is recorded for the partial claims in `semantic/author-032.json`; no issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。
- Author-reviewed total: **156 / 1,399**; remaining: **1,243**. Outcome counts: ACCEPTED 40, PARTIALLY_SUPPORTED 95, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 17. Next pending claim by priority: `2855:objective_ranking_or_market_share:23dcc1ae4b2739ba` (統一證).

## Author batch `author-033` — 2026-10-06

- Reviewed the next eight unreviewed objective ranking/market-share claims in checkpoint order (統一證 2855, 國票金 2889, 群益證 6005 ×2, 元大期 6023, 福邦證 6026, 聯成 1313 ×2). Evidence came from directly downloaded and inspected official disclosures: 統一證111年度年報文件、國票金2021永續報告書、群益證2026年法人說明會簡報、元大期114年股東常會議事手冊、福邦證113年度年報、聯成2020與2025年法人說明會簡報。
- `2855:objective_ranking_or_market_share:23dcc1ae4b2739ba` — `PARTIALLY_SUPPORTED`. 統一證111年報第324及87頁均明載「本公司111年證券經紀市佔率為2.82%，市佔排名為國內本土券商中第11名」，與 claim 之「穩定位居本土券商前十」不符；官方另載「單點平均市佔率為0.09%，在前十大本土券商第5名」，該第5名係單點平均市占之排名。第101頁載電子下單比率108年為79.37%，支持「電子下單比率高」。
- `2889:objective_ranking_or_market_share:9f8aba6960121ca6` — `PARTIALLY_SUPPORTED`. 國票金永續報告第15及17頁載「2002年3月26日」及由國際票券、協和證券、大東綜合證券設立；惟「為台灣唯一以票券業務為核心的金控」之「唯一」未見於官方文件。
- `6005:objective_ranking_or_market_share:083b365bd1c581fa` 與 `5130bfc55573a836` — `PARTIALLY_SUPPORTED`. 群益證2026年簡報第16頁載2025年經紀業務市佔率3.71%、市場排名9，第22頁載2026年1～2月3.53%、排名8，與「約4%」大致相符；惟「排名本土券商第六」與官方第8～9名不符，且簡報未載營業據點總數或客戶結構。
- `6023:objective_ranking_or_market_share:cec62e122390ab9a` — `PARTIALLY_SUPPORTED`. 元大期114年股東常會議事手冊第9頁載113年稅後淨利21.67億元「位居14家專營期貨商之首」、期貨經紀市占率22.62%、選擇權18.14%、客戶保證金占全市場32.89%且「市場存量第一」；惟全份報告未載其資本額或淨值為同業第一，亦未載長期年度市占序列。
- `6026:objective_ranking_or_market_share:f276a5441599570d` — `PARTIALLY_SUPPORTED`. 福邦證113年報第85及89頁載其「以投資銀行業務為核心」、聚焦中型及中小企業客戶、並自述「無金控與銀行合作，缺乏交叉行銷的綜效」；惟所引述之定位語「中小型企業的全方位策略夥伴」未出現於年報。
- `1313:objective_ranking_or_market_share:f7e881e9038a20ac` — `PARTIALLY_SUPPORTED`. 聯成2025年簡報第5及7頁載「聯成為全球最大苯酐及可塑劑製造商」；惟「在大中華區市佔率達30%」出自2020年簡報第3頁（大中華地區30%），2025年簡報第17頁之最新官方數字為「2025年中國大陸可塑劑需求量估約519萬噸，聯成市占約23%」，故當前時點之30%不成立。
- `1313:objective_ranking_or_market_share:440a3c16130704da` — `PARTIALLY_SUPPORTED`. 全球最大產能與其物流儲運業務獲部分佐證；惟「龍頭」於兩份簡報出現次數為0，「一站式垂直海運物流競爭壁壘」與「隸屬於聯華神通集團」之陳述未獲官方文件支持。
- Proposed wording is recorded for the partial claims in `semantic/author-033.json`; no issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。
- Author-reviewed total: **164 / 1,399**; remaining: **1,235**. Outcome counts: ACCEPTED 40, PARTIALLY_SUPPORTED 103, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 17. Next pending claim by priority: `1326:objective_ranking_or_market_share:9a1e08d41d3aa67e` (台化).

## Author batch `author-034` — 2026-10-06

- Reviewed the next eight unreviewed objective ranking/market-share claims in checkpoint order (台化 1326 ×3, 東鹼 1708, 和桐 1714 ×4). Evidence came from directly downloaded and inspected official disclosures: 台化2017年法人說明會簡報、東鹼2025年度英文年報、和桐110年度年報與2025年法人說明會簡報。
- `1326:objective_ranking_or_market_share:9a1e08d41d3aa67e` — `PARTIALLY_SUPPORTED`. 台化簡報第4頁「市場地位」載「全球第2大苯乙烯(SM)製造商；全球第3大ABS、合成酚(PHENOL)製造商；全球第5大PS製造商；全球第7大芳香烴(AROMA)、PTA、PC製造商」，第5頁歷史沿革載其1973至1994年陸續加入耐隆、PTA、PS、ABS 生產，支持垂直整合之產品線。惟官方未以「台灣最大」描述該四項產品，其表述為全球排名（更強但不同之陳述）。
- `1326:objective_ranking_or_market_share:f1c330ef2220ac46` — `PARTIALLY_SUPPORTED`. 全球排名支持其芳香烴與 PTA/SM 之領先地位；惟「台塑集團四大核心旗艦成員」與「全台產能最大」未見於簡報（第13頁僅列個別產品目前與擴建後年產能）。
- `1326:objective_ranking_or_market_share:ab200ad4f1ede1d8` — `UNKNOWN_AFTER_RESEARCH`. 台化簡報第6頁僅列投資架構（含台塑集團(開曼)等），全份未載原料供應來源、未提及台塑化為其供料中心，亦無「獨家」或能源效率之陳述。
- `1708:objective_ranking_or_market_share:1769e438bc571e76` — `PARTIALLY_SUPPORTED`. 東鹼2025年年報載主要產品線為 Potassium sulfate 與 Soda ash，並詳列 Liquid calcium chloride、Hydrochloric Acid、Soda Ash、Baking Soda 等，對應 claim 之產品組合；惟全份年報「the only」出現次數為0，「唯一」未獲支持。
- `1714:objective_ranking_or_market_share:849ab16abec60b83` — `PARTIALLY_SUPPORTED`. 和桐110年度年報第10頁載「作為世界界面活性劑原料工業的龍頭企業」，第18頁載其以成為界面活性劑產業領導者為目標，官方層級高於 claim 之「亞洲最大」；惟「亞洲最大」於年報出現次數為0，正烷屬烴之「龍頭」亦未載（僅載其供應亞洲其他客戶）。
- `1714:objective_ranking_or_market_share:adfae1c40f1b5b8e` — `PARTIALLY_SUPPORTED`. 年報載「目前本公司主要生產原料－煤油均係向台灣中油股份有限公司購入」，支持煤油來自台灣本土大型煉油廠；惟「純苯 (Benzene)」於年報出現次數為0。
- `1714:objective_ranking_or_market_share:1ec145cda72231d8` 與 `54021868aa7d2922` — `PARTIALLY_SUPPORTED`. 兩岸產能佈局（年報第9頁載其為第一家赴大陸投資石化廠之台灣企業）與 LAB/NP 產品線獲支持；客戶部分獲年報第21頁「供給下游清潔劑產品製造商如P&G、Unilever等」支持，惟「花王」「獅王」出現次數均為0，且「全亞洲產量最大」「絕對規模經濟與高度定價優勢」「極高單一供料市占率」均未載。
- Proposed wording is recorded for the partial claims in `semantic/author-034.json`; no issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。
- Author-reviewed total: **172 / 1,399**; remaining: **1,227**. Outcome counts: ACCEPTED 40, PARTIALLY_SUPPORTED 110, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 18. Next pending claim by priority: `1723:objective_ranking_or_market_share:b3cf265f3bf03e83` (中碳).

## Author batch `author-035` — 2026-10-06

- Reviewed the next eight unreviewed objective ranking/market-share claims in checkpoint order (中碳 1723 ×2, 機光科技 6729, 鉅邁 8435, 昶昕 8438 ×4). Evidence came from directly downloaded and inspected official disclosures: 中碳2025年法人說明會簡報、機光科技公司簡介文件、鉅邁2025年法人說明會簡報、昶昕2024與2026Q2法人說明會簡報。
- `1723:objective_ranking_or_market_share:b3cf265f3bf03e83` — `ACCEPTED`. 中碳2025年官方簡報第5頁「基本資料」明載「國內唯一 煤化學工廠」，第6頁主要股東名單第1名為中國鋼鐵股份有限公司（29.04%），第7頁並以「上游產業（中鋼、中龍）—中游產業（中鋼碳素）」呈現其產業位置，claim 兩項敘述均獲支持。
- `1723:objective_ranking_or_market_share:abedfbeca6ee0f1f` — `PARTIALLY_SUPPORTED`. 簡報載「國內唯一 煤化學工廠」與「國內第一家 專業石墨化工廠」，並多處載軟瀝青（6處）、雜酚油（4處）與介相石墨碳微球（6處），後者並載「為24M半固態電池技術唯一驗證合格的負極材料」；惟「寡占」與「綠色金雞母」等修飾語未獲官方文件支持。
- `6729:objective_ranking_or_market_share:878a1a9ec489e500` — `PARTIALLY_SUPPORTED`. 機光科技公司簡介第1頁載「We are shipping to over 70（國）」，支持行銷逾70國；惟該 PDF 多數頁面為圖形排版、可擷取文字僅第1頁，未擷取到「唯一」或「完全自主研發」字樣，該公司亦無易於取得之官方文字年報可供核對。
- `8435:objective_ranking_or_market_share:e80d2822023c88a7` — `PARTIALLY_SUPPORTED`. 鉅邁2025年官方簡報第8頁列冷卻水處理系統、廢水處理系統、鍋爐水處理系統、特用水處理劑、RO阻垢劑／殺菌劑與RO水處理系統，第18頁載其為水處理服務商；惟全份簡報「前三大」「市佔」「市占」出現次數均為0，「市佔約20%」未獲支持。
- `8438:objective_ranking_or_market_share:fc6a98646b04f985` — `PARTIALLY_SUPPORTED`. 昶昕2026Q2官方簡報可擷取文字中「硫酸銅」出現4次、「銅」16次，第11及12頁營業項目列特用化學品與回收廢液；惟「PCB」「市佔」「市占」「80%」「3萬」及「最大」等出現次數均為0，「台灣 PCB 特用化學品龍頭（市佔約80%）」與「東亞最大硫酸銅出口商（年產逾3萬噸）」均未獲支持。
- `8438:objective_ranking_or_market_share:4d8d631a88512604`、`c76e972ea99e7f8f`、`53bcfea6d2bddac1` — `UNKNOWN_AFTER_RESEARCH`. 昶昕2024與2026Q2官方簡報均未具名任何客戶；「臻鼎」「欣興」「健鼎」「華通」「敬鵬」「PCB」「剝膜」於兩份簡報之出現次數均為0（僅2024年簡報以英文載「Glass substrate etching」1次），故客戶關係未獲確立。
- Proposed wording is recorded for the partial claims in `semantic/author-035.json`; no issuer report was modified. Independent review remains pending.
- 來源檢索限制：機光科技簡報為圖形排版 PDF、昶昕簡報文字層稀疏；此為檢索限制之紀錄，未用以推論 claim 真偽。`local-recheck-queue.json` 維持 **15** 筆。
- Author-reviewed total: **180 / 1,399**; remaining: **1,219**. Outcome counts: ACCEPTED 41, PARTIALLY_SUPPORTED 114, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 21. Next pending claim by priority: `2345:objective_ranking_or_market_share:45533474be4d6591` (智邦).

## Author batch `author-036` — 2026-10-06

- Reviewed the next eight unreviewed objective ranking/market-share claims in checkpoint order (智邦 2345, 訊舟 3047 ×3, 波若威 3163 ×2, 台嘉碩 3221 ×2). Evidence came from directly downloaded and inspected official disclosures: 智邦2016年股東會年報、波若威2020年公開說明書、台嘉碩2026年5月法人投資說明會簡報；訊舟與康全電訊之官方來源於本批次全數取得失敗。
- `2345:objective_ranking_or_market_share:45533474be4d6591` — `PARTIALLY_SUPPORTED`. 智邦2016年年報第4頁載其積極參與 OCP（開放運算計畫），第44頁載其為「第一家通過OCP(Open Compute Project)認證的10G交換器」，第42頁載其為享譽全球的 OEM/ODM 領導廠商；惟「白牌」於全份年報出現次數為0，「市佔率近49%」亦未載（第44頁所引數字係 Gartner 之市場環境資料，非智邦自身市占）。
- `3047:objective_ranking_or_market_share:8d08849b1db7901e`、`ccd9decfc4baa78c`、`6665972999a4ae24` — `UNKNOWN_AFTER_RESEARCH`. 本批次嘗試之訊舟科技官方來源全數失敗：官網年報端點（2014、2013年度）均 HTTP 404，公開資訊觀測站年報端點回傳320 bytes 非文件內容、簡報端點 404；與 claim 直接相關之康全電訊（8089）法說會端點 404、年報端點亦回傳320 bytes。故持股約33%、印度最大行動電信業者5G標案與營收成長幅度均無權威來源可確認或否證。
- `3163:objective_ranking_or_market_share:f4538d7b4e0ae3de` 與 `db69c04b1b9da86f` — `PARTIALLY_SUPPORTED`. 波若威2020年公開說明書第36及37頁載其經營範圍為5G、數據中心與光纖到戶之光通訊被動元件、模組及次系統，產品含濾片式 DWDM/CWDM 模組、平面光波導分光器（PLC splitter）與光纖連接產品（含 MPO/MTP、AOC）；第47頁載其於2003/2004年為日本 FTTH 市場光纖耦合器及波分複用器之主要供應商。惟「台灣最大」與「CPO」出現次數均為0（第43頁之5.18%係其占台灣光電產業產值之比率）。
- `3209:objective_ranking_or_market_share:375fbb618f362445` — `PARTIALLY_SUPPORTED`（本筆係於本批次追加，以維持佇列順序）。全科科技111年度年報第8頁公司沿革載2003年「取得Broadcom 公司產品代理權」，並載子公司與 Broadcom 簽訂大陸經銷合約、獲 Broadcom 頒發2012與2014年傑出通路商；沿革亦載「取得Cypress 及Zilltek 之代理權」。惟：年報所載之 Cypress 整合關係為「（Infineon）業務移轉及整合協議，為使Infineon 與Cypress 業務銷售系統整合強化」，即 Cypress 係與 Infineon 整併而非由 Broadcom 併購，claim 之「Broadcom（及併購之Cypress）」在併購主體上不成立；「全球最大網通晶片寡佔廠」「5G基地台聯網」「Wi-Fi 7」「AI資料中心第一手貨源」等於年報中出現次數均為0。
- `3221:objective_ranking_or_market_share:1c545b7df1052ede` 與 `9bfb232098e92952` — `PARTIALLY_SUPPORTED`. 台嘉碩2026年5月官方簡報第4頁載「6' & 4' Wafer Lithography and Foundry」與「MLCSP Assembly and Packaging」（支持其具 SAW 元件晶圓製程與封裝組裝能力），第5頁載完整頻率元件產品線，第10頁車用應用列 TPMS、Keyless Entry (RKE/PEPS/UWB) 與 GNSS，第11頁高速數據通信應用列 Optical/Smart NIC 400G/800G/1.6T。惟「台灣唯一具備全製程能力」「全球非手機用 SAW 濾波器市佔領先」及「核心技術團隊源自 Motorola」均未見於簡報。
- Proposed wording is recorded for the partial claims in `semantic/author-036.json`; no issuer report was modified. Independent review remains pending.
- 方法備註：本批次於 3163 與 3221 之間漏檢 `3209`（全科），經複核佇列順序後立即補做並追加為同批次第9筆，使佇列順序維持不中斷。
- 來源檢索限制：訊舟科技官網年報端點失效、公開資訊觀測站多個端點對該公司回傳非文件內容；此為檢索限制之紀錄，未用以推論 claim 真偽。`local-recheck-queue.json` 維持 **15** 筆。
- Author-reviewed total: **189 / 1,399**; remaining: **1,210**. Outcome counts: ACCEPTED 41, PARTIALLY_SUPPORTED 120, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 24. Next pending claim by priority: `3363:objective_ranking_or_market_share:26fa475a285812b8` (上詮).

## Author batch `author-037` — 2026-10-06

- Reviewed the next seven unreviewed objective ranking/market-share claims in checkpoint order (上詮 3363, 昇達科 3491 ×3, 神準 3558, 智易 3596 ×2). Evidence came from directly downloaded and inspected official disclosures: 上詮2025年度年報、昇達科2026年法人說明會簡報與財務說明文件、神準2022年法人說明會簡報、智易114年度股東會年報。
- `3363:objective_ranking_or_market_share:26fa475a285812b8` — `PARTIALLY_SUPPORTED`. 上詮2025年年報第72頁載其掌握「高密度、高精度的光纖陣列製造，以及ReLFACon 光纖陣列元件FAU 的精準對位與封裝技術」，第73頁列「二維光纖陣列精密對準共封裝技術」與「自動化矽光元件封裝技術」，第68頁載其長期目標為「CPO 光纖陣列元件之主要及重要供應商」。惟「COUPE」與「獨家」於全份年報出現次數均為0；「台積電」2次分別為資深廠長個人經歷與獨立董事研習課程名稱，非 CPO 認證或合作；「唯一」2處亦與市場地位無關。
- `3491:objective_ranking_or_market_share:94f1a06238faac2a` 與 `e76f95644dba4f6a` — `PARTIALLY_SUPPORTED`. 昇達科2026年簡報第3頁載「1999年9月成立」與「集團產品：微波&毫米波元件及天線」。惟「台灣唯一（微波／毫米波元件廠）」未獲支持——簡報中「唯一」出現次數為0，亦未以領導廠商或台灣唯一自稱。
- `3491:objective_ranking_or_market_share:b1519b89f78df062` — `PARTIALLY_SUPPORTED`. 簡報第4頁載低軌道衛星業務（2025年營收佔比59%）之主要客戶為「Amazon Leo / SpaceX / AST SpaceMobile / Intellian」，財務文件第12頁載其深化與 SpaceX、Amazon Kuiper、Eutelsat OneWeb 及 Telesat 之供應鏈關係。惟「SpaceX 為最大客戶」未獲確立：官方文件中「最大客戶」僅出現1次且未具名，其所述發射時程（2025年4月28日首批、2025年6月13日第二批）與 Amazon Leo（Kuiper）之首兩批衛星發射相符，且簡報將 Amazon Leo 列於主要客戶首位。
- `3558:objective_ranking_or_market_share:b07caacadd76de3a` — `UNKNOWN_AFTER_RESEARCH`. 神準2022年官方簡報第4及9頁載其產品為無線與有線解決方案及企業無線電話、OEM/ODM 占銷售92%，支持其以代工為主；惟全份簡報未出現 Cisco 或 Meraki，亦未具名任何客戶，故客戶身分未獲確立。
- `3596:objective_ranking_or_market_share:6e94f9bb077f0c5b` 與 `f3bf92f9c38ba724` — `PARTIALLY_SUPPORTED`. 智易114年度年報第5頁載產品涵蓋 5G FWA、Wi-Fi 7 (802.11be)、GPON/XGSPON/ONT、NG-PON2 與 DOCSIS 4.0，第87頁載寬頻固網產品以 DSL IAD、PON 及 Cable Modem 為主，第116頁載「本公司法人董事暨大股東仁寶電腦工業股份有限公司」，支持隸屬仁寶集團與 IAD 產品線。惟「全球最大整合式接取設備 (IAD) 製造商」未獲支持——年報「全球最大」出現次數為0，「領先」多屬期許性用語；「車聯網雷達」亦未見於年報產品敘述。
- Proposed wording is recorded for the partial claims in `semantic/author-037.json`; no issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。
- Author-reviewed total: **196 / 1,399**; remaining: **1,203**. Outcome counts: ACCEPTED 41, PARTIALLY_SUPPORTED 126, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 25. Next pending claim by priority: `3694:objective_ranking_or_market_share:411bb8cf29a1b2fb` (海華).

## Author batch `author-038` — 2026-10-06

- Reviewed the next eight unreviewed objective ranking/market-share claims in checkpoint order (海華 3694, 合勤控 3704, 台聯電 4905 ×2, 振曜 6143 ×4). Evidence came from directly downloaded and inspected official disclosures: 研華113年度年報、合勤控官方新聞稿、台聯電113年第4季個體財務報告、振曜2024永續報告書與2025年法人說明會簡報。
- `3694:objective_ranking_or_market_share:411bb8cf29a1b2fb` — `PARTIALLY_SUPPORTED`. 研華113年度年報「採用權益法之投資」附註載：「海華於民國112年第3季將買回之限制員工權利新股註銷減資，致本集團持股比例從19.38%增加至19.39%，另本集團於民國112年第4季以現金$1,445處分海華部分股權，其持股比例從19.39%下降至19.37%」——即研華持股約 **19.37%**，與 claim 之「約佔10%股權」不符；年報並列「海華科技股份有限公司(海華)」於關聯企業份額表（帳面金額775,429仟元）。另年報載研華為艾訊、融程、華電網、鴻呈、旭人科技及恒商之單一最大股東，海華不在該名單。惟和碩集團歸屬、工業物聯網與 PC 代工出海口、筆電與電競品牌通路「市佔率高達五成」等均未載於查閱文件。
- `3704:objective_ranking_or_market_share:f2f3c18024370d07` — `ACCEPTED`. 合勤控官方新聞稿（2026-02-24）標題為「合勤控蟬聯入選標普全球永續年鑑 **獲全球通訊設備產業第一**」，內文載其「榮獲通訊設備產業（Communications Equipment）前 Top 1% 榮譽」，與 claim 相符（官方類別用語為通訊設備）。
- `4905:objective_ranking_or_market_share:4172615a2601a106` 與 `f8236f9419738a17` — `PARTIALLY_SUPPORTED`. 台聯電113年第4季個體財報第36頁註3載其對欣德芮持股達61.36%、「經評估對該公司具有控制力，自該日起成為本公司之投資子公司」，支持「子公司欣德芮」；註4則載其對達亞國際持股23.66%、取得一席董事、具重大影響力並改採權益法認列（第37頁列為「投資關聯企業」）。惟財報未載欣德芮「擴廠」，亦未載台聯電為達亞國際之單一最大股東（該報告僅就艾訊、融程、華電網、鴻呈、旭人科技及恒商等公司載明其為單一最大股東）。
- `6143:objective_ranking_or_market_share:eacb93af3612d24a` 與 `55422f78287ce5eb` — `PARTIALLY_SUPPORTED`. 振曜2024年永續報告第6頁載其成立於1997年、自2008年起投入電子書開發、提供 ODM 與 OEM 服務，並載「現為電子書閱讀器代工之領導廠商」，第21頁載電子書閱讀器出貨成長58%；惟「為全球最大電子書閱讀器代工製造廠」未獲支持——兩份官方文件「全球最大」出現次數均為0。
- `6143:objective_ranking_or_market_share:93413fcf26dee269` 與 `73dfb069f9845e04` — `UNKNOWN_AFTER_RESEARCH`. 振曜2024年永續報告與2025年法人說明會簡報均未具名任何客戶，「Kobo」「樂天」「Rakuten」「Amazon」出現次數均為0，故最大單一（代工）客戶身分未獲確立。
- Proposed wording is recorded for the partial claims in `semantic/author-038.json`; no issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。
- Author-reviewed total: **204 / 1,399**; remaining: **1,195**. Outcome counts: ACCEPTED 42, PARTIALLY_SUPPORTED 131, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 27. Next pending claim by priority: `6216:objective_ranking_or_market_share:35cb5307cb38ee31` (居易).

## Author batch `author-039` — 2026-10-06

- Reviewed the next six unreviewed objective ranking/market-share claims in checkpoint order (居易 6216, 岳豐 6220, 立端 6245 ×3, 瑞祺電通 6416). Evidence came from directly downloaded and inspected official disclosures: 居易2025永續報告書、岳豐2020年投資人簡報、立端2025年法人說明會暨年報資料與2020年企業社會責任報告書、瑞祺電通2026年法人說明會簡報。
- `6216:objective_ranking_or_market_share:35cb5307cb38ee31` — `PARTIALLY_SUPPORTED`. 居易永續報告第54頁明載「歐洲是居易的主要市場」，第11頁載其專注自有品牌「Vigor」並「獲得9次英國PC PRO雜誌最佳年度路由器品牌肯定」。惟全份報告未載任何市占率數字或市場排名，亦未就德國、荷蘭市場提出量化陳述。
- `6220:objective_ranking_or_market_share:08b79d0e2afacd31` — `ACCEPTED`. 岳豐2020年投資人簡報第4頁載「自從2006年購併Prime Wire」與「我們在2016年收購Monoprice」，第8頁沿革同載兩案；第7頁載「品牌通路的垂直整合以實現差異」，第20頁載「向下垂直整合並降低原物料價格波動風險」；第10、15及21頁載 Monoprice 電商平台（Monoprice.com）之 B2B／B2C 拓展。
- `6245:objective_ranking_or_market_share:658825ba3e219605` 與 `01e6d42e67b49976` — `PARTIALLY_SUPPORTED`. 立端2025年資料第57頁載「本公司在網路安全、AI 邊緣運算及5G應用市場取得顯著成長」，2020年CSR第18頁載其「網路安全專業平台，目前與全球主要網路安全公司都建立緊密合作關係」。惟「全球最大」於官方文件出現次數為0，「全球市佔率逾四成」與「北美約五成」均未載；文件中唯一市占相關敘述為「持續擴大在 SD-WAN、uCPE 全球市佔率」，產品範圍不同且未附數字。
- `6245:objective_ranking_or_market_share:58a28527f37f9002` — `ACCEPTED`. 立端2020年CSR第6頁載「（2020）年立端…發行了9億元私募無擔保可轉債，由台達電全數認購」，第18頁載「於2020年11月發行私募案，由台達電認購」；2025年資料第47頁「持股比例占前十名之股東」表（114年4月22日）列第1名台達電子工業股份有限公司 26,893,540 股、18.34%（第2名僅7.38%），第11頁並載董事鄭安兼任台達電子董事等職。
- `6416:objective_ranking_or_market_share:a6c6b74e700a6d31` — `PARTIALLY_SUPPORTED`. 瑞祺電通2026年官方簡報第6頁載其既有模式為「硬體供應商模式」（特徵含「一次性硬體銷售」「單一產品銷售模式」「單純為供應商關係」），第11及13頁載2026年H1網路安全（IT+OT）占營收66%，第12頁載美洲占銷售57%。惟全份簡報未出現「白牌」「OEM」字樣，未具名任何客戶，亦未載客戶集中度或出貨占比。
- Proposed wording is recorded for the partial claims in `semantic/author-039.json`; no issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。韋僑（6417）與沅聖（6638）之官方文件於本批次未及取得，留待後續批次處理，佇列順序不受影響。
- Author-reviewed total: **210 / 1,399**; remaining: **1,189**. Outcome counts: ACCEPTED 44, PARTIALLY_SUPPORTED 135, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 27. Next pending claim by priority: `6417:objective_ranking_or_market_share:f2fcac08e268dad2` (韋僑).

## Author batch `author-040` — 2026-10-06

- Reviewed the next eight unreviewed objective ranking/market-share claims in checkpoint order (韋僑 6417, 沅聖 6638, 嘉基 6715, 稜研 7812, 達運光電 8045 ×3, 康全電訊 8089). Evidence came from directly downloaded and inspected official disclosures: 韋僑2021年法人說明會簡報、沅聖113年度年報、嘉基2018年法人說明會簡報、稜研2025年法人說明會簡報、達運光電年報與2017年法人說明會簡報；康全電訊之官方來源再次全數取得失敗。
- `6417:objective_ranking_or_market_share:f2fcac08e268dad2` — `PARTIALLY_SUPPORTED`. 韋僑2021年官方簡報第17頁載「美洲占比最高，係醫療客戶對RFID（之需求）」，第5頁載其為「全球首家RFID廠商取得ISO 13485醫療器材（品質管理系統認證）」，第15頁載「醫療藥品」為主要應用。惟「2025年在美國成立子公司」未獲支持——該簡報發布於2021年，全份未出現「2025年」或「美國子公司」字樣。
- `6638:objective_ranking_or_market_share:a10e7dbfbe350734` — `PARTIALLY_SUPPORTED`. 沅聖113年度年報載「本公司112及113年度其第一大銷貨客戶占總銷售額之比重分別為13%及12%」，並載其「整體而言，本公司應無銷貨集中之風險」；即官方揭露之第一大客戶占比僅為13%與12%，與 claim 之「早期曾佔超八成恐怖收入」在量級上差距甚大。另「最大客戶為 Ring」未獲支持——全份年報「Ring」「Amazon」「亞馬遜」「門鈴」出現次數均為0。
- `6715:objective_ranking_or_market_share:f73e500d5e922beb` — `PARTIALLY_SUPPORTED`. 嘉基2018年官方簡報第5頁載「40G Thunderbolt獲Intel認證」「通過Intel 與 Apple TBT 技術測試認證」及多項 Thunderbolt 3 產品通過 Intel 認證，支持其 Thunderbolt 產品須取得 Intel 認證。惟「Thunderbolt 4/5 規格」「全球 Thunderbolt 技術的唯一授權原始開發者」與「提供高速介面控制器晶片」均未載於簡報（該簡報發布於2018年，早於 Thunderbolt 4）。
- `7812:objective_ranking_or_market_share:e6cb42dfad1770b6` — `UNKNOWN_AFTER_RESEARCH`. 稜研科技2025年1月官方簡報中「毫米波」出現39次（為其核心技術），惟「印度」與「全球最大」出現次數均為0，未載印度電信業者專案或任何「全球最大規模」之描述。
- `8045:objective_ranking_or_market_share:6295b64544ea58b8` — `PARTIALLY_SUPPORTED`. 2017年官方簡報第4頁明載「台灣第一大寬頻放大器（設備商）」，年報第5頁載其產品含1.2GHz及1.8GHz寬頻放大器與數位化光纖傳輸節點。惟「成立於1992年」與「總部位於新北市」未獲支持（查閱文件中「成立於」「1992」出現次數均為0）。
- `8045:objective_ranking_or_market_share:b159b59617de6cf8` 與 `a101d657fc95e240` — `ACCEPTED`. 年報第5頁載「公司是亞洲唯一通過北美主要MSO（多系統營運商）…」，2017年簡報第4頁明載「亞洲唯一通過北美主要MSO認證HFC研製商」與「以ACI自有品牌行銷」；年報第66頁銷售地區表載112年度美洲銷售金額2,164,818仟元、占93.10%（111年度76.50%），內銷僅4.98%，支持出口以美洲（美國）為最大宗且逾七成；2017年簡報第8頁載「通過Comcast認證」、第16頁載「美國前十大MSO，以Comcast及Charter為主，超過100個系統使用ACI產品」。
- `8089:objective_ranking_or_market_share:cee0f405aeaab0db` — `UNKNOWN_AFTER_RESEARCH`. 康全電訊公開資訊觀測站年報端點回應 HTTP 200 但內容僅320 bytes（非文件內容）、法說會端點回應404，本批次未取得任何可檢視之官方文件；其母公司訊舟科技之官方端點亦已於 author-036 證實失效。
- Proposed wording is recorded for the partial claims in `semantic/author-040.json`; no issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。
- Author-reviewed total: **218 / 1,399**; remaining: **1,181**. Outcome counts: ACCEPTED 46, PARTIALLY_SUPPORTED 139, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 29. Next pending claim by priority: `2301:objective_ranking_or_market_share:253cd0fbdf268d3a` (光寶科).

## Author batch `author-041` — 2026-10-06

- Reviewed the next eight unreviewed objective ranking/market-share claims in checkpoint order (光寶科 2301 ×4, 金寶 2312, 中環 2323 ×2, 仁寶 2324). Evidence came from directly downloaded and inspected official disclosures: 中環110年度年報與2025年營運展望簡報、仁寶114年度年報；光寶科技與金寶電子之官方文件於本批次均無法取得可檢索內容。
- `2301:objective_ranking_or_market_share:253cd0fbdf268d3a`、`91dae1d50cf674d0`、`c1562f098f12ec0e`、`0c7d1b024b811bb9` — `UNKNOWN_AFTER_RESEARCH` ×4. 本批次取得之光寶科技官方文件均不可用於文字核對：(1) 公開資訊觀測站 2026-05-04 簡報（2,318,022 bytes）經文字擷取後全檔僅20字元、僅1頁，屬影像／圖形排版；(2) 公開資訊觀測站年報端點 t100sa11_2301_113.pdf 回傳 HTTP 200 但內容僅320 bytes；(3) 官方投資人專區 https://www.liteon.com/zh-tw/investors 回應 HTTP 404；(4) 官方新聞室「為低軌衛星革命注入動能：低軌衛星地面站與強固型電源供應器的關鍵角色」頁面抓取失敗。故低軌衛星電源市占逾六成、橫跨三大遊戲機品牌等陳述均未獲確立。
- `2312:objective_ranking_or_market_share:21dca8dbbc43aba7` — `UNKNOWN_AFTER_RESEARCH`. 金寶電子官方年報（2024_Kinpo_Annual_Report.pdf）與 ESG 報告（esg.kinpo.com.tw）端點均回應 HTTP 403 禁止；公開資訊觀測站年報端點回傳320 bytes 非文件內容，故未取得可檢視之官方文件。
- `2323:objective_ranking_or_market_share:3c7df6a4b4366ff5` — `PARTIALLY_SUPPORTED`. 中環110年度年報第15頁載「中環由全球最大光碟片製造商正式邁進全球性電子品牌」，第18頁載「中環身為全球最大光碟片製造商」，第27頁載「光碟產品達到全球市占率第一」，第30頁載「光碟片全球市佔率達到6成」。惟「成立於1978年」（年報中「1978」僅見於陽明山山仔后美軍宿舍歷史之描述）、「隸屬台泥集團」（「台泥」「臺灣水泥」出現次數均為0）與「總部位於台北」（未以沿革載明）均未獲支持。
- `2323:objective_ranking_or_market_share:b03395fd40ab4638` — `ACCEPTED`. 同上各頁支持其為全球最大光碟片製造商與全球市占第一（年報另載光碟片市佔達6成、其 Verbatim 品牌通路在美歐日亞太「全球市佔率已超過五成」）；2025年官方簡報第3及9頁並載其產品涵蓋光碟、USB、記憶卡、SSD，以及「SSD / Flash + 光碟全鏈方案」。併註記其同時以 Verbatim 品牌自營，故地位陳述涵蓋製造與品牌。
- `2324:objective_ranking_or_market_share:5595511e820cef92` — `PARTIALLY_SUPPORTED`. 仁寶114年度年報中出現「戴爾電腦公司」與「Dell Products L.P.」各1次（於公司關係或往來對象之列示），支持其與 Dell 之往來；惟全份年報未載 Dell 為其最大筆電代工客戶，亦未載客戶別營收占比或排名（年報中「最大」3處分別描述他國為全球最大生產基地、知識管理與股東價值）。
- Proposed wording is recorded for the partial claims in `semantic/author-041.json`; no issuer report was modified. Independent review remains pending.
- 後續處理建議：光寶科技與金寶電子合計5筆 UNKNOWN 之主因為「官方文件不可讀取」（影像版簡報、MOPS端點回傳非文件內容、官方網域403/404），而非 claim 內容有誤。建議於後續輪次以不同路徑重試（例如 MOPS 年報端點於其他時點、或改由公司法說會其他年度簡報），並在獨立複核時一併檢視。此類限制未達 `local-recheck-queue.json` 之門檻（該佇列記錄的是 Cloud 環境之 HTTP 500–504 失敗），故佇列維持 **15** 筆。
- Author-reviewed total: **226 / 1,399**; remaining: **1,173**. Outcome counts: ACCEPTED 47, PARTIALLY_SUPPORTED 141, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 34. Next pending claim by priority: `2356:objective_ranking_or_market_share:ed253454231d412c` (英業達).

## Author batch `author-042` — 2026-10-06

- Reviewed the next seven unreviewed objective ranking/market-share claims in checkpoint order (英業達 2356, 倫飛 2364, 昆盈 2365, 廣達 2382 ×4). Evidence came from directly downloaded and inspected official disclosures: 英業達五十週年特刊、倫飛112年度年報、昆盈103年度年報與111年營運概況報告、廣達2018Q3法人說明會暨年報資料。
- `2356:objective_ranking_or_market_share:ed253454231d412c` — `PARTIALLY_SUPPORTED`. 英業達五十週年特刊第25頁載其與「當時全球最大筆電品牌業者康柏電腦」建立代工合作關係並成為台灣最大筆記型電腦代工業者，第35頁載「2002年，康柏被惠普併購…時期確立的ODM合作關係，延續至惠普時期」，第42頁載「繼續成為HP核心供應商」。惟全份特刊未載 HP 為其最大筆電代工客戶，亦無客戶別占比或排名。
- `2364:objective_ranking_or_market_share:1a5a7e549dde1f07` — `PARTIALLY_SUPPORTED`. 倫飛112年度年報第9頁載公司設有統籌軍規電腦 ODM/OEM 及工規電腦品牌業務之單位並載「對Durabook 現有軍工規產品與品牌之行銷」，第62頁載「持續投入研發軍/工規強固型筆記型電腦」與「業務發展核心為自有品牌Durabook」。惟「於2000年製造出第一台軍規強固型筆電」未載於年報。
- `2365:objective_ranking_or_market_share:694d960ffe356728` — `PARTIALLY_SUPPORTED`. 昆盈103年度年報載其提供國際品牌大廠滑鼠等產品並列多項滑鼠獲獎紀錄（「滑鼠」17次、「Genius」10次）；111年營運概況報告載輸入裝置產品線含滑鼠 Mice 與多個滑鼠系列（「滑鼠」8次、「Genius」7次）。惟「1985」「先驅」「第一支」「首支」於兩份文件中出現次數均為0。
- `2382:objective_ranking_or_market_share:e26e1066260b8298` — `PARTIALLY_SUPPORTED`. 廣達文件載註冊地址「桃園市龜山區文化二路188號」，第90頁明載「廣達筆記型電腦出貨量約4,240萬台，市佔率約為26%，為全球筆記型電腦代工廠之龍頭」，第92頁載其在全球資料中心設備市場出貨量與技術領先同業。惟「成立於1988年」未載（「1988」出現次數為0），「全球最重要之AI伺服器代工廠」屬評價性最高級，官方用語為「雲端運算資料中心解決方案的重要供應商」。
- `2382:objective_ranking_or_market_share:c8e56ca69d86acd4` — `ACCEPTED`. 同頁明載其為「全球筆記型電腦代工廠之龍頭」。
- `2382:objective_ranking_or_market_share:846efe9d83aac395` 與 `beca552fa505ce2a` — `PARTIALLY_SUPPORTED`. 文件第86及88頁載 QCT 為廣達旗下雲端事業部門、第92頁載其在全球資料中心設備市場領先同業；惟「全球前50大資料中心市佔逾五成」未載。
- Proposed wording is recorded for the partial claims in `semantic/author-042.json`; no issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。
- Author-reviewed total: **233 / 1,399**; remaining: **1,166**. Outcome counts: ACCEPTED 48, PARTIALLY_SUPPORTED 147, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 34. Next pending claim by priority: `2385:objective_ranking_or_market_share:22c3e7f8c90b61ca` (群光).

## Author batch `author-043` — 2026-10-06

- Reviewed the next eight unreviewed objective ranking/market-share claims in checkpoint order (群光 2385 ×4, 精元 2387 ×2, 研華 2395 ×2). Evidence came from directly downloaded and inspected official disclosures: 群光2025年報／股東會資料、精元2024永續報告書、研華113年度年報。
- `2385:objective_ranking_or_market_share:22c3e7f8c90b61ca` — `PARTIALLY_SUPPORTED`. 群光年報載「本公司自72年2月22日成立迄今」（民國72年即1983年）、「公司總部位於新北三重」與「總公司地址：新北市三重區光復路二段69號」；第63頁載「據公司內部及來自客戶端的統計資料，群光集團在NB鍵盤、影像模組以及電源供應器產品都是全球市佔率第一」，第64頁載三產品線「均居全球龍頭的地位」。惟「連續多年」於全份文件出現次數為0。
- `2385:objective_ranking_or_market_share:abe9e706555f9c9d`、`bdefdbbe34f7abee`、`57a3aa507e64e4f6` — `ACCEPTED`. 第63頁明載 NB 鍵盤與影像模組全球市佔第一、群光為全球鍵盤龍頭；第56頁輸入裝置產品線含桌上型電腦鍵盤與滑鼠、數位影像產品線含數位攝影機與筆記型電腦內建相機模組；第62頁載其影像技術應用於無線 IPcam；文件中「行車紀錄」出現6次、「車燈」1次（載其持續開發 LED 適應性車燈 (ADB) 模組）。註記：官方用語為「運動型數位攝影機」，claim 之「穿戴式攝影機」為相近但不同之品項。
- `2387:objective_ranking_or_market_share:fc8df196f3e558dc` 與 `e5e02db27813e6d2` — `ACCEPTED`. 精元2024年永續報告第27頁明載「精元電腦創立於1975年，在1999年掛牌上市…其中筆（記型電腦鍵盤為佔營收比重最高之主要產品）」，並載「目前為世界第一大筆記型電腦鍵盤製造商」；第30頁沿革載其參與台中市電腦商業同業公會之紀錄，與總部設於台中相符。
- `2395:objective_ranking_or_market_share:46485c9c097dd36f` 與 `9566784397e27fb6` — `PARTIALLY_SUPPORTED`. 研華113年度年報多處論述工業電腦產業（「工業電腦」出現19次）並載其獲2024台灣精品獎之緊湊型工業電腦系統 IPC-320 與無風扇邊緣AI推理系統等產品，「台北」出現14次。惟全份年報中「全球最大」出現次數為0，未以全球最大工業電腦品牌自稱；「1981」僅出現1次且未見於公司沿革陳述。
- Proposed wording is recorded for the partial claims in `semantic/author-043.json`; no issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。
- Author-reviewed total: **241 / 1,399**; remaining: **1,158**. Outcome counts: ACCEPTED 53, PARTIALLY_SUPPORTED 150, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 34. Next pending claim by priority: `3005:objective_ranking_or_market_share:a3b2b980edcf8e31` (神基).

## Author batch `author-044` — 2026-10-06

- Reviewed the next four unreviewed objective ranking/market-share claims in checkpoint order (神基 3005, 晟銘電 3013, 東碩 3272, 玉晶光 3406). Evidence came from directly downloaded and inspected official disclosures: 豐達科技2026年法人說明會簡報、神基控股2025年法人說明會簡報、晟銘電115年股東常會議事手冊、東碩資訊2014年法人說明會簡報、玉晶光113年度年報。
- `3005:objective_ranking_or_market_share:a3b2b980edcf8e31` — `PARTIALLY_SUPPORTED`. 神基2025年官方簡報第8頁載豐達科技為「系統認證廠商，生產航太應用與高階工業應用之扣件產品，為**亞太區少數獲認證的航太扣（件廠）**」——官方用語為「少數」而非 claim 之「唯一」；豐達科技自身簡報第5頁載主要產品為航太扣件與機加鍛造件、汽車扣件，第6頁載其為「四大航太引擎OEM認證供應商」，第7頁載其打入 CFM/GE 之 GE90、GEnx、GE9X 引擎平台。惟「通過 Safran 旗下 Snecma 認證」未獲支持——兩份簡報中「Snecma」「Safran」均未出現；「汽車安全帶扣件與電動車機構件」亦未載（僅載汽車扣件）。
- `3013:objective_ranking_or_market_share:0924d32218acf258` — `PARTIALLY_SUPPORTED`. 晟銘電子115年股東常會議事手冊載「本公司持續深耕伺服器機殼、機櫃與系統結構件領域，隨著人工智慧（AI）…」，支持其伺服器機殼業務；惟全份文件中「廣達」「緯創」「緯穎」與「最大」出現次數均為0，客戶身分與最大客戶地位未獲支持。
- `3272:objective_ranking_or_market_share:48f05562f3b2586d` — `PARTIALLY_SUPPORTED`. 東碩2014年官方簡報第8頁列多項擴充基座產品線（USB 2.0／3.0／Thunderbolt／4K2K／USB 3.1），第31頁載「東碩資訊於2013年成功完成 worldwide 第一台 Thunderbolt Light Ridge 擴充基座的研發與上市」，並載其與 Intel 合作進行第二代 Falcon Ridge 研發。惟「全球最大擴充基座 ODM 製造商」未獲支持（「全球最大」出現次數為0），「USB-C」亦未出現（簡報發布於2014年，僅載 USB 3.1）。
- `3406:objective_ranking_or_market_share:ccb265f012ed9da6` — `PARTIALLY_SUPPORTED`. 玉晶光113年度年報第59頁「最近二年度主要銷貨客戶資料」以代號揭露（113年度甲、乙、丙公司分別為32.36%、31.15%、8.53%），第67頁載「集團113年度最大銷貨客戶雖佔總營業淨額約32.36%，惟仍係屬國際品牌大廠所指定的交貨客戶」，支持其確有國際品牌大廠客戶。惟「Apple（最大客戶）、Huawei、Vivo」三家具名未獲支持——全份年報中「Apple」「蘋果」「Huawei」「華為」「Vivo」出現次數均為0。
- Proposed wording is recorded for the partial claims in `semantic/author-044.json`; no issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。本批次因時間預算僅完成 4 筆，佇列順序不受影響（下一筆為 3479 安勤）。
- Author-reviewed total: **245 / 1,399**; remaining: **1,154**. Outcome counts: ACCEPTED 53, PARTIALLY_SUPPORTED 154, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 34. Next pending claim by priority: `3479:objective_ranking_or_market_share:ec2d0140eda8f433` (安勤).

## Author batch `author-045` — 2026-10-06

- Reviewed the next four unreviewed objective ranking/market-share claims in checkpoint order (安勤 3479, 磐儀 3594, 鼎翰 3611, 科嘉-KY 5215). Evidence came from directly downloaded and inspected official disclosures: 鼎翰114年度年報、科嘉-KY官方公司文件、磐儀115年股東常會議事手冊；安勤科技之官方端點於本批次全數取得失敗。
- `3479:objective_ranking_or_market_share:ec2d0140eda8f433` — `UNKNOWN_AFTER_RESEARCH`. 本批次嘗試之三條安勤官方路徑均回應 HTTP 404：發行人官方網域年報 PDF（avalue.com/upload/2024_05_29/…）與另一官方年報路徑（avalue.com/upload/2023_08_10/…），以及公開資訊觀測站簡報端點。故仁寶之持股比例與最大股東地位未獲確立。
- `3594:objective_ranking_or_market_share:8a5b9baaa79c34f3` — `UNKNOWN_AFTER_RESEARCH`. 磐儀115年股東常會議事手冊（10,282,022 bytes、67頁）自發行人投資人專區下載成功，惟全文文字擷取結果中「樺漢」「拌漢」「聯發」「磐旭」「智能」「機器人」「主要股東」「持股比例」出現次數均為0（「股東」279次、「持股」10次），且第14頁等內容頁呈現零散數字排列，顯示多數內容頁之文字層無法正常擷取。故樺漢之入股與磐旭智能之合資關係未獲權威文字確認。
- `3611:objective_ranking_or_market_share:2740038399a03d39` — `PARTIALLY_SUPPORTED`. 鼎翰114年度年報中「條碼印表機」出現34次，第10頁載其產品線含條碼印表機並述全球化佈局；惟「台灣第一大」「全球前五大」「全球前5大」「世界第一」「全球第一」出現次數均為0，「市佔」僅1次且為未附數字之通用語（「搶佔市佔率的良機」）。
- `5215:objective_ranking_or_market_share:209ea0f8303b4060` — `PARTIALLY_SUPPORTED`. 科嘉官方公司文件第3及4頁載「公司主要產品：薄膜觸控開關」「MTS – Membrane Touch Switch」「筆電用薄膜觸控開關」並附示意圖（「薄膜觸控開關」5次、「MTS」3次）；惟「全球最大」與「市佔」出現次數均為0。
- Proposed wording is recorded for the partial claims in `semantic/author-045.json`; no issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗之佇列項目；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。本批次完成 4 筆，佇列順序不受影響（下一筆為 6166 凌華）。
- Author-reviewed total: **249 / 1,399**; remaining: **1,150**. Outcome counts: ACCEPTED 53, PARTIALLY_SUPPORTED 156, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 36. Next pending claim by priority: `6166:objective_ranking_or_market_share:b3a2e1a025feff65` (凌華).

## Author batch `author-046` — 2026-10-06

- Reviewed the next five unreviewed objective ranking/market-share claims in checkpoint order (凌華 6166, 廣明 6188, 飛捷 6206, 全譜 6228, 宏正 6277). Evidence came from directly downloaded and inspected official disclosures: 凌華108年度年報、廣明官方股東資料與公開資訊觀測站簡報、飛捷2025年法人說明會簡報、全譜113年度年報與2025年法人說明會簡報、宏正93年度年報。
- `6166:objective_ranking_or_market_share:b3a2e1a025feff65` — `PARTIALLY_SUPPORTED`. 凌華108年度年報載其產品與技術含「COM Express, SMARC, Qseven」等模組化電腦規格，文中「ROS」出現5次。惟「友達」「鴻海」「法博」出現次數均為0，故「友達為最大單一股東」與「與鴻海合資成立法博智能」未獲該文件確認；該年報基準為民國108年度（2020年7月刊印），早於相關股權與合資事件。
- `6188:objective_ranking_or_market_share:22cd3f0905111079` — `PARTIALLY_SUPPORTED`. 廣明官方股東／公司資料載「廣達電腦股份有限公司代表人：蔡文弘」等三筆，顯示廣達電腦為其法人董事（「廣達」3次），其簡報載「硬碟」3次支持儲存裝置業務。惟「客戶」「最大」「Toyota」「豐田」「晶圓」出現次數均為0，最大客戶身分與其他客戶群未獲支持。
- `6206:objective_ranking_or_market_share:11dce486dbff428d` — `PARTIALLY_SUPPORTED`. 飛捷2025年官方簡報第5頁載「自1984年成立以來，飛捷科技持續在零售、餐飲、醫療與工業自動化領域提供硬體創新設計與先進製造技術，其中更專注於POS 端點銷售系統、自助服務系統與嵌入式電腦系統之產品開發」，第6頁載「AI 餐飲解決方案」與「AI 零售解決方案」。惟「市佔」「市占」出現次數均為0，具名客戶、AI 影像辨識與醫療推車亦未載。
- `6228:objective_ranking_or_market_share:5c4944216c7b1727` — `PARTIALLY_SUPPORTED`. 全譜113年度年報第8、51及55頁與法人說明會簡報第4至18頁載底片型掃描器產品（簡報第12頁載「業界最完全的底片對應方案」）。惟「Kodak」「柯達」「Olympus」出現次數均為0，未載曾為該等廠商代工；年報第60頁之市佔率表係針對「螢光與化學光成像系統」市場，其中列全譜（Pacific Image Electronics）推估市佔率為 **<1%**，同頁「底片掃瞄器市場需求及成長預估」僅述需求趨勢、未載市占率；「30%」4處分別為股利政策、實收資本額與房貸成數。
- `6277:objective_ranking_or_market_share:7c8c5bb9d85cb3ea` — `PARTIALLY_SUPPORTED`. 宏正93年度年報中「KVM」出現52次、「台灣」34次、「第一」25次，支持其以 KVM 為核心產品線；惟「全球最大」與「市佔」出現次數均為0。須註記：本批次取得之官方年報為民國93年度（2004年）版本，距查證日逾20年，不足以佐證現況排名。
- Proposed wording is recorded for the partial claims in `semantic/author-046.json`; no issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。
- Author-reviewed total: **254 / 1,399**; remaining: **1,145**. Outcome counts: ACCEPTED 53, PARTIALLY_SUPPORTED 161, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 36. Next pending claim by priority: `6485:objective_ranking_or_market_share:5969e1c71ddb6ef2` (點序).

## Author batch `author-047` — 2026-10-06

- Reviewed the next five unreviewed objective ranking/market-share claims in checkpoint order (點序 6485, 緯穎 6669, 富世達 6805, 海柏特 6884 ×2). Evidence came from directly downloaded and inspected official disclosures: 點序113年度年報、緯穎2026 Annual Report（2025年度）、富世達2023年法人說明會簡報、海柏特2025年法人說明會簡報。
- `6485:objective_ranking_or_market_share:5969e1c71ddb6ef2` — `PARTIALLY_SUPPORTED`. 點序113年度年報第7頁董事名單載「美商金士頓科技（Technical Director of Kingston Flash）」，第26頁載「董事-美商金士頓科（技）」（「金士頓」出現14次），第5頁載其專注於快閃記憶體控制晶片之研發。惟「為其最大客戶」未獲支持（「最大客戶」出現次數為0），「江波龍（Emdoor）」亦未出現（0次）。註記：金士頓於年報中之角色為董事／股東關係，非以客戶身分揭露。
- `6669:objective_ranking_or_market_share:cfb91f237a82edd6` — `PARTIALLY_SUPPORTED`. 緯穎2026 Annual Report（2025年度）於風險事項明列「B. Excessive concentration of customers」並載因應策略（「Our customers are all world-leading large enterprises that provide stable demands to wide users in global markets」），第6頁載2025年合併營收950,663,310仟元及「The revenue share of AI-related products exceeds 50%」。惟「Meta」與「largest customer」出現次數均為0，年報未具名任何客戶；且第6頁之「exceeds 50%」係指 **AI 相關產品**營收占比，非單一客戶占比。
- `6805:objective_ranking_or_market_share:11c34a389f43139d` — `PARTIALLY_SUPPORTED`. 富世達2023年官方簡報第10頁「轉軸產品主要類別」明列「柔性屏轉軸」「外折手機柔性屏轉軸」「內折手機柔性屏轉軸」與「折疊筆電柔性屏轉軸」，第19頁載其「擁有完整的轉軸產品線（折疊手機、筆電）」。惟「華為」「Huawei」「三折」「Mate XT」「Motorola」「摩托羅拉」出現次數均為0。
- `6884:objective_ranking_or_market_share:ab0687cfaac7a080` 與 `b70dfbe1514f5901` — `PARTIALLY_SUPPORTED`. 海柏特2025年官方簡報第22頁載「未來展望: HSN 3.0 亞太授權服務第一品牌」，第9及11頁載其為「亞太區售後服務業的領導者」與「台灣專注於售後服務第一家上櫃公司」，第17頁載「近50品牌授權跨國經驗」，支持其授權服務定位與第一品牌目標；惟「客戶授權維持率自2021年至今均維持九成以上」未獲支持（「維持率」「九成」「90%」出現次數均為0）。第9頁另載「宏碁集團持股：63.18%」，顯示宏碁為母公司／控制股東，惟簡報未載品牌授權營收占比，亦未載 Acer 為最大單一品牌授權來源（其比較基礎為「其他品牌（不含Acer）」與「前五大品牌（不含Acer）」）。
- Proposed wording is recorded for the partial claims in `semantic/author-047.json`; no issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。
- Author-reviewed total: **259 / 1,399**; remaining: **1,140**. Outcome counts: ACCEPTED 53, PARTIALLY_SUPPORTED 166, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 36. Next pending claim by priority: `6928:objective_ranking_or_market_share:1f10b3d64aa834a7` (攸泰科技).

## Author batch `author-048` — 2026-10-07

- Reviewed the next six unreviewed objective ranking/market-share claims in checkpoint order (攸泰科技 6928 ×2, 品安 8088 ×3, 勤誠 8210). 本批次三家公司之官方文件均無法取得可檢索內容，全部結為 `UNKNOWN_AFTER_RESEARCH`，並逐項記錄嘗試路徑與失敗形式。
- `6928:objective_ranking_or_market_share:1f10b3d64aa834a7` 與 `82073e105897f2df` — `UNKNOWN_AFTER_RESEARCH`. 攸泰科技官方年報（ubiqconn.com，兩個年度路徑）皆下載成功（153,217 bytes）但文字擷取僅3字元，屬影像／圖形排版；公開資訊觀測站年報端點回傳320 bytes 非文件內容；公開資訊觀測站簡報 692820250827E001.pdf 下載成功（1,477,347 bytes）但文字擷取僅6,447字元，其中「金礦」「烏茲別克」「強固」「平板」「客戶」「礦」出現次數均為0。故烏茲別克金礦客戶與強固平板應用未獲確立。
- `8088:objective_ranking_or_market_share:6e48c96a0c0e420e`、`4b0c2a97dcdea7ad`、`27f8081da18866e3` — `UNKNOWN_AFTER_RESEARCH`. 品安科技官方議事手冊端點 eng.panram.com.tw 之 DNS 無法解析，www.panram.com.tw 同路徑回應 HTTP 404，公開資訊觀測站年報端點回傳320 bytes 非文件內容；未取得任何可檢視之官方文件，故金士頓之法人股東身分與最大代工客戶地位未獲確立。
- `8210:objective_ranking_or_market_share:e0ee072a64d65aef` — `UNKNOWN_AFTER_RESEARCH`. 勤誠興業官方網域之 2015 與 2016 年度年報端點均回應 HTTP 404，公開資訊觀測站年報端點回傳320 bytes 非文件內容，未取得可檢視之官方文件，故其公司基本資料、全球前三大地位與約13%白牌市占率均未獲確立。
- 後續處理建議（重要）：本批次6筆之共同成因是**官方文件不可讀取**（影像版 PDF、MOPS端點回傳非文件內容、官網 404／DNS 失敗），而非 claim 內容有誤。建議於後續輪次改採替代路徑：(1) 將影像版 PDF 以 pymupdf 轉為頁面影像後，以視覺方式逐頁檢視；(2) 改用各公司其他年度之官方簡報或年報；(3) 於 MOPS 端點可用時重試。此類限制未達 `local-recheck-queue.json` 之門檻（該佇列記錄 Cloud 環境之 HTTP 500–504 失敗），故佇列維持 **15** 筆。
- No issuer report was modified. Independent review remains pending.
- Author-reviewed total: **265 / 1,399**; remaining: **1,134**. Outcome counts: ACCEPTED 53, PARTIALLY_SUPPORTED 166, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 42. Next pending claim by priority: `1435:objective_ranking_or_market_share:6abe79fd3552bb12` (中福).

## Author batch `author-049` — 2026-10-07

- Reviewed the next four unreviewed objective ranking/market-share claims in checkpoint order (中福 1435 ×3, 大同 2371). Evidence came from directly downloaded and inspected official disclosures: 大同113年度年報；中福紡織之官方年報端點回傳非文件內容。
- 更正（author-048）：攸泰科技（6928）官方年報兩個路徑所下載之 PDF（各 153,217 bytes），經以 pymupdf 開啟檢視後確認**實為該公司網站之 404 頁面**（頁面文字含「404 Sorry, we couldn't find the page you were looking for」，僅3頁），而非 author-048 原先推測之「影像／圖形排版」。已於 `semantic/author-048.json` 之兩筆 evidence.note 附加更正說明（保留原文並標註更正），原判定（UNKNOWN_AFTER_RESEARCH）不變。
- `1435:objective_ranking_or_market_share:6abe79fd3552bb12`、`3716d349ab2a4699`、`0263fe5dc37d5f06` — `UNKNOWN_AFTER_RESEARCH`. 本批次嘗試取得中福紡織官方來源之結果：(1) 公開資訊觀測站年報端點 t100sa11_1435_113.pdf 回傳320 bytes 非文件內容；(2) 以臺灣證券交易所 OpenAPI「上市公司每日重大訊息」（openapi.twse.com.tw/v1/opendata/t187ap04_L）查詢，該端點僅回傳最新一日之重大訊息（出表日期1151005），不含本案所述之民國115年9月23日董事會決議；(3) 未查得該公司可檢視之官方投資人專區。註記：該公告主旨（「本公司董事會決議展延委託專業公司以公開標售方式處分位於桃園市中壢區中壢廠全部土地之契約」）可由多家券商與財經媒體之轉載頁面查得，惟依本審核之證據政策，搜尋結果與二手轉載僅作發現線索、不得作為證據，故未採用；該主旨亦未載明受託專業公司之名稱。故第一太平戴維斯（Savills）與仲量聯行（JLL）之角色未獲確立。
- `2371:objective_ranking_or_market_share:d43fbcdfc7da62f6` — `PARTIALLY_SUPPORTED`. 大同113年度年報中「變壓器」出現26次、「重電」21次、「配電盤」6次、「氣體絕緣開關」3次、「電抗器」2次，支持其重電事業群產品涵蓋電力變壓器、配電變壓器、電抗器、配電盤及氣體絕緣開關（GIS）。惟「是台灣唯一同時具備變壓器與開關設備之一體化電力設備製造商」未獲支持——全份年報中「唯一」與「一體化」出現次數均為0；「重電事業群為主要獲利引擎」亦未以該等用語載明。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。
- Author-reviewed total: **269 / 1,399**; remaining: **1,130**. Outcome counts: ACCEPTED 53, PARTIALLY_SUPPORTED 167, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 45. Next pending claim by priority: `2371:objective_ranking_or_market_share:7c1b7458bb352b9a` (大同).

## Author batch `author-050` — 2026-10-07

- Reviewed the next eight unreviewed objective ranking/market-share claims in checkpoint order (大同 2371, 東森 2614, 豐祥-KY 5288 ×3, 匯僑設計 6754, 新應材 4749 ×2). Evidence came from directly downloaded and inspected official disclosures: 大同113年度年報、東森109年度年報、豐祥-KY 2026及2024年法人說明會簡報、匯僑設計2021年法人說明會簡報、新應材2025年法人說明會簡報。
- `2371:objective_ranking_or_market_share:7c1b7458bb352b9a` — `PARTIALLY_SUPPORTED`. 大同113年度年報中「台電」出現33次，包含「配合台電電網強韌計畫」「投入345KV特高壓電纜新廠房與產線建置以因應台電的需求」「台電變電所統包工程」「依台電新規改良套管型桿上變壓器」等；惟「國內最大客戶」「最大客戶」出現次數均為0，「中東」亦為0（「東南亞」7次、「電力公司」8次）。
- `2614:objective_ranking_or_market_share:fc653f741714d04d` — `PARTIALLY_SUPPORTED`. 東森109年度年報第3頁載「東森擁有超過1,500萬月不重複訪客及874萬會員人數，作為台灣最大的網路媒體及電視購物企業」，第5頁載「東森媒體事業群為台灣最大的網路傳媒」，第11頁載「根據comScore所公布的跨平台裝置調查顯示，東森新媒體網路觸及率超過85％，已成為台灣地區新聞類網站第一名」，第12頁載2019年數位廣告營收超過8.4億元。惟「（及）衛星電視頻道」未獲支持——全份年報中「衛星」出現4次，分別為法規名稱「廣播衛星電視新聞自律執行綱要」與物流「衛星倉」，未載其擁有或經營衛星電視頻道。
- `5288:objective_ranking_or_market_share:e2b6169ea8b47d06`、`e03e47ad2fe08132`、`26d23c8673c73aeb` — `PARTIALLY_SUPPORTED` ×3. 豐祥2026及2024年官方簡報沿革載「2006年: 合資成立越南Exedy（機車離合器），持股20%」與「2012年: 開始供應全球ORV大廠Polaris零件」，支持其越南機車零組件合資事業與 Polaris 客戶關係；惟兩份簡報中「Honda」「本田」「Yamaha」「Ducati」「Harley」出現次數均為0，「最大客戶」之身分未載，且簡報未載業務別營收比重，無法確認機車零組件為最大營收來源。
- `6754:objective_ranking_or_market_share:97bcd095ad4b455e` — `PARTIALLY_SUPPORTED`. 匯僑設計2021年官方簡報中「精品」出現6次，包含「►國際精品名牌」「Cartier杭州：大陸首家精品專賣店」「台北101公區及精品櫃位」「本公司深耕精品商業空間30餘年」「專注於高級精品店／高星級飯店／商務空間等高端領域之室內設計及裝修工程」。惟「LVMH」「Kering」「Richemont」與「市佔」出現次數均為0，未載三集團旗下品牌或80%市占率。
- `4749:objective_ranking_or_market_share:b6aa8390164f3bc1` 與 `8a41f0ce8cef58b5` — `PARTIALLY_SUPPORTED`. 新應材2025年官方簡報第6頁載客戶別為「晶圓代工客戶」、產品含「半導體先進製程光阻」與「先進製程用DUV光阻劑」，第18頁標題為「主要客戶先進製程未來產能布局」（「台積電」出現6次，含新聞引用）。惟「最大客戶」出現次數為0；且經逐項核對數字，簡報中「79%」係**半導體應用材料占營業收入之比重**（2019至2025年預估序列之最新值），「79.6%」係**2024年台灣占銷售區域之比重**，兩者均非單一客戶之營收占比。
- Proposed wording is recorded for the partial claims in `semantic/author-050.json`; no issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。
- Author-reviewed total: **277 / 1,399**; remaining: **1,122**. Outcome counts: ACCEPTED 53, PARTIALLY_SUPPORTED 175, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 45. Next pending claim by priority: `5225:objective_ranking_or_market_share:9878893f3dc16044` (東科-KY).

## Author batch `author-051` — 2026-10-07

- Reviewed the next four unreviewed objective ranking/market-share claims in checkpoint order (東科-KY 5225 ×3, 禾聯碩 5283). Evidence came from directly downloaded and inspected official disclosures: 東科-KY 114年股東常會議事手冊、禾聯碩114年度年報。
- `5225:objective_ranking_or_market_share:9878893f3dc16044`、`534c2c4cfb9c89c8`、`017ed3b68dac411f` — `PARTIALLY_SUPPORTED` ×3. 東科114年股東常會議事手冊第9頁載「2025年營運成長動能來自新產品、新客戶，**韓系**、日系及歐美系都有成長，歐美系成長幅度較大。除核心產品 Sound Bars 外，聚焦於高附加價值產品」，第10頁載「為客戶提供從 OEM、ODM 到 JDM 等彈性、靈活商業模式的一站式購（足）」，第11頁載系統產品線與「開發及進一步擴展TV用聲霸(Sound Bars)內嵌標準的SoCs」。全份文件中「Sound Bar」4次、「聲霸」2次、「OEM」2次、「ODM」2次、「客戶」21次、「韓系」1次；惟「Samsung」「三星」「LG」「全球最大」「市佔」「市占」出現次數均為0，故「全球最大影音揚聲器代工廠」、「Sound Bar 全球市佔率極高」與「Samsung 為最大客戶」均未獲支持。
- `5283:objective_ranking_or_market_share:6faaf45e05c0640f` — `PARTIALLY_SUPPORTED`. 禾聯碩114年度年報第5及52頁載其液晶顯示器朝智慧顯示與聯網發展（可作為家庭安全管理中樞、支援人臉辨識），第67頁載其推出國內第一台有錄影功能之液晶顯示器、Hertv 智慧液晶顯示器搭配禾聯智慧語音，並載「全國液晶顯示器尺寸、機種、功能最齊全的領先地位」（「高畫質」6次）。惟「台灣市佔率極高」與發行人自身揭露**不符**：年報第65頁「市場佔有率」段落明載「根據經濟部統計處生產統計月報數據顯示，2024年度國內市場液晶顯示器及家用空調之銷售值分別為新臺幣125.51億元及新台幣209億元，本公司及其子公司2024年度液晶顯示器及空調之銷售金額分別為新臺幣7.04億元及43.86億元，**市占率分別為5.61%及20.99%**」；全份年報中「極高」出現次數為0。建議以官方市占率數字取代該評價性描述。
- Proposed wording is recorded for the partial claims in `semantic/author-051.json`; no issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。
- Author-reviewed total: **281 / 1,399**; remaining: **1,118**. Outcome counts: ACCEPTED 53, PARTIALLY_SUPPORTED 179, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 45. Next pending claim by priority: `6225:objective_ranking_or_market_share:328bec4589432b52` (天瀚).

## Author batch `author-052` — 2026-10-07

- Reviewed the next eight unreviewed objective ranking/market-share claims in checkpoint order (天瀚 6225, 上洋 6728, 第一銅 2009 ×2, 中租-KY 5871 ×4). Evidence came from directly downloaded and inspected official disclosures: 天瀚111年度年報、第一銅112年度年報、中租-KY 110年度年報；上洋114年度年報之文字層呈現亂碼，無法判讀。
- `6225:objective_ranking_or_market_share:328bec4589432b52` — `PARTIALLY_SUPPORTED`. 天瀚111年度年報沿革載其分別對外投資美國 AIPTEK, INC.（美洲行銷）、德國 AIPTEK International GmbH（歐洲行銷）與上海愛普泰克國際貿易（中國行銷），並載「2000年04月 **推出全球第一台3合1筆式數位視訊相機**」。惟「早期從數位手寫板（HyperPen）起家」之品牌名稱未獲支持（「HyperPen」出現次數為0；年報所述為「筆式輸入電磁感應數位板」之技術與 ASIC 開發）。
- `6728:objective_ranking_or_market_share:d66093d3d854cbc7` — `UNKNOWN_AFTER_RESEARCH`. 上洋114年度年報（2,179,859 bytes）之文字擷取結果呈現亂碼（如「΋ǵҁϦљวقΓ」），無法辨識內容；於擷取文字中「AQUA」「Huebsch」「優必洗」「總代理」「洗衣」「日本」出現次數均為0。故 AQUA 之「日本以外全球唯一總代理」與 Huebsch 代理關係未獲確立。
- `2009:objective_ranking_or_market_share:40ef15d8963c4f66` 與 `99c95bc4f4f81779` — `PARTIALLY_SUPPORTED`. 第一銅112年度年報第75頁「上游：銅片製造廠：如台灣目前有**第一伸銅**、名佳利、東弘、…」，第77頁載「在台灣全部合金總銷售量約占**台灣市場30%**」，第7頁載其生產黃銅片、板、管（材）並開發磷青銅、引線架銅等高級合金材料（「黃銅」12次、「磷青銅」7次）。惟「白銅」出現次數為0，未列為其產品項目。
- `5871:objective_ranking_or_market_share:5462990384cd01df` — `PARTIALLY_SUPPORTED`. 中租-KY 110年度年報第10頁載「中租控股**穩居台灣租賃業領先地位**」與海外布局「擴及中國大陸、泰國、越南、馬來西亞、柬埔寨、菲律賓與印尼」（「中租迪和」29次）。惟官方未以「台灣最大」自稱，亦未載租賃業務市占率。
- `5871:objective_ranking_or_market_share:0d13f2e2c5782586` — `PARTIALLY_SUPPORTED`. 年報載業務項目為「租賃、分期付款、應收帳款受讓管理、放款等」並載其核心競爭力在於「與對中小企業客戶的合作模式」；惟「市佔率」出現次數為0，「裕融」「和潤」亦均為0。
- `5871:objective_ranking_or_market_share:87162f778667a426` — `UNKNOWN_AFTER_RESEARCH`. 本批次可檢視之最近官方文件為110年度年報（2021年），全份文件中「zingala」與「銀角」出現次數均為0，未載該平台、會員數或合作商家數。建議後續以2023年以後之年報或永續報告書重查。
- `5871:objective_ranking_or_market_share:8a01608f52e45045` — `PARTIALLY_SUPPORTED`. 年報第5頁載「在2018年裝置容量已成為**全台第一**，至2021年累積擁有2,655座太陽能電廠，年發電量為11.5億度」，第66頁載其「為**全台擁有最多太陽能電廠之企業**」並載2017年「全民電廠－共享金融市集平台」。惟「截至2024年底持有裝置容量超過1.5GW」未獲支持——年報所載為「2021年底合計擁有2,655座太陽能電廠。電廠發電總容量達**918.22MW**」，裝置容量目標為1,091MW。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。
- Author-reviewed total: **289 / 1,399**; remaining: **1,110**. Outcome counts: ACCEPTED 53, PARTIALLY_SUPPORTED 185, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 47. Next pending claim by priority: `6592:objective_ranking_or_market_share:2860da8fae309c7a` (和潤企業).

## Author batch `author-053` — 2026-10-07

- Reviewed the next four unreviewed objective ranking/market-share claims in checkpoint order (和潤企業 6592, 裕融 9941 ×3). Evidence came from directly downloaded and inspected official disclosures: 和潤2026年法人說明會簡報、裕融110年度年報。
- `6592:objective_ranking_or_market_share:2860da8fae309c7a` — `PARTIALLY_SUPPORTED`. 和潤2026年官方簡報第5頁載「成立時間：1999/5/25」「上市日期：2019/12/9」，並載集團架構圖（豊田財務服務株式會社45.4%、和泰汽車股份有限公司22.96%持有和潤企業），以及台灣事業含新車/中古車分期、商用車/大客車分期、企業融資與創能等。惟「為台灣非銀行金融機構中車輛分期租賃市佔率第一之龍頭」未獲支持：全份簡報中「市佔」出現次數為0，「市占」2次均為新車品牌登錄市占（「TOYOTA及LEXUS登錄市占合計達38%」）與市場規模敘述，「第一」與「龍頭」亦均為0。
- `9941:objective_ranking_or_market_share:e7f6d06661d25993`、`fd6ccb1d3918b0e9`、`72928707fcb8c094` — `PARTIALLY_SUPPORTED` ×3. 裕融110年度年報第14頁沿革載「1990.04 裕融企業成立，由裕隆汽車（股）公司與美國奇異財務公司各持50%股權，資本額6仟萬元」、其後「裕融企業在台灣證券交易所上市掛牌交易。（股票代號：9941）」、「購買新鑫（股）公司100%股權，進軍大貨車、大客車分期業務」、「收購格上汽車租賃（股）公司45%股權」、「與格上汽車租賃（股）公司共同購買行將企業（股）公司股權，綜合持股59%…取得SAVE中古車聯盟經營權」（年報中「新鑫」3次、「格上」20次、「行將」1次、「裕富」2次）。惟「台灣第一家上市之汽車融資企業」（「第一家」0次）、「新鑫為商用車融資龍頭、市佔第一」（「龍頭」0次、「市佔」僅1次泛用語）、「裕富數位與新鑫合計貢獻集團約半數獲利」（「半數」0次）與「格上租車每年貢獻約2億元獲利」（「2億」「兩億」皆0次）均未獲支持。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。
- Author-reviewed total: **293 / 1,399**; remaining: **1,106**. Outcome counts: ACCEPTED 53, PARTIALLY_SUPPORTED 189, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 47. Next pending claim by priority: `5904:objective_ranking_or_market_share:1c808dde25b1f8c1` (寶雅).

## Author batch `author-054` — 2026-10-07

- Reviewed the next eight unreviewed objective ranking/market-share claims in checkpoint order (寶雅 5904, 卓越 2496, 廣隆 1537, 直得 1597, 榮星 1617, 僑威 3078, 鴻碩 3092, 崧騰 3484). Evidence came from official issuer pages and directly downloaded official disclosures: 寶雅官方投資人專區公司簡介頁、卓越113年度年報資料、廣隆2022年法人說明會簡報、直得114年度年報、榮星2025年法人說明會簡報、僑威2022年永續報告書、崧騰2020年法人說明會簡報。
- `5904:objective_ranking_or_market_share:1c808dde25b1f8c1` — `PARTIALLY_SUPPORTED`. 寶雅官方投資人專區（HTTP 200）載「地址 台南市民族路三段74號」「產業類別 居家生活」「主要經營業務 (1)時尚美粧美材保養品 (2)流行內衣襪 (3)生活日常用品 (4)精緻個人用品」「公司成立日期 86/03/12」，支持其總部所在與業務性質；惟未載「台灣最大」「連鎖」或市占率。註記：該公司官網兩條財務報告 PDF 路徑均下載失敗（連接意外關閉），公開資訊觀測站年報端點回傳320 bytes 非文件內容。
- `2496:objective_ranking_or_market_share:f13fd59509def495` — `PARTIALLY_SUPPORTED`. 卓越113年度年報資料載「集團旗下之『陳立教育』專業的教學資源，從小學升私中、國中會考、高中學（測）到分科考、二階筆面試等」，並列「財團法人陳立教育基金會董事」等經歷（「陳立」10次、「高中」6次）；惟「全國最大」「最大」與「40年」出現次數均為0。
- `1537:objective_ranking_or_market_share:a9061697368a9c39` — `PARTIALLY_SUPPORTED`. 廣隆2022年官方簡報載「**KLB是東南亞產能最大的專業生產UPS電（池）**」，支持其產能地位；惟須更正範圍——官方用語為「**東南亞**」而非 claim 之「亞洲」（簡報另載「除中國外的亞洲國家生產者少」係描述競爭環境）。另「自有品牌 LONG 行銷逾100國」未獲支持（「LONG」「100國」皆0次）。
- `1597:objective_ranking_or_market_share:00f892e251ed2b4f` — `PARTIALLY_SUPPORTED`. 直得114年度年報中「半導體」32次、「醫療」10次、「自動化」64次、「線性滑軌」37次；惟「最大」6處均為「股東最大利益」「員工福祉為最大之原（則）」等語，無一處描述應用領域排序，亦未載各領域營收比重。
- `1617:objective_ranking_or_market_share:9fba43f07feab108` — `PARTIALLY_SUPPORTED`. 榮星2025年官方簡報中「漆包線」16次；惟「龍頭」「唯一」「最齊全」與「市佔」出現次數均為0（「台灣」僅1次）。
- `3078:objective_ranking_or_market_share:299b9d575f6c2dfd` — `PARTIALLY_SUPPORTED`. 僑威2022年永續報告書中「電源」103次；惟「全球最大」「代工」與「市佔」出現次數均為0。
- `3092:objective_ranking_or_market_share:e36782398881d1ed` — `UNKNOWN_AFTER_RESEARCH`. 鴻碩官方網域年報路徑所下載之 PDF（24,653 bytes）經文字擷取後僅1,086字元，內容為網站頁尾與導覽文字（「• 關於鴻碩」「Copyright © 2025 鴻碩精密電工股份有限公司」，另見「新能源線材系列」），並非公司文件，故其「全球最大顯示器訊號線製造商」地位與 HDMI/DisplayPort/USB 產品範圍未獲確立。
- `3484:objective_ranking_or_market_share:e42a3a40cfbcace6` — `PARTIALLY_SUPPORTED`. 崧騰2020年官方簡報中「開關」9次，並載「高耐受性開關設計」「防水防塵開關設計」與「電動汽車」應用；惟「全球最大」「電動工具」與「市佔」出現次數均為0（簡報所載應用為電動汽車而非電動工具）。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。
- Author-reviewed total: **301 / 1,399**; remaining: **1,098**. Outcome counts: ACCEPTED 53, PARTIALLY_SUPPORTED 196, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 48. Next pending claim by priority: `3484:objective_ranking_or_market_share:277360a2dcd0bf7c` (崧騰).

## Author batch `author-055` — 2026-10-07

- Reviewed the next four unreviewed objective ranking/market-share claims in checkpoint order (崧騰 3484, 維熹 3501 ×2, 碩天 3617). Evidence came from directly downloaded and inspected official disclosures: 崧騰106年度年報、維熹2025年法人說明會簡報、碩天官方年報。
- `3484:objective_ranking_or_market_share:277360a2dcd0bf7c` — `PARTIALLY_SUPPORTED`. 崧騰106年度年報第149頁「主要客戶資訊」表以代號揭露：106年度「甲客戶」銷貨金額1,912,550仟元、占營業收入**51%**（105年度39%），顯示其確有一家占比逾五成之最大客戶；第58頁並載「一般IT開關壽命要求為2.5萬次，專業級的電動手工具機(Professional Portable Power Tool)所要求的壽命則高達50萬次」（第94頁載銷貨對象為國外品牌電動工具機等客戶）。惟「最大客戶為 Makita（牧田）」未獲支持——全份年報中「Makita」「牧田」與「最大客戶」出現次數均為0，客戶一律以代號表示。
- `3501:objective_ranking_or_market_share:96a8139850c775d5` 與 `b771e5d09ccd216c` — `PARTIALLY_SUPPORTED`. 維熹2025年官方簡報第18頁載2025Q1~Q3產品類別「資訊及電機電器類電源線組 93%」（最大類別），第19頁載應用領域「家電類 44%（最大）、機電類15%、通路貿易類14%、其它類11%、消費性電子類8%、電腦網通類5%」。惟「電動車充電線/槍」（「電動車」「充電」皆0次）、「3C電子線材」（未列為獨立產品線）、「在美國家電市場市佔率高」（「美國」0次）與「主要客戶為 GE 與 Whirlpool」（字界比對之「GE」「GENERAL」「Whirlpool」「惠而浦」皆0次）均未獲支持。註記：該公司官方網域 wellshin.com.tw 於本批次無法連線，未取得年報。
- `3617:objective_ranking_or_market_share:c7e1929ec9b00de9` — `PARTIALLY_SUPPORTED`. 碩天官方年報載「（依）PC Data NPD Report 之調查結果，碩天科技之UPS產品，於北美地區**零售市場**拿下**35%之市佔率**並**僅次於全球第一大廠APC**」，支持其「北美第二大、僅次於 APC」之地位，但**數字與範圍須更正**：claim 所稱「約15%」於年報中查無對應（「15%」7處均為股東持股0.15%、研發投資抵減15%等無關敘述）；「20kVA以下」亦未獲支持，年報所述為「全球容量小於1KVA的小型UPS市場」與「**北美容量小於5KVA**的UPS市場」；「Schneider Electric」出現次數為0。註記：該版本依內容判斷為民國100年度（2011年）年報，非近期版本。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。
- Author-reviewed total: **305 / 1,399**; remaining: **1,094**. Outcome counts: ACCEPTED 53, PARTIALLY_SUPPORTED 200, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 48. Next pending claim by priority: `5227:objective_ranking_or_market_share:46ed0624b8da23c3` (立凱-KY).

## Author batch `author-056` — 2026-10-07

- Reviewed the next seven unreviewed objective ranking/market-share claims in checkpoint order (立凱-KY 5227, 新普 6121, 良維 6290, 旭隼 6409, 興能高 6558, 華景電 6788 ×2). Evidence came from directly downloaded and inspected official disclosures: 立凱電能法人說明會簡報、新普2023年永續報告書、良維2020年法人說明會簡報、旭隼2025年法人說明會簡報、興能高2024年永續報告書、華景電通2025年法人說明會簡報。
- `5227:objective_ranking_or_market_share:46ed0624b8da23c3` — `PARTIALLY_SUPPORTED`. 立凱電能官方簡報載「Aleees產品均為客製化產品，將在**美國**、歐洲、澳洲和印度**授權生產**」，並載其為「全球歷史最悠久的LFP材料公司」與「中國以外少數擁有完整LFP鋰電池正極材料製造技術與專利的公司之一」。惟「ICL」「4億」「補貼」「首座」「基建」出現次數均為0，故被授權商身分、4億美元投資、「美國首座」與基建法案補貼均未獲確立。
- `6121:objective_ranking_or_market_share:6289cc549c3bc5c6` — `ACCEPTED`. 新普2023年官方永續報告書載「在全球筆電(NB)電池組的**市佔持續維持全球第一**。每年提供**超過兩億個**電池組，市場上**每三個筆記型電腦中，就有一個為新普科技製造**」，與 claim 之「全球最大」「市佔率極高」「約每三台筆電就有一台」完全對應。
- `6290:objective_ranking_or_market_share:19c3d40cace1a46e` — `UNKNOWN_AFTER_RESEARCH`. 良維2020年官方簡報載其為「全球電源線及連接線的領導廠商」，支持業務性質；惟「Amazon」「Microsoft」「Lenovo」「ChargePoint」「最大客戶」出現次數均為0（「Apple」2次均為市場趨勢段落之「Apple TV+」服務名稱）。該 claim 之實質內容全為具名客戶身分，官方文件未具名任何客戶，故結為 UNKNOWN。
- `6409:objective_ranking_or_market_share:5d7e6075ec84567f` — `PARTIALLY_SUPPORTED`. 旭隼2025年官方簡報載「**100% ODM in UPS**」與「Well-positioned to be the key supplier for all segments of the UPS market globally」（「UPS」33次）。惟「全球最大」「largest」「台積電」出現次數均為0，故「全球最大純代工廠」與「不斷電界的台積電」之稱號未獲支持。
- `6558:objective_ranking_or_market_share:7f263d7df2605e0b` — `PARTIALLY_SUPPORTED`. 興能高2024年官方永續報告書載其產品「廣泛應用於**藍牙耳機**、無線健康穿戴裝置及其他各類可攜帶式電子產品，客戶遍佈於歐洲、北美洲及亞洲等地」；惟「市佔」「12%」出現次數均為0。
- `6788:objective_ranking_or_market_share:4cdbfeafed0be581` 與 `e15a4230aec4e97e` — `UNKNOWN_AFTER_RESEARCH`. 華景電通2025年官方簡報第4頁載其成立於民國89年、主要產品為「晶圓製程AMC防治設備」與「RFID整合派工系統」、子公司華景美國位於亞利桑那州鳳凰城，第9頁列產品應用製程節點（90nm至2nm）；第8頁雖有「優質客戶群」標題，其下文字層僅有英文通稱敘述。全份簡報中「台積電」「TSMC」「聯電」「旺宏」「Micron」「中芯」「最大」出現次數均為0。因兩筆 claim 之實質內容均為具名客戶身分，故結為 UNKNOWN。
- 一致性規則（自本批次起明確採用）：claim 實質內容**全為具名客戶身分**且官方文件未具名任何客戶 → `UNKNOWN_AFTER_RESEARCH`；claim **混合可查證之業務描述與不可查證之客戶／排名** → `PARTIALLY_SUPPORTED`。本批次之 6290 與 6788 兩筆適用前者，5227／6409／6558 適用後者。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。
- Author-reviewed total: **312 / 1,399**; remaining: **1,087**. Outcome counts: ACCEPTED 54, PARTIALLY_SUPPORTED 203, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 51. Next pending claim by priority: `6940:objective_ranking_or_market_share:a339a04db47953d6` (格斯科技).

## Author batch `author-057` — 2026-10-07

- Reviewed the next five unreviewed objective ranking/market-share claims in checkpoint order (格斯科技 6940 ×2, 新代 7750, 長園科 8038, 信錦 1582). Evidence came from directly downloaded and inspected official disclosures: 格斯科技2025年法人說明會簡報、新代2026年法人說明會簡報、長園科2023年法人說明會簡報、信錦2022年度股東會議事錄。
- `6940:objective_ranking_or_market_share:a339a04db47953d6` 與 `6cfe81e246b74e61` — `PARTIALLY_SUPPORTED`. 格斯科技2025年官方簡報以「鈦酸鋰」「LTO」「NCM」為產品主軸（「LTO」18次、「鈦酸鋰」7次、「NCM」9次、「軟包」3次、「儲能」18次），並載「LTO電池代工合約」「LTO,TNO（鈦酸鋰、鈮酸鈦）」，支持其專注 LTO 與 NCM 軟包電池芯；另載「安裝地點：**中油**嘉義綠能所加油站」，為文件中唯一提及中油之處，支持與中油之專案往來。惟「為台灣唯一具產業規模之 LTO 廠」（「台灣唯一」0次）與「中油為其最大客戶（儲能標案）」（「最大客戶」0次，未載標案規模或客戶別占比）均未獲支持。
- `7750:objective_ranking_or_market_share:f2879969d03c99dd` — `PARTIALLY_SUPPORTED`. 新代2026年官方簡報載「CNC 控制器」「AI賦能智慧控制器」「控制器與自動化產品」（「CNC」8次、「控制器」11次）。惟「亞洲領先」（0次）、「中國市佔逾20%」（「市佔」「市占」「逾20%」均0次）與「第三，僅次於 FANUC、Siemens」（「FANUC」「Siemens」均0次；「第三」1次係「第三個五年計劃」之期程用語）均未獲支持。
- `8038:objective_ranking_or_market_share:d89476319d794d57` — `UNKNOWN_AFTER_RESEARCH`. 長園科2023年官方簡報載「鋰鐵電池成市場主流」「半導體產業儲能系統」「UPS、儲能系統電池模組」（「鋰鐵」32次、「UPS」16次、「儲能」33次），支持其業務性質；惟「台積電」與「最大客戶」出現次數均為0。因該 claim 之實質內容為具名客戶身分，依本審核之一致性規則結為 UNKNOWN。
- `1582:objective_ranking_or_market_share:948268fc83d4768f` — `PARTIALLY_SUPPORTED`. 信錦2022年度股東會議事錄載「信錦企業股份有限公司之營業收入主要來自於銷售**顯示器樞紐**產品」，並載其「發明、新型等專利逾140項，多與**液晶監視器底座**產品相關，顯見本公司於**監視器軸承暨底座的領導地位**」。惟「全球最大」「市佔」與「Hinge」出現次數均為0，官方用語為「領導地位」而非全球最大。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。
- Author-reviewed total: **317 / 1,399**; remaining: **1,082**. Outcome counts: ACCEPTED 54, PARTIALLY_SUPPORTED 207, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 52. Next pending claim by priority: `2308:objective_ranking_or_market_share:102dbd9ad2f63ed0` (台達電).

## Author batch `author-058` — 2026-10-07

- Reviewed the next seven unreviewed objective ranking/market-share claims in checkpoint order (台達電 2308 ×3, 鴻海 2317 ×4). 台達電之證據來自官方「致股東報告書」頁面；鴻海之官方來源於本批次全數無法取得可檢視內容，四筆均結為 `UNKNOWN_AFTER_RESEARCH`。
- `2308:objective_ranking_or_market_share:102dbd9ad2f63ed0` 與 `abbcc068786a6239` — `PARTIALLY_SUPPORTED`. 台達電官方「致股東報告書」頁面（HTTP 200）載2025年度財務數據（營業淨利839億元、稅後淨利601億元、EPS 23.14元、ROE 24.1%），產品服務列有「電源及系統」「零組件」等事業範疇，並載其投入「AI電源與散熱解決方案」研發。惟「全球最大」「交換式電源」「市佔」出現次數均為0，未以全球最大交換式電源供應器製造商自稱。
- `2308:objective_ranking_or_market_share:b060444939608ba9` — `PARTIALLY_SUPPORTED`. 同頁載「台達持續關注人工智慧相關技術與應用發展，並與**主要AI晶片供應商及雲端服務客戶**維持合作關係，投入**AI電源與散熱解決方案**之研發」，另載因應高耗電需求導入「800VDC或±400VDC等高壓直流電源架構」、液冷解決方案（微通道液冷冷板、DC Pump、CDU），以及「多相型TLVR電感…已成功導入國際AI晶片大廠、伺服器製造商及雲端資料中心服務供應商」。惟「Tier 1」「CSP」「NVIDIA」「GB200」出現次數均為0，故「美系 Tier 1 CSP 最大供應商」與「NVIDIA DGX GB200 主要電源供應商」未獲支持。
- `2317:objective_ranking_or_market_share:862167a3881f91f4`、`26accf4568e21055`、`31793ac814a59391`、`066e13df74842145` — `UNKNOWN_AFTER_RESEARCH` ×4. 本批次嘗試取得鴻海官方文件之結果：(1) 官方年報專頁回應 HTTP 200 但為前端渲染應用，HTML 中無任何 PDF 連結；(2) 官方新聞稿頁（1977、1553）回應 HTTP 200，惟文字擷取結果僅有標題與樣式表，內文未呈現於靜態 HTML；(3) 官方投資人關係財務資訊網址回應 HTTP 404；(4) 公開資訊觀測站年報端點 t100sa11_2317_113.pdf 回傳320 bytes 非文件內容；(5) 官方股東會議事手冊 PDF（demo2.honhai.com）回應 HTTP 403。故全球最大 EMS/CDMS 地位、2023年營收6.16兆、最大客戶 Apple、雲端及網路營收占比突破41% 等均未獲確立。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。
- Author-reviewed total: **324 / 1,399**; remaining: **1,075**. Outcome counts: ACCEPTED 54, PARTIALLY_SUPPORTED 210, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 56. Next pending claim by priority: `2327:objective_ranking_or_market_share:4bc2906c15245aae` (國巨).

## Author batch `author-059` — 2026-10-07

- Reviewed the next seven unreviewed objective ranking/market-share claims in checkpoint order (國巨 2327, 敬鵬 2355 ×2, 台光電 2383 ×2, 億光 2393 ×2). Evidence came from directly downloaded and inspected official disclosures: 國巨2025年報、敬鵬111年度年報、台光電2023年度年報、億光2021年度年報。
- `2327:objective_ranking_or_market_share:4bc2906c15245aae` — `PARTIALLY_SUPPORTED`. 國巨2025年報第77頁「市場占有率」段明載「**國巨為全球鉭質電容第一大廠，市占率46％以上**，在車用、工業、軍用、航太、醫療、高階電腦等高階市場有極佳的發展位置」，與 claim 之「鉭質電容全球市占率46%（第一）」相符；同頁並載「**本公司是世界最大的晶片電阻製造廠商**」。惟「晶片電阻全球市占率34%」（「34%」之檢索結果為「(1.34%)」形式）、「MLCC 全球市占率15%（第三）」與「電感全球市占率12%（第三）」均未獲支持——年報之積層陶瓷電容與磁性元件段落僅述技術發展方向與市場需求，未載市占率或排名。
- `2355:objective_ranking_or_market_share:e2751dcf4f662431` 與 `45cccbbebc446916` — `PARTIALLY_SUPPORTED` 與 `UNKNOWN_AFTER_RESEARCH`. 敬鵬111年度年報載「營收增長主因為本公司以**汽車板業務為主**」及「的汽車板及以彈性製造為主要訴求的中量電路板為利基市場」（「汽車」17次、「PCB」82次），支持其車用板業務；惟「全球第四」出現次數為0，「市占」僅1次且為台灣 PCB 產業整體趨勢之泛用語，故「全球第四大車用 PCB、市占約10%」未獲支持。另「Bosch」「Denso」「Continental」「Magna」「Delphi」「Visteon」出現次數均為0，客戶清單依一致性規則結為 UNKNOWN。
- `2383:objective_ranking_or_market_share:d7e1c63f7e5f9a21` 與 `8cd3eedf1d33d1d5` — `UNKNOWN_AFTER_RESEARCH`. 台光電2023年度年報之文字層呈現**亂碼**（第2頁顯示「΋ǵҁϦљวقΓǺ」等非可讀字元，與上洋114年報同型之檢索限制），僅少數區段（如子公司資料表）可讀；「基板」「CCL」「載板」出現次數均為0，「銅箔基板」僅見於子公司業務描述。故其高速/高頻 CCL 市占冠軍地位與 M8/M9 平台敘述未獲確立。
- `2393:objective_ranking_or_market_share:855bf0c8d0c3d854` 與 `feb61c76bb10402c` — `ACCEPTED`. 億光2021年度年報第106頁「主要競爭對手及市場佔有率」段明載「**本公司目前為國內最大的LED 專業封裝廠**，在**照明元件、背光元件、手持裝置及消費型電子產品所需元件、車用元件及不可見光元件之產值明顯超過台灣同業**」，與 claim 之「台灣最大的 LED 專業封裝廠」「產品涵蓋照明元件、背光元件、手持裝置元件、車用元件及不可見光元件」「產值明顯超越台灣同業」逐項對應。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。
- Author-reviewed total: **331 / 1,399**; remaining: **1,068**. Outcome counts: ACCEPTED 56, PARTIALLY_SUPPORTED 212, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 59. Next pending claim by priority: `2402:objective_ranking_or_market_share:6eadc6e5bdc3ad83` (毅嘉).

## Author batch `author-060` — 2026-10-07

- Reviewed the next seven unreviewed objective ranking/market-share claims in checkpoint order (毅嘉 2402, 一詮 2486 ×2, 大立光 3008, 奇鋐 3017, 文曄 3036 ×2). 一詮與大立光之證據來自可直接下載檢視之官方文件；毅嘉、奇鋐與文曄之官方來源於本批次均無法取得可檢視內容。
- `2486:objective_ranking_or_market_share:e7b17a5349873c82` 與 `7243ef589ba0d390` — `ACCEPTED`. 一詮2023年永續報告書第15頁載「目前一詮精密**光電產業LED可見光及不可見光導線架的全球市佔率已經排名世界第一**」，並列「主要產品/服務 SMD 導線架 / **LED 導線架**、直下式電視背光模組 / **陶瓷基板**、**均熱片（半導體）** / **IC 導線架**」，與 claim 之「全球最大的 LED 導線架製造商」「產品涵蓋 LED 導線架、IC 導線架、陶瓷基板及散熱元件（均熱片）」逐項對應。
- `2402:objective_ranking_or_market_share:6eadc6e5bdc3ad83` — `UNKNOWN_AFTER_RESEARCH`. 毅嘉科技官網根網址回應 HTTP 200（內容長度97,294字元），惟年報路徑 www.ichia.com/images/shareholders/2025-4.pdf 以 http 與 https 協定存取均回應 HTTP 404，另一網域 www.ichia.com.tw 之同路徑亦為404，官方股東資訊頁 /shareholders.aspx 亦為404。故「全球 FPC 市占約1-2%」未獲確立。
- `3008:objective_ranking_or_market_share:851df492397be9dc` — `UNKNOWN_AFTER_RESEARCH`. 本批次取得之可檢視大立光官方年報為2013年度版本，全份文件中「Apple」「Samsung」「小米」「OPPO」「vivo」與「最大客戶」出現次數均為0（「客戶」27次均為通稱）。因該 claim 之實質內容為具名客戶身分，依一致性規則結為 UNKNOWN，並註記該版本非近期。
- `3017:objective_ranking_or_market_share:f76fbbb6956b1040` — `UNKNOWN_AFTER_RESEARCH`. 以多組查詢字詞搜尋奇鋐之官方年報或法人說明會文件，所取得者均為券商研究報告與第三方財經媒體，未查得發行人官方網域之可檢視 PDF 端點。
- `3036:objective_ranking_or_market_share:48c69f1daccb8476` 與 `8a0838b5f670f054` — `UNKNOWN_AFTER_RESEARCH`. 文曄官方營運簡報端點連續兩次下載嘗試（其中一次延長至420秒）均以「作業已逾時」失敗；另查得之官方永續報告書為2019年度文件。故「鴻海（最大客戶）、廣達、緯創」之客戶清單未獲確立。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。
- 趨勢註記：本批次新增5筆 UNKNOWN，使 UNKNOWN 累計 **64 筆**，佔已審338筆之18.9%，成因均為官方來源不可取得（404、下載逾時、未查得端點）。此類情形與 `local-recheck-queue.json` 所記錄之 Cloud 環境 HTTP 500–504 失敗性質不同，故未計入該佇列。
- Author-reviewed total: **338 / 1,399**; remaining: **1,061**. Outcome counts: ACCEPTED 58, PARTIALLY_SUPPORTED 212, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 64. Next pending claim by priority: `3037:objective_ranking_or_market_share:2416d3deb1742a86` (欣興).

## Author batch `author-061` — 2026-10-07

- Reviewed the next three unreviewed objective ranking/market-share claims in checkpoint order (欣興 3037 ×2, 精金 3049). Evidence came from directly downloaded and inspected official disclosures: 欣興105年度年報、欣興2026年第二季法人說明會合併財務資料、精金年報。
- `3037:objective_ranking_or_market_share:2416d3deb1742a86` — `PARTIALLY_SUPPORTED`. 欣興105年度年報中「載板」出現27次、「PCB」34次，並載「在經營策略上，IC 載板事業處將持續開發新材料與製程以因應未來（需求）」與覆晶載板新廠量產等沿革，「聯電」出現1次與其集團歸屬相符。惟「為全球最大 PCB 與 IC 載板製造商之一」未獲支持（「全球最大」出現次數為0）。註記：本批次可檢視之版本為105年度。
- `3037:objective_ranking_or_market_share:9b2f00b9af8d44c3` — `PARTIALLY_SUPPORTED`. 「從事 IC 載板業務」獲支持（105年報「載板」27次；2026年第二季法人說明會「ABF」1次）。惟「ABF 載板全球市佔率約18%」（105年報「ABF」0次、簡報亦未載市占率）、「僅次於日本 Ibiden」（「Ibiden」0次）與「為 NVIDIA、AMD、Intel 核心供應商」均未獲支持。
- `3049:objective_ranking_or_market_share:6538e9d4932d6c19` — `ACCEPTED`. 精金年報載「**瀚宇彩晶投資本公司**」「（瀚宇彩晶）正式為本公司**最大股東**」「（瀚宇彩晶取得）及兩位獨立董事，另瀚宇彩晶取得一席監察人」「**瀚宇彩晶於98年6月16日董監事改選後，對本公司具控制力**」，並載其業務與觸控與彩色濾光片相關（「觸控」82次、「彩色濾光片」5次、「瀚宇彩晶」26次），與 claim 之「早期從事彩色濾光片，後轉型為觸控感應器專業製造商，主要為瀚宇彩晶（最大股東）供應觸控面板」對應。
- 新增產出：**`semantic/unknown-followup.json`**（UNKNOWN 追蹤清單）。本清單彙整全部 `UNKNOWN_AFTER_RESEARCH` 之 HIGH claim 共 **64 筆**，欄位包含 claim_id、ticker、company、claim 原文、batch_id、failure_signature（失敗分類）、attempted_sources（已嘗試來源網址）與 recommended_retry（建議替代路徑）。失敗分類統計：mops_non_document 24、non_document_response 22、http_404 21、no_official_endpoint_found 21、image_only_or_tiny_text 7、http_403 5、client_rendered_only 4、connection_failure 3、garbled_text_layer 3、download_timeout 2、other_unclassified 30（同一筆可歸屬多類）。此清單供獨立複核階段直接照表重查，避免回溯60餘個批次檔。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。
- Author-reviewed total: **341 / 1,399**; remaining: **1,058**. Outcome counts: ACCEPTED 59, PARTIALLY_SUPPORTED 214, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 64. Next pending claim by priority: `3060:objective_ranking_or_market_share:56574c45f5224560` (銘異).

## Author batch `author-062` — 2026-10-07

- Reviewed the next five unreviewed objective ranking/market-share claims in checkpoint order (銘異 3060, 日電貿 3090 ×4). Evidence came from directly downloaded and inspected official disclosures: 銘異股東會議事手冊（英文版）、日電貿2022年永續報告書。
- `3060:objective_ranking_or_market_share:56574c45f5224560` — `PARTIALLY_SUPPORTED`. 銘異議事手冊（英文版）2023年度產品營收比重表載「**Voice Coil Motor (VCM) 39.38%**」「External Hard Drive (EHD) 16.30%」「**COVER 9.85%**」「HDD 6.90%」等，「Current Main Products」列入 VCM 與 COVER，另載「Top and bottom covers」，支持 claim 之核心產品；惟「在硬碟市場具極高市佔率」未獲支持——手冊中之市占率敘述係指 HDD 供應商（Seagate 43%第一、WD 37%、Toshiba 20%）之市場結構，非該公司自身市占率（「largest」3次均指其為關係企業 MAP 之最大股東）。
- `3090:objective_ranking_or_market_share:7839b23f63f20969`、`d81ef6b94a9da9ee`、`e2b3337349ce58cc`、`28a5bfc166db3a6e` — `ACCEPTED` ×4. 日電貿2022年官方永續報告書載「公司**代理全球最大的鋁質電解電容廠商日本佳美工 Nippon Chemi-con** 的產品，並進行多（元化佈局）」，並載其經營理念為「為**台灣最大被動元件代理商**」及「代理 **NCC** 與 Panasonic 電容器」，與 claim 之「台灣最大專業被動元件通路商」「鋁質電解電容—代理日本 Nippon Chemi-con（NCC，全球第一大）」逐項對應。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。
- Author-reviewed total: **346 / 1,399**; remaining: **1,053**. Outcome counts: ACCEPTED 63, PARTIALLY_SUPPORTED 215, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 64. Next pending claim by priority: `3152:objective_ranking_or_market_share:57faf7aa307b7942` (璟德).

## Author batch `author-063` — 2026-10-07

- Reviewed the next six unreviewed objective ranking/market-share claims in checkpoint order (璟德 3152, 優群 3217, 昇貿 3305, 閎暉 3311, 先進光 3362 ×2). Evidence came from directly downloaded and inspected official disclosures: 璟德2022年股東會議事錄、優群2024年法人說明會簡報、昇貿2026年法人說明會簡報、閎暉2024年法人說明會簡報、先進光股東會相關手冊。
- `3152:objective_ranking_or_market_share:57faf7aa307b7942` — `PARTIALLY_SUPPORTED`. 璟德股東會議事錄載「**璟德為國內首家專注於高頻整合元件與模組的設計及製造公司**」，並載其開發「5G毫米波基站所須高階**LTCC 天線模組**、濾波元件的基板材料與設計技術」。惟「台灣最大」出現次數為0（官方用語為「國內首家」，指進入時間先後而非規模最大），「全球前三大」與「市佔」亦均為0。
- `3217:objective_ranking_or_market_share:2f5f1672a80405d9` — `PARTIALLY_SUPPORTED`. 優群官方簡報載「**DDR4/5 SO-DIMM 系列獲品牌與協會認可, 市占No.1**」，支持其於 SO-DIMM 之領先地位。惟「超過50%市佔率」未獲支持——簡報中「50%」僅1次，原文為「2020年起 DDR 與 M.2 在全球筆電市占率超越50%」，係描述 DDR 與 M.2 規格於全球筆電之滲透率，非該公司自身市占率。
- `3305:objective_ranking_or_market_share:e2ce4b02cefa7379` — `PARTIALLY_SUPPORTED`. 昇貿簡報載其業務為「各種**銲錫製品**之生產及銷售」並列馬來西亞與越南子公司；惟「台灣第一」「全球前三」「千住」「Alpha」「市佔」出現次數均為0。
- `3311:objective_ranking_or_market_share:50321d8ad4f59f0e` — `PARTIALLY_SUPPORTED`. 閎暉2024年官方簡報中「穿戴」出現2次，支持其穿戴裝置零組件業務；惟「手機」「按鍵」「車用」「全球最大」「轉型」出現次數均為0，早期手機按鍵業務之歷史地位未獲支持。
- `3362:objective_ranking_or_market_share:0d1f1f055061087b` 與 `0734bd9829977ceb` — `PARTIALLY_SUPPORTED`. 先進光股東會相關手冊中「鏡頭」出現28次，支持其光學鏡頭業務；惟「NB」「筆電」「市佔」「70%」「龍頭」出現次數均為0，其「全球筆電鏡頭龍頭、市占逾70%」之地位未獲官方文件支持。
- 里程碑：本批次完成後，author 已審 **352 / 1,399（25.2%）**，突破四分之一。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。
- Author-reviewed total: **352 / 1,399**; remaining: **1,047**. Outcome counts: ACCEPTED 63, PARTIALLY_SUPPORTED 221, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 64. Next pending claim by priority: `3441:objective_ranking_or_market_share:8b98c062556b5eb7` (聯一光).

## Author batch `author-064` — 2026-10-07

- Reviewed the next six unreviewed objective ranking/market-share claims in checkpoint order (聯一光 3441, 由田 3455 ×2, 達邁 3645, 健策 3653 ×2). Evidence came from directly downloaded and inspected official disclosures: 由田2025年法人說明會簡報、達邁109年度年報、健策官方公司文件。
- `3441:objective_ranking_or_market_share:8b98c062556b5eb7` — `UNKNOWN_AFTER_RESEARCH`. 聯一光電官方網域之109年度與107年度年報端點均以「要求已經中止：連接意外關閉」失敗（兩種年度路徑均同），本批次未取得可檢視之官方文件，故其「台灣唯一本土資本之光學玻璃毛胚供應商」地位未獲確立。
- `3455:objective_ranking_or_market_share:9dab2c22ab03c4f4` — `PARTIALLY_SUPPORTED`. 由田2025年官方簡報中「PCB」9次、「LCD」5次、「面板」2次、「檢測」82次，支持其檢測設備業務涵蓋該等領域；惟「市佔率高」未獲明確支持——簡報雖載「各產業市佔率提升」「持續為本產業之領先地位及提高市佔率」等語，均為泛用語，未就 PCB 或 LCD 面板檢測載明市占率數字或排名。
- `3455:objective_ranking_or_market_share:7453775b6f91a65d` — `ACCEPTED`. 同簡報明載「**IC 載板 AVI 設備，連續（年數未擷取）年佔有率全球第一**」（AVI 即自動光學外觀檢查，對應 claim 之「外觀檢查」），並列「先進封裝多面檢測設備、半導體二極體晶圓級檢測設備」等產品；簡報中「半導體」23次、「封裝」10次、「載板」8次、「高市佔」1次，與 claim 之「轉型半導體封裝檢測」「在 IC 載板外觀檢查具有高市佔」對應（官方所述為全球第一，強度高於 claim 之「高市佔」）。
- `3645:objective_ranking_or_market_share:b5c3e6a0efaa2e89` — `PARTIALLY_SUPPORTED`. 達邁109年度年報載其業務為「聚醯亞胺薄膜之製造，客製化代工與銷售」，並載其「茁壯成為**全球生產PI薄膜領導廠商之一**」。惟「台灣最大」未獲支持——年報載其為「**台灣第一家**投入生產聚醯亞胺薄膜的廠商」，係指進入時間先後而非規模最大；「全球市佔位居前四名」亦未獲支持（官方用語為「領導廠商之一」）。
- `3653:objective_ranking_or_market_share:32b1017f613092df` 與 `be2f7c2dfae707bf` — `PARTIALLY_SUPPORTED`. 健策官方文件載「均熱片產品說明」「**均熱片產品市場狀況**」與「**伺服器ILM扣件產品說明**」，支持其均熱片與伺服器 ILM 扣件業務；惟「市佔」「台灣最大」與「Vapor」出現次數均為0，其「台灣最大均熱片供應商」「全球精密沖壓及散熱解決方案領導者」與「伺服器市場極高市佔」均未獲支持。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。
- Author-reviewed total: **358 / 1,399**; remaining: **1,041**. Outcome counts: ACCEPTED 64, PARTIALLY_SUPPORTED 225, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 65. Next pending claim by priority: `3481:objective_ranking_or_market_share:44f9e638883c3468` (群創).

## Author batch `author-065` — 2026-10-07

- Reviewed the next six unreviewed objective ranking/market-share claims in checkpoint order (群創 3481, 新鉅科 3630, 德微 3675, 聯嘉投控 3717, 新復興 4909 ×2). Evidence came from directly downloaded and inspected official disclosures: 群創2024年法人說明會簡報、丘鈦科技2021年度年報（香港交易所披露易）、德微2012年法人說明會簡報、聯嘉光電112年度年報、新復興2022年法人說明會簡報。
- `3481:objective_ranking_or_market_share:44f9e638883c3468` — `PARTIALLY_SUPPORTED`. 群創2024年官方簡報載「群創FOPLP的核心競爭力」「群創FOPLP 藍圖」與「**Innolux offers the world's largest panel of FOPLP**」，對應 claim 之「投入 FOPLP」「以業界最大基板開發」。惟「G3.5」「SpaceX」「低軌」「良率」「90%」出現次數均為0，故「G3.5 基板」「獲 SpaceX 低軌衛星晶片封裝訂單」（claim 本身以「傳獲」表述）與「Chip-first 良率達90%以上」均未獲支持。
- `3630:objective_ranking_or_market_share:f9e6204dc7cecd7a` — `PARTIALLY_SUPPORTED`. 丘鈦科技2021年度年報（香港交易所披露易）載「（本集團持續努力推動）**聯營公司新鉅科技股份有限公司**（「新鉅科技」，一家於台灣的證券櫃（檯買賣中心）上櫃之公司，股份代碼：3630）在智能手機攝像頭模組鏡頭、IoT攝像頭模組鏡頭及3D模組鏡頭等的發展」（「新鉅」15次、「聯營公司」36次），可確認兩者之聯營關係；惟全份年報未出現「最大股東」之表述，亦未載持股比例。
- `3675:objective_ranking_or_market_share:ff388e8864de4fbe` — `PARTIALLY_SUPPORTED`. 德微2012年官方簡報載「Diodes 集團」「2004 ~ 2011 年德微公司對 Diodes 集團（之往來）」與「(2) 受到**主要客戶（達爾集團）**之交易計價模式改變」，支持達爾集團為其長期主要客戶；惟「大股東」與「持股」出現次數均為0，其「核心大股東」地位未獲支持（該版本為2012年文件）。
- `3717:objective_ranking_or_market_share:2b120d56b6be96bd` — `PARTIALLY_SUPPORTED`. 聯嘉112年度年報載「（其）LED光源、LED模組及車燈模組並取得多國專利，**客戶包含 Ford、FCA、Tesla、BMW、TOYOTA、GM**」與「（世）界主流EV品牌正式合作包含 **Tesla, Rivian, Fisker, BMW, STLA, GM** 等」，並載「**UniFlex 與 UniFlex Linear** 系列技術亦已導入北美高級純電動跑車／純電休旅車」（「UniFlex」38次、「Tesla」7次、「GM」5次、「Ford」2次、「專利」26次），支持 claim 之技術與客戶；惟「在電動車領域擁有高市佔率」未獲支持——年報中唯一市占數字為「**LED聖誕燈串全球市佔率達20%**」，係指聖誕燈串產品而非電動車車燈。
- `4909:objective_ranking_or_market_share:36ef0e8eeb712017` 與 `154d95fab7c83bda` — `PARTIALLY_SUPPORTED`. 新復興2022年官方簡報載「新復興深耕高頻微波通訊PCB製造經驗累積超過35年，具備豐富的**高頻基板**生產製造經驗」，並列高頻基板、散熱基板、特殊複合材料基板與特殊車用基板等產品線（「LNB」2次、「衛星」4次、「基板」6次），支持其 LNB 與高頻基板業務；惟「市佔」「八成」「80%」與「龍頭」出現次數均為0，「全球市佔率高達八成、為絕對龍頭」未獲支持。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。
- Author-reviewed total: **364 / 1,399**; remaining: **1,035**. Outcome counts: ACCEPTED 64, PARTIALLY_SUPPORTED 231, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 65. Next pending claim by priority: `4555:objective_ranking_or_market_share:0bf8c0e0c843a66a` (氣立).

## Author batch `author-066` — 2026-10-07

- Reviewed the next seven unreviewed objective ranking/market-share claims in checkpoint order (氣立 4555, 泰鼎-KY 4927 ×3, 友輝 4933, 茂林-KY 4935, 臻鼎-KY 4958). Evidence came from directly downloaded and inspected official disclosures: 氣立2025年法人說明會簡報（英文版）、泰鼎-KY年報、茂林-KY 2024年永續報告書。
- `4555:objective_ranking_or_market_share:0bf8c0e0c843a66a` — `PARTIALLY_SUPPORTED`. 氣立2025年官方簡報（英文版）載「**Pneumatic Components (65%)**」「Precision Metal Manufacturing (35%)」與轉型方向「Automation & Robotics Industry」，並列「Automation Equipment」為應用。惟全份簡報中「Foxconn」「Hon Hai」「largest」出現次數均為0，未具名任何客戶，其「鴻海供應鏈（歷史最大客戶）」未獲支持。
- `4927:objective_ranking_or_market_share:9a67db1c7ece4dcb` — `PARTIALLY_SUPPORTED`. 泰鼎年報載其「主要營業項目為單面、雙面與多層硬式印刷電路板之製造與銷售」「產品除內銷**泰國**當地外，尚外銷至亞洲、歐洲及美洲等地區」（「泰國」112次、「PCB」50次）。惟「泰國最大台資 PCB 廠／泰國 PCB 王」未獲支持（「最大客戶」與「泰國PCB王」均為0次），且產能數字須更正——年報載「在115年依據業務預算，泰鼎之**月產能將落在50萬至60萬平方米**」，單位為平方公尺，與 claim 之「約100萬平方呎」不對應。
- `4927:objective_ranking_or_market_share:f082dccad3e35593` 與 `d87b353d1a5581c6` — `PARTIALLY_SUPPORTED`. 年報載「本公司及子公司之**主要客戶品牌包括 Samsung**、Sony、Bosch、Vantiva、Canon、HP、Toshiba與WDC 等國際一線客戶。本公司及子公司所生產之印刷電路板主要應用於包括**電視**、車用多媒體、電腦週邊、網通設備、家用娛樂設備等產品」，支持 Samsung 為其具名主要客戶品牌且電視為應用領域；惟「為最大客戶」未獲支持（「最大客戶」0次）。
- `4933:objective_ranking_or_market_share:349902327df33902` 與 `4958:objective_ranking_or_market_share:a4361df276711165` — `UNKNOWN_AFTER_RESEARCH`. 友輝官方年報端點以「連接意外關閉」失敗；臻鼎官方新聞稿 PDF（779,313 bytes）經文字擷取後全檔僅3字元（影像排版）。兩者之市場地位因此未獲確立。
- `4935:objective_ranking_or_market_share:4d485947dcc08af8` — `PARTIALLY_SUPPORTED`. 茂林2024年官方永續報告書中「導光板」38次、「發光鍵盤」2次，支持其相關業務；惟「Apple」「MacBook」與「最大供應商」出現次數均為0。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。UNKNOWN 追蹤清單已同步刷新至 **67 筆**。
- Author-reviewed total: **371 / 1,399**; remaining: **1,028**. Outcome counts: ACCEPTED 64, PARTIALLY_SUPPORTED 236, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 67. Next pending claim by priority: `4939:objective_ranking_or_market_share:2a2e5d7a4b653457` (亞電).

## Author batch `author-067` — 2026-10-07

- Reviewed the next seven unreviewed objective ranking/market-share claims in checkpoint order (亞電 4939, 臻鼎-KY 4958 ×2, 誠美材 4960, 鈺鎧 5228 ×3). Evidence came from directly downloaded and inspected official disclosures: 亞電108年度年報、誠美材公司文件、鈺鎧2022年法人說明會簡報。
- `4939:objective_ranking_or_market_share:2a2e5d7a4b653457` — `PARTIALLY_SUPPORTED`. 亞電108年度年報中「軟板」67次、「覆蓋膜」65次、「手機」49次、「FPC」39次、「穿戴」20次，支持其軟性印刷電路板相關材料業務與手機、穿戴應用；惟「最大宗」出現次數為0，且「車用」僅2次、未載「電池模組 FPC」之具體應用。
- `4958:objective_ranking_or_market_share:e9718e647cdf6213` 與 `40a491b3e2ad9593` — `UNKNOWN_AFTER_RESEARCH`. 本批次嘗試取得臻鼎-KY官方文件之結果：官方新聞稿 PDF（779,313 bytes）經文字擷取後全檔僅3字元；另查得之 topco-global.com 年報（ANNUAL-111CHN.pdf）經檢視後確認**非臻鼎之文件**（「臻鼎」「4958」「Zhen Ding」「ZDT」出現次數均為0）。故其 FPC 市占地位、客戶身分（Apple／Google／Microsoft）均未獲確立。
- `4960:objective_ranking_or_market_share:d14cd3d4febf570b` — `PARTIALLY_SUPPORTED`. 誠美材公司文件「董事及經理人資料」註記載「**群創光電(股)公司及代表人劉昭賢於109年5月6日辭任**」，顯示群創曾指派法人代表擔任其董事（且該法人董事已於2020年辭任）；惟全份文件中「群創」僅出現1次，未載其為客戶、長期合作夥伴或最大出海口（文件之核心產品為偏光板，出現16次）。
- `5228:objective_ranking_or_market_share:b96cf4a86eed0538`、`bc677a4369a50038`、`95ce91a2dd332b21` — `PARTIALLY_SUPPORTED` 與 `UNKNOWN_AFTER_RESEARCH` ×2. 鈺鎧2022年官方簡報載其為磁性被動元件製造廠，市場含「車用市場」「網通市場」「醫療電子」（「車用」17次、「醫療」14次、「網通」3次），支持其應用領域；惟「Cochlear」與「全球最大」出現次數均為0（簡報僅載「無線充電產品已被應用於電子耳朵」），故「全球最大電子耳品牌」及其客戶身分未獲確立。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。UNKNOWN 追蹤清單已同步刷新至 **71 筆**。
- Author-reviewed total: **378 / 1,399**; remaining: **1,021**. Outcome counts: ACCEPTED 64, PARTIALLY_SUPPORTED 239, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 71. Next pending claim by priority: `5243:objective_ranking_or_market_share:7d90a20a437364ad` (乙盛-KY).

## Author batch `author-068` — 2026-10-07

- Reviewed the next six unreviewed objective ranking/market-share claims in checkpoint order (乙盛-KY 5243 ×2, jpp-KY 5284, 光聯 5315, 佳總 5355 ×2). Evidence came from directly downloaded and inspected official disclosures: 乙盛2025年報、jpp-KY 2023年法人說明會簡報（英文版）、光聯109年度年報、佳總110年股東會議事手冊。
- `5243:objective_ranking_or_market_share:7d90a20a437364ad` — `PARTIALLY_SUPPORTED`. 乙盛2025年報（封面載「Eson Precision Ind. Co., Ltd. 乙盛精密工業股份有限公司 2025 年報」「股票代號 5243」）載「5.墨西哥子公司」與多處「**墨西哥來料加工廠**」（Engineering S.A. de C.V.、Multiwin de Mexico S.A. DE C.V.、Esonmex Monterrey S.A. DE C.V.），並載「**2023年啟動建置墨西哥蒙特雷新廠**」，支持其墨西哥生產據點；另載「資料庫中心(Data Center)、**AI 伺服器**產業及低軌衛星等等產業，皆為本公司長期以來關（注之領域）」（「伺服器」47次）。惟「最大生產基地」與「車廠」出現次數均為0。
- `5243:objective_ranking_or_market_share:94480ceb66fb33f4` — `UNKNOWN_AFTER_RESEARCH`. 年報中「Tesla」「特斯拉」與「最大客戶」出現次數均為0，未具名任何電動車客戶，依具名客戶身分規則結為 UNKNOWN。
- `5284:objective_ranking_or_market_share:48a30f3d8d283f3f` — `PARTIALLY_SUPPORTED`. jpp-KY 2023年官方簡報（英文）見「Thailand」2次、「經寶」4次與多處廠區規劃（AeroSpace / Non-Aero / Assembly plant、39,228m2、49,297m2、New plant 2023）；惟「1998」「鈑金」「largest」「最大」出現次數均為0。
- `5315:objective_ranking_or_market_share:a798cfedc1bf6d88` — `PARTIALLY_SUPPORTED`. 光聯109年度年報中「歐洲」8次、「高亮度」11次；惟「60%」全份僅1次且其上下文為「已買回數量占預定買回數量之比率(%) **60%**」（庫藏股買回比率），**與歐洲市場營收占比無關**；「寬溫」與「防水」出現次數均為0。
- `5355:objective_ranking_or_market_share:bc0ba778fa8f319e` 與 `357362a9262ba16e` — `PARTIALLY_SUPPORTED`. 佳總110年股東會議事手冊載研發方向含「持續開發厚鋼車用大功率電源單側雙層**鋁基板**開發」「**DBC厚鋼陶瓷板**新產品開發」「**MiniLED**板產品導入生產」等；惟「台灣最大」與「市占」出現次數均為0，且未載 TV 背光板或照明燈具等具體應用別。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。UNKNOWN 追蹤清單已同步刷新至 **72 筆**。
- Author-reviewed total: **384 / 1,399**; remaining: **1,015**. Outcome counts: ACCEPTED 64, PARTIALLY_SUPPORTED 244, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 72. Next pending claim by priority: `5392:objective_ranking_or_market_share:d4e84f8d9cd9bfc8` (能率).

## Author batch `author-069` — 2026-10-07

- Reviewed the next four unreviewed objective ranking/market-share claims in checkpoint order (能率 5392, 瀚宇博 5469 ×2, 嘉聯益 6153). Evidence came from directly downloaded and inspected official disclosures: 能率2023年法人說明會簡報、IKKA-KY（2250）2025年法人說明會簡報、瀚宇博2025年法人說明會簡報、嘉聯益2022年法人說明會簡報。
- `5392:objective_ranking_or_market_share:d4e84f8d9cd9bfc8` — `PARTIALLY_SUPPORTED`. 能率2023年官方簡報載集團關係「IKKA-JABON International Co.,Ltd. **IKKA-KY (2250 TT)** ABICO (8071 TT)」，確認其與 IKKA-KY 之關聯；而 IKKA-KY（2250）自身之2025年官方簡報載「碟式電子手煞車(EPB)零件(**AISIN**)」「電動滑門、車門零件(**AISIN**)」與「車用機構零組件及模組」（「AISIN」3次、「車用」9次），支持 AISIN 為其車用零件客戶（跨公司查證）。惟「供應日系車廠 **Toyota、Honda**」未獲支持（Toyota 僅見於能率簡報之資料來源註記「Data from Toyota website」，Honda 0次），「車用營收占比**逾五成**」亦未載。
- `5469:objective_ranking_or_market_share:bf78a8b9fd6271dd` 與 `a8dabb9d5e45edd8` — `PARTIALLY_SUPPORTED`. 瀚宇博2025年官方簡報載「**PC/NB**」「AI advanced NB, Switch」等產品線（「PCB」13次、「PC」20次、「NB」5次），支持其 PC／NB 用 PCB 業務；惟「全球最大」「市佔」「第一」與「華新麗華」出現次數均為0，其「全球最大 Notebook PCB 供應商」「PC/NB 全球市佔第一」「華新麗華集團旗下」均未獲支持。
- `6153:objective_ranking_or_market_share:aac6a63b7c86262a` — `UNKNOWN_AFTER_RESEARCH`. 嘉聯益2022年官方簡報中「客戶」出現3次（均為通稱），「Apple」「蘋果」「廣達」「仁寶」「非蘋」與「最大」出現次數均為0，未具名任何客戶，故其「Apple（最大且最重要的客戶）」等客戶身分未獲確立。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。UNKNOWN 追蹤清單已同步刷新至 **73 筆**。
- Author-reviewed total: **388 / 1,399**; remaining: **1,011**. Outcome counts: ACCEPTED 64, PARTIALLY_SUPPORTED 247, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 73. Next pending claim by priority: `5493:objective_ranking_or_market_share:f94ffe7b1a69c19b` (三聯).

## Author batch `author-070` — 2026-10-07

- Reviewed the next six unreviewed objective ranking/market-share claims in checkpoint order (三聯 5493, 達運 6120 ×2, 業強 6124, 瑞儀 6176 ×2). Evidence came from directly downloaded and inspected official disclosures: 三聯2024年永續報告書、達運公司文件、業強2025年法人說明會簡報、瑞儀111年度年報與2023年法人說明會簡報。
- `5493:objective_ranking_or_market_share:f94ffe7b1a69c19b` — `ACCEPTED`. 三聯2024年官方永續報告書載「三聯深耕台灣，為**國內環境監測、微振動感測技術與系統整合服務第一品牌**」，與 claim 之「為國內環境監測與微振動感測技術第一品牌」對應；報告書並載其投入天然災害量測儀器研發、開發地震預警感測器（「地震」29次、「監測」29次、「預警」15次、「水庫」3次、「橋樑」1次），對應 claim 之「提供地震預警、水庫／橋樑土木工程安全監測服務」。
- `6120:objective_ranking_or_market_share:f6aa9a39447d6971` 與 `e0d35ee261ddca36` — `PARTIALLY_SUPPORTED`. 達運公司文件載「註1：本公司**法人董事友達光電(股)公司**於114.06.11改派代表人為謝忠賢先生…」（「友達」65次），顯示友達光電為其法人董事；並載產品營收比重表含「液晶顯示器及模組代工」等（「背光模組」30次、「導光板」29次）。惟全份文件中「最大客戶」與「主要客戶」出現次數均為0（「客戶」63次均為通稱），友達之「最大客戶」地位未獲載明。
- `6124:objective_ranking_or_market_share:cd511f2d451fdacd` — `PARTIALLY_SUPPORTED`. 業強2025年官方簡報中「熱導管」3次、「熱導」4次，支持其熱導元件業務；惟「台灣最大」「全球」「市占」出現次數均為0。
- `6176:objective_ranking_or_market_share:b2f52f3fc1ef841a` 與 `4f9df07548e31112` — `PARTIALLY_SUPPORTED`. 瑞儀111年度年報載其「為**台灣第一家**專業從事背光模組(Backlight Module)研發與製造之廠商，逐（步）成為**全球背光模組廠中領導地位**」，並載服務範圍涵蓋背光模組設計、製造、組裝（「導光板」17次）；惟「全球第一」「第一大」「Apple」「最大客戶」與「一條龍」出現次數均為0，其「全球第一大」地位、「Apple 為最大客戶」與「一條龍整合能力」之表述均未獲支持。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）；UNKNOWN 追蹤清單維持 **73** 筆（本批次無新增 UNKNOWN）。
- Author-reviewed total: **394 / 1,399**; remaining: **1,005**. Outcome counts: ACCEPTED 65, PARTIALLY_SUPPORTED 252, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 73. Next pending claim by priority: `6165:objective_ranking_or_market_share:b2f8d9c3fcc1a02a` (浪凡).

## Author batch `author-071` — 2026-10-07

- Reviewed the next six unreviewed objective ranking/market-share claims in checkpoint order (浪凡 6165, 安碁 6174, 瑞儀 6176, 雷科 6207, 聚鼎 6224, 鈺邦 6449). Evidence came from directly downloaded and inspected official disclosures: 浪凡股東會議事手冊、安碁2025年法人說明會簡報、瑞儀111年度年報、雷科2024年公司文件、聚鼎2022年法人說明會簡報（英文版）、鈺邦112年度年報（英文版）。本批次完成後，author 已審 **400 / 1,399（28.6%）**。
- `6165:objective_ranking_or_market_share:b2f8d9c3fcc1a02a` — `PARTIALLY_SUPPORTED`. 浪凡議事手冊載「最主要為子公司旭瑞公司所帶來的**網路直播業務- 浪Live**」「**以直播事業為核心**」（「直播」22次）；惟「第一家」與「AI」出現次數均為0。
- `6174:objective_ranking_or_market_share:d7e2f404f69ba714` — `PARTIALLY_SUPPORTED`. 安碁2025年官方簡報載地區別銷售比例台灣22%、美國24%、大陸36%、歐洲15%、其他3%，支持「銷售遍及兩岸、歐美」；惟其產品別分析係依產品型態（**OSC & XTAL** 銷售金額佔比）而非終端應用別，「車用」「工業控制」「網通」與「五成」出現次數均為0。
- `6176:objective_ranking_or_market_share:98d2560ecfdbae12` — `UNKNOWN_AFTER_RESEARCH`. 瑞儀111年度年報中「Apple」與「最大客戶」出現次數均為0，未具名任何客戶，依具名客戶身分規則結為 UNKNOWN。
- `6207:objective_ranking_or_market_share:5b5191cdf2afd95c` — `PARTIALLY_SUPPORTED`. 雷科2024年官方文件載其業務含「雷射精密加工、**雷射修整機**製造加工及銷售、測試探針卡設計及銷售」；惟「60%」出現4次，上下文分別為「SMT 設備、被動元件產業生產設備等佔約**60%以上**」之**產品別營收占比**、持股比例（49.60%）與赴大陸投資限額，**並非該公司於雷射修整機之全球市占率**；「市佔」僅1次且為泛用語。
- `6224:objective_ranking_or_market_share:163934390430b572` — `PARTIALLY_SUPPORTED`. 聚鼎2022年官方簡報「大事記」載「1998 SMD Mass Production for **ASUS customer**」與「2014 Design-Win the **Top 3 global cell phone company**」；惟「Littelfuse」「shareholder」與「largest」出現次數均為0，未載其股東結構或最大代工客戶。
- `6449:objective_ranking_or_market_share:4466a7526d81896b` — `ACCEPTED`. 鈺邦112年度年報「Market share」段載「Currently, it has been the **largest supplier of coiled solid-state capacitors in the world with a leading position in the solid-state capacitor industry**」，對應 claim 之全球地位；年報主要股東表列「**TAI-TECH ADVANCED ELECTRONICS CO., LTD. 28.11%**」為最大股東，並註記「INPAQ Technology 原為本公司法人董事，自2023年4月13日起解任」，關係人交易段落列有「**Walsin Technology**」（華新科技），與 claim 之集團歸屬相符。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。UNKNOWN 追蹤清單已同步刷新至 **74 筆**。
- Author-reviewed total: **400 / 1,399**; remaining: **999**. Outcome counts: ACCEPTED 66, PARTIALLY_SUPPORTED 256, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 74. Next pending claim by priority: `6196:objective_ranking_or_market_share:c712b83c2829b483` (帆宣).

## Author batch `author-072` — 2026-10-08

- Reviewed the next five unreviewed objective ranking/market-share claims in checkpoint order (帆宣 6196, 尼得科超眾 6230, 華豫寧 6474, ticker 6512 ×2). Evidence came from directly downloaded and inspected official disclosures: 帆宣公司文件、尼得科超眾2025年上半年度法人說明會簡報、華豫寧2025年法人說明會簡報，另下載南俊國際（6584）官方簡報作為 ticker 身分比對。
- `6196:objective_ranking_or_market_share:c712b83c2829b483` — `PARTIALLY_SUPPORTED`. 帆宣官方文件載「**榮獲台積電15廠A/B**」「榮獲**台積電**2022年【**優良承攬商**】」與「2022 **日月光**（…）」（「半導體」33次、「顯示器」7次、「客戶」80次），支持其工程承攬業務涵蓋半導體與顯示器產業；惟「最大客戶」與「鴻海」出現次數均為0。
- `6230:objective_ranking_or_market_share:d3934452c5eec0ad` — `PARTIALLY_SUPPORTED`. 尼得科超眾2025年官方簡報載「主營業務: **散熱模組、散熱片、熱導管及微均熱板**」與產品「覆蓋10W NB至10kW AI Server」；惟「市佔」「45%」與「霸主」出現次數均為0，且「30%」唯一命中為「Nidec 持股達**86.30%**（2025年7月）」之持股比例，非市場占有率。
- `6474:objective_ranking_or_market_share:e1e8b7bc5f77c89b` — `PARTIALLY_SUPPORTED`. 華豫寧2025年官方簡報載「2019**成立WAFERLOCK子公司**暨併購利滙」、電子鎖產品線（歐規／日規／美規）與「智慧建築系統整合…**門禁系統**」（「門鎖」4次、「門禁」4次、「IoT」8次）；惟「市佔率超過五成」之「50%」唯一命中為銷售漏斗示意圖之一階段（「10% -> 30% -> **50%** -> 70~90% -> 100%」），「IoT 營收占比約25%」與「外銷歐洲比例」亦未見對應敘述。
- `6512:objective_ranking_or_market_share:52216fcbf3c5cfac` 與 `2876e98579307c73` — `UNKNOWN_AFTER_RESEARCH`. **本批次發現 ticker-公司身分不符情形**：兩筆 claim 所述業務主體為「**南俊**」（伺服器滑軌、成為美超微主力滑軌供應商、NVIDIA GB200/GB300 推薦供應商資格），惟查得之官方文件主體為**南俊國際股份有限公司（股票代號 6584）**（簡報首頁載「南俊國際股份有限公司（6584TW）」「**全球鋼珠導軌的專家** THE GLOBAL BALL BEARING SLIDE PROFESSIONAL」，可自 /nas/STR/**6584**20260511M001.pdf 下載）；而該兩筆 claim 之隊列紀錄為 ticker **6512**、公司名「啟發電」、路徑 `Pilot_Reports/Electronic Components/6512_啟發電.md`。因 claim 內容與其掛載之 ticker 不一致，本批次未能就 6512 取得對應證據，故結為 UNKNOWN_AFTER_RESEARCH，並依專案規則第2條將身分不符情形記錄於 evidence.note 供 author 端覆核。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。
- Author-reviewed total: **405 / 1,399**; remaining: **994**. Outcome counts: ACCEPTED 66, PARTIALLY_SUPPORTED 259, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 76. Next pending claim by priority: `6538:objective_ranking_or_market_share:84142ea1fb4928c3` (倉和).

## Author batch `author-073` — 2026-10-08

- Reviewed the next six unreviewed objective ranking/market-share claims in checkpoint order (倉和 6538, 和詮 6673 ×2, 旭暉應材 6698, 昇佳電子 6732, 永道-KY 6863). Evidence came from directly downloaded and inspected official disclosures: 倉和111年度年報、旭暉應材年報、昇佳電子法人說明會簡報、永道-KY公開資訊文件。
- `6538:objective_ranking_or_market_share:84142ea1fb4928c3` — `PARTIALLY_SUPPORTED`. 倉和111年度年報載「於2022年致力持續優化**CF 系列**產品**3D 無網結網版**」「應用**3D 無網結、高網目數、極細線化**的網版製程技術」與「深耕**太陽能**網版印刷領域多年」（「網版」56次、「無網結」9次、「太陽能」24次、「銀漿」6次、「PI」6次）；惟「全球唯一」「獨家」「首家」出現次數均為0。
- `6673:objective_ranking_or_market_share:e881d11eadac0b96` 與 `5837eee3cc7c02e7` — `UNKNOWN_AFTER_RESEARCH`. 和詮科技官方年報端點回應 **HTTP 404**，未取得可檢視之官方文件，其「全球最大特殊投影抗光幕材料製造商」與「業界唯一…光遮蔽率80%以上、120吋」等敘述均未獲確立。
- `6698:objective_ranking_or_market_share:e3db967c354ef4c5` — `PARTIALLY_SUPPORTED`. 旭暉年報「產業上、中、下游之關聯性－《金屬遮罩》」載「本集團主要產品之一，為 **AMOLED 面板關鍵製程用精密金屬遮罩**」，支持其金屬遮罩業務。惟二項陳述未獲支持或須更正：(1)「在中國大陸市佔率約 **40%**」——年報中該40%係指「展望2021年 **AMOLED 智慧型手機應用的比重**將可攀升至40%左右」，**為產業應用比重而非該公司市占率**，年報就旭暉自身市占率僅載「預期…逐年提高」而未載數字；(2)「尚未打入京東方與華星光電」——年報之產業關聯表將「中國京東方、中國和輝、中國華星、中國維信諾」併列為**下游（OLED面板）代表公司**（同表並列韓國LGD、韓國三星、中國天馬、友達），未區分是否已為其客戶，故該敘述無法以該表確認或否證。
- `6732:objective_ranking_or_market_share:60bfec13a29befba` — `PARTIALLY_SUPPORTED`. 昇佳電子官方簡報中「環境光」7次、「ALS」2次、「PS」2次、「近接」1次，支持其光學感測器業務；惟「非蘋」「Android」「市佔」與「色溫」「閃爍」出現次數均為0。
- `6863:objective_ranking_or_market_share:208c742c8478bb55` — `PARTIALLY_SUPPORTED`. 永道-KY公開資訊文件中「**RFID**」9次、「**永豐餘**」3次，支持其 RFID 電子標籤業務與集團關聯；惟「全球第二」「亞洲最大」「市佔」「25%」與「50億」出現次數均為0。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。UNKNOWN 追蹤清單已同步刷新至 **78 筆**。
- Author-reviewed total: **411 / 1,399**; remaining: **988**. Outcome counts: ACCEPTED 66, PARTIALLY_SUPPORTED 263, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 78. Next pending claim by priority: `6962:objective_ranking_or_market_share:8a6e457c9cf41c59` (奕力-KY).

## Author batch `author-074` — 2026-10-08

- Reviewed the next five unreviewed objective ranking/market-share claims in checkpoint order (奕力-KY 6962, 台虹 8039, 南電 8046, 元太 8069 ×2). Evidence came from directly downloaded and inspected official disclosures: 奕力-KY 2024與2026年法人說明會簡報、台虹114年股東會相關文件、南電113年度年報、元太公司文件。
- `6962:objective_ranking_or_market_share:8a6e457c9cf41c59` — `PARTIALLY_SUPPORTED`. 奕力2024年與2026年官方簡報均載其產品線含「**車用TDDI**」「**工控TDDI**」「**平板TDDI**」「**穿戴TDDI**」（2024年「TDDI」19次；2026年9次），支持其 TDDI 產品業務；惟「全球 TDDI **市佔率排名第二**」與「由原奕力科技與**聯詠**子公司觸控 IC 部門整合而成」均未獲支持（「市佔」「第二」「聯詠」出現次數均為0）。
- `8039:objective_ranking_or_market_share:0708d00d3969d082` — `PARTIALLY_SUPPORTED`. 本批次自發行人官方網域取得並檢視者為其114年股東會相關文件（非完整年報），其中「銅箔」出現1次；「全球前三大」「大中華」「FCCL」與「市佔」出現次數均為0（「第一」24次多為「第一季」等非排名用語），故其 FCCL 市場地位未獲敘述。
- `8046:objective_ranking_or_market_share:b6b6b05ab39bd5c8` — `PARTIALLY_SUPPORTED`. 南電113年度年報載「積極切入**AI 伺服器**供應鏈」與多項「**ABF載板**」擴建案（樹林廠、昆山廠），並載應用含「（伺）服器晶片、**高效能運算晶片(HPC)**、5G 交換器晶片」及「（自行開發）**ASIC**」（「載板」67次、「ABF」16次、「ASIC」2次、「HPC」1次）；惟「高階 **GPU、CPU**」未獲支持（兩者出現次數均為0）。
- `8069:objective_ranking_or_market_share:2ea0db4264ee1d7d` — `PARTIALLY_SUPPORTED`. 元太官方文件載「**元太科技在全球擁有極高的市占率，全球主要電子閱讀器品牌供應商都使用元太科技生產的 EPD**」（「電子紙」360次、「專利」55次），支持其電子紙領導地位；惟「市占率**超過九成**」未獲支持（「九成」0次，「市占」僅1次且為定性描述）。
- `8069:objective_ranking_or_market_share:5f18abcc84d8634a` — `PARTIALLY_SUPPORTED`. 元太文件載其協同「振曜科技、**樂天Kobo**、天鈺科技、同泰電子、茂林光電、恆顥科技與群創光電等**電子紙生態圈夥伴**」（「Kobo」2次）；惟「**Amazon (Kindle)**」未獲支持（「Amazon」與「Kindle」均為0次），文件亦未就各品牌之市場排名作敘述。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）；UNKNOWN 追蹤清單維持 **78 筆**（本批次無新增 UNKNOWN）。
- Author-reviewed total: **416 / 1,399**; remaining: **983**. Outcome counts: ACCEPTED 66, PARTIALLY_SUPPORTED 268, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 78. Next pending claim by priority: `8074:objective_ranking_or_market_share:0d087bffe38bc6c8` (鉅橡).

## Author batch `author-075` — 2026-10-08

- Reviewed the next seven unreviewed objective ranking/market-share claims in checkpoint order (鉅橡 8074 ×2, 越峰 8121, 達方 8163 ×4). Evidence came from directly downloaded and inspected official disclosures: 鉅橡113年度年報、越峰113年度年報、達方113年度年報；三份文件均以其封面之公司名稱與股票代號確認身分。
- `8074:objective_ranking_or_market_share:0d087bffe38bc6c8` 與 `f6920c2cb74e6a31` — `PARTIALLY_SUPPORTED`. 鉅橡113年度年報載「（半）導體至下游的 PCB 相關族群。例:以**欣興**為首的 **ABF 載板**廠商，皆一直再加大台灣市（場）」，「墊板」35次、「鑽孔」14次、「蓋板」6次、「ABF」3次，支持其 PCB 鑽孔製程用墊板／蓋板材料業務及與欣興、景碩之往來；惟「**唯一**」與「**南電**」出現次數均為0。
- `8121:objective_ranking_or_market_share:24f39c0d0754d000` — `PARTIALLY_SUPPORTED`. 越峰113年度年報載「一一三年度**碳化矽粉**銷售量與金額分別為 **125 噸**與新台幣 **621,123**（仟元）」（「碳化矽」39次、「SiC」19次）；惟「**長晶**」僅1次、「（台灣）**唯一**」與「**本土**」「**粉料**」出現次數均為0。
- `8163:objective_ranking_or_market_share:c5addd1ec6068c09`、`c8a87aa8bf948eee`、`d28f7bc2f49da606`、`a9244fd19563c328` — `PARTIALLY_SUPPORTED` ×4. 達方113年度年報「智能產品」段載「**筆記型及桌上型電腦鍵盤**、發光鍵盤、滑鼠、電競鍵盤、電競滑鼠、平板電腦使用之可攜（式鍵盤）」（「鍵盤」45次、「明基」25次、「1997」3次），支持其鍵盤模組業務與集團歸屬；惟「**全球最大**」「全球領導」「領導廠」出現次數均為0。另須更正數字歸屬：年報中「**第一大**」1次係指「本公司董事兼大股東**佳世達科技**…佔公司20.72%之股權，為本公司**第一大股東**」，**為股東結構而非市場排名**；「市占」1次之上下文為被動元件與電動車之產業趨勢敘述。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）；UNKNOWN 追蹤清單維持 **78 筆**。
- Author-reviewed total: **423 / 1,399**; remaining: **976**. Outcome counts: ACCEPTED 66, PARTIALLY_SUPPORTED 275, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 78. Next pending claim by priority: `8215:objective_ranking_or_market_share:e396f3af21b11405` (明基材).































































