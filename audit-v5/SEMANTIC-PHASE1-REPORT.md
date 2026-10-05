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

Author-reviewed: **978 / 1,399** unique HIGH claims across batches `author-001` (8), `author-002` (1), `author-003` (1), `author-004` (2), `author-005` (1), `author-006` (1), `author-007` (1), `author-008` (1), `author-009` (1), `author-010` (1), `author-011` (2), `author-012` (1), `author-013` (3), `author-014` (2), `author-015` (2), `author-016` (3), `author-017` (6), `author-018` (7), `author-019` (8), `author-020` (8), `author-021` (10), `author-022` (8), `author-023` (7), `author-024` (9), `author-025` (7), `author-026` (8), `author-027` (8), `author-028` (8), `author-029` (8), `author-030` (8), `author-031` (7), `author-032` (8), `author-033` (8), `author-034` (8), `author-035` (8), `author-036` (9), `author-037` (7), `author-038` (8), `author-039` (6), `author-040` (8), `author-041` (8), `author-042` (7), `author-043` (8), `author-044` (4), `author-045` (4), `author-046` (5), `author-047` (5), `author-048` (6), `author-049` (4), `author-050` (8), `author-051` (4), `author-052` (8), `author-053` (4), `author-054` (8), `author-055` (4), `author-056` (7), `author-057` (5), `author-058` (7), `author-059` (7), `author-060` (7), `author-061` (3), `author-062` (5), `author-063` (6), `author-064` (6), `author-065` (6), `author-066` (7), `author-067` (7), `author-068` (6), `author-069` (4), `author-070` (6), `author-071` (6), `author-072` (5), `author-073` (6), `author-074` (5), `author-075` (7), `author-076` (5), `author-077` (7), `author-078` (6), `author-079` (7), `author-080` (6), `author-081` (7), `author-082` (7), `author-083` (8), `author-084` (6), `author-085` (8), `author-086` (8), `author-087` (6), `author-088` (8), `author-089` (8), `author-090` (7), `author-091` (8), `author-092` (5), `author-093` (8), `author-094` (8), `author-095` (8), `author-096` (8), `author-097` (6), `author-098` (5), `author-099` (8), `author-100` (7), `author-101` (7), `author-102` (6), `author-103` (7), `author-104` (8), `author-105` (8), `author-106` (5), `author-107` (8), `author-108` (8), `author-109` (4), `author-110` (4), `author-111` (5), `author-112` (8), `author-113` (8), `author-114` (8), `author-115` (5), `author-116` (3), `author-117` (5), `author-118` (5), `author-119` (6), `author-120` (8), `author-121` (8), `author-122` (4), `author-123` (8), `author-124` (5), `author-125` (5), `author-126` (3), `author-127` (5), `author-128` (4), `author-129` (4), `author-130` (4), `author-131` (4), `author-132` (5), `author-133` (3), `author-134` (5), `author-135` (3), `author-136` (5), `author-137` (3), `author-138` (4), `author-139` (4), `author-140` (6), `author-141` (4), `author-142` (4), `author-143` (4), `author-144` (5), `author-145` (3), `author-146` (5), `author-147` (5), `author-148` (3), `author-149` (3), `author-150` (4), `author-151` (3), `author-152` (3), `author-153` (3), `author-154` (3), `author-155` (4), `author-156` (2), `author-157` (4), `author-158` (2), `author-159` (4), `author-160` (2), `author-161` (4), `author-162` (4), `author-163` (2), `author-164` (5), `author-165` (2), `author-166` (4), `author-167` (3), `author-168` (4), `author-169` (5), `author-170` (5), `author-171` (6), `author-172` (4), `author-173` (7), `author-174` (2), `author-175` (2), `author-176` (6), `author-177` (2), `author-178` (5), `author-179` (2), `author-180` (5), `author-181` (4), `author-182` (4), and `author-183` (5).

- ACCEPTED by author: 94
- PARTIALLY_SUPPORTED: 638
- UNSUPPORTED: 1
- SOURCE_UNAVAILABLE: 3
- Other allowed author decisions: 242
- Remaining author queue: 421

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

## Author batch `author-076` — 2026-10-08

- Reviewed the next five unreviewed objective ranking/market-share claims in checkpoint order (明基材 8215, 華宏 8240, 歐買尬／綠界科技 3687, 智冠 5478 ×2). Evidence came from directly downloaded and inspected official disclosures: 明基材2022年報、華宏2021年報、綠界科技115年度年報、智冠集團營運報告。
- `8215:objective_ranking_or_market_share:e396f3af21b11405` — `PARTIALLY_SUPPORTED`. 明基材2022年報載其合資設立「達尼特材料科技(蕪湖)有限公司，從事**鋰電池用隔離膜**產品製造銷售」，並載「隔離膜多方應用前景可期」與鋰電池技術路線（「隔離膜」6次、「捲對捲」2次、「塗佈」3次、「電動車」8次、「儲能」6次）；惟「為**台灣唯一**鋰電池隔離膜製造商」未獲支持（「台灣唯一」0次）。
- `8240:objective_ranking_or_market_share:ad10cdcb6cd24cc2` — `ACCEPTED`. 華宏2021年報載「（光）模組**光學膜片最大專業製造裁切廠**，各項產品皆具有高的市場佔有率」，與 claim 之「為背光模組光學膜片最大專業裁切廠」對應；所列產品「偏光板、擴散膜、增亮膜、導光板、**量子點**膜、觸控面板**防爆膜**」亦逐項出現於年報（「量子點」7次、「防爆膜」6次、「觸控面板」4次、「擴散膜」15次、「增亮膜」9次、「導光板」6次）。
- `3687:objective_ranking_or_market_share:cae577f91575490d` — `PARTIALLY_SUPPORTED`. 綠界科技115年度年報載「（憑藉）卓越的營運韌性，**維持第三方支付市場龍頭地位**」（「第三方支付」26次、「綠界」54次）；惟「市佔率極高」未獲量化或定性支持（「市佔」2次分別為「將面臨市佔流失風（險）」與「拓展市佔率」），「服務**數十萬**中小型電商賣家」（「數十萬」0次）與「競爭對手為藍新科技、LINE Pay」（兩者均0次）亦未獲支持。
- `5478:objective_ranking_or_market_share:ce91f88d8082e000` 與 `66491f95bfe4f0d6` — `PARTIALLY_SUPPORTED`. 智冠2025年集團營運報告載「遊戲通路領導品牌：智冠全方位整合行銷 ★**台港澳市佔率最高 60%** ★玩家會員人數逾 735萬 ★國內外據點突破 5萬家 ★**合作產品 2,400+** ★合作廠商逾 700家」，並另載「**市佔第一**」，支持其市占領先與 60% 之數字；惟**官方所述市占之地理範圍為「台港澳」，claim 表述為「台灣」**，兩者範圍不同；「全台四大便利商店」與「東南亞」等通路敘述亦未見於簡報。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）；UNKNOWN 追蹤清單維持 **78 筆**。
- Author-reviewed total: **428 / 1,399**; remaining: **971**. Outcome counts: ACCEPTED 67, PARTIALLY_SUPPORTED 279, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 78. Next pending claim by priority: `6473:objective_ranking_or_market_share:b29d00af5856229f` (美賣).

## Author batch `author-077` — 2026-10-08

- Reviewed the next seven unreviewed objective ranking/market-share claims in checkpoint order (美賣 6473, 華電 1603 ×2, 聯強 2347, 華立 3010, 威健 3033 ×2). Evidence came from directly downloaded and inspected official disclosures: 華電2025年法人說明會簡報、聯強2024年度年報、華立111年度年報、威健2021年永續報告書。
- `6473:objective_ranking_or_market_share:b29d00af5856229f` — `UNKNOWN_AFTER_RESEARCH`. 美賣（6473，興櫃公司）未查得可下載之年報或法人說明會簡報端點，搜尋所得僅為其官網平台介紹（「網紅媒合AI選物平台」）與證券櫃檯買賣中心之公司基本資料頁；因未取得可檢視之發行人正式文件，其社群電商市占拓展敘述未獲確立。
- `1603:objective_ranking_or_market_share:12171e5a5dfe2650` 與 `fe4b64c156172c36` — `UNKNOWN_AFTER_RESEARCH`. 華電2025年官方簡報（英文版）含「Partner」與「客戶 Customer 名稱 Items」之訂單列表（如「114.02.21 台電花東供電區處 超耐熱鋼心鋁線 210mm2」），惟全份簡報中「第一銅」「華新麗華」「銅」「鋁錠」「供應」與英文「Copper」「Supplier」出現次數均為0，**未見供應商名單**，故具名供應商之 claim 依一致性規則結為 UNKNOWN。
- `2347:objective_ranking_or_market_share:8fff79b3fa219000` — `PARTIALLY_SUPPORTED`. 聯強2024年度年報載「聯強已在**亞太地區主要城市建立數十座智能化的運籌服務中心**，形成覆蓋面廣泛的運籌網絡」，並載「多品牌採購，擴大業務規模」（「品牌」12次）；惟「**亞太第一大**」與「第一大」出現次數均為0；「**440**」唯一命中為「440.4」（數值）；「**30,000**」4次之上下文均為「15,000,000元（含）～30,000,000元」等**酬金級距**，非產品項數。
- `3010:objective_ranking_or_market_share:23e0e98b40b54555` — `PARTIALLY_SUPPORTED`. 華立111年度年報載其業務涵蓋「工程塑膠及PCB相關材料及設備應用於高速傳輸伺服器、5G行動裝置及材料、AI人工智能裝置、雲端計算、AIOT、汽車影像及雷達、電子電力功率模組」（「半導體」35次、「綠能」14次、「工程塑膠」5次）；惟「高科技材料通路」0次，且「最大」2次之上下文分別為「使員工工作之穩定性**最大化**」與「使員工發揮**最大**之工作潛能」，**非市場地位敘述**。
- `3033:objective_ranking_or_market_share:54d8ccbbd3d4f3e1` 與 `720516a156c7c28d` — `PARTIALLY_SUPPORTED`. 威健2021年官方永續報告書載「**威健實業股份有限公司代理之電子零組件包括例如：AMD、Amazing、Cypress、Infineon、Lattice、Microchip、Molex、NXP、Si（…）**」（「Microchip」8次、「AMD」7次、「Vishay」6次、「NXP」5次），所列 Infineon、NXP、Microchip、Vishay 皆可對應；惟「**最大代理線**」未獲支持（「最大」5次之上下文分別為「最大銷售冠軍代理夥伴獎」等獎項與「最大貢獻度」「最大化」等泛用語），「CPU」與「GPU」出現次數亦為0。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。UNKNOWN 追蹤清單已同步刷新至 **81 筆**。
- Author-reviewed total: **435 / 1,399**; remaining: **964**. Outcome counts: ACCEPTED 67, PARTIALLY_SUPPORTED 283, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 81. Next pending claim by priority: `2450:objective_ranking_or_market_share:d4c4eba514df929a` (神腦).

## Author batch `author-078` — 2026-10-08

- Reviewed the next six unreviewed objective ranking/market-share claims in checkpoint order (神腦 2450, 益登 3048 ×2, 弘憶股 3312 ×2, 大聯大 3702). Evidence came from directly downloaded and inspected official disclosures: 神腦106年度年報、弘憶110年度年報、大聯大2022年度年報。
- `2450:objective_ranking_or_market_share:d4c4eba514df929a` — `ACCEPTED`. 神腦106年度年報載「神腦國際**創立於1979年**，為**全台行動手持裝置最大通路商**」，並載「身為**全台數位滙流裝置最大之通路商**」與「（中華電信認）購，成為神腦**最大股東**」（「中華電信」16次、「1979」3次），與 claim 之「成立於1979年」「為台灣最大通訊通路代理商」「隸屬於中華電信集團」逐項對應。
- `3048:objective_ranking_or_market_share:e7578b46e213723c` 與 `144af8e9daef4625` — `UNKNOWN_AFTER_RESEARCH`. **本批次於來源身分複核中發現一項誤配**：就益登搜尋所取得之 zenitron.com.tw 端點檔案，經下載檢視後其內容為「**2023 永續報告書**」且目錄載「Chapter 1 關於**增你強**」，確認該文件**屬增你強（3028）而非益登（3048）**，故不予採用；就 ticker 3048 未取得可檢視之發行人正式文件（所檢視文件中「NVIDIA」「Jetson」「GPU」均為0次），其與 NVIDIA 之代理關係及「最大供應商」地位未獲確立。
- `3312:objective_ranking_or_market_share:ef9a168379d5a594` 與 `30b39681faeb2489` — `PARTIALLY_SUPPORTED`. 弘憶110年度年報載「**代理並銷售瑞昱半導體科技(股)公司電子零組件產品**」，並載瑞昱應用於資訊科技電子、消費性電子與**網路通訊**產業（「瑞昱」39次、「代理線」2次）；惟「**最大代理線**」與「**最大供應商**」均未獲支持（「最大」9次均為「開創最大營收」「給予客戶最大的採購效益」等泛用語），「營收佔比**逾7成**」亦未獲支持——「7成」與「營收佔比」均為0次，而「**70%**」出現2次，其上下文均為**員工福利精算假設之折現率（0.70%）**，與營收占比無關。
- `3702:objective_ranking_or_market_share:bbfe49daa140f2f0` — `PARTIALLY_SUPPORTED`. 大聯大2022年度年報載「**大聯大控股是全球第二、亞太區第一大的半導體零組件通路商**，總部位於臺（北）」（「全球第二」3次、「亞太區第一大」1次、「2005」6次）；惟 claim 之「為**全球最大**半導體零組件通路商之一」與官方明確之「**全球第二**」用語不同，且「2024年合併營收達8,806億元」無法以2022年度年報查證（「8,806」0次）。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。UNKNOWN 追蹤清單已同步刷新至 **83 筆**。
- Author-reviewed total: **441 / 1,399**; remaining: **958**. Outcome counts: ACCEPTED 68, PARTIALLY_SUPPORTED 286, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 83. Next pending claim by priority: `3360:objective_ranking_or_market_share:1e5c4a342b962d2f` (尚立).

## Author batch `author-079` — 2026-10-08

- Reviewed the next seven unreviewed objective ranking/market-share claims in checkpoint order (尚立 3360, 力致 3483, 大聯大 3702, 崇越 5434, 茂綸 6227, 長華 8070 ×2). Evidence came from directly downloaded and inspected official disclosures: 力致2025年法人說明會簡報、大聯大2022年度年報、崇越113年度年報、茂綸股東會年報、長華2018年度年報；尚立部分則採第三人於交易所申報之公開文件。
- `3360:objective_ranking_or_market_share:1e5c4a342b962d2f` — `PARTIALLY_SUPPORTED`. 本批次未取得尚立自身可檢視之官方文件，惟深圳證券交易所公開文件（影石創新申報文件）載「報告期內，發行人向**尚立（香港）股份有限公司**採購的 **CMOS 圖像傳感器**價格係由影石創新與**日本索尼（Sony）**根據需求量協商確定…並直接與日本索尼（Sony）的**代理（商）**（…）」，支持尚立處於 Sony CIS 之供應／代理環節；惟「最大供應商」未獲支持。（註記：本件為第三人於交易所申報之公開文件，非尚立自身揭露。）
- `3483:objective_ranking_or_market_share:eb582bc6e017b55f` — `ACCEPTED`. 力致2025年官方簡報「我們的優勢」頁明載「**筆電風扇市佔率最高**」，與 claim 之「在筆記型電腦 (NB) 風扇市場擁有極高市佔率」對應（官方用語強度高於 claim）；簡報並載其產品為「風扇 Cooling Fan」及「結合風扇、熱管、均溫板、水冷」之散熱解決方案（「散熱」10次、「風扇」7次）。
- `3702:objective_ranking_or_market_share:c5f8ff6dd3f3b9ef` — `PARTIALLY_SUPPORTED`. 大聯大2022年度年報中「世平」出現35次、「WPI」18次，支持世平興業為其集團之半導體通路事業；惟「最大子公司」出現次數為0。
- `5434:objective_ranking_or_market_share:a062e5f5b5b17bbb` — `PARTIALLY_SUPPORTED`. 崇越113年度年報中「光阻」15次、「矽晶圓」14次、「先進製程」12次，支持其供應先進製程關鍵材料；惟「最大客戶」出現次數為0。
- `6227:objective_ranking_or_market_share:43389475739d47d9` — `PARTIALLY_SUPPORTED`. 茂綸股東會年報載其與 **Macnica** 集團之關係（22次）與代理業務（106次），並見「NVIDIA」4次、「Renesas」4次、「Intel」1次；惟「日本第一大」出現次數為0。
- `8070:objective_ranking_or_market_share:db178e56e65db8b1` 與 `ab0adc7ddd6d83f3` — `PARTIALLY_SUPPORTED`. 長華2018年度年報載其「整併日商**住友**導線架業務…成為**全球第三大導線架廠**」，並見「封膠」19次、「EMC」2次，支持其導線架與封膠樹脂業務。惟**多項數字經查證後全數須更正**：「**51%**」唯一命中為**員工學歷分布之高中比率**；「**28%**」唯一命中為財務結構表「長期資金佔不動產、廠房及設備比率 **8,028%**」之子字串；「**33%**」唯一命中為「瑞康投資(股)公司(**4.33%**)」之持股比例；「**67%**」3次分別為**董事實際出席率67%**與法人股東持股比例；「市佔」5次之上下文均為**台灣半導體產業整體**（如「台灣晶圓代工產值全球排名第一，市佔率約七成」）。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）；UNKNOWN 追蹤清單維持 **83 筆**。
- Author-reviewed total: **448 / 1,399**; remaining: **951**. Outcome counts: ACCEPTED 69, PARTIALLY_SUPPORTED 292, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 83. Next pending claim by priority: `6776:objective_ranking_or_market_share:59f0a1faacffbf5e` (展碁國際).

## Author batch `author-080` — 2026-10-08

- Reviewed the next six unreviewed objective ranking/market-share claims in checkpoint order (展碁國際 6776, 長華 8070, 世紀風電 2072, 洋基工程 6691 ×2, 泰創工程 6750). Evidence came from directly downloaded and inspected official disclosures: 展碁國際公司文件、長華2018年度年報、世紀鋼2025年法人說明會簡報、洋基工程2026年法人說明會簡報。
- `6776:objective_ranking_or_market_share:59f0a1faacffbf5e` — `PARTIALLY_SUPPORTED`. 展碁文件載「於2020年9月取得**代理銷售 Adobe 產品**」「**代理 Adobe 全系列產品**」並見「Microsoft」1次、「軟體」50次、「授權」10次，支持其商用軟體授權分銷業務；惟「為**台灣最大軟體通路商**」未獲支持——全份文件中「最大」8次之上下文包含「**LG 在台最大品牌代理商**」「仍是新冠狀病毒影響經濟景氣**最大**變數」等。
- `8070:objective_ranking_or_market_share:13e7c6a3959a27bd` — `PARTIALLY_SUPPORTED`. 本 claim 為長華同一事實之條目表述（「住友培科封膠樹脂代理，國內市佔67%」）。其代理封膠樹脂業務獲年報支持（「住友」7次、「封膠」19次）；惟「67%」3次之上下文分別為**董事實際出席率67%**與法人股東持股比例（如95.67%），**非國內市占率**。
- `2072:objective_ranking_or_market_share:033b7b8eb52cfe3b` — `PARTIALLY_SUPPORTED`. 世紀鋼2025年官方簡報載「**世紀風電**」「**世紀風電-台北港**」「**水下基礎**基樁Section製造」「水下基礎腿管製造」與「得天獨厚條件：專用深水港、廣袤製造及儲存區因應水下基礎大型化」（「水下基礎」17次、「世紀風電」4次），支持世紀風電為集團水下基礎業務主體；惟「為**台灣本土製造量能最大**之水下基礎供應商」未獲支持（「本土」與「量能最大」均為0次）。
- `6691:objective_ranking_or_market_share:4a06f569d516bc7a` 與 `d5272625e216200f` — `UNKNOWN_AFTER_RESEARCH`. 洋基工程2026年官方簡報中「台積電」「ASML」與「最大客戶」出現次數均為0（「客戶」2次均為通稱），且「40%」2次之上下文為「**0.40%**」之財務比率而非營收占比，故具名客戶身分及客戶集中度未獲確立，依一致性規則結為 UNKNOWN。
- `6750:objective_ranking_or_market_share:40044574fe259065` — `UNKNOWN_AFTER_RESEARCH`. 泰創工程搜尋所得均為其官方網站之服務與工程案例頁，未查得可下載之年報或法人說明會簡報端點，故其與晶碩光學之越南無塵室工程關係未獲確立。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。UNKNOWN 追蹤清單已同步刷新至 **86 筆**。
- Author-reviewed total: **454 / 1,399**; remaining: **945**. Outcome counts: ACCEPTED 69, PARTIALLY_SUPPORTED 295, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 86. Next pending claim by priority: `6873:objective_ranking_or_market_share:8e8bea538366ff4d` (泓德能源).

## Author batch `author-081` — 2026-10-08

- Reviewed the next seven unreviewed objective ranking/market-share claims in checkpoint order (泓德能源 6873, 巨漢 6903, 台汽電 8926 ×2, 中鼎 9933, 潤泰新 9945 ×2). Evidence came from directly downloaded and inspected official disclosures: 泓德能源2025年法人說明會簡報、巨漢2025年法人說明會簡報、台汽電2024年法人說明會簡報、中鼎111年度年報、潤泰新公司文件。
- `6873:objective_ranking_or_market_share:8e8bea538366ff4d` — `PARTIALLY_SUPPORTED`. 泓德2025年官方簡報載「（每）年轉供約 **6,700 萬度綠電**給**台灣大哥大**」與「成為**台灣大哥大最大綠電供應**（商）」（「星星電力」10次、「綠電」47次、「轉供」24次），具體轉供事實與客戶關係獲支持；惟「為台灣綠電**市佔率極高**之售電業者」未獲支持（「市佔」0次），「**自2021年起**」之起始年度亦未見於簡報。
- `6903:objective_ranking_or_market_share:d9e643e450e273d5` — `PARTIALLY_SUPPORTED`. 巨漢2025年官方簡報中「**無塵室**」出現5次，支持其無塵室系統工程業務；惟「**台積電**（最大客戶群）」未獲支持（「台積電」「最大客戶」「先進製程」均為0次，「客戶」8次均為通稱）。
- `8926:objective_ranking_or_market_share:374f48cdf5d509d2` 與 `edc06851f49467ab` — `PARTIALLY_SUPPORTED`. 台汽電2024年官方簡報載「（電）力三家燃氣**民營電力**（業者）」，顯示其民營電力事業；並載「**台電**公司已於11月14日公告第二次117年商轉燃氣機組電力採（購）」「承攬沃旭二期及**台電**離岸風電二期計畫陸上變電站、輸電線（工程）」（「台電」4次、「PPA」1次），顯示與台電之交易往來。惟「成立於**1992年**」「為台灣**最大**民營電力集團之一」與「台電為**最大客戶**」均未獲支持；簡報中台電之敘述並包含「**台電公司向本公司所轉投資民營電廠主張損害賠償**」之爭訟事項。
- `9933:objective_ranking_or_market_share:ae067a7c3022090f` — `PARTIALLY_SUPPORTED`. 中鼎111年度年報載「**設立日期：民國68年4月6日**」（即1979年）與「（本公司為）國內外聲譽卓著之**綜合性統包工程公司**」，「中技社」29次、「籌設」1次，支持成立年、與中技社之關聯及統包工程業務；惟「為**台灣最大**統包工程公司（以總資產及年營收計）」未獲支持（「最大統包」「國內最大」「第一大」均為0次）。**方法論註記：年報以民國年表述日期，「1979」之西元數字自然不會命中，須以「民國68」比對。**
- `9945:objective_ranking_or_market_share:0956ae2b616a5788` 與 `596c67d69f51bdc0` — `PARTIALLY_SUPPORTED`. 潤泰新官方文件載其轉投資「**南山人壽**」（12次）與「**持股比例：25%**」「註2：直接及間接持有南山人壽投資金額約200億元」，並見「**日友**（環保）」5次，支持持股與投資布局；惟「為**最大獲利來源**」未見於文件。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）；UNKNOWN 追蹤清單維持 **86 筆**。
- Author-reviewed total: **461 / 1,399**; remaining: **938**. Outcome counts: ACCEPTED 69, PARTIALLY_SUPPORTED 302, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 86. Next pending claim by priority: `6464:objective_ranking_or_market_share:7ee6bae723c03229` (台數科).

## Author batch `author-082` — 2026-10-08

- Reviewed the next seven unreviewed objective ranking/market-share claims in checkpoint order (台數科 6464, 必應 6625, 愛爾達-創 8487, 大武山 6952 ×2, 超秦 8345 ×2). Evidence came from directly downloaded and inspected official disclosures: 台數科公司文件、必應111年度年報、愛爾達官方公司文件、大武山114年度年報、超秦114年度營業報告書。
- `6464:objective_ranking_or_market_share:7ee6bae723c03229` — `PARTIALLY_SUPPORTED`. 台數科官方文件載其「為台灣地區**有線電視多系統經營者（Multiple System Operator, MSO）**，主要係提供有線電視節目播送、安裝、廣告、頻道出（租）及付費頻道等有線電視相關服務」（「有線電視」9次、「MSO」1次、「多系統」1次）；惟「為台灣**中部最大**的有線電視多系統營運商」未獲支持（「中部最大」0次），「服務區域涵蓋苗栗、台中、南投、彰化、雲林及嘉義等縣市，約 **30 萬家庭訂戶**」亦未獲支持（「30萬」「訂戶」均0次）。
- `6625:objective_ranking_or_market_share:2ffa2be8731ab449` — `UNKNOWN_AFTER_RESEARCH`. 必應111年度年報之 PDF **文字層呈現亂碼**（第1頁顯示「΋΋΋ԃࡋ」「Ϧ໒ၗૻ」等非可讀字元，與台光電2023年報、上洋114年報同型之檢索限制），無法判讀其業務規模與與相信音樂之沿革，故以 UNKNOWN 結案。
- `8487:objective_ranking_or_market_share:14898f3649f7c437` — `ACCEPTED`. 愛爾達官方文件載「**以「體育轉播」為核心的新媒體**」，並在其「愛爾達創新經營模式」頁標示「**全台第一家**」，另載「打造**台灣No.1 運動轉播大平台**」與「轉播9屆奧運、4屆世足，自營6+10個頻道」（「體育」20次、「轉播」17次、「新媒體」8次），與 claim 之核心陳述對應。
- `6952:objective_ranking_or_market_share:ea612b92d7bf70a2` 與 `9f37dbda4677cd61` — `PARTIALLY_SUPPORTED`. 大武山114年度年報中「**大成**」與「**卜蜂**」各出現1次（「蛋」384次），顯示同業被提及；惟「市占」2次之上下文均為該公司自身之目標敘述（「擴大市占率」「提高洗選鮮蛋市占率」），**未載大成或卜蜂之市占率數字**，「約10%」與「約5%」未獲支持（「10%」11次、「5%」43次之上下文為財務比率或持股比例等）。
- `8345:objective_ranking_or_market_share:c3e3bf688a893fdd` 與 `f78f0cd9a0168655` — `PARTIALLY_SUPPORTED`. 超秦114年度營業報告書見「**屠宰**」2次並載其面臨「國內產量大增而進口雞肉不減的市場供需失衡」，支持其畜產加工業務；惟「為**北台灣最大**家禽電宰場」未獲支持（「北台灣」「家禽」「電宰」「最大（市場地位用語）」均為0次），「創立於1985年」（「1985」「74年」0次）與「2025年6月登錄興櫃」（「興櫃」1次但未載日期）亦未獲支持。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。UNKNOWN 追蹤清單已同步刷新至 **87 筆**。
- Author-reviewed total: **468 / 1,399**; remaining: **931**. Outcome counts: ACCEPTED 70, PARTIALLY_SUPPORTED 307, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 87. Next pending claim by priority: `2885:objective_ranking_or_market_share:3f642a85d15abc7f` (元大金).

## Author batch `author-083` — 2026-10-08

- Reviewed the next eight unreviewed objective ranking/market-share claims in checkpoint order (元大金 2885 ×2, 勝悅-KY 1340, 志強-KY 6768, 寶成 9904, 豐泰 9910 ×3). Evidence came from directly downloaded and inspected official disclosures: 元大金114年度股東常會議事錄與法人說明會簡報、勝悅公司文件、志強-KY 2022永續報告書、寶成2017年企業社會責任報告、豐泰2023永續報告書。
- `2885:objective_ranking_or_market_share:3f642a85d15abc7f` 與 `34fa1b47f82e8a61` — `PARTIALLY_SUPPORTED`. 元大金股東常會議事錄載「以股份轉換方式將**元大證券投資信託**股份有限公司納為百分之百持股子公司」（「元大證券」3次、「證券」38次），MOPS 法說會簡報「期貨」3次，支持其證券核心事業之集團架構。惟本批次實際下載之兩份文件中「**市占**」「**13.83**」「**146**」「**148**」「**龍頭**」「**選擇權**」出現次數**均為0**，故「元大證券為台灣證券業龍頭、經紀市占率約13.5%、全台146家分公司」與「元大期貨國內期貨選擇權市占率第一」未獲確立。**註記：搜尋結果摘要曾顯示含「114年經紀業務累計市占率13.83%…站穩業界龍頭地位」之語句並指向同一端點，惟該內容未出現於本批次實際下載之檔案中，依證據政策不得採用。**
- `1340:objective_ranking_or_market_share:aa0e110f4fff1178` — `PARTIALLY_SUPPORTED`. 勝悅官方文件載「3. 最近兩年度**鞋底**及 **EVO** 顆粒銷售額及營收占比」（「EVO」5次、「雙色」6次、「鞋底」15次）；惟「以**獨家**研發的 EVO 材料聞名」與「曾為**中國最大**雙色鞋底生產企業」未獲支持（「獨家」「中國最大」均為0次）。
- `6768:objective_ranking_or_market_share:e263c027dd77e13c` — `PARTIALLY_SUPPORTED`. 志強-KY 2022年永續報告書載其「為 **Nike、Adidas、PUMA、ASICS** 等知名品牌代工，為**全球最大的足球鞋供應商**」（「足球鞋」22次、「NIKE」9次、「代工」5次），其地位敘述強度高於 claim；惟「在全球足球鞋代工市場拿下約**兩成市佔率**」未獲支持（「市佔」「兩成」均為0次）。
- `9904:objective_ranking_or_market_share:675f224ad21d1b3c` — `ACCEPTED`. 寶成2017年企業社會責任報告載「**寶成工業股份有限公司成立於 1969年9月**，全球營運總部位於臺灣臺中市西屯區臺灣大道四段600號」，並載集團成績單「**全球最大製鞋集團**」「2017生產 324.6百萬雙鞋」「2017 **全球市佔率(以批發價格計)** 約佔全球運動鞋及休閒鞋市場批發價格計算之 **20%**」，與 claim 之「成立於1969年」「總部位於台灣台中」「為全球最大的品牌運動鞋與休閒鞋製造商」逐項對應。
- `9910:objective_ranking_or_market_share:24bbf5f32a0bcc3a`、`da42301dd92043d2`、`e7538ca8506bbc46` — `PARTIALLY_SUPPORTED` ×3. 豐泰2023年永續報告書載「豐泰企業成立於1971年…為主要客戶 **Nike 最資深之製鞋合作夥伴**」，支持其為 Nike 核心製鞋夥伴；惟「六分之一」「**氣墊**」「**Air**」「**研發中心**」「**85%**」之出現次數均為0（「1992」1次係出現於官網導覽選單文字），故「佔 Nike 全球銷售量約六分之一」「唯一授權氣墊 (Air Max) 生產工廠」「1992年共同成立亞洲第一個製鞋研發中心」「Nike 佔營收約85%~90%」均未獲支持。**註記：該永續報告書之文字擷取僅2,388字元，內容多為官網導覽選單，實質敘述有限。**
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）；UNKNOWN 追蹤清單維持 **87 筆**。
- Author-reviewed total: **476 / 1,399**; remaining: **923**. Outcome counts: ACCEPTED 71, PARTIALLY_SUPPORTED 314, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 87. Next pending claim by priority: `9910:objective_ranking_or_market_share:d6ba6478547062ad` (豐泰).

## Author batch `author-084` — 2026-10-08

- Reviewed the next six unreviewed objective ranking/market-share claims in checkpoint order (豐泰 9910, 伸興 1558 ×4, 艾美特-KY 1626). Evidence came from directly downloaded and inspected official disclosures: 豐泰永續報告書、伸興2022年度年報、艾美特-KY 2023年法人說明會簡報。
- `9910:objective_ranking_or_market_share:d6ba6478547062ad` — `PARTIALLY_SUPPORTED`. 豐泰官方永續報告書載其「為主要客戶 **Nike 最資深之製鞋合作夥伴**」，支持雙方長期代工關係；惟「佔營收約 **85%~90%**」（「85%」0次）、「為其**全球六分之一**產能供應商」（「六分之一」0次）與「**唯一**授權氣墊工廠」（「氣墊」0次）均未獲支持。**註記：該公司官網另一路徑之 2018CSR.pdf 經下載後檔案大小與內容完全相同（同為126,337 bytes、同為2,388字元擷取），顯示該路徑並非供應2018年度文件。**
- `1558:objective_ranking_or_market_share:87cc034abe16d845`、`c93aec6e76435d1b`、`01444720c98b05b0`、`0fd3b72d834f9729` — `PARTIALLY_SUPPORTED` ×4. 伸興2022年度年報載其同業／客戶群含「**SVP 集團**、日本JANOME、日本BROTHER、瑞士BERNINA、日本JUKI、日本JAGUAR、日本HAPPY 及中國大陸飛躍、恆強、萬維等廠商」（「SVP」2次、「越南」49次、「越南廠」3次），支持其與 SVP 集團之產業關聯及越南生產據點；惟「1968」（0次）、「全球最大」（0次）、「最大客戶」（0次）、「七成」（0次）與「全球市佔第一」均未獲支持。**數字歸屬須更正：「90%」唯一命中為「-46.90%」（財務變動比例）；「30%」4次分別為「獨立董事比率為30%」與「持股分級30,001至40,000」等，均非市占率。**
- `1626:objective_ranking_or_market_share:2a014c4508c270a2` — `PARTIALLY_SUPPORTED`. 艾美特-KY 2023年官方簡報載「**Electric heater ranked #1**」與「**Household fan ranked as #2 in China**」，並列 Fan、Electric heater 等產品線（「fan」5次、「heater」5次）；**惟電風扇之排名範圍明確標示為「in China」（中國），而 claim 表述為「全球**銷量第二」；電暖器之「#1」亦未標明範圍；「僅次於美的集團」與「No.1」未出現（「No.1」0次）。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）；UNKNOWN 追蹤清單維持 **87 筆**。
- Author-reviewed total: **482 / 1,399**; remaining: **917**. Outcome counts: ACCEPTED 71, PARTIALLY_SUPPORTED 320, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 87. Next pending claim by priority: `1810:objective_ranking_or_market_share:51ab5ce5d9716cb5` (和成).

## Author batch `author-085` — 2026-10-08

- Reviewed the next eight unreviewed objective ranking/market-share claims in checkpoint order (和成 1810 ×2, 川湖 2059 ×2, 元翎 4564 ×2, 泰金-KY 6629 ×2). Evidence came from directly downloaded and inspected official disclosures: 和成98年股東會年報、川湖2025年法人說明會簡報、元翎2024年永續報告書、泰金-KY 2022年法人說明會簡報。
- `1810:objective_ranking_or_market_share:51ab5ce5d9716cb5` 與 `18cac244bb931018` — `PARTIALLY_SUPPORTED`. 和成98年度年報載其業務與「**衛浴**（設備）」相關（「衛浴」46次）並多處敘述「**中國**」市場（78次）；惟「**市佔第二**」「**市佔第四**」「**市佔第一**」「**菲律賓**」與「越南」之出現次數均為0，故「台灣市佔第二、中國市佔第四、菲律賓市佔第一」未獲確立。註記：本批次自該官方網域可取得之版本為**98年度**，非近期版本。
- `2059:objective_ranking_or_market_share:c23a7e78fb5bb734` — `PARTIALLY_SUPPORTED`. 川湖2025年官方簡報載「**亞洲第一伺服器導軌製造商**」，與 claim 之「亞洲最大伺服器導軌製造商」相符（「導軌」11次、「1986」2次）；惟「**全球第二大**」與「全球市佔率約**三成**」未獲支持（「全球第二」「三成」均為0次）。
- `2059:objective_ranking_or_market_share:4efb402a64a4a4a6` — `UNKNOWN_AFTER_RESEARCH`. 「Accuride（全球市佔第一，約66%）」未獲確立：川湖官方簡報中「**Accuride**」與「**66%**」出現次數均為0，且本批次未取得 Accuride 自身之官方文件，依第三人市場地位之一致性規則結為 UNKNOWN。
- `4564:objective_ranking_or_market_share:5b9331d6b36946b2` 與 `44be16e89884bbf0` — `PARTIALLY_SUPPORTED`. 元翎2024年官方永續報告書載其「（生產）之各式高壓充氣鋼瓶，成為**全球高壓充氣鋼瓶製造領導廠**」與「成為**全球消費性高壓充氣鋼瓶領導廠商**」（「領導」8次），並見「**安全氣囊**」7次、「**比亞迪**」2次，支持其領導地位與安全氣囊業務及中國新能源車客戶關聯；惟「自有品牌**MOSA**」「全球市佔率**超過40%**」與「亞洲除日本外**唯一**」「**全系列**」均未獲支持。
- `6629:objective_ranking_or_market_share:011aa453e3809aa4` 與 `f4667886c406f031` — `UNKNOWN_AFTER_RESEARCH`. 泰金-KY 2022年官方簡報（文字擷取1,587字元）內容為公司基本資料、集團架構與產品應用類型（掛件/支架、窗飾、把手、衛浴），全份簡報中「**Home Depot**」「**IKEA**」與「最大」出現次數均為0，其客戶身分未獲確立。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。UNKNOWN 追蹤清單已同步刷新至 **90 筆**。
- Author-reviewed total: **490 / 1,399**; remaining: **909**. Outcome counts: ACCEPTED 71, PARTIALLY_SUPPORTED 325, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 90. Next pending claim by priority: `6629:objective_ranking_or_market_share:a8ac715de8b715a0` (泰金-KY).

