# Risk Policy

Version: `risk-3-calibrated`

## HIGH

Mandatory semantic review for identity conflict/cross-company contamination, rename/merger/split/delisting/ticker reuse, conflicting authoritative sources, unsupported material customer/supplier relationships, period mismatch, material financial mismatch, valuation price mismatch, material unsupported PDF/OCR, prior reviewer rejection, historical legal-identity conflict, and high-impact assertions such as largest/first/only/leader, margin/profit-engine claims, market share, named major customers/suppliers, export relationships and claimed supply-chain entry.

## MEDIUM

Examples include changed product mix, capacity, technical applications, general supply-chain position, current company self-description with unclear historical applicability, stale/undated sources, secondary-only evidence, formula ambiguity and address-field semantic mismatch.

## LOW

Previously accepted and unchanged facts with unchanged evidence/period/identity/policy, plus deterministic exact matches.

## Claim time class

Narrative claims should also be tagged:

- `STATIC`: durable legal/history facts such as incorporation/listing dates.
- `PERIOD_SCOPED`: claims explicitly tied to a reporting period.
- `DYNAMIC`: current products/capacity/customer/supplier/strategy facts.
- `HIGH_IMPACT_ASSERTION`: ranking, profitability, market share or named commercial relationship assertions requiring stronger evidence.


## Calibration v2 — claim-level HIGH classification

Issuer-level HIGH is now derived from claim-level signals inside narrative sections only. Headings, metadata and financial tables cannot create semantic HIGH.

HIGH requires at least one of:

- explicit ranking/market-share assertion (e.g. largest, first, only, leader, market share);
- profitability/earnings-contribution assertion (e.g. high margin, profit engine);
- material corporate event (M&A, acquisition, split, delisting, renaming);
- named commercial relationship where the same claim contains both a customer/supplier/ship-to/procurement relation and a named entity;
- export assertion tied to a concrete geography or percentage.

Generic export language, generic supply-chain language and other dynamic business descriptions are MEDIUM.

This calibration intentionally optimizes precision over recall at the issuer HIGH level: borderline cases stay MEDIUM and may still be sampled or escalated later.


## Calibration v3 — immediate HIGH versus reviewable MEDIUM

The second calibration showed that treating every named relationship and every "leader/leading" phrase as HIGH would classify 1,304 of 1,733 issuers as HIGH, which defeats risk-based triage.

v3 therefore reserves immediate HIGH for:

- objective largest/first/only/market-share/ranking assertions;
- profitability or earnings-contribution assertions;
- identity-changing legal events;
- acquisitions implying full control/succession;
- named commercial relationships with materiality or inference-risk qualifiers such as major/core/largest customer or supplier, revenue share, Tier 1, direct supply, exclusive, design-in, supply-chain entry, end customer, designated supplier or certification;
- export concentration/share assertions.

Ordinary named supplier/customer relationships, geography-only export assertions, acquisitions without identity/control implications, and subjective "leader/leading" positioning are MEDIUM. They remain reviewable and sampleable; they are simply not immediate HIGH.


## Calibration acceptance

Calibration v3 is accepted as the active issuer triage policy for the GitHub-native v5 baseline.

Acceptance basis:

- all v5 unit/regression tests passed;
- full 1,733-report machine gate passed with zero identity-unresolved and zero structural-blocked reports;
- semantic HIGH is now derived from narrative claims only;
- the over-broad v2 result (1,304 HIGH issuers) was rejected;
- v3 classifies 836 HIGH, 750 MEDIUM and 147 LOW issuers;
- HIGH samples were inspected across objective ranking/market-share, material named relationships, profitability, identity-changing events, control acquisitions and export concentration;
- generic headings, metadata, financial tables, ordinary supplier/customer relationships, geography-only export claims and subjective leader/leading language no longer force HIGH.

This calibration is about triage priority, not factual acceptance. HIGH claims still require evidence review before they become verified facts.
