# 首批獨立複核：reviewer-001

檢視時間：2026-10-06T00:15:29.507279Z。作者基線：`a0685469882bd423587577ad9aa093a6db75e757`；分支 `audit-v5`。

完成12筆唯一claim的獨立內容複核，引用21份來源。Reviewer判定：部分支持9、接受1、不支持1、期間未解1。與作者現行decision同意2筆、分歧10筆；最終完整接受0筆。剩餘未複核1,387筆，另10筆須裁決。

這是來源與內容複核，不是盲審。已讀作者判定，再自行核對文件／頁面、公司身分、子句與期間；新證據包含IFC投資披露、協禧真實年報、華夏2025年報與2026年第二季財報。HTTP成功不直接改變語意判定，作者歷史failure與原始檔案保持原樣。

| 公司／疑點 | 作者 | 複核 | 處理 |
|---|---|---|---|
| 2208 台船／船舶排名 | `UNSUPPORTED` | `PARTIALLY_SUPPORTED` | 待分歧裁決 |
| 1712 興農／排名市占出口 | `SOURCE_UNAVAILABLE` | `PARTIALLY_SUPPORTED` | 待分歧裁決 |
| 1722 台肥段落／OCP排名 | `SOURCE_UNAVAILABLE` | `ACCEPTED` | 待分歧裁決 |
| 2610 華航段落／中油唯一 | `SOURCE_UNAVAILABLE` | `UNSUPPORTED` | 待分歧裁決 |
| 6225 天瀚／外銷地區 | `UNSUPPORTED` | `PERIOD_UNRESOLVED` | 待分歧裁決 |
| 3071 協禧／錯公司來源 | `UNKNOWN_AFTER_RESEARCH` | `PARTIALLY_SUPPORTED` | 待分歧裁決 |
| 3338 泰碩／核心供應商 | `ACCEPTED` | `PARTIALLY_SUPPORTED` | 待分歧裁決 |
| 3338 泰碩／CDU量產規格 | `PARTIALLY_SUPPORTED` | `PARTIALLY_SUPPORTED` | 同意部分支持 |
| 3338 泰碩／RVL與供貨關係 | `PARTIALLY_SUPPORTED` | `PARTIALLY_SUPPORTED` | 同意部分支持 |
| 3481 群創／併購與三家客戶 | `ACCEPTED` | `PARTIALLY_SUPPORTED` | 待分歧裁決 |
| 5009 榮剛／三類高毛利 | `UNKNOWN_AFTER_RESEARCH` | `PARTIALLY_SUPPORTED` | 待分歧裁決 |
| 1305 華夏／87%股權與供應 | `ACCEPTED` | `PARTIALLY_SUPPORTED` | 待分歧裁決 |

## 對後續公司／產業研究論文的影響

本批沒有完整原句取得最終ACCEPTED。OCP雖被本reviewer接受，仍與作者SOURCE_UNAVAILABLE分歧，不能跳過裁決。部分支持的同意也只定下分類，未核准作者或reviewer改寫；正文重寫尚未進行。

論文候選句必須保留公司、指標口徑、適用期間與來源。特別是：(1)排名按官方不同描述保留衝突，不能只挑有利版本；(2)平台相容不寫成直接客戶；(3)送驗或開發不寫成量產；(4)股權／產能不寫成穩定供應保證；(5)2023/2024銷售資料不當成2026出口目的地。

## 逐筆紀錄

### 2208 台船／船舶排名

鍵：`2208:objective_ranking_or_market_share:ac3375b6f79fe6f3`；hash：`ac3375b6f79fe6f3e3260058c79b0edf86091db63943c45d531cdf544b8534fe`。

原claim：(3) [[離岸風電]]海事工程 — 與比利時[[DEME]]集團合資成立台船環海 (CDWE)，擁有亞洲最大浮吊船「環海翡翠輪」，承攬彰芳暨西島及海龍離岸風場安裝工程；

