# Audit Engine v5 Operations

## Active queue rule

Only v5 may become the active new queue after migration verification. v1-v4 remain read-only. Never operate two writable queues against the same corpus.

## Worker layout

Preferred operating shape when available:

- root: high-capability adjudicator
- routine worker A
- routine worker B
- independent QA/reviewer slot

Actual picker/model version must be observed and recorded; never infer it from preference text.

Routine accepted work bypasses root. Pause new author work when independent-review backlog is full. Root escalation backlog must not block already accepted routine work.

## Resource boundaries

- Reuse existing source cache and GPU preprocessing where hashes match.
- Do not re-download or reprocess because the engine/model/session changed.
- New source versions are append-only and must not overwrite prior raw artifacts.
- Do not commit source caches, GPU caches, SQLite state, WAL/SHM files, generated work output or downloaded PDFs to Git.

## Safe startup

Before using local v4 data, obtain its authoritative state with the existing v4 control command. Do not claim new v4 routine work.

Then export v4 through a read-only adapter into the normalized v5 migration contract and run:

```bash
python -X utf8 audit-v5/auditctl.py validate-v4-export <export.json>
```

Activation is prohibited until counts, hashes, lineage and 1304 regression checks pass.

## Checkpoints

Checkpoint after each original narrative fragment or every five minutes. Preserve immutable prior checkpoints.

## Reporting

Allowed operational counts include issuers/items by state, risk class, auto-verified, carry-forward, model-reviewed, unresolved, rejected and QA sample outcomes. Do not manufacture an overall completion percentage or ETA without an explicit denominator and measured throughput definition.
