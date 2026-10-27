# P2 年報事實抽取（Claude 子代理）

Repo 根目錄：`C:\Users\Neo Pegasus\Documents\ChatGPT\078-kaori sample\artifacts\stock-coverage-audit-20261003\incoming\latest-audit\My-TW-Coverage`。路徑請加引號；Python 一律用 `.venv/Scripts/python.exe -X utf8`。

## 必讀規則（全部遵守）
1. `research-site/prompts/extract-company-facts.md` 與 `research-site/schemas/company-facts.schema.json`
2. `research-site/ops/handoff-20261013/tools/extract_full_brief.md`：照它的流程走，但 helper 資料夾改用下面指定的位置。
3. `research-site/ops/handoff-20261013/tools/extract_rules_v2.md`
4. `research-site/ops/handoff-20261013/tools/codex_extract_task.md` 的「Hard rules」與「Depth requirement」兩節。其中「不能寫檔」那條不適用，你要寫檔。
5. `research-site/ops/handoff-20261013/tools/review_rules_v4.md`。審查員會用這份規則審你的結果，所以抽取時就要符合，尤其以下幾點：
   - 金額必須有幣別與單位，沒有就不要寫。
   - 陳述不能超出引文的意思。
   - 原文對數字有範圍限定（例如只限某條產線、某個子公司），陳述要保留。
   - 原文標示為關係人、關係企業或母公司的，陳述要寫明。
   - 不可把登記的營業項目寫成主要產品。
   - 表格沒有合計列，就不能寫「占合計」。
   - 年報內同一個數字前後不一致時，不要採用。
   - 名稱裡有可疑罕用字或簡體字（可能是 PDF 錯字）時，不要寫入。
   - 原文只有純數字的民國日期（例如 109.12、107/05/30）時，不要寫這個日期；也不要自行改寫成「民國109年12月」，因為機械查核會對不上原文。只用原文本身就以中文寫的年份（例如「114年度」「109年12月」）。

## 你的工作
- 只處理任務指定的那一家公司（代號＋簡稱）。
- 讀 `research-site/data/annual-slices/{ticker}.json`，只用來複製 `legal_name` 和 `source` 的五個欄位（citation_url、fy、filename、text_sha256、text_path），內容不可改動。
- 接著讀 `text_path` 指向的**完整年報文字**（頁碼標記為 `[PDF PAGE n]`），以營運概況章節為主。
- 寫出 `research-site/data/company-facts/{ticker}.json`：
  - 15 至 25 則 facts，id 從 `{ticker}-AR-01` 開始編號。
  - `company` 用任務給的簡稱。
  - 不要寫 `verification` 欄位。
- 若年報不是這家公司，就不要寫檔，回報原因。判斷依據：法定名稱、檔名中的代號、年報內文的自稱。年報封面是圖片時，關係企業或法人董事的名稱可能出現得比本公司多，不要被誤導。
- 若這家公司處於研發階段、尚未量產，照實寫，不要為了湊數硬抽。
- 寫檔前用 Python 自我檢查以下各點：
  - 每段 excerpt 都是年報文字的**逐字子字串**。要用程式從原文複製，不可去除空白、不可做正規化。
  - 第一段 excerpt 在 `page` 頁，其餘在 `page` 或 `page+1` 頁。
  - 每段 excerpt 至少 4 個字。
  - 陳述裡的每個數字都出現在 excerpt 中。
- 不要執行 `verify_extraction.py`，不要修改任何其他檔案，不要上網，也不要用既有知識補內容。
- helper 檔案只能放在 `research-site/ops/full-coverage-p2/work/{ticker}/`。

## 最後回覆（只寫一行，繁體中文）
格式為 `代號 簡稱 facts 數 ｜ 值得注意的一句話`，或 `代號 簡稱 跳過 ｜ 原因`。其他細節寫進 `research-site/ops/full-coverage-p2/work/{ticker}/notes.md`。
