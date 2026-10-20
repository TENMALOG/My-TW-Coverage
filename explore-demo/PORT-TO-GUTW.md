# 探索層移植到 股.tw：計畫（待董事長核准）

> 本文件只規劃，不修改 `075-Stock-surf-rewrite`。核准後才動 股.tw 的程式碼。

## 1. 兩邊現況

| | 探索層示範站（本 repo `explore-demo/`） | 股.tw（`075-Stock-surf-rewrite`） |
|---|---|---|
| 前端 | Astro 7 靜態頁 | React 19 + Vite 6，伺服器端渲染加預先產生頁面，Tailwind 4，React Query |
| 後端 | 無（純靜態） | Node（`backend/routes/*.js`），研究資料放在 `backend/data/` |
| 研究資料 | 本研究查核後的資料（31,606 條事實，產業已更正分類） | 原專案固定版本的 `research.json`，加上自建的查證層 |
| 圖表與動畫 | ECharts 6.1、Motion | 目前沒有 |

## 2. 原則
- **股.tw 是主站，研究網站（Quarto）是查證層**：探索層的每張卡片都可以連回研究網站的年報出處頁。研究網站建議放在 `research.股.tw`。
- **資料只走一條路**：本 repo 匯出「有版本號的資料集」（`dataset/`，附 manifest 和 SHA256），股.tw 只讀取這份資料集，不另外抄寫數字。
- **探索層是 React 元件**：重寫成 React，不把 Astro 搬進去，沿用 股.tw 現有的版面、品牌和 SEO 機制（`seo.tsx`）。

## 3. 工作拆解（每一步都可以單獨驗收）

| # | 工作 | 內容 | 驗收 |
|---|---|---|---|
| 1 | 資料集匯出 | 本 repo 新增 `export_dataset.py`：公司資料、摘要、名詞表、YouTube 代號、分享卡清單，附 manifest 和 SHA256 | 雜湊一致；1,733 家齊全 |
| 2 | 後端 API | `backend/routes/research.js`：`/api/research/:ticker`、`/api/research/summary`，從資料集載入記憶體 | 回傳內容和資料集逐欄位一致 |
| 3 | 公司卡片頁 | 把 `CompanyCard`（卡片牆、年報出處抽屜、觀察清單、分享）接進現有公司頁，**取代或並存** `ResearchPanels`（待決定） | 手機和桌面截圖；數字抽查 |
| 4 | 影片內嵌 | 點了才載入的 YouTube 元件（youtube-nocookie）＋封面圖 | 還沒上傳的公司顯示封面圖 |
| 5 | 分享卡 | 1,829 張分享圖放在靜態資源或 CDN，`seo.tsx` 輸出 og:image | 用分享預覽工具檢查 |
| 6 | 工具頁 | 比較、篩選、觀察清單、供應鏈地圖、產業故事，新增 5 條路由；ECharts 等點開或捲到時才載入 | 首頁的 JS 大小不增加；手機上不出現橫向捲動 |
| 7 | 名詞小卡 | `Term` 元件（瀏覽器內建的彈出視窗功能） | 鍵盤可以操作；通過 axe 無障礙檢查 |
| 8 | 搜尋 | 頁面預先產生後，再跑 Pagefind（中文斷詞）；或者擴充現有的 `SearchBox` | 「CoWoS」「電動機車」的搜尋結果和示範站相同 |
| 9 | 品質檢查 | 擴充 `scripts/verify-research.mjs`：畫面上的數字和資料集一致、公司身分一致、不出現自然人姓名 | 全部通過 |

## 4. 風險與對策
- **頁面變肥**：ECharts 約 1MB，一律等使用者點開或捲到時才載入，不放進首頁。
- **分享圖 89MB**：放 CDN 或物件儲存，不放進 repo。
- **舊研究面板**：`ResearchPanels` 用的是原專案的敘述（部分已列入勘誤表）。建議改用新的資料集，舊面板退場；這一點需要董事長決定。
- **授權**：沿用原專案 MIT 授權聲明（`My-TW-Coverage-LICENSE.txt` 已存在），並註明「股.tw 研究室」的查核與更正。

## 5. 需要董事長決定
1. 公司頁的舊研究面板要**取代**，還是和新卡片**並存**一段時間？（建議：取代）
2. 研究網站的網址：`research.股.tw` 可以嗎？
3. 核准後是否由 Codex 分工實作（每一步都由 Claude 審查後再交付）？