## Author batch `author-086` — 2026-10-08

- Reviewed the next eight unreviewed objective ranking/market-share claims in checkpoint order (泰金-KY 6629 ×2, 峰源-KY 6807, 來思達 8066, 億豐 8464 ×2, 櫻花 9911 ×2). Evidence came from directly downloaded and inspected official disclosures: 泰金-KY 2022年法人說明會簡報、峰源113年度年報、來思達2015年法人說明會簡報、億豐111年度年報、櫻花102年度股東會年報。
- `6629:objective_ranking_or_market_share:a8ac715de8b715a0` 與 `6df22dec22cccf22` — `UNKNOWN_AFTER_RESEARCH`. 泰金-KY官方簡報（文字擷取1,587字元）內容為公司基本資料、集團架構與產品應用類型，全份簡報中「**Home Depot**」「**IKEA**」與「最大」出現次數均為0，客戶身分未獲確立。
- `6807:objective_ranking_or_market_share:cf492ef06b948781` — `UNKNOWN_AFTER_RESEARCH`. 峰源113年度年報之封面與發言人頁可讀，**惟自第4頁起之文字層呈現亂碼**（如「Ϧљᐱҥဠ٣」「ҽԖज़Ϧљ(ᆵ᡼ഝ྽മ)」等，與台光電、上洋、必應之年報同型），以關鍵字檢索「IKEA」「customer」「largest」「70%」與「25 years」之出現次數均為0，故「最大客戶為 IKEA、佔營收約七成、合作逾25年」未獲確立。
- `8066:objective_ranking_or_market_share:8d3161d07c2c386f` — `PARTIALLY_SUPPORTED`. 來思達2015年官方簡報中「**自有品牌**」出現3次，支持其自有品牌家具業務；惟「成立於1996年」（「1996」0次）與「台灣**唯一**擁有自有品牌並以 **B2B** 行銷全球」（「唯一」「B2B」均0次）未獲支持。註記：該版本為2015年。
- `8464:objective_ranking_or_market_share:12cdc0907b6edc55` — `PARTIALLY_SUPPORTED`. 億豐111年度年報中「**北美**」出現20次、「**PVC**」12次、「窗簾」219次，支持其北美市場之重要性及 PVC 管材產品；惟「北美市場為**最大營收來源**」未獲支持——「最大營收」2次之上下文均為**氣候風險情境**（「採產值比例推算，對億豐最大營收衝擊是0.2%、0.4%」），且「**除濕機**」「**空氣清淨**」出現次數均為0。
- `8464:objective_ranking_or_market_share:a2b185b497e23211` — `UNKNOWN_AFTER_RESEARCH`. 億豐年報中「**Hunter**」出現次數為0；年報中「全球最大」3次之一係指**億豐自身**「按2023年3月31日收盤價…市值約為美金33億，為**全球最大市值窗簾公司**」，**並非**對 Hunter Douglas 之敘述（且該表述係以市值為基準而非製造規模），故該第三人市場地位未獲確立。
- `9911:objective_ranking_or_market_share:9919abbc162a9a07` 與 `58fa6a469bd3bfc1` — `PARTIALLY_SUPPORTED`. 櫻花102年度年報中「**熱水器**」出現42次、「**莊頭北**」1次，支持其熱水器業務及同業關係；惟「創立於1978年」（「1978」0次）、「為台灣廚衛電器**第一品牌**」（0次）、「主要競爭者包括**林內**」（0次）與「熱水器台灣**市佔第一**」（0次）均未獲支持。註記：該版本為102年度。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。UNKNOWN 追蹤清單已同步刷新至 **94 筆**。
- Author-reviewed total: **498 / 1,399**; remaining: **901**. Outcome counts: ACCEPTED 71, PARTIALLY_SUPPORTED 329, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 94. Next pending claim by priority: `9935:objective_ranking_or_market_share:edace39a5abeffd8` (慶豐富).

## Author batch `author-087` — 2026-10-08

