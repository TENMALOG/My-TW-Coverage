"""Write the Quarto `book.chapters` list for all industries to research-site/_generated/book-chapters.yml.

Order: the existing front matter and 研究主文 part (copied unchanged from _quarto.yml), then one part per
industry in company-count order (industry chapter + its company pages; Aerospace & Defense keeps its
existing chapter and page order), then the existing trailing chapters (公司索引, 參考文獻).
research-site/_quarto.yml is never modified. `--merge-into PATH` writes a merged copy of a _quarto.yml
(refused for the repository's own file); `--industry` restricts the industry parts (for test renders).

  python research-site/scripts/generic/build_book_config.py [--industry FOLDER ...] [--merge-into COPY/_quarto.yml]
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from industries import AERO_FOLDER, SITE, companies, industry_names, ordered_industries  # noqa: E402

QUARTO = SITE / '_quarto.yml'
OUT = SITE / '_generated/book-chapters.yml'
INDUSTRY_PART = '產業專章'
AERO_PAGES_PART = '公司研究頁：航太與國防'


def parse_chapters(text: str):
    """Return (start, end, entries) of the book.chapters block. entries: ('file', path) | ('part', title, [paths])."""
    lines = text.splitlines()
    start = next(i for i, l in enumerate(lines) if re.match(r'^  chapters:\s*(#.*)?$', l))
    end = next(i for i in range(start + 1, len(lines)) if re.match(r'^  \S', lines[i]) or re.match(r'^\S', lines[i]))
    entries, cur = [], None
    for l in lines[start + 1:end]:
        s = l.split('#', 1)[0].rstrip() if not l.strip().startswith('- part:') else l.rstrip()
        m = re.match(r'^    - part:\s*"(.*)"\s*$', s) or re.match(r'^    - part:\s*(.*?)\s*$', s)
        if m:
            cur = ('part', m.group(1), [])
            entries.append(cur)
            continue
        m = re.match(r'^        - (\S+)\s*$', s)
        if m and cur:
            cur[2].append(m.group(1))
            continue
        m = re.match(r'^    - (\S+)\s*$', s)
        if m:
            cur = None
            entries.append(('file', m.group(1)))
    return start, end, entries


def build_entries(entries, industries_filter=None):
    names = industry_names()
    rows = companies()
    try:
        cut = next(i for i, e in enumerate(entries) if e[0] == 'part' and e[1] == INDUSTRY_PART)
    except StopIteration:
        raise SystemExit(f'_quarto.yml has no part "{INDUSTRY_PART}"')
    head = entries[:cut]
    aero_part = next((e for e in entries if e[0] == 'part' and e[1] == AERO_PAGES_PART), None)
    industry_part = entries[cut]
    tail = [e for e in entries[cut + 1:] if e is not aero_part]
    parts = []
    for folder, n in ordered_industries(rows):
        if industries_filter is not None and folder not in industries_filter and folder != AERO_FOLDER:
            continue
        slug = names[folder]['slug']
        if folder == AERO_FOLDER:
            chap = [p for p in industry_part[2] if p.endswith(f'/{slug}.qmd')] or [f'chapters/industries/{slug}.qmd']
            pages = aero_part[2] if aero_part else []
        else:
            chap = [f'chapters/industries/{slug}.qmd']
            pages = [f'chapters/companies/{r["ticker"]}.qmd'
                     for r in sorted((r for r in rows if r['industry_folder'] == folder), key=lambda r: r['ticker'])]
        parts.append(('part', f'{names[folder]["name_zh"]}', chap + pages))
    return head + parts + tail


def dump(entries) -> str:
    L = ['  chapters:   # 由 research-site/scripts/generic/build_book_config.py 產生']
    for e in entries:
        if e[0] == 'file':
            L.append(f'    - {e[1]}')
        else:
            L.append(f'    - part: "{e[1]}"')
            L.append('      chapters:')
            L += [f'        - {p}' for p in e[2]]
    return '\n'.join(L) + '\n'


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument('--industry', nargs='*', default=None, help='restrict industry parts (Aerospace & Defense is always kept)')
    ap.add_argument('--merge-into', default=None, help='a COPY of _quarto.yml to rewrite with the generated chapter list')
    ap.add_argument('--out', default=str(OUT))
    a = ap.parse_args(argv)
    text = QUARTO.read_text(encoding='utf-8')
    start, end, entries = parse_chapters(text)
    new = build_entries(entries, set(a.industry) if a.industry else None)
    block = dump(new)
    out = Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text('# book.chapters — generated; see README.md in this folder for how to merge.\n' + block,
                   encoding='utf-8', newline='\n')
    n_parts = sum(1 for e in new if e[0] == 'part')
    n_files = sum(1 if e[0] == 'file' else len(e[2]) for e in new)
    print(f'{out}: {n_parts} parts, {n_files} chapter files')
    if a.merge_into:
        target = Path(a.merge_into).resolve()
        if target == QUARTO.resolve():
            raise SystemExit('refusing to overwrite research-site/_quarto.yml; merge into a copy')
        t_text = target.read_text(encoding='utf-8')
        ts, te, _ = parse_chapters(t_text)
        tl = t_text.splitlines()
        target.write_text('\n'.join(tl[:ts]) + '\n' + block + '\n'.join(tl[te:]) + '\n', encoding='utf-8', newline='\n')
        print(f'merged into {target}')


if __name__ == '__main__':
    main()
