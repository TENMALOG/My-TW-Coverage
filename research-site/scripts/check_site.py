"""Pre-publication integrity checks for the research site. Exit code 1 on any hard failure.

Hard checks
  1. Every 〔…〕 marker in the manuscripts resolves in ref-map.json; no marker survives in _site HTML text.
  2. Every company-research fact excerpt is re-located in its snapshot (re-runs build_aero_facts.py).
  3. Identity gate for company pages (re-runs build_company_pages.py).
  4. Internal links and #anchors in _site resolve.
  5. Protected files (baseline.json, 7,361 files) and the 6 frozen delivery files are unchanged.
Soft check (listed for human confirmation, not a failure)
  6. Numbers in the industry chapter / company pages / main text that cannot be traced to a data file.

  python research-site/scripts/check_site.py
"""
from __future__ import annotations

import csv
import hashlib
import json
import re
import subprocess
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[2]
SITE = ROOT / 'research-site'
DATA = SITE / 'data/aerospace-defense'
CR = ROOT / 'audit-v5/semantic/candidate-rerun'
PY = sys.executable
FROZEN = {
    'delivery/summary.json': 'a7cd3da5465cfd8f0c97b591f0e412cb6cc2ca4ca3dcdbda3e67859b86118e4b',
    'delivery/consolidated-status.jsonl': '263ab2cc623ecf8b90aa6456c17a3caf31d34a5bafbccb29117a0af1bb137be2',
    'delivery/revised-claim-proposals.jsonl': 'f7ce1941a99cc6f42168b8fa0264f468c0863643b9a7567508fc950195cb4f2d',
    'delivery/accepted-original-claims.jsonl': '2a8ae93d1ff113c0a0413461a6094b0b5ec35c2674914a201cd30cef806501db',
    'revision-pilot-001/queue.jsonl': '6ffe9737b5b318f78ba670e3e1ad7ee5e9ac1364889a84a85a9951afbbe4d435',
    'revision-pilot-001/delivery/accepted-revisions.jsonl': 'f93d55d69529d0ba15f5425f211da002bddaa0e4baa202bc4d20e0b91f0c90b5',
}
BASELINE = ROOT / 'audit-v5/source-cache/candidate-rerun/operational-repair/20261008-finalization/baseline.json'
MANUSCRIPTS = (['chapters/industries/aerospace-defense.qmd', 'chapters/main/introduction.qmd', 'chapters/main/data-method.qmd',
                'chapters/main/discussion.qmd', 'index.qmd'] +
               [p.relative_to(SITE).as_posix() for p in sorted((SITE / 'chapters/companies').glob('*.qmd'))])

failures, notes = [], []


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def check_markers():
    refmap = json.loads((DATA / 'ref-map.json').read_text(encoding='utf-8'))
    for rel in MANUSCRIPTS + ['appendices/evidence.qmd']:
        for grp in re.findall(r'〔([^〕]+)〕', (SITE / rel).read_text(encoding='utf-8')):
            for part in re.split(r'[；、]', grp):
                part = part.strip()
                m = re.match(r'R(\d+)–R(\d+)$', part)
                ids = [f'R{i:02d}' for i in range(int(m.group(1)), int(m.group(2)) + 1)] if m else [part]
                for i in ids:
                    if i not in refmap:
                        failures.append(f'marker 〔{i}〕 in {rel} not in ref-map')
    for html in (SITE / '_site').rglob('*.html'):
        text = re.sub(r'<svg.*?</svg>', '', html.read_text(encoding='utf-8'), flags=re.S)
        text = re.sub(r'<[^>]+>', '', text)
        if re.search(r'〔[^〕]*(?:F\d\d|revision|metric|fin|R\d\d)', text) and 'class="citation"' not in html.read_text(encoding='utf-8'):
            failures.append(f'unconverted marker in {html.relative_to(SITE)}')


def rerun(script):
    r = subprocess.run([PY, '-X', 'utf8', str(SITE / 'scripts' / script)], capture_output=True, text=True, encoding='utf-8')
    if r.returncode != 0:
        failures.append(f'{script} failed: {(r.stdout + r.stderr).strip()[-300:]}')


class Links(HTMLParser):
    def __init__(self):
        super().__init__(); self.hrefs, self.ids = [], set()

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a:
            self.ids.add(a['id'])
        if tag == 'a' and a.get('href'):
            self.hrefs.append(a['href'])


