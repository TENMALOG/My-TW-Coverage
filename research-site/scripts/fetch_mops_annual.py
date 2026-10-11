"""Fetch official annual reports (股東會年報, type F04) from MOPS doc.twse.com.tw and snapshot them.

  python research-site/scripts/fetch_mops_annual.py 2208 2634 ... [--fy 2025]

Snapshots go to audit-v5/source-cache/research-site/mops-annual/ (raw PDF + extracted text +
metadata with SHA256). The citation URL is the stable MOPS step=9 request for the filename.
"""
from __future__ import annotations

import argparse
import hashlib
import io
import json
import re
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CACHE = ROOT / 'audit-v5/source-cache/research-site/mops-annual'
BASE = 'https://doc.twse.com.tw'
UA = {'User-Agent': 'Mozilla/5.0 (compatible; TW-Coverage research)'}


def post(path, data):
    req = urllib.request.Request(BASE + path, data=urllib.parse.urlencode(data).encode(), headers=UA)
    return urllib.request.urlopen(req, timeout=60).read()


def sha(b):
    return hashlib.sha256(b).hexdigest()


def fetch(ticker, fy):
    meta_path = CACHE / f'{ticker}_{fy}_F04.json'
    if meta_path.exists():
        return json.loads(meta_path.read_text(encoding='utf-8'))
    listing = post('/server-java/t57sb01', {'step': '1', 'colorchg': '1', 'co_id': ticker, 'year': str(fy - 1911 + 1),
                                           'mtype': 'F', 'seamon': '', 'dtype': ''}).decode('big5', errors='replace')
    names = re.findall(rf'readfile2\("F","{ticker}","({fy}_{ticker}_\d+F04\.pdf)"\)', listing)
    if not names:
        return {'ticker': ticker, 'status': 'not_found', 'fy': fy}
    filename = names[-1]
    page = post('/server-java/t57sb01', {'step': '9', 'kind': 'F', 'co_id': ticker, 'filename': filename}).decode('big5', errors='replace')
    link = re.search(r"href='?\"?(/pdf/[^'\"> ]+\.pdf)", page)
    if not link:
        return {'ticker': ticker, 'status': 'no_pdf_link', 'filename': filename}
    raw = urllib.request.urlopen(urllib.request.Request(BASE + link.group(1), headers=UA), timeout=120).read()
    from pypdf import PdfReader
    pdf = PdfReader(io.BytesIO(raw))
    text = '\n'.join(f'\n[PDF PAGE {i+1}]\n' + (p.extract_text() or '') for i, p in enumerate(pdf.pages))
    CACHE.mkdir(parents=True, exist_ok=True)
    (CACHE / f'{sha(raw)}.pdf').write_bytes(raw)
    tb = text.encode('utf-8')
    (CACHE / f'{sha(tb)}.txt').write_bytes(tb)
    meta = {'ticker': ticker, 'fy': fy, 'status': 'captured', 'filename': filename,
            'citation_url': f'{BASE}/server-java/t57sb01?step=9&kind=F&co_id={ticker}&filename={filename}',
            'resolved_pdf_url': BASE + link.group(1), 'captured_at': datetime.now(timezone.utc).isoformat(),
            'raw_path': (CACHE / f'{sha(raw)}.pdf').relative_to(ROOT).as_posix(), 'raw_sha256': sha(raw),
            'text_path': (CACHE / f'{sha(tb)}.txt').relative_to(ROOT).as_posix(), 'text_sha256': sha(tb),
            'pages': len(pdf.pages), 'text_characters': len(text)}
    meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding='utf-8')
    return meta


def main():
    p = argparse.ArgumentParser()
    p.add_argument('tickers', nargs='+')
    p.add_argument('--fy', type=int, default=2025)
    a = p.parse_args()
    for t in a.tickers:
        try:
            m = fetch(t, a.fy)
        except Exception as exc:
            m = {'ticker': t, 'status': f'error {type(exc).__name__}: {exc}'}
        print(t, m.get('status'), m.get('filename', ''), m.get('pages', ''), m.get('text_characters', ''))


if __name__ == '__main__':
    main()
