# Audit Engine v5 Protocol

Protocol: `1.2.0-draft`

## Objective

Maintain defensible factual correctness across the Taiwan equity coverage corpus without repeatedly re-proving immutable evidence.

The operating order is:

`machine gate -> change detection -> risk classification -> carry-forward -> semantic review -> independent QA -> root escalation`

## Non-negotiable invariants

- v1-v4 are historical and read-only.
- No direct database state flips; every transition creates an event.
- Old sources, extracted text, results, revisions, checkpoints, acceptances, author/reviewer lineage, session/model metadata, and migration records remain immutable.
- A model/session/quota/date change alone never invalidates an accepted fact.
- Unsupported PDF/OCR evidence remains unresolved.
- Search snippets are leads, never sufficient final evidence by themselves.
- Unknown can close only as `UNKNOWN_AFTER_RESEARCH` with documented authoritative research.
- Audit work is local only; production edits, deployment, Git merge/push, purchases, shutdown and sleep are out of scope unless separately authorized.

## Atomic states

`PENDING_MACHINE`, `AUTO_VERIFIED`, `CARRY_FORWARD_ACCEPTED`, `NEEDS_MODEL_REVIEW`, `UNDER_REVIEW`, `ACCEPTED`, `PARTIALLY_SUPPORTED`, `UNSUPPORTED`, `METHOD_UNRESOLVED`, `PERIOD_UNRESOLVED`, `IDENTITY_UNRESOLVED`, `UNRESOLVED_PDF`, `SOURCE_UNAVAILABLE`, `UNKNOWN_AFTER_RESEARCH`, `REJECTED`, `REVISION_REQUIRED`, `BLOCKED`.

## Dimensions

Each issuer is tracked independently across:

- identity
- identity_history
- narrative
- supply_chain
- customers_suppliers
- financials
- valuation
- source_period_integrity

Issuer-level status may be `VERIFIED`, `VERIFIED_WITH_EXCEPTIONS`, `PARTIALLY_VERIFIED`, `NEEDS_REVIEW`, or `BLOCKED`.

## Deterministic first

An item may become `AUTO_VERIFIED` only when a deterministic rule proves the relevant identity, period, scope, currency/unit, mapping and exact/within-policy numeric comparison. Machine evidence must record all inputs and the applicable rule version.

`AUTO_VERIFIED` never means the whole issuer is verified.

## Carry-forward

An already accepted item may become `CARRY_FORWARD_ACCEPTED` only if all of these remain equal:

- normalized claim hash
- source raw hash
- extracted source text hash
- evidence span hash
- factual period binding
- issuer binding
- materially applicable policy binding

A changed fragment reopens only itself and directly dependent items. Unchanged siblings do not reopen automatically.

## Semantic review

New or materially changed HIGH-risk factual claims require independent author/reviewer separation. Normal reviewer acceptance does not require root review.

Root handles only disagreements, rejection, conflicting authoritative evidence, identity ambiguity, accounting/valuation method conflicts, policy exceptions, systematic QA failures, migration anomalies and cross-issuer contamination.

## Claims and recovery

One issuer per active claim. Routine assignments must not overlap. Same-session resume rotates the current token. Lease age alone is not sufficient for recovery; authoritative liveness must show the owner terminal first. Checkpoint after each original fragment or five minutes, whichever occurs first.
