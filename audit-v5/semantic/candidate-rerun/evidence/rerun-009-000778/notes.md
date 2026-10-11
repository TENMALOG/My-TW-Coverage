# 重驗筆記 — 是方 / 6561:objective_ranking_or_market_share:06e71ebe14750575

原始 claim：「是方」在台灣雲端基礎建設中極具戰略地位，不僅是全台最大的海纜交換中心，更是各大國際公有雲(AWS、Azure、GCP、Oracle等)落地台灣的關鍵直連節點(Direct Connect)。

## 原子主張

1. `UNKNOWN` — 是方在台灣雲端基礎建設中「極具戰略地位」。
   期間：未明確；原文未指定評估期間。
   說明：是方公開資料描述其雲端與網路服務，但「極具戰略地位」沒有明確的評估標準或市場分母，現有資料不足以驗證此評價。
   來源：[Chief Cloud eXchange (CCX) Center](https://en.chief.com.tw/exchange-center/)；定位：服務簡介及服務特色
   來源：[Chief builds the 1st Taiwan Network eXchange Gateway to meet the digital transformation and cybersecurity needs of businesses](https://en.chief.com.tw/blog/ccx-202306)；定位：TPCX、TPIX與台灣網路服務描述
2. `UNKNOWN` — 是方的TPCX是全台最大的海纜交換中心。
   期間：原文未指定排名期間。
   說明：公司資料證實TPCX匯集多條海纜，並稱其為東亞主要海纜閘口、少數可由單一閘口介接多家海纜業者的機房之一；未找到可證明「全台最大」的排名。原文也未定義最大是按海纜數、容量、流量、業者數或其他分母衡量。
   來源：[台北海纜交換中心](https://www.chief.com.tw/exchange-center/tpcx/)；定位：服務簡介、服務特色
   來源：[Chief Company Introduction, 2025 Q1](https://en.chief.com.tw/wp-content/uploads/2025/05/Investor-conference-2025Q1.pdf)；定位：第5.1節 Taipei Cable Exchange Center (TPCX)
3. `SUPPORTED` — 是方CCX提供連接AWS、Azure、GCP及Oracle Cloud的直接或私有雲端連線。
   期間：公司公告涵蓋2018至2021年；CCX服務頁目前未標示發布日期。
   說明：是方公告分別證實AWS Direct Connect、Azure ExpressRoute、Google Cloud Interconnect及Oracle FastConnect的服務或連線方案。這支持連線服務存在，不等同證明是方對各公有雲具有「關鍵」或「最大」地位；Oracle連線公告描述經CCX及其全球網路節點提供服務，未證明Oracle在台灣設有落地節點。
   來源：[AWS Direct Connect Now Available in Chief Telecom’s Taipei Data Center](https://en.chief.com.tw/news/aws-direct-connect-now-available-in-chief-telecoms-taipei-data-center)；定位：公告首段
   來源：[Chief Cloud eXchange (CCX) provides Azure ExpressRoute connectivity service in Taipei Now](https://en.chief.com.tw/news/chief-cloud-exchange-ccx-provides-azure-expressroute-connectivity-service-in-taipei-now/)；定位：公告首段及第二段
   來源：[Google Cloud Interconnect (GCI) Now Available in Chief Telecom’s Data Center](https://en.chief.com.tw/news/google-cloud-interconnect-gci-now-available-in-chief-telecoms-data-center)；定位：公告首段
   來源：[Chief Telecom expand map of cloud services with Oracle FastConnect launch](https://en.chief.com.tw/news/chief-telecom-expand-map-of-cloud-services-with-oracle-fastconnect-launch)；定位：公告內Oracle FastConnect服務說明
4. `UNKNOWN` — 是方是AWS、Azure、GCP、Oracle等國際公有雲落地台灣的「關鍵直連節點」。
   期間：原文未指定期間。
   說明：官方公告支持部分雲端服務在是方台北機房有連線點，並支持CCX提供列名雲端的私有連線；但「關鍵」沒有判定標準，且沒有證據證明所有列名業者均透過是方在台落地。尤其Oracle來源只確認FastConnect透過CCX及全球節點提供，未確認台灣落地點。
   來源：[AWS Direct Connect Now Available in Chief Telecom’s Taipei Data Center](https://en.chief.com.tw/news/aws-direct-connect-now-available-in-chief-telecoms-taipei-data-center)；定位：公告首段
   來源：[Chief Cloud eXchange (CCX) provides Azure ExpressRoute connectivity service in Taipei Now](https://en.chief.com.tw/news/chief-cloud-exchange-ccx-provides-azure-expressroute-connectivity-service-in-taipei-now/)；定位：公告首段及第二段
   來源：[Google Cloud Interconnect (GCI) Now Available in Chief Telecom’s Data Center](https://en.chief.com.tw/news/google-cloud-interconnect-gci-now-available-in-chief-telecoms-data-center)；定位：公告首段
   來源：[Chief Telecom expand map of cloud services with Oracle FastConnect launch](https://en.chief.com.tw/news/chief-telecom-expand-map-of-cloud-services-with-oracle-fastconnect-launch)；定位：公告內Oracle FastConnect服務說明

## 判定

Overall `PARTIAL`。

建議改寫：是方公開資料顯示，TPCX匯集多條區域與國際海纜，CCX則提供AWS Direct Connect、Azure ExpressRoute、Google Cloud Interconnect及Oracle FastConnect等私有連線服務；現有證據不足以證明TPCX為全台最大海纜交換中心，或是方為所有上述公有雲在台落地的關鍵節點。

來源限制：
- 關於TPCX規模及是方市場地位的主要資料來自公司自述，未找到採用明確、可比較分母的獨立排名。
- 雲端連線公告證明服務或特定連線位置曾經提供，不足以證明目前市場排名或所有雲端業者均在是方落地。
- 「極具戰略地位」、「最大」及「關鍵節點」均缺乏原文定義的衡量期間、標準或市場分母。

已查閱是方官方TPCX與CCX資料、投資人簡報及各雲端連線公告；連線服務可確認，但未找到可驗證「全台最大」或「關鍵落地節點」的比較證據，未決原子保留UNKNOWN。

此紀錄來自獨立 Hermes 單筆重驗。只追加候選重驗結果，未修改原報告、作者決策或既有複核帳本。


追溯補正：僅復原與原結果完全吻合的 stdout、prompt 及各原子句來源定位。此補正未重新研究，原語意結論及原研究日期保持不變。
