"""Prospectus rules v2: fetch the latest FINAL prospectus (公開說明書, MOPS kind B) for companies without an
annual report, snapshot it and write the source record the extractor copies.

  .venv/Scripts/python.exe -X utf8 research-site/ops/full-coverage-p2/prospectus/fetch_prospectus.py 7915 7924 ...

Drafts (labels containing 稿本) are never used. Among final documents filed in ROC years 114-115 the latest
filing month wins. Raw PDF, text (pypdf; PyMuPDF when pypdf is garbled) and metadata go to prospectus/cache/;
the source record goes to prospectus/sources/{ticker}.json. 6 s between MOPS requests; 查詢過量 backs off.
"""
from __future__ import annotations

import hashlib
import io
import json
import re
import sys
import time
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(ROOT / 'research-site/scripts/annual'))
from slice_annual import is_garbled  # noqa: E402

CACHE = HERE / 'cache'
SOURCES = HERE / 'sources'
BASE = 'https://doc.twse.com.tw'
UA = {'User-Agent': 'Mozilla/5.0 (compatible; TW-Coverage research)'}
ROW_RE = re.compile(r'<td[^>]*>([^<]{2,40})</td>\s*<td[^>]*>[^<]*</td>\s*<td[^>]*><a[^>]*readfile2\("B","(\w+)","([^"]+)"\)')


def post(data, tries=4):
    for i in range(tries):
        time.sleep(6)
        req = urllib.request.Request(BASE + '/server-java/t57sb01', data=urllib.parse.urlencode(data).encode(), headers=UA)
        body = urllib.request.urlopen(req, timeout=60).read()
        if '查詢過量'.encode('big5') not in body and '查詢過量'.encode() not in body:
            return body
        time.sleep(60 * (i + 1))
    raise RuntimeError('MOPS 查詢過量 after retries')


def sha(b):
    return hashlib.sha256(b).hexdigest()


def latest_final(ticker):
    docs = []
    for year in ('115', '114'):
        html = post({'step': '1', 'colorchg': '1', 'co_id': ticker, 'year': year, 'mtype': 'B', 'seamon': '', 'dtype': ''}).decode('big5', errors='replace')
        for label, co, fn in ROW_RE.findall(html):
            if co == ticker:
                docs.append({'label': label.strip(), 'filename': fn})
    finals = [d for d in docs if '稿本' not in d['label']]
    # filenames start with the filing month (yyyymm); later code (B07 after B06) breaks ties; newest first
    finals.sort(key=lambda d: (d['filename'][:6], d['filename']), reverse=True)
    return finals, docs


def fetch(ticker, legal_name):
    finals, listed = latest_final(ticker)
    if not finals:
        return {'ticker': ticker, 'status': 'no_final_prospectus', 'listed': listed}
    drafts = []
    for doc in finals:
        meta = fetch_one(ticker, legal_name, doc, listed, drafts)
        # MOPS can list a document as final while its cover says 稿本 (7934 B07): fall back to the next final
        if meta.get('status') != 'cover_says_draft':
            return meta
        drafts.append(doc['filename'])
    return {'ticker': ticker, 'status': 'no_final_prospectus', 'cover_says_draft': drafts, 'listed': listed}


def fetch_one(ticker, legal_name, doc, listed, skipped):
    fn = doc['filename']
    page = post({'step': '9', 'kind': 'B', 'co_id': ticker, 'filename': fn}).decode('big5', errors='replace')
    link = re.search(r"href='?\"?(/pdf/[^'\"> ]+\.pdf)", page)
    if not link:
        return {'ticker': ticker, 'status': 'no_pdf_link', 'filename': fn}
    raw = urllib.request.urlopen(urllib.request.Request(BASE + link.group(1), headers=UA), timeout=180).read()
    from pypdf import PdfReader
    pdf = PdfReader(io.BytesIO(raw))
    text = '\n'.join(f'\n[PDF PAGE {i + 1}]\n' + (p.extract_text() or '') for i, p in enumerate(pdf.pages))
    extractor = 'pypdf'
    if is_garbled(text):
        import pymupdf
        alt = '\n'.join(f'\n[PDF PAGE {i + 1}]\n' + p.get_text() for i, p in enumerate(pymupdf.open(stream=raw, filetype='pdf')))
        if not is_garbled(alt):
            text, extractor = alt, f'pymupdf {pymupdf.VersionBind}'
    # lone UTF-16 surrogates cannot be stored as UTF-8
    text = ''.join('�' if '\ud800' <= c <= '\udfff' else c for c in text)
    # the cover is often an image (7918); the 刊印目的 line is repeated on the summary pages that follow
    if '稿本' in ''.join(re.split(r'\[PDF PAGE \d+\]', text)[1:9]):
        return {'ticker': ticker, 'status': 'cover_says_draft', 'filename': fn}
    tb = text.encode('utf-8')
    CACHE.mkdir(parents=True, exist_ok=True)
    (CACHE / f'{sha(raw)}.pdf').write_bytes(raw)
    (CACHE / f'{sha(tb)}.txt').write_bytes(tb)
    meta = {'ticker': ticker, 'status': 'captured', 'doc_type': '公開說明書', 'doc_label': doc['label'], 'filename': fn,
            'filed_month': f'{fn[:4]}-{fn[4:6]}', 'listed_documents': listed, 'skipped_cover_draft': skipped,
            'citation_url': f'{BASE}/server-java/t57sb01?step=9&kind=B&co_id={ticker}&filename={fn}',
            'resolved_pdf_url': BASE + link.group(1), 'captured_at': datetime.now(timezone.utc).isoformat(),
            'raw_path': (CACHE / f'{sha(raw)}.pdf').relative_to(ROOT).as_posix(), 'raw_sha256': sha(raw),
            'text_path': (CACHE / f'{sha(tb)}.txt').relative_to(ROOT).as_posix(), 'text_sha256': sha(tb),
            'text_extractor': extractor, 'pages': len(pdf.pages), 'text_characters': len(text),
            'garbled': is_garbled(text)}
    (CACHE / f'{ticker}_{fn[:-4]}.json').write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding='utf-8')
    if not meta['garbled']:
        SOURCES.mkdir(exist_ok=True)
        src = {'ticker': ticker, 'legal_name': legal_name,
               'source': {k: meta[k] for k in ('doc_type', 'doc_label', 'filed_month', 'citation_url', 'filename', 'text_sha256', 'text_path')}}
        (SOURCES / f'{ticker}.json').write_text(json.dumps(src, ensure_ascii=False, indent=1), encoding='utf-8')
    return meta


def main():
    directory = {c['ticker']: c for c in json.loads((ROOT / 'research-site/data/official-directory.json').read_text(encoding='utf-8'))['companies']}
    for t in sys.argv[1:]:
        try:
            m = fetch(t, directory[t]['legal_name'])
        except Exception as exc:
            m = {'ticker': t, 'status': f'error {type(exc).__name__}: {exc}'}
        print(t, m.get('status'), m.get('doc_label', ''), m.get('filename', ''), m.get('pages', ''),
              m.get('text_extractor', ''), 'GARBLED' if m.get('garbled') else '', flush=True)


if __name__ == '__main__':
    main()
