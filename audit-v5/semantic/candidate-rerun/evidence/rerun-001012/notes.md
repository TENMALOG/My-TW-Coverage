# 重驗筆記 — 台光電 / 2383:material_named_relationship:db9504c222045fa9

原始 claim：[[NVIDIA]] (H100/GB200/GB300 OAM/UBB，供應超過 80%)

## 原子主張

1. `SUPPORTED` — 台光電供應 NVIDIA H100 OAM／UBB 所用 CCL 材料。
   期間：截至 2024-03-13 的市場報導
   說明：報導引述法人稱台光電當時是 H100 OAM／UBB 的獨家 CCL 供應商。這支持該時點的供應關係，但不是台光電或 NVIDIA 的直接確認。
   來源：[焦點股》台光電：韓廠斗山搶單？股價連兩日重挫](https://ec.ltn.com.tw/article/breakingnews/4605997)；定位：文中法人分析段
2. `UNKNOWN` — 台光電供應 NVIDIA GB200／GB300 OAM／UBB 所用 CCL 材料。
   期間：GB200／GB300 世代；公開資料所述約為 2025 年
   說明：找到的供應鏈資料沒有充分確認台光電在這些指定板型的實際供應範圍。KGI 報告將 Doosan 列為 B200／300 的 OAM、UBB CCL 供應商，也將台光電列於 GB200 NVL72 Switch Tray；這些不同板型和供應商列示不足以證實或排除台光電供應 GB200／GB300 OAM／UBB。
   來源：[Taiwan IT Hardware Industry Report](https://www.kgi.com.hk/zh-hk/-/media/files/kgishk/research-reports/tw-reports/it-hardware-07072025e.pdf)；定位：圖 19：主要 CPU 及 ASIC 伺服器 CCL 及 PCB 規格比較
   來源：[台光電子材料股份有限公司 2025 年報](https://www.emctw.com/upload/media/New_Investors/Financial_Information/Annual_Reports/CH/2025.pdf)；定位：致股東報告書第 2 頁；PDF 第 5 頁，行 136–162
3. `UNKNOWN` — 台光電在 NVIDIA H100、GB200、GB300 的 OAM／UBB CCL 供應份額均超過 80%。
   期間：原 claim 未指定；可找到的 H100 說法為 2024 年，GB200／GB300 資料約為 2025 年
   說明：「超過 80%」未指明適用哪一世代、OAM 或 UBB、統計期間，或分母是訂單量、材料用量、板數還是供應商份額。2024 年報導稱 H100 OAM／UBB 當時由台光電獨供；同一報導中的「80% 以上訂單」則是對 B100 的市場預期，不能移作 GB200／GB300 證據。另有投資評論轉述元大投顧對 GB200／GB300 UBB 的估計為 20–25%，但未取得原始報告作直接核驗，因此不據此判定相反數字已確證。
   來源：[焦點股》台光電：韓廠斗山搶單？股價連兩日重挫](https://ec.ltn.com.tw/article/breakingnews/4605997)；定位：文中法人分析段
   來源：[台光電（2383）AI 伺服器：市佔率評析與供應鏈驗證邏輯](https://vocus.cc/article/68594fa3fd8978000132d4ca)；定位：「台光電 AI 伺服器市佔率拆解」段

## 判定

Overall `PARTIAL`。

建議改寫：截至 2024 年的媒體報導曾引述法人稱台光電獨供 NVIDIA H100 OAM／UBB 的 CCL；目前查得資料不足以證實台光電在 GB200／GB300 OAM／UBB 的供應範圍或超過 80% 的份額。80% 的期間、產品範圍及分母未明，不能把 H100 的供應說法或 B100 的市場預期外推至 GB200／GB300。

來源限制：
- 台光電最新查得的 2025 年報披露 AI 伺服器材料的概括性領先地位，但未點名 NVIDIA 或披露指定 GPU 世代及板型份額。
- 市場供應鏈報告可作為交叉參考，但供應商名單不等同於完整供貨比例；同一系統中的 OAM、UBB、Switch Tray 等板型不可互換。
- GB200／GB300 UBB 的 20–25% 數字來自投資評論對券商報告的轉述，未取得原始報告直接核驗。

已完成聚焦查找並核對發行人 2025 年報及供應鏈研究資料；公開證據仍未解析 GB200／GB300 的指定板型供應關係，也未界定或驗證「超過 80%」的期間與分母。

此紀錄來自獨立 Hermes 單筆重驗。只追加候選重驗結果，未修改原報告、作者決策或既有複核帳本。
