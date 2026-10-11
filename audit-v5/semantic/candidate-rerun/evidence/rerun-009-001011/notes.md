# 重驗筆記 — 台光電 / 2383:material_named_relationship:76a1350152921c96

原始 claim：為 [[NVIDIA]] H100/GB200/GB300 系列 [[AI 伺服器]] OAM 及 UBB 的主要高階 CCL 供應商 (供應比重超過 80%)，亦為 [[AWS]] 自研 AI 晶片 Trainium 2/3 的 M8 等級高階材料獨家供應商。

## 原子主張

1. `SUPPORTED` — 台光電於2023年是 NVIDIA H100 AI 伺服器 OAM/UBB 的主要高階 CCL 供應商，供應比重超過 80%。
   期間：2023年（來源報導日期：2023-08-23）
   說明：次級報導稱台光電是 NVIDIA 伺服器 CCL 主要供應商，整體市占率超過80%，並稱 OAM 與 UBB 市占率超過90%。報導未交代市占計算方式、具體出貨期間或分母定義；此證據僅限當時報導，不可外推至 GB200/GB300。
   來源：[〖新台股龍捲風〗當大家都在看NVIDIA財報時，美國偷偷出現小動作！？目的？](https://news.cnyes.com/news/id/5299807)；定位：正文第21行
2. `UNKNOWN` — 台光電是 NVIDIA GB200/GB300 系列 AI 伺服器 OAM 及 UBB 的主要高階 CCL 供應商。
   期間：至少涉及2025年產品配置；來源未驗證實際全年供貨情況
   說明：凱基2025年7月的供應商估列將台光電列為 GB200 NVL72 Switch tray 的 M8 CCL 供應商，但將 GB200 Compute tray、B200/300 UBB 與 OAM 列為斗山供應。這與台光電在其他部分供貨相容，但不能證明其是所稱 OAM/UBB 的主要供應商；報告未提供該精確範圍的份額。
   來源：[台灣電子硬體產業：IT Hardware](https://www.kgi.com.hk/zh-cn/-/media/files/kgishk/research-reports/tw-reports/it-hardware-07072025e.pdf)；定位：第8頁圖19，PDF行581-593
3. `UNKNOWN` — 台光電在 NVIDIA GB200/GB300 指定 OAM/UBB CCL 市場的供應比重超過80%。
   期間：未能確認；相關次級資料涵蓋2025年
   說明：未找到採用相同產品範圍、期間與分母的可靠份額數據。TechNews轉述外資估算台光電 GB300 的 AI GPU CCL 市占約70%，但這是較廣義的AI GPU CCL分母，不能直接作為OAM/UBB份額的反證或替代值；凱基的供應商表亦沒有量化份額。
   來源：[受惠輝達 Rubin 世代 CCL 規格升級！外資點名台光電是唯一 M9 合格供應商](https://technews.tw/2025/09/04/ccl-rubin/)；定位：正文第122-124行
   來源：[台灣電子硬體產業：IT Hardware](https://www.kgi.com.hk/zh-cn/-/media/files/kgishk/research-reports/tw-reports/it-hardware-07072025e.pdf)；定位：第8頁圖19，PDF行581-593
4. `SUPPORTED` — 台光電是 AWS Trainium 2/2.5 compute tray 的 M8 CCL 供應商。
   期間：2025年報告所描述的 Trainium 2/2.5 配置
   說明：凱基報告的供應商表將台光電列為 AWS Trainium 2/2.5 compute tray 的 M8 CCL 供應商；該列示本身不表示獨家。
   來源：[台灣電子硬體產業：IT Hardware](https://www.kgi.com.hk/zh-cn/-/media/files/kgishk/research-reports/tw-reports/it-hardware-07072025e.pdf)；定位：第8頁圖19，PDF行581-593
5. `UNKNOWN` — 台光電是 AWS Trainium 2 的 M8 等級高階材料獨家供應商。
   期間：Trainium 2；可查報告涵蓋2025年配置
   說明：有次級供應商表列出台光電，但未明示獨家，也未提供供應商完整性或份額。單一供應商被列出不能證明獨家。
   來源：[台灣電子硬體產業：IT Hardware](https://www.kgi.com.hk/zh-cn/-/media/files/kgishk/research-reports/tw-reports/it-hardware-07072025e.pdf)；定位：第8頁圖19，PDF行581-593
6. `CONTRADICTED` — 台光電是 AWS Trainium 3 的 M8 等級高階材料獨家供應商。
   期間：2026-02-02報告對預計量產的Trainium 3配置
   說明：富邦研究報告明確列出台光電及台燿同為 Trainium 3 M8 CCL 供應商，與「獨家供應」不符。該資料是券商報告的 Scribd 鏡像，來源層級與原始券商發布頁面不同，仍需以原始報告或公司披露進一步核驗。
   來源：[Fubon Research AWS Trainium 3 伺服器展望](https://www.scribd.com/document/1013677185/%E5%AF%8C%E9%82%A6-AWS-Trainium-3-%E4%BC%BA%E6%9C%8D%E5%99%A8%E5%B1%95%E6%9C%9B-20260202)；定位：正文第8頁，Scribd文本行364-372

## 判定

Overall `PARTIAL`。

建議改寫：已查資料僅支持：2023年次級報導曾稱台光電在NVIDIA伺服器OAM/UBB的CCL市占超過90%；該歷史說法不能外推至GB200/GB300。凱基2025年報告列出台光電為AWS Trainium 2/2.5 compute tray的M8 CCL供應商，但未證實獨家；富邦2026年2月報告則列出台光電與台燿同為Trainium 3的M8 CCL供應商。

來源限制：
- 未找到台光電或相關客戶公開、逐平台列出NVIDIA/AWS供應商及市場份額的官方披露。
- 市占率主張必須限定產品代際、板件類型、觀察期間與分母；來源對GB300的廣義AI GPU CCL市占估算不能替代OAM/UBB專屬份額。
- 凱基與富邦資料屬券商研究估列，不等同發行人或客戶確認；富邦報告本次可讀版本為Scribd鏡像。
- 2023年對NVIDIA OAM/UBB份額的報導未充分交代計算口徑，僅支持其當時曾被如此報導。

已找到可區分H100歷史市占、GB200/GB300供應商估列，以及Trainium 2與Trainium 3獨供狀態的資料；剩餘未決事項缺少相同產品範圍與分母的官方份額披露，故未以相鄰平台或較廣市場數據補足。

此紀錄來自獨立 Hermes 單筆重驗。只追加候選重驗結果，未修改原報告、作者決策或既有複核帳本。


追溯補正：僅復原與原結果完全吻合的 stdout、prompt 及各原子句來源定位。此補正未重新研究，原語意結論及原研究日期保持不變。
