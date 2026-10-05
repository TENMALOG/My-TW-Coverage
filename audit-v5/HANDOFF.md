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


## Risk calibration milestone

HIGH calibration is complete and accepted under `risk-3-calibrated`.

Final issuer triage:

- HIGH 836
- MEDIUM 750
- LOW 147

The HIGH queue is claim-level, not issuer-forensic. The accepted calibration is documented in `RISK-CALIBRATION-REPORT.md` and machine-readable details are in `generated/risk-calibration.json`.


## Financial Phase 1 milestone

The current-period general-industry accounting mapping and exception-resolution work is complete.

Canonical mappings:

- Revenue -> MOPS/TWSE 營業收入
- Gross Profit -> MOPS/TWSE 營業毛利（毛損）
- Operating Income -> MOPS 營業利益（損失） / Mopsfin OperatingIncome
- Net Income -> MOPS 母公司業主（淨利∕損）

The former 1,029 METHOD_UNRESOLVED population is no longer treated as 1,029 issuer-specific investigations:

- 1,019 Operating Income mismatches are classified as SOURCE_DEFINITION_DIFFERENCE caused by the legacy Yahoo/yfinance field versus the approved MOPS concept;
- 10 items remain METHOD_UNRESOLVED for specialized financial-sector schemas.

The 26 true non-operating current-period differences were cross-checked against a second official MOPSFIN statement source. All 26 were confirmed as repository errors and repaired across 20 issuer reports. The post-repair official checker reports FINANCIAL_DIFFERENCE = 0.

See `FINANCIAL-PHASE1-REPORT.md` and `generated/financial-difference-resolution.json`.


## Financial Phase 1 final closure

Financial Phase 1 is complete for all deterministically comparable current-period cells:

- 6,207 / 6,207 AUTO_VERIFIED
- 0 FINANCIAL_DIFFERENCE
- 0 METHOD_UNRESOLVED
- 0 SOURCE_DEFINITION_DIFFERENCE
- 0 REPO_VALUE_UNAVAILABLE

3659, 4546 and 6618 are explicitly handled as 2026H1 semiannual/YTD cases; no synthetic Q1 split was invented.
