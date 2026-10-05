# Audit Engine v5

`audit-engine-v5` is the GitHub-native long-running audit layer for `TENMALOG/My-TW-Coverage`.

## Authoritative baseline

By explicit project decision on 2026-10-05, v5 bootstraps from the current GitHub repository rather than requiring the local v4 audit database. The GitHub corpus is the operational source of truth for v5.

Observed before the first GitHub-native refresh:

- branch: `audit-v5`
- source commit: `39d5e4417864fefe5b5e7905ee2532026962725f`
- report files: 1,734
- sector directories: 98
- README still declared 1,735 companies / 99 sectors, so that mismatch is an audit finding, not something to hide.

The local v4 work is not required for v5 activation. Its complete lineage is therefore not claimed as migrated. The known 1304 台聚 result remains a regression fixture so v5 cannot gain speed by swallowing known differences or method gaps.

## Operating model

1. deterministic machine checks first;
2. refresh financials/valuation from the repository's existing updater;
3. rebuild derived indexes;
4. hash the complete GitHub corpus;
5. classify risk;
6. use semantic review only for changed/ambiguous/high-risk claims;
7. carry forward unchanged accepted evidence in future cycles.

## GitHub Actions

`.github/workflows/audit-v5-full-refresh.yml` performs the first full GitHub-native machine refresh and validation on `audit-v5`.

It:

- runs unit tests and 1304 regression;
- scans every report before refresh;
- refreshes all financial/valuation sections, retrying transient failures;
- rebuilds wikilink/theme/network outputs;
- scans every report after refresh;
- writes a persistent GitHub snapshot and summary;
- uploads detailed diagnostics as a workflow artifact;
- commits refreshed data back to `audit-v5` only when the refresh completes cleanly.

Narrative/source semantic verification is intentionally not mislabeled as complete merely because machine checks pass.
