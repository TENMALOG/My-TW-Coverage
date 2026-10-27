"""Prospectus rules v2: run the annual-report verifier and glyph scan on prospectus facts.

  .venv/Scripts/python.exe -X utf8 research-site/ops/full-coverage-p2/prospectus/verify_prospectus.py [TICKER ...]

Same five deterministic checks as verify_extraction.py (source hash, excerpt found, page match, numbers
supported, identity), against research-site/schemas/company-facts-prospectus.schema.json and the files in
research-site/data/company-facts-prospectus/. Glyph flags use the annual-report character frequencies and are
written to prospectus/glyph-flags.jsonl.
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(ROOT / 'research-site/scripts/annual'))
import scan_glyphs  # noqa: E402
import verify_extraction as ve  # noqa: E402

FACTS = ROOT / 'research-site/data/company-facts-prospectus'
ve.SCHEMA_PATH = ROOT / 'research-site/schemas/company-facts-prospectus.schema.json'
tickers = sys.argv[1:]
ve.main(['--dir', str(FACTS)] + (['--tickers', *tickers] if tickers else []))

df = scan_glyphs.doc_freq()
out = []
for path in sorted(FACTS.glob('[0-9]*.json')):
    if tickers and path.stem not in tickers:
        continue
    for f in json.loads(path.read_text(encoding='utf-8'))['facts']:
        hits = sorted({(c, r) for c in f['statement'] if (r := scan_glyphs.reasons(c, df, 3))})
        if hits:
            out.append({'id': f['id'], 'statement': f['statement'],
                        'chars': [{'char': c, 'codepoint': f'U+{ord(c):04X}', 'reason': r} for c, r in hits]})
(HERE / 'glyph-flags.jsonl').write_text(''.join(json.dumps(x, ensure_ascii=False) + '\n' for x in out), encoding='utf-8')
print(f'glyph flags={len(out)}')
for x in out:
    print(' ', x['id'], ' '.join(f"{c['char']}({c['reason']})" for c in x['chars']), '|', x['statement'][:60])
