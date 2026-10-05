# Risk Calibration Report — HIGH queue

Status: **COMPLETE / ACCEPTED**

Date: 2026-10-05  
Corpus: 1,733 issuer reports / 98 sectors  
Branch: `audit-v5`

## Objective

Calibrate the original issuer-level HIGH queue so v5 does not waste semantic-review capacity on headings, metadata, financial-table language, generic supply-chain wording or ordinary named relationships.

The calibration target was precision: HIGH should mean "review this material/fragile claim first", not merely "this report contains a risky keyword".

## Baseline

Before calibration:

- HIGH: 884
- MEDIUM: 591
- LOW: 258

The original classifier was term-based and could elevate an entire issuer when a keyword appeared anywhere in the narrative input.

## Calibration experiments

### v2 — rejected

Claim-level parsing was introduced, but all named commercial relationships and subjective leader/leading language were still HIGH.

Result:

- HIGH: 1,304
- MEDIUM: 277
- LOW: 152
- HIGH share: 75.25%

This was rejected because it made the HIGH queue less selective than the original classifier.

### v3 — accepted

Immediate HIGH is now limited to:

- objective largest / first / only / market-share / explicit ranking assertions;
- profitability or earnings-contribution assertions;
- identity-changing legal events;
- acquisitions implying control or succession;
- named commercial relationships with materiality/inference-risk qualifiers such as major/core/largest customer or supplier, revenue share, Tier 1, direct supply, exclusive, design-in, supply-chain entry, end customer, designated supplier or certification;
- export concentration/share assertions.

Moved to MEDIUM:

- ordinary named customer/supplier relationships;
- subjective "leader/leading" positioning;
- acquisitions without control/identity implications;
- geography-only export assertions;
- generic export/supply-chain/dynamic-business language.

Final result:

- **HIGH: 836**
- **MEDIUM: 750**
- **LOW: 147**
- HIGH share: **48.24%**

## HIGH claim signals

The accepted calibration found 1,410 immediate-HIGH claim signals across the 836 HIGH issuers:

- objective ranking / market share: 951
- material named commercial relationship: 317
- profitability assertion: 67
- identity-changing event: 42
- export concentration: 28
- control acquisition: 5

These are claim counts, not issuer counts; one issuer may contain multiple HIGH claims.

## Verification of calibration behavior

The automated calibration asserts all of the following:

- headings cannot create semantic HIGH;
- metadata cannot create semantic HIGH;
- financial tables cannot create semantic HIGH;
- generic export language is MEDIUM;
- generic supply-chain language is MEDIUM;
- ordinary named supplier/customer relationships are MEDIUM;
- subjective "leader/leading" language is MEDIUM;
- objective largest/first/only/market-share claims remain HIGH;
- major/core/Tier-1/direct/exclusive/design-in/end-customer relationships remain HIGH;
- profitability claims remain HIGH;
- identity-changing events remain HIGH.

The GitHub Actions validation run completed successfully after these rules were applied.

## Interpretation

The final 836 is intentionally not forced downward to an arbitrary quota. The remaining HIGH population is large because the source corpus itself contains many explicit ranking, market-share and material customer/supplier assertions.

v5 must therefore review **HIGH claims**, not rerun full forensic audits on all 836 issuers.

The next semantic-review unit is the individual HIGH claim, with unchanged unrelated content eligible for carry-forward.