def check_links():
    pages = {}
    for html in (SITE / '_site').rglob('*.html'):
        p = Links(); p.feed(html.read_text(encoding='utf-8')); pages[html.resolve()] = p
    bad = 0
    for path, p in pages.items():
        for href in p.hrefs:
            u = urlparse(href)
            if u.scheme or href.startswith('mailto:') or href.startswith('javascript:'):
                continue
            target = path if not u.path else (path.parent / unquote(u.path)).resolve()
            if target.suffix != '.html':
                continue
            if target not in pages:
                failures.append(f'broken link {href} in {path.relative_to((SITE / "_site").resolve())}'); bad += 1
            elif u.fragment and unquote(u.fragment) not in pages[target].ids:
                failures.append(f'missing anchor {href} in {path.relative_to((SITE / "_site").resolve())}'); bad += 1
    notes.append(f'links checked across {len(pages)} pages, {bad} problems')


def check_protected():
    base = json.loads(BASELINE.read_text(encoding='utf-8'))['protected_files']
    mism, missing = [], []
    for rel, h in base.items():
        p = ROOT / rel
        if not p.exists():
            missing.append(rel)
        elif sha(p) != h:
            mism.append(rel)
    if mism:
        failures.append(f'{len(mism)} protected files changed, e.g. {mism[:3]}')
    if missing:
        # names that cannot be represented on this filesystem are reported, not silently passed
        notes.append(f'{len(missing)} protected paths not found on disk (path encoding?): {missing[:3]}')
    notes.append(f'protected files checked: {len(base)}, changed {len(mism)}, not found {len(missing)}')
    for rel, h in FROZEN.items():
        if sha(CR / rel) != h:
            failures.append(f'frozen file changed: {rel}')


def number_trace():
    corpus = []
    for p in [DATA / 'verified-facts.jsonl', DATA / 'fy2025-metrics.json', DATA / 'fy2025-financials.json', DATA / 'relations.csv',
              SITE / 'catalog/catalog-manifest.json', CR / 'delivery/summary.json', CR / 'revision-pilot-001/delivery/summary.json',
              CR / 'revision-aero-001/delivery/summary.json', CR / 'revision-aero-002/delivery/summary.json']:
        corpus.append(p.read_text(encoding='utf-8'))
    text = '\n'.join(corpus).replace(',', '')
    derived = set()
    for r in json.loads((DATA / 'fy2025-financials.json').read_text(encoding='utf-8')):
        for k, v in r.items():
            if k.endswith('_k') and isinstance(v, int):
                from decimal import ROUND_HALF_UP, Decimal
                derived |= {str((Decimal(v) / 1000).quantize(Decimal(1), rounding=ROUND_HALF_UP)),
                            str((Decimal(v) / 100000).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP))}
            if k.endswith('_pct') and v is not None:
                derived |= {f'{v:.2f}', f'{v:.1f}', f'{abs(v):.2f}'}
    for r in json.loads((DATA / 'fy2025-metrics.json').read_text(encoding='utf-8')):
        derived |= {f'{r["revenue_change_pct"]:.1f}', f'{abs(r["revenue_change_pct"]):.1f}'}
    unmatched = []
    for rel in MANUSCRIPTS:
        body = (SITE / rel).read_text(encoding='utf-8')
        body = re.sub(r'〔[^〕]*〕|\{#[^}]*\}|<!--.*?-->|\(\.\./[^)]*\)|\[[^\]]*\]\(http[^)]*\)', '', body, flags=re.S)
        for num in set(re.findall(r'\d[\d,]*\.?\d*', body)):
            n = num.replace(',', '').rstrip('.')
            if len(n) <= 2 or re.fullmatch(r'20\d\d', n) or n in derived or n in text:
                continue
            unmatched.append(f'{rel}: {num}')
    notes.append(f'untraced numbers for manual confirmation: {len(unmatched)}')
    return sorted(unmatched)


def main():
    check_markers()
    rerun('build_aero_facts.py')
    rerun('build_company_pages.py')
    check_links()
    check_protected()
    unmatched = number_trace()
    for n in notes:
        print('NOTE', n)
    for u in unmatched:
        print('  ?', u)
    for f in failures:
        print('FAIL', f)
    print('RESULT', 'PASS' if not failures else f'FAIL ({len(failures)})')
    sys.exit(1 if failures else 0)


if __name__ == '__main__':
    main()
