# 第一版（示範版 0.1）交付審閱說明

日期：2026-10-11。資料截止：評估基準日 2026-10-08；年報與財務快照 2026-10-10。

## 交付內容

| 項目 | 位置 |
|---|---|
| 網站預覽 | 本機 `http://localhost:4321`（`.claude/launch.json` 的 `research-site`） |
| 網站原稿 | `research-site/`（Quarto 1.10.18；`quarto render research-site`） |
| PDF | `research-site/_site/tw-industry-research.pdf`（143 頁） |
| 研究資料 | `research-site/data/aerospace-defense/`：已驗證事實 43 條、2025 年度指標、合併財務、關係 26 條、引用對照、段落對照 |
| 參考文獻 | `research-site/references/aerospace-defense.json`（43 筆） |
| 新查核批次 | `audit-v5/semantic/candidate-rerun/revision-aero-001`、`revision-aero-002`、`company-research-aero-001` |
| 來源快照 | `audit-v5/source-cache/research-site/`（公開資訊觀測站年報與損益彙總） |

## 重建步驟

```bash
.venv/Scripts/python.exe -X utf8 research-site/scripts/build_aero_facts.py
.venv/Scripts/python.exe -X utf8 research-site/scripts/build_aero_metrics.py
.venv/Scripts/python.exe -X utf8 research-site/scripts/build_aero_financials.py
.venv/Scripts/python.exe -X utf8 research-site/scripts/build_company_pages.py
.venv/Scripts/python.exe -X utf8 research-site/scripts/build_relation_graph.py
.venv/Scripts/python.exe -X utf8 research-site/scripts/build_appendices.py
.venv/Scripts/python.exe -X utf8 research-site/scripts/build_company_index.py
.venv/Scripts/python.exe -X utf8 research-site/scripts/build_main_results.py
.venv/Scripts/python.exe -X utf8 research-site/scripts/build_bib.py
quarto render research-site
.venv/Scripts/python.exe -X utf8 research-site/scripts/check_site.py
```

## 品質檢查結果（check_site.py）

- **引用**：所有〔〕標記都對得到資料表，輸出的頁面裡沒有殘留未轉換的標記。
- **原文摘錄**：43 條事實的摘錄都能在來源快照中重新找到；公司身分核對全部通過。
- **連結**：21 頁的內部連結與錨點全部有效。
- **凍結檔案**：受保護檔案 7,361 個沒有異動，6 個凍結交付檔的雜湊不變。
- **數字**：正文中的數字全部追得到資料檔。
- **瀏覽器實測**：桌面版與手機版（375px）都沒有整頁橫向捲軸；全站搜尋「2645」可找到；索引頁的篩選功能正常。

## 需要董事長決定的事項

1. **網站名稱與署名**：目前是暫定的「臺灣上市櫃企業的產業定位與供應鏈關係」，署名「臺灣產業研究專案」。
2. **部署平台與網域**：例如 GitHub Pages、Netlify 或 Cloudflare Pages，以及是否使用自有網域。
3. **舊入口怎麼處理**：原專案的 README、WIKILINKS 與 network 頁面要改為指向新網站，還是保留並列。
4. **公開範圍**：第一版是否公開證據附錄中的「原報告敘述」原文。目前的做法是公開，並明確標示為「未經證實的查核對象」。
5. **是否 commit**：要不要把 `research-site/`、新增的腳本與新批次 commit 到 `audit-v5` 分支。目前都還沒 commit。

## 已知限制

- 中信造船的財務口徑待確認。
- Typst 書籍範本的頁首會顯示簡體的「章节」字樣，需要另外調整範本。
- PDF 版不含 1,733 家公司索引表和互動關係圖。