合資成立、船舶及承攬安排有正式公司資料支持。作者所據2024新聞稿說亞洲第二大，但另行讀取2025台灣精品產品介紹說亞洲第一大。來源未交代相同排名口徑與變動原因，且「浮吊船」範圍大於「風電工程船」。不能接受原句的最大限定，也不能把作者的否定直接定案；保留排名衝突。

缺口類型：ranking_definition, conflicting_official_descriptions, period。

改寫提案：台船與DEME集團旗下GeoSea合資成立台船環海；官方2019年資料載彰芳、西島與海龍工程承攬安排，2024年資料載環海翡翠輪參與離岸風場基礎安裝。

檢視來源：

- [台船環海：中能風場31座水下基礎安裝完成](https://www.cdwe.com.tw/news_detail.php?id=93)；HTML 新聞日期及首段／工程進度段；2024-03-05；不得直接延伸為2026年排名。檢視摘要：[本機紀錄](semantic/reviewer-evidence/reviewer-001/cdwe93.md)。
- [台船環海：環海翡翠輪交船典禮](https://www.cdwe.com.tw/news_detail.php?id=83)；HTML 交船及船舶描述段；2023年交船新聞；全球排名與亞洲排名不可直接互換。檢視摘要：[本機紀錄](semantic/reviewer-evidence/reviewer-001/cdwe83.md)。
- [台船環海公司開幕](https://www.cdwe.com.tw/news_detail1.php)；HTML 開幕、彰芳西島及海龍契約段；2019年合資成立及當時承攬安排。檢視摘要：[本機紀錄](semantic/reviewer-evidence/reviewer-001/cdwe2019.md)。
- [台灣精品：台船海工全迴旋大型浮吊船 Hno.1175](https://www.taiwanexcellence.org/tw/award/product/1140055)；HTML 產品介紹；產品型號及廠商欄；2025台灣精品產品條目；網頁無可核實刊登日期。檢視摘要：[本機紀錄](semantic/reviewer-evidence/reviewer-001/greenjade_award2025.md)。

### 1712 興農／排名市占出口

鍵：`1712:objective_ranking_or_market_share:ababe1bd116826cb`；hash：`ababe1bd116826cbfd47d4882a25bff4d8747b130304aeb0417a1b4216255fb9`。

原claim：興農股份有限公司 (1712，Sinon Corporation) 為台灣最大農藥製造商，國內農藥零售市佔約 18%，產品外銷逾 60 國。

獨立讀取興農官方正文支持农藥生產行銷業務，但最大、零售市占18%、外銷逾60國三個限定均未確立。先前503與空殼不能支持SOURCE_UNAVAILABLE。官網恢復不是本判定依據，內容才是。逾60國另有搜尋線索但未取得有效可讀正文，未納作證據。

缺口類型：objective_ranking, market_share_denominator, export_country_count, undated_source。

改寫提案：興農官方企業介紹與植物保護事業頁說明其從事農藥等植保產品的生產與行銷；本次未確立市場排名、市占或出口國數。

檢視來源：

- [興農：企業理念](https://www.sinon.com.tw/about/)；HTML About Sinon 主文；未標日期之官網；2026-10-06檢視，歷史起點明示1955年。檢視摘要：[本機紀錄](semantic/reviewer-evidence/reviewer-001/sinon_about.md)。
- [興農：植物保護事業](https://www.sinon.com.tw/careers-detail/28/)；HTML 植物保護事業正文；未標日期之官方事業介紹；2026-10-06檢視。檢視摘要：[本機紀錄](semantic/reviewer-evidence/reviewer-001/sinon_plant.md)。

### 1722 台肥段落／OCP排名

鍵：`1722:objective_ranking_or_market_share:7cd11cc6ee9fc2c7`；hash：`7cd11cc6ee9fc2c78658a18bd2f1d2163474c88523cacb8b26ea0a82cb5d801b`。

原claim：[[OCP Group]] (摩洛哥，全球最大磷礦出口商)

IFC 2026項目披露在公司／股東段明示OCP為全球最大磷礦石出口商，國別為摩洛哥；對象、礦種、排名及出口角色吻合。只接受此正式披露所支持的2026描述，不以國家礦產排名替代公司排名，也不驗證台肥與OCP的交易關係。作者SOURCE_UNAVAILABLE與本判定不同，須升级裁決，不能直接最終接受。

缺口類型：本句在指定披露期間內無缺口。

改寫提案：IFC於2026年披露的OCP項目資料稱，摩洛哥OCP是全球最大磷礦石出口商。

檢視來源：

- [IFC：OCP Phosphogypsum，project 51794](https://disclosures.ifc.org/project-detail/SII/51794/ocp-phosphogypsum)；HTML Company / Shareholders、Country、Date SPI Disclosed、Last Updated Date；2026年項目披露；最後更新2026-05-29。檢視摘要：[本機紀錄](semantic/reviewer-evidence/reviewer-001/ifc51794.md)。

### 2610 華航段落／中油唯一

鍵：`2610:objective_ranking_or_market_share:e790282c63b01303`；hash：`e790282c63b0130355e0ae4b13e6e92daee4094dba97ee82f28743d3a3c05df5`。

原claim：[[台灣中油]] — 國內機場唯一航油供應商

台塑石化113年報具體載其在桃園、松山、臺中、高雄均有供油服務，直接反駁無期間限定的「國內機場唯一」市場敘述；中油2025業務簡介另列2024航油市占59.4%。不是從503推論內容錯誤，也不是把市占單獨當機場供應商名冊。直接反證限2024及2025刊印時；尚未取得2026全部機場名冊，因此改寫明示歷史期間。

缺口類型：exclusivity_contradicted, period。

改寫提案：依2024年度官方資料，台灣中油與台塑石化均從事國內航空燃油供應；台塑石化年報列其在桃園、松山、臺中、高雄機場提供供油服務。

檢視來源：

- [台塑石化股份有限公司113年度年報](https://www.fpcc.com.tw/uploads/images/ir/%E5%8F%B0%E5%A1%91%E7%9F%B3%E5%8C%96113%E5%B9%B4%E8%82%A1%E6%9D%B1%E6%9C%83%E5%B9%B4%E5%A0%B1.pdf)；PDF第116頁／印刷頁111，C.航空燃油；2024年度及2025-04-30刊印時；2026完整名冊未取得。檢視摘要：[本機紀錄](semantic/reviewer-evidence/reviewer-001/fpcc_ar113.md)。
- [台灣中油：2025業務簡介，油品行銷](https://ws.cpc.com.tw/cpcannual/2025/files/basic-html/page24.html)；HTML page24；印刷頁22；2025出版內容；銷售市占資料為2024年。檢視摘要：[本機紀錄](semantic/reviewer-evidence/reviewer-001/cpc2025.md)。

### 6225 天瀚／外銷地區

鍵：`6225:export_concentration:e4146e23ad193cf5`；hash：`e4146e23ad193cf514ab606be7bf62b4934d3bfa8a2f086a5dbc279b36f7d03d`。

原claim：產品以歐美為主要外銷市場。

2023年無外銷，2024年主要商品銷售表亦全在台灣，足以阻止將舊外銷描述當成該期事實。但「國內為主要市場」與「出口主要目的地」是不同分母，7.2%風險文字又未與2023零外銷一致。報告估值日期為2026而句子未標期間；未取得2025/2026目的地資料，不足以斷言現行或歷史所有期間均被否定，故改為期間未解。

缺口類型：period, export_denominator, internal_source_inconsistency。

改寫提案：依天瀚2024年度年報，2023及2024年度主要商品銷售地區表列台灣占100%；此為歷史銷售資料，未用來判定2026年出口目的地。

檢視來源：

- [天瀚科技股份有限公司112年度年報](https://www.aiptek.com.tw/uploads/information_shareholders/tw/112%e5%b9%b4%e5%a0%b1.pdf)；PDF第45、51、133頁／印刷頁40、46、127；2023年度；歷史快取下载時間未經核實。檢視摘要：[本機紀錄](semantic/reviewer-evidence/reviewer-001/aiptek_ar112.md)。
- [天瀚科技股份有限公司113年度年報](https://www.aiptek.com.tw/uploads/information_year/tw/113%E5%B9%B4%E5%A0%B1.pdf)；PDF第35、38、44頁／印刷頁31、34、40；2024年度；銷售表並列2023年度，非2026年度。檢視摘要：[本機紀錄](semantic/reviewer-evidence/reviewer-001/aiptek_ar113.md)。

### 3071 協禧／錯公司來源

鍵：`3071:material_named_relationship:2d5f28d692feacbe`；hash：`2d5f28d692feacbeb8a49e289369339b46b9c36ef470dd3ace00d9d75513b1a2`。

原claim：近年轉型聚焦：(1) 車用電子 — 獲歐美 Tier 1 認證，應用於車燈/座椅通風/電池散熱，間接供應[[Tesla]]、[[GM]]、[[Ford]]；

視覺核對確認emctw年報為2383，排除為3071證據，認同author-217來源歸屬更正。另從協禧官方股東會頁連結下載、核對封面3071並讀取2023年報及汽車電子正文，支持車用散熱領域。歐美Tier 1認證、車燈／座椅／電池三項用途及Tesla／GM／Ford間接供應鏈未逐項確立。對台光電文件做OCR不是本claim的正確下一步。

缺口類型：source_identity_mismatch_resolved, certification, named_end_customer, specific_application, period。

改寫提案：協禧2023年度年報及官方汽車電子應用頁介紹其車用散熱產品與研發；本次未確立歐美Tier 1認證或特定車廠間接供應關係。

檢視來源：

- [台光電子材料股份有限公司112年度年報](https://www.emctw.com/upload/media/New_Investors/Financial_Information/Annual_Reports/CH/2023.pdf)；PDF封面；2023年度；封面刊印2024-05-08；歷史快取下载時間未經核實。檢視摘要：[本機紀錄](semantic/reviewer-evidence/reviewer-001/emc_ar112.md)。
- [協禧電機股份有限公司112年年報](https://adda.show.ad-design.tw/upload/investors_page_file/3.pdf)；PDF封面、第5、6頁／印刷頁3、4；2023年度；2024年刊印。檢視摘要：[本機紀錄](semantic/reviewer-evidence/reviewer-001/adda_ar112.md)。
- [協禧：汽車電子應用散熱風扇](https://www.adda.com.tw/application/Automotive-Electronics/)；HTML 汽車電子主文；未標日期之官方產品应用頁；2026-10-06檢視。檢視摘要：[本機紀錄](semantic/reviewer-evidence/reviewer-001/adda_auto.md)。

歷史事件：

- author-217 corrections：來源由3071更正為2383；更正正確，但原rationale的協禧OCR建議未同步修正

### 3338 泰碩／核心供應商

鍵：`3338:material_named_relationship:f05e7d30c8a03bef`；hash：`f05e7d30c8a03bef0a63f4c190f2e1e68587d651c7aca4c8a58f6e4d4a40b3f0`。

原claim：泰碩電子 (3338，[[TaiSol]]) 為專業散熱模組與連接器製造商，近年成功轉型為 [[AI 伺服器]]液冷散熱核心供應商。

113年報支持散熱模組與AI/HPC液冷研發，但未證明已成功轉型為核心供應商；114年展望中的轉型與技術商業化屬計畫，不能當完成事件。連接器詞在董監事兼職公司的名稱中亦不足證明當期產品線。官方網站轉載2025新聞提供進度線索，證據位階與年報區分。

缺口類型：core_supplier_qualifier, planned_vs_completed, product_scope, period。

改寫提案：泰碩2024年度年報介紹散熱模組業務，以及AI/HPC伺服器液冷技術研發與2025年商業化規劃。

檢視來源：

- [泰碩電子股份有限公司113年度年報](https://www.taisol.com/wp-content/uploads/2025/06/113%E5%B9%B4%E8%82%A1%E6%9D%B1%E6%9C%83%E5%B9%B4%E5%A0%B1.pdf)；PDF第6、58、62頁／印刷頁2、54、58；2024年度；包含2025未來展望／計畫。檢視摘要：[本機紀錄](semantic/reviewer-evidence/reviewer-001/taisol_ar113.md)。
- [泰碩官網轉載：120KW CDU將送客戶驗證](https://www.taisol.com/news/%E7%9E%84%E6%BA%96%E4%BC%BA%E6%9C%8D%E5%99%A8%E9%AB%98%E5%83%B9%E6%B7%B1%E6%B0%B4%E5%8D%80%EF%BC%8C%E6%B3%B0%E7%A2%A9120kw-cdu%E6%90%B6%E5%B8%82/?lang=en_US)；HTML Release Date及MoneyDJ轉載正文；2025-08-18狀態及下一年度目標；不等同2026實績。檢視摘要：[本機紀錄](semantic/reviewer-evidence/reviewer-001/taisol120news.md)。

歷史事件：

- author-223 amendment／author-224：UNKNOWN改ACCEPTED；新文件有效，但完整句子未被蘊涵

### 3338 泰碩／CDU量產規格

鍵：`3338:profitability_assertion:d8fd097329e5101b`；hash：`d8fd097329e5101bf83fe774b55e2dbba35584dac2daaee6aac272e37547857c`。

原claim：核心業務與成長引擎：(1) AI 液冷散熱 — 開發 CDM (冷卻分配歧管)、LCM (液冷模組) 及 CDU (冷卻液分配單元) 等核心技術，120KW CDU 已量產出貨，150KW 產品開發中。

同意CDU與Manifold液冷研發受支持，但缺口不限CDM/LCM名稱：120kW量產出貨、150kW當期開發狀態及成長引擎地位也需證明。2025-08-18轉載文字為120kW送驗及下一年供應鏈目標，不是量產實績，不能將該時間點延伸為2026尚未出貨。

缺口類型：model_specification, mass_production_vs_testing, growth_engine, period。

改寫提案：泰碩2024年度年報列CDU與Manifold相關液冷技術研發；2025年8月官網轉載另述120kW CDU送驗進度，未作量產出貨判斷。

檢視來源：

- [泰碩電子股份有限公司113年度年報](https://www.taisol.com/wp-content/uploads/2025/06/113%E5%B9%B4%E8%82%A1%E6%9D%B1%E6%9C%83%E5%B9%B4%E5%A0%B1.pdf)；PDF第6、58、62頁／印刷頁2、54、58；2024年度；包含2025未來展望／計畫。檢視摘要：[本機紀錄](semantic/reviewer-evidence/reviewer-001/taisol_ar113.md)。
- [泰碩官網轉載：120KW CDU將送客戶驗證](https://www.taisol.com/news/%E7%9E%84%E6%BA%96%E4%BC%BA%E6%9C%8D%E5%99%A8%E9%AB%98%E5%83%B9%E6%B7%B1%E6%B0%B4%E5%8D%80%EF%BC%8C%E6%B3%B0%E7%A2%A9120kw-cdu%E6%90%B6%E5%B8%82/?lang=en_US)；HTML Release Date及MoneyDJ轉載正文；2025-08-18狀態及下一年度目標；不等同2026實績。檢視摘要：[本機紀錄](semantic/reviewer-evidence/reviewer-001/taisol120news.md)。

歷史事件：

- author-223 amendment／author-224：UNKNOWN改PARTIAL；同意分類並擴充缺口

### 3338 泰碩／RVL與供貨關係

鍵：`3338:material_named_relationship:f2a716d3ac6b0cbc`；hash：`f2a716d3ac6b0cbccdc75f80bc1ed1766778078c78420c8d9813b2dbf0c95683`。

原claim：已獲 [[NVIDIA]] RVL 推薦供應商資格，產品打入台系與陸系伺服器大廠供應鏈；

同意部分支持，僅支持對NVIDIA/AMD/Intel CPU/GPU平台提供散熱方案的產品範圍。平台相容／配合開發時程不是三家晶片廠的直接採購關係，故不採用作者proposed_text。RVL資格與台系／陸系伺服器大廠供應鏈進入仍未確立；文字層未找到不是資格不存在的證明。

缺口類型：platform_vs_customer_relationship, certification, supply_chain_entry, period。

改寫提案：泰碩2024年度年報介紹用於NVIDIA、AMD、Intel CPU/GPU高效運算伺服器平台的散熱解決方案；未據此認定三家晶片廠為直接客戶或泰碩具RVL資格。

檢視來源：

- [泰碩電子股份有限公司113年度年報](https://www.taisol.com/wp-content/uploads/2025/06/113%E5%B9%B4%E8%82%A1%E6%9D%B1%E6%9C%83%E5%B9%B4%E5%A0%B1.pdf)；PDF第6、58、62頁／印刷頁2、54、58；2024年度；包含2025未來展望／計畫。檢視摘要：[本機紀錄](semantic/reviewer-evidence/reviewer-001/taisol_ar113.md)。

歷史事件：

- author-223 amendment／author-224：UNKNOWN改PARTIAL；分類同意，作者改寫不採用

### 3481 群創／併購與三家客戶

鍵：`3481:material_named_relationship:1a7976baa56b151f`；hash：`1a7976baa56b151ff64ad63f771d53416999af7c7fef7996aa935314e5151d1a`。

原claim：近年積極推動「雙軌轉型」(More than Panel)，拓展非顯示器領域：(1) 車用 — 子公司 CarUX 合併日本 [[Pioneer]]，升級為 Tier 1 車用顯示方案供應商，供應 [[BMW]]、[[GM]]、[[Tesla]] 等車廠；

114年報支持双軌轉型、CarUX Tier 1角色及2025年底收購Pioneer完成，但不能略過BMW、GM、Tesla具名供應關係，也不能將收購無條件寫為法定合併。另有媒體及教育網站圖示線索，未取得對本句時間與關係完整的正式披露，不據摘要或Logo接受全句。

缺口類型：named_customer, acquisition_vs_legal_merger, period。

改寫提案：群創2025年度年報說明雙軌轉型與CarUX車用Tier 1角色，並載CarUX於2025年底完成收購Pioneer；本次未確立本句所列三家車廠供應關係。

檢視來源：

- [群創光電股份有限公司114年度年報](https://www.innolux.com/Uploads/InvestorShareholdersMeetingsFile/%E7%BE%A4%E5%89%B5114%E5%B9%B4%E5%A0%B1_130948.pdf)；PDF第5、14、99頁／印刷頁1、10、95；2025年度；敘述2025年底Pioneer收購完成及2026展望。檢視摘要：[本機紀錄](semantic/reviewer-evidence/reviewer-001/innolux_ar114.md)。

歷史事件：

- author-223 amendment／author-224：UNKNOWN改ACCEPTED；新證據有效但遺漏客戶子句

### 5009 榮剛／三類高毛利

鍵：`5009:profitability_assertion:b8037559961325d8`；hash：`b8037559961325d829c4106c524a6b2ac74b88368dfc15064e9fd1db571ad363`。

原claim：三大高毛利產品線：

新簡報支持高毛利產品接單出貨的概括說法，因此不以舊404維持全文UNKNOWN。但原公司報告冒號後確實有航太、能源、軍工三項，不是無從讀取的缺失context。讀取上下文後仍缺三類各別高毛利的直接綁定或分部數字；並列行業與一句高毛利不能建立逐項關係。

缺口類型：truncated_queue_context_resolved, profitability_category_binding, period。

改寫提案：榮剛日期為2024年3月14日的法說簡報討論航太、能源、油氣與國防等需求，並概括說明高毛利產品接單出貨；未列原文三類各別毛利率。

檢視來源：

- [榮剛材料科技股份有限公司2024法說會簡報](https://emops.twse.com.tw/nas/STR/500920240313E001.pdf)；PDF第9頁／投影片9，近期產業概況；投影片內頁日期2024/3/14；URL檔名含20240313，兩者分開保存。檢視摘要：[本機紀錄](semantic/reviewer-evidence/reviewer-001/gmtc2024.md)。

歷史事件：

- author-261原UNKNOWN與amendment PARTIAL均保留；本review與原decision分歧
- author-262重複項已移除且轉入261 amendment；目前全帳本該key唯一，確認修復
- URL檔名20240313與投影片日期2024/3/14區分保存

### 1305 華夏／87%股權與供應

鍵：`1305:material_named_relationship:374aa8610279391e`；hash：`374aa8610279391ed5ae955d6b3744e783dd95438c19ac849633bd6eeef4bb55`。

原claim：持有[[台灣氯乙烯]] (TVCM) 87% 股權，確保關鍵原料 VCM 穩定供應 (年產能 48.5 萬噸)。

原作者87%依據是2020 CSR節能表0.87%的子字串，且文件被誤稱年報，不能支持股權。新讀2026第二季合併財報確立台氯持股87.31%，2025年報確立VCM產能48.5萬噸；87%可以視為整數近似，但論文應用精確值與日期。持股及產能不能單獨證明「確保穩定供應」這個因果／保證用語，因此完整原句仍僅部分支持。

缺口類型：substring_false_positive, document_type_mismatch, supply_stability_inference, period。

改寫提案：華夏截至2026年6月30日持有台灣氯乙烯87.31%股權；華夏2025年度年報揭露VCM年產能48.5萬噸。

檢視來源：

- [華夏2020企業社會責任報告書（非年報）](https://mopsov.twse.com.tw/server-java/FileDownLoad?step=9&filePath=/home/html/nas/protect/t100/&fileName=t100sa11_1305_109.pdf)；PDF封面、第12、56頁／印刷頁11、55；2020報告；部分2021/2022計畫；歷史快取下载時間未經核實。檢視摘要：[本機紀錄](semantic/reviewer-evidence/reviewer-001/cgpc_csr2020.md)。
- [華夏海灣塑膠股份有限公司114年度年報](https://www.cgpc.com.tw/PDF/Meeting/MeetingP3_115.pdf)；PDF第105、113頁／印刷頁101、109；2025年度；持股表2025-12-31，產能揭露以該年報口徑。檢視摘要：[本機紀錄](semantic/reviewer-evidence/reviewer-001/cgpc_ar114.md)。
- [華夏及子公司115年第二季合併財務報告](https://www.cgpc.com.tw/PDF/Meeting/115Q2m.pdf)；PDF第19、20頁／印刷頁19、20，子公司附註；2026-06-30；比較日期2025-12-31及2025-06-30。檢視摘要：[本機紀錄](semantic/reviewer-evidence/reviewer-001/cgpc_115q2.md)。

## 證據與驗證界線

原始PDF／HTML與完整文字在本機ignored cache，已保存內容hash與頁碼；本commit保存21份檢視摘要、來源manifest、16項重要字串診斷。clone不包含來源原檔，論文交付前需打包並核對。零次命中只限擷取文字層，不能證明圖表或其他文件沒有該內容。此批沒有宣稱驗完所有作者rationale數字。

作者266批共1,399筆，唯一鍵與佇列hash須完全一致；原作者final_state及independent_review仍全部null。Cloud15筆queue未更動；本機觀察另存獨立檔案。既有狀態的未來日期為未核實作者metadata，保留在歷史快照，沒有猜測修補。
