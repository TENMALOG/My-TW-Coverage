"""Render the Quarto book in N parallel shards, then merge into research-site/_site.

  py research-site/scripts/render_parallel.py [--shards 16]
  py research-site/scripts/render_parallel.py --files list.txt [--shards 8]   re-render only the listed .qmd

A single `quarto render` is sequential (~5 h for 1,841 pages). Each shard is a copy of the project sources
(without _site, ops, caches and the big data folders, which the pages do not read at render time) that
renders an interleaved slice of the chapter list. Every page carries the full book sidebar from
_quarto.yml, so pages rendered in different shards are identical to a single-process render.
Merging copies each shard's _site over the main one and unions the search indexes (search.json).
With --files the existing _site is kept: only the listed pages and their search entries are replaced. Use it only
when _quarto.yml changes reach no other page (sidebar titles, chapter list) — otherwise render the whole book.
"""
import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

SITE = Path(__file__).resolve().parents[1]                     # research-site
WORK = SITE.parents[4] / 'render-shards'                       # outside the repo
QUARTO = Path(os.environ['LOCALAPPDATA']) / 'Programs/quarto-1.10.18/bin/quarto.exe'
SKIP = {'_site', 'ops', '.quarto', 'site_libs', 'index.html', 'data'}
DATA_NEEDED = ['aerospace-defense']                              # read by filters/refs.lua


def chapters():
    files = re.findall(r'^\s*-\s+(\S+\.qmd)\s*$', (SITE / '_quarto.yml').read_text(encoding='utf-8'), re.M)
    seen, out = set(), []
    for f in files:
        if f not in seen and (SITE / f).exists():
            seen.add(f); out.append(f)
    return out


def make_copy(dst):
    if dst.exists():
        shutil.rmtree(dst)
    dst.mkdir(parents=True)
    for p in SITE.iterdir():
        if p.name in SKIP:
            continue
        (shutil.copytree if p.is_dir() else shutil.copy2)(p, dst / p.name)
    for d in DATA_NEEDED:
        shutil.copytree(SITE / 'data' / d, dst / 'data' / d)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--shards', type=int, default=16)
    ap.add_argument('--merge-only', action='store_true', help='merge finished shards (driver process gone)')
    ap.add_argument('--files', help='text file of .qmd paths (relative to research-site/) to re-render into the existing _site')
    a = ap.parse_args()
    if a.merge_only:
        return merge_only()
    n = a.shards
    if a.files:
        files = [f.strip().replace('\\', '/').removeprefix('research-site/')
                 for f in Path(a.files).read_text(encoding='utf-8').splitlines() if f.strip()]
        absent = [f for f in files if not (SITE / f).is_file()]
        if absent or 'references.qmd' in files or not (SITE / '_site' / 'index.html').exists():
            raise SystemExit(f'--files needs an existing _site and listed sources (absent: {absent[:3]}); '
                             'references.qmd needs a full render')
        n = min(n, len(files))
        parts = [files[i::n] for i in range(n)]
    else:
        files = chapters()
        # the bibliography page lists only works cited in the same render: keep it with every citing page in shard 0
        cites = [f for f in files if f == 'references.qmd' or re.search(r'\[@|〔', (SITE / f).read_text(encoding='utf-8'))]
        rest = [f for f in files if f not in cites]
        parts = [rest[i::n] for i in range(n)]
        parts[0] = cites + parts[0]
    print(f'{len(files)} pages in {n} shards', flush=True)
    for old in WORK.glob('s[0-9][0-9]'):  # stale shards from an earlier run would be merged by --merge-only
        shutil.rmtree(old)
    WORK.mkdir(parents=True, exist_ok=True)
    (WORK / 'mode.txt').write_text('overlay' if a.files else 'full', encoding='utf-8')
    procs = []
    for i, part in enumerate(parts):
        d = WORK / f's{i:02d}'
        make_copy(d)
        (d / 'files.txt').write_text('\n'.join(part), encoding='utf-8')
        log = open(d / 'render.log', 'w', encoding='utf-8')
        procs.append((d, part, log, subprocess.Popen([str(QUARTO), 'render', *part, '--to', 'html'], cwd=d,
                                                     stdout=log, stderr=subprocess.STDOUT)))
    t0 = time.time()
    while any(p.poll() is None for *_, p in procs):
        time.sleep(60)
        done = sum(sum(1 for f in part if (d / '_site' / f.replace('.qmd', '.html')).exists()) for d, part, _, _ in procs)
        print(f'{int(time.time() - t0) // 60:>3} min  {done}/{len(files)} pages', flush=True)
    bad = [(d.name, p.returncode) for d, _, _, p in procs if p.returncode != 0]
    missing = [f for d, part, _, _ in procs for f in part if not (d / '_site' / f.replace('.qmd', '.html')).exists()]
    print('failed shards', bad, 'missing pages', len(missing), missing[:10], flush=True)
    if bad or missing:
        sys.exit(1)
    merge([(d, part) for d, part, _, _ in procs], t0, overlay=bool(a.files))


def merge(shards, t0=None, overlay=False):
    """Fresh _site from shard outputs (each shard's own pages + all non-HTML resources); search index = union.
    overlay: keep the existing _site and replace only the shards' pages and those pages' search entries."""
    t0 = t0 or time.time()
    out = SITE / '_site'
    search = {}
    if overlay:
        pages = {f.replace('.qmd', '.html') for _, part in shards for f in part}
        for e in json.loads((out / 'search.json').read_text(encoding='utf-8')):
            if (e.get('href') or '').split('#')[0] not in pages:
                search[(e.get('objectID'), e.get('href'))] = e
    elif out.exists():
        shutil.rmtree(out)
    for d, part in shards:
        # a shard writes placeholder pages (e.g. a self-redirecting index.html) for chapters it did not render
        mine = {f.replace('.qmd', '.html') for f in part}
        shutil.copytree(d / '_site', out, dirs_exist_ok=True,
                        ignore=lambda src, names, d=d, mine=mine: [
                            n for n in names if n.endswith('.html')
                            and Path(src, n).relative_to(d / '_site').as_posix() not in mine])
        for e in json.loads((d / '_site' / 'search.json').read_text(encoding='utf-8')):
            if not overlay or (e.get('href') or '').split('#')[0] in mine:
                search[(e.get('objectID'), e.get('href'))] = e
    (out / 'search.json').write_text(json.dumps(list(search.values()), ensure_ascii=False), encoding='utf-8')
    html = sum(1 for _ in out.rglob('*.html'))
    print(f'merged into {out}: {html} html files, {len(search)} search entries, {int(time.time() - t0) // 60} min',
          flush=True)


def merge_only():
    """Merge finished shards when the driver process is gone (e.g. the session ended mid-render)."""
    shards = []
    for d in sorted(WORK.glob('s[0-9][0-9]')):
        part = (d / 'files.txt').read_text(encoding='utf-8').split()
        missing = [f for f in part if not (d / '_site' / f.replace('.qmd', '.html')).exists()]
        if missing:
            raise SystemExit(f'{d.name}: {len(missing)} pages not rendered yet, e.g. {missing[:3]}')
        shards.append((d, part))
    mode = WORK / 'mode.txt'
    merge(shards, overlay=mode.exists() and mode.read_text(encoding='utf-8').strip() == 'overlay')


if __name__ == '__main__':
    main()
