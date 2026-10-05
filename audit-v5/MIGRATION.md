# v5 Bootstrap / Legacy Migration

## Active decision

v5 no longer requires migration from the user's local `audit-engine-v4` database.

The authoritative v5 baseline is the current GitHub corpus in `TENMALOG/My-TW-Coverage`.

This is a deliberate reset of operational provenance, not a claim that v4 lineage was imported.

## What is preserved from v4

Only information actually present in GitHub or explicitly recorded in v5 is part of v5 provenance.

The 1304 台聚 regression fixture preserves known v4 summary invariants:

- 30 narrative claims;
- 98 financial cells;
- 66 exact matches;
- 11 numeric differences;
- 21 method gaps;
- 8 valuation cells;
- 6 identity/history items.

The immutable local v4 evidence database is not represented as migrated unless it is later imported explicitly.

## GitHub-native bootstrap

The first v5 refresh must:

1. identify the exact parent Git commit;
2. scan every `Pilot_Reports/**/*.md` file;
3. refresh financials/valuation;
4. rescan the resulting corpus;
5. hash every report into `audit-v5/generated/github-baseline.json`;
6. record actual report and sector counts;
7. detect duplicate tickers/company filenames;
8. persist `audit-v5/generated/audit-summary.json`;
9. retain full machine-gate logs as a GitHub Actions artifact;
10. commit the refreshed corpus to `audit-v5`, never directly to `master`.

## Historical v4 import

A later v4 import is optional. If ever performed, it must be append-only and must not retroactively rewrite the GitHub-native baseline.
