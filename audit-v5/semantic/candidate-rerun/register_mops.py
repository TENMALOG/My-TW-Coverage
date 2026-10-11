#!/usr/bin/env python3
"""Register a research-site MOPS annual-report snapshot as a captured source in a batch cache.

  python register_mops.py --batch revision-batch-005 --ticker 8112 --fy 2025
Prints the citation URL to use in claude_write specs.
"""
import argparse, json
from run_revision_batch import BASE, CACHE_ROOT, digest

p = argparse.ArgumentParser(); p.add_argument('--batch', required=True); p.add_argument('--ticker', required=True); p.add_argument('--fy', default='2025')
a = p.parse_args()
m = json.loads((BASE / f'audit-v5/source-cache/research-site/mops-annual/{a.ticker}_{a.fy}_F04.json').read_text(encoding='utf-8'))
url = m['citation_url']
text = (BASE / m['text_path']).read_text(encoding='utf-8')
meta = {'url': url, 'captured_at': m.get('captured_at'), 'capture_method': 'research-site fetch_mops_annual (MOPS F04 PDF)',
        'resolved_url': m.get('resolved_pdf_url'), 'status': 'captured', 'kind': 'pdf', 'raw_path': m['raw_path'],
        'text_path': m['text_path'], 'raw_sha256': digest((BASE / m['raw_path']).read_bytes()),
        'text_sha256': digest(text.encode()), 'text_characters': len(text)}
out = CACHE_ROOT / a.batch / 'sources' / (digest(url.encode()) + '.json')
out.write_text(json.dumps(meta, ensure_ascii=False, indent=1), encoding='utf-8')
print(url)
