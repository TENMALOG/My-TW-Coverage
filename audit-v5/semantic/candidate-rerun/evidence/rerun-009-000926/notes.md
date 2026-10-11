# 重驗筆記 — 智易 / 3596:material_named_relationship:b62201e689d59f0c

原始 claim：5G FWA 設備已成功打入 [[T-Mobile]] (美國) 成為核心供應商，歐洲則供貨予 [[Vodafone]]、[[Deutsche Telekom]] 等一線電信商。

## 原子主張

1. `SUPPORTED` — 智易的5G FWA設備已進入美國T-Mobile的產品組合，存在供貨關係。
   期間：至少自2022年起；FCC資料列出2026年適用的相關設備
   說明：T-Mobile於2022年開始銷售Arcadyan FWA設備；T-Mobile支援頁列有Arcadyan KVD21，FCC文件亦將Arcadyan路由器列為T-Mobile 5G FWA寬頻設備。這支持供貨／產品組合關係，不代表供貨份額或供應商排名。
   來源：[Supply concerns ease as T-Mobile adds Arcadyan to FWA lineup](https://www.lightreading.com/5g/supply-concerns-ease-as-t-mobile-adds-arcadyan-to-fwa-lineup)；定位：正文及T-Mobile引述
   來源：[T-Mobile Internet Gateway Setup](https://www.t-mobile.com/support/home-internet/t-mobile-gateway)；定位：Gateway Support列表
   來源：[Federal Communications Commission, DA 26-875](https://docs.fcc.gov/public/attachments/DA-26-875A1.pdf)；定位：設備範圍表；Arcadyan routers for T-Mobile 5G FWA broadband devices
2. `UNKNOWN` — 智易已成為T-Mobile（美國）的核心供應商。
   期間：原 claim 未界定期間；現有資料涵蓋2022年及2026年設備
   說明：資料能確認Arcadyan是T-Mobile FWA設備供應商之一，但沒有供貨份額、採購量、排名或「核心供應商」的明確界定。T-Mobile 2022年資料還提到Nokia亦供應設備，但這本身不足以否定Arcadyan可能具有重要地位。
   來源：[Supply concerns ease as T-Mobile adds Arcadyan to FWA lineup](https://www.lightreading.com/5g/supply-concerns-ease-as-t-mobile-adds-arcadyan-to-fwa-lineup)；定位：正文及T-Mobile引述
3. `SUPPORTED` — 智易曾向歐洲Vodafone供貨。
   期間：歷史供貨；安全公告記錄Vodafone Germany EasyBox 802/803，未證明目前仍持續供貨
   說明：SEC Consult公告稱相關EasyBox DSL閘道由Arcadyan/Astoria Networks製造並由Vodafone Germany貼牌。這支持歷史供貨關係，但不能據此推定目前仍有供貨或涉及5G FWA設備。
   來源：[SEC Consult SA-20130805-0: Vodafone EasyBox Default WPS PIN Algorithm Weakness](https://seclists.org/bugtraq/2013/Aug/25)；定位：Vendor/product description
4. `SUPPORTED` — 智易向Deutsche Telekom供貨。
   期間：自2018年至智易2023年永續報告所述期間
   說明：智易官方永續報告稱，自2018年起，售予Deutsche Telekom的每個產品型號均申請相關環保標章並接受能效測試。報告支持該期間的產品銷售關係，但不證明2023年報告期後的持續供貨。
   來源：[Arcadyan 2023 Sustainability Report](https://csr.arcadyan.com/media/resources/reports/2023_Arcadyan_SUSTAINABILITY_REPORT_EN.pdf)；定位：Section 3.4.2, TÜV Green Product Mark
5. `UNKNOWN` — 智易亦向其他歐洲一線電信商供貨。
   期間：原 claim 未界定期間；未能確認其他歐洲營運商的具體名單及供貨期間
   說明：已核實的資料支持Vodafone的歷史產品案例及Deutsche Telekom在報告所述期間的產品銷售，但不足以確認「其他」歐洲一線電信商的具體客戶、供貨範圍或當前關係。

## 判定

Overall `PARTIAL`。

建議改寫：可核實資料顯示，智易曾向美國T-Mobile供應5G FWA閘道設備；但現有公開證據未能確認其為T-Mobile核心供應商。歐洲方面，資料支持智易歷史上為Vodafone Germany供應EasyBox設備，且智易2023年永續報告記載自2018年起有產品售予Deutsche Telekom；目前供貨是否持續及其他歐洲電信商的具體供貨關係尚未核實。

來源限制：
- 「核心供應商」缺少份額、排名、採購量或明確定義，不能由列入供應商組合推定。
- Vodafone證據是歷史EasyBox產品，不能替代目前供貨或5G FWA供貨的證據。
- Deutsche Telekom證據截止於智易2023年永續報告所述期間；未據此推定2026年仍持續供貨。
- 「其他一線電信商」未具體列名，現有來源不足以確認該概括性主張。

已檢索T-Mobile官方支援資料、FCC文件、智易官方永續報告及相關次級資料。資料足以確認部分供貨關係，但未找到能證明T-Mobile核心供應商地位、Vodafone目前供貨或其他歐洲客戶具體名單與期間的可靠證據；未解決原子維持UNKNOWN。

此紀錄來自獨立 Hermes 單筆重驗。只追加候選重驗結果，未修改原報告、作者決策或既有複核帳本。


追溯補正：僅復原與原結果完全吻合的 stdout、prompt 及各原子句來源定位。此補正未重新研究，原語意結論及原研究日期保持不變。
