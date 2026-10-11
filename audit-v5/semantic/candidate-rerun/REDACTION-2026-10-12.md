# 金鑰遮蔽紀錄（2026-10-12）

- **原因**：環境部開放資料 API 網址內含兩把非官方範例的 api_key（官方 openapi.yaml 範例金鑰為 9be7b239-…），疑為會員個人金鑰；repo 為公開，push 前遮蔽。
- **授權**：董事長 2026-10-12 核准選項 A（含凍結檔 revision-pilot-001/inventory.jsonl 破例修改）。
- **做法**：兩把金鑰字串一律替換為 `<REDACTED>`，其他位元組不變。
- **未改動的歷史紀錄**：各批次 queue.jsonl 的 proposal_binding.input_sha256 與 queue.manifest.json 仍記載舊 inventory 雜湊 3c2b97ed…；batch-015 queue.manifest.json 的 queue_sha256 仍為舊值 99efc523…。比對時請以下表換算。
- research-site/catalog/catalog-manifest.json 的 inventory 雜湊已更新為新值。
- 已知影響：build_revision_inventory.py 的 freeze() 若重跑會因內容不同而拒絕，需先還原或改用新雜湊。

| 檔案 | 遮蔽前 SHA-256 | 遮蔽後 SHA-256 |
|---|---|---|
| `audit-v5/semantic/candidate-rerun/evidence/rerun-000844/manifest.json` | 0e83baa9fb3efbdf56057696a653c3966b27d4e3404ff54d407f5c737683d025 | 2a35ee6ea9ffdc359dd978340e6c3aebc9508f880b2f5246741dd40e481051bd |
| `audit-v5/semantic/candidate-rerun/evidence/rerun-000844/notes.md` | 80b304bba97bdde6251373d71e1a104955fc8a47e4d35545637232c412849729 | 9b9c76f58cad5a3a1563c7f49825d7534cf5cab19defe2083859a72176737503 |
| `audit-v5/semantic/candidate-rerun/evidence/rerun-000845/manifest.json` | dd8385f11c1aab4597b79cb827a415be4ee53f08c24dd280f7bb5be395346512 | c635068b20e6e70bad8ed7b07d725e9e0b3ce1dc8a75cf1ad7b08dce3180181b |
| `audit-v5/semantic/candidate-rerun/evidence/rerun-000845/notes.md` | fcb1ed23d5a168d5b2efe5409c60c278839fe69e692bb9bcb34982e03e488ad8 | 02284c05fb4d505fb97abd9e084986c805edb43a5d104d0636192cc8ae57e1ec |
| `audit-v5/semantic/candidate-rerun/evidence/rerun-009-000844/manifest.json` | 97483a2d1ab0406a0357fd928ff5b0f5411c3a9b3077daf473a1f67b5c0aa6be | 1d0ac0158800f0fa9b101944f92d71e3c7a0ff2568c7d58c6dd1b4ddfc702da5 |
| `audit-v5/semantic/candidate-rerun/evidence/rerun-009-000844/notes.md` | 9272890d175d13071dc10465498c47950de6d9436f84de28f94e3e81fa801b05 | 1401ec54c74174c96a627b92cbb294834b9e450dc857f4a4bfade85159f2d5a5 |
| `audit-v5/semantic/candidate-rerun/evidence/rerun-009-000845/manifest.json` | e68adb18f5b8d719c4388630062797acc1d02e7902eeca9df24d81e93cbdd0ff | ef80cc71aaf5de33d59d8bad7df70df19e081b32a171006d5fbd8358e3e4a361 |
| `audit-v5/semantic/candidate-rerun/evidence/rerun-009-000845/notes.md` | 62ef0be06567d5dc352a1a12738fa26825acfa6a9cad1fdbfec8ad52790a3bca | b370fd44360093313a857dca4477f73041f37ececac603d49dc0c9f2eabeccf9 |
| `audit-v5/semantic/candidate-rerun/revision-batch-015/queue.jsonl` | 99efc523cab8867ffef7c901bd5f79609f702722d22b4224239e058e2ab99390 | bfaeb7543d936e4f9c07a7299b1e43cd48f50e4212982e418e8de75d4a739320 |
| `audit-v5/semantic/candidate-rerun/revision-pilot-001/inventory.jsonl` | 3c2b97edd0947c6b5248833a9147a90c3e14899c6048a85aadbe90a82199d553 | 18058b4917ced8bf63721f8b669a5ae8594b4e3a3279852ad3f54a8560758d33 |
