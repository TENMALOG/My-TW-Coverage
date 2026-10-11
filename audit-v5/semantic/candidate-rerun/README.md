# Claim reverification and strong final adjudication

## Scope and decision authority

The frozen rerun queue contains 833 original `PARTIALLY_SUPPORTED` and 450 original `UNKNOWN_AFTER_RESEARCH` claims: 1,283 total. The 111 original author `ACCEPTED` claims have a separate strong final-review queue. Two original `UNSUPPORTED` and three `SOURCE_UNAVAILABLE` claims are outside the requested rerun scope.

One claim receives one isolated context. Every compound assertion must be split into atomic claims, retaining entity, period, units, denominator, geography, ranking and named relationships. UNKNOWN is a valid research outcome. Missing evidence is not disproof. A supported rewrite does not establish support for the complete original.

Luna may emit only `UNKNOWN`, `PARTIAL`, or `CANDIDATE_ACCEPTED`. Every candidate requires final adjudication. Sol evaluates the complete original wording with prior verdicts and atom conclusions withheld; previous sources are only discovery leads. A final ACCEPTED requires full original support, verified client model configuration, independently captured supporting content, reproducible quotations, and a primary-agent check of actual source context.

## Append-only records and repairs

- `queue.jsonl`: frozen 1,283 original inputs, claim identity and author linkage.
- `batches/batch-001.jsonl` through `batch-008.jsonl`: immutable initial results.
- `batches/batch-009.jsonl`: 1,232 metadata-only corrections. Exact saved Hermes payloads and frozen prompts were reconciled; 498 incorrect output-path bindings were corrected. Citation IDs now bind the complete stable metadata, so separate locators/periods sharing a URL remain distinct. This batch is not new research.
- `batches/batch-010.jsonl`: supplemental Luna research for sequences 1–51 and 1239, preserving old rows. The first 50 had no Hermes execution capture, sequence 51 had no recoverable matching stdout, and sequence 1239 had SUPPORTED atoms without usable source URLs.
- `evidence/{rerun-id}/`: claim-bound manifests and notes; raw prompts, outputs and source bodies are in the ignored source-cache directory.
- `checkpoint.json`: effective counts from the latest result per queue sequence; physical append count is not a completed-claim count.

The requested Luna execution is Hermes `openai-codex`, `gpt-6-luna`, `xhigh`, one-shot, web tools, eight research turns. Requested configuration is distinguished from observed/resolved metadata; unavailable model observations remain null. The runner refuses unsafe paths, duplicate identities, missing evidence URLs for supported atoms and final ACCEPTED output. Operational timeouts, invalid JSON and quota failures are not counted as successful factual UNKNOWN results.

Resume supplemental work with the same batch ID:

```sh
python3 audit-v5/semantic/candidate-rerun/run_hermes_batch.py --workers 2 --attempts 1 --run-budget 660 --rerun-sequences 1-51,1239 --batch-id rerun-010
python3 audit-v5/semantic/candidate-rerun/validate_candidate_ledger.py
```

`validation/ledger-quality.json` is a structural and execution-binding audit, not a certificate of semantic truth. The candidate queue can be frozen only when this gate passes for all effective records.

## Strong final adjudication

`run_final_adjudication.py` uses native Codex CLI `gpt-6-sol` with `high` reasoning, live web access and a read-only isolated context. Explicit Max rechecks can be requested with `--effort max --recheck-claim-id EXACT_ID`. Public turn configuration verifies client selection; private reasoning is not read and transport-resolved model metadata is not invented.

- `adjudication/original-queue.jsonl`: frozen original 111-claim cohort.
- `adjudication/candidate-queue.jsonl`: frozen latest Luna candidates, created after supplemental research and quality validation.
- Both queues have SHA-256 manifests.
- `adjudication/results.jsonl`: append-only strong results; latest record per claim is effective.
- `adjudication/primary-source-review.jsonl`: primary-agent checks keyed to the exact model-output hash, including citation corrections.
- `adjudication/operational-failures.jsonl`: failures excluded from processed counts.
- Ignored `audit-v5/source-cache/candidate-rerun/adjudication/`: model execution artifacts and captured raw/text sources with hashes.

When a direct HTTP response contains a website block instead of source content, a separately saved `web.run.open` page excerpt can supplement it. These artifacts explicitly record `kind: web_tool_page_excerpt`, `partial_document: true`, captured line ranges, and the exact saved tool response; their raw artifact is **not** labelled a raw HTTP body. Earlier HTTP snapshots are preserved. `adjudication/supplemental-source-leads.jsonl` supplies claim-specific source URLs to subsequent fresh reviews without prior conclusions or changes to frozen input identity.

