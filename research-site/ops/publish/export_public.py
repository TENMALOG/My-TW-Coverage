"""Build the public repository tree (fresh history) from this private working repo.

  python research-site/ops/publish/export_public.py <out_dir>

Copies only what may be published:
  research-site/ site sources (qmd, config, filters, assets, references), generator scripts, the catalog,
  verified data (company facts without verbatim excerpts, published relations, renames, financials,
  industry-analysis drafts), the rendered site (_site), the original reports under archive/, and
  LICENSE / NOTICE / README.
Never copied: audit-v5 caches, annual-report slices and snapshots, ops/ working files, raw original-project
sentence data, rejected or unverified facts, verbatim report excerpts (they may contain natural-person names).
Prints a manifest summary; run scan_public.py on the result before any push.
"""
import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SITE = ROOT / 'research-site'
HERE = Path(__file__).resolve().parent

SITE_DIRS = ['chapters', 'appendices', 'references', 'filters', 'assets', 'catalog', 'scripts', '_site']
SITE_FILES = ['_quarto.yml', 'index.qmd', 'index-companies.qmd', '.gitignore']
DATA_COPY = ['relations/listed_edges.csv', 'company-renames.json', 'financials', 'industry-analysis',
             'aerospace-defense']
FACT_KEYS = ['id', 'field', 'statement', 'period', 'page', 'attribution']


def rejected_ids() -> set:
    latest = {}
    for line in (SITE / 'data/company-facts/_semantic-review.jsonl').read_text(encoding='utf-8').splitlines():
        if line.strip():
            r = json.loads(line)
            latest[r['id']] = r['verdict']
    return {k for k, v in latest.items() if v == 'REJECT'}


def copy(src: Path, dst: Path):
    if src.is_dir():
        shutil.copytree(src, dst, ignore=shutil.ignore_patterns('__pycache__', '*.pyc', '.quarto', '*_files'))
    elif src.exists():
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)


def main(out: Path):
    if out.exists() and any(out.iterdir()):
        sys.exit(f'{out} is not empty')
    out.mkdir(parents=True, exist_ok=True)
    rs = out / 'research-site'
    for d in SITE_DIRS:
        copy(SITE / d, rs / d)
    for f in SITE_FILES:
        copy(SITE / f, rs / f)
    for d in DATA_COPY:
        copy(SITE / 'data' / d, rs / 'data' / d)

    # company facts: only PASS and not rejected, without verbatim excerpts or local paths
    rej = rejected_ids()
    kept = dropped = 0
    (rs / 'data/company-facts').mkdir(parents=True, exist_ok=True)
    for f in sorted((SITE / 'data/company-facts').glob('[0-9]*.json')):
        doc = json.loads(f.read_text(encoding='utf-8'))
        facts = []
        for x in doc['facts']:
            if (x.get('verification') or {}).get('status') == 'PASS' and x['id'] not in rej:
                facts.append({k: x[k] for k in FACT_KEYS if k in x})
                kept += 1
            else:
                dropped += 1
        src = doc['source']
        pub = {'ticker': doc['ticker'], 'company': doc['company'], 'legal_name': doc.get('legal_name', ''),
               'source': {'citation_url': src['citation_url'], 'fy': src.get('fy'), 'filename': src.get('filename')},
               'facts': facts}
        (rs / 'data/company-facts' / f.name).write_text(json.dumps(pub, ensure_ascii=False, indent=1) + '\n',
                                                         encoding='utf-8')

    copy(ROOT / 'Pilot_Reports', out / 'archive/original-reports')
    lic = (ROOT / 'LICENSE').read_text(encoding='utf-8')
    orig = 'Copyright (c) 2026 idk_mostoftime'
    assert orig in lic
    (out / 'LICENSE').write_text(lic.replace(orig, orig + '\nCopyright (c) 2026 股.tw 研究室'), encoding='utf-8')
    for name in ('NOTICE.md', 'README.md'):
        copy(HERE / name, out / name)
    print(json.dumps({'out': str(out), 'facts_kept': kept, 'facts_dropped': dropped}, ensure_ascii=False))


if __name__ == '__main__':
    main(Path(sys.argv[1]).resolve())