- Reviewed the next six unreviewed objective ranking/market-share claims in checkpoint order (慶豐富 9935, 毛寶 1732, 南六 6504 ×3, 康那香 9919). Evidence came from directly downloaded and inspected official disclosures: 慶豐富2018年法人說明會簡報、毛寶2020年企業社會責任報告書、南六年報、康那香2026年法人說明會簡報。
- `9935:objective_ranking_or_market_share:edace39a5abeffd8` — `UNKNOWN_AFTER_RESEARCH`. 慶豐富2018年官方簡報中「**Walmart**」與「**沃爾瑪**」出現次數均為0（「窗簾」11次、「客戶」2次均為通稱），未具名任何客戶，依具名客戶身分規則結為 UNKNOWN。
- `1732:objective_ranking_or_market_share:481aee35491d420d` — `PARTIALLY_SUPPORTED`. 毛寶2020年企業社會責任報告書載「生產及開發洗廁劑、玻璃亮光劑、**冷洗精**、廚房油污清潔劑（…）」（「冷洗精」3次），支持其冷洗精等清潔產品業務；惟「以『毛寶』及『**白鷺**』品牌聞名」（「白鷺」0次）與「**冷洗精市佔領先**」（「市佔」0次）未獲支持。註記：本批次取得者為企業社會責任報告書，非年報。
- `6504:objective_ranking_or_market_share:a9d7ea309cd8da26` — `PARTIALLY_SUPPORTED`. 南六年報「市場佔有率」段載「本公司主要產品為熱壓不織布、**水針不織布**及生技相關產品…就113年合併營業收入與同業比較，皆已優於康那香、新麗及恒大」，並載「依據美國主要的不織布月刊 Nonwovens Industry 統計，2023年**全球不織布銷售排名，本公司係列於第23名**，已超過國內之同業於世界排名之名次，並成為**亞洲地區重要的不織布大廠**」（「不織布」153次、「水針」35次、「高雄」16次），其中「第23名」屬於 claim 所述「全球前40大」之範圍；惟「為**亞洲水針不織布供應龍頭**」未獲支持（年報用語為「亞洲地區**重要的**不織布大廠」；「**龍頭**」1次之上下文為「**水龍頭**」之省水裝置），「成立於1972年」之「1972」亦為0次（年報以民國年表述）。
- `6504:objective_ranking_or_market_share:dad592a04c1ad087` 與 `b60ee696040661e2` — `PARTIALLY_SUPPORTED`. 南六年報載其產品包含「生技相關產品(包含**柔濕巾、面膜、乳液**等保養品）」，顯示其向下游消費產品延伸；惟全份年報中「**蘭韻**」「**康乃馨**」與「**化妝棉**」出現次數均為0，該兩品牌及「化妝棉國內市佔龍頭」未獲支持。
- `9919:objective_ranking_or_market_share:2affdfaaf7479723` — `PARTIALLY_SUPPORTED`. 康那香2026年官方簡報中「**不織布**」出現24次，支持其不織布製造業務；惟「成立於**1968年**」（「1968」0次）、「**衛生用品**製造大廠」（0次）與「位列**全球前40大**不織布廠商」（「全球前40」0次）均未獲支持。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。UNKNOWN 追蹤清單已同步刷新至 **95 筆**。
- Author-reviewed total: **504 / 1,399**; remaining: **895**. Outcome counts: ACCEPTED 71, PARTIALLY_SUPPORTED 334, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 95. Next pending claim by priority: `6671:objective_ranking_or_market_share:1c6728d636eea59e` (三能-KY).

## Author batch `author-088` — 2026-10-08

- Reviewed the next eight unreviewed objective ranking/market-share claims in checkpoint order (三能-KY 6671, 富堡 8929, 震旦行 2373, 巨路 6192 ×5). Evidence came from directly downloaded and inspected official disclosures: 三能集團年報、富堡公司年報營運概況、巨路111年度年報。
- `6671:objective_ranking_or_market_share:1c6728d636eea59e` — `PARTIALLY_SUPPORTED`. 三能集團官方年報載其「營運模式係以**自有品牌**之銷售為（主）」（「自有品牌」3次、「**SANNENG**」18次、「烘焙」353次、「烤模」10次），支持其自有品牌烘焙器具業務；惟「**UNOPAN**」出現次數為0，且「在亞洲商用烘焙市場**享有極高市佔率**」未獲支持——「市佔」1次之上下文為「提升線上銷售**市佔率**…」之**營運目標**敘述。
- `8929:objective_ranking_or_market_share:9995e14a016110bb` — `PARTIALLY_SUPPORTED`. 富堡官方文件載「**成人紙尿褲**」25次、「**看護墊**」4次、「**復健褲**」2次、「**安安**」1次，與 claim 所列產品線及品牌相符；惟「在台灣市場佔有**一至二成市佔率**」未獲支持（「市佔」與「Ancare」均為0次）。
- `2373:objective_ranking_or_market_share:3dc2f728f9ba57e4` — `UNKNOWN_AFTER_RESEARCH`. 震旦行官方網域之108年股東會年報端點、106.pdf 端點與2025永續報告書端點**均回應 HTTP 404**，未取得可檢視之官方文件，故其成立年與「台灣最大辦公設備通路集團之一」之地位未獲確立。
- `6192:objective_ranking_or_market_share:7b550e9b311db4ef` 與 `3a45ecd2ce0afe92` — `PARTIALLY_SUPPORTED`. 巨路111年度年報載「巨路在產品面主要與國際程控**領導品牌 Emerson** 合作，與其**共同開發大中華**（市場）」及「巨路合作夥伴 Emerson 仍為程控廠商之技術及品牌**領導廠商**」（「Emerson」4次、「程控」108次、「代理」43次），支持其與 Emerson 之合作與代理關係。惟「**獨家**代理」未獲支持（「獨家」0次，且年報載其「主要供應商包括 Emerson、ABB、Honeywell、Yokogawa 及 Siemens 等」）、「**最大**程控設備原廠」未獲支持（官方用語為「領導廠商」「領導品牌」）、「協助**台積電**等半導體大廠…進行全球建廠之自動化控制專案」亦未獲支持（「台積電」0次）。
- `6192:objective_ranking_or_market_share:9d3d9e091d15025a`、`29dfc8d397ce595b`、`7b53b3873666c020` — `UNKNOWN_AFTER_RESEARCH`. 三筆均為「台積電為程控營收最大客戶、約佔三成／30%」之具名客戶與集中度陳述；年報中「**台積電**」與「**三成**」出現次數均為0，且「**30%**」8次之上下文均為**淨值比率**（如「不超過本公司之淨值30%」），故依一致性規則結為 UNKNOWN。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。UNKNOWN 追蹤清單已同步刷新至 **99 筆**。
- Author-reviewed total: **512 / 1,399**; remaining: **887**. Outcome counts: ACCEPTED 71, PARTIALLY_SUPPORTED 338, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 99. Next pending claim by priority: `6192:objective_ranking_or_market_share:d0ce09fbc459509c` (巨路).

## Author batch `author-089` — 2026-10-08

- Reviewed the next eight unreviewed objective ranking/market-share claims in checkpoint order (巨路 6192, 羅昇 8374, 嘉實 3158, 精誠 6214, 晉泰 6221, 資拓宏宇 6614, 現觀科 6906 ×2). Evidence came from directly downloaded and inspected official disclosures: 巨路111年度年報、羅昇110年度年報、晉泰2023年法人說明會簡報、資拓宏宇114年度年報、現觀科技112年度年報。
- `6192:objective_ranking_or_market_share:d0ce09fbc459509c` — `PARTIALLY_SUPPORTED`. 本 claim 為巨路同一事實之條目表述（「Emerson（**全球最大**程控製造商，**獨家**代理）」）。年報載其「主要與國際程控**領導品牌 Emerson** 合作」且 Emerson「為程控廠商之技術及品牌**領導廠商**」；惟「全球最大」與「獨家」出現次數均為0，且年報明載其「主要供應商包括 **Emerson、ABB、Honeywell、Yokogawa 及 Siemens** 等」。
- `8374:objective_ranking_or_market_share:3152a46dc54ea3c8` — `PARTIALLY_SUPPORTED`. 羅昇110年度年報載「本公司屬**自動化機電零組件代理商暨技術服務業者**」（「自動化」66次、「代理」48次），支持其通路業務；惟「成立於1984年」（「1984」0次）與「為台灣**最大**專業自動化機電組件通路商」（「最大」0次）未獲支持。
- `3158:objective_ranking_or_market_share:6f3b16014ede3133` — `UNKNOWN_AFTER_RESEARCH`. 本批次未查得嘉實（3158）發行人官方網域之可下載年報或法人說明會端點，未取得可檢視之正式文件，其資料來源（證交所、櫃買中心、期交所、NASDAQ、NYSE）之具名關係未獲確立。
- `6214:objective_ranking_or_market_share:efede12ca151ffcc` — `UNKNOWN_AFTER_RESEARCH`. 本批次自精誠資訊官方網域下載之**兩份年報檔案均僅5,574 bytes**，經 PDF 文字擷取後各僅得1字元，顯非完整文件，故不予採用；本批次未取得精誠可檢視之官方文件。
- `6221:objective_ranking_or_market_share:03dcbb306517351e` — `UNKNOWN_AFTER_RESEARCH`. 晉泰2023年官方簡報（文字擷取6,626字元）內容為公司基本資料、數位轉型策略與資通訊方案，全份簡報中「**精誠**」「三成」與「最大股東」出現次數均為0，其股東身分與持股比例未獲確立。
- `6614:objective_ranking_or_market_share:a2228d1fc670af08` — `PARTIALLY_SUPPORTED`. 資拓宏宇114年度年報「市場占有率」段載其深耕「**智慧政府、智慧金融、智慧醫療與智慧城市**等四大領域」，並載「行政院轄下43機關中，切入41個機關，涵蓋率達**95%**；全國28個縣市政府其中有24個是本公司客戶，涵蓋率達**86%**；而**38間本國銀行切入其中35間，涵蓋率逾90%**」，與 claim 之「智慧政府（戶政／勞保等大型公共系統）」及「智慧金融（**服務逾90%台灣本土銀行**）」對應；惟「擁有**極高市佔率**」未獲支持——年報之官方用語為「**涵蓋率**」（「市佔」0次），「智慧政府在手訂單**逾30億元**」亦未獲支持（「30億」0次）。
- `6906:objective_ranking_or_market_share:662269e93948f5e3` 與 `d7f499644ed091ed` — `ACCEPTED`. 現觀科技112年度年報載「取得**中東地區最大電信業者 STC** CovMo™合作合約」與「透過合作夥伴取得**中東地區的最大電信業者 STC 集團**第十次 CovMo™產品擴充（訂單）」（「STC」4次、「中東」5次、「最大電信」4次），與 claim 之「Saudi Telecom (STC) — 中東最大電信營運商」逐字對應。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。UNKNOWN 追蹤清單已同步刷新至 **102 筆**。
- Author-reviewed total: **520 / 1,399**; remaining: **879**. Outcome counts: ACCEPTED 73, PARTIALLY_SUPPORTED 341, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 102. Next pending claim by priority: `7765:objective_ranking_or_market_share:ca7dd7afc3bd6233` (中華資安).

## Author batch `author-090` — 2026-10-08

- Reviewed the next seven unreviewed objective ranking/market-share claims in checkpoint order (中華資安 7765 ×2, 國泰金 2882 ×4, 凱基金 2883). Evidence came from directly downloaded and inspected official disclosures: 中華資安公司文件、國泰金控官方文件（含致股東報告書）。
- `7765:objective_ranking_or_market_share:ca7dd7afc3bd6233` 與 `5ea2c57aff387b29` — `PARTIALLY_SUPPORTED`. 中華資安年報載「**本公司之母公司為中華電信股份有限公司**，於114年及113年（…）」（「中華電信」3次），支持其母子公司關係；惟「全台第一大 **ISP 寬頻**與 **5G 網路骨幹**」未獲支持（全份文件中「ISP」「寬頻」「5G」「骨幹」「通路」出現次數均為0，該等敘述係對中華電信之描述）。
- `2882:objective_ranking_or_market_share:bdb9b99f8967d1f7` — `PARTIALLY_SUPPORTED`. 國泰金控官方文件載「**國泰金控為臺灣最大金融控股公司之一**，總資產 NT$12.8兆元(US$4,183.9億元)」，總資產規模明確；惟官方用語含「**之一**」，與 claim 之「為台灣**資產規模最大**之金融控股公司」不同（「資產規模最大」0次），「霖園集團核心」亦未獲支持（「霖園」4次為轉投資事業名稱）。
- `2882:objective_ranking_or_market_share:a2ee540a3626fa41` — `PARTIALLY_SUPPORTED`. 文件載「**國泰人壽成立於1962年，為臺灣最大人壽保險公司**」，與 claim 相符；惟「暨**最大機構投資者之一**，資產配置能力強」未獲支持（該語未見於文件；文件載其餘子公司「皆具產業領導地位」）。
- `2882:objective_ranking_or_market_share:cadef22332fa1adf` — `PARTIALLY_SUPPORTED`. 文件載「國泰世華銀行 **CUBE卡『一卡抵多卡』，流通卡數近600萬張**，刷卡占比超過全行刷卡量五成，成為**國內最大宗的銀行卡**」，與 claim 之「信用卡發卡王（CUBE 卡流通卡數近 600 萬張）」相符；惟「**財富管理與房貸業務市佔率極高**」未獲支持（「房貸」0次，「財富管理」13次未載市占率，「發卡」亦為0次）。
- `2882:objective_ranking_or_market_share:214bbde45faed47f` — `PARTIALLY_SUPPORTED`. 文件載其「主要子公司包括國泰人壽、國泰世華銀行、國泰產險、**國泰證券**、**國泰投信**、國泰創投等成員」且「皆具產業領導地位」（「國泰證券」54次、「國泰投信」43次）；惟「國泰投信為台灣**最大 ETF 發行商之一**」未獲支持（「ETF」31次之上下文為投資論壇與資產配置敘述）。
- `2883:objective_ranking_or_market_share:7060f1b3248b8161` — `UNKNOWN_AFTER_RESEARCH`. **本批次再次發現來源身分不符**：就凱基金控取得之檔案經下載檢視後，其封面為「2024 永續報告書」且目錄載「關於**凱基期貨**」，確認該文件**屬凱基期貨而非凱基金控**，故不予採用（全份文件中「中華開發」「創投」「私募」均為0次）；就 ticker 2883 未取得可檢視之控股公司正式文件。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。UNKNOWN 追蹤清單已同步刷新至 **103 筆**。
- Author-reviewed total: **527 / 1,399**; remaining: **872**. Outcome counts: ACCEPTED 73, PARTIALLY_SUPPORTED 347, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 103. Next pending claim by priority: `2852:objective_ranking_or_market_share:4a5ef4fd4fdcb9d2` (第一保).

## Author batch `author-091` — 2026-10-08

- Reviewed the next eight unreviewed objective ranking/market-share claims in checkpoint order (第一保 2852 ×5, 中再保 2851 ×3). Evidence came from directly downloaded and inspected official disclosures: 第一保2025年法人說明會簡報、中再保成立50周年特刊。
- `2852:objective_ranking_or_market_share:4a5ef4fd4fdcb9d2` — `PARTIALLY_SUPPORTED`. 第一保2025年官方簡報「基本資料」頁載「**設立日期 1962年**」，並載股東結構「金融機構1.15%、其他法人36.43%、**個人57.14%**、外國機構及外國人5.28%」，顯示無單一金融機構之控制性持股，與「獨立民營」相符；惟「與**第一金控**無直接股權隸屬關係」未獲來源陳述（全份簡報「第一金」「第一銀行」均為0次）。
- `2852:objective_ranking_or_market_share:a9cea9f32089f2c8`、`0ed2489ebb872b77`、`d1acd16b4de6e7eb` — `UNKNOWN_AFTER_RESEARCH`. 三筆均涉及「**第一銀行**長期銀行保險／銀保通路合作」：第一保官方簡報中「第一銀行」「銀保」「銀行保險」「車商」與「保險經紀人」出現次數均為0，具名通路夥伴關係未獲確立。
- `2852:objective_ranking_or_market_share:fb910ccfdc42b585` — `PARTIALLY_SUPPORTED`. 簡報「業務概況」呈現簽單保費收入（2024年8,941,329仟元）、自留保費收入與業務結構（汽車任意險48.94%、火災保險20.00%等），支持其產物保險承保業務；惟「核保、保單設計、理賠管理與資產運用」之職能區分未見於簡報敘述。
- `2851:objective_ranking_or_market_share:f4428cbe7406c75a` — `ACCEPTED`. 中再保50周年特刊（民國107年出版）載「**民國52年**7月奉准…籌設『中央再保險公司』，並於**民國57年10月31日正式成立**」「於**民國91年**7月11日財政部第二階段釋股，公股持股比率降至48.12%，自此本公司**轉換為民營公司**」及「**長榮集團為本公司之最大股東，持股比率為58.68%**，財政部持股比率為20.39%」，三項要素（1968年成立、2002年民營化、長榮集團為最大股東）逐項對應。**方法論註記：特刊以西元數字「1968」與「2002」檢索均為0次，須以民國57年與民國91年比對（本審核第二類假陰性）。**
- `2851:objective_ranking_or_market_share:5019a1f91c5268c9` — `PARTIALLY_SUPPORTED`. 特刊載其為「**國內唯一的本土專業再保險公司**」並「成為國內**唯一專業之上市再保險公司**」（「唯一」4次）；惟「在國內市場具備**寡占**優勢」未獲支持（「寡占」「市占」均為0次）。
- `2851:objective_ranking_or_market_share:31637d692bd9234c` — `PARTIALLY_SUPPORTED`. 特刊載「**財產再保險業務發展**」「**人身再保險業務發展**」等業務範疇；惟「財產再保險**市占率約18.8%**、人身再保險**市占率約19.4%**」未獲支持——全份特刊「**市占**」0次，且「18.8」與「19.4」各出現1次之上下文均為**未標示名稱之數字表格**，未以「市占率」表述該二數值。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。UNKNOWN 追蹤清單將於下一批次同步刷新至 **106 筆**。
- Author-reviewed total: **535 / 1,399**; remaining: **864**. Outcome counts: ACCEPTED 74, PARTIALLY_SUPPORTED 351, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 106. Next pending claim by priority: `5878:objective_ranking_or_market_share:ac33ab82c59a8a20` (台名).

## Author batch `author-092` — 2026-10-08

- Reviewed the next five unreviewed objective ranking/market-share claims in checkpoint order (台名 5878, 榮運 2607 ×3, 中航 2612). Evidence came from directly downloaded and inspected official disclosures: 台名公司文件、榮運2026年法人說明會簡報、中航112年度年報。
- `5878:objective_ranking_or_market_share:ac33ab82c59a8a20` — `PARTIALLY_SUPPORTED`. 台名官方文件載其「（壽）險公司之首年度保費及**續年度保費之佣金收入**為新台幣480,838仟元，佔營業（收入）」，並載「台名集團之**佣金收入**認列主係於客戶合約辨認履約義務後…」（「經紀」34次、「佣金」16次、「壽險」9次、「續年」4次），支持其以壽險經紀佣金為主要收入來源；惟 claim 所述之**收入結構百分比（壽險經紀約48%、續年約27%、獎金及手續費約15%、產險及其他約10%）**未見於本件之分項結構。
- `2607:objective_ranking_or_market_share:eae39f4c4c4f4d7b` — `PARTIALLY_SUPPORTED`. 榮運2026年官方簡報「公司業務」頁載「**貨櫃運輸**：5座車庫｜**156部曳引車**｜**740部板架**」「2座內陸貨櫃場」「台中港貨櫃碼頭…**40部船邊專用解櫃車輛**」「**10家直靠航商客戶**，遍及兩岸、東南亞及東北亞」「62部交通遊覽車」等，支持其內陸貨櫃運輸業務且車隊規模具體；惟「擁有**全台最大**貨櫃車隊」未獲支持（「全台最大」與「貨櫃車隊」均為0次）。
- `2607:objective_ranking_or_market_share:4b0fbf64456a202c` 與 `8f8f4b26870312a9` — `UNKNOWN_AFTER_RESEARCH`. 兩筆均涉及具名客戶「**長榮海運**（最大客戶）」「**陽明海運**」：榮運官方簡報中該二公司名稱與「最大客戶」出現次數均為0，客戶僅以「**10家直靠航商客戶**」通稱而未具名。
- `2612:objective_ranking_or_market_share:f023856ea96f015b` — `PARTIALLY_SUPPORTED`. 中航112年度年報中「**偉聯運輸**」出現41次、「內陸」38次、「拖車」1次，並載該公司為其子公司及其業務性質，支持其透過子公司經營內陸貨櫃運輸；惟「**市佔率頗高**」未獲支持（「市佔」0次）。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。UNKNOWN 追蹤清單已同步刷新至 **108 筆**。
- Author-reviewed total: **540 / 1,399**; remaining: **859**. Outcome counts: ACCEPTED 74, PARTIALLY_SUPPORTED 354, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 108. Next pending claim by priority: `2636:objective_ranking_or_market_share:b0e48b98528244b3` (台驊控股).

## Author batch `author-093` — 2026-10-08

- Reviewed the next eight unreviewed objective ranking/market-share claims in checkpoint order (台驊控股 2636, 宅配通 2642, 數字 5287 ×3, 富邦媒 8454 ×3). Evidence came from directly downloaded and inspected official disclosures: 宅配通個體財務報告（114年度及113年度）、數字科技股東會年報、富邦媒2024 Annual Report（英文版）。
- `2636:objective_ranking_or_market_share:b0e48b98528244b3` — `UNKNOWN_AFTER_RESEARCH`. 台驊控股發行人官方網域之財務專區為**文件索引形式**，未直接提供可下載之年報或法人說明會簡報 PDF，本批次未能取得載有營收結構之可檢視官方文件。
- `2642:objective_ranking_or_market_share:6cfd9d7f082d8b12` — `PARTIALLY_SUPPORTED`. 宅配通財務報告載「台灣宅配通股份有限公司…主要營業項目為**汽車路線貨運及宅配**等專業物流配送服務。**東元電機股份有限公司持有本公司**（…）」（「東元」15次），支持其宅配業務與東元之持股關係；惟「為台灣**第一家**提供**戶對戶（Door-to-Door）**宅配服務之業者」（「第一家」「戶對戶」0次）與「與**日本通運**技術合作成立」（「日本通運」0次）未獲支持。
- `5287:objective_ranking_or_market_share:b429f32154c5e076` — `PARTIALLY_SUPPORTED`. 數字科技年報載 591（85次）、8591（35次）、「房屋」31次、「寶物」12次、「人力」23次、「室內設計」8次與「小雞上工：全臺最大的打工APP」，平台組合與領域涵蓋與 claim 相符；惟「旗下擁有多個**高市佔率**之垂直媒合平台」之概括表述未獲支持（「市占」0次）。
- `5287:objective_ranking_or_market_share:ee2db393fbb7a072` — `PARTIALLY_SUPPORTED`. 年報載「臺灣591 房屋交易網」持具積極導入更多新服務（如VR看屋），支持該平台之存在；惟「**台灣最大**房屋租售媒合平台」未獲支持——全份文件中以「最大」描述者為 **8591**（臺灣最大的線上遊戲虛擬寶物交易平台）與**小雞上工**（全臺最大的打工APP），**未見以「最大」描述 591 之敘述**。
- `5287:objective_ranking_or_market_share:bd1a0819aadbeb8c` — `ACCEPTED`. 年報載「**8591 寶物交易網：臺灣最大的線上遊戲虛擬寶物交易平台**，採用C2C 商業（模式）」，與 claim 逐字對應。
- `8454:objective_ranking_or_market_share:831fc9adc6fce229`、`8562fb574e9c1bc9`、`faf0013285a9ca12` — `PARTIALLY_SUPPORTED`. 富邦媒2024年報（**英文版**）載「（A）s the **leading e-commerce player** in（Taiwan）」「leading the **No. 1 e-commerce brand** in（Taiwan）」與「momo invested more than NT$3 billion to build the **largest warehouse** in southern（Taiwan）」（「leading」8次、「largest」6次、「e-commerce」35次、「B2C」9次），支持其電商領先地位與 B2C 業務；惟「年營收**突破千億**台幣」與「隸屬於**富邦集團**」未獲對應陳述（「3C、家電、美妝、食品、日用品全品類」之逐項敘述亦未見）。**方法論註記：本件為英文版文件，以中文關鍵字檢索「電子商務」「營收」「市佔」「第一」「領導」之出現次數均為0，須改以英文詞彙比對（本審核第四類假陰性）。**
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。UNKNOWN 追蹤清單已同步刷新至 **109 筆**。
- Author-reviewed total: **548 / 1,399**; remaining: **851**. Outcome counts: ACCEPTED 75, PARTIALLY_SUPPORTED 360, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 109. Next pending claim by priority: `1432:objective_ranking_or_market_share:308460c572bff85d` (大魯閣).

## Author batch `author-094` — 2026-10-08

- Reviewed the next eight unreviewed objective ranking/market-share claims in checkpoint order (大魯閣 1432, 力山 1515 ×2, 岱宇 1598, 喬山 1736, 世界健身-KY 2762, 拓凱 4536 ×2). Evidence came from directly downloaded and inspected official disclosures: 大魯閣年報、世界健身-KY 2025年股東常會議事錄、拓凱2024 Q4投資人簡報（英文版）。
- `1432:objective_ranking_or_market_share:308460c572bff85d` — `PARTIALLY_SUPPORTED`. 大魯閣年報載其「（棒）壘球打擊場，**4 家保齡球館**、1 家卡丁車場、3 家『Roller 186 滑輪場』、2 家『福湯岩盤浴』」（「棒壘球」6次、「打擊場」14次、「保齡球」5次），其中「**4 家保齡球館**」與 claim 相符；惟「全台**唯一**」（「唯一」0次）、「規模最大」（年報用語為「為**台灣最大的運動休閒場館經營者之一**」，**含「之一」之緩和語**）與「全國擁有 **12 座打擊場**」（「12 座」0次）未獲支持。
- `1515:objective_ranking_or_market_share:5787037fd7c3cb1b` 與 `e690fdc93cc165d0` — `UNKNOWN_AFTER_RESEARCH`. 力山官方簡報之文字擷取**僅2,124字元**（19頁）且實質內容極少，以關鍵字檢索「Peloton」「Life Fitness」「Precor」「Technogym」與「最大」之出現次數均為0，不足以支持或否定 claim 所述之客戶組合與營收結構。
- `1598:objective_ranking_or_market_share:e02e4b48f7e5db2a` — `UNKNOWN_AFTER_RESEARCH`. 岱宇官方網域之108年度年報端點回應 **HTTP 404**，未取得可檢視之檔案。
- `1736:objective_ranking_or_market_share:6ff73dcc29c7c647` — `UNKNOWN_AFTER_RESEARCH`. 喬山法人說明會簡報端點所取得之檔案**僅690 bytes**，經 PDF 文字擷取後僅得1字元，**顯非完整文件**，故不予採用。
- `2762:objective_ranking_or_market_share:d7e0098f0ada0257` — `PARTIALLY_SUPPORTED`. 世界健身-KY 2025年股東常會議事錄載「2024年，是世界健身-KY展現市場影響力的一年…世界健身-KY在2024年1月24日正式掛牌上市…並在同年10月28日宣布完成收購美國 World Gym Internati（onal）」，支持其品牌經營、上市與國際收購；惟「為台灣**市佔率第一**的連鎖健身品牌」（「**市佔**」0次；「第一」4次之上下文為「第一季」「第一審」）、「會員數超過 **45 萬人**」（0次）與「全台據點逾 **100 間**」（0次）均未獲支持。
- `4536:objective_ranking_or_market_share:7dac44f797d7d0a3` 與 `a33703172baf7eba` — `PARTIALLY_SUPPORTED`. 拓凱2024 Q4投資人簡報（英文版）載「Started with **tennis racket** business」「Diversified into **bike and helmet** business」並見 **Wilson** 與 **Babolat** 各1次（「racket」7次、「helmet」5次、「bike」5次、「market share」2次）；惟「**largest**」「**leading**」「**world**」與「**No.1**」出現次數均為0，故「**全球最大**網球拍 OEM 廠」與「Wilson（**最大客戶**）」均未獲支持。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。UNKNOWN 追蹤清單已同步刷新至 **113 筆**。
- Author-reviewed total: **556 / 1,399**; remaining: **843**. Outcome counts: ACCEPTED 75, PARTIALLY_SUPPORTED 364, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 113. Next pending claim by priority: `6670:objective_ranking_or_market_share:0b9c48bd7d884e3f` (復盛應用).

## Author batch `author-095` — 2026-10-08

- Reviewed the next eight unreviewed objective ranking/market-share claims in checkpoint order (復盛應用 6670, 波力-KY 8467 ×3, 美利達 9914 ×2, 巨大 9921 ×2). Evidence came from directly downloaded and inspected official disclosures: 復盛應用2022年永續報告書、波力-KY 111年度年報、美利達2025年8月法人說明會簡報。
- `6670:objective_ranking_or_market_share:0b9c48bd7d884e3f` — `PARTIALLY_SUPPORTED`. 復盛應用2022年永續報告書載「（本公司）成立於1989年，為**全球最大之高爾夫球桿頭生產據點**」與「復盛應用身為**全球最大之高爾夫球桿頭製造商**」（「全球最大」2次、「桿頭」24次），與 claim 之核心地位相符；惟「在全球中高階球桿頭市場佔有率**高達五成以上**」未獲支持——全份報告書中「五成」「市占」「市佔」**均為0次**，且「50%」1次之上下文為**供應商季度考核之D類佔比**（「D 類佔比5%以下」），**非市占率**（數字脫離語意）。
- `8467:objective_ranking_or_market_share:48dd1d22ba83c457` — `PARTIALLY_SUPPORTED`. 波力-KY 111年度年報載「A公司是目前**全球最大曲棍球品牌**」，並載「品質持續提升與交貨準確度促使其**全球市占率自2005年8%穩定成長至50%**」，另段具名「與主要客戶 **Bauer Hockey** 合作逾十年」（「Bauer」2次）；惟「在高階冰球桿市場市佔率**已超過 50%**」未獲精確支持（官方為「成長**至** 50%」，且未以「高階」界定該市場）。**註記：年報部分段落將該客戶匿名為「A公司」，另一段落則具名 Bauer Hockey。**
- `8467:objective_ranking_or_market_share:9a6071b2054ff71b` 與 `5b5b16a8a12e4d56` — `PARTIALLY_SUPPORTED`. 代工關係與「頭盔」2次成立；惟「**最大客戶**」出現次數為0（官方僅稱「主要客戶」），「高階市佔逾50%」亦如上述未獲精確支持。
- `9914:objective_ranking_or_market_share:6f51a2c9276ae36b` 與 `f9ee3f3ed9072675` — `PARTIALLY_SUPPORTED`. 美利達2025年8月官方簡報載「**歐洲是主要市場**(Europe is the（…）)」及「台灣廠銷往歐洲市場的車款比例」「歐洲市場銷售成長」（「歐洲」4次）；惟「（**最大市場**）」未獲支持（「最大市場」0次，官方語為「主要市場」）。
- `9921:objective_ranking_or_market_share:53af3876a9921e62` 與 `c46e30a478d1a6f2` — `UNKNOWN_AFTER_RESEARCH`. 本批次就巨大（9921）嘗試三個官方端點（109年報、112年報與 MOPS 之 2024法人說明會簡報），**三者均回應 HTTP 404**，未取得可檢視之官方文件。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。UNKNOWN 追蹤清單已同步刷新至 **115 筆**。
- Author-reviewed total: **564 / 1,399**; remaining: **835**. Outcome counts: ACCEPTED 75, PARTIALLY_SUPPORTED 370, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 115. Next pending claim by priority: `6655:objective_ranking_or_market_share:0f29d3a1cca9dfcd` (科定).

## Author batch `author-096` — 2026-10-09

- Reviewed the next eight unreviewed objective ranking/market-share claims in checkpoint order (科定 6655 ×3, 綠河-KY 8444, 長榮 2603, 慧洋-KY 2637, 建新國際 8367 ×2). Evidence came from directly downloaded and inspected official disclosures: 科定2019年法人說明會簡報、綠河-KY 2025年法人說明會簡報、長榮海運115年4月法人說明會簡報。
- `6655:objective_ranking_or_market_share:0f29d3a1cca9dfcd` — `ACCEPTED`. 科定官方簡報載「生產總部：**嘉義縣大林鎮大埔美園區五路10號**」與「生產總部 嘉義**大埔美**一廠｜嘉義**大埔美**二廠」，並在競爭優勢項下載「2. **業界唯一，產銷一條龍垂直整合**」（「大埔美」3次、「唯一」1次、「一條龍」1次、「垂直整合」1次），與 claim 之兩項要素（生產總部位於嘉義大埔美、業界唯一產銷一條龍垂直整合）逐項對應。
- `6655:objective_ranking_or_market_share:055a6afbd23947d4` 與 `ccaa6c4b5d8549e4` — `UNKNOWN_AFTER_RESEARCH`. 兩筆均涉及「**大日本印刷 (DNP)**」：查閱之科定官方簡報中「**大日本印刷**」「**DNP**」「ECO」「PP」「EB」與「食品級」之出現次數**均為0**，未載該策略合作或 ECO+ 產品之技術內容，且本批次未取得 DNP 自身之官方文件。
- `8444:objective_ranking_or_market_share:1ba76f09f75f204f` — `PARTIALLY_SUPPORTED`. 綠河-KY 2025年官方簡報中「**塑合板**」出現37次、「泰國」4次，支持其於泰國經營塑合板（粒片板）業務；惟「為**亞洲最大**粒片板（塑合板）廠之一」未獲支持——「**亞洲最大**」僅出現1次，其上下文為「（燃）煤發電廠(南韓也是**亞洲最大**木質顆（粒）)」之**產業用電情境敘述**，**非**對綠河自身地位之描述。
- `2603:objective_ranking_or_market_share:c49229ece3415b49` — `PARTIALLY_SUPPORTED`. 長榮海運2026年4月官方簡報「公司現況」頁載「**7th 全球船隊運能排名**」「**船隊運能市佔率 5.8%**」「集團總營運船隻數 238」「全球航線擴及國家 101」，第7名屬「全球前十大」之範圍；惟「成立於**1968年**」（「1968」0次；長榮成立於民國57年，惟本件未載）與「為**台灣最大**（貨櫃航運公司）」（0次）未獲支持。
- `2637:objective_ranking_or_market_share:c179a03f49adb48f` — `UNKNOWN_AFTER_RESEARCH`. 慧洋-KY 官方網域之2025年度年報端點回應 **HTTP 404**，未取得可檢視之檔案。
- `8367:objective_ranking_or_market_share:654fe06c1da29251` 與 `50a32e6e94716675` — `UNKNOWN_AFTER_RESEARCH`. 建新國際之法人說明會簡報端點所取得之檔案**僅690 bytes**，經 PDF 文字擷取後僅得1字元，**顯非完整文件**，故不予採用。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。UNKNOWN 追蹤清單已同步刷新至 **120 筆**。
- Author-reviewed total: **572 / 1,399**; remaining: **827**. Outcome counts: ACCEPTED 76, PARTIALLY_SUPPORTED 372, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 120. Next pending claim by priority: `1343:objective_ranking_or_market_share:f0a65b719a264687` (旭東環保).

## Author batch `author-097` — 2026-10-09

- Reviewed the next six unreviewed objective ranking/market-share claims in checkpoint order (旭東環保 1343, 勤美 1532, 精剛 1584, 光洋科 1785 ×2, 錩新 2415). Evidence came from directly downloaded and inspected official disclosures: 旭東環保2021年法人說明會簡報、精剛2026年法人說明會簡報、錩新2023年法人說明會簡報。
- `1343:objective_ranking_or_market_share:f0a65b719a264687` — `UNKNOWN_AFTER_RESEARCH`. 旭東環保官方簡報載其「開發**水面**型太陽能支撐座」「開發直徑20米**海上**箱網系統」與「**屏東**加工出口區設立新廠」（「屏東」4次、「水面」2次）；惟「**佳冬**」「**太陽光電**」「**全球最大**」與「案場」之出現次數均為0，該特定案場及其全球排名未獲確立。
- `1532:objective_ranking_or_market_share:63f553b91ed507d5` — `UNKNOWN_AFTER_RESEARCH`. 勤美官方網域之文件端點回應 **HTTP 404**，未取得可檢視之檔案。
- `1584:objective_ranking_or_market_share:e15f16a6d0286001` — `PARTIALLY_SUPPORTED`. 精剛2026年4月官方簡報中「**鈦合金**」出現9次、「**超合金**」出現4次、「台灣」2次，支持其超合金與鈦合金材料之生產；惟「為台灣**唯一**專業生產…之工廠」未獲支持（「唯一」0次；且該簡報文字擷取僅2,003字元）。
- `1785:objective_ranking_or_market_share:6815a6279f48d47c` 與 `32849e7d1bc93f05` — `UNKNOWN_AFTER_RESEARCH`. 光洋科之法人說明會簡報端點所取得之檔案**僅690 bytes**，經 PDF 文字擷取後僅得1字元，**顯非完整文件**，故不予採用。
- `2415:objective_ranking_or_market_share:b314132dd634687f` — `PARTIALLY_SUPPORTED`. 錩新2023年8月官方簡報中「**鍛造**」出現9次、「**揚聲器**」出現6次，支持其揚聲器鍛造零組件之製造；惟「為全球揚聲器鍛造零組件**龍頭**」（「龍頭」0次）與「車用揚聲器全球市佔**逾19%**」（「19%」「市佔」均0次）未獲支持。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。UNKNOWN 追蹤清單已同步刷新至 **124 筆**。
- Author-reviewed total: **578 / 1,399**; remaining: **821**. Outcome counts: ACCEPTED 76, PARTIALLY_SUPPORTED 374, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 124. Next pending claim by priority: `4534:objective_ranking_or_market_share:9544823face2741c` (慶騰).

## Author batch `author-098` — 2026-10-09

- Reviewed the next five unreviewed objective ranking/market-share claims in checkpoint order (慶騰 4534 ×2, 健椿 4561, 聯德控股-KY 4912, 匯僑 2904). Evidence came from directly downloaded and inspected official disclosures: 健椿2024年度年報、匯僑2024年法人說明會簡報。
- `4534:objective_ranking_or_market_share:9544823face2741c` 與 `df5a6c2d9d123139` — `UNKNOWN_AFTER_RESEARCH`. 本批次就慶騰（4534）搜尋可檢視之官方文件，所取得之結果均為第三方財經資料庫與獎項名單頁面，**未查得發行人官方網域之可下載年報或法人說明會簡報端點**；另亦未取得 Höganäs 自身之官方文件，故「客戶含 Bosch、Makita、Stanley Black & Decker、TTI」與「上游金屬粉末來自 Höganäs（全球最大鐵粉廠）」均未獲確立。
- `4561:objective_ranking_or_market_share:97a04d12e6cfe518` — `PARTIALLY_SUPPORTED`. 健椿2024年度年報中「**主軸**」出現162次、「精密」104次、「上櫃」20次、「**KENTURN**」2次（年報載「對於本公司自有品牌『KENTURN』之產品形象及國際競爭力均有正面助益」），支持其精密主軸製造業務、品牌名稱與上櫃身分；惟「為台灣**唯一**上櫃精密主軸專業廠」未獲支持（「唯一」0次）。
- `4912:objective_ranking_or_market_share:8324f94ac4ccaf9f` — `UNKNOWN_AFTER_RESEARCH`. 聯德控股官方網域之2019年法人說明會簡報端點回應 **HTTP 404**，未取得可檢視之檔案；亦未取得 Autoliv 自身之官方文件，故「Autoliv（全球最大安全氣囊供應商）」未獲確立。
- `2904:objective_ranking_or_market_share:7f1bb17b9de305f7` — `PARTIALLY_SUPPORTED`. 匯僑2024年8月官方簡報中「**儲槽**」出現6次，支持其石化儲槽倉儲業務；惟「為台灣**最大民營**石化**岸槽**倉儲服務商」（「台灣最大」「岸槽」「民營」均0次）與「儲槽規模**僅次於台塑集團與台灣中油**」（「**台塑**」「**中油**」均0次）未獲支持。註記：該簡報文字擷取僅3,103字元。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。UNKNOWN 追蹤清單已同步刷新至 **127 筆**。
- Author-reviewed total: **583 / 1,399**; remaining: **816**. Outcome counts: ACCEPTED 76, PARTIALLY_SUPPORTED 376, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 127. Next pending claim by priority: `6505:objective_ranking_or_market_share:7f3ac62fdb7f42ab` (台塑化).

## Author batch `author-099` — 2026-10-09

- Reviewed the next eight unreviewed objective ranking/market-share claims in checkpoint order (台塑化 6505 ×3, 聯友金屬-創 7610 ×4, 泰銘 9927). Evidence came from directly downloaded and inspected official disclosures: 台塑化112年度股東會年報、聯友金屬114年度年報、泰銘2012年法人說明會簡報。
- `6505:objective_ranking_or_market_share:7f3ac62fdb7f42ab` — `PARTIALLY_SUPPORTED`. 台塑化112年度年報載「（本公司）生產銷售事業，為**國內唯一之民營石油煉製業者**」，並見「六輕」13次、「麥寮」20次、「煉油」5次，支持其唯一民營煉製地位與麥寮六輕生產基地；惟「**1992年**由台塑、南亞塑膠、台化、福懋等共同投資設立」未獲支持（「1992」0次；台塑化設立於民國81年，惟本件未載）。
- `6505:objective_ranking_or_market_share:e384f6967f7009fd` 與 `e2932b76fb13de47` — `PARTIALLY_SUPPORTED`. 年報載其為石油煉製業者、「六輕」13次，支持油品與石化事業之經營；惟四項數字均未獲支持（「**62%**」「**54萬**」「**600座**」「**24%**」「**313萬**」與「**最大石化**」均0次；「**69%**」3次之上下文含「15.69%」等財務比率，**未以市占率表述**）。
- `7610:objective_ranking_or_market_share:66f0a1d3b55f8053` — `PARTIALLY_SUPPORTED`. 聯友金屬114年度年報載「本公司為**國內唯一**以二次硬質合金物料及製程產生之碎削為原料**再製生產鎢酸（鈉）**」，並載「為**台灣首家也是唯一**一家以自有研發的鎢金屬循（環）」，支持其再生產鎢酸鈉之業務與國內唯一性；惟「為**全球最大**『再製』鎢酸鈉製造商」未獲支持——「全球最大」0次，年報之唯一性表述範圍**為國內**（**範圍放大**）；「年出口量約 **2,500 噸**」亦未獲支持——「2,500」1次之上下文為產業**每年消耗量**「約略為2,000-2,500噸」。
- `7610:objective_ranking_or_market_share:8dc2d0884b44a2f2`、`f09b19c3cba50f22` 與 `0e82075cdeab2da0` — `UNKNOWN_AFTER_RESEARCH`. 三筆分別涉及具名客戶「台積電、Apple、Tesla」與第三人「Alconix」：聯友114年度年報中「**台積電**」「**Apple**」「**Tesla**」「**Alconix**」與「合格供應」之出現次數**均為0**，且未取得 Alconix 自身之官方文件。
- `9927:objective_ranking_or_market_share:55726d612dd2b764` — `PARTIALLY_SUPPORTED`. 泰銘官方簡報中「**鉛合金**」出現1次，支持其鉛合金相關業務；惟「為**亞洲最大**鉛合金**提煉**廠」（「亞洲最大」「提煉」均0次）與「台灣鉛合金市佔 **85%**」（「85%」「市佔」均0次）未獲支持。註記：該簡報文字擷取僅2,338字元、版本為2012年。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。UNKNOWN 追蹤清單已同步刷新至 **130 筆**。
- Author-reviewed total: **591 / 1,399**; remaining: **808**. Outcome counts: ACCEPTED 76, PARTIALLY_SUPPORTED 381, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 130. Next pending claim by priority: `9927:objective_ranking_or_market_share:d1bcdef3b01aa98b` (泰銘).

## Author batch `author-100` — 2026-10-09

- Reviewed the next seven unreviewed objective ranking/market-share claims in checkpoint order (泰銘 9927 ×2, 達邦蛋白 6578, 萬達寵物 6968 ×2, 永裕 1323, 福貞-KY 8411). Evidence came from directly downloaded and inspected official disclosures: 泰銘2012年法人說明會簡報、達邦蛋白114年度年報、福貞-KY 2026年法人說明會簡報。
- `9927:objective_ranking_or_market_share:d1bcdef3b01aa98b` — `PARTIALLY_SUPPORTED`. 泰銘官方簡報「重要記事」頁載「**1994年 成立甲級廢棄物清除機構**」「**1994年 成立甲級廢棄物處理機構**」與「2009年 泰銘(越南)公司取得**回收清運處理執照**」（「回收」2次、「許可」1次），支持其具廢棄物清除處理資格；惟「為**台灣唯一**具**廢鉛蓄電池**回收處理許可」未獲支持——「**唯一**」「**廢鉛**」「**蓄電池**」之出現次數均為0。
- `9927:objective_ranking_or_market_share:83c2cace1a7adb89` — `UNKNOWN_AFTER_RESEARCH`. 泰銘官方簡報中「**廣隆**」「**湯淺**」「**統一工業**」與「**85%**」之出現次數均為0，未具名該等客戶或載其市占率。
- `6578:objective_ranking_or_market_share:09e7de3479451061` — `PARTIALLY_SUPPORTED`. 達邦蛋白114年度年報中「**水解**」63次、「**黃豆**」70次、「**胜肽**」66次、「HACCP」4次，並載「通過歐盟最高標準 **HACCP、ISO22000 及 FAMI-QS 三重認證**」，支持其產品與認證；惟「為**亞洲規模最大**的水解黃豆胜肽蛋白製造商」（「亞洲規模最大」「亞洲最大」均0次）與「**亞洲首家**取得 HACCP 認證」（「**首家**」0次）未獲支持。
- `6968:objective_ranking_or_market_share:e2da6fd04d9bf077` 與 `7e52a1cf3bc0a020` — `UNKNOWN_AFTER_RESEARCH`. 萬達寵物之法人說明會簡報端點回應 **HTTP 404**，未取得可檢視之官方文件。
- `1323:objective_ranking_or_market_share:61b971a876a3995b` — `UNKNOWN_AFTER_RESEARCH`. 永裕官方網域之文件端點**無法連接至遠端伺服器**（連線失敗），未取得可檢視之檔案。
- `8411:objective_ranking_or_market_share:3998dade30256c2c` — `PARTIALLY_SUPPORTED`. 福貞-KY 2026年官方簡報中「**馬口鐵**」出現2次、「**三片罐**」1次、「中國」2次，支持其馬口鐵包裝容器及三片罐業務；惟「為中國大陸**第三大**」（「第三大」0次）與「馬口鐵三片罐**市佔率約15%**」（「15%」「市佔」均0次）未獲支持。註記：該簡報文字擷取僅1,542字元。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。UNKNOWN 追蹤清單已同步刷新至 **134 筆**。
- Author-reviewed total: **598 / 1,399**; remaining: **801**. Outcome counts: ACCEPTED 76, PARTIALLY_SUPPORTED 384, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 134. Next pending claim by priority: `9905:objective_ranking_or_market_share:9dd75a043dafb144` (大華).

## Author batch `author-101` — 2026-10-09

- Reviewed the next seven unreviewed objective ranking/market-share claims in checkpoint order (大華 9905, 統一實 9907, 宏全 9939, 龍巖 5530 ×2, 旭然 4556, 大車隊 2640). Evidence came from directly downloaded and inspected official disclosures: 大華2026年法人說明會簡報、統一實年報、宏全2010年法人說明會簡報、龍巖2024年法人說明會簡報、旭然2015年法人說明會簡報、大車隊2024年法人說明會簡報。
- `9905:objective_ranking_or_market_share:9dd75a043dafb144` — `PARTIALLY_SUPPORTED`. 大華2026年官方簡報中「**鋁罐**」出現7次，支持其鋁罐製造業務；惟「國內**唯一綜合性**包裝容器製造企業」（「唯一」「綜合性」均0次）、「為**台灣最大**鋁罐製造商」（「最大」0次）與「市佔率約 **35%**」（「市佔」0次；且「**35%**」1次之上下文為**財務比率**「費用率…5.35%」，**非市占率**）未獲支持。
- `9907:objective_ranking_or_market_share:bd571e06d78ed907` — `PARTIALLY_SUPPORTED`. 統一實年報中「**馬口鐵**」出現81次、「**垂直整合**」1次，支持其馬口鐵製造業務與垂直整合模式；惟「為國內最大且**亞洲第一**的馬口鐵廠」（「亞洲第一」0次）與「在中國大陸規模僅次於**寶鋼**」（「**寶鋼**」0次）未獲支持。
- `9939:objective_ranking_or_market_share:15e2e8695fe9d5ba` — `PARTIALLY_SUPPORTED`. 宏全官方簡報中「**1969**」出現2次、「**包材**」19次、「**大中華**」4次，支持其成立年度、包裝材料業務及大中華市場布局；惟「為台灣**規模最大**之包裝材料製造商之一」（「最大」0次）與「為大中華地區**第三大**飲料包材公司」（「第三大」0次）未獲支持。註記：版本為2010年。
- `5530:objective_ranking_or_market_share:c4e955be65adb681` — `PARTIALLY_SUPPORTED`. 龍巖2024年官方簡報載「**生前契約市佔率**」與「**約79%**」，並載「服務範圍有**禮儀服務、生前契約**、塔位墓園及百年後之祭祀活動」（「生前契約」10次、「79%」1次），支持其市占率敘述；惟「禮儀服務**占營收約60%**」未獲明確對應（「60%」3次之上下文未明確指涉該比例）。
- `5530:objective_ranking_or_market_share:eb56e880bb5d11f6` — `ACCEPTED`. 龍巖2024年官方簡報載「**生前契約市佔率**」與「**約79%**」，與 claim 之「龍巖生前契約市占率約79%」逐項對應。
- `4556:objective_ranking_or_market_share:9b2b2b95d0b2860e` — `PARTIALLY_SUPPORTED`. 旭然2015年官方簡報之客戶列載「旗勝科技、漢唐集成、群創光電、旭硝子、**台積電**、（…）」，並載「工業用**超純水**」與「**日月光**」（「過濾」25次），支持其過濾耗材業務及台積電、日月光等客戶；惟「**聯電**」（0次）與「台積電（**最大客戶群**）」（「最大客戶」0次）未獲支持。
- `2640:objective_ranking_or_market_share:aa3a18660be7ca86` — `PARTIALLY_SUPPORTED`. 大車隊2024年官方簡報中「**車隊**」出現6次，支持其計程車隊經營業務；惟「為台灣**市占率第一**的計程車隊」（「市占」「第一」均0次）、「約 **24,000** 名司機會員」與「約 **29,000** 輛營運車輛」（該二數字均0次）未獲支持。註記：該簡報文字擷取僅1,935字元。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）；UNKNOWN 追蹤清單維持 **134 筆**。
- Author-reviewed total: **605 / 1,399**; remaining: **794**. Outcome counts: ACCEPTED 77, PARTIALLY_SUPPORTED 390, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 134. Next pending claim by priority: `5292:objective_ranking_or_market_share:b7b5d29e96b2972f` (華懋).

## Author batch `author-102` — 2026-10-09

- Reviewed the next six unreviewed objective ranking/market-share claims in checkpoint order (華懋 5292, 潤隆 1808, 櫻花建 2539, 興富發 2542 ×3). Evidence came from directly downloaded and inspected official disclosures: 華懋2024年法人說明會簡報、潤隆2024年法人說明會簡報、櫻花建2024 Investor Conference（英文版）、興富發113年度年報。
- `5292:objective_ranking_or_market_share:b7b5d29e96b2972f` — `PARTIALLY_SUPPORTED`. 華懋2024年官方簡報載「（廢）物**VOCs污染防治系統**」「高科技**VOCs淨化設備**」「產業**VOCs廢氣處理**」（「VOCs」6次、「轉輪」5次），支持其 VOCs 廢氣處理設備業務；惟「**沸石**轉輪濃縮轉化系統」（「沸石」0次）、「（市佔率**高**）」（「市佔」0次）與「應用於半導體**黃光製程**」（「黃光」0次）未獲支持。
- `1808:objective_ranking_or_market_share:ee0f0ac169c03e89` — `PARTIALLY_SUPPORTED`. 潤隆官方簡報中「**完工**」出現3次、「2025」3次，支持其建案完工之敘述；惟「迎來**史上最大**完工**交屋**潮，營收與獲利成長可期」未獲支持（「最大」「交屋」均0次，亦未見營收獲利成長之對應預期）。
- `2539:objective_ranking_or_market_share:0660a4ba59fb2fd6` — `PARTIALLY_SUPPORTED`. 櫻花建2024年官方簡報（**英文版**）中「**Taichung**」出現18次，支持其營運地點；惟「成立於**1988年**」（「1988」0次）與「隸屬於**台灣最大推案機構寶佳機構**」（「largest」「Baujia」均0次）未獲支持；「由**林家宏**擔任董事長」則須註記——簡報載「Chairman and Spokesperson: **Mr. Chen, Shin-Ying**」，**所揭露之董事長姓名與 claim 不同**（「林家宏」0次）。
- `2542:objective_ranking_or_market_share:ca12741b0453c297` 與 `ed6d035d3884b395` — `PARTIALLY_SUPPORTED`. 興富發113年度年報中「**曹淵博**」出現18次，支持其經營團隊揭露；惟「成立於**1980年**」（0次）與「為**全台最大民營建商**之一」（「全台最大」「民營建商」均0次）未獲支持。**須特別註記：年報中「全球最大」之敘述係指其合作對象「全球最大連鎖酒店萬豪集團」，並非對興富發自身市場地位之描述（主詞錯置風險）。**
- `2542:objective_ranking_or_market_share:c259dca2ad8e1373` — `PARTIALLY_SUPPORTED`. 年報中「**齊裕營造**」出現11次（並載「集團子公司─齊裕營造工程收入」），支持其為集團子公司；惟「為**全國地下室挖掘量最大**」未獲支持（「地下室」0次）。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）；UNKNOWN 追蹤清單維持 **134 筆**。
- Author-reviewed total: **611 / 1,399**; remaining: **788**. Outcome counts: ACCEPTED 77, PARTIALLY_SUPPORTED 396, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 134. Next pending claim by priority: `2923:objective_ranking_or_market_share:2deccd89094eaab3` (鼎固-KY).

## Author batch `author-103` — 2026-10-09

- Reviewed the next seven unreviewed objective ranking/market-share claims in checkpoint order (鼎固-KY 2923, 森寶 3489, 信義 9940, 東哥遊艇 8478 ×3, 致茂 2360). Evidence came from directly downloaded and inspected official disclosures: 鼎固控股公司文件、森寶2025年法人說明會簡報、信義房屋2025年法人說明會簡報、東哥遊艇2026年法人說明會簡報、致茂114年度年報。
- `2923:objective_ranking_or_market_share:2deccd89094eaab3` — `PARTIALLY_SUPPORTED`. 鼎固官方文件中「**日月光**」出現59次，支持其與日月光集團之關係；惟「為**全球最大**半導體**封測**廠」未獲支持（「全球最大」與「封測」均0次，該地位屬第三人市場地位，本件未載）。
- `3489:objective_ranking_or_market_share:6f1e5cdcedde4c99` — `PARTIALLY_SUPPORTED`. 森寶2025年官方簡報中「**森碁**」出現2次、「營造」3次、「100%」2次，支持該子公司及持股關係；惟「**一條龍**」與「**垂直整合**」出現次數均為0。
- `9940:objective_ranking_or_market_share:103ba9aa17da7009` — `PARTIALLY_SUPPORTED`. 信義房屋2025年官方簡報載「註：**2024年10月店數為464家直營分店**」，支持其直營經營型態；惟「成立於**1987年**」（0次）與「為台灣**最大**房屋仲介品牌」（0次）未獲支持，且「全台擁有**超過500間**直營門市」與官方所載**464家**不符。
- `8478:objective_ranking_or_market_share:1d158029ffa49cb9` — `PARTIALLY_SUPPORTED`. 該 claim 之業務敘述以發行人官方簡報本身之來源身分為據（東哥企業之法說會簡報）；惟「**亞洲最大**」「**全球第三**」與「**Ocean**」出現次數均為0。
- `8478:objective_ranking_or_market_share:28a1bcd15fe9985b` 與 `803bb81e8eda9129` — `UNKNOWN_AFTER_RESEARCH`. 東哥官方簡報中「**MarineMax**」出現次數為0；且「**50%**」5次之上下文分別為「新廠貢獻**產能+50%**」「**回購率50%+**」與「2026-2027 市占率優於同業大幅成長」，**均非**經銷商占本公司營收之比例（數字脫離語意）；亦未取得 MarineMax 自身之官方文件。
- `2360:objective_ranking_or_market_share:1e49821a8cff17a7` — `PARTIALLY_SUPPORTED`. 致茂114年度年報中「**量測**」出現44次、「**自動化測試**」6次，支持其業務；惟「為**亞洲最大**之自動化測試與量測設備製造商」（0次）與「成立於**1984年**」（0次）未獲支持。註記：該年報**封面頁之文字層呈現亂碼**，其後頁面擷取正常。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。UNKNOWN 追蹤清單已同步刷新至 **136 筆**。
- Author-reviewed total: **618 / 1,399**; remaining: **781**. Outcome counts: ACCEPTED 77, PARTIALLY_SUPPORTED 401, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 136. Next pending claim by priority: `2423:objective_ranking_or_market_share:89e017344f0a4685` (固緯).

## Author batch `author-104` — 2026-10-09

- Reviewed the next eight unreviewed objective ranking/market-share claims in checkpoint order (固緯 2423 ×3, 德律 3030, 閎康 3587 ×2, 勤崴國際 6516, 泰藝 8289). Evidence came from directly downloaded and inspected official disclosures: 德律107年度年報、閎康IR Conference簡報（英文版）、勤崴國際115年股東常會議事錄、泰藝2025年法人說明會簡報。
- `2423:objective_ranking_or_market_share:89e017344f0a4685`、`ac4c5aacc850ead3` 與 `598bd6f5b3e719aa` — `UNKNOWN_AFTER_RESEARCH`. 本批次就固緯（2423）嘗試三個端點，**均未取得可檢視之文件**：(1) 官方網域 gwinstek.co.uk 之113年報端點——**SSL/TLS 憑證信任失敗**；(2) 官方網域 gwinstek.de 之同一文件端點——**同樣 SSL/TLS 憑證信任失敗**（含以略過憑證檢查方式重試後仍失敗）；(3) 公開資訊觀測站 t100 端點——所取得檔案**僅320 bytes**（擷取1字元，顯非完整文件）。
- `3030:objective_ranking_or_market_share:0bce561f06e3e4e6` — `PARTIALLY_SUPPORTED`. 德律107年度年報中「**AOI**」出現58次、「**自動光學**」12次、「全球」20次，支持其 AOI 設備業務；惟「為**台灣最大**的自動光學檢測設備廠商」（「台灣最大」「國內最大」均0次）與「**全球市佔率名列前茅**」未獲支持——「**市佔**」2次之上下文為「提升公司產品的全球**市佔率**」「進一步擴大**市佔**（率）」之**營運目標**敘述。
- `3587:objective_ranking_or_market_share:d51886a6ad107637` 與 `807d8b6094e488c5` — `PARTIALLY_SUPPORTED`. 閎康2024年官方簡報（**英文版**）載「**Kumamoto (MA)**」「Japan – National Project (Rapidus)」「Recent Major Chip Investments in Japan」（「Kumamoto」4次、「Japan」9次），支持其日本（含熊本）營運布局；惟「[[台積電]] — **最大客戶**」未獲支持（全份簡報中「**TSMC**」與「**largest**（customer）」之出現次數均為0）。
- `6516:objective_ranking_or_market_share:ee30bf28283d37f0` — `PARTIALLY_SUPPORTED`. 勤崴國際115年股東常會議事錄中「**電子地圖**」出現1次，支持該業務之存在；惟「在台灣電子地圖市場**超過七成**的絕對市佔率」（「七成」「市佔」均0次）、「為 **[[Google]] Maps** 在台灣的圖資合作夥伴」（「Google」0次）與「已成功轉型為智慧移動系統整合商」均未獲支持。註記：該文件為股東常會議事錄，資訊揭露型態與年報不同。
- `8289:objective_ranking_or_market_share:3e8264bf27a8e71f` — `PARTIALLY_SUPPORTED`. 泰藝2025年官方簡報中「**OCXO**」出現2次、「**衛星**」4次、「**5G**」2次，支持其 OCXO 產品與應用；惟「為台灣**唯一**具備 OCXO 技術之製造商」（「唯一」0次）與「將石英晶體置於**恆溫**槽中」（「恆溫」0次）未獲支持。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。UNKNOWN 追蹤清單已同步刷新至 **139 筆**（新增 `tls_failure` 分類）。
- Author-reviewed total: **626 / 1,399**; remaining: **773**. Outcome counts: ACCEPTED 77, PARTIALLY_SUPPORTED 406, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 139. Next pending claim by priority: `8289:objective_ranking_or_market_share:f64fe0dc9d652473` (泰藝).

## Author batch `author-105` — 2026-10-09

- Reviewed the next eight unreviewed objective ranking/market-share claims in checkpoint order (泰藝 8289, 慧友 5484 ×3, 中保科 9917, 順德 2351 ×2, 全新 2455). Evidence came from directly downloaded and inspected official disclosures: 泰藝2025年法人說明會簡報、中保科公司文件、順德2026年法人說明會簡報、全新光電2022年度年報（英文版）。
- `8289:objective_ranking_or_market_share:f64fe0dc9d652473` — `PARTIALLY_SUPPORTED`. 泰藝2025年官方簡報中「**石英**」2次、「**TCXO**」5次、「**VCXO**」3次、「**OCXO**」2次、「振盪器」8次，支持其石英振盪器之設計與製造；惟「**石英諧振器**」（「諧振器」0次，官方用語為「振盪器」）與「（台灣**唯一** OCXO 廠）」（「唯一」0次）未獲支持。
- `5484:objective_ranking_or_market_share:6db0feefd513243e`、`821685f1c25c5b71` 與 `ce6fd1fdc3f662bb` — `UNKNOWN_AFTER_RESEARCH`. 本批次自慧友官方網域之下載端點取得檔案時回應 **HTTP 403（禁止）**，未取得可檢視之官方文件。
- `9917:objective_ranking_or_market_share:1cb9babd3bf0854f` — `PARTIALLY_SUPPORTED`. 中保科官方文件載「（民國）**1977年11月**（…）」與「與**日本最大的SECOM公司合資技術合作**，正式成立了中興保全股（份有限公司）」（「保全」390次、「SECOM」14次），支持其成立年度與技術合作關係；惟「為**台灣最大**保全集團」未獲支持——「最大」14次之上下文包括「**最大宗**整合系統」「**美國最大**國際消費性電子展」「**全國最大**的安控產業教育訓練中（心）」與「日本SECOM為我方**最大股東之一**」，**均非**該表述。
- `2351:objective_ranking_or_market_share:33136b7be916bb4a` 與 `f9a2de7507ee264c` — `PARTIALLY_SUPPORTED`. 順德2026年官方簡報中「**導線架**」出現3次、「**功率**」2次，支持其導線架業務；惟「全球**前五大**導線架供應商」（「前五大」0次）與「全球**最大**的功率及分離式導線架製造商」（「全球最大」0次）未獲支持。
- `2455:objective_ranking_or_market_share:c7875bcac9220f55` — `PARTIALLY_SUPPORTED`. 全新2022年度年報中「**砷化鎵**」出現54次、「**磊晶**」29次、「**IQE**」3次，支持其砷化鎵磊晶業務；惟「為全球砷化鎵磊晶市場**領導者**」（「領導」0次）與「已**超越**英國 IQE 成為**全球最大**供應商」（「全球最大」0次；「IQE」3次之上下文為**同業列舉**「IQE 等」「IQE、IET-KY」）未獲支持。**註記：公開資訊觀測站之 t100 年報端點所取得檔案之文字層無法擷取（0字元），故改採發行人官方網域之英文版年報。**
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。UNKNOWN 追蹤清單已同步刷新至 **142 筆**。
- Author-reviewed total: **634 / 1,399**; remaining: **765**. Outcome counts: ACCEPTED 77, PARTIALLY_SUPPORTED 411, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 142. Next pending claim by priority: `2455:objective_ranking_or_market_share:0c9b77b516d1cc7d` (全新).

## Author batch `author-106` — 2026-10-09

- Reviewed the next five unreviewed objective ranking/market-share claims in checkpoint order (全新 2455 ×2, 嘉晶 3016, 弘塑 3131, 台勝科 3532). Evidence came from directly downloaded and inspected official disclosures: 全新光電2022年度年報（英文版）、嘉晶114年度年報、弘塑2024年法人說明會簡報、台勝科113年度營業報告書。
- `2455:objective_ranking_or_market_share:0c9b77b516d1cc7d` 與 `3efdbb27a667196e` — `PARTIALLY_SUPPORTED`. 全新2022年度年報中「**穩懋**」出現10次、「宏捷」多次，**惟該等上下文均將二者定位為「同業」**——例如「相較於台灣**同業宏捷與穩懋**產品以手機功率放大器(PA)、WLAN（用）」「綜觀目前國內上市櫃**同業公司宏捷與穩懋**亦提供晶圓代工製造生產服務」，另有數筆為**人員經歷**（如「穩懋半導體股份有限公司工程部經理」）。全份年報中「**最大客戶**」與「**營收占比**」出現次數均為0，「**28%**」5次之上下文為財務比率（如「增加148.28%」「0.28%」）而非客戶營收占比，「宏捷科」亦為0次。**故「穩懋為最大客戶、占營收約28%」未獲支持，且該二公司在官方文件中之定位為同業而非客戶。**
- `3016:objective_ranking_or_market_share:40c7fe6e149af7e4` — `PARTIALLY_SUPPORTED`. 嘉晶114年度年報中「**磊晶**」出現80次、「**漢磊**」32次、「**碳化矽**」9次、「**氮化鎵**」9次，支持其磊晶業務、集團歸屬及產品材料；惟「為台灣**唯一**能量產4吋及6吋碳化矽磊晶及6吋氮化鎵磊晶的廠商」未獲支持（「**唯一**」「**4吋**」「**6吋**」之出現次數均為0）。
- `3131:objective_ranking_or_market_share:9ac9f9c3666d39ed` — `PARTIALLY_SUPPORTED`. 弘塑2024年官方簡報中「**台積電**」出現1次、「**CoWoS**」3次、「**先進封裝**」2次，支持其先進封裝業務及與台積電之關聯；惟「台積電（**最大客戶**）」未獲支持（「最大客戶」0次）。
- `3532:objective_ranking_or_market_share:2d49a09b19587fc8` — `PARTIALLY_SUPPORTED`. 台勝科113年度營業報告書載其矽晶圓業務及與台塑集團、SUMCO 之關聯（「**矽晶圓**」13次、「**台塑**」3次、「**SUMCO**」2次）；惟「生產 **8 吋及 12 吋**矽晶圓」（0次）與「為台灣**最大**矽晶圓廠之一」（「最大」0次）未獲支持。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）；UNKNOWN 追蹤清單維持 **142 筆**。
- Author-reviewed total: **639 / 1,399**; remaining: **760**. Outcome counts: ACCEPTED 77, PARTIALLY_SUPPORTED 416, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 142. Next pending claim by priority: `3189:objective_ranking_or_market_share:d30c008603686d3a` (景碩).

## Author batch `author-107` — 2026-10-09

- Reviewed the next eight unreviewed objective ranking/market-share claims in checkpoint order (景碩 3189, 京鼎 3413, 世禾 3551, 牧德 3563, 全訊 5222 ×2, 笙科 5272, 中美晶 5483). Evidence came from directly downloaded and inspected official disclosures: 全訊114年度年報、中美晶110年度年報。
- `3189:objective_ranking_or_market_share:d30c008603686d3a` — `UNKNOWN_AFTER_RESEARCH`. 景碩官方網域之年報端點（114年度與112年度）回應 **HTTP 401（未經授權）**，未取得可檢視之檔案。
- `3413:objective_ranking_or_market_share:ebe2223d339ab310` — `UNKNOWN_AFTER_RESEARCH`. 京鼎之公開資訊觀測站簡報端點回應 **HTTP 404**。
- `3551:objective_ranking_or_market_share:21c365ea8b4c5152` — `UNKNOWN_AFTER_RESEARCH`. 世禾2025年官方簡報中「**台積電**」出現次數為0（「營收」5次、「清洗」3次支持其設備清洗業務，惟未具名客戶）；「最大」2次為「最大限度地發揮」「達到最大的利益」等泛用語，故該具名客戶之營收貢獻未獲確立。
- `3563:objective_ranking_or_market_share:678d0af119707979` — `UNKNOWN_AFTER_RESEARCH`. 牧德官方網域之法人說明會簡報端點**連線中斷**（「要求已經中止: 連接意外關閉」），未取得可檢視之檔案。
- `5222:objective_ranking_or_market_share:dbde28318bead583` — `PARTIALLY_SUPPORTED`. 全訊114年度年報載「本公司自 **1998 年成立**以來，從設立半導體廠房、開發 pHEMT 元件積體電路製程…」與「砷化鎵及**氮化鎵**元件係無線通訊產業之關鍵性零組件…**化合物半導體**已成為…重要功率元件」（「氮化鎵」10次、「化合物」4次），支持其成立年度與製程；惟「是台灣**唯一**專精於化合物半導體製程的整合元件製造廠（IDM）」未獲支持（「唯一」0次）。
- `5222:objective_ranking_or_market_share:ac86f330feeaa01a` — `PARTIALLY_SUPPORTED`. 年報中「**雷達**」出現32次、「**飛彈**」4次，支持其功率放大器之國防應用；惟「**最大客戶**」（0次）與「佔營收比重…曾達 **8成**」（0次）未獲支持。
- `5272:objective_ranking_or_market_share:5a22c41a58004d2c` — `UNKNOWN_AFTER_RESEARCH`. 笙科官方網域之民國102年度年報（6.8 MB）之**文字層僅能擷取3,559字元**（封面與發言人頁等），實質業務敘述無法擷取；「SRD」「LNB」「聯笙」「RF IC」與「唯一」之出現次數均為0。
- `5483:objective_ranking_or_market_share:f9ec0490463350f9` — `PARTIALLY_SUPPORTED`. 中美晶110年度年報中「**矽晶圓**」53次、「**太陽能**」139次、「**藍寶石**」6次，支持其三大事業架構；惟「為台灣**最大**的矽晶圓供應商」（「台灣最大」0次；「最大」7次為「解決最大的土地限制因素」「追求組織最大利益」「為其單一最大股東」「代表最大信用暴險金額」等泛用語）與「**3 吋至 12 吋**矽晶圓」（「3吋」「12吋」均0次）未獲支持。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。UNKNOWN 追蹤清單已同步刷新至 **147 筆**。
- Author-reviewed total: **647 / 1,399**; remaining: **752**. Outcome counts: ACCEPTED 77, PARTIALLY_SUPPORTED 419, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 147. Next pending claim by priority: `5483:objective_ranking_or_market_share:330863256f88c588` (中美晶).

## Author batch `author-108` — 2026-10-09

- Reviewed the next eight unreviewed objective ranking/market-share claims in checkpoint order (中美晶 5483, 頎邦 6147 ×3, 久元 6261, 瑞耘 6532 ×2, 晶心科 6533). Evidence came from directly downloaded and inspected official disclosures: 中美晶110年度年報、頎邦110年度年報、久元112年度年報、瑞耘113年度年報、晶心科114年股東常會議事手冊。
- `5483:objective_ranking_or_market_share:330863256f88c588` — `PARTIALLY_SUPPORTED`. 中美晶110年度年報中「**矽晶圓**」出現53次，支持其矽晶棒／矽晶圓業務；惟「**3-12吋**」（「3吋」「12吋」均0次）與「（**台灣最大**）」（0次，且「最大」7次為泛用語）未獲支持。
- `6147:objective_ranking_or_market_share:b5110c677f121bef`、`55e95765fe157fbc` 與 `6bdc058d1011e062` — `PARTIALLY_SUPPORTED`. 頎邦110年度年報中「**驅動IC**」出現8次、「**凸塊**」13次、「**COF**」5次、「**COG**」5次，支持其驅動 IC 封裝及 COF／COG／凸塊業務；惟「是**全球最大**的驅動 IC 封裝廠」（0次）、「全球市占率約 **50%**」（「50%」9次之上下文為「削減50%（逐年減少10%）」「50% 提升至75%」與財務比率「25.50%」等，**非市占率**）與「**南茂**」（0次）未獲支持。
- `6261:objective_ranking_or_market_share:37228631f06f5ce4` — `UNKNOWN_AFTER_RESEARCH`. 久元112年度年報中「**晶元**」出現次數為**0**（「客戶」108次、「光電」36次均為通稱或其他公司），「**最大客戶**」與「**占營收**」亦均為0，故「晶元光電（最大客戶，占營收23.5%）」未獲確立。
- `6532:objective_ranking_or_market_share:9f3fc56944fd9568` — `PARTIALLY_SUPPORTED`. 瑞耘113年度年報載「瑞耘科技以 **OEM** 為主要的經營模式…」「本公司銷貨客戶集中在半導體產業，透過 **OEM** 合作模式直接接單或代理商（…）」（「OEM」4次），並見「**晶圓旋乾**」3次與「SRD」2次，支持其 OEM 模式與濕式製程設備；惟「打入全球最大半導體設備龍頭**應用材料（Applied Materials）**的原廠供應鏈」（「應用材料」「Applied Materials」均0次；「Applied」2次之一為「Applied Physics A 學術期刊」）與「長達**十數年**」未獲支持。
- `6532:objective_ranking_or_market_share:7e0ba7530f386152` — `UNKNOWN_AFTER_RESEARCH`. 瑞耘113年度年報中「**應用材料**」「**Applied Materials**」「**台積電**」「**日月光**」「**最大客戶**」與「**六成**」之出現次數**均為0**，未具名該等客戶或載其營收占比。
- `6533:objective_ranking_or_market_share:de4c47986928bfbe` — `UNKNOWN_AFTER_RESEARCH`. 本批次自晶心科官方網域取得之文件為**114年股東常會議事手冊**（開會程序、議程、議案等），資訊揭露型態與年報不同；「**Meta**」「MTIA」「**聯發科**」「**聯詠**」與「Renesas」之出現次數**均為0**，未載客戶或授權對象敘述。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。UNKNOWN 追蹤清單已同步刷新至 **150 筆**。
- Author-reviewed total: **655 / 1,399**; remaining: **744**. Outcome counts: ACCEPTED 77, PARTIALLY_SUPPORTED 424, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 150. Next pending claim by priority: `6830:objective_ranking_or_market_share:f1578b23f3b713fe` (汎銓).

## Author batch `author-109` — 2026-10-09

- Reviewed the next four unreviewed objective ranking/market-share claims in checkpoint order (汎銓 6830 ×2, 昇陽半導體 8028 ×2). Evidence came from directly downloaded and inspected official disclosures: 汎銓2024年永續報告書、昇陽半導體2023年永續報告書。
- `6830:objective_ranking_or_market_share:f1578b23f3b713fe` — `PARTIALLY_SUPPORTED`. 汎銓2024年永續報告書載「鼓勵員工激發產能，進一步提升汎銓科技整體競爭力，**展現在高科技檢測領域中的領導地位**」，並見「**材料分析**」24次、「**TEM**」9次、「FIB」2次、「先進製程」11次，支持其材料分析業務與檢測領域領導地位之敘述；惟「全球先進製程材料分析市占率**超過50%**」未獲支持——全份報告書中「**市占**」與「超過50」均為0次，且「**50%**」1次之上下文為「朝2025年前**節能50%**的目標邁進」，**非市占率**。
- `6830:objective_ranking_or_market_share:261e22e52765eec0` — `PARTIALLY_SUPPORTED`. 本 claim 為同一事實之條目表述（「汎銓（TEM/FIB 材料分析，全球市占 50%+）」）。報告書支持其 TEM／FIB 材料分析業務；惟「全球市占 50%+」未獲支持（「市占」0次；「50%」為節能目標）。
- `8028:objective_ranking_or_market_share:36af13fbf6f495ec` — `PARTIALLY_SUPPORTED`. 昇陽半導體2023年永續報告書中「**晶圓再生**」出現10次，支持其晶圓再生業務；惟「為**台灣最大**的矽晶圓再生廠之一」未獲支持——「**最大**」4次之上下文為「盡**最大**努力與責任」「廠內**最大宗**廢棄物」「達到資源再利用**最大**化」等泛用語；「主要客戶為**台積電**等晶圓代工廠」亦未獲支持（「**台積電**」0次）。
- `8028:objective_ranking_or_market_share:6f62e2054fe7535b` — `UNKNOWN_AFTER_RESEARCH`. 昇陽半導體2023年永續報告書中「**台積電**」出現次數為0，未具名該客戶，依具名客戶身分規則以 UNKNOWN 結案。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。UNKNOWN 追蹤清單已同步刷新至 **151 筆**。
- Author-reviewed total: **659 / 1,399**; remaining: **740**. Outcome counts: ACCEPTED 77, PARTIALLY_SUPPORTED 427, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 151. Next pending claim by priority: `2330:objective_ranking_or_market_share:69b238d963f6d1c7` (台積電).

## Author batch `author-110` — 2026-10-09

- Reviewed the next four unreviewed objective ranking/market-share claims in checkpoint order (台積電 2330, 旺宏 2337, 茂矽 2342, 瑞昱 2379). Evidence came from directly downloaded and inspected official disclosures: 旺宏2023年永續報告書、茂矽公司文件、瑞昱2024 Annual Report（英文版）。
- `2330:objective_ranking_or_market_share:69b238d963f6d1c7` — `UNKNOWN_AFTER_RESEARCH`. 本批次就台積電嘗試**四個官方端點**（investor.tsmc.com 之2024年報 PDF、年報索引頁、Business Overview PDF、年報電子書頁面 HTML，並已附加一般瀏覽器 User-Agent），**均回應 HTTP 403（禁止）**；該網域對自動化請求採取封鎖措施，本批次未能取得可檢視之官方文件。
- `2337:objective_ranking_or_market_share:53d3a9c34ff6edb7` — `PARTIALLY_SUPPORTED`. 旺宏2023年永續報告書載「**ROM** 唯讀記憶體、**NOR** 型快閃記憶體以及NAND 型快閃記憶體解決方（案）」（「NOR」35次、「ROM」10次、「車用」12次），支持其產品線與應用；惟「在 ROM 市場為**全球最大**供應商」（「全球最大」0次；「最大」4次為獎項與產品名稱）、「主要受惠於 **Nintendo** 遊戲機」（「任天堂」「Nintendo」均0次）與「車用及工業用 NOR Flash 市場也居**全球領先地位**」（「領先」3次之上下文為「領先發表全球首篇Flash 前瞻技術之3D NOR論文」「領先國內業界投保董事責任保險」「領先業界興建設備最齊全（的）」）均未獲支持。
- `2342:objective_ranking_or_market_share:b2bd16648dd7b771` — `PARTIALLY_SUPPORTED`. 茂矽官方文件載「註1:**朋程科技股份有限公司**於民國112年6月2日**取得本公司之控制力**，成為（本公司之母公司）」（「朋程」12次），顯示朋程為茂矽之控制股東／母公司；惟「（車用整流二極體模組，**最大客戶**）」未獲支持（「最大客戶」「整流二極體」「車用」均0次）。**須特別註記：本件所揭露之朋程角色為「取得控制力」之母公司／控制股東，而非客戶（關係角色錯置）。**
- `2379:objective_ranking_or_market_share:c21c8f86d0573984` — `PARTIALLY_SUPPORTED`. 瑞昱2024年報（**英文版**）中「**Ethernet**」50次、「**Audio**」77次、「**Wi-Fi**」37次、「**Bluetooth**」36次、「market share」14次、「leading」21次（含「leading market share」），支持其產品線與市場地位敘述；惟「Audio Codec（**PC 音效晶片市佔極高**）」未見以 PC 音效晶片為對象之市占率專述。**方法論註記：本件為英文版文件，以中文關鍵字檢索不具意義。**
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。UNKNOWN 追蹤清單已同步刷新至 **152 筆**。
- Author-reviewed total: **663 / 1,399**; remaining: **736**. Outcome counts: ACCEPTED 77, PARTIALLY_SUPPORTED 430, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 152. Next pending claim by priority: `2408:objective_ranking_or_market_share:c4377f2679307d07` (南亞科).

## Author batch `author-111` — 2026-10-09

- Reviewed the next five unreviewed objective ranking/market-share claims in checkpoint order (南亞科 2408, 偉詮電 2436, 京元電子 2449, 聯發科 2454 ×2). Evidence came from directly downloaded and inspected official disclosures: 南亞科年報、偉詮電3Q25法人說明會簡報、京元電子113年度年報、聯發科2025 Annual Report（英文版）。
- `2408:objective_ranking_or_market_share:c4377f2679307d07` — `PARTIALLY_SUPPORTED`. 南亞科年報中「**DRAM**」出現77次、「全球」36次，支持其 DRAM 製造業務；惟「是台灣**最大**的 DRAM 製造商」（「台灣最大」0次）與「也是**全球第四大** DRAM 廠」（「第四大」0次）未獲支持。
- `2436:objective_ranking_or_market_share:57909ce03d931541` — `PARTIALLY_SUPPORTED`. 偉詮電2025年12月官方簡報中「**USB PD**」出現4次、「USB」17次、「電源管理」3次、「筆電」1次、「充電器」1次，支持其產品線與應用；惟「在 USB PD 控制器領域**市佔率極高**」（「市佔」0次）與「**遊戲機**適配器」（0次）未獲支持。
- `2449:objective_ranking_or_market_share:fea783f1ad9c465a` — `PARTIALLY_SUPPORTED`. 京元電子113年度年報中「**測試**」出現108次、「**封裝**」36次、「**burn-in**」9次、「**預燒**」7次，支持其服務範疇；惟「是台灣**最大**的**獨立**半導體測試服務廠商」未獲支持（「**台灣最大**」0次；「**獨立**」137次之上下文包含「獨立董事」與「獨立整合元件製造廠(IDM)委外測試」等）。
- `2454:objective_ranking_or_market_share:f41e65769c42213b` — `PARTIALLY_SUPPORTED`. 聯發科2025年報（**英文版**）中「**AI**」出現944次、「**5G**」15次、「leading」17次，支持其 AI 與 5G 產品線；惟「在 5G 手機晶片**市占率位居全球前二**」未獲支持——「**market share**」7次之上下文為連網技術、車用與旗艦機種之市占成長敘述（「second」17次之上下文多為「second degree of kinship」等親屬關係）。
- `2454:objective_ranking_or_market_share:5905335fb55488f0` — `PARTIALLY_SUPPORTED`. 年報載「tape out of its flagship SoC using **TSMC's 2nm process** in 2025」（「**TSMC**」7次、「foundry」4次），支持其與台積電之合作；惟「（**最大供應商**）」未獲支持（「**largest supplier**」0次）。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）；UNKNOWN 追蹤清單維持 **152 筆**。
- Author-reviewed total: **668 / 1,399**; remaining: **731**. Outcome counts: ACCEPTED 77, PARTIALLY_SUPPORTED 435, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 152. Next pending claim by priority: `2458:objective_ranking_or_market_share:16cff6fcb439c815` (義隆).

## Author batch `author-112` — 2026-10-09

- Reviewed the next eight unreviewed objective ranking/market-share claims in checkpoint order (義隆 2458 ×2, 聯陽 3014 ×2, 聯詠 3034, 穩懋 3105 ×2, 晶宏 3141). Evidence came from directly downloaded and inspected official disclosures: 義隆110年度年報、聯陽115年股東常會議事手冊、聯詠法人說明會新聞稿、晶宏2022年度年報。
- `2458:objective_ranking_or_market_share:16cff6fcb439c815` 與 `c5189d74c609f774` — `PARTIALLY_SUPPORTED`. 義隆110年度年報載「目前在**筆電**的零配件中**觸控板**模組、觸控螢幕晶片（…）」（「觸控板」6次、「車用」3次），支持其產品線與車用布局；惟「在全球筆電觸控板市場**市佔率第一**」未獲支持——「**市佔**」4次之上下文**均為目標或趨勢敘述**（「市佔率能有效鞏固及提升」「短期：提升既有產品的市佔率」「提前搶佔市佔率」），「**第一**」7次之上下文為「COVID-19疫苗第一劑接種率」「一一五年第一季業績展望」等；「AI PC」亦為0次。
- `3014:objective_ranking_or_market_share:43a2413ceb931801` 與 `6d9b204267d9ed3f` — `PARTIALLY_SUPPORTED`. 聯陽115年股東常會議事手冊中「**聯華**」出現6次，支持其與聯華電子集團之關係；惟「Super I/O」「EC」「嵌入式」「控制晶片」「IC設計」與「市占」之出現次數**均為0**，故「全球 Super I/O（市占45-50%）及筆電 EC（市占35-40%）領導廠商」與「全球市占率領先」未獲確立。註記：該文件為股東常會議事手冊。
- `3034:objective_ranking_or_market_share:36d59c043f9f3ce8` — `UNKNOWN_AFTER_RESEARCH`. 本批次所取得之聯詠官方文件為**法人說明會新聞稿**（內容以114年自結合併財務數字為主），**未載產品線市占率或客戶結構之業務敘述**，故「大尺寸面板驅動 IC 市佔率全球領先」未獲確立。
- `3105:objective_ranking_or_market_share:d03113074c1b8d2c` 與 `c33bbc30d1e971dd` — `UNKNOWN_AFTER_RESEARCH`. 穩懋官方網域之端點回應 **SSL/TLS 憑證信任失敗**，未取得可檢視之檔案。
- `3141:objective_ranking_or_market_share:84f650c3f04863f8` — `PARTIALLY_SUPPORTED`. 晶宏2022年度年報中「**電子貨架標籤**」出現4次、「**ESL**」6次，支持其 ESL 驅動晶片業務；惟「是**全球**…**龍頭**，市占率達 **55%**」未獲支持——「**55%**」5次之上下文**均為百分比區間**（「0.52%~2.55%」「0.55%～0.61%」「1.00%～1.55%」），**非市占率**；「元太」亦未見於可檢索文字。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。UNKNOWN 追蹤清單已同步刷新至 **155 筆**。
- Author-reviewed total: **676 / 1,399**; remaining: **723**. Outcome counts: ACCEPTED 77, PARTIALLY_SUPPORTED 440, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 155. Next pending claim by priority: `3141:objective_ranking_or_market_share:65a03ef2f2732bd5` (晶宏).

## Author batch `author-113` — 2026-10-09

- Reviewed the next eight unreviewed objective ranking/market-share claims in checkpoint order (晶宏 3141 ×2, 原相 3227, 欣銓 3264 ×2, 創意 3443, 聚積 3527 ×2). Evidence came from directly downloaded and inspected official disclosures: 晶宏2022年度年報、欣銓111年度年報、創意電子氣候相關財務揭露報告書、聚積112年股東常會議事手冊。
- `3141:objective_ranking_or_market_share:65a03ef2f2732bd5` 與 `76eab7724d46fd0c` — `UNKNOWN_AFTER_RESEARCH`. 晶宏2022年度年報中「**元太**」出現次數為**0**、「**最大客戶**」為0；「**E Ink**」1次之上下文為「成功開發搭配 **E Ink Spectra 3100** 四色電子標籤 IC」，係指**電子紙技術規格名稱**而非客戶；「**母公司**」158次之上下文多為財務報表用語（如「歸屬於**母公司**業主之權益」），未載元太為其母公司。
- `3227:objective_ranking_or_market_share:9484acc8041462d9` — `UNKNOWN_AFTER_RESEARCH`. 原相官方網域之年報端點所取得之檔案**僅111 bytes**，PDF 解析回應「no objects found / Failed to open file as type pdf」，**顯非 PDF 文件**，故不予採用。
- `3264:objective_ranking_or_market_share:60de4d8a051579fe` 與 `067c7811d5d64930` — `UNKNOWN_AFTER_RESEARCH`. 欣銓111年度年報之**文字層呈現亂碼**（如「΋ǵวقΓǵж౛วقΓۉӜǵᙍᆀǵᖄ๎ႝ」等非可讀字元，與台光電2023年報、上洋114年報、必應111年報、峰源113年報同型之檢索限制），以關鍵字檢索「車用」「測試」「MCU」「市占」與「前三大」之出現次數均為0。
- `3443:objective_ranking_or_market_share:0e18f8dc0286575f` — `UNKNOWN_AFTER_RESEARCH`. 本批次自發行人官方網域所取得之文件經檢視後為「**2022 創意電子氣候相關財務揭露報告書**」（TCFD 報告書），**資訊揭露型態與年報不同**，未載 ASIC 設計服務之市場地位或股東結構（「台積電」與「最大股東」皆為0次）。
- `3527:objective_ranking_or_market_share:8eb795fd7f9d812e` — `PARTIALLY_SUPPORTED`. 聚積112年股東常會議事手冊載「（本公司）的積體驅動電路，為**全球第一大顯示屏LED 驅動IC 廠**」（「LED」45次、「驅動IC」4次），並見「Mini」6次、「Micro」3次，支持其全球第一地位與 Mini／Micro LED 產品發展；惟「及**物聯網精準行銷系統**」未獲支持。
- `3527:objective_ranking_or_market_share:39a26c1aea2cd59c` — `ACCEPTED`. 議事手冊載「為**全球第一大顯示屏LED 驅動IC 廠**」，與 claim 之「聚積（全球第一大 LED 顯示屏驅動 IC）」逐項對應。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。UNKNOWN 追蹤清單已同步刷新至 **161 筆**。
- Author-reviewed total: **684 / 1,399**; remaining: **715**. Outcome counts: ACCEPTED 78, PARTIALLY_SUPPORTED 441, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 161. Next pending claim by priority: `3545:objective_ranking_or_market_share:3863a18a0b35d83b` (敦泰).

## Author batch `author-114` — 2026-10-09

- Reviewed the next eight unreviewed objective ranking/market-share claims in checkpoint order (敦泰 3545 ×2, 逸昌 3567, 辛耘 3583 ×2, 世芯-KY 3661, 家登 3680 ×2). Evidence came from directly downloaded and inspected official disclosures: 敦泰2024年度年報、辛耘2025年度年報、逸昌112年度年報、世芯年報、家登公司文件。
- `3545:objective_ranking_or_market_share:3863a18a0b35d83b` 與 `b0c570c3eee08a0b` — `ACCEPTED`. 敦泰2024年度年報載「（本公司）**觸控IC** 年度出貨逾4億顆，成為**全球最大觸控IC 供應商**」，並見「**電容式**」15次、「**顯示驅動**」17次、「觸控IC」14次、「**指紋**」68次、「TDDI」2次，與 claim 之「全球最大電容式觸控 IC 出貨商之一」及產品線（觸控 IC、顯示驅動 IC、TDDI 及指紋辨識 IC）逐項對應。
- `3567:objective_ranking_or_market_share:771daad65f7afad8` — `PARTIALLY_SUPPORTED`. 逸昌112年度年報中「**類比**」66次、「**混合訊號**」6次、「**晶圓測試**」16次、「**100%**」3次，支持其專注類比及混合訊號 IC 測試之業務；惟「是台灣**第一家**100% 專注…」（「**第一家**」0次）與服務項目中之「**晶圓雷射修整**」「**捲帶包裝**」（均0次）未獲支持。
- `3583:objective_ranking_or_market_share:d01d05af66a35f62` — `PARTIALLY_SUPPORTED`. 辛耘2025年度年報中「**濕式**」5次、「**矽晶圓再生**」2次，支持其濕式製程設備及矽晶圓再生業務；惟「12吋矽晶圓再生服務為**國內最大**」、「月產能**16萬片**」（0次）與「製程至**16nm**」（0次）未獲支持。
- `3583:objective_ranking_or_market_share:9f4f88d12436b18e` — `UNKNOWN_AFTER_RESEARCH`. 辛耘年報中「**最大客戶**」與「**19.37**」之出現次數均為0；「**台積電**」9次之上下文包含**人員經歷**（「台積電採購副理」）與產業敘述（「製造商如台積電、三星和英特爾將進入2奈米量產階段」），**非**客戶關係或營收占比之表述。
- `3661:objective_ranking_or_market_share:3565731645cc816a` — `PARTIALLY_SUPPORTED`. 世芯年報中「**ASIC**」84次、「**先進製程**」4次、「**台積電**」3次，支持其 ASIC 設計服務及與台積電之先進製程合作；惟「（先進製程**唯一夥伴**）」未獲支持（「**唯一**」0次）。
- `3680:objective_ranking_or_market_share:6827b5060d58507e` 與 `7bf17ffbe1bd9dda` — `PARTIALLY_SUPPORTED`. 家登公司文件中「**EUV**」1次、「**FOUP**」4次，支持其 EUV 光罩盒與 FOUP 晶圓載具業務；惟「全球極少數獲得 **ASML** 認證」（「ASML」0次）、「全球先進製程市佔率超過 **80%**」（0次）與「市佔率目標 **50%** 以上」（0次）未獲支持。註記：該檔案文字擷取僅3,381字元，可能為年報之部分章節。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。UNKNOWN 追蹤清單已同步刷新至 **162 筆**。
- Author-reviewed total: **692 / 1,399**; remaining: **707**. Outcome counts: ACCEPTED 80, PARTIALLY_SUPPORTED 446, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 162. Next pending claim by priority: `3680:objective_ranking_or_market_share:c865bf5112c73bab` (家登).

## Author batch `author-115` — 2026-10-09

- Reviewed the next five unreviewed objective ranking/market-share claims in checkpoint order (家登 3680, 漢磊 3707, 日月光投控 3711 ×3). Evidence came from directly downloaded and inspected official disclosures: 家登完整年報、漢磊2024年永續報告書、日月光投控2024營運模式文件。
- `3680:objective_ranking_or_market_share:c865bf5112c73bab` — `PARTIALLY_SUPPORTED`. 家登**完整年報**（文字擷取235,590字元）載「（本公司）**全球微影設備大廠ASML 認證，成為全球唯二家經ASML 認證之**（廠商）」，並見「**台積電**」14次、「**Intel**」3次、「**ASML**」4次、「**EUV**」23次，支持其與該等廠商之業務關係；惟「台積電（**最大客戶**）」（全份年報中0次）、「營收佔比 **>50%**」（「50%」25次之上下文多為財務比率與持股比例）與「**Samsung／三星**」（0次）未獲支持。**註記：本批次另取得該公司完整年報；先前批次（author-114）僅取得該公司文件之部分章節（3,381字元）。**
- `3707:objective_ranking_or_market_share:13a1c75c5f1b260d` — `PARTIALLY_SUPPORTED`. 漢磊2024年永續報告書中「**化合物**」出現23次、「**碳化矽**」9次、「**氮化鎵**」7次、「**專業代工**」2次，支持其轉型化合物半導體專業代工廠並專注碳化矽及氮化鎵功率半導體；惟「為**全球第一家 Sub-micron Bipolar／BiCMOS** 專業代工廠」未獲支持（「**Sub-micron**」與「**BiCMOS**」均0次）。
- `3711:objective_ranking_or_market_share:c038454aa18420d4`、`4d7b58600a93fb56` 與 `f3500d5d502f4ad0` — `UNKNOWN_AFTER_RESEARCH`. 本批次自日月光投控官方網域所取得之「2024 營運模式」文件，經 PDF 文字擷取後**僅得4頁、內容極為有限**（可能以圖形排版為主），未載全球封測市占率、排名或客戶結構之敘述。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。UNKNOWN 追蹤清單已同步刷新至 **165 筆**。
- Author-reviewed total: **697 / 1,399**; remaining: **702**. Outcome counts: ACCEPTED 80, PARTIALLY_SUPPORTED 448, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 165. Next pending claim by priority: `4966:objective_ranking_or_market_share:c9c039a42c112b9a` (譜瑞-KY).

## Author batch `author-116` — 2026-10-09

- Reviewed the next three unreviewed objective ranking/market-share claims in checkpoint order (譜瑞-KY 4966, 凌陽創新 5236, 智晶 5245). Evidence came from directly downloaded and inspected official disclosures: 譜瑞-KY2019年度年報（中文版）、凌陽創新113年度年報、智晶光電法人說明會簡報。
- `4966:objective_ranking_or_market_share:c9c039a42c112b9a` — `PARTIALLY_SUPPORTED`. 譜瑞2019年度年報中「**eDP**」出現67次、「**TCON**」48次、「**Touch**」49次、「T-CON」3次，支持其 eDP T-CON、高速介面 IC 及觸控 IC 之產品線；惟「**最大客戶**（貢獻營收約 **40-50%**）」未獲支持（全份年報中未見「最大客戶」，亦未見該客戶營收占比敘述）。
- `5236:objective_ranking_or_market_share:f457de3e9c8982f8` — `PARTIALLY_SUPPORTED`. 凌陽創新113年度年報中「**網路攝影機**」出現18次、「**Webcam**」5次、「滑鼠」1次、「鍵盤」1次，支持其產品線；惟「（**全球市佔率領先**）」未獲支持——「**市佔**」僅出現1次，其上下文為**目標敘述**「之要求，引領市場需求，**擴大市佔率**進而增加（…）」。
- `5245:objective_ranking_or_market_share:a910f6713c84621f` — `UNKNOWN_AFTER_RESEARCH`. 所取得之智晶官方簡報文字擷取僅5,079字元（以圖形排版為主），「**PMOLED**」「**信利**」「**市占**」與「**領導**」之出現次數均為0，未載 PMOLED 之市場地位或市占率敘述。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。UNKNOWN 追蹤清單已同步刷新至 **166 筆**。
- Author-reviewed total: **700 / 1,399**; remaining: **699**. Outcome counts: ACCEPTED 80, PARTIALLY_SUPPORTED 450, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 166. Next pending claim by priority: `5262:objective_ranking_or_market_share:f119d6b2ee83a82c` (立達).

## Author batch `author-117` — 2026-10-09

- Reviewed the next five unreviewed objective ranking/market-share claims in checkpoint order (立達 5262, 信驊 5274, 松翰 5471, 盛群 6202, 驊訊 6237). Evidence came from directly downloaded and inspected official disclosures: 立達公司文件、信驊2024年第四季法人說明會簡報、松翰2024年度年報、盛群2025年度年報、驊訊相關文件（**證券商網站彙編，source_level 2**）。
- `5262:objective_ranking_or_market_share:f119d6b2ee83a82c` — `PARTIALLY_SUPPORTED`. 立達文件載「立達公司積極拓展全球銷售通路，…並於同年**上架 Amazon** 與中國最大網購通路『京東商城』」（「通路」5次、「Amazon」1次），支持其以 Amazon 為銷售通路；惟「[[Amazon]]（**全球最大客戶**）」（0次）與「**[[Costco]]**、美國實體零售商」（「Costco」0次）未獲支持。
- `5274:objective_ranking_or_market_share:0273091c5ede01d3` — `PARTIALLY_SUPPORTED`. 信驊2024年第四季官方簡報載「• **拿下BMC市佔率第一**」（「**BMC**」24次），與 claim 之「全球 BMC 市場龍頭」對應；惟「市佔率**高達 70% 以上**」未獲支持（「**70%**」與「**龍頭**」均0次）。
- `5471:objective_ranking_or_market_share:15c0951019aab7a5` — `PARTIALLY_SUPPORTED`. 松翰2024年度年報中「**血壓計**」3次、「**耳溫槍**」1次、「**車用**」8次、「**攝影機**」11次、「USB」8次，支持其醫療健康量測與車用電子之拓展；惟「在 USB 視訊攝影機控制晶片市場佔有**高市佔率**」未獲支持（「**視訊攝影機**」與「**高市佔**」均0次）。
- `6202:objective_ranking_or_market_share:5eb42ab1bfebd2f0` — `PARTIALLY_SUPPORTED`. 盛群2025年度年報中「**MCU**」出現146次、「**ASIC**」4次、「**中國**」25次，支持其雙軌業務模式與市場布局；惟「在中國等新興市場擁有**極高市佔率**」未獲支持（「**市佔**」0次）。
- `6237:objective_ranking_or_market_share:ea961f6789113b61` — `PARTIALLY_SUPPORTED`. 文件支持其 PCI／USB 介面音效晶片業務（「**USB**」515次、「PCI」8次、「**音效晶片**」8次、「筆電」41次）；惟「過去在個人電腦與筆電音效晶片市場擁有**極高市佔率**」未獲支持——「**市佔**」11次之上下文多係指**其他公司**（如「B 公司」「該公司」「全球主要PC大廠」）。**須註記本件之來源層級**：該文件係自**證券商網站**下載之文件彙編（非發行人自身官方網域之申報文件），依政策屬間接來源，本件僅用於產品線之佐證，市場地位之斷言不予採認。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）；UNKNOWN 追蹤清單維持 **166 筆**。
- Author-reviewed total: **705 / 1,399**; remaining: **694**. Outcome counts: ACCEPTED 80, PARTIALLY_SUPPORTED 455, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 166. Next pending claim by priority: `6239:objective_ranking_or_market_share:1ef7e877642549e6` (力成).

## Author batch `author-118` — 2026-10-09

- Reviewed the next five unreviewed objective ranking/market-share claims in checkpoint order (力成 6239 ×2, 台表科 6278, 晶焱 6411 ×2). Evidence came from directly downloaded and inspected official disclosures: 力成114年度年報、台表科113年度年報（英文版）、晶焱2023年永續報告書。
- `6239:objective_ranking_or_market_share:1ef7e877642549e6` — `PARTIALLY_SUPPORTED`. 力成114年度年報中「**封裝**」出現165次、「**測試**」85次、「**記憶體**」29次，支持其記憶體封測業務；惟「是全球**前五大**」（0次）與「全球『**最大**』的記憶體半導體封裝測試廠」未獲支持——「**最大**」3次之上下文為「發揮專利保護之**最大**效用」「**最大**利基」「員工的健康是企業**最大**的財富」等**泛用語**。
- `6239:objective_ranking_or_market_share:91405f2a46c49ae7` — `PARTIALLY_SUPPORTED`. 年報中「**金士頓**」出現28次、「**美光**」4次、「**Kioxia**」3次、「SK」2次，支持其與該等廠商之業務關係；惟「美光（**最大客戶**兼長期夥伴）」（「最大客戶」0次）與「**NVIDIA**」（「NVIDIA」與「Micron」均0次；年報係以中文名「美光」表述）未獲支持。
- `6278:objective_ranking_or_market_share:20a7b48918d5cfec` — `PARTIALLY_SUPPORTED`. 台表科113年度年報（**英文版**）中「**SMT**」出現114次、「**EMS**」36次，支持其該等業務；惟「是**全球最大**的…服務商之一」未獲支持（「**largest**」與「No.1」均0次；「**world**」3次之上下文為「consumers all over the **world** experience（…）」「recognized by the **world**'s major Electronics factories」等泛用語）。
- `6411:objective_ranking_or_market_share:39af3c3dfe85aa8b` — `PARTIALLY_SUPPORTED`. 晶焱2023年永續報告書中「**靜電**」出現26次、「**ESD**」9次，支持其 ESD 防護 IC 業務；惟「是**台灣首家**」（「首家」「台灣首」均0次）與「全球**市佔率名列前茅**」（「市佔」0次）未獲支持。
- `6411:objective_ranking_or_market_share:27fa17d018a64993` — `PARTIALLY_SUPPORTED`. 報告書支持其 ESD 元件之應用領域；惟「在 PC 及消費性電子市場佔有**支配地位**」與「擴大…**市佔率**」（「市佔」0次）未獲支持。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）；UNKNOWN 追蹤清單維持 **166 筆**。
- Author-reviewed total: **710 / 1,399**; remaining: **689**. Outcome counts: ACCEPTED 80, PARTIALLY_SUPPORTED 460, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 166. Next pending claim by priority: `6415:objective_ranking_or_market_share:5b44c9f8d34a07a8` (矽力-KY).

## Author batch `author-119` — 2026-10-09

- Reviewed the next six unreviewed objective ranking/market-share claims in checkpoint order (矽力-KY 6415, 環球晶 6488, 九齊 6494, 穎崴 6515 ×2, 宏觀 6568). Evidence came from directly downloaded and inspected official disclosures: 矽力-KY法人說明會簡報、環球晶法人說明會簡報、九齊公司簡介文件、穎崴法人說明會簡報、宏觀微電子法人說明會簡報。
- `6415:objective_ranking_or_market_share:5b44c9f8d34a07a8` — `PARTIALLY_SUPPORTED`. 矽力簡報中「**AI**」出現2次、「**BMS**」2次，支持其跨足該等應用；惟「受惠於中國半導體『**國產替代**』政策」（「國產」「中國」均0次）與「在中國**市佔率節節攀升**」（「市佔」0次）未獲支持。
- `6488:objective_ranking_or_market_share:d5518e9a98f8f76b` — `PARTIALLY_SUPPORTED`. 環球晶簡報中「**矽晶圓**」出現15次、「全球」15次，支持其矽晶圓業務；惟「隸屬於[[中美晶]]集團」（「中美晶」0次）、「全球**前三大**」（0次）與「**台灣第一大**」（0次）未獲支持。
- `6494:objective_ranking_or_market_share:98025032285ef223` — `PARTIALLY_SUPPORTED`. 九齊公司簡介文件中「**玩具**」出現9次、「**MCU**」4次、「**4位元**」4次、「**8位元**」2次、「**32位元**」1次、「**語音**」4次，支持其產品線與應用領域；惟「享有**極高的市佔率**」未獲支持（「**市佔**」0次）。
- `6515:objective_ranking_or_market_share:1e4a6714d95ead3a` — `PARTIALLY_SUPPORTED`. 穎崴簡報中「**Test Socket**」出現2次、「**測試座**」1次，支持其測試座業務；惟「位居全球**前三大**」（0次）與「躍升為全球**第一大**測試座供應商」（0次）未獲支持。
- `6515:objective_ranking_or_market_share:7d430c6cf1e6bc6c` — `UNKNOWN_AFTER_RESEARCH`. 所取得之官方簡報中「**前20大**」與「**九成**」之出現次數均為0，未載客戶集中度敘述。
- `6568:objective_ranking_or_market_share:f46d76f198f50997` — `PARTIALLY_SUPPORTED`. 宏觀簡報中「**RF**」出現2次、「**射頻**」2次，支持其射頻 IC 業務；惟「是**台灣唯一**」（「唯一」「台灣」均0次）與「位居全球**前三大**」（0次）未獲支持。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。UNKNOWN 追蹤清單已同步刷新至 **167 筆**。
- Author-reviewed total: **716 / 1,399**; remaining: **683**. Outcome counts: ACCEPTED 80, PARTIALLY_SUPPORTED 465, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 167. Next pending claim by priority: `6573:objective_ranking_or_market_share:0ab58d2ad0c9cdd6` (虹揚-KY).

## Author batch `author-120` — 2026-10-09

- Reviewed the next eight unreviewed objective ranking/market-share claims in checkpoint order (虹揚-KY 6573, 鈺太 6679 ×2, 采鈺 6789 ×2, 宏捷科 8086 ×3). Evidence came from directly downloaded and inspected official disclosures: 虹揚-KY上市前業績發表會文件、鈺太科技上櫃前業績發表會文件、采鈺114年股東常會議事手冊、宏捷科民國97年度財務報告。
- `6573:objective_ranking_or_market_share:0ab58d2ad0c9cdd6` — `PARTIALLY_SUPPORTED`. 虹揚文件支持其太陽能旁路二極體及電源產品業務（「**太陽能**」13次、「**旁路二極體**」1次）；惟「在…旁路二極體市場擁有**極高的市佔率**」（「市佔」0次）、「切入**強固型工業電腦**」（「工業電腦」0次）與「[[AI 伺服器]]的電源供應鏈」（「AI」0次）未獲支持。
- `6679:objective_ranking_or_market_share:37679da783fb2682` 與 `7459dd76809acab4` — `PARTIALLY_SUPPORTED`. 鈺太文件支持其 MEMS 麥克風 IC 業務（「**MEMS**」27次、「**麥克風**」16次、「筆電」4次）；惟「為全球 MEMS 麥克風 IC 設計**龍頭**廠商」（「龍頭」0次）與「筆電 MEMS 麥克風市場**市占率高達55-60%**」（「市占」0次）未獲支持。
- `6789:objective_ranking_or_market_share:0b84bdb1ceb376d2` 與 `113f7291089fc909` — `PARTIALLY_SUPPORTED`. 采鈺114年股東常會議事手冊支持其彩色濾光片業務（「**彩色濾光**」4次）；惟「為[[台積電]]旗下**子公司**」（「台積電」0次）、「全球彩色濾光片製造**市占率約45-50%**」與「居**世界第一**」（「市占」「世界第一」均0次）未獲支持。
- `8086:objective_ranking_or_market_share:afb154ac23e8d0ac`、`f979a0ca4a7bc6dd` 與 `2b8e68c61d000145` — `PARTIALLY_SUPPORTED`. 宏捷科**民國97年度財務報告**支持其砷化鎵業務及與 [[Skyworks]] 之業務往來（「**Skyworks**」7次、「**砷化鎵**」2次）；惟「為全球**第二大** GaAs **晶圓代工**廠」（「第二大」「晶圓代工」均0次）、「**市占率約24%**」、「（Skyworks 為）**最大客戶**、貢獻約 **56%** 營收」（「最大客戶」「56%」均0次）未獲支持。**註記：該文件為民國97年度財務報告，非近期版本。**
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）；UNKNOWN 追蹤清單維持 **167 筆**。
- Author-reviewed total: **724 / 1,399**; remaining: **675**. Outcome counts: ACCEPTED 80, PARTIALLY_SUPPORTED 473, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 167. Next pending claim by priority: `8086:objective_ranking_or_market_share:195cb9f67a470584` (宏捷科).

## Author batch `author-121` — 2026-10-09

- Reviewed the next eight unreviewed objective ranking/market-share claims in checkpoint order (宏捷科 8086, 福懋科 8131 ×3, 微矽電子 8162 ×2, 富鼎 8261, 群聯 8299). Evidence came from directly downloaded and inspected official disclosures: 宏捷科111年股東常會議事錄、福懋科110年度年報、微矽電子法人說明會簡報、富鼎公司文件。
- `8086:objective_ranking_or_market_share:195cb9f67a470584` — `UNKNOWN_AFTER_RESEARCH`. 該 claim 之實質內容為**第三人（穩懋）之市場地位**。宏捷科111年股東常會議事錄中「**穩懋**」「**全球最大**」與「**代工**」之出現次數**均為0**；穩懋自身之官方網域取證先前遭遇 SSL/TLS 憑證信任失敗（author-112），故未能就該第三人地位取得可檢視之官方文件。
- `8131:objective_ranking_or_market_share:5930424229e429b1` — `ACCEPTED`. 福懋科110年度年報載「2020年福懋興業股權移轉給南亞科技，**南亞科技股份有限公司持股比例達32% 成為本公司最大股東**，**褔懋興業股份有限公司持股比例降為30.68%**」，並附「福懋科技公司與台塑集團關聯圖」及「一貫化垂直整合之公司」之敘述，與 claim 之持股比例、第一大／第二大股東與集團內垂直整合**逐項對應**。
- `8131:objective_ranking_or_market_share:478f771b0c4ced7b` — `PARTIALLY_SUPPORTED`. 「南亞科技為第一大股東，持股32%」獲逐字支持；惟「（**最大客戶**）」未獲支持（「最大客戶」0次）。
- `8131:objective_ranking_or_market_share:468108abf2d6a30b` — `PARTIALLY_SUPPORTED`. 「南亞科技為第一大股東」獲支持；惟「（客戶，**占營收 50%**）」未獲支持——「**50%**」1次之上下文為員工年齡別統計（如「40~49歲 40.05%」），非客戶營收占比。
- `8162:objective_ranking_or_market_share:53be25f984132f29` 與 `e32635bf5c906e45` — `ACCEPTED`. 微矽電子法人說明會簡報載「• 微矽電子**深耕半導體產業超過38年**」「• **為國內電源管理IC、MOSFET、氮化鎵(GaN)晶圓測試服務的最大供應商**」，與 claim 逐項對應。
- `8261:objective_ranking_or_market_share:49acbcc2abe7bd34` — `PARTIALLY_SUPPORTED`. 富鼎文件中「**MOSFET**」出現1次；惟「是**台灣第一家**成功整合**6吋 DMOS**製程之 IC 設計公司」未獲支持（「6吋」「DMOS」「第一家」均0次）。
- `8299:objective_ranking_or_market_share:cd78eed6eeac704c` — `UNKNOWN_AFTER_RESEARCH`. 群聯官方網域之年報端點連線**中斷**（「要求已經中止: 連接意外關閉」），未取得可檢視之檔案。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。UNKNOWN 追蹤清單已同步刷新至 **169 筆**。
- Author-reviewed total: **732 / 1,399**; remaining: **667**. Outcome counts: ACCEPTED 83, PARTIALLY_SUPPORTED 476, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 169. Next pending claim by priority: `3570:objective_ranking_or_market_share:35138bf9d920ff85` (大塚).

## Author batch `author-122` — 2026-10-10

- Reviewed the next four unreviewed objective ranking/market-share claims in checkpoint order (大塚 3570 ×2, 研勤 3632, 凱衛 5201). Evidence came from directly downloaded and inspected official disclosures: 大塚法人說明會簡報、凱衛102年度年報。
- `3570:objective_ranking_or_market_share:35138bf9d920ff85` — `PARTIALLY_SUPPORTED`. 大塚法人說明會簡報載「**白金級全產品代理商**」「*獲得**Autodesk**唯一」「*獲得**PTC**唯一白金級**」（「Autodesk」8次、「PTC」7次、「全產品」6次、「**Siemens**」6次），支持其為 Autodesk 及 PTC 在台灣之唯一白金級全產品代理商及代理 Siemens 產品；惟代理品牌之**具體產品名稱**未獲支持——「**AutoCAD**」「**Inventor**」「**Revit**」「**Creo**」「**Windchill**」與「**Chaos**」之出現次數**均為0**（該簡報以圖形排版為主，產品名稱可能以圖像呈現而未被文字層擷取）。
- `3570:objective_ranking_or_market_share:ecc5b3d321654048` — `PARTIALLY_SUPPORTED`. 「台灣**唯一白金級全產品代理商**」獲支持；惟「（佔進貨比**逾六成**）」未獲支持（「六成」0次）。
- `3632:objective_ranking_or_market_share:ddac08bae5982648` — `UNKNOWN_AFTER_RESEARCH`. 本批次自研勤官方網域下載年報時回應 **HTTP 404**，未取得可檢視之檔案。
- `5201:objective_ranking_or_market_share:b747625e09fd4b18` — `PARTIALLY_SUPPORTED`. 凱衛102年度年報中「**證券**」出現88次、「外資券商」1次，支持其金融證券軟體業務；惟「在外資券商在台據點之**市佔率極高（約七成）**」未獲支持——「**市佔**」3次之上下文**均為目標敘述**（「提高市佔率」「代理韓國市佔率第一名 HTS 產品」「提高外資及電子交易市場市佔率」），「**七成**」亦為0次。註記：該年報為民國102年度版本，非近期。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。UNKNOWN 追蹤清單已同步刷新至 **170 筆**。
- Author-reviewed total: **736 / 1,399**; remaining: **663**. Outcome counts: ACCEPTED 83, PARTIALLY_SUPPORTED 479, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 170. Next pending claim by priority: `5202:objective_ranking_or_market_share:0a310a8ce7f2645f` (力新).

## Author batch `author-123` — 2026-10-10

- Reviewed the next eight unreviewed objective ranking/market-share claims in checkpoint order (力新 5202, 中菲 5403 ×3, 系微 6231, 普鴻 6590, 鼎恒 6738 ×2). Evidence came from directly downloaded and inspected official disclosures: 力新永續報告書、系微公司簡介文件、普鴻法人說明會簡報、鼎恒112年股東會年報。
- `5202:objective_ranking_or_market_share:0a310a8ce7f2645f` — `UNKNOWN_AFTER_RESEARCH`. 所取得之力新文件經檢視為**永續報告書性質**（含「關於本報告書」「董事會組成」等章節），其中「金融」3次之上下文為**董事會專長**敘述（「財務金融」）；「**第一金**」與「**富邦金**」之出現次數**均為0**，該具名金融機構客群未獲確立。
- `5403:objective_ranking_or_market_share:5c94bad17f7166b3`、`e50a246d694f5936` 與 `6ea45e064b9f4141` — `UNKNOWN_AFTER_RESEARCH`. 本批次兩度自中菲官方網域下載年報，**均回應「無法解析遠端名稱: 'www.ddsc.com.tw'」（DNS 解析失敗）**，未取得可檢視之檔案。
- `6231:objective_ranking_or_market_share:1da870e8d9816ee5` — `PARTIALLY_SUPPORTED`. 系微公司簡介中「**BIOS**」5次、「**Intel**」8次、「**AMD**」3次、「**Snapdragon**」1次、「NRE」2次，支持其 BIOS 業務及與該等平台之關聯；惟「在 **AI PC** 市場擁有**極高市佔率**」未獲支持（「AI PC」與「市佔」均0次）。
- `6590:objective_ranking_or_market_share:b5dc93a1541f6920` — `PARTIALLY_SUPPORTED`. 普鴻簡報中「**資安**」10次、「**支付**」3次、「**票交**」1次，支持其該等業務；惟「**清算**」「**跨行**」與「**市佔**」之出現次數均為0。
- `6738:objective_ranking_or_market_share:16908d8f6cf3d1a7` — `PARTIALLY_SUPPORTED`. 鼎恒112年報載「在**超過 95% 高續約率**的推升（下）」與「微軟大中華區合作夥伴生態大會，**台灣區唯一合作夥伴代表**」；惟「服務超過 **1,300** 家企業」未獲支持——「**1,300**」3次之上下文**均為財務數字**（「辦理增資17,300 仟元，實收資本額51,300 仟元」）；「客群涵蓋[[緯創]]集團」亦未獲支持——「**緯創**」1次之上下文為**個人職稱**（「**緯創軟體董事李紹唐**也指出：…」）；「[[遠雄]]集團」為0次。
- `6738:objective_ranking_or_market_share:7d16cd36e6e8ebf5` — `PARTIALLY_SUPPORTED`. 年報中「**Azure**」9次、「**Microsoft**」11次、「**微軟**」8次，支持其與微軟雲端平台之合作；惟「（台灣微軟**唯一 HR 創新合作夥伴**）」未獲完整支持——「唯一」3次之上下文為「**台灣區唯一合作夥伴代表**」（屬活動代表身分），「**創新合作夥伴**」一詞為0次。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。UNKNOWN 追蹤清單已同步刷新至 **174 筆**。
- Author-reviewed total: **744 / 1,399**; remaining: **655**. Outcome counts: ACCEPTED 83, PARTIALLY_SUPPORTED 483, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 174. Next pending claim by priority: `6902:objective_ranking_or_market_share:f2d0f66b5bcf6aed` (GOGOLOOK).

## Author batch `author-124` — 2026-10-10

- Reviewed the next five unreviewed objective ranking/market-share claims in checkpoint order (GOGOLOOK 6902, 三竹 8284, 實威 8416, 凌網 5212, 悠遊卡 6035). Evidence came from directly downloaded and inspected official disclosures: GOGOLOOK法人說明會簡報、三竹年報、實威公司簡介文件、凌網投資人簡報。
- `6902:objective_ranking_or_market_share:f2d0f66b5bcf6aed` — `UNKNOWN_AFTER_RESEARCH`. GOGOLOOK法人說明會簡報中「**NAVER**」（區分大小寫）之出現次數為**0**；唯一含「Nav」字串者為**經營團隊經歷**——「**Naver Business Platform 行銷與營運部門負責人**」（該公司營運長之過往任職），**並非股東或控股關係**。「**LINE**」2次之上下文分別為「（詐騙）誘導家長加入 **Line 群組**進行（…）」與「**LINE OA**」；「控股」出現次數為0。
- `8284:objective_ranking_or_market_share:f6ddbfcfc3bb8e15` — `PARTIALLY_SUPPORTED`. 三竹年報中「**簡訊**」出現103次，支持其簡訊業務；惟「是簡訊業界**唯一**獲**行政院**頒發電信防堵**感謝狀**之企業」未獲支持——「**行政院**」與「**感謝狀**」均0次，「**唯一**」2次之上下文均為**智慧電視看盤下單產品**。
- `8416:objective_ranking_or_market_share:4ac1005c2eaa974f` — `PARTIALLY_SUPPORTED`. 實威公司簡介文件中「**SolidWorks**」出現17次、「**Dassault**」1次，支持其代理關係；惟「為 Dassault Systemes 在**亞洲最大**專業代理商」（「亞洲最大」「代理商」均0次）與「成立於 **1997** 年」（未見）未獲支持。
- `5212:objective_ranking_or_market_share:79f144a9e5531357` — `PARTIALLY_SUPPORTED`. 凌網投資人簡報中「**HyRead**」出現11次，支持其平台業務；惟「**市佔第一**」「**圖書館**自動化系統」與「自助借還書機」未獲支持（「市佔」「第一」「圖書館」均0次）。
- `6035:objective_ranking_or_market_share:c0678fc201114b7d` — `UNKNOWN_AFTER_RESEARCH`. 悠遊卡相關網域之文件下載遭 **SSL/TLS 安全通道信任關係失敗**，未取得可檢視之官方文件。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。UNKNOWN 追蹤清單已同步刷新至 **176 筆**。
- Author-reviewed total: **749 / 1,399**; remaining: **650**. Outcome counts: ACCEPTED 83, PARTIALLY_SUPPORTED 486, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 176. Next pending claim by priority: `6462:objective_ranking_or_market_share:d15da7bf0a3e513d` (神盾).

## Author batch `author-125` — 2026-10-10

- Reviewed the next five unreviewed objective ranking/market-share claims in checkpoint order (神盾 6462, 安碁資訊 6690 ×2, 綠界科技 6763, 歐付寶 6878). Evidence came from directly downloaded and inspected official disclosures: 神盾112年股東常會議事手冊、安碁資訊公司文件、綠界科技115年度年報、歐付寶115年股東常會議事手冊。
- `6462:objective_ranking_or_market_share:d15da7bf0a3e513d` — `UNKNOWN_AFTER_RESEARCH`. 神盾112年股東常會議事手冊中「**指紋**」出現25次，支持其業務；惟「**三星**」「**Samsung**」「**起亞**」「**KIA**」「**CSP**」與「**IP驗證**」之出現次數**均為0**，未具名任何客戶；「**市占**」2次之上下文**均為目標敘述**（「擴大指紋辨識晶片產品市占率」）。
- `6690:objective_ranking_or_market_share:2ca855b26577abb8` — `PARTIALLY_SUPPORTED`. 安碁資訊公司文件中「**宏碁**」出現92次（支持集團歸屬）、「**SOC**」61次、「**委外**」3次；惟「是台灣**最大**的專業資訊安全監控委外服務商」未獲支持（「**台灣最大**」0次；「**領導**」2次之上下文為「七、領導能力」與「成為資安服務中的技術領導廠商」）。
- `6690:objective_ranking_or_market_share:e280e76cce489447` — `UNKNOWN_AFTER_RESEARCH`. 「客戶涵蓋超過 **300** 家政府機關與企業，政府佔 **45%**、金融佔 **40%**、製造業佔 **15%**，為台灣 SOC 市場市佔率**逾六成**」未獲確立——「**市佔**」「**六成**」「**45%**」「**40%**」均0次；「**300**」20次之上下文多為**財務數字**（「辦理現金增資計 **300,000** 仟元，增資後實收資本額為 **300,500** 仟元」「**300,500,000**」），非客戶家數。
- `6763:objective_ranking_or_market_share:66e5afa9447c9ff4` — `PARTIALLY_SUPPORTED`. 綠界科技115年度年報中「**第三方支付**」出現26次、「信用卡」37次，支持其第三方支付業務；惟「為台灣第三方支付市場**規模最大**的支付品牌」未獲支持——「**市占**」1次之上下文為**目標敘述**（「易市占率，鞏固市場領導地位」），「**最大**」8次之上下文**多為泛用語**（「發揮最大的潛能」「追求最大限度減少溫室氣體排放」「最大值」等）。
- `6878:objective_ranking_or_market_share:ac1050bc146ee810` — `PARTIALLY_SUPPORTED`. 歐付寶115年股東常會議事手冊中「**電子支付**」出現19次、「**專營**」4次，支持其專營電子支付之性質；惟「隸屬於[[綠界科技]]母集團」（「綠界」0次）、「為台灣**第一家**取得[[金管會]]核發專營電子支付機構營業執照」（「第一家」「執照」均0次）與「（**2015** 年）」（0次）未獲支持。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。UNKNOWN 追蹤清單已同步刷新至 **178 筆**。
- Author-reviewed total: **754 / 1,399**; remaining: **645**. Outcome counts: ACCEPTED 83, PARTIALLY_SUPPORTED 489, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 178. Next pending claim by priority: `6925:objective_ranking_or_market_share:f4539b5294dcb0a4` (意藍).

## Author batch `author-126` — 2026-10-10

- Reviewed the next three unreviewed objective ranking/market-share claims in checkpoint order (意藍 6925, 碩網 7547, 精誠金融 7819). Evidence came from directly downloaded and inspected official disclosures: 意藍公司概況資料表、碩網上櫃前業績發表會簡報。
- `6925:objective_ranking_or_market_share:f4539b5294dcb0a4` — `PARTIALLY_SUPPORTED`. 意藍公司概況資料表載「別，意藍資訊《**OpView 社群口碑資料**》，**評選為第一名**」，並見「**大數據**」6次、「**語意**」4次、「**SaaS**」8次，支持其業務領域；惟「**市佔第一**」未獲支持——全份文件中「**市佔**」為0次，「**第一**」2次之上下文分別為「（產品）**評選為第一名**」（屬**獎項／評選**而非市占率）與「**第一**時間展開接觸與推廣交叉銷」。
- `7547:objective_ranking_or_market_share:516a2ec6196c6b5e` — `PARTIALLY_SUPPORTED`. 碩網上櫃前業績發表會簡報載「**客戶數：全球市場企業客戶＞700家**」與「Success Cases (IV) – Over **700+ Customers**」，並見「**SmartRobot**」2次、「**智能客服**」7次、「**金融**」4次，支持其逾700家企業客戶與智能客服產品；惟「在台灣金融業擁有**超過八成市佔率**」未獲支持（「**八成**」與「**市占**」均0次）。
- `7819:objective_ranking_or_market_share:e0b3c59b20774ef5` — `UNKNOWN_AFTER_RESEARCH`. 精誠金融相關網域之登錄資料下載遭 **SSL/TLS 安全通道信任關係失敗**，未取得可檢視之官方文件。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。UNKNOWN 追蹤清單已同步刷新至 **179 筆**。
- Author-reviewed total: **757 / 1,399**; remaining: **642**. Outcome counts: ACCEPTED 83, PARTIALLY_SUPPORTED 491, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 179. Next pending claim by priority: `3576:objective_ranking_or_market_share:862c3863436e97cd` (聯合再生).

## Author batch `author-127` — 2026-10-10

- Reviewed the next five unreviewed objective ranking/market-share claims in checkpoint order (聯合再生 3576 ×2, 聚恆 4582, 太極 4934, 元晶 6443). Evidence came from directly downloaded and inspected official disclosures: 聯合再生公司簡介／法人說明會簡報、聚恆法人說明會簡報、太極能源法人說明會簡報。
- `3576:objective_ranking_or_market_share:862c3863436e97cd` — `ACCEPTED`. 聯合再生簡報載「（**新日光、昱晶、昇陽合併**，為**台灣最大**太陽（能…）」，與 claim 之「由[[新日光]]、[[昱晶]]、[[昇陽光電]]三家合併而成」「為台灣最大的太陽能模組品牌」**逐項對應**；「系統整合」1次亦支持其系統整合業務。
- `3576:objective_ranking_or_market_share:4e7dfe3251cf2110` — `ACCEPTED`. 簡報載「**URE 模組已連續4年為台灣模組出貨量/市佔率第一**，並榮獲全球多個第三方機構認證」，並見「連續4年度為臺灣第一大的太陽能供應商」與「台灣第一」，與 claim 之「連續多年維持台灣模組銷售市占率第一」**逐字對應**。
- `4582:objective_ranking_or_market_share:fc48e08d8acca449` — `PARTIALLY_SUPPORTED`. 聚恆簡報載「2017年取得德國萊茵 **TÜV O&M認證**，成爲**台灣第一家、亞洲第二家**提供國際級維運服務之廠商」，支持其取得認證及維運服務；惟「為國內**唯一**通過…認證之公司」未獲精確支持——官方敘述為「**第一家**」（時間上之首次），與「唯一」（排他性）不同；簡報中「唯一」1次之上下文為「不因全球動盪而停擺的唯一解方！」。
- `4934:objective_ranking_or_market_share:b478e7aa2ee7a26e` — `PARTIALLY_SUPPORTED`. 太極簡報中「**模組**」13次、「**越南**」1次，支持其模組業務及越南據點；惟「**越南產能最大**」（「產能」0次）、「具備規避**反傾銷稅**優勢」（0次）與「出口**美國**市場」（0次）未獲支持。
- `6443:objective_ranking_or_market_share:07b85c17bb52a20f` — `UNKNOWN_AFTER_RESEARCH`. 元晶官方網域之文件下載遭 **SSL/TLS 安全通道信任關係失敗**，未取得可檢視之官方文件。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。UNKNOWN 追蹤清單已同步刷新至 **180 筆**。
- Author-reviewed total: **762 / 1,399**; remaining: **637**. Outcome counts: ACCEPTED 85, PARTIALLY_SUPPORTED 493, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 180. Next pending claim by priority: `5607:objective_ranking_or_market_share:7941e3f89be589bb` (遠雄港).

## Author batch `author-128` — 2026-10-10

- Reviewed the next four unreviewed objective ranking/market-share claims in checkpoint order (遠雄港 5607, 耕興 6146, 程曦資訊 6898 ×2). Evidence came from directly downloaded and inspected official disclosures: 遠雄港個體財務報告、耕興112年度財務報告、程曦資訊法人說明會簡報。
- `5607:objective_ranking_or_market_share:7941e3f89be589bb` — `PARTIALLY_SUPPORTED`. 遠雄港個體財務報告載「（遠）雄航空自由貿易港區即為其中之一，也是**台灣唯一航空自由貿易港區**」，並見「**境內關外**」8次、「**通關**」15次、「**優惠**」13次，支持其唯一性與境內關外、通關優惠；惟「**賦稅**優惠」未獲支持（「賦稅」0次），且「成為**跨國電子**與 **AI 伺服器**等高科技產業在亞洲的關鍵物流樞紐」未獲支持（「跨國電子」與「AI」均0次；「伺服器」1次、「樞紐」3次）。
- `6146:objective_ranking_or_market_share:a90215729c3e9aa9` — `ACCEPTED`. 耕興112年度財務報告載「本公司原有**三座10M 室內電波隔離暗室**，二十八座標準半電波隔（離暗室）」「（…）Chamber，十三座SAR 及多套手機RF 與 Conformance 檢測平（台）」與「擁有業界**規模最大**檢測範圍最完整之實驗場地及設備」「由於具有**規模最大**之實驗場地及多項認證資格」（「**EMC**」51次、「**電磁相容**」40次、「**實驗室**」292次、「**安規**」73次），與 claim 之「3座」「規模最大」「EMC 與安規專業認證實驗室」逐項對應。
- `6898:objective_ranking_or_market_share:23e9ccff7ebaf06c` — `PARTIALLY_SUPPORTED`. 程曦資訊法人說明會簡報中「**委外**」出現14次、「**DCRM**」2次、「**BPO**」1次，支持其該等業務；惟「是台灣**最大**的…服務**龍頭**」未獲支持（「**最大**」「**龍頭**」均0次）。
- `6898:objective_ranking_or_market_share:f2bfb4ba7e7a6c99` — `PARTIALLY_SUPPORTED`. 簡報中「**2004**」出現2次、「**委外**」14次，支持其跨足年分與業務；惟「為業界**唯一**同時具備原生技術、營運經驗及流程管理能力之一站式服務商」未獲支持（「**唯一**」0次）。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）；UNKNOWN 追蹤清單維持 **180 筆**。
- Author-reviewed total: **766 / 1,399**; remaining: **633**. Outcome counts: ACCEPTED 86, PARTIALLY_SUPPORTED 496, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 180. Next pending claim by priority: `7786:objective_ranking_or_market_share:8c416fbea251b784` (東方風能).

## Author batch `author-129` — 2026-10-10

- Reviewed the next four unreviewed objective ranking/market-share claims in checkpoint order (東方風能 7786 ×2, 秋雨 9929, 台塑 1301). Evidence came from directly downloaded and inspected official disclosures: 東方風能公司文件、秋雨113年度個體財務報告、台塑2023年度年報。
- `7786:objective_ranking_or_market_share:8c416fbea251b784` — `PARTIALLY_SUPPORTED`. 東方風能文件中「**離岸風電**」6次、「**海事工程**」5次、「**船隊**」12次，支持其業務性質；惟「為台灣本土**唯一**具備[[離岸風電]]全方位海事工程能力之特種船隊營運商」未獲精確支持——「**唯一**」1次之上下文為「業界**唯一掌握多項長期合約**的領航者，確保企業持續穩健成長與規模長期領先」，係指**長期合約之掌握**。
- `7786:objective_ranking_or_market_share:b764fb96ef27fd17` — `PARTIALLY_SUPPORTED`. 文件載「**市場位置: 台灣最大規模離岸船隊。**」與「" 共**18艘船舶**，**台灣規模最大的國際級多元化船隊** "」，並見「**人員運輸**」2次、「**駁船**」2次、「**運維船**」2次、「**SOV**」3次，逐項對應 claim 之船隊規模與船型；惟「特種**鋼鐵**船隊」未獲支持（「**鋼鐵**」0次；「**CTV**」縮寫亦為0）。
- `9929:objective_ranking_or_market_share:5873511e414e911d` — `UNKNOWN_AFTER_RESEARCH`. 所取得之秋雨文件為**個體財務報告**（含會計師查核報告及財務報表），不含公司沿革或上市歷史——「**1946**」「**第一家**」與「**上市**」之出現次數**均為0**。
- `1301:objective_ranking_or_market_share:f4d83761669c4fba` — `PARTIALLY_SUPPORTED`. 台塑2023年度年報中「**PVC**」86次、「**PE**」102次、「**PP**」89次、「**碳纖維**」7次、「**SAP**」30次、「**垂直整合**」1次，支持其產品線與垂直整合；惟「為台灣**最大**石化工業集團」未獲支持——「**最大**」9次之上下文包括「中國大陸為全球石化原料最大市場」（產業）、「台灣年產能為133.8萬公噸，不僅是台灣**最大生產廠**」（**單一產品之產能**）與「為所有股東創造最大利益」「使用率最大化」（泛用語）。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。UNKNOWN 追蹤清單已同步刷新至 **181 筆**。
- Author-reviewed total: **770 / 1,399**; remaining: **629**. Outcome counts: ACCEPTED 86, PARTIALLY_SUPPORTED 499, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 181. Next pending claim by priority: `1303:objective_ranking_or_market_share:4efa616b8fa69cfb` (南亞).

## Author batch `author-130` — 2026-10-10

- Reviewed the next four unreviewed objective ranking/market-share claims in checkpoint order (南亞 1303, 台聚 1304, 中石化 1314 ×2). Evidence came from directly downloaded and inspected official disclosures: 台聚法人說明會簡報、中石化110年度年報。
- `1303:objective_ranking_or_market_share:4efa616b8fa69cfb` — `UNKNOWN_AFTER_RESEARCH`. 本批次自台灣塑膠集團官方網域所取得之2023年 TCFD 報告書檔案**僅244 bytes**（PDF 文字擷取後僅144字元），實質內容不可得，未取得可檢視之官方文件。
- `1304:objective_ranking_or_market_share:67cf53fe6274fce5` — `PARTIALLY_SUPPORTED`. 台聚法人說明會簡報中「**聚乙烯**」出現3次、「**PE**」21次、「集團」2次，支持其聚乙烯業務及集團架構；惟「不僅是台灣**第一家**生產聚乙烯的石化廠」（「第一家」「首家」均0次）與「跨足**電子材料**領域」（0次）未獲支持。
- `1314:objective_ranking_or_market_share:8ac4eb234307c882` — `PARTIALLY_SUPPORTED`. 中石化110年度年報中「**CPL**」與「**AN**」各出現1次，支持其該等產品之提及；惟「**己內醯胺**」「**丙烯腈**」「**前五大**」「**前十大**」與「**唯一**」之出現次數**均為0**，故「為台灣唯一之 CPL 生產商，亦為全球前五大 CPL 與前十大 AN 製造商」未獲支持。**另註記：本批次自發行人官方網域（cpdc.com.tw）之下載嘗試回應 HTTP 403。**
- `1314:objective_ranking_or_market_share:c2c42ce76293c2c1` — `UNKNOWN_AFTER_RESEARCH`. 中石化110年度年報中「**尼龍6**」出現次數為0，未載該產品角色之敘述，故「[[尼龍6]]（Nylon 6）纖維與工程塑膠之唯一原料」未獲確立。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。UNKNOWN 追蹤清單已同步刷新至 **183 筆**。
- Author-reviewed total: **774 / 1,399**; remaining: **625**. Outcome counts: ACCEPTED 86, PARTIALLY_SUPPORTED 501, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 183. Next pending claim by priority: `1337:objective_ranking_or_market_share:7301f1077bcac945` (再生-KY).

## Author batch `author-131` — 2026-10-10

- Reviewed the next four unreviewed objective ranking/market-share claims in checkpoint order (再生-KY 1337, 中纖 1718, 台橡 2103, 國際中橡 2104). Evidence came from directly downloaded and inspected official disclosures: 再生-KY111年度年報、中纖年報、台橡年報、國際中橡2022年永續報告書。
- `1337:objective_ranking_or_market_share:7301f1077bcac945` — `PARTIALLY_SUPPORTED`. 再生-KY111年度年報中「**開曼**」3次、「**晉江**」9次、「**EVA**」46次、「**回收**」30次、「**再生**」143次，支持其註冊地、營運據點及業務性質；惟「為**中國最大** EVA 回收再生製造商」未獲支持（「**最大**」0次）。
- `1718:objective_ranking_or_market_share:806de1b1b6f17477` — `PARTIALLY_SUPPORTED`. 中纖年報中「**機密**」出現8次，惟其上下文**均為員工保密義務**（「本公司人員所知悉或取得有關公司及/或關係企業之用戶…之**機密**資訊…皆應嚴守保密義務」），非「受限商業機密未公開客戶名單」；核心斷言「**國內市占率極高**」未獲支持（「**市占**」與「**極高**」均0次）。
- `2103:objective_ranking_or_market_share:d3bfe3d982942ba8` — `PARTIALLY_SUPPORTED`. 台橡年報中「**合成橡膠**」出現68次，支持其業務；惟「為**全球第七大**」未獲支持——「**第七**」5次之上下文**均為法規條號**（「誠信經營守則第七條」「國際財務報導準則第七號」等）；「**亞洲最大**」亦為0次，且「**最大**」5次之上下文為「能資源利用最大化」「代表最大信用暴險金額」等泛用語。
- `2104:objective_ranking_or_market_share:61c58054080f7d16` — `PARTIALLY_SUPPORTED`. 國際中橡2022年永續報告書載「碳黑事業以 **Continental Carbon** 品牌，為**台灣唯一、全球排名第六**之碳黑領（導廠商）」與「國際中橡碳黑事業群為**台灣唯一碳黑公司，全球產能排名第六**」（「**碳黑**」297次），**逐字支持**claim 之「台灣唯一」與「全球前六大碳黑製造商」；惟「（全球市佔約 **6%**）」未獲支持——「**市佔**」0次，「**6%**」32次之上下文**均為其他百分比**（「鞍山廠：16%」「馬鞍山廠：26%」「董事平均出席率達96%」等）。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）；UNKNOWN 追蹤清單維持 **183 筆**。
- Author-reviewed total: **778 / 1,399**; remaining: **621**. Outcome counts: ACCEPTED 86, PARTIALLY_SUPPORTED 505, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 183. Next pending claim by priority: `2108:objective_ranking_or_market_share:2ea49757ee9617b6` (南帝).

## Author batch `author-132` — 2026-10-10

- Reviewed the next five unreviewed objective ranking/market-share claims in checkpoint order (南帝 2108, 炎洲 4306, 中美實 4702, 大恭 4706 ×2). Evidence came from directly downloaded and inspected official disclosures: 南帝公司文件、炎洲集團2022年永續報告書、中美實法人說明會簡報、大恭公司簡介文件（英文版）。
- `2108:objective_ranking_or_market_share:2ea49757ee9617b6` — `PARTIALLY_SUPPORTED`. 南帝公司文件載「（本公司為）**前五大NBR 橡膠生產商。**」（「**NBR**」27次、「**丁腈**」19次），**逐字支持**其全球前五大 NBR 製造商之地位；惟「隸屬**台南紡織**集團」（0次）、「台灣**第一大**」（0次）與「年產能約 **18 萬噸**，全球市佔率約 **12%**」（「18萬」0次；「**12%**」1次之上下文為「**0.012%**」）未獲支持。
- `4306:objective_ranking_or_market_share:88dab30976986d42` — `PARTIALLY_SUPPORTED`. 炎洲集團2022年永續報告書中「1978」3次、「**膠帶**」78次、「**BOPP**」16次，支持其成立年分與業務；惟「為全球**前三大**膠帶製造商」（「前三大」0次）與「亦為全球**第一大** BOPP 薄膜生產商」未獲精確支持——「**最大**」5次之上下文包括「（**目標**成為）全球**膠帶最大製造廠商**」（**目標敘述**）、「以美洲及亞洲地區為**最大**市場」「才能發揮**最大**效力」。
- `4702:objective_ranking_or_market_share:1977e5e4d2e51aaf` — `PARTIALLY_SUPPORTED`. 中美實法人說明會簡報中「**分散性染料**」出現1次；惟「**1964**」「**酸性染料**」「**反應性染料**」「**最大**」與「**遠東新世紀／力麗**」之出現次數**均為0**（該簡報文字擷取僅1,583字元）。
- `4706:objective_ranking_or_market_share:821cbf49841c14fb` — `PARTIALLY_SUPPORTED`. 大恭公司簡介文件（**英文版**）載「Date of Incorporation：**April 20, 1966**」，**逐字支持**其成立年分；惟「為台灣**顏料產量最大**之製造商」未獲支持（「顏料」「產量」均0次）。
- `4706:objective_ranking_or_market_share:3755cfeb9bb8b2db` — `UNKNOWN_AFTER_RESEARCH`. 所取得之大恭文件為英文版且以圖形排版為主，「**住化**」「**住友**」「**29.28**」之出現次數均為0，未載股東結構。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。UNKNOWN 追蹤清單已同步刷新至 **184 筆**。
- Author-reviewed total: **783 / 1,399**; remaining: **616**. Outcome counts: ACCEPTED 86, PARTIALLY_SUPPORTED 509, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 184. Next pending claim by priority: `4707:objective_ranking_or_market_share:940bad081308ace4` (磐亞).

## Author batch `author-133` — 2026-10-10

- Reviewed the next three unreviewed objective ranking/market-share claims in checkpoint order (磐亞 4707, 德淵 4720, 康普 4739). Evidence came from directly downloaded and inspected official disclosures: 磐亞法人說明會簡報、德淵2025投資人簡報（英文版）、康普100年度年報。
- `4707:objective_ranking_or_market_share:940bad081308ace4` — `PARTIALLY_SUPPORTED`. 磐亞法人說明會簡報中「**界面活性劑**」4次、「**非離子**」3次，支持其該產品業務；惟「為台灣**最大**非離子界面活性劑製造商」（「最大」0次）與「隸屬[[中石化]]集團」（「中石化」0次）未獲支持。
- `4720:objective_ranking_or_market_share:d3f95d7597dbb5f5` — `PARTIALLY_SUPPORTED`. 德淵2025投資人簡報（**英文版**）中「**Hot Melt**」5次、「hot melt」3次、「**adhesive**」9次，並載「**1976**」，支持其熱熔膠接著劑業務與成立年分；惟「為**台灣最大**熱熔膠製造商」以及「全球 **9 座**生產基地（台灣／中國／**越南**／**印度**／**波蘭**）」之中文詞彙均為0次。**方法論註記：本件為英文版文件，中文關鍵字檢索不具意義。**
- `4739:objective_ranking_or_market_share:a8d39b69c3670ca4` — `PARTIALLY_SUPPORTED`. 康普100年度年報載其「主要業務為**氧化觸媒**、先進材料及電池材料之金屬化學產品專業製造商」（「**氧化觸媒**」63次、「**觸媒**」89次、「**PTA**」73次），支持其氧化觸媒業務；惟「**市佔率高**」未獲支持——「**市佔**」1次之上下文為**產業敘述**「使得**鋰電池市佔率**逐年增加」。註記：該年報為民國100年度版本，非近期。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）；UNKNOWN 追蹤清單維持 **184 筆**。
- Author-reviewed total: **786 / 1,399**; remaining: **613**. Outcome counts: ACCEPTED 86, PARTIALLY_SUPPORTED 512, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 184. Next pending claim by priority: `4754:objective_ranking_or_market_share:a2cc9eca34a71824` (國碳科).

## Author batch `author-134` — 2026-10-10

- Reviewed the next five unreviewed objective ranking/market-share claims in checkpoint order (國碳科 4754, 材料-KY 4763, 南寶 4766, 台特化 4772 ×2). Evidence came from directly downloaded and inspected official disclosures: 國碳科105年度年報、材料-KY法人說明會簡報、南寶法人說明會簡報、台特化公司簡介文件。
- `4754:objective_ranking_or_market_share:a2cc9eca34a71824` — `PARTIALLY_SUPPORTED`. 國碳科105年度年報中「**防火**」81次、「**UL**」4次、「**FM**」3次，支持其防火延燒材料業務及相關認證；惟「擁有**亞洲唯一** UL／FM **雙認證**」未獲支持（「**亞洲唯一**」「**唯一**」「**雙認證**」均0次）。
- `4763:objective_ranking_or_market_share:86c143e3b1fdeacf` — `PARTIALLY_SUPPORTED`. 材料-KY法人說明會簡報中「**絲束**」25次，並載「競爭同業：紡絲級 **Celanese、Eastman、Solvay及Daicel**；塑料級Eastman、Daicel及四川普什」，支持其絲束業務及同業結構；惟各項市占率數字未獲支持——「38%」「25%」「19%」「15%」未見，「**2%**」6次之上下文為**其他數字之子字串**（「27.**2%**」「71.1**2%**」）。
- `4766:objective_ranking_or_market_share:37f70358d3db2a81` — `PARTIALLY_SUPPORTED`. 南寶法人說明會簡報載「南寶樹脂是世界級的化學和材料公司…**我們是世界第一的運動鞋用接（著劑）**」（「接著劑」26次、「鞋用」6次），**逐字支持**其全球鞋用接著劑市佔第一；惟「（Tier-1 品牌**市佔約 50%**）」未獲支持——「**市佔**」2次之上下文**均為目標敘述**，「**50%**」6次之上下文**均非**該市占率（「目標2030年減少50%的高關注化學品」「加入工會的人數比例為50%」）。
- `4772:objective_ranking_or_market_share:2d583dbd82c12ed3` 與 `3e71412bc838ad92` — `PARTIALLY_SUPPORTED`. 台特化公司簡介文件中「**半導體**」30次，支持其半導體特用材料業務；惟「**中美晶**」「**大立光**」「**環球晶圓**」「**最大股東**」與「**30%**」之出現次數**均為0**，股東結構未獲確立。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）；UNKNOWN 追蹤清單維持 **184 筆**。
- Author-reviewed total: **791 / 1,399**; remaining: **608**. Outcome counts: ACCEPTED 86, PARTIALLY_SUPPORTED 517, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 184. Next pending claim by priority: `6434:objective_ranking_or_market_share:4cdefa173c0d7b8e` (達輝光電).

## Author batch `author-135` — 2026-10-10

- Reviewed the next three unreviewed objective ranking/market-share claims in checkpoint order (達輝光電 6434, 聚和 6509, 榮炭 6555). Evidence came from directly downloaded and inspected official disclosures: 達輝光電公司簡介及主要業務與產品、聚和111年度年報。
- `6434:objective_ranking_or_market_share:4cdefa173c0d7b8e` — `ACCEPTED`. 達輝光電文件載「致力於 **TAC 膜（Triacetate Cellulose Film，三醋酸纖維素薄膜）** 之研發、製造及銷售。TAC 膜為液晶顯示器中偏光板之關鍵零組件…」與「…**是國內唯一生產該項產品並具競爭力之生產廠商**」，並載「母公司（**新光合纖**）強而有力的集團支持」（「TAC」9次、「三醋酸」1次、「光學膜」1次、「唯一」1次、「新光合纖」1次），與 claim 逐項對應。
- `6509:objective_ranking_or_market_share:c068206ce2be8b0d` — `PARTIALLY_SUPPORTED`. 聚和111年度年報中「**精密化學品**」出現11次、「**生技**」5次、「**製藥**」2次、「**電池**」7次、「主軸」7次，支持其精密化學品事業之應用領域；惟「是近年營運成長的**最大主軸**」（「最大主軸」0次）、「[[電動車]]電池**電解液**」（0次）與「[[台積電]]與[[日月光投控]]等[[半導體]]大廠的 **3D 先進封裝異質整合填孔電鍍製程**」（「台積電」「日月光」「先進封裝」「填孔」均0次）未獲支持。
- `6555:objective_ranking_or_market_share:56167743ae5aa1a5` — `UNKNOWN_AFTER_RESEARCH`. 本批次自榮炭官方網域下載財務報告時回應 **HTTP 404**，未取得可檢視之檔案。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。UNKNOWN 追蹤清單已同步刷新至 **185 筆**。
- Author-reviewed total: **794 / 1,399**; remaining: **605**. Outcome counts: ACCEPTED 87, PARTIALLY_SUPPORTED 518, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 185. Next pending claim by priority: `6582:objective_ranking_or_market_share:35bb14dd44c6df25` (申豐).

## Author batch `author-136` — 2026-10-10

- Reviewed the next five unreviewed objective ranking/market-share claims in checkpoint order (申豐 6582, 兆捷科技 6959, 邦泰 8935 ×3). Evidence came from directly downloaded and inspected official disclosures: 申豐法人說明會簡報、兆捷科技法人說明會簡報、邦泰法人說明會簡報。
- `6582:objective_ranking_or_market_share:35bb14dd44c6df25` — `PARTIALLY_SUPPORTED`. 申豐法人說明會簡報中「**乳膠**」13次、「**手套**」6次、「NBR」1次，支持其 NBR 乳膠及手套應用；惟「年產能約 **8 萬噸**」（0次）、「全球市佔約 **6%**」（「6%」3次中之一上下文不足，另二者為「7.6%」與「**-36%**」之子字串）與「客戶涵蓋 [[Top Glove]]、[[Hartalega]]、[[Kossan]]、[[Supermax]]」（四者均0次）未獲支持。
- `6959:objective_ranking_or_market_share:04813286c96d4265` — `PARTIALLY_SUPPORTED`. 兆捷科技法人說明會簡報中「**特殊氣體**」出現4次，支持其業務；惟「為台灣目前**唯一**能提供**四大類**半導體特殊氣體之業者」未獲支持——「**唯一**」3次之上下文分別為「唯一同時持有特殊氣體銷售、儲存、製造及運輸完整**執照**的（…）」「台灣唯一**整合型平台**」「在新竹科學園區中，唯一同時持有大規模毒性、易爆性（…）」，且「**AsH3**」「**PH3**」「**BF3**」「**離子植入**」與「**四大類**」均為0次。
- `8935:objective_ranking_or_market_share:5b7fd516ddccfb07` — `PARTIALLY_SUPPORTED`. 邦泰法人說明會簡報中「**CROCS**」出現1次，支持其代工關係，「棒球」1次之上下文為**鞋類列舉**「（足球/棒球/壘球/美式足球/高爾夫鞋）」；惟「長期為 [[Nike]] **棒球鞋底亞洲最大供應商**」（「Nike」「亞洲最大」均0次）與「另供應 [[安踏]]、[[特步]]」（均0次）未獲支持。
- `8935:objective_ranking_or_market_share:4f531d8d97f7214b` 與 `6e616151ae29b468` — `UNKNOWN_AFTER_RESEARCH`. 邦泰法人說明會簡報中「**Nike**」與「**亞洲最大**」之出現次數均為0，該具名客戶關係與市場地位未獲確立。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。UNKNOWN 追蹤清單已同步刷新至 **187 筆**。
- Author-reviewed total: **799 / 1,399**; remaining: **600**. Outcome counts: ACCEPTED 87, PARTIALLY_SUPPORTED 521, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 187. Next pending claim by priority: `1513:objective_ranking_or_market_share:bf4e992193fcae82` (中興電).

## Author batch `author-137` — 2026-10-10

- Reviewed the next three unreviewed objective ranking/market-share claims in checkpoint order (中興電 1513 ×2, 亞崴 1530). Evidence came from directly downloaded and inspected official disclosures: 中興電公司背景文件（英文版）、亞崴114年第四季個體財務報告。
- `1513:objective_ranking_or_market_share:bf4e992193fcae82` — `PARTIALLY_SUPPORTED`. 中興電公司背景文件（**英文版**）載「**CHEM holds independent innovation of development in technology for GIS (Gas-Insulated Switchgear)**」（「**GIS**」2次、「switchgear」1次），支持其 GIS 技術與業務；惟「為台灣 GIS **領導廠**」（「market share」「largest」均0次）、「國內高壓 GIS **市佔約七成**」（同前）與「**唯一**取得[[台電]] **345kV** GIS 認證」（「Taipower」「Taiwan Power」均0次）未獲支持。
- `1513:objective_ranking_or_market_share:9130fb44b84a3c57` — `UNKNOWN_AFTER_RESEARCH`. 文件中「**Taipower**」「**Taiwan Power**」「**largest**」之出現次數均為0，未載「[[台電]] — 最大客戶（345kV GIS、變電站統包）」之具名客戶與專案敘述。
- `1530:objective_ranking_or_market_share:03337988477ef09c` — `PARTIALLY_SUPPORTED`. 亞崴114年第四季個體財務報告中「**程泰**」出現1次、「**加工中心**」3次、「**龍門**」1次，支持其集團歸屬與產品類型；惟「有『**龍門世家**』之稱」（0次）與「為台灣龍門型加工中心機**市占領先者**」（「市占」「領先」均0次）未獲支持。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。UNKNOWN 追蹤清單已同步刷新至 **188 筆**。
- Author-reviewed total: **802 / 1,399**; remaining: **597**. Outcome counts: ACCEPTED 87, PARTIALLY_SUPPORTED 523, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 188. Next pending claim by priority: `1539:objective_ranking_or_market_share:fa11a3ede72b0d04` (巨庭).

## Author batch `author-138` — 2026-10-10

- Reviewed the next four unreviewed objective ranking/market-share claims in checkpoint order (巨庭 1539, 喬福 1540, 新麥 1580, 程泰 1583). Evidence came from directly downloaded and inspected official disclosures: 巨庭114年度年報（自第三方彙整站取得，內容經檢視確為發行人年報全文）、喬福112年及111年第一季財務報告、新麥營運報告（英文版）、程泰104年度年報。
- `1539:objective_ranking_or_market_share:fa11a3ede72b0d04` — `UNKNOWN_AFTER_RESEARCH`. 巨庭114年度年報中「**Stanley**」「**DEWALT**」「**SawStop**」「**TTI**」與「**RYOBI**」之出現次數**均為0**（「客戶」30次支持其有客戶敘述，惟未具名該等對象），故「最大客戶 [[Stanley Black & Decker]]（含 [[DEWALT]]），另供應 [[SawStop]] 及 [[TTI]]（RYOBI）」未獲確立。
- `1540:objective_ranking_or_market_share:6d45c395e82f2ccd` — `UNKNOWN_AFTER_RESEARCH`. 喬福112年及111年第一季財務報告中「**美國**」「**USA**」與「**America**」之出現次數**均為0**，未載「美國為最大市場」之敘述。
- `1580:objective_ranking_or_market_share:5560d01646da11a1` — `PARTIALLY_SUPPORTED`. 新麥營運報告（**英文版**）載「**SINMAG EQUIPMENT CORPORATION**」（「**SINMAG**」16次）與「**baking**」13次、「**Baking**」5次，支持其烘焙設備業務與品牌；惟「為**亞洲最大**」（「largest」2次之上下文未見完整之亞洲最大表述）與「客戶逾 **3,000 家**」（「3,000」0次）未獲支持。
- `1583:objective_ranking_or_market_share:25159825fab9a7d1` — `PARTIALLY_SUPPORTED`. 程泰104年度年報中「**車床**」220次、「**GOODWAY**」8次、「台灣」62次，支持其 CNC 車床業務與品牌；惟「為**台灣最大** CNC 車床製造商之一」未獲支持——「**最大**」17次之上下文**多為加工規格**（「最大車削直徑 Ø16 ~ Ø42 mm」「最大研磨直徑 Ø190 mm ~ Ø400 mm」「最大工件直徑Ø6,000mm」等），非市場地位表述。註記：該年報為民國104年度版本。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。UNKNOWN 追蹤清單已同步刷新至 **190 筆**。
- Author-reviewed total: **806 / 1,399**; remaining: **593**. Outcome counts: ACCEPTED 87, PARTIALLY_SUPPORTED 525, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 190. Next pending claim by priority: `1590:objective_ranking_or_market_share:9214f561cebb3418` (亞德客-KY).

## Author batch `author-139` — 2026-10-10

- Reviewed the next four unreviewed objective ranking/market-share claims in checkpoint order (亞德客-KY 1590, 川寶 1595, 宇隆 2233 ×2). Evidence came from directly downloaded and inspected official disclosures: 亞德客集團公司文件、川寶年報、宇隆公司簡介文件。
- `1590:objective_ranking_or_market_share:9214f561cebb3418` — `PARTIALLY_SUPPORTED`. 亞德客集團文件中「**氣動元件**」9次、「**中國**」45次、「全球」27次，支持其氣動元件業務與中國市場布局；惟「中國**市佔約30%**」未獲確認——「**市佔**」1次之上下文為**目標敘述**（「■ **提高市佔**」），「**30%**」4次中之一為「（市）**場約30%**」，惟該片段**上下文不完整，無法確認其主詞是否為本公司市占率**。
- `1595:objective_ranking_or_market_share:59183f089735bcd1` — `PARTIALLY_SUPPORTED`. 川寶年報中「**PCB**」56次、「曝光」2次，支持其 PCB 相關設備業務；惟「為**全球最大** PCB **半自動曝光機**廠」未獲支持（「曝光機」「半自動」「最大」均0次）。
- `2233:objective_ranking_or_market_share:c9096bb9c6aa992d` — `PARTIALLY_SUPPORTED`. 宇隆公司簡介文件中「**Bosch**」12次、「博世」1次，並載「**成為BOSCH優選供應商**」，支持其與 Bosch 之供應關係；惟「**最大客戶**（佔約 **72%**）」未獲支持（「最大客戶」「72%」均0次）。
- `2233:objective_ranking_or_market_share:bf4ac0b6acfe8253` — `PARTIALLY_SUPPORTED`. 本 claim 為同一具名客戶事實之條目表述；文件支持其與 [[Robert Bosch]] 之供應關係，惟「最大」（客戶）未獲支持。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）；UNKNOWN 追蹤清單維持 **190 筆**。
- Author-reviewed total: **810 / 1,399**; remaining: **589**. Outcome counts: ACCEPTED 87, PARTIALLY_SUPPORTED 529, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 190. Next pending claim by priority: `2421:objective_ranking_or_market_share:7f00f533ae4191d0` (建準).

## Author batch `author-140` — 2026-10-10

- Reviewed the next six unreviewed objective ranking/market-share claims in checkpoint order (建準 2421, 盟立 2464, 鉅祥 2476, 倚強科 3219 ×3). Evidence came from directly downloaded and inspected official disclosures: 建準2023 Q4營運成果簡報（英文版）、盟立法人說明會簡報、倚強科113年度年報。
- `2421:objective_ranking_or_market_share:7f00f533ae4191d0` — `PARTIALLY_SUPPORTED`. 建準簡報（**英文版**）載「**FIRST CHOICE GLOBALLY Cooling Solutions**」，並見「**cooling**」16次、「**Fan／fan／FAN**」合計13次、「**AI**」38次，支持其業務；惟「全球 [[AI 伺服器]]風扇**市占約 20%**」未獲完整支持——「**market share**」1次之上下文僅為「market share.」（**片段，無法判讀**），「**20%**」6次中之一為「20%」單獨出現；「**位居前三**」則見「**The Company ranks among the top 3 leading brands in terms of**（…）」（**句子未完整擷取**）。
- `2464:objective_ranking_or_market_share:251a126c32c2c2ec` — `PARTIALLY_SUPPORTED`. 盟立法人說明會簡報中「**自動化**」6次、「**OHT**」3次、「**Stocker**」2次，支持其自動化系統整合及半導體製程設備業務；惟「為台灣**最大**」（0次）、「智慧自動化**物流系統（AS/RS）**」（0次）與「及**機器人**應用」（0次）未獲支持。
- `2476:objective_ranking_or_market_share:e9cbf6611b6656f4` — `UNKNOWN_AFTER_RESEARCH`. 鉅祥官方網域之文件下載遭 **SSL/TLS 安全通道信任關係失敗**，未取得可檢視之官方文件。
- `3219:objective_ranking_or_market_share:0ef62b067682d21f`、`9bca902ddfd55250` 與 `96e9ac24bd44c81e` — `UNKNOWN_AFTER_RESEARCH`. 倚強科113年度年報中「**Meta**」「**最大客戶**」與「**BFT**」之出現次數**均為0**（「測試」69次、「AI 伺服器」2次支持其業務，惟未具名客戶）。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。UNKNOWN 追蹤清單已同步刷新至 **194 筆**。
- Author-reviewed total: **816 / 1,399**; remaining: **583**. Outcome counts: ACCEPTED 87, PARTIALLY_SUPPORTED 531, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 194. Next pending claim by priority: `3616:objective_ranking_or_market_share:da6309bf6fbd75aa` (泓辰).

## Author batch `author-141` — 2026-10-10

- Reviewed the next four unreviewed objective ranking/market-share claims in checkpoint order (泓辰 3616, 宏偉 4565, 科際精密 4568 ×2). Evidence came from directly downloaded and inspected official disclosures: 泓辰法人說明會簡報、宏偉法人說明會簡報、科際精密公司簡報。
- `3616:objective_ranking_or_market_share:da6309bf6fbd75aa` — `PARTIALLY_SUPPORTED`. 泓辰法人說明會簡報載「**LMFP居領先地位**」與「**LMFP正極材料開發**」「**首座LMFP量產線**」（「**LMFP**」26次、「**正極**」7次、「量產」2次），支持其 LMFP 正極材料量產能力；惟「成立於 **2001** 年」（0次；沿革載「粉體設備 **1997**」）、「總部位於**桃園市平鎮區**」（「平鎮」「桃園」均0次）與「為全球**唯一『非中國』**之 LMFP 正極材料製造商」（「唯一」「非中國」「台灣」均0次）未獲支持。
- `4565:objective_ranking_or_market_share:e8f4df672e4b53fe` — `PARTIALLY_SUPPORTED`. 宏偉法人說明會簡報中「**電梯**」出現11次、「**歐賓**」2次，支持其電梯業務與品牌；惟「為台灣工業**貨梯龍頭**」（「貨梯」「龍頭」均0次）、「**市佔逾 30%**」（「市佔」0次；「**30%**」1次之上下文為**圖表座標軸刻度**「0% 10% 20% **30%** 40% 50% …營收比重」）與「自有品牌 **VOLBIN**」（0次）未獲支持。
- `4568:objective_ranking_or_market_share:9189892b50ee5bb9` — `PARTIALLY_SUPPORTED`. 科際精密簡報中「**腰托**」出現3次、「**按摩**」3次，支持其汽車座椅氣動應用之業務；惟「為**微型泵浦與電磁閥**專業廠」（「微型泵浦」「電磁閥」均0次）與「用氣泵**全球市占約 80%**」（「80%」0次）未獲支持。
- `4568:objective_ranking_or_market_share:14f79b7b43f1f4b4` — `UNKNOWN_AFTER_RESEARCH`. 簡報中「**Alfmeier**」「**Faurecia**」「**Continental**」與「**80%**」之出現次數均為0，未具名該等客戶／夥伴或載明市占率。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。UNKNOWN 追蹤清單已同步刷新至 **195 筆**。
- Author-reviewed total: **820 / 1,399**; remaining: **579**. Outcome counts: ACCEPTED 87, PARTIALLY_SUPPORTED 534, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 195. Next pending claim by priority: `4575:objective_ranking_or_market_share:8ef602a5b67e7880` (銓寶).

## Author batch `author-142` — 2026-10-10

- Reviewed the next four unreviewed objective ranking/market-share claims in checkpoint order (銓寶 4575 ×2, 台灣精銳 4583, 達明 4585). Evidence came from directly downloaded and inspected official disclosures: 銓寶年報、達明機器人公司簡介文件。
- `4575:objective_ranking_or_market_share:8ef602a5b67e7880` — `PARTIALLY_SUPPORTED`. 銓寶年報中「**PET**」47次、「**吹瓶機**」51次，支持其 PET 吹瓶機業務；惟「為**台灣最大** PET 吹瓶機製造商」未獲支持——全份年報中「**台灣最大**」1次之上下文為「**亦是台灣最大手工具、工具機用夾頭製造商**」，**該「最大」係修飾夾頭而非吹瓶機**；「佔全國 **85%** 出口額」（0次）、「全球逾 **4,000 台**裝機量」與「行銷 **103 國**」亦未獲完整支持。
- `4575:objective_ranking_or_market_share:804fbb6663ee345a` — `PARTIALLY_SUPPORTED`. 年報中「**鑽夾頭**」12次，並載「**亦是台灣最大手工具、工具機用夾頭製造商**」，支持其夾頭業務及該產品之台灣最大地位；惟「（**40 年**經驗）」未獲支持（「40年」「40 年」均0次）。
- `4583:objective_ranking_or_market_share:6384a87c92b38584` — `UNKNOWN_AFTER_RESEARCH`. 本批次自台灣精銳官方網域下載年報時回應 **HTTP 404**，未取得可檢視之檔案。
- `4585:objective_ranking_or_market_share:2917276f3dfdb362` — `PARTIALLY_SUPPORTED`. 達明公司簡介文件中「**cobot**」11次、「協作機器人」1次，並見「**Universal Robots**」1次，支持其協作機器人業務；惟「為**全球第二大**協作機器人品牌」（「全球第二」0次）與「台灣**唯一**協作機器人製造商」（「唯一」0次）未獲支持。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。UNKNOWN 追蹤清單已同步刷新至 **196 筆**。
- Author-reviewed total: **824 / 1,399**; remaining: **575**. Outcome counts: ACCEPTED 87, PARTIALLY_SUPPORTED 537, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 196. Next pending claim by priority: `4587:objective_ranking_or_market_share:d95215ea397fbeb3` (寶元數控).

## Author batch `author-143` — 2026-10-10

- Reviewed the next four unreviewed objective ranking/market-share claims in checkpoint order (寶元數控 4587, 富田-創 4590 ×2, 萬潤 6187). Evidence came from directly downloaded and inspected official disclosures: 寶元數控公司概況資料表、富田電機112年度年報、萬潤公司簡介文件。
- `4587:objective_ranking_or_market_share:d95215ea397fbeb3` — `PARTIALLY_SUPPORTED`. 寶元數控公司概況資料表中「**研華**」出現2次、「CNC」1次，支持其集團歸屬與 CNC 控制器業務；惟「（**2013 年併購**）」（0次）、「以『**Advantech-LNC**』雙品牌行銷」（0次）、「為台灣／華語圈**最大** CNC 控制器品牌」（「最大」「華語」均0次）與「全球累計逾 **500 家**設備廠客戶」（0次）未獲支持。
- `4590:objective_ranking_or_market_share:360bcbc09d6f1e13` 與 `fdd0dd5d84053326` — `PARTIALLY_SUPPORTED`. 富田112年度年報**以中文名稱「特斯拉」表述該客戶**（「**特斯拉**」2次、「**驅動馬達**」1次），支持其電動車動力系統業務與供應關係；惟「（**最大客戶**）」（0次）、「**最資深供應商**」（0次）與「[[Mazda]]」（「Mazda」「馬自達」均0次）未獲支持。**方法論註記：本件以中文公司名表述，以英文名檢索不具意義。**
- `6187:objective_ranking_or_market_share:6ca35e4decf8dbab` — `PARTIALLY_SUPPORTED`. 萬潤公司簡介文件中「**CoWoS**」出現2次、「**LED**」2次，支持其先進封裝及 LED 相關設備業務；惟「**台積電**」（及「最大客戶」）、「**日月光**」「**矽品**」與「**被動元件**」之出現次數**均為0**。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）；UNKNOWN 追蹤清單維持 **196 筆**。
- Author-reviewed total: **828 / 1,399**; remaining: **571**. Outcome counts: ACCEPTED 87, PARTIALLY_SUPPORTED 541, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 196. Next pending claim by priority: `6208:objective_ranking_or_market_share:96caba418bc3233c` (日揚).

## Author batch `author-144` — 2026-10-11

- Reviewed the next five unreviewed objective ranking/market-share claims in checkpoint order (日揚 6208 ×3, 富強鑫 6603 ×2). Evidence came from directly downloaded and inspected official disclosures: 日揚2025年度年報、富強鑫公司文件。
- `6208:objective_ranking_or_market_share:96caba418bc3233c`、`5fdb674b7ffcd8a1` 與 `fb06ea6703cac885` — `UNKNOWN_AFTER_RESEARCH`. 日揚2025年度年報中「**最大客戶**」出現次數為**0**；「**台積電**」5次之上下文**均為產業展望敘述**——「**台積電**的高階製程仍是全球（…）」「**台積電**預期市占率將攀升至73%，並提升資本支出(CAPEX)」「先進製程帶動晶圓代工市場成長20％，**台積電**(2330)市占將達73%」，**非**客戶關係；「逾20」與「20 %」亦均為0。**註記**：claim 所述之業務範疇（真空設備、Scrubber、清洗）於年報中獲支持（「**真空**」137次、「**Scrubber**」12次、「**清洗**」11次），惟具名客戶關係未獲確立，依一致性規則以 UNKNOWN_AFTER_RESEARCH 結案。
- `6603:objective_ranking_or_market_share:54f19d2754e289e6` — `PARTIALLY_SUPPORTED`. 富強鑫公司文件中「**1974**」出現3次，**逐字支持**其成立年分；惟「為台灣**最大且唯一上市**之**塑膠射出成型機**製造商」未獲支持（「射出成型機」「最大」「唯一」均0次）。
- `6603:objective_ranking_or_market_share:ca23047c4b4f0093` — `PARTIALLY_SUPPORTED`. 文件中「**多色**」出現13次，支持其多色射出相關技術；惟「技術壁壘在**雙色**／多色射出成型機」（「雙色」「射出成型機」均0次）與「**全球領先市占**」（0次）未獲支持。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。UNKNOWN 追蹤清單已同步刷新至 **199 筆**。
- Author-reviewed total: **833 / 1,399**; remaining: **566**. Outcome counts: ACCEPTED 87, PARTIALLY_SUPPORTED 543, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 199. Next pending claim by priority: `6618:objective_ranking_or_market_share:43a37be574cd8eb6` (永虹先進).

## Author batch `author-145` — 2026-10-11

- Reviewed the next three unreviewed objective ranking/market-share claims in checkpoint order (永虹先進 6618, 亞泰金屬 6727 ×2). Evidence came from official disclosure endpoints.
- `6618:objective_ranking_or_market_share:43a37be574cd8eb6` — `UNKNOWN_AFTER_RESEARCH`. 本批次自永虹先進官方網域下載文件時回應 **HTTP 404**，未取得可檢視之檔案。
- `6727:objective_ranking_or_market_share:396efdcf88c26ee4` — `UNKNOWN_AFTER_RESEARCH`. 所取得之亞泰金屬年報（9.75 MB、擷取225,116字元）之**文字層呈現系統性字元位移之亂碼**——例如公司英文名「Asia Metal Industries, Inc.」被擷取為「**$VLD 0HWDO ,QGXVWULHV\u000f ,QF\u0011**」，中文部分亦呈「**٥ੀߎឦπ཰ި**」等非可讀字元（與台光電2023年報、上洋114年報、必應111年報、峰源113年報、欣銓111年報同型之檢索限制）；以關鍵字檢索「含浸」「塗佈」「CCL」「銅箔基板」「七成」之出現次數均為0。
- `6727:objective_ranking_or_market_share:addbac4d018e6d92` — `UNKNOWN_AFTER_RESEARCH`. 本 claim 為同一事實之條目表述（「亞泰（CCL 含浸塗佈設備, 市佔 70%+）」）；年報文字層為亂碼，「含浸」「塗佈」「CCL」「70%」之出現次數均為0。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。UNKNOWN 追蹤清單已同步刷新至 **202 筆**。
- Author-reviewed total: **836 / 1,399**; remaining: **563**. Outcome counts: ACCEPTED 87, PARTIALLY_SUPPORTED 543, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 202. Next pending claim by priority: `6793:objective_ranking_or_market_share:9972aa426778a50b` (天力離岸).

## Author batch `author-146` — 2026-10-11

- Reviewed the next five unreviewed objective ranking/market-share claims in checkpoint order (天力離岸 6793 ×3, 創控 6909 ×2). Evidence came from directly downloaded and inspected official disclosures: 天力離岸Company Profile（英文版）、創控科技公司文件。
- `6793:objective_ranking_or_market_share:9972aa426778a50b` — `PARTIALLY_SUPPORTED`. 天力離岸Company Profile（**英文版**）載「**Business item：manufacturing of offshore wind power blades**」，並見「**blade／Blade**」合計21次、「**offshore**」23次、「**manufactur**」6次、「**carbon**」3次，支持其離岸風機葉片製造業務；惟「台灣**唯一**」未獲支持（「only」4次之上下文未見）。
- `6793:objective_ranking_or_market_share:90e8d4fffb58444d` 與 `8a637f74762efb6c` — `PARTIALLY_SUPPORTED`. 「**Vestas**」出現5次，惟其上下文主要為**合資公司**敘述（「About **MHI Vestas Offshore Wind (MVOW)**」「MHI Vestas Offshore Wind is 50% owned by **Vestas** Wind Systems A/S and 50% by Mitsubishi Heavy Industries (MHI)」）；「（**唯一客戶**）／（**唯一**）」與「（**2025 終止**／終止合作）」未獲支持——「2025」6次之上下文為離岸風電容量目標（「seizing 5.7GW of offshore wind power in Taiwan before **2025**」）。**註記：該文件為2020年版本，早於 claim 所述之2025年事件。**
- `6909:objective_ranking_or_market_share:257a1dfe814cf98a` — `PARTIALLY_SUPPORTED`. 創控公司文件載「**MiTAP M3**量測酸性、鹼性（…）」「創控 **MiTAP** 系列產品從半導體廠務環境的監控，進一步擴展到個別製程段」（「**MiTAP**」3次、「**AMC**」19次），支持其 MiTAP 系列產品與 AMC 監測業務；惟「被[[台積電]]認可」（0次）與「為**唯一高度推薦**」（「唯一」「高度推薦」均0次）未獲支持。
- `6909:objective_ranking_or_market_share:16496bc64a01509f` — `PARTIALLY_SUPPORTED`. 本 claim 為同一事實之條目表述；文件支持其 AMC 監測業務，惟「台積電」與「唯一高度推薦」未獲支持。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）；UNKNOWN 追蹤清單維持 **202 筆**。
- Author-reviewed total: **841 / 1,399**; remaining: **558**. Outcome counts: ACCEPTED 87, PARTIALLY_SUPPORTED 548, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 202. Next pending claim by priority: `6982:objective_ranking_or_market_share:6ce0f1f566a2483c` (大井泵浦).

## Author batch `author-147` — 2026-10-11

- Reviewed the next five unreviewed objective ranking/market-share claims in checkpoint order (大井泵浦 6982 ×2, 長廣 7795 ×3). Evidence came from directly downloaded and inspected official disclosures: 大井泵浦企業簡介、長廣精機114年度年報。
- `6982:objective_ranking_or_market_share:6ce0f1f566a2483c` — `PARTIALLY_SUPPORTED`. 大井泵浦企業簡報中「**加壓**」10次、「**馬達**」6次，支持其加壓馬達業務；惟「為台灣…**龍頭**」（0次）與「（**市佔六成+**）」（「市佔」「六成」均0次；「**60%**」2次之上下文於文字層中僅見「60%」單獨出現，**無法確認指涉**）未獲支持。
- `6982:objective_ranking_or_market_share:d789441c0ced0dea` — `PARTIALLY_SUPPORTED`. 本 claim 為同一事實之條目表述；簡報支持加壓馬達業務，惟「市佔 60%+」未獲支持，「住宅」與「五金行」亦為0次。
- `7795:objective_ranking_or_market_share:1fece52690003c4d` — `PARTIALLY_SUPPORTED`. 長廣114年度年報中「**長興**」88次、「子公司」65次、「**壓膜**」68次、「**載板**」68次、「**真空**」49次、「**ABF**」35次、「全球」40次，支持其集團歸屬與 ABF 載板真空壓膜設備業務；惟「市佔**超過95%**」未獲支持（「95%」「市佔」均0次）。
- `7795:objective_ranking_or_market_share:b856cd136904fdc5` — `PARTIALLY_SUPPORTED`. 「ABF 載板真空壓膜機」業務獲支持；惟「市佔 **95%+**」（均0次）與「**醫療推桿**」（「醫療」「推桿」均0次）未獲支持。
- `7795:objective_ranking_or_market_share:c8947ab48156fadc` — `UNKNOWN_AFTER_RESEARCH`. 年報中「**欣興**」與「**南亞電路板**」之出現次數**均為0**（「南亞」3次之上下文未見「南亞電路板」），且「95%」「市佔」亦為0，該具名客戶與市占率未獲確立。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。UNKNOWN 追蹤清單已同步刷新至 **203 筆**。
- Author-reviewed total: **846 / 1,399**; remaining: **553**. Outcome counts: ACCEPTED 87, PARTIALLY_SUPPORTED 552, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 203. Next pending claim by priority: `8996:objective_ranking_or_market_share:49ffb2ed084de05d` (高力).

## Author batch `author-148` — 2026-10-11

- Reviewed the next three unreviewed objective ranking/market-share claims in checkpoint order (高力 8996, 燦坤 2430, 山隆 2616). Evidence came from directly downloaded and inspected official disclosures: 高力2015年度年報、燦坤公司文件、山隆年報。
- `8996:objective_ranking_or_market_share:49ffb2ed084de05d` — `PARTIALLY_SUPPORTED`. 高力2015年度年報中「**板式熱交換器**」出現58次、「**硬銲**」13次、「**真空**」5次，支持其產品與技術；惟「為台灣**唯一**具備該技術之廠商」（「唯一」0次）、「國內市佔**超過九成**」（「九成」0次；「**市佔**」1次之上下文為**目標敘述**「全力衝刺外銷市場，**提升市佔率**」）與「行銷 **70+ 國**」未獲支持。註記：該年報為民國104年度版本。
- `2430:objective_ranking_or_market_share:2b76127105ffe4fa` — `PARTIALLY_SUPPORTED`. 燦坤公司文件中「**門市**」出現4次，支持其門市經營敘述；惟「曾為台灣**最大 3C 零售通路**」（「3C」「零售」「最大」均0次）、「近年面臨**電商競爭**」（「電商」「通路」均0次）與「門市**轉型**挑戰」未獲支持。
- `2616:objective_ranking_or_market_share:5e8301b7ce9d8b48` — `PARTIALLY_SUPPORTED`. 山隆年報**逐字載明站數**——「自民國87年成立山隆的第一座加油站，經過不斷的努力經營，**現已達77座**」（「**加油站**」87次、「**柴油**」12次），77座符合 claim 所述之「約70座以上」；惟「為國內**最大民營柴油發油商**」未獲支持——「民營」「貨卡車」均0次，且「**最大**」2次之上下文**均非市場地位**（其一為會計用語「金融資產之帳面金額代表**最大**信用暴險金額」）。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）；UNKNOWN 追蹤清單維持 **203 筆**。
- Author-reviewed total: **849 / 1,399**; remaining: **550**. Outcome counts: ACCEPTED 87, PARTIALLY_SUPPORTED 555, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 203. Next pending claim by priority: `2947:objective_ranking_or_market_share:b566dc40942a6a98` (振宇五金).

## Author batch `author-149` — 2026-10-11

- Reviewed the next three unreviewed objective ranking/market-share claims in checkpoint order (振宇五金 2947, 弘帆 8433, 全國 9937). Evidence came from directly downloaded and inspected official disclosures: 弘帆公司簡介（櫃買中心刊物第163期）、全國加油站113年法人說明會簡報。
- `2947:objective_ranking_or_market_share:b566dc40942a6a98` — `UNKNOWN_AFTER_RESEARCH`. 本批次自振宇五金官方網域下載永續報告書時回應 **「要求已經中止: 連接意外關閉」**（連線層失敗），**經重試一次仍為相同結果**，未取得可檢視之檔案。
- `8433:objective_ranking_or_market_share:869a93b4d335968e` — `PARTIALLY_SUPPORTED`. 弘帆公司簡介載其從事流行**髮飾**等產品之設計、生產及銷售（「**髮飾**」5次），並**將 Goody 列為客戶**——「Wal-Mart、ZARA、H&M、Watsons、**Goody** 等均與弘帆公司保持多年良好的合作關係」。**惟「70%」1次之上下文為本公司自身之營收地區結構**——「弘帆公司近**70%** 的營收來自美洲市場，22% 左右的營收來源於歐洲客戶」，**並非**「三大通路品牌合計控制約70%市佔」；「**Conair**」「**Scunci**」「**最大**」與「**第一供應商**」之出現次數均為0。
- `9937:objective_ranking_or_market_share:2afddb814522cda5` — `PARTIALLY_SUPPORTED`. 全國加油站113年法人說明會簡報之油品品項旁標示「（**台塑油品**）」（「**台塑**」5次、「加油站」13次），支持其販售台塑油品之敘述；惟「為**唯一**油品供應商」未獲支持——「**唯一**」0次，且「**中油**」出現**3次**（與「唯一供應商」之敘述不相容）。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。UNKNOWN 追蹤清單已同步刷新至 **204 筆**。
- Author-reviewed total: **852 / 1,399**; remaining: **547**. Outcome counts: ACCEPTED 87, PARTIALLY_SUPPORTED 557, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 204. Next pending claim by priority: `9960:objective_ranking_or_market_share:e41b23b10a6c9c28` (邁達康).

## Author batch `author-150` — 2026-10-11

- Reviewed the next four unreviewed objective ranking/market-share claims in checkpoint order (邁達康 9960 ×2, 一零四 3130 ×2). Evidence came from directly downloaded and inspected official disclosures: 一零四新聞稿。
- `9960:objective_ranking_or_market_share:e41b23b10a6c9c28` 與 `6dccf464a9b18112` — `UNKNOWN_AFTER_RESEARCH`. 本批次自邁達康官方網域下載年報時回應 **「無法解析遠端名稱: 'www.golfshop.com.tw'」**（**DNS 解析失敗**），未取得可檢視之檔案。
- `3130:objective_ranking_or_market_share:566bc6a4f3ac3901` — `PARTIALLY_SUPPORTED`. 一零四新聞稿**逐字載**「**104 人力銀行成立於1996 年**，2006 年以『一零四資訊科技股份有限公司』於台灣證券交易所掛牌，成為**台灣第一家上市的網路公司**，**穩居台灣流量最多的人力資源服務網站**，持續以成為華人地區人力資源**領導品牌**為使命」，支持其平台之領先地位；惟「創立於 **1993** 年」未獲支持且**與文件不符**——文件載成立年為「**1996 年**」，且「最大」一詞為0（文件用語為「流量最多」）。**註記**：文件以「**104 人力銀行**」（**含空格**）表述，故以無空格之「104人力銀行」檢索為0，屬**字串假陰性**。
- `3130:objective_ranking_or_market_share:96c37785e24a9e4c` — `PARTIALLY_SUPPORTED`. 新聞稿載其以「C.M.O.S.A.五大核心概念（cloud 雲端、mobile 行動、open 開放、social 社群、**AI 人工智慧**）」提供網路求職求才等服務，且「穩居台灣流量最多的人力資源服務網站」，支持其平台領先地位與 AI 應用；惟「**全台最大線上職缺庫**」與「**大數據**職缺推薦」未獲逐字支持（「最大」「大數據」均0次）。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。UNKNOWN 追蹤清單已同步刷新至 **206 筆**。
- Author-reviewed total: **856 / 1,399**; remaining: **543**. Outcome counts: ACCEPTED 87, PARTIALLY_SUPPORTED 559, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 206. Next pending claim by priority: `2002:objective_ranking_or_market_share:71c65f9aa39ab582` (中鋼).

## Author batch `author-151` — 2026-10-11

- Reviewed the next three unreviewed objective ranking/market-share claims in checkpoint order (東和鋼鐵 2006 ×2, 春雨 2012). Evidence came from directly downloaded and inspected official disclosures: 東和鋼鐵106年度年報、春雨104年度年報。
- `2006:objective_ranking_or_market_share:af9053f6081a9d90` — `PARTIALLY_SUPPORTED`. 東和鋼鐵106年度年報中「**電爐**」出現9次，支持其電爐煉鋼業務；惟「為台灣**最大**電爐鋼廠之一」未獲支持——全份年報中「**最大**」5次之上下文**均為泛用語**（「為股東創造**最大**的價值」「鋼鐵產業今年**最大**的難題」「員工是公司**最大**資產」），**無一為市場地位表述**。
- `2006:objective_ranking_or_market_share:9ea68a7171bfd47f` — `PARTIALLY_SUPPORTED`. 年報中「**鋼筋**」52次、「**H型鋼**」21次，支持其該兩項產品；惟「（台灣市占**九成**）」未獲支持——「**九成**」0次，「**市佔**」3次之上下文於文字層中僅見「市佔率」一詞，未能擷取完整敘述。
- `2012:objective_ranking_or_market_share:49de828dafb735f1` — `PARTIALLY_SUPPORTED`. 春雨104年度年報中「**螺絲**」146次、「**螺帽**」58次、「**扣件**」27次、「**雄獅**」（自有品牌）24次，支持其扣件製造業務與品牌；惟「為台灣**最大**扣件製造商之一」未獲支持——「**最大**」7次之上下文**多為泛用語**（「將有限資源作**最大**的貢獻」「達到整體資源之**最大**貢獻」「是留住客戶**最大**關鍵」「對信用風險**最大**（暴險）」）。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）；UNKNOWN 追蹤清單維持 **206 筆**。
- Author-reviewed total: **859 / 1,399**; remaining: **540**. Outcome counts: ACCEPTED 87, PARTIALLY_SUPPORTED 562, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 206. Next pending claim by priority: `2002:objective_ranking_or_market_share:71c65f9aa39ab582` (中鋼).

## Author batch `author-152` — 2026-10-11

- Reviewed the next three unreviewed objective ranking/market-share claims in checkpoint order (中鋼 2002, 大成鋼 2027, 彰源 2030). Evidence came from directly downloaded and inspected official disclosures: 中鋼民國96年股東會年報、大成鋼法人說明會簡報、彰源法人說明會簡報。
- `2002:objective_ranking_or_market_share:71c65f9aa39ab582` — `PARTIALLY_SUPPORTED`. 中鋼年報中「**高爐**」44次、「**一貫**」4次、「**粗鋼**」13次，支持其高爐煉鋼一貫作業之敘述；惟「年粗鋼 **1,050 萬噸**」未獲支持——「1,050」15次之上下文經檢視包括「1,050,000」「1,051,050」「氣氮1,050噸」等，**未見「年粗鋼1,050萬噸」之完整表述**；「台灣**最大**鋼鐵企業」與「**唯一**」亦未見完整市場地位表述。註記：該年報為民國96年度版本。
- `2027:objective_ranking_or_market_share:ef66ad3900032a5c` — `PARTIALLY_SUPPORTED`. 大成鋼法人說明會簡報載「大成**不銹鋼**工業股份有限公司 **TA CHEN STAINLESS PIPE COMPANY LIMITED**」，並見「**不銹鋼**」19次、「**鋁**」12次、「**通路**」17次、「**美國**」8次，支持其通路業務與美國市場布局；惟「為**全球最大**之不銹鋼及鋁捲板通路商」未獲支持（「全球最大」0次）。
- `2030:objective_ranking_or_market_share:7946eb2d40401c49` — `PARTIALLY_SUPPORTED`. 彰源法人說明會簡報載「彰源企業股份有限公司 **FROCH ENTERPRISE CO., LTD.**」，並見「**不銹鋼**」5次、「管」4次，支持其不銹鋼產品業務；惟「為台灣**第一大**不銹鋼管及不銹鋼板製造廠」未獲支持（「第一大」與「最大」均0次）。
- **方法論註記（第 7 類術語變體）**：大成鋼與彰源之簡報均以「**不銹鋼**」（**銹**）表述，與 claim 所用之「不鏽鋼」（**鏽**）為**異體字**，**同一概念以不同字形檢索會得到不同結果**（大成鋼「不銹鋼」19次、「不鏽鋼」0次）。此為繼年份表示法、數字表示法、語言版本、縮寫全名、外國公司中譯、數字與中文間空格之後的第 7 類。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）；UNKNOWN 追蹤清單維持 **206 筆**。
- Author-reviewed total: **862 / 1,399**; remaining: **537**. Outcome counts: ACCEPTED 87, PARTIALLY_SUPPORTED 565, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 206. Next pending claim by priority: `2034:objective_ranking_or_market_share:9db08fbb1d4b60e5` (允強).

## Author batch `author-153` — 2026-10-11

- Reviewed the next three unreviewed objective ranking/market-share claims in checkpoint order (燁聯 9957, 榮剛 5009, 有益 9962). Evidence came from directly downloaded and inspected official disclosures: 榮剛法人說明會簡報（英文版）、有益民國95年度財務報表。
- `9957:objective_ranking_or_market_share:08d89bac647cd335` — `UNKNOWN_AFTER_RESEARCH`. 本批次自燁聯官方網域下載110年度報告時回應 **HTTP 404**，未取得可檢視之檔案。
- `5009:objective_ranking_or_market_share:25a19381ca4321d2` — `PARTIALLY_SUPPORTED`. 榮剛法人說明會簡報（**英文版**）載「**Gloria Material Technology Corp. (Ticker：5009)**」「Company profile」，並見「**alloy**」14次、「**specialty**」3次，支持其特殊合金鋼業務；惟「隸屬於**台灣鋼鐵集團（TSG）**」（「**TSG**」0次）、「具備**全製程**」（「integrated」0次）與「為台灣**唯一**」（「only」2次之上下文未見唯一性之完整表述）未獲支持。**方法論註記：本件為英文版文件，中文關鍵字檢索不具意義。**
- `9962:objective_ranking_or_market_share:b9679f9639e82fcf` — `PARTIALLY_SUPPORTED`. 有益文件中「**不銹鋼**」出現2次；惟「為台灣**唯一**且**全球前三大**不鏽鋼**厚板**專業廠」未獲支持（「**厚板**」「板材」「唯一」「前三大」均0次）。**重要侷限**：本批次所取得之文件為**民國95年度之財務報表暨會計師查核報告**（**非年報**，內容為財務報表，不含業務簡介或市場地位敘述），且**非近期版本**；建議複核者改取該公司之**年報或公開說明書**重查。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。UNKNOWN 追蹤清單已同步刷新至 **207 筆**。
- Author-reviewed total: **865 / 1,399**; remaining: **534**. Outcome counts: ACCEPTED 87, PARTIALLY_SUPPORTED 567, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 207. Next pending claim by priority: `2034:objective_ranking_or_market_share:9db08fbb1d4b60e5` (允強).

## Author batch `author-154` — 2026-10-11

- Reviewed the next three unreviewed objective ranking/market-share claims in checkpoint order (允強 2034, 中華電 2412 ×2). Evidence came from directly downloaded and inspected official disclosures: 中華電信2024年度年報（中文版）。
- `2034:objective_ranking_or_market_share:9db08fbb1d4b60e5` — `UNKNOWN_AFTER_RESEARCH`. 本批次檢視允強官方投資人專區頁面，**未提供可下載之年報 PDF 連結**；另檢索所及之 MOPS 端點為**財務報表**（t164sb01，非年報，不含業務簡介或市場地位敘述），未取得可檢視之年報或公開說明書。
- `2412:objective_ranking_or_market_share:a66e2cfee2300a0e` — `PARTIALLY_SUPPORTED`. 中華電信2024年度年報中「**5G**」115次、「**固網**」34次、「**用戶數**30次、「**ICT**」10次、「**行動通訊**」2次、「**數據通信**」2次（**四項業務皆獲對應之敘述**），且載其行動客戶數**市占達38.0%**、「皆**居同業之冠**」、「**大幅領先同業**」，支持其電信服務之領先地位；惟「隸屬政府持股之**國營事業轉民營**企業」未獲逐字支持（「**國營**」0次）。
- `2412:objective_ranking_or_market_share:de26eb6e820bab9c` — `ACCEPTED`. 年報**明文**載「（行）動**客戶數市占達38.0%**，113 全年行動營收市占達40.4%」「皆**居同業之冠**，且營收市占持續超越行動客戶市占」「中華電信的**5G 客戶數市占**較整體行動客戶數市占更勝一籌，達**38.8%**，**大幅領先同業**」——「**客戶數市占**」直接對應 claim 之「用戶數」，「**居同業之冠**」與「**大幅領先同業**」直接對應 claim 之「最大」，且「**5G**」115次充分支持其 5G 業務敘述。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。UNKNOWN 追蹤清單已同步刷新至 **208 筆**。
- Author-reviewed total: **868 / 1,399**; remaining: **531**. Outcome counts: ACCEPTED 88, PARTIALLY_SUPPORTED 568, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 208. Next pending claim by priority: `6163:objective_ranking_or_market_share:5fe18513d52e2e8a` (華電網).

## Author batch `author-155` — 2026-10-11

- Reviewed the next four unreviewed objective ranking/market-share claims in checkpoint order (是方 6561 ×3, 統振 6170). Evidence came from directly downloaded and inspected official disclosures: 是方電訊2023年度年報、統振法人說明會簡報。
- `6561:objective_ranking_or_market_share:8a87b4b5a9098e5e` — `PARTIALLY_SUPPORTED`. 是方年報中「**中華電**」84次、「**IDC**」73次、「**資料中心**」13次、「**中立**」8次，支持其集團歸屬與 IDC 業務；惟「（為其**最大股東**）」未見，且「是全台**規模最大**且保持高度中立之電信級 IDC 營運商」未獲支持——全份年報中「**最大**」4次之上下文**均非 IDC**（分別為 TPIX 交換中心、電信寬頻代理經銷體系、數據通信所通路商）。
- `6561:objective_ranking_or_market_share:06e71ebe14750575` — `PARTIALLY_SUPPORTED`. 年報載國際公有雲清單「廠(**AWS, Microsoft, Google, Oracle, IBM**, etc.)」，並載「**Azure ExpressRoute** 雲服務解決方案」「提供東京的 **Oracle** 公有雲直連服務」「台北直連**Azure** 雲端服務正式啟用」（「**AWS**」6次、「**Direct Connect**」1次），支持其為國際公有雲落地台灣之直連節點；惟「是全台**最大**的**海纜**交換中心」未獲逐字支持（海纜見12次，其敘述未含「最大」）。
- `6561:objective_ranking_or_market_share:e4ab212b6a0af4ad` — `PARTIALLY_SUPPORTED`. 年報見「**第一類電信**」與「**綠電**」之敘述，支持其上游包含第一類電信業者及綠電供應商；惟「[[伺服器]]製造商、機房設備廠」未獲逐字支持。
- `6170:objective_ranking_or_market_share:ea74cedd3701221c` — `PARTIALLY_SUPPORTED`. 統振法人說明會簡報中「**移工**」19次、「**匯兌**」7次，支持其外籍移工匯兌業務；惟「**QuickPay**」與「**首家**」均0次，「有效會員數**超過40萬人**」**與文件不符**（簡報載「總體市佔率擴大中, **有效會員超過30萬人**」，而「**40萬**」1次之上下文為**台灣外籍勞動力規模**「**40萬外來人力**，補足勞動力缺口」），「累計匯款金額逾 500 億元」與「市佔率約 40%」亦為0。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）；UNKNOWN 追蹤清單維持 **208 筆**。
- Author-reviewed total: **872 / 1,399**; remaining: **527**. Outcome counts: ACCEPTED 88, PARTIALLY_SUPPORTED 572, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 208. Next pending claim by priority: `6163:objective_ranking_or_market_share:5fe18513d52e2e8a` (華電網).

## Author batch `author-156` — 2026-10-11

- Reviewed the next two unreviewed objective ranking/market-share claims in checkpoint order (華電網 6163, 三芳 1307). Evidence came from directly downloaded and inspected official disclosures: 華電網法人說明會簡報、三芳Operating Information（英文版）。
- `6163:objective_ranking_or_market_share:5fe18513d52e2e8a` — `ACCEPTED`. 華電網法人說明會簡報**逐字載明**兩項實績：「• 建置台灣**第⼀套ADSL**寬頻網路(Cisco)」與「• 建置**亞洲最⼤**的**IPTV(MOD)**系統(Cisco)」（「**IPTV**」4次、「**MOD**」6次、「**ADSL**」1次、「中華電」8次、「建置」43次）；該處之範圍為「**亞洲**最大」，**涵蓋** claim 所述之最大 IPTV 系統，與 claim 之要素逐項對應。**註記**：簡報中「第**⼀**套」之「⼀」為 **U+2F00 康熙部首**字形（非一般漢字「一」U+4E00），以一般「第一」檢索將無法命中，屬**異體字形**造成之檢索落差（本審核第 8 類）。
- `1307:objective_ranking_or_market_share:dd1e646d1fa31e1b` — `PARTIALLY_SUPPORTED`. 三芳文件（**英文版**）載「The major products are **Microfiber artificial leather, PU synthetic leather**, films and fiber core technology of synthetic leather」（「**leather**」9次、「**synthetic**」4次、「PU」18次），支持其 PU 合成皮與人工皮革產品；惟「為**全球最大**之運動鞋用…製造商」未獲支持（「**largest**」「**market share**」「**footwear**」「**athletic**」均0次），「市佔率**逾40%**」亦未獲支持（「**40%**」2次之上下文於文字層中未見完整敘述）。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）；UNKNOWN 追蹤清單維持 **208 筆**。
- Author-reviewed total: **874 / 1,399**; remaining: **525**. Outcome counts: ACCEPTED 89, PARTIALLY_SUPPORTED 573, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 208. Next pending claim by priority: `1341:objective_ranking_or_market_share:c464f0b0ce8ffced` (富林-KY).

## Author batch `author-157` — 2026-10-11

- Reviewed the next four unreviewed objective ranking/market-share claims in checkpoint order (富林-KY 1341 ×2, 利華 1423, 福懋 1434). Evidence came from directly downloaded and inspected official disclosures: 富林法人說明會簡報（英文版）、利華法人說明會簡報、福懋99年度年報。
- `1341:objective_ranking_or_market_share:c464f0b0ce8ffced` — `PARTIALLY_SUPPORTED`. 富林法人說明會簡報（**英文版**）見「**leather**」34次、「**PU**」30次、「**PVC**」17次、「**Vietnam**」14次、「artificial」2次，支持其 PVC／PU 皮革產品與越南布局；惟「是越南**最大**的 PVC 人造皮革製造商」未獲支持（「**largest**」「**leading**」均0次；「人造皮革」「乳膠皮」「膠布」「柔軟皮」之中文詞亦均0次）。**方法論註記：本件為英文版文件，中文關鍵字檢索不具意義。**
- `1341:objective_ranking_or_market_share:f6b48a6d16324bcd` — `UNKNOWN_AFTER_RESEARCH`. 簡報中「**Ashley**」之出現次數為0，未載「[[Ashley]]（美國最大家具商）」之具名客戶。
- `1423:objective_ranking_or_market_share:bb8fd0329f920772` — `PARTIALLY_SUPPORTED`. 利華法人說明會簡報載「喀什米爾特性的**羊毛**介紹 Cashmere–like wool」（「**羊毛**」19次、「**防縮**」4次、「**毛條**」1次），支持其羊毛防縮處理及毛條業務；惟「是台灣**唯一**…製造廠」未獲支持（「**唯一**」0次）。
- `1434:objective_ranking_or_market_share:78a69698062119b8` — `PARTIALLY_SUPPORTED`. 福懋99年度年報中「**織布**」48次、「**聚酯**」26次、「供應」26次，支持其紡織業務；惟「**簾布**事業群為台灣**最大輪胎簾布**製造商，供應國內外輪胎大廠」未獲支持——全份年報中「**簾布**」與「**輪胎**」之出現次數**均為0**。**重要侷限**：該年報為**民國99年度**版本（非近期），且**公司名以相容表意字排版**（封面作「**福懋**」，非標準「福」），以標準字形檢索可能無法命中；建議改取較近年度之年報或公開說明書重查。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。UNKNOWN 追蹤清單已同步刷新至 **209 筆**。
- Author-reviewed total: **878 / 1,399**; remaining: **521**. Outcome counts: ACCEPTED 89, PARTIALLY_SUPPORTED 576, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 209. Next pending claim by priority: `1440:objective_ranking_or_market_share:95d130b7d3a12dab` (南紡).

## Author batch `author-158` — 2026-10-11

- Reviewed the next two unreviewed objective ranking/market-share claims in checkpoint order (南紡 1440, 力鵬 1447). Evidence came from directly downloaded and inspected official disclosures: 南紡110年度年報、力鵬106年度年報。
- `1440:objective_ranking_or_market_share:95d130b7d3a12dab` — `ACCEPTED`. 南紡110年度年報**逐字載**「南紡以棉紗事業起家，並逐步向上游纖維製造及下游織布等發展，**為國內最大棉紗廠**」（其「最大」之程度**強於** claim 所述之「之一」）；四項產品於年報中各有對應敘述（「棉紗」7次、「**聚酯粒**」12次、「**聚酯棉**」15次、「**機能**」4次），「**越南**」26次支持其產能布局。
- `1447:objective_ranking_or_market_share:2c3ecc5fc9630935` — `ACCEPTED`. 力鵬106年度年報**逐字載**「（一貫化）流程，**為亞洲地區最大之Nylon 6 粒製造商**」（「**尼龍粒**」24次、「一貫」7次），「**力麗**」15次、「集團」6次支持其集團歸屬。**對照註記**：同份年報另載「產能將由800噸提升至1,100噸，**成為全球最大尼龍粒供應商為目標**」——該句為**目標敘述**（未來），與上引之「為亞洲地區最大」（現狀）性質不同；本 claim 係就現狀而為，故採認。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）；UNKNOWN 追蹤清單維持 **209 筆**。
- Author-reviewed total: **880 / 1,399**; remaining: **519**. Outcome counts: ACCEPTED 91, PARTIALLY_SUPPORTED 576, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 209. Next pending claim by priority: `1451:objective_ranking_or_market_share:e4b27d6e2db182fd` (年興).

## Author batch `author-159` — 2026-10-11

- Reviewed the next four unreviewed objective ranking/market-share claims in checkpoint order (東隆興 4401, 金洲 4417, 利勤 4426 ×2). Evidence came from directly downloaded and inspected official disclosures: 東隆興法人說明會簡報（中英對照）、金洲法人說明會簡報、利勤112年度年報。
- `4401:objective_ranking_or_market_share:6969f05f343aab89` — `PARTIALLY_SUPPORTED`. 東隆興法人說明會簡報（中英對照）見「**yarn**」10次、「**Nylon**」2次、「sportswear」2次，支持其線紗及尼龍業務；惟「**亞洲最大**」未獲支持（「largest」「Asia」均0次），「尼龍 66」「機能性加工絲」「領導」之中文詞亦均0次。
- `4417:objective_ranking_or_market_share:1a2bf66757d1745b` — `PARTIALLY_SUPPORTED`. 金洲法人說明會簡報載「●各種漁具、**漁網**、線(繩)、索等之製造、加工、內外銷業務」，並載其市場地位之**量化敘述**——「**數量位居全球第㇐（一），其規模是第2至第5名總和的三倍，排名第2至第5依（序）**」（「**漁網**」7次、「海洋」7次），**該敘述不僅支持「全球前三大」，實已載明其位居全球第一**；惟「**台灣第一大**」（簡報未以該詞表述）與「以自有品牌 **King Net** 行銷全球」（「**King Net**」0次）未獲支持。**字形註記**：文中「第**㇐**」為 **CJK 筆畫字元**（非漢字「一」），以「第一」檢索無法命中——此為本審核第 8 類字形落差之又一實例（繼 U+2F00 康熙部首、U+FA1B 相容表意字之後）。
- `4426:objective_ranking_or_market_share:61a3927d443dd49c` — `PARTIALLY_SUPPORTED`. 利勤112年度年報中「**立體織物**」22次、「**Spacer**」1次，並載「**立體織物為主力**」及「94年06月本公司與NIKE 合作研發，並由本公司生產之第一塊全電腦無接縫鞋型圖案**立體織物**」，支持其 3D 立體織物業務；惟「為**全球最大**之…領導廠商」未獲支持（「**全球最大**」0次）。
- `4426:objective_ranking_or_market_share:892c19ef3e0b894a` — `PARTIALLY_SUPPORTED`. 年報中「**Nike**」10次、「Adidas」2次，並載「**本公司與NIKE 合作研發**」，支持其與 Nike 之研發合作關係；惟「（**最大客戶，長期核心供應商**）」未獲逐字支持（「**最大客戶**」0次），「Reebok」「Asics」「New Balance」亦均0次。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）；UNKNOWN 追蹤清單維持 **209 筆**。
- Author-reviewed total: **884 / 1,399**; remaining: **515**. Outcome counts: ACCEPTED 91, PARTIALLY_SUPPORTED 580, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 209. Next pending claim by priority: `1451:objective_ranking_or_market_share:e4b27d6e2db182fd` (年興).

## Author batch `author-160` — 2026-10-11

- Reviewed the next two unreviewed objective ranking/market-share claims in checkpoint order (年興 1451, 冠星-KY 4439). Evidence came from directly downloaded and inspected official disclosures: 年興投資人說明會簡報、冠星民國109年及108年第一季合併財務報告。
- `1451:objective_ranking_or_market_share:e4b27d6e2db182fd` — `UNKNOWN_AFTER_RESEARCH`. 年興投資人說明會簡報載「營運項目：織布／紡紗／成衣」「**牛仔布**」「牛仔褲裝」與「全球佈局：墨西哥、台灣、賴索托、越南」（「**牛仔**」10次），支持其牛仔布及成衣業務；**惟全份簡報中「客戶」與「品牌」之出現次數均為0**，「Levi」「Lee」「EDWIN」「CK」「DKNY」亦均為0，未具名任何客戶或品牌，故「[[Levi's]]（最大客戶）、[[LEE]]、[[EDWIN]]、[[CK]]、[[DKNY]]」未獲確立。
- `4439:objective_ranking_or_market_share:08e2b4dca14ff3c3` — `UNKNOWN_AFTER_RESEARCH`. 本批次所取得之冠星文件為**民國109年及108年第一季合併財務報告暨會計師核閱報告**（**財務報告而非年報**，內容為會計師核閱報告與財務報表，不含業務簡介或客戶敘述），其中「**adidas**」「**Gap**」「**Puma**」「**Decathlon**」「**Li-Ning**」與「**customer**」之出現次數**均為0**；本批次未取得該公司之年報或公開說明書。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。UNKNOWN 追蹤清單已同步刷新至 **211 筆**。
- Author-reviewed total: **886 / 1,399**; remaining: **513**. Outcome counts: ACCEPTED 91, PARTIALLY_SUPPORTED 580, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 211. Next pending claim by priority: `5475:objective_ranking_or_market_share:71e82525f40ff47e` (德宏).

## Author batch `author-161` — 2026-10-11

- Reviewed the next four unreviewed objective ranking/market-share claims in checkpoint order (德宏 5475, 光隆 8916, 百和 9938 ×2). Evidence came from directly downloaded and inspected official disclosures: 德宏法人說明會簡報、光隆法人說明會簡報、百和法人說明會簡報。
- `5475:objective_ranking_or_market_share:71e82525f40ff47e` — `PARTIALLY_SUPPORTED`. 德宏法人說明會簡報載「◼主要產品：**E玻纖布及石英紗、布產銷**」，並見「**石英**」18次、「**玻纖布**」3次、「**Q-Glass**」2次、「**電子級**」3次，支持其該兩項產品業務；惟「為台灣**第三大**電子級玻纖布廠」（「第三大」0次）與「為台灣**唯一**具備石英纖維布量產能力之業者」（「**唯一**」0次）未獲支持。
- `8916:objective_ranking_or_market_share:94054a91233ed989` — `PARTIALLY_SUPPORTED`. 光隆法人說明會簡報中「**羽絨**」10次、「**垂直整合**」1次（「深度供應鏈連結，賦能**垂直整合**服務」），支持其羽絨及垂直整合業務；惟「成立於 **1966** 年」（0次）、「總部位於台灣**台北**」（0次）與「為全球羽絨產業**唯一**整合上游羽絨原料**精洗**生產與下游成衣及家居紡織製造的垂直整合供應商」（「**唯一**」「精洗」均0次）未獲支持。
- `9938:objective_ranking_or_market_share:d3614a1e78765800` — `PARTIALLY_SUPPORTED`. 百和法人說明會簡報載「**1979** 成立初期稱為三合興公司，提供客戶『**黏扣帶**』產品」（「**黏扣帶**」16次、「1979」2次），支持其成立年分與產品；惟「總部位於台灣**彰化**」（0次）、「為**全球最大**之黏扣帶與鞋用輔料製造商之一」（0次）與「（**Hook & Loop**）」（「Hook」0次）未獲支持。
- `9938:objective_ranking_or_market_share:75e89fb7124e96b1` — `PARTIALLY_SUPPORTED`. 簡報載「2014 獲邀**Adidas** A-Team成員-全球僅11家具前瞻性開發之供應商」與「百和為全球唯一副料供應商；**獲選Nike成衣『先鋒供應商』-策略性夥伴**」，**明文載明與兩大品牌之供應關係**；惟「（**最大品牌佔比約 23%**）」（「23%」1次之上下文未見完整敘述）、「（約 **19%**）」（0次）與「[[On Running]]、[[Hoka]]」（均0次）未獲支持。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）；UNKNOWN 追蹤清單維持 **211 筆**。
- Author-reviewed total: **890 / 1,399**; remaining: **509**. Outcome counts: ACCEPTED 91, PARTIALLY_SUPPORTED 584, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 211. Next pending claim by priority: `6832:objective_ranking_or_market_share:e80b2b9b51da51df` (金鼎科).

## Author batch `author-162` — 2026-10-11

- Reviewed the next four unreviewed objective ranking/market-share claims in checkpoint order (金鼎科 6832, 鑽全 1527, 中砂 1560 ×2). Evidence came from directly downloaded and inspected official disclosures: 鑽全法人說明會簡報、中砂法人座談簡報。
- `6832:objective_ranking_or_market_share:e80b2b9b51da51df` — `UNKNOWN_AFTER_RESEARCH`. 本批次就金鼎科進行官方文件檢索，**未查得該公司本身之官方端點或可檢視之官方文件**；檢索所及者為**中國 A 股之「廣東金鼎光學技術股份有限公司」**，與本標的**並非同一法人**（依身分不符原則不予採用）。
- `1527:objective_ranking_or_market_share:2cd5717ea34e0ce8` — `PARTIALLY_SUPPORTED`. 鑽全法人說明會簡報載「• **創立日期：民國72年**」（民國72年＝1983年），並見「**釘槍**」1次、「**代工**」2次、「**氣動**」2次，支持其成立年分與業務；惟「總部位於台灣**台中**工業區」（「台中」0次）與「為**全球最大**氣動釘槍（Pneumatic Nailer）代工廠」（「全球最大」「Nailer」均0次）未獲支持。**方法論註記**：簡報以**民國年**表述創立日期，故以「1983」檢索為0（第 1 類字串落差）。
- `1560:objective_ranking_or_market_share:4fb13831c5b7dbba` — `PARTIALLY_SUPPORTED`. 中砂法人座談簡報中「**鑽石碟**」13次、「**Diamond Disk**」10次、「**CMP**」14次、「**修整**」7次、「再生晶圓」8次，支持其鑽石碟（CMP 修整器）及再生晶圓業務；惟「為[[台積電]]先進製程（3nm/2nm）的**核心耗材**」（「**台積電**」0次）、「**市佔率領先**」（「市佔」「領先」均0次）與「三大事業體」未獲支持。
- `1560:objective_ranking_or_market_share:06635179641a8d57` — `UNKNOWN_AFTER_RESEARCH`. 簡報中「**台積電**」「**最大單一**」與「**六成**」之出現次數**均為0**，未具名該等客戶或載明出貨占比。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。UNKNOWN 追蹤清單已同步刷新至 **213 筆**。
- Author-reviewed total: **894 / 1,399**; remaining: **505**. Outcome counts: ACCEPTED 91, PARTIALLY_SUPPORTED 586, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 213. Next pending claim by priority: `1541:objective_ranking_or_market_share:d200dd9c531c0610` (錩泰).

## Author batch `author-163` — 2026-10-11

- Reviewed the next two unreviewed objective ranking/market-share claims in checkpoint order (錩泰 1541 ×2). Evidence came from directly downloaded and inspected official disclosures: 錩泰投資人簡報（英文版）。
- `1541:objective_ranking_or_market_share:d200dd9c531c0610` — `PARTIALLY_SUPPORTED`. 錩泰投資人簡報（**英文版**）載「**Sales by Area**」並見其美國子公司「**Delta Power Equipment Corporation**」（Place: **Spartanburg County SC**），支持其北美市場布局；惟「**最大客戶為 [[Stanley Black & Decker]]**」未獲支持（「**Stanley**」與「最大客戶」均0次）。
- `1541:objective_ranking_or_market_share:57a50cd0ac0fa618` — `PARTIALLY_SUPPORTED`. 簡報中「**DEWALT**」出現1次；惟「**最大客戶**」（0次）、「代工 **CRAFTSMAN** 品牌」（0次）與「**圓鋸機**」（0次；簡報之產品類別為「Woodworking Machines」）未獲支持。
- **來源取得註記**：本批次併同嘗試之 MOPS 年報端點（t100sa11_1541_112.pdf）回傳 **320 bytes 之非文件內容**，未取得可檢視之年報；本次判定係基於 2017 年之英文投資人簡報。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）；UNKNOWN 追蹤清單維持 **213 筆**。
- Author-reviewed total: **896 / 1,399**; remaining: **503**. Outcome counts: ACCEPTED 91, PARTIALLY_SUPPORTED 588, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 213. Next pending claim by priority: `1570:objective_ranking_or_market_share:c4ddcbe07eeee869` (力肯).

## Author batch `author-164` — 2026-10-11

- Reviewed the next five unreviewed objective ranking/market-share claims in checkpoint order (力肯 1570, 駿吉-KY 1591, 世鎧 2063 ×3). Evidence came from directly downloaded and inspected official disclosures: 力肯主要產品類別簡報、駿吉公司簡報、世鎧法人說明會簡報。
- `1570:objective_ranking_or_market_share:c4ddcbe07eeee869` — `PARTIALLY_SUPPORTED`. 力肯簡報載「專業級氣動**釘槍**」「電動**釘槍**」（「**釘槍**」2次），支持其釘槍產品業務；惟「**美國**知名釘槍**品牌**為其**最大客戶**」未獲支持（「**最大客戶**」「**美國**」「品牌」均0次）。
- `1591:objective_ranking_or_market_share:01629e23762694d3` — `PARTIALLY_SUPPORTED`. 駿吉簡報載「**1989年3月**」與「工業用**氣動式風槍釘**」，並見「**馬來西亞**」2次、「**開曼**」2次，支持其成立年分、產品及註冊地；惟「（前身為 **1990** 年設立之馬來西亞工廠）」（0次）、「為**東南亞最大**規模之…製造商」（「東南亞」「最大」均0次）與「（**特殊鋼釘**）」（0次）未獲支持。
- `2063:objective_ranking_or_market_share:7739d7e6a87f3c8e` — `PARTIALLY_SUPPORTED`. 世鎧法人說明會簡報**逐字載**「**公司成立 : 西元 1992 / 4 月 ( 西元 2010 / 9 月上櫃 )**」（「**複合螺絲**」12次）；惟「總部位於台灣**高雄**」（0次）、「為台灣**最大**複合螺絲製造商」（0次）與「高雄扣件產業聚落之重要成員」未獲支持。
- `2063:objective_ranking_or_market_share:8917b6e2421fdaa3` — `PARTIALLY_SUPPORTED`. 簡報中「**歐洲**」5次，支持其與歐洲市場之關聯；惟「歐洲為**最大市場**」（0次）、「（市佔率約 **24%**）」與「為**全球前二大**複合螺絲供應商」（0次）未獲支持。**關鍵發現**：全份簡報中「**24%**」1次之上下文為**營收衰退幅度**——「(1) 螺絲事業營收相較同期**減少近24%**」，**並非市占率**。
- `2063:objective_ranking_or_market_share:d1d0957d7c075d6d` — `UNKNOWN_AFTER_RESEARCH`. 簡報中「**Würth**」「**Hilti**」「**Home Depot**」「**Lowe's**」之出現次數**均為0**，未具名任何通路，且「24%」為營收衰退幅度而非市占率。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。UNKNOWN 追蹤清單已同步刷新至 **214 筆**。
- Author-reviewed total: **901 / 1,399**; remaining: **498**. Outcome counts: ACCEPTED 91, PARTIALLY_SUPPORTED 592, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 214. Next pending claim by priority: `2049:objective_ranking_or_market_share:1bbe1fedf9ba0664` (上銀).

## Author batch `author-165` — 2026-10-11

- Reviewed the next two unreviewed objective ranking/market-share claims in checkpoint order (上銀 2049, 世鎧 2063). Evidence came from directly downloaded and inspected official disclosures: 上銀2020年度年報、世鎧法人說明會簡報。
- `2049:objective_ranking_or_market_share:1bbe1fedf9ba0664` — `PARTIALLY_SUPPORTED`. 上銀2020年度年報（文字擷取316,050字元）中「**滾珠螺桿**」81次、「**線性滑軌**」67次、「**HIWIN**」85次、「**1989**」5次、「**台中**」29次，**充分支持**其成立年分、總部地點、自有品牌與兩項主要產品；惟「為**全球第二大**滾珠螺桿製造商」（0次）、「**全球前三大**線性滑軌製造商」（0次）與「與日商 [[THK]] 及 [[NSK]] 合計**市佔率超過七成**」（「THK」「NSK」「七成」均0次）未獲支持；「**市佔**」1次之上下文為**目標敘述**（「提高工業機器人與醫療機器人**市占率**」）。
- `2063:objective_ranking_or_market_share:6515f294bf11593a` — `PARTIALLY_SUPPORTED`. 世鎧法人說明會簡報中「**歐洲**」出現5次，支持其與歐洲市場之關聯；惟「**歐洲建材通路商**」（「建材」「通路商」均0次）、「**五金經銷商**」（「五金」「經銷商」均0次）與「（**最大市場**）」（0次）未獲支持。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）；UNKNOWN 追蹤清單維持 **214 筆**。
- Author-reviewed total: **903 / 1,399**; remaining: **496**. Outcome counts: ACCEPTED 91, PARTIALLY_SUPPORTED 594, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 214. Next pending claim by priority: `2065:objective_ranking_or_market_share:d09032770245bcd5` (世豐).

## Author batch `author-166` — 2026-10-11

- Reviewed the next four unreviewed objective ranking/market-share claims in checkpoint order (世豐 2065, 豐達科 3004 ×2, 強信-KY 4560). Evidence came from directly downloaded and inspected official disclosures: 世豐104年度年報、強信法人說明會簡報。
- `2065:objective_ranking_or_market_share:d09032770245bcd5` — `PARTIALLY_SUPPORTED`. 世豐104年度年報中「**歐洲**」出現4次，支持其與歐洲市場之關聯；惟「歐洲**建材**（通路商）」（「建材」0次）、「**五金**（通路商）」（「五金」0次）與「（**最大市場**）」（「最大市場」「通路」均0次）未獲支持。**字形註記**：該年報封面之公司名作「世豐**螺**絲」，其「**螺**」為**相容表意字**（非標準「螺」U+87BA），**故以「螺絲」檢索為0**——此為本審核第 7／8 類字形落差之又一實例（與福懋之「福」、華電網之「⼀」、金洲之「㇐」同型）。
- `3004:objective_ranking_or_market_share:b2cfe0c3e68357a9` — `UNKNOWN_AFTER_RESEARCH`. 所取得之豐達科年報（145,405字元）之**文字層呈現系統性字元位移之亂碼**（封面中文作「**ද೯ިި**」「**ҁϦљԃൔ࣬**」等，英文部分「National Aerospace Fasteners Corporation」則可辨識），擷取過程並出現多次「**MuPDF error: format error: non-page object in page tree**」結構錯誤；「航太」「扣件」「引擎」「唯一」「認證」之出現次數均為0。
- `3004:objective_ranking_or_market_share:6e42f02d92f00cdb` — `UNKNOWN_AFTER_RESEARCH`. 本 claim 為同一文件之條目表述（「[[神基投控]]（3005）— 最大股東（約 40%）」）；年報文字層為亂碼，「**神基**」「**最大股東**」之出現次數均為0。
- `4560:objective_ranking_or_market_share:1dbc11a600b8a933` — `PARTIALLY_SUPPORTED`. 強信法人說明會簡報載「**強信機械科技(萊州)有限公司**，1,222人」與「品項，客戶為全球10大工業縫紉機品牌，**為全球最大工業縫紉機零配（件）**」（「**縫紉機**」5次、「**STRONG H**」3次、「**萊州**」1次），**逐字支持**其「全球最大工業縫紉機零配件製造商」及萊州生產基地；惟「註冊於**開曼群島**」（0次）與「生產基地位於中國**山東**萊州」（0次）未獲支持。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。UNKNOWN 追蹤清單已同步刷新至 **216 筆**。
- Author-reviewed total: **907 / 1,399**; remaining: **492**. Outcome counts: ACCEPTED 91, PARTIALLY_SUPPORTED 596, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 216. Next pending claim by priority: `4571:objective_ranking_or_market_share:9128f3d0f1a0417a` (鈞興-KY).

## Author batch `author-167` — 2026-10-11

- Reviewed the next three unreviewed objective ranking/market-share claims in checkpoint order (鈞興-KY 4571, 三星 5007, 久陽 5011). Evidence came from directly downloaded and inspected official disclosures: 鈞興2024年度年報、三星法人說明會簡報、久陽法人說明會簡報。
- `4571:objective_ranking_or_market_share:9128f3d0f1a0417a` — `UNKNOWN_AFTER_RESEARCH`. 鈞興年報（93,410字元）中「**齒輪**」174次、「鈞興」74次、「**客戶**」104次，顯示其有齒輪業務與客戶敘述；惟「**創科**」「**TTI**」「**Techtronic**」與「**Milwaukee**」「**Ryobi**」之出現次數**均為0**，未具名該客戶或其品牌。
- `5007:objective_ranking_or_market_share:4847fe2cc4ab7293` — `PARTIALLY_SUPPORTED`. 三星法人說明會簡報載「**1965年7月2日成立**」（**逐字支持**成立年分）與「**產業地位：全球最大汽車螺帽製造廠**」，並載「螺帽和螺絲**95%以上外銷歐美日地區**，**螺帽出口量占台灣（總出口量約六分之一）**」（「**螺帽**」19次、「出口」13次）。**範圍差異註記**：claim 稱「為**全球最大螺帽製造商**」，而簡報原文為「全球最大**汽車**螺帽製造廠」——**claim 省略了「汽車」之限定而將其一般化**。另「總部位於台灣**高雄**」（0次）與「**台灣最大**螺帽出口商」（0次；簡報僅載出口量占比）未獲支持。
- `5011:objective_ranking_or_market_share:858cd671ae58c706` — `PARTIALLY_SUPPORTED`. 久陽法人說明會簡報載「業務項目從螺絲製造擴展至環保、能源產業」「成長為持有五家子公司的久陽集團」，並見「**螺栓**」4次、「**六角**」2次、「**扣件**」1次、「**1984**」1次，支持其成立年分與產品；惟「總部位於台灣**高雄**」（0次）、「隸屬於**台灣鋼鐵集團（TSG）**」（0次）與「外銷」（0次）未獲支持。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。UNKNOWN 追蹤清單已同步刷新至 **217 筆**。
- Author-reviewed total: **910 / 1,399**; remaining: **489**. Outcome counts: ACCEPTED 91, PARTIALLY_SUPPORTED 598, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 217. Next pending claim by priority: `5015:objective_ranking_or_market_share:2276d54bba3d3a65` (華祺).

## Author batch `author-168` — 2026-10-12

- Reviewed the next four unreviewed objective ranking/market-share claims in checkpoint order (華祺 5015, 數泓科 6855, 伯鑫 6904, 大國鋼 8415). Evidence came from directly downloaded and inspected official disclosures: 華祺法人說明會簡報、數泓114年度年報、大國鋼法人說明會簡報。
- `5015:objective_ranking_or_market_share:2276d54bba3d3a65` — `PARTIALLY_SUPPORTED`. 華祺法人說明會簡報中「**不銹鋼**」出現2次（以「銹」表述），支持其不銹鋼產品業務；惟「總部位於台灣**桃園**」（0次）、「（**小螺絲**）」（0次）與「為**全球最大**不銹鋼小螺絲專業製造商」（0次）未獲支持。
- `6855:objective_ranking_or_market_share:dbc4554952212ac3` — `PARTIALLY_SUPPORTED`. 數泓114年度年報中「**手工具**」72次、「**研發**」36次、「**上櫃**」27次、「**智能**」6次，支持其手工具業務與研發、上櫃敘述；惟「成立於 **2006** 年」（0次）、「為台灣**首家**」（0次）與「也是**唯一**具備『**數位**智能手工具』完整研發與製造能力」（「唯一」「數位」均0次）未獲支持。
- `6904:objective_ranking_or_market_share:c9e2cfd9b443469d` — `UNKNOWN_AFTER_RESEARCH`. 本批次自發行人官方網域下載「113年股東會年報」端點，**所取得之檔案並非年報本身，而係該公司官方網站之「股東專區」導覽／下載頁面**（文字擷取僅1,284字元，內容為網站選單與年報下載連結清單及各年度「下載」欄位），**不含年報之實質內容**；「全球最大」「25%」「市佔」之出現次數均為0。
- `8415:objective_ranking_or_market_share:5d18e323f2d8e7b8` — `PARTIALLY_SUPPORTED`. 大國鋼法人說明會簡報載「**成立日期：2008年**」與「核心服務：**採購整合、電子商務銷售(B2B)及實體配銷**」，並見「Brighton」3次、「BBI」2次、「扣件」11次、「配銷」1次。**範圍差異註記**：簡報之市場地位原文為「目前為**全美最大**不銹鋼通路商」與「**全美最大扣件通路商**」，而 claim 所用者為「**北美**最大」——**「全美」（美國）與「北美」（含加拿大、墨西哥）為不同範圍**，claim 之範圍**大於**官方敘述；「**北美**」之出現次數為0。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。UNKNOWN 追蹤清單已同步刷新至 **218 筆**。
- Author-reviewed total: **914 / 1,399**; remaining: **485**. Outcome counts: ACCEPTED 91, PARTIALLY_SUPPORTED 601, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 218. Next pending claim by priority: `8415:objective_ranking_or_market_share:016f3d5d3ac36d27` (大國鋼).

## Author batch `author-169` — 2026-10-12

- Reviewed the next five unreviewed objective ranking/market-share claims in checkpoint order (大國鋼 8415 ×2, 嘉里大榮 2608 ×3). Evidence came from directly downloaded and inspected official disclosures: 大國鋼法人說明會簡報、嘉里大榮2025年前三季業績發表會簡報。
- `8415:objective_ranking_or_market_share:016f3d5d3ac36d27` — `UNKNOWN_AFTER_RESEARCH`. 大國鋼簡報中「**6.74%**」「**BBI-USA**」與「**進口**」之出現次數**均為0**，未載該具名子公司之市占率數字。
- `8415:objective_ranking_or_market_share:1ca8b457e27ce836` — `PARTIALLY_SUPPORTED`. 簡報載「核心服務：**採購整合、電子商務銷售(B2B)及實體配銷**」（「Brighton」3次、「BBI」2次、「扣件」11次、「配銷」1次、「平台」1次）；惟「**北美**最大」（0次；簡報之範圍為「全美」）、「整合**倉儲**」（0次）與「及**物流**」（0次）未獲支持。
- `2608:objective_ranking_or_market_share:8bdb0d8de660d7b1` — `PARTIALLY_SUPPORTED`. 嘉里大榮簡報載「**3,350+ 營業車輛**」（**逐字支持**），並見「物流中心」2次、「營業站」2次。**惟多項數字與文件不符**：「營運據點達 **190 處**」（簡報為「**160 營業據點**」）、「含 **11 座**物流中心及 **92 個**營業站」（簡報為「**90/10 營業站所/物流中心**」）與「國內貨運**市佔率約 35%**」（「市佔」0次）；「最綿密之配送網絡」亦為0次。
- `2608:objective_ranking_or_market_share:8073210a19686ced` — `PARTIALLY_SUPPORTED`. 簡報「十大核心項目」載「**醫藥物流 車輛/據點：234/13**」，並見「醫藥」4次、「醫藥倉/空調倉」，支持其醫藥物流業務；惟「子公司**嘉里醫藥物流**」（0次）、「為全台**唯一**專業開放型醫藥物流商」（0次）、「市佔率達**五成**」（0次）與「符合 **PIC/S GDP** 規範」（「PIC/S」0次）未獲支持。
- `2608:objective_ranking_or_market_share:31d8ab6170333d31` — `UNKNOWN_AFTER_RESEARCH`. 簡報中「**嘉里醫藥**」與「**五成**」之出現次數**均為0**，未載該具名子公司名稱或市占率數字。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。UNKNOWN 追蹤清單已同步刷新至 **220 筆**。
- Author-reviewed total: **919 / 1,399**; remaining: **480**. Outcome counts: ACCEPTED 91, PARTIALLY_SUPPORTED 604, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 220. Next pending claim by priority: `5604:objective_ranking_or_market_share:16da157ef7a9024f` (中連).

## Author batch `author-170` — 2026-10-12

- Reviewed the next five unreviewed objective ranking/market-share claims in checkpoint order (中連 5604 ×3, 大台北 9908 ×2). Evidence came from official disclosure endpoints.
- `5604:objective_ranking_or_market_share:16da157ef7a9024f`、`0e3541b15942f7ee` 與 `b23601c5085ed50f` — `UNKNOWN_AFTER_RESEARCH`. 本批次就中連進行官方文件檢索，遭遇兩類限制：**(1) 所取得之第三方文件經檢視並非中連之文件**——該檔（700,412字元）內容為**另一公司之公開說明書**（文中載「**福貞台灣新竹廠**」「台灣廠：新竹縣新豐鄉建興路2段372號」「2022年收購TSMP公司股權」等，為**福貞-KY**之公開說明書），**「中連」之出現次數為0**，屬**身分不符**，不予採用；**(2) 本批次另嘗試之 MOPS 年報端點（t100sa11_5604_110／111／112.pdf）三者皆回傳 320 bytes 之非文件內容**。三筆 claim 之核心（[[新竹物流]]為最大承租戶、承租約半數場站土地）因而未獲確立。
- `9908:objective_ranking_or_market_share:41dadca39e0dbe40` 與 `31cc2bfe1d4bcbbb` — `UNKNOWN_AFTER_RESEARCH`. 本批次自大台北官方網域下載文件時回應 **HTTP 403（禁止）**，未取得可檢視之檔案；「成立於1964年、大台北地區最大且歷史最悠久之天然氣公用事業」與「台北市及新北市數十萬戶家庭住宅天然氣用戶（最大客戶群）」因而未獲確立。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。UNKNOWN 追蹤清單已同步刷新至 **225 筆**。
- Author-reviewed total: **924 / 1,399**; remaining: **475**. Outcome counts: ACCEPTED 91, PARTIALLY_SUPPORTED 604, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 225. Next pending claim by priority: `6977:objective_ranking_or_market_share:578892ccae2b59f4` (聯純).

## Author batch `author-171` — 2026-10-12

- Reviewed the next six unreviewed objective ranking/market-share claims in checkpoint order (聯純 6977, 森崴能源 6806, 雲豹能源 6869 ×2, 富威電力 6994 ×2). Evidence came from directly downloaded and inspected official disclosures: 聯純公司資料表、森崴能源公司文件、雲豹能源年報。
- `6977:objective_ranking_or_market_share:578892ccae2b59f4` — `PARTIALLY_SUPPORTED`. 聯純公司資料表中「**超純水**」6次、「**水處理**」6次，支持其該項業務；惟「**日月光**」「**矽品**」「**超豐**」與「供應鏈」之出現次數**均為0**。
- `6806:objective_ranking_or_market_share:8a5ced4ccef9e61c` — `PARTIALLY_SUPPORTED`. 森崴能源文件中「**離岸風電**」19次、「**統包**」6次、「**EPC**」3次、「**正崴**」2次，支持其集團歸屬與業務；惟「為台灣**最大本土**離岸風電統包工程商」未獲支持——「**最大**」1次之上下文為**產業成長敘述**（「其中以太陽能設置量成長幅度**最大**」），「本土」1次之上下文為**國產化政策**（「國產項目應達申設容量之60%」），「統包」之出現分屬**富崴能源**、液化天然氣與台電二期等專案。
- `6869:objective_ranking_or_market_share:e69c35c8ab2af08d` — `PARTIALLY_SUPPORTED`. 雲豹能源年報載「本公司之轉投資子公司『**天能綠電股份有限公司**』**取得售電業執照**」與「子公司**天能綠電**協助**玉山金控**完成集團首筆**綠電轉供**」（「**天能綠電**」12次、「**綠電**」62次、「**售電**」38次）；惟「為台灣**最大民間**綠電售電平台」（「最大」之上下文為**太陽能電廠**）、「2024年營收**突破 10 億元**（年增 **338%**）」（「10億」「338%」均0次）、「長約保障已達 **160 億度**電」（0次）與「合約總價值約 **880 億元**」（0次）未獲支持。
- `6869:objective_ranking_or_market_share:7e2d1e75d0b3577d` — `PARTIALLY_SUPPORTED`. 年報支持 [[天能綠電]] 為綠電**售電平台**；惟「台灣**最大民間**綠電售電平台」未獲支持——年報中「**最大**」之上下文**均為太陽能電廠**（「全台最大地層下陷區太陽能電廠」「亞洲最大薄膜屋頂型」）。
- `6994:objective_ranking_or_market_share:2ce556a2bce652ca` 與 `4a494708c5380bf7` — `UNKNOWN_AFTER_RESEARCH`. 本批次就富威電力（**6994**）進行官方文件檢索，**所取得之檔案經檢視並非富威電力之文件**——該檔封面載「**兆聯實業股份有限公司 MEGA UNION TECHNOLOGY INCORPORATED 一一四年度年報**」「**股票代號：6944**」，為**兆聯實業（6944）之年報**，**「富威」之出現次數為0**，屬**身分不符**，不予採用；且該檔文字層**部分為字元位移之亂碼**。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。UNKNOWN 追蹤清單已同步刷新至 **227 筆**。
- Author-reviewed total: **930 / 1,399**; remaining: **469**. Outcome counts: ACCEPTED 91, PARTIALLY_SUPPORTED 608, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 227. Next pending claim by priority: `6803:objective_ranking_or_market_share:d6b824ac14940918` (崑鼎).

## Author batch `author-172` — 2026-10-12

- Reviewed the next four unreviewed objective ranking/market-share claims in checkpoint order (崑鼎 6803, 日友 8341 ×3). Evidence came from directly downloaded and inspected official disclosures: 崑鼎114年度年報、日友公司簡報。
- `6803:objective_ranking_or_market_share:d6b824ac14940918` — `PARTIALLY_SUPPORTED`. 崑鼎114年度年報中「**中鼎**」95次、「**焚化廠**」86次、「**綠能環保**」73次、「**營運管理**」23次、「控股」13次，**充分支持**其集團歸屬與焚化廠營運管理業務；惟「為**台灣最大**垃圾焚化廠營運管理商」未獲支持——全份年報中「**最大**」9次之上下文**均為泛用語**（「為股東追求**最大**利益」「年**最大**⼀日降雨量」「**最大**連續不降雨日數」「本公司整體之**最大**利益」），**無一為市場地位表述**。
- `8341:objective_ranking_or_market_share:8859f2ab9e89b9b4` — `ACCEPTED`. 日友公司簡報**逐字載**「**日友公司是臺灣第一家專業生物醫療廢棄物焚化處理廠**」與「日友公司成立國內**第一家**醫療廢棄物處理廠」，並載「台灣最大的專業廢棄物處理廠商之一」（「**焚化**」17次、「**1994**」2次、「第一家」2次、「生物醫療」1次），與 claim 之「成立於1994年」「台灣第一家專業生物醫療廢棄物焚化處理廠」逐項對應。
- `8341:objective_ranking_or_market_share:3f33ab11ca3de778` — `PARTIALLY_SUPPORTED`. 簡報中「**青新**」6次，支持其子公司關係；惟「為**全台最大**醫療廢棄物清運商」未獲支持（簡報之「最大」1次係指**日友本身**為「台灣最大的專業廢棄物處理廠商之一」），「**石綿瓦**清運量增加帶動營收」亦未獲支持（「石綿」0次）。
- `8341:objective_ranking_or_market_share:04de738dcd712a81` — `UNKNOWN_AFTER_RESEARCH`. 簡報中「**台大**」「**長庚**」「**榮總**」「**醫療院所**」與「**網絡**」之出現次數**均為0**（「青新」6次支持子公司關係，惟未具名任何醫療院所）。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。UNKNOWN 追蹤清單已同步刷新至 **228 筆**。
- Author-reviewed total: **934 / 1,399**; remaining: **465**. Outcome counts: ACCEPTED 92, PARTIALLY_SUPPORTED 610, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 228. Next pending claim by priority: `6951:objective_ranking_or_market_share:f85c202bfd3023a7` (青新-創).

## Author batch `author-173` — 2026-10-12

- Reviewed the next seven unreviewed objective ranking/market-share claims in checkpoint order (青新-創 6951 ×4, 可寧衛 8422, 綠電 8440 ×2). Evidence came from directly downloaded and inspected official disclosures: 青新法人說明會簡報、綠電再生法人說明會簡報。
- `6951:objective_ranking_or_market_share:f85c202bfd3023a7` — `PARTIALLY_SUPPORTED`. 青新法人說明會簡報載「本公司向**母公司日友環保**取（…）」與「**醫療廢棄物清除服務**」（「**青新**」6次、「**日友**」1次），支持其集團歸屬與業務；惟「為台灣**最大**醫療廢棄物清除服務商」未獲支持（「**最大**」0次）。
- `6951:objective_ranking_or_market_share:118a4a05e6c010b3` — `PARTIALLY_SUPPORTED`. 簡報載其為「一家專業醫療廢棄物及**事業廢棄物**清除機構」（即工業廢棄物）；惟「全台累計近 **11,000** 家客戶」（0次）、「醫療廢棄物收集**市佔率超過 30%**」（0次）與「工業廢棄物收集市佔率約 **10%**」（0次）未獲支持。
- `6951:objective_ranking_or_market_share:dfc8c55e4d895e58` — `PARTIALLY_SUPPORTED`. 簡報載「醫療廢棄物清除服務」「醫療廢棄物再利用處理」；惟「布建『**星型**運輸網絡』」（0次）、「『**廢棄物集中中繼轉運站**』模式」（0次）與「提供全台**最大規模**之醫療感染廢棄物清運服務」（0次）未獲支持。
- `6951:objective_ranking_or_market_share:477ec4a344c88ad9` — `PARTIALLY_SUPPORTED`. 簡報載「**青新木**製造銷售」「雲林**青新木**工廠」（「**青新木**」5次）；惟「為**全國最大**醫療及**有害**事業廢棄物清運轉運」（「最大」「有害」均0次）與「醫療廢**塑膠**資源化回收」之完整表述未獲支持。
- `8422:objective_ranking_or_market_share:8c9bc6fbd3f61732` — `UNKNOWN_AFTER_RESEARCH`. 本批次自公開資訊觀測站端點所取得之檔案僅 **690 bytes**，**為非文件內容**，未取得可檢視之簡報或年報。
- `8440:objective_ranking_or_market_share:80bc4d426ebfd8b7` — `PARTIALLY_SUPPORTED`. 綠電再生簡報載「1998-2000」與「**亞洲第一家廢家電資源化處理廠**」（「**廢家電**」5次、「廢家電及廢資訊物品」），支持其設立年分與首家地位——**官方所述範圍（亞洲）強於 claim 之「國內」**；惟「亦為台灣**最大**的廢家電與廢資訊物品回收處理廠」未獲支持（「**最大**」0次）。
- `8440:objective_ranking_or_market_share:583e2c8ff693e85f` — `UNKNOWN_AFTER_RESEARCH`. 簡報中「**唯一**」「**中部**」與「獨佔」之出現次數**均為0**——簡報僅載「亞洲第一家廢家電資源化處理廠」（全國／亞洲層級），未載任何**區域性獨占**之敘述。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。UNKNOWN 追蹤清單已同步刷新至 **230 筆**。
- Author-reviewed total: **941 / 1,399**; remaining: **458**. Outcome counts: ACCEPTED 92, PARTIALLY_SUPPORTED 615, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 230. Next pending claim by priority: `7507:objective_ranking_or_market_share:bfc75b334da69cf9` (環拓科技).
## Author batch `author-174` — 2026-10-12

- Reviewed the final two unreviewed objective ranking/market-share claims in checkpoint order (環拓科技 7507, 金益鼎 8390). Evidence came from official disclosure endpoints.
- `7507:objective_ranking_or_market_share:bfc75b334da69cf9` — `UNKNOWN_AFTER_RESEARCH`. 本批次自環拓科技官方網域下載年報時回應 **HTTP 404**，未取得可檢視之檔案。
- `8390:objective_ranking_or_market_share:f55fed9eabcb8974` — `UNKNOWN_AFTER_RESEARCH`. 本批次自公開資訊觀測站端點所取得之檔案僅 **690 bytes**，**為非文件內容**，未取得可檢視之簡報或年報。
- **重大里程碑：objective_ranking_or_market_share 訊號類型之隊列已全數審畢**（本審核之第一階段）。後續待審 456 筆改依其他訊號類型推進，其分布為：`material_named_relationship` **315**、`identity_changing_event` **42**、`export_concentration` **27**、`profitability_assertion` **67**、`control_acquisition` **5**。下一筆待審為 `2645:material_named_relationship:8a2772f0488a5e3a`（長榮航太）。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。UNKNOWN 追蹤清單已同步刷新至 **232 筆**。
- Author-reviewed total: **943 / 1,399**; remaining: **456**. Outcome counts: ACCEPTED 92, PARTIALLY_SUPPORTED 615, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 232.
## Author batch `author-175` — 2026-10-12

- Began the second phase, `material_named_relationship`, reviewing its first two claims in checkpoint order (長榮航太 2645 ×2). Evidence came from directly downloaded and inspected official disclosures: 長榮航太上市前業績發表會簡報、長榮航太法人說明會簡報。
- `2645:material_named_relationship:8a2772f0488a5e3a` — `PARTIALLY_SUPPORTED`. 長榮航太上市前業績發表會簡報載其業務為「2.**機體**、發動機零組件之**製造**及加工」與「商用飛機**機體**維修及改裝服務」，並載「—獲得**BOEING**客機改貨機品質**認證**、擴大技術競爭力」（「**Boeing**」6次、「**機體**」15次、「**認證**」17次），支持其機體零組件製造業務及與 Boeing 之認證關係；惟「為 [[Airbus]] 之 Tier 1 供應商」（「**Airbus**」「**空中巴士**」「**Tier**」均0次）與「2025年正式升格為 Airbus **一階**機體零組件**直供商**」（「一階」「**直供**」均0次；且該簡報為2023年版本）未獲支持。
- `2645:material_named_relationship:25d41503b8a9ab48` — `UNKNOWN_AFTER_RESEARCH`. 兩份簡報（2024年法人說明會、2023年上市前業績發表會）中「**Airbus**」「空中巴士」與「原廠件」之出現次數**均為0**，未載與 Airbus 之供應或認證關係。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。UNKNOWN 追蹤清單已同步刷新至 **233 筆**。
- Author-reviewed total: **945 / 1,399**; remaining: **454**. Outcome counts: ACCEPTED 92, PARTIALLY_SUPPORTED 616, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 233.
## Author batch `author-176` — 2026-10-12

- Reviewed the next six material-named-relationship claims in checkpoint order (晟田 4541 ×3, 駐龍 4572 ×2, 寶一 8222). Evidence came from directly downloaded and inspected official disclosures: 晟田法人說明會簡報、駐龍法人說明會簡報、寶一113年度年報。
- `4541:material_named_relationship:2ab6d5fc7471158f` — `PARTIALLY_SUPPORTED`. 晟田簡報中「**漢翔**」11次、「**Safran**」2次、「**SPP**」4次、「**MOOG**」4次、「**起落架**」7次、「**GE**」57次、「Boeing」11次、「Airbus」9次，支持其航太零組件業務及該等具名廠商之供應關係；惟「（佔營收約 **75%**）」（0次）、「[[三菱重工]]」（**0次**）與「終端客戶涵蓋…機體結構件」之完整表述未獲支持。**註記**：該簡報文字層多為**孤立詞組**。
- `4541:material_named_relationship:df473dfcdc3e30d8` — `PARTIALLY_SUPPORTED`. 「**食品**」3次、「**10%**」1次，支持其食品包裝設備業務；惟「供應[[三菱重工]]等食品飲料充填設備零組件」未獲支持（「**三菱重工**」0次）。
- `4541:material_named_relationship:bcf536822f52729b` — `PARTIALLY_SUPPORTED`. 「**漢翔**」11次、「41%」1次、「Boeing」11次、「Airbus」9次**均有出現**；惟「41%」與「漢翔」之**連結無法由文字層確認**（該簡報之文字層多為孤立詞組，未能擷取完整句子），「間接供應引擎與機體零組件」之完整表述亦未見。
- `4572:material_named_relationship:b06442b0f8987e25` — `PARTIALLY_SUPPORTED`. 駐龍簡報中「**Boeing**」6次、「**認證**」5次，支持其為 Boeing 合格供應商並持有認證；惟「為 Boeing 在台灣**僅三家**合格供應商之一」（「**三家**」0次）與「持有 Boeing **全製程**認證」（「**全製程**」0次）未獲支持。
- `4572:material_named_relationship:425087302d080000` — `PARTIALLY_SUPPORTED`. 簡報中「**737**」3次、「**777**」3次、「**787**」2次、「**Spirit**」6次、「勢必銳」1次、「**Safran**」4次，並見「**Boeing** program, A320, Bombardier-Challenger 350」，**逐項對應**；惟「及**漢翔**等 Tier 1 廠商」未獲支持（「**漢翔**」與「**Tier**」均0次）。
- `8222:material_named_relationship:710cbe41e0f8945e` — `PARTIALLY_SUPPORTED`. 寶一113年度年報中「**Safran**」27次、「**Pratt**」10次、「**Tier**」11次、「**MTU**」2次，支持其供應商地位；惟「[[川崎重工]]」（0次）、「[[GE Avio]]」（0次）與「波蘭」（0次；「比利時」2次）未獲支持。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）；UNKNOWN 追蹤清單維持 **233 筆**。
- Author-reviewed total: **951 / 1,399**; remaining: **448**. Outcome counts: ACCEPTED 92, PARTIALLY_SUPPORTED 622, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 233.
## Author batch `author-177` — 2026-10-12

- Reviewed the next two export-concentration claims in checkpoint order (惠光 6508 ×2). Evidence came from official disclosure endpoints.
- `6508:export_concentration:d679e0352a3e6a29` 與 `6508:export_concentration:9321018679533bfd` — `UNKNOWN_AFTER_RESEARCH`. 本批次自發行人官方網域（huikwang.com）下載113年股東會年報，**回應 HTTP 403（禁止）**；另嘗試同網域之2024年永續報告書端點，**亦回應 HTTP 403**；**經加入 User-Agent 與 Referer 標頭重試，兩者仍為 403**。故「內銷台灣約佔三成，中國大陸約佔四成，東南亞及澳洲為主要外銷市場，近期新增美國市場帶動成長」與「中國（佔外銷約 20%）、澳洲（約 20%）、越南（約 10%）— 掩埋場、水利及基礎建設工程」均未獲確立。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。UNKNOWN 追蹤清單已同步刷新至 **235 筆**。
- Author-reviewed total: **953 / 1,399**; remaining: **446**. Outcome counts: ACCEPTED 92, PARTIALLY_SUPPORTED 622, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 235.
## Author batch `author-178` — 2026-10-12

- Reviewed the next five material-named-relationship and export-concentration claims in checkpoint order (華航 2610, 星宇航空 2646 ×3, 森鉅 8942). Evidence came from directly downloaded and inspected official disclosures: 星宇航空公司概況資料表、森鉅101年度年報。
- `2610:material_named_relationship:2e40073714d0a5be` — `UNKNOWN_AFTER_RESEARCH`. 本批次自華航官方網域下載年報時回應 **HTTP 403**，未取得可檢視之檔案。
- `2646:material_named_relationship:bb36b2baf871ecc0` 與 `2646:export_concentration:3f957a41898c043c` — `UNKNOWN_AFTER_RESEARCH`. 星宇公司概況資料表中「**AI 伺服器**」「**北美**」與「**72%**」之出現次數**均為0**，且該文件為 **2022 年**版本，**早於**其貨運業務之開展。
- `2646:material_named_relationship:2da1bdd0a02eaff8` — `PARTIALLY_SUPPORTED`. 文件載「首架**A321neo**客機交機」與「引進**A321neo**窄體客機、**A330-900neo**中長程廣體客機及**A350-900**長程廣體客機三種新世代機種」（「**A321neo**」3次、「**A350**」2次）；惟「[[Airbus]]」（**0次**；文件僅載機型代號）、「（**A330neo**）」（文件作「**A330-900neo**」，型號命名差異）、「A350-1000」（0次）、「A350F」（0次）與「全機隊**獨家**供應」（「獨家」0次）未獲支持。
- `8942:material_named_relationship:3ed45ecdbb814b9b` — `UNKNOWN_AFTER_RESEARCH`. 森鉅年報（**101 年度＝2012年，非近期版本**）中「**北美**」「**拖車**」「**trailer**」與「[[Wabash]]」「[[Great Dane]]」「[[Utility Trailer]]」「[[Vanguard National Trailer]]」「[[Stoughton Trailers]]」之出現次數**均為0**。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。UNKNOWN 追蹤清單已同步刷新至 **239 筆**。
- Author-reviewed total: **958 / 1,399**; remaining: **441**. Outcome counts: ACCEPTED 92, PARTIALLY_SUPPORTED 623, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 239.
## Author batch `author-179` — 2026-10-12

- Reviewed the next two material-named-relationship claims in checkpoint order (寶緯 4558, 立敦 6175). Evidence came from directly downloaded and inspected official disclosures: 寶緯法人說明會簡報、立敦2025英文年報。
- `4558:material_named_relationship:bd9a41e2bb96675f` — `PARTIALLY_SUPPORTED`. 寶緯法人說明會簡報載「主要產品:**鋁擠型**…」「**進入半導體產業供應鏈**」與「**-半導體軌道**」（「**半導體**」4次、「**軌道**」2次、「**鋁擠**」3次），支持其鋁擠型業務及進入半導體供應鏈之敘述；惟「晶圓廠**無塵室**」（0次）、「**天車**軌道」（0次）與「終端客戶包含[[台積電]]」（**0次**）未獲支持。
- `6175:material_named_relationship:08af81112ac77be6` — `PARTIALLY_SUPPORTED`. 立敦2025年報（**英文版**）中「**foil**」153次、「**etch**」37次，並載「**electrode foil** industry」「expanded low-voltage **foil** production capacity」，**充分支持其電蝕鋁箔業務**；惟「透過與[[東陽光]]合資之[[立東電子]]」（「**Sunshine**」「**Dongyang**」「**joint venture**」均0次）與「自給率已達 **70%**」（「**self-supply**」0次）未獲支持。**方法論註記：本件為英文版文件，中文關鍵字檢索不具意義。**
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）；UNKNOWN 追蹤清單維持 **239 筆**。
- Author-reviewed total: **960 / 1,399**; remaining: **439**. Outcome counts: ACCEPTED 92, PARTIALLY_SUPPORTED 625, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 239.
## Author batch `author-180` — 2026-10-12

- Reviewed the next five claims in checkpoint order (達新 1315, 宏太-KY 2924, 如興 4414 ×3). Evidence came from directly downloaded and inspected official disclosures: 達新法人說明會簡報、宏太法人說明會簡報、如興民國113年法人說明會簡報。
- `1315:material_named_relationship:c0ee757c6cd7ab74` — `PARTIALLY_SUPPORTED`. 達新簡報載「PET、**PVC**及壓克力板等資材輸入販售」，支持其 PVC 資材販售；**惟「南亞」1次之上下文為投資而非供應商關係**——「本公司截至目前取得**南亞股票**累積持有股數32,140張，金額為10億9,437萬元」；「**台塑**」「**塑膠粒**」與「供應商」之出現次數均為0。
- `2924:identity_changing_event:bdc91f7aaff60bfd` — `PARTIALLY_SUPPORTED`. 宏太簡報中「**東凌**」6次、「**1988**」2次、「**Cayman**」2次，支持其原名、成立年分與註冊地；惟「（2924，Cayman **宏太**）…**2023 年更名為宏太-KY**」未獲支持（「宏太」「2023」「更名」均0次）。**時點註記**：該簡報為 **2020 年**版本，早於所述之2023年更名事件。
- `4414:material_named_relationship:1784fcab0b4355b8` — `PARTIALLY_SUPPORTED`. 如興簡報載「全球**牛仔**成衣領導廠商」與**前五大客戶營收占比**表——2024年1-11月「**LEVI'S** 26%」「**GAP** 19%」，2023年1-11月「**LEVI'S** 27%」「**GAP** 14%」；惟「[[Calvin Klein]] Jeans」未獲支持（「**Calvin**」與「**Klein**」均0次；前五大為 WalMart、LEVI'S、GAP、GU、TCP）。
- `4414:material_named_relationship:d5be7e550754288b` — `ACCEPTED`. 簡報之「**前五大客戶營收占比**」表明列「**LEVI'S**」27%（2023年1-11月）與26%（2024年1-11月），**逐字支持其為主要客戶**。
- `4414:material_named_relationship:4b8e7b132cec3345` — `ACCEPTED`. 簡報之「**前五大客戶營收占比**」表明列「**GAP**」14%（2023年1-11月）與19%（2024年1-11月），**逐字支持其為主要客戶**。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）；UNKNOWN 追蹤清單維持 **239 筆**。
- Author-reviewed total: **965 / 1,399**; remaining: **434**. Outcome counts: ACCEPTED 94, PARTIALLY_SUPPORTED 628, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 239.
## Author batch `author-181` — 2026-10-12

- Reviewed the next four material-named-relationship claims in checkpoint order (廣越 4438 ×4). Evidence came from directly downloaded and inspected official disclosures: 廣越投資人簡報（2025-11-11）、廣越投資人簡報（2025-04-15）。
- `4438:material_named_relationship:71def6e48a4142d5` — `PARTIALLY_SUPPORTED`. 兩份簡報中「**adidas**」7次、「**Nike**」6次、「**Patagonia**」4次、「**lululemon**」3次、「**VF**」2次、「**The North Face**」1次，**五個品牌與其母公司均有對應敘述**（含「獲**The North Face** 全球（…）」）；惟各品牌之訂單成長率（年增60%／10%／60%／5%）**與品牌之連結無法由文字層確認**（文字層多為孤立詞組）。
- `4438:material_named_relationship:103d9b9caad76508` — `PARTIALLY_SUPPORTED`. 兩份簡報均載「2. 透過第**㇐**大供應商**福懋**(**全球最大的尼龍布供應商**)穩定供貨」，**逐字支持福懋為其主要布料供應商**；惟「策略性股東…持股約 **20%**」未獲支持——「**持股**」「**股東**」與「策略性」均0次，且「**20%**」各次上下文**均非福懋持股**（約旦出貨比重、約旦關稅、ROE 目標）。**字形註記**：「第**㇐**大」之「**㇐**」為 CJK 筆畫字元。
- `4438:material_named_relationship:d4f5adfeb43875d9` 與 `10d632776ea4921a` — `PARTIALLY_SUPPORTED`. 供應商關係獲逐字支持；惟「（同時為 **20% 策略股東**）」與「台灣／越南／中國設廠配合」未獲支持。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）；UNKNOWN 追蹤清單維持 **239 筆**。
- Author-reviewed total: **969 / 1,399**; remaining: **430**. Outcome counts: ACCEPTED 94, PARTIALLY_SUPPORTED 632, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 239.
## Author batch `author-182` — 2026-10-12

- Reviewed the next four claims in checkpoint order (鴻華先進-創 2258 ×2, 台翰 1336, 正道 1506). Evidence came from directly downloaded and inspected official disclosures: 台翰113年度年報、正道107年度年報。
- `2258:control_acquisition:a2cce4203b591026` 與 `2258:material_named_relationship:918bd151a76df137` — `UNKNOWN_AFTER_RESEARCH`. 本批次自公開資訊觀測站端點下載鴻華先進簡報時回應 **HTTP 404**，未取得可檢視之檔案；「已收購[[納智捷]] 100% 股權…」與「[[MIH]]聯盟成員 — 台灣供應商佔比逾 50%」因而未獲確立。
- `1336:material_named_relationship:060ea61467d8c536` — `PARTIALLY_SUPPORTED`. 台翰113年度年報中「**事務機**」9次、「**日系**」7次、「**Brother**」1次，支持其日系事務機客戶之敘述並具名 Brother；惟「**Canon**」「**Kyocera**」與「**Epson**」之出現次數**均為0**。
- `1506:material_named_relationship:bfd3eddf17697b9b` — `PARTIALLY_SUPPORTED`. 正道107年度年報（**2018年，非近期版本**）中「**壓縮機**」5次、「**冷凍**」2次、「**Thermo**」4次、「**BRP**」2次，支持其冷凍壓縮機業務並具名 Thermo 與 BRP；惟「**Trane**」「**Polaris**」與「**Yamaha**」之出現次數**均為0**。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。UNKNOWN 追蹤清單已同步刷新至 **241 筆**。
- Author-reviewed total: **973 / 1,399**; remaining: **426**. Outcome counts: ACCEPTED 94, PARTIALLY_SUPPORTED 634, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 241.
## Author batch `author-183` — 2026-10-12

- Reviewed the next five material-named-relationship claims in checkpoint order (大億 1521, 江申 1525, 和大 1536 ×3). Evidence came from directly downloaded and inspected official disclosures: 大億2024年度年報、江申115年股東會年報、和大法人說明會簡報。
- `1521:material_named_relationship:3643e47a5051e4fd` — `PARTIALLY_SUPPORTED`. 大億年報中「**軌道**」13次、「**航太**」5次、「捷運」2次、「機外」1次；**惟多數「軌道」之出現屬登記營業項目**（「(5)CD01020 **軌道**車輛及其零件製造業」「(6)F114080 **軌道**車輛及其零件批發業」）**或研發方向**（「(9)大眾運輸 (巴士/**軌道**/航空) 空氣消毒燈研發：」），非已交付實績；「**漢翔**」（0次）、「**Alstom**」（0次）與「**環狀線**」（0次）未獲支持。
- `1525:material_named_relationship:1413ebbb5d206bf5` — `PARTIALLY_SUPPORTED`. 江申115年股東會年報中「**豐田**」5次、「**日產**」2次、「**金龍**」8次（另「合資」6次），**支持其與 Toyota、Nissan 及廈門金龍之合作敘述——惟須以中文廠名檢索，以英文名檢索將得0次**；惟「供應[[寧德時代]]（電池盒）」（「寧德」「電池盒」均0次）、「[[小米汽車]]」（0次）、「[[蔚來汽車]]」（0次）、「[[Honda]]」（「本田」0次）、「[[Mazda]]」（「馬自達」0次）與「[[Volvo]]」（「富豪」0次）未獲支持。
- `1536:material_named_relationship:155354e2481c1bb3` — `PARTIALLY_SUPPORTED`. 和大簡報中「**減速**」3次、「**齒輪**」4次、「**電動車**」2次，並載其為「歐美日車廠之一階供應商」；**惟「第二大客戶 [[Tesla]]」（「Tesla」「特斯拉」均0次）**、「佔營收約20%」、「**獨家**供應」與「Model S/X、Semi、Model 3/Y」（「Model」「Semi」均0次）未獲支持。**字形註記**：簡報中「機器人」被**換行拆為「機器」與「人」**。
- `1536:material_named_relationship:1b0a30cf02a7f3d9` — `PARTIALLY_SUPPORTED`. 簡報中「**行星**」1次、「減速」3次，產品應用載明含「機（換行）器（換行）人」；惟「獲 [[Tesla]] 邀請」（0次）、「[[Optimus]] 人形機器人」（「Optimus」「人形」均0次）、「台灣獨家供應商」與「每台約40組」未獲支持。
- `1536:material_named_relationship:896f01fa3513114d` — `UNKNOWN_AFTER_RESEARCH`. 所取得之簡報中「**Tesla**」與「**特斯拉**」之出現次數**均為0**，**未具名該客戶**，亦未載20%營收占比與獨家供應之敘述。
- No issuer report was modified. Independent review remains pending.
- 本批次未新增來源取得失敗；`local-recheck-queue.json` 維持 **15** 筆（HTTP 500 × 8、HTTP 503 × 7）。UNKNOWN 追蹤清單已同步刷新至 **242 筆**。
- Author-reviewed total: **978 / 1,399**; remaining: **421**. Outcome counts: ACCEPTED 94, PARTIALLY_SUPPORTED 638, UNSUPPORTED 1, SOURCE_UNAVAILABLE 3, PERIOD_UNRESOLVED 0, UNKNOWN_AFTER_RESEARCH 242.











































































































































































