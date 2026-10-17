# Company name history from annual reports

Repo root: the folder that contains `research-site/`. Read-only Python: `.venv/Scripts/python.exe -X utf8`.

Input: one job file (JSON list). Each entry is a listed company: `id` (= ticker), `company`, `legal_name`,
`fy`, and `hits` = pages (1-based page numbers as written by the page markers in the text snapshot) whose
text mentions a name change, with snippets. The full annual-report text is the snapshot at
`research-site/data/company-facts/{ticker}.json` -> `source.text_path`; read pages with
`research-site/scripts/annual/slice_annual.py` `page_texts(text)` (dict page_no -> text).

For every company, open each hit page (and the neighbouring page when the sentence continues) and record
only the name changes of THE LISTED COMPANY ITSELF (the issuer whose ticker this is). Typical source: the
公司沿革 / 公司簡介 section ("本公司於民國XX年更名為…", "原名…").

Do NOT record: subsidiaries' or investees' renames, product or brand renames, department renames,
counterparties' renames, merger targets' names (unless the issuer itself took a new name), English-name-only
changes are fine to record (mark kind "english").

Output one JSON line per input entry, same order:

    {"id": "1234", "renames": [{"former_name": "...", "new_name": "...", "date_text": "...",
      "kind": "chinese"|"english", "page": 12, "excerpt": "..."}], "note": "..."}

- `excerpt` is copied verbatim from the page (at least 8 characters, contains the former name if stated), so it can be
  matched mechanically; `date_text` exactly as the report writes it (民國111年8月, 2011年) or "" if absent.
- Names as the report writes them; never guess a name that is not on the page; no natural-person names.
- If the report says the issuer changed its name but does not state the former name, still record it with
  `"former_name": ""` (the excerpt then contains the new name and the date); never guess the former name.
- If the hits are only about subsidiaries or products, output `"renames": []` and say why in `note`.
