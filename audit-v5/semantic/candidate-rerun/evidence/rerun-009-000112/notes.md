# 重驗筆記 — 華票 / 2820:objective_ranking_or_market_share:4ea2d7d9b3fa5942

原始 claim：最大股東為[[王道銀行]] (持股約 28%)，第二大股東為[[寶佳集團]] (持股約 17%)。

## 原子主張

1. `SUPPORTED` — 王道銀行是華票最大股東。
   期間：截至2026-03-24的年報資料
   說明：華票2025年年報的董事持股資料列出王道銀行代表持有約28.36%；二手資料按該年報資料將王道銀行列為最大股東。原 claim 未標期間，因此此處限定為所查得的最新資料基準日。
   來源：[CHINA BILLS FINANCE CORPORATION 2025 ANNUAL REPORT](https://doc.twse.com.tw/pdf/2025_2820_20260612FE4_20260930_112600.pdf)；定位：Corporate Governance Report, director shareholding table; O-Bank representative: 380,982 thousand shares, 28.36%
   來源：[華票(2820)股價與合理價：可以買嗎？1 個量化訊號觸發中](https://finlab.finance/stocks/2820)；定位：公司資料及主要股東摘要
2. `SUPPORTED` — 王道銀行持股約28%。
   期間：截至2026-03-24的年報資料
   說明：官方年報摘錄列示28.36%，符合「約28%」。分母為華票已發行股份；單位為持股百分比。
   來源：[CHINA BILLS FINANCE CORPORATION 2025 ANNUAL REPORT](https://doc.twse.com.tw/pdf/2025_2820_20260612FE4_20260930_112600.pdf)；定位：Corporate Governance Report, director shareholding table; O-Bank representative: 380,982 thousand shares, 28.36%
3. `SUPPORTED` — 寶佳系股東為華票第二大股東。
   期間：截至2026-03-24的年報資料
   說明：二手資料將寶佳資產管理列為第二大單一法人股東。此處的支持僅適用於該法律實體／單一股東口徑；不能直接等同於寶佳關係企業合計持股排名。
   來源：[華票(2820)股價與合理價：可以買嗎？1 個量化訊號觸發中](https://finlab.finance/stocks/2820)；定位：公司資料及主要股東摘要
   來源：[開年震撼彈！寶佳近10年首度減碼華票 申讓3萬張套現估逾5億](https://tw.stock.yahoo.com/news/%E9%96%8B%E5%B9%B4%E9%9C%87%E6%92%BC%E5%BD%88-%E5%AF%B6%E4%BD%B3%E8%BF%9110%E5%B9%B4%E9%A6%96%E5%BA%A6%E6%B8%9B%E7%A2%BC%E8%8F%AF%E7%A5%A8-%E7%94%B3%E8%AE%933%E8%90%AC%E5%BC%B5%E5%A5%97%E7%8F%BE%E4%BC%B0%E9%80%BE5%E5%84%84-142700427.html)；定位：Article text on Baojia Asset Management and aggregate Baojia-related holdings
4. `UNKNOWN` — 寶佳集團持股約17%。
   期間：原 claim 未指定；可查資料涉及2026年初及截至2026-03-24
   說明：約17%可對應寶佳資產管理這一單一法人股東的持股（二手資料報為16.66%至16.99%）；但同一資料亦稱寶佳系多家公司合計持股逾兩成。未能確認 claim 中「寶佳集團」指單一法人還是關係企業合計，故不能把單一法人比例當作集團合計比例。
   來源：[華票(2820)股價與合理價：可以買嗎？1 個量化訊號觸發中](https://finlab.finance/stocks/2820)；定位：公司資料及主要股東摘要
   來源：[開年震撼彈！寶佳近10年首度減碼華票 申讓3萬張套現估逾5億](https://tw.stock.yahoo.com/news/%E9%96%8B%E5%B9%B4%E9%9C%87%E6%92%BC%E5%BD%88-%E5%AF%B6%E4%BD%B3%E8%BF%9110%E5%B9%B4%E9%A6%96%E5%BA%A6%E6%B8%9B%E7%A2%BC%E8%8F%AF%E7%A5%A8-%E7%94%B3%E8%AE%933%E8%90%AC%E5%BC%B5%E5%A5%97%E7%8F%BE%E4%BC%B0%E9%80%BE5%E5%84%84-142700427.html)；定位：Article text on Baojia Asset Management and aggregate Baojia-related holdings

## 判定

Overall `PARTIAL`。

建議改寫：截至2026-03-24，王道銀行為華票最大單一股東，持股28.36%；寶佳資產管理為第二大單一法人股東，持股16.66%。寶佳關係企業合計持股口徑不同，不能直接表述為約17%。

來源限制：
- 原 claim 未提供持股資料基準日；此 re-verification 以所查得的2025年報資料基準日2026-03-24為參照。
- 官方年報摘錄核實了王道銀行28.36%的持股，但擷取內容未呈現完整主要股東排名表；寶佳的排名與比例主要依二手年報整理。
- 「寶佳集團」可能指單一寶佳資產管理法人，也可能指多家關係企業合計；兩者持股口徑不同。

已達可用研究／工具回合上限；寶佳集團與單一法人持股口徑未能以完整官方股東排名表確認，該原子主張維持UNKNOWN。

此紀錄來自獨立 Hermes 單筆重驗。只追加候選重驗結果，未修改原報告、作者決策或既有複核帳本。


追溯補正：僅復原與原結果完全吻合的 stdout、prompt 及各原子句來源定位。此補正未重新研究，原語意結論及原研究日期保持不變。
