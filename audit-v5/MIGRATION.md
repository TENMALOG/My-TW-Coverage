# v4 -> v5 Migration

Status: **BLOCKED PENDING AUTHORITATIVE LOCAL V4 EXPORT**.

The GitHub fork does not contain the user's local `audit-engine-v4` database, immutable results, source cache or acceptance lineage. v5 must not invent those records.

## Migration phases

1. Read v4 authoritative state in place, read-only.
2. Produce a normalized export with a manifest plus atomic items and lineage references.
3. Validate export integrity without changing either engine.
4. Dry-run mapping into v5 IDs/states.
5. Verify counts, hashes, evidence references, acceptance lineage and orphan/collision counts.
6. Run 1304 regression.
7. Pilot several issuer classes.
8. Only then mark v5 active.

## Required manifest fields

The adapter should emit at least:

- source engine/protocol
- export timestamp
- source database hash
- issuer/job/result/acceptance/event/source-binding/policy-binding counts
- frozen-input manifest hash
- source-cache manifest hash if available

Each atomic item must preserve its old stable ID when available, issuer ID, prior status, source/result hashes, policy/period bindings and origin engine. If v5 needs a new ID, maintain an explicit old-ID -> new-ID mapping.

## Failure conditions

Migration fails on any lost issuer, evidence orphan, result/acceptance hash mismatch, broken lineage, duplicate active item, ID collision without mapping, altered v4 artifact, or unexplained count drift.

No unresolved v4 item may be promoted merely because v5 exists. A v5 deterministic promotion such as `AUTO_VERIFIED` must cite preserved v4 evidence and the exact v5 rule that establishes it.
