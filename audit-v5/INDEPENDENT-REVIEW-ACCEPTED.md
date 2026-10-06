# 作者 ACCEPTED 111筆的獨立複核總表

截至 2026-10-06T01:17:15.066958Z，原作者標為 ACCEPTED 的111筆已全部獨立讀取來源並複核；本步新增108筆，另3筆已在 reviewer-001 完成。作者判定不是採納依據。本次不是盲審：已知道作者標籤及交接疑點，判定依來源內容與上下文逐子句進行。

| 獨立複核判定 | 筆數 | 原完整句可用性 |
|---|---:|---|
| ACCEPTED | 21 | 可引用，但須保留來源主體、產品範圍、期間及自述性質 |
| PARTIALLY_SUPPORTED | 70 | 部分子句有支持；完整句與改寫提案仍待裁決 |
| PERIOD_UNRESOLVED | 19 | 來源中的歷史資料不足以確立原句未限定期間的現在狀態 |
| UNKNOWN_AFTER_RESEARCH | 1 | 未能確立，不代表內容為假 |
| 合計 | 111 | 90筆與作者不同，final_state 保持分歧待裁決 |

整體獨立複核為120/1,399，其餘1,279筆尚未複核。120筆的 reviewer ACCEPTED 有22筆，但 final ACCEPTED 只有21筆：另一筆1722與作者不同，仍待裁決。不能混用作者判定、reviewer判定及final_state三種計數。

## 先前是否有來源

這111筆作者紀錄均列有來源參照。本次逐筆另存來源原始內容或明確標示的網頁可讀摘錄、SHA-256、頁碼／段落、期間和子句判定。然而「列有URL」與「內容支持整句」不同：取回的200頁面可能是保護頁、空殼；可讀文件也可能年份過舊、主體錯置或只支持部分產品。1筆研究後未確立及19筆期間未解都不能轉成內容有誤。

本次讀PDF文字與上下文，對指定圖表、封面及字型不良頁面做影像檢視；沒有宣稱逐頁看完每份年報。字串數量僅是診斷，不是關係或排名的證明；沒有宣稱已驗證所有作者 rationale 的數字。

## 對論文寫作的影響

21筆通過是句子層級的來源支持，不是第三方對所有市場事實的測量。公司官網或簡報宣稱的「最大／第一」，論文應寫成「公司於某年報／網頁自述」，列出產品與比較範圍；來源未提供母體、指標、資料期間及計算方法時，不得自行補上。歷史更名、設立與併購要寫出發生年度；股東投資、集團歸屬、子公司、客戶及供應商不可互換。

90筆仍待裁決，其 proposed_text 是有來源依據的改寫候選，尚未正式接受，也沒有寫回發行人報告。若論文需要這些內容，先裁決子句及改寫；不能直接把作者ACCEPTED或複核的提案當定論。

交接中特別提到的薄證據結果：世德Tier1/Tier2與東隆興POY/FDY為部分支持；三星的95%涉及產品及歐美日範圍，為部分支持；新海的獨家氣源由2023年報支持，但未確立未限定期間的現在狀態，為期間未解。華夏已在 reviewer-001 判為部分支持並保留分歧。相關頁碼、來源及缺口均在下表所連結批次。

## 更正與保存

新增 [reviewer-amendments-001.json](semantic/reviewer-amendments-001.json)：群光2024年報實體第6頁明列鍵盤、影像、電源三大事業部，故移除該筆 business_group_count 缺口；筆電鍵盤全球第一仍未確立。原 reviewer-003、判定及final_state未改。下列總表及JSON索引套用此子句更正，不另計新claim。

作者266份帳本、1,399個原final_state與independent_review的null、發行人報告及Cloud15筆失敗觀察保留原樣。各批最多25筆且唯一鍵與佇列hash一致。本機取得的全部觀察另存 [accepted-review-retrieval-observations.json](semantic/accepted-review-retrieval-observations.json)，網路成功或失敗沒有直接決定語意。

原PDF／HTML在ignored本機快取，Git clone不含它們；論文交付前還需打包來源原檔並核對hash。明基集團頁的可讀摘錄明記hash僅覆蓋保存的UTF-8摘錄，不冒稱原HTML原檔。歷史快取首次取得日期不明則為null，不沿用未核實的作者時間。

結構化索引：[accepted-review-index.json](semantic/accepted-review-index.json)，含111筆完整原claim、作者／reviewer批次hash、有效子句、更正、來源定位、缺口及改寫候選。這是衍生索引，不是第三份判定帳本。

## 111筆索引（依原佇列順序）

