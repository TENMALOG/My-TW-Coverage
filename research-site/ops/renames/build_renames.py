"""Verify extracted company renames against the annual-report snapshots and write the rename table.

  python research-site/ops/renames/build_renames.py

Reads out/*.jsonl (Sonnet) and codex_out/*.jsonl (Codex). A rename is kept only when its excerpt
(whitespace-insensitive) is on the cited page or the next one, and a stated former name occurs on those
pages too. Writes research-site/data/company-renames.json {ticker: [rename, ...]} and prints rejects.
"""
import glob
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT / 'research-site/scripts/annual'))
from slice_annual import page_texts  # noqa: E402

FACTS = ROOT / 'research-site/data/company-facts'
OUT = ROOT / 'research-site/data/company-renames.json'


def squash(s):
    return re.sub(r'\s+', '', s or '')


rows = {}
for f in sorted(glob.glob(str(HERE / 'out/rn_*.jsonl'))) + sorted(glob.glob(str(HERE / 'codex_out/rn_*.jsonl'))):
    for line in Path(f).read_text(encoding='utf-8').splitlines():
        if line.strip():
            r = json.loads(line)
            rows[r['id']] = r

table, rejects = {}, []
for tk, r in sorted(rows.items()):
    renames = r.get('renames') or []
    if not renames:
        continue
    doc = json.loads((FACTS / f'{tk}.json').read_text(encoding='utf-8'))
    pages = page_texts((ROOT / doc['source']['text_path']).read_text(encoding='utf-8', errors='replace'))
    for x in renames:
        ex, page = squash(x.get('excerpt')), int(x.get('page') or 0)
        hay = squash(pages.get(page, '')) + squash(pages.get(page + 1, ''))
        why = []
        if len(ex) < 6 or ex not in hay:
            why.append('excerpt_not_on_page')
        if x.get('former_name') and squash(x['former_name']) not in hay:
            why.append('former_name_not_on_page')
        if not x.get('new_name'):
            why.append('no_new_name')
        if why:
            rejects.append((tk, x.get('former_name'), x.get('new_name'), why))
            continue
        table.setdefault(tk, []).append({
            'former_name': x.get('former_name', ''), 'new_name': x['new_name'], 'date_text': x.get('date_text', ''),
            'kind': x.get('kind', 'chinese'), 'page': page, 'excerpt': x['excerpt'],
            'source': doc['source']['citation_url'], 'fy': doc['source'].get('fy')})

OUT.write_text(json.dumps(table, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print(f'companies reviewed {len(rows)}; companies with renames {len(table)}; renames kept {sum(map(len, table.values()))}; rejected {len(rejects)}')
for x in rejects:
    print('REJECT', *x)
