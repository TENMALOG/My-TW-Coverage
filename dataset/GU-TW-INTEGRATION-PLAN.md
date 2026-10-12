# 股.tw 接入已驗證研究資料集：規劃書

日期：2026-10-12。規劃者：Claude（Opus）。狀態：規劃，尚未在 075 專案動工。

## 一、現況

| 項目 | 股.tw（`075-Stock-surf-rewrite`） | 本專案（My-TW-Coverage） |
|---|---|---|
| 架構 | Node.js 後端＋React SSR，無資料庫；研究資料為 `backend/data/*.json`，啟動時載入記憶體 | Python 腳本產生資料，Quarto 研究網站 |
| 研究來源 | Timeverse/My-TW-Coverage 固定版本 `396b8da`（2026-03-26）的 1,679 份 Markdown，只取三段，全部標示「第三方研究、未核實」 | 已逐條查核 1,394 條敘述；1,337 條已驗證敘述；年報事實擷取中 |
| 核實層 | `research-evidence.json`，目前 10 項；以 `blockId`＋區塊 SHA-256＋原文片段三者比對才套用 | 每條結果都有原文摘錄、來源快照雜湊與覆核依據 |
| 官方資料 | TWSE opendata：月營收、重大訊息、股利，**只有上市** | 公開資訊觀測站：綜合損益彙總（上市＋上櫃）、公司基本資料（上市＋上櫃） |

股.tw 已經採用的原則（固定版本、雜湊比對、代號＋全名雙重身分核對、不捏造關係圖、未知保持 null）與本研究一致，因此接入方式是「延伸它既有的機制」，不是重寫。

## 二、交付介面：`dataset/releases/{version}/`

版本號格式 `YYYY.MM.N`（例如 `2026.10.0`）。每個版本是一個不再修改的資料夾；更正一律發新版本。

| 檔案 | 每列一筆 | 主要欄位 |
|---|---|---|
| `manifest.json` | 整個版本 | `version`、`generated_at`、`assessment_date`、`source_commit`（本專案 commit）、`files: {name: {sha256, rows}}`、`schema_version`、授權聲明 |
| `companies.jsonl` | 公司 | `ticker`、`short_name`、`legal_name`（公開資訊觀測站登記）、`name_en`、`market`（上市／上櫃）、`industry`（英文分類＋中文名＋slug）、`established`、`address`、上市櫃日期、`source` |
| `facts.jsonl` | 年報事實（只放驗證 PASS） | `id`、`ticker`、`field`、`statement`、`period`、`attribution`（`annual_report` / `self_description` / `third_party`）、`source: {citation_url, fy, page, excerpts[], text_sha256}`、`verified_at` |
| `statements.jsonl` | 已驗證敘述 | `id`（claim_id）、`ticker`、`text`、`kind`（`original` / `revised`）、`period`、`claim_type`、`citations[]`（url、title、locator、excerpt、publication_date、inspection_method）、`audit: {batch, round}` |
| `audits.jsonl` | 1,394 條查核結果（含未通過） | `claim_id`、`ticker`、`original_text`、`outcome`、`adopted_text`、`gu_tw`（見第三節） |
| `financials.jsonl` | 公司×年度 | `ticker`、`year`、`table_kind`、`items_k`（原報表項目，仟元）、`gross_margin_pct`、`operating_margin_pct`、`source` |
| `entities.jsonl`、`mentions.jsonl` | 第二階段 | 統一名稱的產品／技術／公司實體，以及每次提及所在的事實或敘述 |
| `LICENSE-NOTICE.md` | — | MIT 原作者聲明與本資料集授權 |

原則：

- 只有通過驗證的內容會出現在 `facts`、`statements`；未通過的只出現在 `audits`，而且只帶結果與原文定位，不帶可被誤讀為事實的文字。
- 每個檔案的 SHA-256 記在 `manifest.json`；股.tw 匯入時逐一核對，不符就拒絕。
- 未知一律 `null`，不以版本日期冒充內容期間（與股.tw 現行規則相同）。

## 三、查核結果對應到股.tw 現有核實格式

股.tw 的 `claimsFor()` 只在 `sourceCommit`、區塊 SHA-256、原文片段三者都相符時才套用核實紀錄。本專案會在匯出時，直接用股.tw 的 `backend/data/research.json`（其中已有每家公司的區塊原文）預先比對，把每條查核結果算成股.tw 的格式：

