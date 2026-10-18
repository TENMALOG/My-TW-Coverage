"""Render the Quarto book in N parallel shards, then merge into research-site/_site.

  py research-site/scripts/render_parallel.py [--shards 16]

A single `quarto render` is sequential (~5 h for 1,841 pages). Each shard is a copy of the project sources
(without _site, ops, caches and the big data folders, which the pages do not read at render time) that
renders an interleaved slice of the chapter list. Every page carries the full book sidebar from
_quarto.yml, so pages rendered in different shards are identical to a single-process render.
Merging copies each shard's _site over the main one and unions the search indexes (search.json).
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
    a = ap.parse_args()
    files = chapters()
    n = a.shards
    # the bibliography page lists only works cited in the same render: keep it with every citing page in shard 0
    cites = [f for f in files if f == 'references.qmd' or re.search(r'\[@|〔', (SITE / f).read_text(encoding='utf-8'))]
    rest = [f for f in files if f not in cites]
    parts = [rest[i::n] for i in range(n)]
    parts[0] = cites + parts[0]
    print(f'{len(files)} pages in {n} shards', flush=True)
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
    # merge: fresh _site from shard outputs; search index = union by href
    out = SITE / '_site'
    if out.exists():
        shutil.rmtree(out)
    search = {}
    for d, part, _, _ in procs:
        # a shard writes placeholder pages (e.g. a self-redirecting index.html) for chapters it did not render:
        # copy only its own pages, plus every non-HTML resource
        mine = {f.replace('.qmd', '.html') for f in part}
        shutil.copytree(d / '_site', out, dirs_exist_ok=True,
                        ignore=lambda src, names, d=d, mine=mine: [
                            n for n in names if n.endswith('.html')
                            and Path(src, n).relative_to(d / '_site').as_posix() not in mine])
        for e in json.loads((d / '_site' / 'search.json').read_text(encoding='utf-8')):
            search[(e.get('objectID'), e.get('href'))] = e
    own = {f.replace('.qmd', '.html') for f in files}
    (out / 'search.json').write_text(json.dumps(list(search.values()), ensure_ascii=False), encoding='utf-8')
    html = sum(1 for _ in out.rglob('*.html'))
    print(f'merged into {out}: {html} html files, {len(search)} search entries, {int(time.time() - t0) // 60} min',
          flush=True)


if __name__ == '__main__':
    main()
