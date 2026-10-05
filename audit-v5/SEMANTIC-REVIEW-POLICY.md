# Semantic HIGH Review Policy

Version: `semantic-high-1`

Scope: the calibrated HIGH queue only. The review unit is one HIGH claim, never the whole issuer by default.

## Required lineage

Every claim records a stable claim id, ticker/company/path, exact claim text, normalized claim hash, signal type, evidence records, author decision, independent-review decision, and final state.

## Evidence

Prefer TWSE / TPEx / MOPS / MOEA / regulator or government sources, then formal issuer disclosures, annual reports, investor presentations and official issuer pages. Search-result snippets are discovery leads only and cannot by themselves close a claim.

Each evidence record must preserve source URL/title, source level, publication/effective period when known, accessed date, and a short evidence note. Do not silently use a current undated page to prove a historical claim.

## Transient retrieval failures

HTTP 500–504, upstream connect errors, connection resets/timeouts, TLS/connect failures, and equivalent transient infrastructure/network errors are retrieval observations only. Do not infer from them that the source is unavailable, that Codex Cloud is blocked, that the source lacks supporting evidence, or that the claim is unsupported. In particular, `503` with an Envoy upstream-connect error before headers is an upstream/network-path failure, and `500` with an nginx error page is a server/reverse-proxy failure unless direct evidence establishes another cause.

Continue the claim review using other authoritative sources. A failed URL alone cannot determine the semantic decision. If no equivalent authoritative evidence can resolve a material qualifier, use the existing conservative `UNKNOWN_AFTER_RESEARCH` or `PARTIALLY_SUPPORTED` outcome as warranted and mark the affected source `LOCAL_RECHECK_PENDING`; do not use `SOURCE_UNAVAILABLE` solely because a transient retrieval failed.

Record material failures in `semantic/local-recheck-queue.json`. The queue key is a stable SHA-256 over `claim_id`, `normalized_claim_hash`, the exact attempted URL, and a stable `failure_signature` that distinguishes materially different failures. Repeated observations of the same failure append to that entry; they do not create duplicate entries. Preserve the timestamp/date, status, relevant response headers, exact error text, `retrieval_environment` (`codex-cloud`), issuer, claim text, and semantic consequence where available. Missing historical fields remain explicitly unknown and must not be reconstructed.

Queue observations are append-only. A later home-network result records source availability only and must be appended as a second observation; it cannot overwrite a Codex Cloud failure or directly change an author semantic decision. Codex Cloud remains responsible for inspecting any newly available source and making any later semantic decision through the normal author-review process. No local retrieval worker is implied by this policy.

## Decisions

Allowed semantic outcomes: `ACCEPTED`, `PARTIALLY_SUPPORTED`, `UNSUPPORTED`, `PERIOD_UNRESOLVED`, `SOURCE_UNAVAILABLE`, `UNKNOWN_AFTER_RESEARCH`.

HIGH claims require independent author/reviewer separation before final acceptance. Reviewer disagreement escalates; it must not be overwritten.

## Editing rule

Semantic verification does not silently rewrite reports. A supported correction may be proposed with `proposed_text`; corpus edits occur only through a separate auditable repair step.

## Carry-forward

An accepted claim can be carried forward only when claim hash, evidence/source hashes, period/issuer binding and materially applicable policy are unchanged.
