# 重驗筆記 — 偉詮電 / 2436:objective_ranking_or_market_share:57909ce03d931541

原始 claim：偉詮電在 USB PD 控制器領域市佔率極高，廣泛應用於筆電、手機充電器及遊戲機適配器。

## 原子主張

1. `UNKNOWN` — 偉詮電在整體 USB PD 控制器市場的市佔率極高。
   期間：未指定
   說明：可查到筆電充電器供電端及 Nintendo Switch 相關應用的特定市佔數字，但原句未界定整體市場的產品範圍、地區、期間或市佔率分母，不能由局部應用市場推論整體 USB PD 控制器市場的市佔率。
   來源：[AI機櫃風扇用量放大，偉詮電高壓IC推升ASP](https://www.moneydj.com/kmdj/news/newsviewer.aspx?a=c7beefa5-eb7a-41f0-84c0-769b28e6ce12)；定位：USB PD 市佔段
2. `SUPPORTED` — 偉詮電 USB PD 控制 IC 在筆電充電器供電端市佔約六成。
   期間：2026年（報導公司2026年上半年狀況）
   說明：MoneyDJ 報導公司表示市佔約六成。範圍限於筆電充電器供電端；報導未說明市佔率按出貨量或營收計算，也未明確給出地理範圍。
   來源：[AI機櫃風扇用量放大，偉詮電高壓IC推升ASP](https://www.moneydj.com/kmdj/news/newsviewer.aspx?a=c7beefa5-eb7f-46dc-9fe5-31c49f2ad56e)；定位：文中「Nintendo Switch相關應用市占約七成」
3. `SUPPORTED` — 偉詮電 USB PD 控制 IC 在 Nintendo Switch 相關應用市佔約七成。
   期間：2026年（報導公司2026年上半年狀況）
   說明：MoneyDJ 報導公司表示 Nintendo Switch 相關應用市佔約七成。這是特定遊戲機應用，不代表整體遊戲機適配器或 USB PD 控制器市場；市佔計算分母未說明。
   來源：[AI機櫃風扇用量放大，偉詮電高壓IC推升ASP](https://www.moneydj.com/kmdj/news/newsviewer.aspx?a=c7beefa5-eb7f-46dc-9fe5-31c49f2ad56e)；定位：文中「Nintendo Switch相關應用市占約七成」
4. `SUPPORTED` — 偉詮電提供用於筆電相關應用的 USB PD 控制晶片。
   期間：公司現行產品／應用資料（頁面未標示期間）
   說明：公司應用頁列出筆記型電腦受電端 USB PD 控制晶片及 USB 充電器完整方案；這證實產品應用範圍，不證明市場普及程度。
   來源：[Weltrend | Applications — 桌上型和筆記型電腦](https://www.weltrend.com.tw/tw/applications/detail/pcs)；定位：詳細介紹
5. `SUPPORTED` — 偉詮電提供用於手機快充／手機充電器的 USB PD 控制晶片。
   期間：公司現行產品／應用資料（頁面未標示期間）
   說明：公司官方頁面說明手機供電端及受電端快充控制晶片，並列出充電器相關產品；這證實產品應用範圍，不證明市場普及程度。
   來源：[Weltrend | Applications — 手機（電源供應器）](https://www.weltrend.com.tw/tw/applications/detail/supplies-mobile-phones)；定位：詳細介紹及充電器相關產品
6. `SUPPORTED` — 偉詮電提供用於遊戲機 USB-C 充電器的控制晶片。
   期間：公司現行產品／應用資料（頁面未標示期間）
   說明：公司官方遊戲機應用頁明列 USB-C 充電器控制晶片；這證實產品應用範圍，不證明各類遊戲機適配器的市場普及程度。
   來源：[Weltrend | Applications — 遊戲機](https://www.weltrend.com.tw/tw/applications/detail/gaming)；定位：詳細介紹
7. `UNKNOWN` — 上述 USB PD 產品已在筆電、手機充電器及遊戲機適配器中「廣泛應用」。
   期間：未指定
   說明：公司產品及應用頁證明產品面向這些應用，但未提供各類終端的實際採用範圍、出貨分布或可驗證的普及程度，無法核實「廣泛」這一程度描述。
   來源：[Weltrend | USB PD控制器](https://www.weltrend.com.tw/tw/products/7cUfq2Rpd5)；定位：產品介紹
   來源：[Weltrend | Applications — 桌上型和筆記型電腦](https://www.weltrend.com.tw/tw/applications/detail/pcs)；定位：詳細介紹
   來源：[Weltrend | Applications — 遊戲機](https://www.weltrend.com.tw/tw/applications/detail/gaming)；定位：詳細介紹

## 判定

Overall `PARTIAL`。

建議改寫：MoneyDJ於2026年報導偉詮電表示，其USB PD控制IC在筆電充電器供電端市佔約六成、Nintendo Switch相關應用約七成；公司產品資料亦列有筆電、手機快充及遊戲機USB-C充電器等應用。這些特定應用資料不足以確定其在整體USB PD控制器市場的市佔，或證明上述終端的產品普及程度。

來源限制：
- 市佔率數字來自 MoneyDJ 對公司說法的報導，並非本次查得的監管文件或獨立市場統計。
- 報導中的筆電及 Nintendo Switch 市佔率各有特定應用範圍；市佔計算分母、地理範圍及衡量方式未明。
- 公司官網證實產品及應用範圍，但沒有量化實際採用廣度，不能單憑產品目錄證成「廣泛應用」。

已達本次工具迭代上限，停止檢索。已有特定應用市佔及官方產品應用資料；整體USB PD控制器市場市佔定義與「廣泛應用」的採用程度仍無法核實。

此紀錄來自獨立 Hermes 單筆重驗。只追加候選重驗結果，未修改原報告、作者決策或既有複核帳本。


追溯補正：僅復原與原結果完全吻合的 stdout、prompt 及各原子句來源定位。此補正未重新研究，原語意結論及原研究日期保持不變。
