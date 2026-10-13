"""OCR annual reports whose PDF text layer is unusable (garbled even with PyMuPDF).

  python research-site/scripts/annual/ocr_annual.py 2441 3576 ...

Each page of the cached raw PDF is rendered at 200 dpi (PyMuPDF) and read by the built-in Windows
OCR engine (zh-Hant-TW, winocr.ps1). The page texts are joined in the usual '[PDF PAGE n]' layout;
the only cleanup is removing the single spaces the engine puts between two CJK characters. The
snapshot is stored under its SHA256 and the metadata points at it, keeping the previous text in
`text_previous` and recording the extractor. Page images stay in audit-v5/source-cache/.../ocr-pages
so every OCR'd excerpt can be checked against the image.
"""
from __future__ import annotations

import glob
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

import pymupdf

ROOT = Path(__file__).resolve().parents[3]
CACHE = ROOT / 'audit-v5/source-cache/research-site/mops-annual'
PAGES = ROOT / 'audit-v5/source-cache/research-site/ocr-pages'
PS1 = Path(__file__).resolve().parent / 'winocr.ps1'
CJK = r'[　-〿一-鿿＀-￯]'
EXTRACTOR = 'windows-ocr zh-Hant-TW (pymupdf render 200dpi; spaces between CJK removed)'


def main():
    for t in sys.argv[1:]:
        mp = Path(sorted(glob.glob(str(CACHE / f'{t}_*_F04.json')))[-1])
        m = json.loads(mp.read_text(encoding='utf-8'))
        if m.get('text_extractor', '').startswith('windows-ocr'):
            print(t, 'already OCR')
            continue
        out = PAGES / t
        out.mkdir(parents=True, exist_ok=True)
        doc = pymupdf.open(ROOT / m['raw_path'])
        for i, page in enumerate(doc):
            png = out / f'p{i + 1:04d}.png'
            if not png.exists():
                page.get_pixmap(dpi=200).save(png)
        subprocess.run(['powershell', '-NoProfile', '-ExecutionPolicy', 'Bypass', '-File', str(PS1), str(out)], check=True)
        parts = []
        for i in range(len(doc)):
            txt = (out / f'p{i + 1:04d}.txt').read_text(encoding='utf-8')
            txt = re.sub(rf'(?<={CJK}) (?={CJK})', '', txt)
            parts.append(f'\n[PDF PAGE {i + 1}]\n' + txt)
        text = '\n'.join(parts)
        tb = text.encode('utf-8')
        h = hashlib.sha256(tb).hexdigest()
        (CACHE / f'{h}.txt').write_bytes(tb)
        m['text_previous'] = {'text_path': m['text_path'], 'text_sha256': m['text_sha256'],
                              'text_extractor': m.get('text_extractor', 'pypdf')}
        m['text_path'] = (CACHE / f'{h}.txt').relative_to(ROOT).as_posix()
        m['text_sha256'] = h
        m['text_characters'] = len(text)
        m['text_extractor'] = EXTRACTOR
        m['ocr_pages_dir'] = out.relative_to(ROOT).as_posix()
        mp.write_text(json.dumps(m, ensure_ascii=False, indent=2), encoding='utf-8')
        print(t, 'OCR pages', len(doc), 'chars', len(text))


if __name__ == '__main__':
    main()
