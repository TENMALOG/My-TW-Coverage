# Task for Codex (READ-ONLY): independent QA audit of fact statements

Read `research-site/ops/qa-audit4/brief.md` and apply its ACCEPT/REJECT rules exactly, with one
difference: you cannot write files. Your FINAL MESSAGE must be only JSON Lines, one line per id of your
id file, same order:

    {"id": "...", "verdict": "ACCEPT"|"REJECT", "reason": "..."}

`reason` is short Traditional Chinese; for REJECT say exactly what is wrong. Open the cited page of every
fact (read-only Python: `.venv/Scripts/python.exe -X utf8 -c "..."`) — never judge from the statement alone.
