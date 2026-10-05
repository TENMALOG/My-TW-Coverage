# Valuation Audit Policy

Version: `valuation-1-draft`

## Price

For a stated trading date, v5's canonical public price should use the official TWSE/TPEx closing price when available and label it explicitly as close/date/currency.

A legacy value that only says `as of` without a close/intraday basis is recorded as `SOURCE_PRICE_BASIS_UNKNOWN`; do not spend unbounded research trying to reverse-engineer an undocumented vendor convention.

## P/B, P/S and market cap

Verification requires a fixed formula, explicit price date, denominator period, share-count definition and treasury-share policy. If these cannot be reproduced, do not mark verified.

## Forward P/E

Verify only with a traceable public forecast/consensus source including publication/as-of time and EPS definition. Without a reliable public consensus source, use `SOURCE_UNAVAILABLE` or a policy-specific unavailable disposition rather than inventing a comparison.

## EV / EV-EBITDA

Verification requires explicit components for market cap, debt, cash and any applicable preferred/non-controlling interests, plus an EBITDA definition and period. If components/definition cannot reproduce the value, use `METHOD_UNRESOLVED`.