Failed acceptance/proof checks produce `PENDING_PROOF_REVIEW`, never ACCEPTED. UNSUPPORTED requires directly reproduced contradictory evidence. A blocked page or inaccessible source alone cannot establish a negative finding. Sources hosted by an exchange may still be AI summaries or marketing; the underlying filing must be inspected.

After a cohort finishes, `--recheck-held --effort max` reopens its effective proof holds and primary semantic review requests in fresh independent contexts. Requests can apply to any verdict, including a partial result with an unresolved interpretation issue. Credit exhaustion, quota and authentication failures stop subsequent queued requests in the current controller. No automatic credit reset or billing change is made.

Run the original cohort using the bundled Python runtime with pypdf:

```sh
/Users/sigmatrades/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 audit-v5/semantic/candidate-rerun/run_final_adjudication.py --cohort original --workers 1 --budget 900
```

Run the candidate cohort after the quality gate passes. `--parallel-with-legacy-original` is only for coexisting with the original legacy controller already running; it verifies that process and serializes result persistence.

```sh
/Users/sigmatrades/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 audit-v5/semantic/candidate-rerun/run_final_adjudication.py --cohort candidate --workers 3 --budget 900
```

## Progress and delivery

```sh
python3 audit-v5/semantic/candidate-rerun/summarize_adjudication.py
```

- `delivery/summary.json`: live counts and an explicit completion flag.
- `delivery/remaining-issues.json`: missing reviews, proof holds, integrity failures and required source checks. An empty list is necessary for completion.
- `delivery/accepted-original-claims.jsonl`: only complete originals passing both the strong proof gate and primary source review.
- `delivery/revised-claim-proposals.jsonl`: proposed rewrites; these do not modify the corpus or accept the original.
- `delivery/consolidated-status.jsonl`: the 1,394 in-scope claims, retaining the assessment stage and final-acceptance gate. Unreviewed author acceptances and pending source reviews remain explicitly pending.
- `validation/protected-integrity.json`: comparison against 7,361 preexisting protected-file hashes.

Original reports, author ledgers, reviewer ledgers, initial result batches and their evidence remain unchanged. Corrections and adjudications are separate records. The current delivery files are progress snapshots until `summary.json` reports `complete: true`; starting workers is not task completion.

### 原報告上下文補強（2026-10-09）

最終複核輸入另保存原報告 SHA-256、命中行與標題階層；「主要客戶」等段落限定語不得省略。原 claim ID、凍結佇列與作者 ledger 維持原樣。僅有工程實績而不能證明主要客戶的重要性者須重新裁決；`--recheck-held` 同時涵蓋來源補證與主代理要求的語義重審。新結果會保存逐次獨立的上下文快照，既有通過項目另經原報告段落檢視。

### 原始來源擷取補正

`repair_capture_hold.py CLAIM_ID` 僅可補正「已由 Sol 判定 ACCEPTED，但全部待審原因都是短引文未在本地來源重現」的項目。它必須核對原提示、實際模型輸出與 SHA-256，使用已保存的真實 HTTP 或明確標示為部分內容的網頁工具快照重跑相同證據門檻；不修改模型裁定、原 claim、執行綁定或舊 ledger 行。新行附原結果快照與雜湊，彙整器會檢查補正前後不可改變的欄位。解除擷取障礙後，仍須另經原報告範圍、來源期間與實際正文複核才會進入最終通過檔案。研究未完成、語意疑點或原句要件缺漏均不能用此工具解除。

### 每筆身份綁定及保留項目

每次強模型執行使用獨立的 `claim-output-schema.json`，把 `claim_id` 與 `normalized_claim_hash` 限定為該筆凍結值，並保存 schema 與控制程式版本雜湊。原報告上下文與補充來源線索亦保存逐次快照。當相近原句對同一來源的期間或範圍產生不同解讀，記錄 `REVIEW_REQUIRED` 並交由 fresh Max 再審；不直接改寫已有裁定以追求一致。

### 大型官方 PDF 與全稱量詞

原始來源擷取上限調整為 64 MiB，以保存約 44 MiB 的大台北 2025 永續報告原檔；仍核對 PDF 標頭、實際文字、原始位元組及雜湊。全稱量詞須保留原文主語與範圍：全部公司向某供應商採購，不能直接替代每家公司全部採購僅來自該供應商。營運上的唯一供應來源可用直接揭露證明，無須一律要求法律排他契約；範圍仍有歧義時保留不確定性。
