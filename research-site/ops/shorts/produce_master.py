"""Batch: final 9:16 master for every company → out/master/{t}_youtube.mp4, {t}_web.mp4, out/meta/{t}.txt/.json

  py produce_master.py [--parallel 6] [--workers 3] [tickers...]

Resumable: a company is skipped when both videos and its meta exist and are newer than master.html and its
storyboard. Each company runs in its own process (record_master.py), so one failure never stops the batch.
Progress: out/master/produce.log (one line per company; FAIL lines carry the last error line).
"""
import argparse
import datetime as dt
import os
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / 'out' / 'master'
META = HERE / 'out' / 'meta'
LOG = OUT / 'produce.log'
ENV = {**os.environ, 'PYTHONIOENCODING': 'utf-8'}


def log(msg):
    line = f'{dt.datetime.now():%m-%d %H:%M:%S} {msg}'
    print(line, flush=True)
    with LOG.open('a', encoding='utf-8') as fh:
        fh.write(line + '\n')


def done(t):
    deps = [HERE / 'master.html', HERE / 'storyboard' / f'{t}.json']
    outs = [OUT / f'{t}_youtube.mp4', OUT / f'{t}_web.mp4', META / f'{t}.txt']
    return all(o.exists() for o in outs) and min(o.stat().st_mtime for o in outs) > max(d.stat().st_mtime for d in deps)


def one(t, workers):
    t0 = time.time()
    r = subprocess.run([sys.executable, 'record_master.py', 'video', t, str(workers)], cwd=HERE, env=ENV,
                       capture_output=True, text=True, encoding='utf-8', errors='replace')
    if r.returncode or not (OUT / f'{t}_youtube.mp4').exists():
        err = (r.stderr or r.stdout).strip().splitlines()[-1:] or ['?']
        log(f'{t} FAIL {err[0][:200]}')
        return False
    m = subprocess.run([sys.executable, 'youtube_meta.py', t], cwd=HERE, env=ENV, capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    if m.returncode:
        log(f'{t} META-FAIL {(m.stderr or "").strip().splitlines()[-1:]}')
        return False
    log(f'{t} OK {time.time() - t0:.0f}s')
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--parallel', type=int, default=6)
    ap.add_argument('--workers', type=int, default=3)
    ap.add_argument('tickers', nargs='*')
    a = ap.parse_args()
    OUT.mkdir(parents=True, exist_ok=True)
    META.mkdir(parents=True, exist_ok=True)
    allt = a.tickers or sorted(p.stem for p in (HERE / 'storyboard').glob('*.json') if p.stem.isdigit())
    todo = [t for t in allt if not done(t)]
    log(f'start: {len(todo)} to do of {len(allt)} (parallel {a.parallel} x workers {a.workers})')
    with ThreadPoolExecutor(a.parallel) as ex:
        ok = sum(ex.map(lambda t: one(t, a.workers), todo))
    log(f'finished: {ok}/{len(todo)} ok')


if __name__ == '__main__':
    main()
