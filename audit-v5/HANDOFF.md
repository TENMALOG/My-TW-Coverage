# v5 Handoff

Current mode: **GitHub-native bootstrap**.

The user explicitly chose to use the current GitHub repository as the v5 baseline instead of waiting for local v4 migration.

## Implemented

- deterministic report machine gate;
- filename/title identity checks compatible with the existing report format;
- section checks compatible with suffixed headings such as `財務概況 (單位...)`;
- exact financial auto-verification guard;
- carry-forward fingerprint contract;
- risk/source/financial/valuation/sampling policies;
- 1304 regression contract;
- GitHub corpus manifest generator;
- full financial-refresh wrapper with retry/failure guard;
- audit summary generator;
- GitHub Actions full-refresh workflow.

## First full run

The workflow is designed to run on `audit-v5` and, if GitHub Actions is enabled for the fork, perform the complete machine-verifiable refresh.

After the run, inspect:

- `audit-v5/generated/financial-refresh-summary.json`
- `audit-v5/generated/github-baseline.json`
- `audit-v5/generated/audit-summary.json`
- workflow artifact containing before/after machine-gate details and legacy audit logs.

## Important boundary

A successful workflow means the machine-verifiable layer completed. It does not by itself prove every narrative/customer/supplier/high-impact claim. Those remain queued by v5 risk classification for semantic/source verification.

Do not merge `audit-v5` into `master` until the first refresh result is reviewed.