| # | 公司／Ticker | Claim | Reviewer | Final state | 批次 |
|---:|---|---|---|---|---|
| 1 | 台船／2208 | 台灣國際造船 (2208，CSBC Corporation) 是台灣最大的造船廠，隸屬公營事業體系。 | PARTIALLY_SUPPORTED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-002.json](INDEPENDENT-REVIEW-002.md) |
| 2 | 台船／2208 | [[中鋼]] — 造船用低溫鋼板主要供應商 | UNKNOWN_AFTER_RESEARCH | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-002.json](INDEPENDENT-REVIEW-002.md) |
| 3 | 漢翔／2634 | 與[[Lockheed Martin]]合作建立亞太唯一 [[F-16]] 維修中心； | PARTIALLY_SUPPORTED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-002.json](INDEPENDENT-REVIEW-002.md) |
| 4 | 中信造船／2644 | 中信造船 (2644，Jong Shyn Shipbuilding) 為台灣規模最大的民營造船廠，由「台灣船王」韓碧祥創辦。 | PARTIALLY_SUPPORTED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-002.json](INDEPENDENT-REVIEW-002.md) |
| 5 | 中信造船／2644 | 旗下子公司高鼎遊艇為亞洲最大鋼鋁遊艇製造商。 | PARTIALLY_SUPPORTED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-002.json](INDEPENDENT-REVIEW-002.md) |
| 6 | 台灣虎航／6757 | 年輕自由行觀光客 — 日本為最大航線市場 | PARTIALLY_SUPPORTED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-002.json](INDEPENDENT-REVIEW-002.md) |
| 7 | 立敦／6175 | [[Nippon Chemi-Con]] — 全球最大鋁電解電容廠； | ACCEPTED | ACCEPTED | [reviewer-002.json](INDEPENDENT-REVIEW-002.md) |
| 8 | 如興／4414 | [[Levi's]] — 主要客戶； | PERIOD_UNRESOLVED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-005.json](INDEPENDENT-REVIEW-005.md) |
| 9 | 如興／4414 | [[GAP]] — 主要客戶； | PERIOD_UNRESOLVED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-005.json](INDEPENDENT-REVIEW-005.md) |
| 10 | 和泰車／2207 | 和泰汽車 (2207，Hotai Motor) 為台灣最大汽車經銷商，獨家代理[[Toyota Motor Corporation]]、[[Lexus]]及[[日野汽車]] (Hino) 品牌，國內新車市佔率約 40%。 | PARTIALLY_SUPPORTED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-002.json](INDEPENDENT-REVIEW-002.md) |
| 11 | 和泰車／2207 | 在台製造夥伴為[[國瑞汽車]] ([[Toyota]]/Hino 台灣唯一組裝廠)。 | PARTIALLY_SUPPORTED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-002.json](INDEPENDENT-REVIEW-002.md) |
| 12 | 和泰車／2207 | [[國瑞汽車]] — [[Toyota]]/Hino 台灣唯一組裝廠 | PARTIALLY_SUPPORTED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-002.json](INDEPENDENT-REVIEW-002.md) |
| 13 | 三陽工業／2206 | 機車事業方面，公司以自有品牌「SYM」穩居台灣機車市佔率龍頭，並外銷至全球市場，同時替歐洲品牌 (如 Peugeot、Lambretta) 代工。 | ACCEPTED | ACCEPTED | [reviewer-002.json](INDEPENDENT-REVIEW-002.md) |
| 14 | 東陽／1319 | [[LKQ]]、[[Keystone Automotive]] — 北美最大 AM 經銷 | PARTIALLY_SUPPORTED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-002.json](INDEPENDENT-REVIEW-002.md) |
| 15 | 東陽／1319 | [[LKQ]]、[[Keystone Automotive]] — 北美最大 AM 通路 | PARTIALLY_SUPPORTED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-002.json](INDEPENDENT-REVIEW-002.md) |
| 16 | 台翰／1336 | 最大股東為[[宣德科技]]，最終母公司為中國[[立訊精密]]。 | PARTIALLY_SUPPORTED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-002.json](INDEPENDENT-REVIEW-002.md) |
| 17 | 台翰／1336 | [[宣德科技]] (最大股東)、[[立訊精密]] (最終母公司) | PARTIALLY_SUPPORTED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-002.json](INDEPENDENT-REVIEW-002.md) |
| 18 | 廣華-KY／1338 | 客戶結構已從日系為主轉型為多元分散：日系 46% — [[Nissan]] (最大客戶)、[[Honda]]； | PERIOD_UNRESOLVED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-002.json](INDEPENDENT-REVIEW-002.md) |
| 19 | 廣華-KY／1338 | [[Nissan]] (最大客戶)、[[Honda]] | PERIOD_UNRESOLVED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-002.json](INDEPENDENT-REVIEW-002.md) |
| 20 | 和大／1536 | 和大工業 (1536，Hota Industrial) 為台灣最大汽車齒輪與傳動零件製造商。 | ACCEPTED | ACCEPTED | [reviewer-002.json](INDEPENDENT-REVIEW-002.md) |
| 21 | 巧新／1563 | [[Otto Fuchs]] — 全球第一大鍛造輪圈廠 (德國) | PARTIALLY_SUPPORTED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-002.json](INDEPENDENT-REVIEW-002.md) |
| 22 | 建大／2106 | 建大工業 (2106，Kenda Rubber Industrial) 為全球前 30 大輪胎廠，自有品牌[[Kenda]]行銷全球。 | PARTIALLY_SUPPORTED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-002.json](INDEPENDENT-REVIEW-002.md) |
| 23 | 鑫永銓／2114 | (2) 橡皮壩 — 日本進口第一大供應商，應用於水利基礎設施； | PERIOD_UNRESOLVED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-002.json](INDEPENDENT-REVIEW-002.md) |
| 24 | 鑫永銓／2114 | 橡皮壩 — 日本進口第一 | PERIOD_UNRESOLVED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-002.json](INDEPENDENT-REVIEW-002.md) |
| 25 | 鑫永銓／2114 | 日本水利基礎設施 — 橡皮壩進口第一 | PERIOD_UNRESOLVED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-002.json](INDEPENDENT-REVIEW-002.md) |
| 26 | 謚源／2235 | [[LKQ]] — 美國最大汽車零件商； | PARTIALLY_SUPPORTED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-002.json](INDEPENDENT-REVIEW-002.md) |
| 27 | 英利-KY／2239 | 核心客戶為[[一汽大眾]] (FAW-VW，最大客戶)、[[北京奔馳]] (Beijing Benz)、[[上汽大眾]] (SAIC-VW)，另供應[[Audi]] (一汽奧迪全車系儀錶板骨架)。 | PERIOD_UNRESOLVED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-002.json](INDEPENDENT-REVIEW-002.md) |
| 28 | 英利-KY／2239 | [[一汽大眾]] (最大客戶)、[[北京奔馳]]、[[上汽大眾]]、[[Audi]] — 車身結構件 | PERIOD_UNRESOLVED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-003.json](INDEPENDENT-REVIEW-003.md) |
| 29 | 永新-KY／4557 | 永新應用科技-KY (4557) 為北美最大 AM 煞車總泵/分泵供應商，正拓展煞車卡鉗及 OEM 煞車來令片 (中國電動車市場)。 | PARTIALLY_SUPPORTED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-003.json](INDEPENDENT-REVIEW-003.md) |
| 30 | 彰銀／2801 | [[財政部]]為最大股東，全台設有逾 180 家國內分行，海外據點遍及紐約、東京、倫敦、香港、新加坡等地。 | PARTIALLY_SUPPORTED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-003.json](INDEPENDENT-REVIEW-003.md) |
| 31 | 華南金／2880 | [[華南金融控股]] (2880) 成立於 2001 年，為台灣第一家依《金融控股公司法》成立的金控。 | ACCEPTED | ACCEPTED | [reviewer-003.json](INDEPENDENT-REVIEW-003.md) |
| 32 | 華南金／2880 | [[財政部]]透過[[台灣銀行]]間接為最大股東。 | PERIOD_UNRESOLVED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-003.json](INDEPENDENT-REVIEW-003.md) |
| 33 | 玉山金／2884 | 其他子公司包括[[玉山證券]]及[[玉山投信]] (2025 年收購[[保德信投信]]後更名)。 | ACCEPTED | ACCEPTED | [reviewer-005.json](INDEPENDENT-REVIEW-005.md) |
| 34 | 永豐金／2890 | 永豐銀行在太陽能光電融資領域市占率全台第一 (近三成)，為台灣綠色金融標竿銀行。 | PARTIALLY_SUPPORTED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-003.json](INDEPENDENT-REVIEW-003.md) |
| 35 | 第一金／2892 | **[[第一金證券]]** (證券經紀) | ACCEPTED | ACCEPTED | [reviewer-003.json](INDEPENDENT-REVIEW-003.md) |
| 36 | 第一金／2892 | **[[第一金投信]]** (基金管理) | ACCEPTED | ACCEPTED | [reviewer-003.json](INDEPENDENT-REVIEW-003.md) |
| 37 | 第一金／2892 | **[[第一金人壽]]** (壽險) | ACCEPTED | ACCEPTED | [reviewer-003.json](INDEPENDENT-REVIEW-003.md) |
| 38 | 王道銀行／2897 | [[王道商業銀行]] (2897) 前身為[[台灣工業銀行]]，2017 年改制為商業銀行並更名。 | ACCEPTED | ACCEPTED | [reviewer-005.json](INDEPENDENT-REVIEW-005.md) |
| 39 | 台泥／1101 | 台灣水泥股份有限公司 (1101，TCC Group) 成立於 1946 年，為台灣第一家股票上市公司，已從傳統水泥製造廠轉型為「綠色環境工程集團」。 | PARTIALLY_SUPPORTED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-003.json](INDEPENDENT-REVIEW-003.md) |
| 40 | 國產／2504 | 公司為台灣 **預拌混凝土 (Ready-Mixed Concrete)** 龍頭，市占率全台第一。 | PARTIALLY_SUPPORTED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-003.json](INDEPENDENT-REVIEW-003.md) |
| 41 | 中聯資源／9930 | 公司為台灣規模最大之高爐石粉專業產銷業者，在**循環經濟**領域扮演樞紐角色。 | PARTIALLY_SUPPORTED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-003.json](INDEPENDENT-REVIEW-003.md) |
| 42 | 上福／6128 | 上福全球科技股份有限公司 (6128) 是台灣唯一具備碳粉匣及 OPC 感光鼓精密齒輪研發與製造能力的事務機器耗材大廠。 | PARTIALLY_SUPPORTED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-003.json](INDEPENDENT-REVIEW-003.md) |
| 43 | 阜爾運通／6914 | 阜爾運通股份有限公司 (6914) 為台灣市佔率最高的連鎖停車場品牌「[[城市車旅]] (City Parking)」營運商。 | PARTIALLY_SUPPORTED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-003.json](INDEPENDENT-REVIEW-003.md) |
| 44 | 華票／2820 | [[王道銀行]] (持股約 28%) — 最大股東 | PERIOD_UNRESOLVED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-003.json](INDEPENDENT-REVIEW-003.md) |
| 45 | 中碳／1723 | 公司為[[中鋼集團]]成員，是台灣唯一之專業[[煤化工]]製造商。 | ACCEPTED | ACCEPTED | [reviewer-003.json](INDEPENDENT-REVIEW-003.md) |
| 46 | 合勤控／3704 | 公司 2026 年獲選入 S&P Global 永續年鑑，在全球電信設備製造商中排名第一。 | PARTIALLY_SUPPORTED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-003.json](INDEPENDENT-REVIEW-003.md) |
| 47 | 岳豐／6220 | 公司最大競爭優勢在於深度「垂直整合」，透過併購美國 Prime Wire & Cable (實體通路電源線品牌) 及 [[Monoprice]] (知名 3C 電商平台)，將製造端與北美終端消費市場直接串聯。 | PARTIALLY_SUPPORTED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-003.json](INDEPENDENT-REVIEW-003.md) |
| 48 | 立端／6245 | 2020 年[[台達電]] (Delta Electronics) 入股成為最大股東，提供電源管理及散熱技術支援。 | PARTIALLY_SUPPORTED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-003.json](INDEPENDENT-REVIEW-003.md) |
| 49 | 達運光電／8045 | 公司為亞洲唯一通過北美主要有線電視多系統營運商 (MSO) 認證之混合光纖同軸 ([[HFC]]) 傳輸設備研發製造廠商，並以自有品牌 ACI 行銷全球。 | PARTIALLY_SUPPORTED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-003.json](INDEPENDENT-REVIEW-003.md) |
| 50 | 達運光電／8045 | 公司出口以美國為最大宗，佔營業額七成以上，已成功通過 [[Comcast]] 嚴格認證並打入北美大型營運商一級供應鏈。 | PARTIALLY_SUPPORTED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-003.json](INDEPENDENT-REVIEW-003.md) |
| 51 | 中環／2323 | **中環** (全球最大 CD/DVD/Blu-ray 光碟 OEM 廠) | PERIOD_UNRESOLVED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-003.json](INDEPENDENT-REVIEW-003.md) |
| 52 | 廣達／2382 | **[[廣達]]** (全球最大筆電 ODM 廠) | PARTIALLY_SUPPORTED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-003.json](INDEPENDENT-REVIEW-003.md) |
| 53 | 群光／2385 | 三大事業群：(1) 輸入裝置：筆電鍵盤 (全球市佔第一)、桌機鍵盤、滑鼠； | PARTIALLY_SUPPORTED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-003.json](INDEPENDENT-REVIEW-003.md) |
| 54 | 群光／2385 | (2) 影像模組：攝影機模組 (全球市佔第一)、行車紀錄器、戶外 IP Cam、穿戴式攝影機、車用影像系統及 LED 車燈； | PARTIALLY_SUPPORTED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-003.json](INDEPENDENT-REVIEW-003.md) |
| 55 | 群光／2385 | **群光** (筆電鍵盤全球第一、桌機鍵盤/滑鼠) | PARTIALLY_SUPPORTED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-004.json](INDEPENDENT-REVIEW-004.md) |
| 56 | 精元／2387 | 精元電腦 (2387，[[Sunrex Technology]]) 成立於 1975 年，總部位於台中，為全球最大筆記型電腦鍵盤製造商。 | ACCEPTED | ACCEPTED | [reviewer-004.json](INDEPENDENT-REVIEW-004.md) |
| 57 | 精元／2387 | **精元** (全球最大筆電鍵盤製造商) | ACCEPTED | ACCEPTED | [reviewer-004.json](INDEPENDENT-REVIEW-004.md) |
| 58 | 精聯／3652 | 精技電腦 (2414) — 原分割母公司 | ACCEPTED | ACCEPTED | [reviewer-005.json](INDEPENDENT-REVIEW-005.md) |
| 59 | 天品／6199 | 憑藉深厚的[[半導體]]清洗經驗與高階無塵室設備，天品成功打入國際知名[[AI]]晶片(如Rubin)[[散熱]]系統([[水冷]]/液冷)的清洗服務供應鏈，打造出第二成長曲線。 | PARTIALLY_SUPPORTED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-005.json](INDEPENDENT-REVIEW-005.md) |
| 60 | 新普／6121 | 新普科技股份有限公司 (6121) 是全球最大的筆記型電腦鋰離子電池模組製造商，市佔率極高(約每三台筆電就有一台使用新普電池)。 | PERIOD_UNRESOLVED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-004.json](INDEPENDENT-REVIEW-004.md) |
| 61 | 億光／2393 | 億光電子 (2393) 是台灣最大的 [[LED]] 專業封裝廠，產品涵蓋照明元件、背光元件、手持裝置元件、車用元件及不可見光元件，產值明顯超越台灣同業。 | PARTIALLY_SUPPORTED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-004.json](INDEPENDENT-REVIEW-004.md) |
| 62 | 億光／2393 | **億光** (台灣最大 LED 封裝，照明/車用/紅外線) | PARTIALLY_SUPPORTED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-004.json](INDEPENDENT-REVIEW-004.md) |
| 63 | 一詮／2486 | 一詮精密 (2486) 是全球最大的 [[LED 導線架]]製造商，產品涵蓋 LED [[導線架]]、IC [[導線架]]、[[陶瓷基板]]及[[散熱]]元件 (均熱片)。 | PARTIALLY_SUPPORTED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-004.json](INDEPENDENT-REVIEW-004.md) |
| 64 | 一詮／2486 | **一詮** (全球最大 LED [[導線架]]，含陶瓷基板/均熱片) | PARTIALLY_SUPPORTED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-004.json](INDEPENDENT-REVIEW-004.md) |
| 65 | 精金／3049 | 早期從事彩色濾光片，後轉型為觸控感應器 (Touch Sensor) 專業製造商，主要為 [[瀚宇彩晶]] (最大股東) 供應觸控面板。 | PARTIALLY_SUPPORTED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-004.json](INDEPENDENT-REVIEW-004.md) |
| 66 | 日電貿／3090 | 日電貿 ([[Nichidenbo]]) 為台灣最大專業被動元件通路商。 | ACCEPTED | ACCEPTED | [reviewer-004.json](INDEPENDENT-REVIEW-004.md) |
| 67 | 日電貿／3090 | 核心代理產品：(1) 鋁質電解電容 — 代理日本 [[Nippon Chemi-con]] (NCC，全球第一大)； | ACCEPTED | ACCEPTED | [reviewer-004.json](INDEPENDENT-REVIEW-004.md) |
| 68 | 日電貿／3090 | [[Nippon Chemi-con]] (NCC) — 全球第一大 | PARTIALLY_SUPPORTED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-004.json](INDEPENDENT-REVIEW-004.md) |
| 69 | 日電貿／3090 | [[Nippon Chemi-con]] — 全球第一大鋁電解電容 | ACCEPTED | ACCEPTED | [reviewer-004.json](INDEPENDENT-REVIEW-004.md) |
| 70 | 泰碩／3338 | 泰碩電子 (3338，[[TaiSol]]) 為專業散熱模組與連接器製造商，近年成功轉型為 [[AI 伺服器]]液冷散熱核心供應商。 | PARTIALLY_SUPPORTED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-001.json](INDEPENDENT-REVIEW-001.md) |
| 71 | 由田／3455 | 近年積極轉型 **半導體封裝檢測**，尤其在 **IC 載板** ([[ABF]]/BT) 外觀檢查具有高市佔。 | PARTIALLY_SUPPORTED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-004.json](INDEPENDENT-REVIEW-004.md) |
| 72 | 群創／3481 | 近年積極推動「雙軌轉型」(More than Panel)，拓展非顯示器領域：(1) 車用 — 子公司 CarUX 合併日本 [[Pioneer]]，升級為 Tier 1 車用顯示方案供應商，供應 [[BMW]]、[[GM]]、[[Tesla]] 等車廠； | PARTIALLY_SUPPORTED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-001.json](INDEPENDENT-REVIEW-001.md) |
| 73 | 光頡／3624 | 3. **車用市場**: 通過 [[AEC-Q200]] 認證，打入 Tier 1 車廠與 [[電動車]] 供應鏈 (OBC、BMS 應用)。 | PARTIALLY_SUPPORTED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-005.json](INDEPENDENT-REVIEW-005.md) |
| 74 | 三聯／5493 | (2) 自動化監測 — 提供地震預警、水庫/橋樑土木工程安全監測服務，為國內環境監測與微振動感測技術第一品牌； | PARTIALLY_SUPPORTED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-004.json](INDEPENDENT-REVIEW-004.md) |
| 75 | 鈺邦／6449 | 鈺邦科技股份有限公司 (6449) 隸屬於[[華新科]]集團，是全球產能及市佔率名列前茅的導電高分子固態電容(Solid Capacitor)製造商。 | PARTIALLY_SUPPORTED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-004.json](INDEPENDENT-REVIEW-004.md) |
| 76 | 澤米／6742 | 業務結構與動能：(1) AR/VR 光學元件 — 投入光波導 (LOE) 顯示元件鍍膜技術，掌握奈米級光學薄膜製程，成功打入 [[Meta]] AR 眼鏡供應鏈，供應繞射/光導光學元件鍍膜； | PARTIALLY_SUPPORTED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-005.json](INDEPENDENT-REVIEW-005.md) |
| 77 | 明基材／8215 | 明基材料 (8215，BenQ Materials) 為 [[明基]] (BenQ) 集團旗下之先進材料公司，前身為達信科技，2010 年更名。 | ACCEPTED | ACCEPTED | [reviewer-006.json](INDEPENDENT-REVIEW-006.md) |
| 78 | 華宏／8240 | 核心業務涵蓋：(1) 光電材料 — 為台灣背光模組光學膜片最大專業裁切廠，產品包括 [[偏光板]]、擴散膜、增亮膜、導光板、量子點膜、觸控面板防爆膜等，服務面板廠之背光模組需求； | PARTIALLY_SUPPORTED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-004.json](INDEPENDENT-REVIEW-004.md) |
| 79 | 神腦／2450 | 神腦國際企業 (2450，Senao International) 成立於 1979 年，總部位於新北市，為台灣最大通訊通路代理商，隸屬於[[中華電信]]集團。 | PARTIALLY_SUPPORTED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-004.json](INDEPENDENT-REVIEW-004.md) |
| 80 | 力致／3483 | 在筆記型電腦 (NB) 風扇市場擁有極高市佔率，為主要獲利來源。 | PARTIALLY_SUPPORTED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-004.json](INDEPENDENT-REVIEW-004.md) |
| 81 | 愛爾達-創／8487 | 愛爾達科技 (8487，ELTA Technology) 為台灣第一家以體育賽事轉播為核心的新媒體平台。 | PARTIALLY_SUPPORTED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-004.json](INDEPENDENT-REVIEW-004.md) |
| 82 | 寶成／9904 | 寶成工業股份有限公司 (9904) 成立於 1969 年，總部位於台灣台中，為全球最大的品牌運動鞋與休閒鞋製造商。 | PARTIALLY_SUPPORTED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-004.json](INDEPENDENT-REVIEW-004.md) |
| 83 | 現觀科／6906 | [[Saudi Telecom]] (STC) — 中東最大電信 | PERIOD_UNRESOLVED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-004.json](INDEPENDENT-REVIEW-004.md) |
| 84 | 現觀科／6906 | [[Saudi Telecom]] (STC) — 中東最大電信營運商 | PERIOD_UNRESOLVED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-004.json](INDEPENDENT-REVIEW-004.md) |
| 85 | 中再保／2851 | 中央再保險 (2851，Central Reinsurance Corp.) 成立於 1968 年，2002 年完成民營化，現由[[長榮集團]]入主為最大股東。 | PARTIALLY_SUPPORTED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-004.json](INDEPENDENT-REVIEW-004.md) |
| 86 | 數字／5287 | (2) 8591 寶物交易網 — 台灣最大遊戲虛擬寶物交易平台，以手續費為收入模式； | ACCEPTED | ACCEPTED | [reviewer-004.json](INDEPENDENT-REVIEW-004.md) |
| 87 | 科定／6655 | 生產總部位於嘉義大埔美工業區，擁有業界唯一從原木採購到終端銷售通路的完整一條龍垂直整合產線。 | PARTIALLY_SUPPORTED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-005.json](INDEPENDENT-REVIEW-005.md) |
| 88 | 聯友金屬-創／7610 | [[Apple]] — 100% 再生[[鎢]]金屬供應商 | PARTIALLY_SUPPORTED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-006.json](INDEPENDENT-REVIEW-006.md) |
| 89 | 龍巖／5530 | 全台各地家庭 — 龍巖生前契約市占率約 79% | PARTIALLY_SUPPORTED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-005.json](INDEPENDENT-REVIEW-005.md) |
| 90 | 富華新／3056 | [[富華創新]] (3056，富華新，原總太地產) 發跡於台中，2023 年由「總太地產」正式更名。 | PARTIALLY_SUPPORTED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-006.json](INDEPENDENT-REVIEW-006.md) |
| 91 | 聚積／3527 | **聚積** (全球第一大 LED 顯示屏驅動 IC) | PERIOD_UNRESOLVED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-005.json](INDEPENDENT-REVIEW-005.md) |
| 92 | 敦泰／3545 | 敦泰電子 (3545) 是全球最大電容式觸控 IC 出貨商之一，產品涵蓋觸控 IC、顯示驅動 IC、[[TDDI]] (觸控顯示整合單晶片) 及指紋辨識 IC。 | PARTIALLY_SUPPORTED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-005.json](INDEPENDENT-REVIEW-005.md) |
| 93 | 敦泰／3545 | **敦泰** (TDDI/觸控/驅動/指紋，全球最大觸控 IC 之一) | PARTIALLY_SUPPORTED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-005.json](INDEPENDENT-REVIEW-005.md) |
| 94 | 福懋科／8131 | [[南亞科技]]持股 32% 為第一大股東，[[福懋興業]]持股約 30% 為第二大股東，形成集團內垂直整合。 | PARTIALLY_SUPPORTED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-005.json](INDEPENDENT-REVIEW-005.md) |
| 95 | 微矽電子-創／8162 | 微矽電子 (8162) 深耕半導體後段服務逾 38 年，為國內[[電源管理 IC]]、[[MOSFET]] 及 [[氮化鎵]] 晶圓測試最大供應商，以「晶圓廠內部實驗室」創新模式與知名晶圓代工廠合作。 | PARTIALLY_SUPPORTED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-005.json](INDEPENDENT-REVIEW-005.md) |
| 96 | 微矽電子-創／8162 | **微矽** (電源 IC/[[MOSFET]]/GaN 晶圓測試最大供應商) | PERIOD_UNRESOLVED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-005.json](INDEPENDENT-REVIEW-005.md) |
| 97 | 聯合再生／3576 | 聯合再生能源股份有限公司 (3576) 為台灣最大的太陽能模組品牌與系統整合廠，由[[新日光]]、[[昱晶]]、[[昇陽光電]]三家合併而成。 | PARTIALLY_SUPPORTED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-005.json](INDEPENDENT-REVIEW-005.md) |
| 98 | 聯合再生／3576 | 1. **太陽能模組：** 經營自有品牌，主攻台灣內需市場，連續多年維持台灣模組銷售市占率第一。 | PARTIALLY_SUPPORTED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-005.json](INDEPENDENT-REVIEW-005.md) |
| 99 | 耕興／6146 | 1. **[[EMC]]電磁相容性測試：** 台灣擁有3座規模最大的[[EMC]]與安規專業認證實驗室。 | PARTIALLY_SUPPORTED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-005.json](INDEPENDENT-REVIEW-005.md) |
| 100 | 華夏／1305 | 持有[[台灣氯乙烯]] (TVCM) 87% 股權，確保關鍵原料 VCM 穩定供應 (年產能 48.5 萬噸)。 | PARTIALLY_SUPPORTED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-001.json](INDEPENDENT-REVIEW-001.md) |
| 101 | 達輝光電／6434 | 達輝光電 (6434，TacBright Optronics) 為台灣唯一具 TAC (三醋酸纖維素) 光學膜量產技術之專業廠商，[[新光合纖]]轉投資子公司。 | PARTIALLY_SUPPORTED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-005.json](INDEPENDENT-REVIEW-005.md) |
| 102 | 中華電／2412 | 業務結構與動能：(1) 行動通訊 — [[5G]]/4G 行動網路服務，為台灣用戶數最大之電信營運商； | ACCEPTED | ACCEPTED | [reviewer-005.json](INDEPENDENT-REVIEW-005.md) |
| 103 | 華電網／6163 | 公司曾建置台灣首套 ADSL 系統及最大 IPTV (MOD) 系統。 | ACCEPTED | ACCEPTED | [reviewer-005.json](INDEPENDENT-REVIEW-005.md) |
| 104 | 南紡／1440 | 紡織部門為台灣最大聚酯棉/紡紗廠之一，產品包括棉紗、聚酯粒、聚酯棉、機能性布料，產能布局台灣及越南； | PARTIALLY_SUPPORTED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-005.json](INDEPENDENT-REVIEW-005.md) |
| 105 | 力鵬／1447 | [[力鵬]]企業 (Li Peng Enterprise) 為力麗集團成員，亞洲最大的[[尼龍粒]] (Nylon Chips) 生產商之一。 | PARTIALLY_SUPPORTED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-005.json](INDEPENDENT-REVIEW-005.md) |
| 106 | 東隆興／4401 | **上游**：採購 [[POY]] (預取向絲) 與 [[FDY]] (全延伸絲) 原絲，主要供應商為 [[遠東新]]、[[力鵬]]。 | PARTIALLY_SUPPORTED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-006.json](INDEPENDENT-REVIEW-006.md) |
| 107 | 世德／2066 | 世德已通過 [[GM]] (通用汽車) 及 [[Chrysler]] (克萊斯勒) Tier 1 供應商認證，並為 [[Toyota]] 及 [[Tesla]] 之 Tier 2 供應商。 | PARTIALLY_SUPPORTED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-006.json](INDEPENDENT-REVIEW-006.md) |
| 108 | 三星／5007 | 外銷比重逾 95%，以歐美市場為主。 | PARTIALLY_SUPPORTED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-006.json](INDEPENDENT-REVIEW-006.md) |
| 109 | 新海／9926 | [[台灣中油]]（CPC，天然氣獨家供應商） | PERIOD_UNRESOLVED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-006.json](INDEPENDENT-REVIEW-006.md) |
| 110 | 新海／9926 | [[台灣中油]]（CPC，天然氣獨家供應來源） | PERIOD_UNRESOLVED | ESCALATED_REVIEW_DISAGREEMENT | [reviewer-006.json](INDEPENDENT-REVIEW-006.md) |
| 111 | 日友／8341 | 日友環保科技股份有限公司 (8341) 成立於1994年，為台灣第一家專業生物醫療廢棄物焚化處理廠。 | ACCEPTED | ACCEPTED | [reviewer-005.json](INDEPENDENT-REVIEW-005.md) |

## 完整性驗證

- 44/44 tests passed：既有37個regression tests及7個更正／索引完整性測試。
- 檢查2,026份受保護檔案：266份作者帳本、1,733份發行人報告、26份首批reviewer紀錄及Cloud佇列；hash異動0。
- 本機126份保存的回應／快取來源原檔或明示範圍的文字摘錄，hash不符0。未取得原檔的失敗觀察另記，不假造內容hash。
- 1,399個作者唯一鍵與佇列一致且作者null政策維持；120個reviewer唯一鍵無重複；111筆ACCEPTED索引與套用更正後的帳本一致。

驗證紀錄：[accepted-cohort-validation.json](semantic/reviewer-evidence/accepted-cohort-validation.json)。驗證命令：`.venv/Scripts/python.exe -X utf8 audit-v5/validate_reviewer_ledger.py --check-local-sources`。本機Python版本為3.13.15；本次未在交接建議的3.12重跑。測試驗證帳本與程式完整性，不替代語意判定。
