# Task for Codex (READ-ONLY): fix percentages without a named denominator

Follow `research-site/ops/codex-review/adjudicate_brief.md` exactly, with one difference: you cannot
write files. Your FINAL MESSAGE must be only the JSON Lines described there — one line per id of your
input file, same order:

    {"id": "...", "action": "KEEP"|"FIX"|"DROP", "new_statement": "...", "new_attribution": "...", "reason": "..."}

Most items only need the denominator named from the table the excerpts quote (占銷售地區表合計、
占全年度銷貨淨額、占全年度進貨淨額、營業比重、占營業收入淨額合計). KEEP if the denominator is already
clear. Never add a number that is not in the fact's excerpts. Use read-only Python
(`.venv/Scripts/python.exe -X utf8 -c "..."`) to read the fact files and report pages.
