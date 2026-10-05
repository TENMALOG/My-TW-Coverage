# Semantic HIGH Review Policy

Version: `semantic-high-1`

Scope: the calibrated HIGH queue only. The review unit is one HIGH claim, never the whole issuer by default.

## Required lineage

Every claim records a stable claim id, ticker/company/path, exact claim text, normalized claim hash, signal type, evidence records, author decision, independent-review decision, and final state.

## Evidence

Prefer TWSE / TPEx / MOPS / MOEA / regulator or government sources, then formal issuer disclosures, annual reports, investor presentations and official issuer pages. Search-result snippets are discovery leads only and cannot by themselves close a claim.

Each evidence record must preserve source URL/title, source level, publication/effective period when known, accessed date, and a short evidence note. Do not silently use a current undated page to prove a historical claim.

## Decisions

Allowed semantic outcomes: `ACCEPTED`, `PARTIALLY_SUPPORTED`, `UNSUPPORTED`, `PERIOD_UNRESOLVED`, `SOURCE_UNAVAILABLE`, `UNKNOWN_AFTER_RESEARCH`.

HIGH claims require independent author/reviewer separation before final acceptance. Reviewer disagreement escalates; it must not be overwritten.

## Editing rule

Semantic verification does not silently rewrite reports. A supported correction may be proposed with `proposed_text`; corpus edits occur only through a separate auditable repair step.

## Carry-forward

An accepted claim can be carried forward only when claim hash, evidence/source hashes, period/issuer binding and materially applicable policy are unchanged.
