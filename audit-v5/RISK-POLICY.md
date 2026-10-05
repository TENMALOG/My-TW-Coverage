# Risk Policy

Version: `risk-1-draft`

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
