# 重驗筆記 — 勁豐 / 6577:material_named_relationship:f31c724d57d9cdc3

原始 claim：業務結構與動能：(1) 醫療照護 — 病床邊照護系統 (Bedside Terminal)、手術室顯示器等醫療級觸控顯示裝置，通過歐美醫療認證 (如 [[UL]]、IEC 60601)，供應歐美醫療設備整合商；

## 原子主張

1. `UNKNOWN` — 勁豐醫療照護產品包括病床邊照護系統（Bedside Terminal）。
   期間：未指定
   說明：查得的公司資料確認其提供醫療用觸控顯示器及醫院用觸控顯示控制器，但未確認 Bedside Terminal 這一特定產品或應用。
   來源：[醫院用觸控顯示控制器](https://www.promate.com/cht/modern-touchscreen-console-hospitals/)；定位：系統需求、應用環境
   來源：[2024 勁豐電子永續報告書](https://www.promate.com/wp-content/uploads/2024-Promate-PSC-ESG-Report-C.pdf)；定位：公司概況、主要產品
2. `UNKNOWN` — 勁豐醫療照護產品包括手術室顯示器。
   期間：未指定
   說明：查得資料支持公司有醫療顯示產品及超音波顯示器相關方案，但未確認手術室顯示器是勁豐的產品；未以其他公司的手術顯示器資料代替證據。
   來源：[關於勁豐](https://www.promate.com/cht/about-psc/)；定位：勁豐簡介
   來源：[醫療顯示器應用－機構設計最佳化](https://www.promate.com/cht/mechanical-optimization-medical-ultrasound-monitor/)；定位：專案需求、解決方案
3. `SUPPORTED` — 勁豐從事醫療用觸控顯示裝置業務。
   期間：公司現行產品資訊及FY2024揭露
   說明：公司介紹及永續報告將醫療用觸控顯示器列為主要產品；公司案例另描述醫院用觸控顯示控制器。
   來源：[關於勁豐](https://www.promate.com/cht/about-psc/)；定位：勁豐簡介
   來源：[2024 勁豐電子永續報告書](https://www.promate.com/wp-content/uploads/2024-Promate-PSC-ESG-Report-C.pdf)；定位：公司概況、主要產品
4. `UNKNOWN` — 勁豐相關醫療產品已取得 UL 醫療安全認證。
   期間：未指定
   說明：公司醫院控制器案例提到產品設計與製造需符合 UL 安全標準，這是需求描述，不能證明特定產品已取得 UL 認證。公司列出的 ISO 13485 是醫療器材品質管理系統認證，不能替代產品認證證據。
   來源：[醫院用觸控顯示控制器](https://www.promate.com/cht/modern-touchscreen-console-hospitals/)；定位：系統需求、應用環境
   來源：[供應商管理政策](https://www.promate.com/cht/supplychain-management/)；定位：國際認證證書
5. `UNKNOWN` — 勁豐相關醫療產品已通過 IEC 60601 認證或測試。
   期間：未指定
   說明：本次查得的勁豐官方資料未確認特定產品已取得 IEC 60601 認證或通過相關測試；不以一般醫療業務或 ISO 13485 系統認證推定產品符合 IEC 60601。
   來源：[供應商管理政策](https://www.promate.com/cht/supplychain-management/)；定位：國際認證證書
   來源：[醫院用觸控顯示控制器](https://www.promate.com/cht/modern-touchscreen-console-hospitals/)；定位：系統需求、應用環境
6. `UNKNOWN` — 勁豐供應歐美醫療設備系統整合商。
   期間：未指定
   說明：公司公開資料提到歐美品牌客戶及與歐美知名大廠長期合作，但未確認這些關係屬於醫療設備業務，也未確認客戶是系統整合商。一般客戶關係或營運地區不能替代這項具體供應關係。
   來源：[豐藝電子與勁豐電子正式通過 ISO 50001 能源管理系統國際驗證](https://www.promate.com/cht/news-20251205/)；定位：關於豐藝電子與勁豐電子；勁豐電子段落
   來源：[2024 年度勁豐電子 TCFD 氣候相關財務揭露報告書](https://www.promate.com/wp-content/uploads/2024-Promate-Solutions-TCFD-report.pdf)；定位：客戶要求相關揭露

## 判定

Overall `PARTIAL`。

建議改寫：勁豐官方資料支持其從事醫療用觸控顯示器業務，並揭露醫院用觸控顯示控制器及超音波顯示器相關方案。查得資料尚不足以確認 Bedside Terminal、手術室顯示器、UL 或 IEC 60601 產品認證，以及供應歐美醫療設備系統整合商等具體說法。

來源限制：
- 醫療用觸控顯示器是公司產品線揭露；不能據此推定特定終端產品型號或臨床用途。
- 公司所列 ISO 13485 為品質管理系統認證，與特定產品取得 UL 或符合 IEC 60601 的證據不同。
- 歐美客戶或品牌合作的揭露未必指醫療業務，也未確認客戶屬系統整合商。

已完成4輪聚焦查找。官方資料足以支持一般醫療觸控顯示器業務，但產品細項、指定標準的產品認證及客戶類型仍缺乏可核實證據；未以近似資料填補，未解原子維持 UNKNOWN。

此紀錄來自獨立 Hermes 單筆重驗。只追加候選重驗結果，未修改原報告、作者決策或既有複核帳本。


追溯補正：僅復原與原結果完全吻合的 stdout、prompt 及各原子句來源定位。此補正未重新研究，原語意結論及原研究日期保持不變。
