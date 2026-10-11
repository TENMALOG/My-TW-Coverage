#!/usr/bin/env python3
"""Preserve OCR observations and assemble table rows by their image position."""
import argparse
import hashlib
import json
from pathlib import Path
from datetime import datetime, timezone

BASE = Path(__file__).resolve().parents[3]
CACHE = BASE/'audit-v5/source-cache/candidate-rerun/adjudication'


def digest(data):
    return hashlib.sha256(data).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('claim_id'); ap.add_argument('page', type=int)
    ap.add_argument('image'); ap.add_argument('observations'); args = ap.parse_args()
    pilot = Path(__file__).resolve().parent/'revision-pilot-001'
    rows = [json.loads(x) for x in (pilot/'adjudication/results.jsonl').read_text().splitlines()]
    row = next(r for r in reversed(rows) if r['claim_id']==args.claim_id)
    url = row['acceptance_hold_reasons'][0].split(': ', 1)[1]
    source = next(c for c in row['source_captures'] if c['url']==url)
    if digest(Path(source['raw_path']).read_bytes()) != source['raw_sha256']:
        raise ValueError('Original PDF changed')
    observations = json.loads(Path(args.observations).read_text())
    grouped = []
    for o in sorted(observations, key=lambda x: -(x['bounds'][1]+x['bounds'][3]/2)):
        y = o['bounds'][1]+o['bounds'][3]/2
        group = next((g for g in grouped if abs(g[0]-y)<0.011), None)
        if group is None:
            group = [y, []]; grouped.append(group)
        group[1].append(o)
    text = '[PDF PAGE '+str(args.page)+'; OCR-derived partial page]\n'
    text += '\n'.join(' '.join(o['text'] for o in sorted(g[1], key=lambda x: x['bounds'][0])) for g in grouped)+'\n'
    # Copy exact bytes to content-addressed files; never correct OCR words or digits.
    directory = CACHE/'ocr-sources'; directory.mkdir(exist_ok=True)
    meta = {'url': url, 'resolved_url': source['resolved_url'], 'captured_at': datetime.now(timezone.utc).isoformat(),
            'status': 'captured', 'kind': 'pdf_page_ocr', 'capture_method': 'macOS.Vision_VNRecognizeTextRequest',
            'partial_document': True, 'pdf_page': args.page, 'raw_path': source['raw_path'], 'raw_sha256': source['raw_sha256'],
            'original_extracted_text_path': source['text_path'], 'original_extracted_text_sha256': source['text_sha256'],
            'text_characters': len(text), 'ocr_requires_visual_review': True}
    blobs = {'image': (Path(args.image).read_bytes(), '.png'),
             'observations': (Path(args.observations).read_bytes(), '.json'),
             'ocr_code': (Path(__file__).with_name('ocr_revision_page.swift').read_bytes(), '.swift'),
             'assembly_code': (Path(__file__).read_bytes(), '.py'), 'text': (text.encode(), '.txt')}
    for kind, (data, suffix) in blobs.items():
        path = directory/(digest(data)+suffix)
        if path.exists() and path.read_bytes()!=data:
            raise ValueError('Content address collision')
        path.write_bytes(data); meta[kind+'_path'] = str(path); meta[kind+'_sha256'] = digest(data)
    destination = directory/(digest(url.encode())+'.json')
    if destination.exists():
        raise ValueError('OCR supplement already exists; preserve prior record')
    destination.write_text(json.dumps(meta, ensure_ascii=False, indent=2)+'\n')
    print(text)


if __name__ == '__main__':
    main()
