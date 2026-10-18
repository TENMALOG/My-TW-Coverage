"""Batch-produce company Shorts: silent master (out/{t}.mp4) + scored version (out/{t}_full.mp4).

  py produce_all.py [--parallel 4] [--workers 4] [tickers...]

Skips tickers whose _full.mp4 is newer than their storyboard, short.html and score.py, so it can be stopped
and restarted. Silent masters are kept: changing the mix later only needs `audio/score.py`, not a re-record.
Progress goes to produce.log.
"""
import argparse
import datetime as dt
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

HERE = Path(__file__).resolve().parent
LOG = HERE / 'produce.log'
PY = sys.executable


def log(msg):
    line = f'{dt.datetime.now():%H:%M:%S} {msg}'
    print(line, flush=True)
    with LOG.open('a', encoding='utf-8') as fh:
        fh.write(line + '\n')


def fresh(t):
    full = HERE / 'out' / f'{t}_full.mp4'
    deps = [HERE / 'storyboard' / f'{t}.json', HERE / 'short.html', HERE / 'audio' / 'score.py']
    return full.exists() and all(full.stat().st_mtime > d.stat().st_mtime for d in deps)


def one(t, workers):
    env = {'PYTHONIOENCODING': 'utf-8', **__import__('os').environ}
    r1 = subprocess.run([PY, 'record_short.py', 'video', t, str(workers)], cwd=HERE, env=env, capture_output=True, text=True)
    if r1.returncode:
        log(f'{t} RECORD FAIL {r1.stderr[-300:]!r}')
        return False
    r2 = subprocess.run([PY, 'score.py', t], cwd=HERE / 'audio', env=env, capture_output=True, text=True)
    if r2.returncode:
        log(f'{t} SCORE FAIL {r2.stderr[-300:]!r}')
        return False
    log(f'{t} OK')
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--parallel', type=int, default=4)
    ap.add_argument('--workers', type=int, default=4)
    ap.add_argument('tickers', nargs='*')
    a = ap.parse_args()
    todo = a.tickers or sorted(p.stem for p in (HERE / 'storyboard').glob('*.json'))
    todo = [t for t in todo if not fresh(t)]
    log(f'start {len(todo)} shorts, parallel {a.parallel} x workers {a.workers}')
    with ThreadPoolExecutor(a.parallel) as ex:
        ok = sum(ex.map(lambda t: one(t, a.workers), todo))
    log(f'done {ok}/{len(todo)}')


if __name__ == '__main__':
    main()
