# 年報切片與事實驗證工具

在 repo 根目錄執行，Python 用 `.venv/Scripts/python.exe -X utf8`。只用標準函式庫，不連網，不修改年報快取。

## 流程

1. `slice_annual.py`：讀 `audit-v5/source-cache/research-site/mops-annual/*_F04.json`（status = captured，同一檔股票取最新 fy），把年報文字切成十個章節，輸出 `research-site/data/annual-slices/{ticker}.json`。
   ```
   python research-site/scripts/annual/slice_annual.py [--tickers 2208 1582 ...]
   ```
   結束時印出報告數、亂碼（garbled）數與各章節的命中率（heading / keyword / missing）。
2. 把切片連同 `research-site/prompts/extract-company-facts.md` 交給 LLM 抽取，結果存成 `research-site/data/company-facts/{ticker}.json`（格式見 `research-site/schemas/company-facts.schema.json`，不含 `verification`）。
3. `verify_extraction.py`：驗證 schema，逐則 fact 檢查並只寫回 `verification`。
   ```
   python research-site/scripts/annual/verify_extraction.py [--tickers 2208 ...]
   ```
   檢查項目：`source_hash`（快照雜湊）、`excerpt_found`（引文逐字存在）、`page_match`（引文在標示頁，可延續到下一頁）、`numbers_supported`（陳述數字出現在引文；民國年與西元年互換視為相同）、`identity`（法定名稱出現在前 3 頁、檔名股票代號相符）。全部通過才是 PASS。

## 切片規則重點

- 比對時用 NFKC 並移除所有空白（pypdf 會在中文字之間插入空白）；輸出的 `text` 是原文。
- 目錄頁（有點線頁碼的行）不當作章節標題。
- `heading`＝短行（無逗號、句號）且以關鍵字開頭；`keyword`＝內文行含關鍵字。`confidence` 會標明。
- 營運概況章節（`肆、營運概況`）之後才搜尋營運類章節，避免抓到公司治理或永續章節裡的字句。
- 文字層亂碼（中文字比例 < 0.15 或大量私有區字元）者 `garbled: true`、`sections: []`。

## 測試

```
python -X utf8 -m unittest research-site/scripts/annual/test_annual.py
```

## 已知限制

- 新版年報（約 2022 年後）多半已不含「公司簡介／沿革」與「生產量值」章節，`company_profile`、`production_sales` 缺漏屬正常。
- 封面是圖片的年報，`legal_name` 改用全文最常出現的「XX股份有限公司」推得，`identity` 檢查（前 3 頁）會因此 FAIL，需人工確認。
- 表格被攤平成文字，欄位對應需靠 LLM 與人工複核。
