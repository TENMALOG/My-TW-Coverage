# Financial Audit Policy

Version: `financial-1-draft`

## Principle

Do not spend model reasoning confirming arithmetic equality. Financial exact matches are deterministic; accounting-definition ambiguity is not.

## AUTO_VERIFIED prerequisites

A financial cell may be auto-verified only when all are established:

- issuer identity match
- reporting period match
- annual/quarterly context match
- consolidated/individual scope match
- currency match
- unit normalization match
- unambiguous account/tag mapping
- approved rounding/tolerance rule
- original and official values compare equal within policy

If any prerequisite is missing, do not auto-pass.

## Differences

A numeric mismatch becomes `NEEDS_MODEL_REVIEW` or a more specific unresolved state. The original and official value, exact source context and calculation must be retained.

## Global method questions

Questions such as which net-income concept to use, CAPEX definition, operating-income adjustments or FCF formula are corpus-level policy questions. They must be decided once and versioned here rather than re-litigated independently for every issuer.

Until approved, affected cells remain `METHOD_UNRESOLVED`.

## Initial draft choices intentionally not finalized

This file does **not** yet approve a single net-income or CAPEX mapping because the local v4 schema/evidence has not been inspected here. The first v5 migration must surface the existing v4 definitions before finalizing these mappings.
