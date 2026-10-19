# 任務：核對上市櫃公司的產業分類

原專案把 1,733 家公司分進 98 個產業，分類來自外部資料庫（Yahoo Finance 風格的英文產業別），從來沒有和年報核對過。已知一個錯誤：6536 碩豐的主要業務是 POS 軟硬體，卻被歸在「Gambling（博弈）」。你的工作是逐家判斷「目前的分類」和年報描述的實際業務是否相符。

## 輸入

- `in_K.jsonl`：每行一家公司，欄位如下：
  - `ticker`、`name`、`legal_name`
  - `current`、`current_zh`：目前的產業分類
  - `mops_industry`：公開資訊觀測站登記的官方產業別，較粗，只作參考
  - `facts`：已查核通過的年報事實，含業務範圍、產品、營收結構等
- `industries.csv`：98 個可選產業（英文 folder、中文名稱、目前公司數）

## 判斷規則

1. **以年報事實為準**：看主要業務和營收占比最大的部門。官方產業別只作輔助，因為它很粗，例如「其他電子業」。
2. **OK**：目前的分類能合理描述主要業務。不同分類都說得通時（例如「電子零組件」和「電子設備」），一律判 OK，不要為了更精確而改。
3. **MISMATCH**：目前的分類明顯錯誤，例如：
   - 主要業務根本不在這個產業（像碩豐被歸在博弈）。
   - 控股公司被歸到和旗下主要業務無關的產業。
   - 業務已經轉型，年報清楚寫著現在的主業是別的產業。

   這時要從 `industries.csv` 選一個最合適的 `suggested`。
4. **UNSURE**：事實太少，或業務橫跨多個產業，無法判斷時使用。
5. **不可上網，不可猜測**：只用 `facts` 和 `mops_industry` 判斷。

## 輸出

每家公司一行 JSON，寫到 `out_K.jsonl`（UTF-8），順序與輸入相同：

```json
{"ticker": "6536", "verdict": "MISMATCH", "current": "Gambling", "suggested": "Software - Application", "confidence": "high", "reason": "年報主要業務為POS軟硬體，軟體收入占52.32%，與博弈無關", "facts": ["6536-AR-02", "6536-AR-04"]}
{"ticker": "1101", "verdict": "OK"}
```

- OK 只需要寫 `ticker` 和 `verdict`。
- MISMATCH 和 UNSURE 必須附上 `reason`（繁體中文，40 字內）和引用的 `facts`。
- `confidence` 填 `high` 或 `medium`。只有 high 會被直接採用，medium 會再由人工複核。
- 不要修改任何其他檔案。
