# v5 Handoff

Current status: **foundation implemented; activation blocked**.

## What is now defined

- v5 protocol and immutable-history rules
- deterministic-first machine gate
- exact binding fingerprint for carry-forward
- risk policy
- source policy
- financial/valuation draft policy
- dimension-level issuer state model
- independent-review/root escalation split
- low-risk QA sampling policy
- SQLite state skeleton
- locked 1304 regression contract

## What must happen next on the user's machine

The authoritative v4 workspace lives outside this GitHub fork. Before migration, inspect the real v4 locked docs/database and build a read-only export adapter that preserves IDs, hashes, source/policy/period bindings, revisions, acceptances and event lineage.

Do not guess the v4 schema from this branch.

Expected sequence:

1. resume v4 authoritative state read-only;
2. inspect actual v4 schema and locked protocol files;
3. implement/export a normalized v4 manifest without mutating v4;
4. run `auditctl.py validate-v4-export`;
5. dry-run import into a fresh v5 work database;
6. compare counts/hashes/orphans/collisions;
7. import 1304 lineage and run regression;
8. run a small pilot across different issuer types;
9. only after all gates pass, change `QA-REPAIR-REPORT.json` through a versioned commit.

## Important

The `fixtures/1304-regression.json` file records the already-known v4 summary supplied by the user. It deliberately does not claim to contain the immutable v4 evidence itself.
