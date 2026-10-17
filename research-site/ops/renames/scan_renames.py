"""Find annual-report pages that mention a company name change, per listed company.

  python research-site/ops/renames/scan_renames.py

Writes research-site/ops/renames/candidates.json: one entry per company with the pages (1-based, as
split_pages numbers them) whose text mentions 更名 / 名稱變更 / 原名 etc., plus short snippets.
Also splits the companies into job files jobs/rn_NNN.json (about 40 companies each) for review.
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

PAT = re.compile(r'更名|改名|原名|名稱變更|變更名稱|更改名稱|變更公司名稱|更改公司名稱|公司名稱由|名稱改為|易名')
out = []
for f in sorted(glob.glob(str(ROOT / 'research-site/data/company-facts/[0-9]*.json'))):
    d = json.loads(Path(f).read_text(encoding='utf-8'))
    tp = ROOT / d['source']['text_path']
    if not tp.exists():
        continue
    pages = page_texts(tp.read_text(encoding="utf-8", errors="replace"))
    hits = []
    for i, p in sorted(pages.items()):
        snips = []
        for m in PAT.finditer(p):
            snips.append(re.sub(r'\s+', ' ', p[max(0, m.start() - 60):m.end() + 60]))
        if snips:
            hits.append({'page': i, 'snippets': snips[:4]})
    if hits:
        out.append({'ticker': d['ticker'], 'company': d['company'], 'legal_name': d.get('legal_name', ''),
                    'fy': d['source'].get('fy'), 'hits': hits[:12]})
(HERE / 'candidates.json').write_text(json.dumps(out, ensure_ascii=False, indent=0), encoding='utf-8')
jobs = HERE / 'jobs'
jobs.mkdir(exist_ok=True)
for k in range(0, len(out), 40):
    (jobs / f'rn_{k // 40:03d}.json').write_text(json.dumps(out[k:k + 40], ensure_ascii=False, indent=0), encoding='utf-8')
print(len(out), 'companies with candidate pages;', sum(len(x['hits']) for x in out), 'pages;', (len(out) + 39) // 40, 'jobs')
