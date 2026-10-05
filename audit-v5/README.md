# Audit Engine v5

`audit-engine-v5` is the long-running audit layer for `My-TW-Coverage`.

Its purpose is not to weaken the v4 forensic standard. It changes when expensive semantic review is used:

1. deterministic machine checks first;
2. unchanged accepted evidence carries forward;
3. only changed, ambiguous, conflicting, or high-risk content reaches model review;
4. root adjudication is reserved for disputes and policy exceptions;
5. low-risk carried-forward content is sampled for QA.

## Safety status

**NOT READY FOR PRODUCTION.** This branch currently contains the v5 protocol, state schema, deterministic scanner, carry-forward fingerprint logic, financial exact-match guard, and the locked 1304 regression contract. A verified export of the local v4 authoritative state has not yet been imported into this repository, so migration and activation remain blocked.

## Local commands

```bash
python -X utf8 audit-v5/auditctl.py init
python -X utf8 audit-v5/auditctl.py scan --root Pilot_Reports --ticker 1304
python -X utf8 audit-v5/auditctl.py regression-1304
python -m unittest discover -s audit-v5/tests -v
```

Validate a normalized read-only v4 export before any migration:

```bash
python -X utf8 audit-v5/auditctl.py validate-v4-export path/to/v4-export.json
```

No command in v5 writes production report Markdown, deploys the site, pushes Git, or edits v4 artifacts.