```json
"gu_tw": {
  "source_commit": "396b8dada6c32347245ee5af6c246c17b347ed2a",
  "target": {"blockId": "2327:relationships:3", "sha256": "…", "quote": "…原文片段…"},
  "status": "corrected",
  "text": "…已驗證的修正說法…",
  "scope": "…適用範圍…",
  "period": "…",
  "reviewedAt": "2026-10-11",
  "verifiedAt": "2026-10-11",
  "officialSources": [{"label": "…", "url": "…", "publishedOn": null}]
}
```

| 本研究結果 | 股.tw `status` | `verifiedAt` |
|---|---|---|
| 原句最終通過 | `verified` | 裁定日 |
| 原句未通過、修正句通過 | `corrected`（原文保留，旁附修正） | 裁定日 |
| 兩輪仍部分支持 | `partial` | null |
| 不支持 | `not_supported` | null |
| 期間無法確定 | `needs_period` | null |
| 研究後仍未知、來源覆核未通過 | `unverified` | null |

比對不到股.tw 區塊的條目（原專案在 `396b8da` 之後改寫過的句子、被股.tw 排除的 56 份報告）會列在 `audits.jsonl` 的 `gu_tw: null` 並附原因，匯出報告列出數量，不以相似文字猜測。

`officialSources` 只放直接支持判定的來源；股.tw 現行規則「不能拿公司首頁當內容佐證」照樣適用。

## 四、股.tw 端的修改（分階段）

所有修改都在 075 專案另開分支／worktree 進行，不碰目前 `codex/research-evidence-and-search` 分支上未提交的變更。部署依 `DEPLOYMENT.md`，需董事長另行授權。

### 第一階段：匯入與核實擴充（效益最大）
1. 新增 `scripts/import-verified-dataset.mjs`：輸入固定版本資料夾，核對 `manifest.json` 雜湊，輸出 `backend/data/verified/`（依代號分組的 facts、statements、financials、companies）。與現有 `import-coverage.mjs` 並存。
2. 由 `audits.jsonl` 的 `gu_tw` 欄位產生 `research-evidence.json` 的新紀錄（保留現有 10 項人工紀錄，衝突時人工紀錄優先並列出差異）。現有 `claimsFor()` 不需修改即可套用。
3. 測試：雜湊不符拒絕匯入、`gu_tw` 目標失效時不套用、未知欄位保持 null、身分不符不套用。

### 第二階段：公司頁呈現已驗證內容
1. 後端新增 `lib/verified-research.js`，公司頁 payload 增加 `verified: {facts, statements, financials, basic}`。
2. 前端新增「已驗證資料」區塊，放在現有「第三方研究（未核實）」之前；每條附來源類型標籤（年報揭露／公司自述／第三方引述／已查證報導）、期間、出處連結與頁碼。
3. 財務摘要與基本資料涵蓋**上櫃公司**，補上現行官方資料只有上市的缺口。

### 第三階段：主題搜尋以已驗證內容為先
1. 匯入 `entities.jsonl`、`mentions.jsonl`。
2. `/explore` 結果分兩層：先列已驗證提及，再列原專案歷史快照（維持「未核實」標示）。
3. 實體名稱統一後，「搜尋 Apple 找供應商」只回傳有證據的關係，並附證據連結。

### 第四階段：例行更新
- 每年 5–6 月新年報公布後，本專案增量更新並發布新版本；股.tw 重新匯入固定新版本。
- 財務每季更新。版本之間附變更清單（新增、更正、撤回）。

## 五、本專案端待辦

1. 完成 1,733 家年報事實擷取與驗證（進行中，電子零組件先行）。
2. 撰寫 `dataset/scripts/export_dataset.py`：產生上述檔案與 manifest，並對股.tw `research.json` 預先比對 `gu_tw` 目標。
3. 撰寫 `dataset/scripts/validate_dataset.py`：結構、雜湊、身分、只含 PASS 的檢查。
4. 實體與提及資料（第三階段所需）。
5. 首個版本 `2026.10.0` 發布前，向董事長回報比對率與限制。

## 六、風險與處理

| 風險 | 處理 |
|---|---|
| 股.tw 固定的原專案版本與本專案查核時的報告文字不同，導致比對不到 | 只做精確片段比對；比對不到就列出，不猜。之後可評估股.tw 改固定到本專案版本 |
| 資料量增加影響記憶體 | 預估 facts＋statements 約 20–30 MB；可依代號分檔、延遲載入 |
| 已核實狀態被新匯入覆蓋 | 沿用股.tw 規則：雜湊或片段不符就不套用，不自動延續 |
| 授權 | 資料集附 MIT 原作者聲明；股.tw 已保存原授權副本 |
| 對外部署 | 本規劃不包含部署；部署前需董事長授權 |
