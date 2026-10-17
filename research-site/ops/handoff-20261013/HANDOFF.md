# 交接：2026-10-13 進度與下一步（下一次執行：星期六 2026-10-17）

目標：完整產業研究網站，最終取代原專案（1,733 家、98 產業），只用逐字核對過的年報事實。

## 已完成
| 項目 | 狀態 | 位置 |
|---|---|---|
| 年報事實 | 1,733 家、32,083 筆，全數通過 verify_extraction | `research-site/data/company-facts/` |
| 語意審查 | 17,208 筆已審，347 筆退回（不會呈現） | `company-facts/_semantic-review.jsonl` |
| 亂碼年報 | 14 家 PyMuPDF 重抽、11 家 Windows OCR（頁面影像保留） | `scripts/annual/reextract_pymupdf.py`、`ocr_annual.py`、`winocr.ps1` |
| 關係資料 | 7,935 筆；上市櫃間 684 筆經 Sonnet 逐筆審查 → 可公開 554 筆 | `data/relations/`、`scripts/relations/`（`build_relations.py` → `apply_edge_review.py` → `listed_edges.csv`） |
| 目錄名稱 | 修正 7 家亂碼簡稱（含 8349 恒耀） | `scripts/build_catalog.py` FILENAME_NAME_FIXES |
| 產業分析草稿 | 97 產業（航太為手寫章，不在內）由 Codex 撰寫，機械檢查全數通過 | `data/industry-analysis/{slug}.md`；檢查／產生：`scripts/generic/build_industry_analysis.py` |

已 commit（本機，未 push）：`5d2d7604`、`a412cf8e`。之後的變更（relations、industry-analysis、build_industry_analysis.py、build_catalog 修正、codex_quota CODEX_HOME 支援）尚未 commit。

## 產業分析（10/13 晚間完成）
- 97 份草稿經 Sonnet 逐句審查（12 組，結果在 `anarev_out/`），104 句依審查改寫（紀錄 `data/industry-analysis/_review-log.jsonl`，工具 `tools/apply_anarev.py`），
  再經 `build_industry_analysis.py` 檢查全數通過，已產生 `chapters/industries/_analysis/*.qmd`（97 份，含年報頁碼註腳）。

## 下一步（依序）
2. 用現有產生器重建全部頁面（目前頁面是年報事實補齊前產生的）：
   `scripts/generic/build_company_pages_all.py`、`build_industry_chapters.py`、`build_book_config.py`；
   公司頁加入 `listed_edges.csv` 的已審關係；各產業關係圖（參考 `scripts/build_relation_graph.py`）。
3. `quarto render research-site` + `scripts/check_site.py`；瀏覽器實測（桌面／375px）。
4. 本機 commit（需董事長同意的事項見下）。
5. 之後：未對到名單的具名對象清理（`data/relations/unresolved_named.csv`，品質差，目前不公開）；
   2412/2884/1589/4406 待 2025 年報（MOPS 尚無 F04）。

## 需董事長決定（push 前）
網站名稱與署名、部署平台與網域、舊入口處理、原報告封存方式、股.tw（075）匯入；push 前要加 MIT 署名
（Timeverse/My-TW-Coverage, "Copyright (c) 2026 idk_mostoftime"）、掃描機密、repo 改名。

## 分工與工具
- Codex 兩個帳號：預設 `~/.codex`、第二帳號 `CODEX_HOME=~/.codex-b`；額度：`audit-v5/semantic/candidate-rerun/codex_quota.py`（支援 CODEX_HOME）。
  Codex 寫檔只開放新資料夾；擷取任務要寫明 15–25 筆（`tools/codex_extract_task.md`）。
- Sonnet：擷取審查（`tools/review_brief.md` + `review_rules_v3.md`）、關係審查（`relrev_brief.md`）、分析審查（`anarev_brief.md`）。
- 修正工具：`fix_edit.py`（改寫陳述，數字不變）、`drop_facts.py`、`merge_review.py`、`select_review.py`，皆在 `tools/`。

## 待重新分類（董事長清單）
- 6536 碩豐：POS 系統業者，原專案歸在 Gambling（博弈）。
- 2406 國碩／3691 碩禾：主要供應商 E 公司、客戶 AD 公司的進銷貨金額完全相同但百分比不同，擷取可能有誤，需回年報查核。

## 2026-10-18 凌晨狀態（最新，以此為準）
- 頁面：公司頁加「與其他上市櫃公司的往來關係」（`scripts/generic/company_relations.py`），產業章加關係圖（`build_industry_relation_graphs.py` → `chapters/industries/_relations/`）；`_quarto.yml` 已改為完整版（1,841 頁）。
- 第二輪審查：未審 14,810 筆全數審完（Codex 49 工作＋Sonnet 124 工作，`ops/codex-review/`）；退回 286＋名次掃描 179 → 複核（`adj_out_*.jsonl`）→ `apply_second_pass.py` 已套用：修正 329、刪除 24。
- 關係：Sonnet 名稱比對新增 84 筆（`data/relations/name_matches.jsonl`）；可公開 638 筆。國碩／碩禾疑點已查清，無誤。
- QA 稽核：隨機 400 筆已通過事實，退回 34（8.5%，多為百分比未寫分母）→ 全面掃描 3,154 筆「百分比無分母」：
  - Sonnet 處理 `ops/bare-percent/jobs_sonnet/bp001-008`（輸出 `ops/bare-percent/out/`）；
  - Codex 佇列處理 `ops/bare-percent/jobs/bp009-025`（`codex_queue.py --jobs bare-percent/jobs --out bare-percent/out --task bare-percent/codex_task.md`，額度滿會自動睡到重置）。
  - 完成後：把 `ops/bare-percent/out/*.jsonl` 依 `apply_second_pass.py` 的 FIX/DROP/KEEP 邏輯套用（需複製該腳本改讀 bare-percent/out，batch 標籤另取），再重產頁面。
- 待複核：`ops/pending_adjudication.json`（32 筆，已暫標 REJECT）。
- 網站建置：背景執行中（失敗自動重試 3 次）；上次因檔案被占用（可能 pCloud 同步）中斷。建置完要跑 `scripts/check_site.py` 與瀏覽器實測；套用分母修正後需再重產頁面、重建。
- 額度管理：每輪 Claude 5 小時額度目標用到 95–99%（記憶 pace-claude-5h-quota）；分配 Claude:CodexA:CodexB ≈ 5:1:1。
