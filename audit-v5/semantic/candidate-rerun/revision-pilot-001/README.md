# 修正句獨立複核與報告草稿

本批次從 1,491 筆修正提案（1,370 個父 claim）選取 30 筆，涵蓋 29 家公司。目的為獨立確認修正後的完整文字，並產生可檢視的報告修改草稿。評估基準日固定為 2026-10-08。

2026-10-10 完成：30 筆均已複核，26 筆為 `REVISED_SUPPORTED`、4 筆為 `PARTIALLY_SUPPORTED`；通過句納入 25 份草稿。交付檢查無阻擋問題，7,361 個保護檔案無異動，財務段落逐 byte 一致。詳見 `delivery/review-summary.md` 與 `delivery/summary.json`。

使用者要求：後續工作中，五小時額度剩餘降至 15% 或以下時，開始撰寫交接計畫，供其他模型續接。本批次完成時剩餘 34%，尚未觸發此門檻。

## 審查與採用規則

- 六類問題各 5 筆：排名、市占與分母、客戶與歷史合作、供應商與獨家限定、沿革與組織變更、期間與數值口徑。
- 新修正句使用新 revision ID，保留父 claim、提案與模型輸出的 SHA256 綁定。
- 每一筆使用獨立上下文。既有裁定與原子 claim 狀態不作為本次判決證據。
- `CANDIDATE_REVISED_SUPPORTED` 只是模型候選票。原始來源、引文、日期、實體、限定語與預定段落都通過來源複核，才能交付為 `REVISED_SUPPORTED`。
- 模型 JSON 延用舊欄位 `original_text` 與 `complete_original_supported`；在本執行它們只指新修正句。模型輸出的 `ACCEPTED` 也只指新句的模型票。
- 通過新句不改變父 claim 的裁定。前一階段 28 筆原文最終 ACCEPTED 維持獨立。
- 原始報告不寫入，另存草稿與差異檔；財務概況從標題至檔案結尾逐 byte 保留。
- 通過的歷史或來源歸屬句放入中性的「業務與歷史資料」段落，避免「主要客戶」等舊標題擴大含義。其餘原報告內容保留，但不代表本批次已驗證整篇。
- `PARTIALLY_SUPPORTED`、`PERIOD_UNRESOLVED`、`UNKNOWN_AFTER_RESEARCH`、`UNSUPPORTED` 都是有效研究結果。不將缺乏證據推成反證；模型另寫的替代句須以新 ID 再作獨立審查。
- 額度不足、登入錯誤、抓取失敗等保留操作紀錄，不能直接改判成事實 UNKNOWN。
- PDF 字型編碼錯誤時，可另存頁面 OCR 補充資料。原 PDF 與既有擷取文字保留；辨識影像、觀測座標、信心、執行程式及組列程式均綁定 SHA256。OCR 不作手動改字，相關表格仍須視讀核對。

## 檔案

| 檔案 | 用途 |
|---|---|
| `inventory.jsonl` | 凍結的全量提案盤點、父 claim、版本、優先級、來源線索與原報告位置 |
| `inventory.summary.json` | 全量盤點數量與選樣分布 |
| `queue.jsonl`、`queue.manifest.json` | 凍結的 30 筆獨立複核佇列與來源雜湊 |
| `checkpoint.json` | 模型處理進度，候選票尚未等於來源通過 |
| `adjudication/results.jsonl` | 只追加的獨立模型結果；同 ID 以最新筆為準 |
| `adjudication/primary-source-review.jsonl` | 綁定當次輸出 hash 與預定段落的來源複核 |
| `adjudication/operational-failures.jsonl` | 執行問題，不是事實判決 |
| `delivery/summary.json` | 經來源與產物完整性檢查的最新交付狀態 |
| `delivery/review-summary.md` | 逐筆結果、保留問題、草稿及差異檔連結 |
| `delivery/accepted-revisions.jsonl` | 真正通過的修正句及完整證據 |
| `delivery/pilot-outcomes.jsonl` | 30 筆結果，包括未完成與不通過 |
| `delivery/change-register.jsonl` | 原句、新句、限定語改動、來源與輸出 hash |
| `delivery/remaining-issues.json` | 尚須處理的問題 |
| `delivery/draft-manifest.json` | 草稿及差異檔雜湊、財務段落保留紀錄 |
| `report-drafts/` | 完整報告副本，僅通過修正句已替換 |
| `report-diffs/` | 原報告對草稿的逐行差異 |

## 範圍與完成條件

目前工作範圍為這 30 筆試批次。其餘全量提案仍是待驗證版本，不自動採用。以 `delivery/summary.json` 的 `complete` 為準：30 筆均有可追溯判決、通過修正句均具來源複核與草稿、無完整性問題，才算本批次完成。

源文件與原報告並未因這份草稿更新。任何報告整體發布或正式覆寫仍需另外處理。

## 操作紀錄

由田 113 年度年報的內嵌字型使文字擷取出現亂碼。來源補充位於 `audit-v5/source-cache/candidate-rerun/adjudication/ocr-sources/`，內容限於 PDF 第 50 頁；模型原始輸出、修正句與原裁決均未改寫。此頁與 114 年度對照表已另作視讀核對。

宏碁遊戲年報的 2024 年產品金額與同表印刷百分比不一致。本批次只採用明示依金額重算的修正句，營收總額另由證交所資料核對。原檔名及原標題已有公司名稱亂碼，索引以代號 6908 識別；不因此更換原檔。
