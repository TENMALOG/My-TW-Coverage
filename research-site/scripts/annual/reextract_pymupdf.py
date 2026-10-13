"""Re-extract annual-report text with PyMuPDF when pypdf produced a garbled text layer.

  python research-site/scripts/annual/reextract_pymupdf.py 2415 3711 ...

Reads the cached raw PDF named in each mops-annual metadata file, writes the new text snapshot
(same '[PDF PAGE n]' layout as fetch_mops_annual.py) under its SHA256, and points the metadata at
it. The previous text path/hash are kept in `text_previous` and the extractor is recorded, so the
provenance of every excerpt stays traceable. A report is only switched when the new text is not
garbled by the same test slice_annual.py uses.
"""
from __future__ import annotations

import glob
import hashlib
import json
import sys
from pathlib import Path

import pymupdf

ROOT = Path(__file__).resolve().parents[3]
CACHE = ROOT / 'audit-v5/source-cache/research-site/mops-annual'
sys.path.insert(0, str(Path(__file__).resolve().parent))
from slice_annual import is_garbled  # noqa: E402


def main():
    for t in sys.argv[1:]:
        metas = sorted(glob.glob(str(CACHE / f'{t}_*_F04.json')))
        if not metas:
            print(t, 'no metadata')
            continue
        mp = Path(metas[-1])
        m = json.loads(mp.read_text(encoding='utf-8'))
        if m.get('text_extractor', '').startswith('pymupdf'):
            print(t, 'already pymupdf')
            continue
        doc = pymupdf.open(ROOT / m['raw_path'])
        text = '\n'.join(f'\n[PDF PAGE {i + 1}]\n' + p.get_text() for i, p in enumerate(doc))
        # lone UTF-16 surrogates cannot be stored as UTF-8
        text = ''.join('�' if '\ud800' <= c <= '\udfff' else c for c in text)
        if is_garbled(text):
            print(t, 'still garbled with pymupdf; unchanged')
            continue
        tb = text.encode('utf-8')
        h = hashlib.sha256(tb).hexdigest()
        (CACHE / f'{h}.txt').write_bytes(tb)
        m['text_previous'] = {'text_path': m['text_path'], 'text_sha256': m['text_sha256'],
                              'text_extractor': m.get('text_extractor', 'pypdf')}
        m['text_path'] = (CACHE / f'{h}.txt').relative_to(ROOT).as_posix()
        m['text_sha256'] = h
        m['text_characters'] = len(text)
        m['text_extractor'] = f'pymupdf {pymupdf.VersionBind}'
        mp.write_text(json.dumps(m, ensure_ascii=False, indent=2), encoding='utf-8')
        print(t, 'switched to pymupdf', len(text))


if __name__ == '__main__':
    main()
