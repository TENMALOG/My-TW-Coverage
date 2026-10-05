# Decision Log

## 2026-10-05 — Bootstrap v5 directly from GitHub

Decision: use `TENMALOG/My-TW-Coverage` as the authoritative v5 operational baseline and do not require the local v4 audit workspace for activation.

Rationale:

- only 1304 had been fully run through the expensive v4 forensic flow;
- continuing v4 across the whole corpus would impose disproportionate time cost;
- v5 is intentionally deterministic-first and risk-based;
- current GitHub content is complete enough to establish a fresh, hashable baseline.

Consequences:

- v5 does not claim full migration of v4 author/reviewer/source lineage;
- the known 1304 v4 result remains a regression contract;
- the first GitHub-native refresh creates new v5 provenance;
- future accepted unchanged items can use v5 carry-forward;
- `master` remains untouched until explicit merge approval.

## 2026-10-05 — First GitHub-native full refresh requested

The user authorized v5 to use the current GitHub corpus directly for the full update/validation cycle. This commit also serves as the first workflow trigger after the refresh workflow was installed.
