# 獨立複核帳本

作者帳本的 `decision` 是作者判定。1,399 筆原 `independent_review` 與 `final_state` 維持 null；獨立複核寫入 `reviewer-NNN.json`，不能以填回作者檔案的方式覆蓋歷史。

首批使用 `semantic-manual-independent-review-2`。這次是 Codex 的來源內容複核，與作者作業分離；已看過作者判定，因此不是盲審。沒有呼叫既有 `semantic_independent_review.py`：該程式只把作者證據摘要交給 API，不自行讀來源，也缺完整 hash、期間與頁碼 lineage。

每筆保留佇列原 claim 文本與 `claim_id + normalized_claim_hash`、作者批次／批次 SHA-256、作者現行判定與 amendment，以及 reviewer 判定、原子子句、來源頁碼與內容 hash、缺口類型、改寫提案。需要原文上下文時另記錄，不改固定 claim hash。

作者批次、manifest、文字診斷及檢視摘要的 hash 使用 UTF-8／LF 正規化，避免 Git 在 Windows 的 CRLF 轉換造成偽異動；作者現場原始位元組 hash 另保留為 `author_batch_observed_bytes_sha256`。PDF／HTML 來源 `source_sha256` 一律雜湊下載原始位元組，不做換行轉換。

- 作者與複核判定標籤一致：`final_state` 為該分類。`PARTIALLY_SUPPORTED` 仍不接受完整原句，也不自動接受任何改寫。
- 標籤不同：`final_state=ESCALATED_REVIEW_DISAGREEMENT`，保留兩者，由後續裁決處理。Reviewer 單方 `ACCEPTED` 不能算最終接受。
- 已複核的相同鍵不放入另一個基礎批次。後續更正須新增 amendment／裁決事件，引用前一紀錄的內容 hash；不可悄悄改掉已 commit 的判定或證據。
- `reviewer-amendments-NNN.json` 使用 `semantic-reviewer-component-amendment-1`，每批最多25個事件。僅允許子句、缺口及改寫提案的更正，不准變更原 decision／final_state／status。事件保存目標批次hash、唯一鍵、before／after、理由及新增定位／摘要hash。Validator驗證鏈結、前值與來源；讀取者須依事件順序覆加更正，不能只讀舊批次。更動實質判定的裁決流程仍待實作。
- 每批最多 25 claims。修改限 audit 分支；不改發行人原報告。`proposed_text` 保持提案，論文採用與 corpus repair 是後續可稽核步驟。

`reviewer-checkpoint.json` 按唯一鍵計數。「已複核」包含有分歧的項目，因此需同時查看 `adjudication_pending`；不能把進度當成已定案數。

`reviewer-evidence/reviewer-NNN/manifest.json` 保存 URL、來源類型、期間、PDF實體頁與印刷頁、原始內容 SHA-256 及檢視摘要。原始 PDF/HTML 與完整擷取文字在 ignored cache；目前 Git clone 不會包含它們。論文交付前須另打包來源原檔並核對 hash。首次取得時間不明的歷史快取明記 null，不沿用作者未核實日期。僅有網頁可讀摘錄而無原HTML時，`source_hash_scope` 明記為保存的UTF-8文字摘錄；不能以該hash宣稱驗證原網站HTML。

文字出現次數只涵蓋擷取文字層。`numeric-counterchecks.json` 是針對本批重要疑點的診斷，沒有宣稱查完所有作者 rationale 數字。零次不是反證，Logo／圖表／翻譯／字串邊界須另檢視。

本機取得觀察另存每批 `reviewer-NNN-retrieval-observations.json`，作者ACCEPTED複核另有完整本機觀察索引 `accepted-review-retrieval-observations.json`，含未採用的失敗與回應。Cloud 的15筆 `local-recheck-queue.json` 原樣保留；HTTP 200或本機可取得都不是語意結論。沒有實作或執行既有提案中的本機 retrieval worker；本次為手動複核輔助擷取。

全部111筆作者ACCEPTED的複核總表在 `../INDEPENDENT-REVIEW-ACCEPTED.md`；`accepted-review-index.json` 是套用子句更正的衍生索引，並非新增判定帳本。只有21筆final ACCEPTED，仍須按來源範圍與期間引用；90筆分歧及改寫提案待裁決。

Windows 驗證命令（在 repository 根目錄）：

```powershell
.venv/Scripts/python.exe -X utf8 audit-v5/validate_reviewer_ledger.py
.venv/Scripts/python.exe -X utf8 audit-v5/validate_reviewer_ledger.py --check-local-sources
```

第一個命令驗證帳本唯一鍵、佇列及作者版本、null政策、分歧規則、來源摘要 hash 與 checkpoint。第二個再核對本機原檔 hash；離線 clone 缺原檔時應失敗，不應被誤報為語意內容有誤。
