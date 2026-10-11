# revision-aero-001 接手程序（Codex 額度不足時）

Codex 每週額度重置：2026-10-14 19:31（Asia/Taipei）。5 小時額度依最新 rollout 的 `rate_limits` 判斷。

## 判斷剩餘工作
```bash
cd audit-v5/semantic/candidate-rerun
../../../.venv/Scripts/python.exe -X utf8 run_revision_batch.py status --batch revision-aero-001   # PENDING = 尚無模型輸出
```
- `adjudication/results.jsonl`：已完成（同 ID 以最後一筆為準）。
- `adjudication/operational-failures.jsonl`：額度／逾時等操作失敗，不是事實 UNKNOWN。
- 中斷的 attempt 目錄保留，不刪除；在該目錄加 `aborted.json` 說明。
- 公司研究：`audit-v5/source-cache/candidate-rerun/company-research-aero-001/companies/<ticker>/attempt-*/final.json` 不存在即未完成。

## Claude 接手方式
1. 每筆只讀該筆 `queue.jsonl` 紀錄、`prompt-template.txt` 規則與已擷取來源；不讀同批其他結果及首批裁定。
2. 用 WebSearch／WebFetch 與本地擷取檔研究，依 `claim-output-schema.template.json` 寫 JSON（claim_id、hash 須與佇列一致）。
3. 以 `record_claude_adjudication.py` 記錄；執行標示為 `claude_takeover`／`claude-opus-5-5`，不得冒用 Codex thread 或輸出雜湊。
4. 所有結果（Codex 或 Claude）都要經 `check_batch_excerpts.py` 機械比對及 Claude 來源覆核，才能標 REVISED_SUPPORTED。
5. 董事長於 2026-10-11 決定：Claude 視為第三方獨立審查者。紀錄仍如實保存 Claude 同時擔任批次協調者的事實。
