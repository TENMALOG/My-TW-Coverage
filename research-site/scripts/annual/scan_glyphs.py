"""Flag facts whose statement contains characters that are likely PDF text-layer errors.

  .venv/Scripts/python.exe -X utf8 research-site/scripts/annual/scan_glyphs.py [--tickers ...] [--max-df 3]

verify_extraction.py cannot catch a wrong glyph: the bad character exists verbatim in the snapshot
text, so the excerpt check passes (P1 pilot: 7911 「強雊」 for 強韌, 「大孙宙」 for 宇宙). A statement
character is flagged when it is
  - U+FFFD, a private-use character, or a CJK compatibility ideograph (U+F900–U+FAFF), or
  - a CJK ideograph that Big5 (cp950) cannot encode (e.g. simplified forms), or
  - a CJK ideograph that appears in at most --max-df of all cached annual-report texts.
Flags are for human review only; this script never changes facts or their verification.
Writes research-site/data/company-facts/_glyph-flags.jsonl (one line per flagged fact).
"""
from __future__ import annotations

import argparse
import json
import sys
import unicodedata
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from slice_annual import CACHE, ROOT  # noqa: E402

FACTS = ROOT / 'research-site/data/company-facts'
DF_CACHE = ROOT / 'research-site/data/annual-slices/_char-doc-freq.json'


def is_cjk(c):
    return 'CJK' in unicodedata.name(c, '')


def doc_freq():
    """Number of cached annual-report texts each CJK character occurs in (cached by text_sha256 set)."""
    texts = sorted({json.loads(p.read_text(encoding='utf-8')).get('text_path') for p in CACHE.glob('*_F04.json')} - {None})
    key = f'{len(texts)}'
    if DF_CACHE.exists():
        saved = json.loads(DF_CACHE.read_text(encoding='utf-8'))
        if saved.get('key') == key:
            return saved['df']
    df = {}
    for t in texts:
        path = ROOT / t
        if not path.exists():
            continue
        for c in set(path.read_text(encoding='utf-8')):
            if is_cjk(c):
                df[c] = df.get(c, 0) + 1
    DF_CACHE.write_text(json.dumps({'key': key, 'df': df}, ensure_ascii=False), encoding='utf-8')
    return df


def reasons(c, df, max_df):
    o = ord(c)
    if c == '�' or 0xE000 <= o <= 0xF8FF:
        return 'replacement_or_private_use'
    if 0xF900 <= o <= 0xFAFF:
        return 'cjk_compatibility'
    if not is_cjk(c):
        return None
    try:
        c.encode('cp950')
    except UnicodeEncodeError:
        return 'not_in_big5'
    if df.get(c, 0) <= max_df:
        return f'rare_df_{df.get(c, 0)}'
    return None


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--tickers', nargs='*'); ap.add_argument('--max-df', type=int, default=3)
    a = ap.parse_args()
    df = doc_freq()
    files = [FACTS / f'{t}.json' for t in a.tickers] if a.tickers else sorted(FACTS.glob('[0-9]*.json'))
    out, n = [], 0
    for path in files:
        if not path.exists():
            continue
        doc = json.loads(path.read_text(encoding='utf-8'))
        for f in doc['facts']:
            n += 1
            hits = sorted({(c, r) for c in f['statement'] if (r := reasons(c, df, a.max_df))})
            if hits:
                out.append({'id': f['id'], 'statement': f['statement'], 'chars': [{'char': c, 'codepoint': f'U+{ord(c):04X}', 'reason': r} for c, r in hits]})
    (FACTS / '_glyph-flags.jsonl').write_text(''.join(json.dumps(x, ensure_ascii=False) + '\n' for x in out), encoding='utf-8')
    print(f'facts={n} flagged={len(out)}')
    for x in out[:40]:
        print(' ', x['id'], ' '.join(f"{c['char']}({c['reason']})" for c in x['chars']), '|', x['statement'][:60])


if __name__ == '__main__':
    main()
