"""Unattended Codex job queue across two accounts with quota guard.

  python research-site/ops/codex-review/codex_queue.py [--parallel 4] [--max-five-hour 85]

Jobs: research-site/ops/codex-review/jobs/*.txt (one fact id per line). For each job without a
finished output (out/{job}.jsonl with one valid line per id) a read-only `codex exec` is started on
whichever account has quota (five-hour usage below the limit, weekly below 95%). When both accounts
are at the limit the queue sleeps until the earliest reset and continues. Progress is appended to
queue.log. Safe to stop and restart at any time.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
JOBS, OUT = HERE / 'jobs', HERE / 'out'
TASK = HERE / 'codex_review_task.md'
HOMES = {'A': Path.home() / '.codex', 'B': Path.home() / '.codex-b'}
CODEX = str(Path(os.environ.get('APPDATA', '')) / 'npm' / 'codex.cmd')
LOG = HERE / 'queue.log'


def log(msg: str):
    line = f'{dt.datetime.now():%Y-%m-%d %H:%M:%S} {msg}'
    print(line, flush=True)
    with LOG.open('a', encoding='utf-8') as fh:
        fh.write(line + '\n')


def quota(home: Path) -> tuple[float, float, float]:
    """(five_hour %, weekly %, epoch when five-hour window resets) from the newest session log."""
    files = sorted((home / 'sessions').rglob('rollout-*.jsonl'), key=lambda p: p.stat().st_mtime, reverse=True)
    dec = json.JSONDecoder()
    for f in files[:50]:
        text = f.read_text(encoding='utf-8', errors='replace')
        for m in reversed(list(re.finditer(r'"rate_limits":', text))):
            try:
                rl, _ = dec.raw_decode(text, m.end())
            except json.JSONDecodeError:
                continue
            if isinstance(rl, dict) and rl.get('primary') and rl.get('secondary'):
                p, s = rl['primary'], rl['secondary']
                reset = p.get('resets_at') or 0
                five = p.get('used_percent', 0) if reset > time.time() else 0.0
                week = s.get('used_percent', 0) if (s.get('resets_at') or 0) > time.time() else 0.0
                return five, week, reset
    return 0.0, 0.0, 0


def job_ids(job: Path) -> list:
    if job.suffix == '.json':
        return [x['id'] for x in json.loads(job.read_text(encoding='utf-8'))]
    return job.read_text().split()


def done(job: Path) -> bool:
    out = OUT / f'{job.stem}.jsonl'
    if not out.exists():
        return False
    ids = job_ids(job)
    try:
        got = [json.loads(l)['id'] for l in out.read_text(encoding='utf-8').splitlines() if l.strip()]
    except (json.JSONDecodeError, KeyError):
        return False
    return got == ids


def run(job: Path, acct: str) -> bool:
    raw = OUT / f'{job.stem}.raw.txt'
    env = {**os.environ, 'CODEX_HOME': str(HOMES[acct])}
    prompt = (f'Read and follow the task file {TASK} exactly. Your id file is {job} . '
              'Your final message must be only the JSON Lines described in the task file.')
    if job.suffix == '.json':
        prompt = (f'Read and follow the task file {TASK} exactly. Your input file is {job} . '
                  'Your final message must be only the JSON Lines described in the task file.')
    cmd = [CODEX, 'exec', '--skip-git-repo-check', '--sandbox', 'read-only', '-c', 'windows.sandbox="unelevated"',
           '-o', str(raw), prompt]
    r = subprocess.run(cmd, cwd=ROOT, env=env, capture_output=True, text=True, encoding='utf-8', errors='replace')
    text = raw.read_text(encoding='utf-8', errors='replace') if raw.exists() else ''
    lines = []
    for l in text.splitlines():
        l = l.strip().strip('`')
        if l.startswith('{'):
            try:
                lines.append(json.loads(l))
            except json.JSONDecodeError:
                pass
    ids = job_ids(job)
    if [x.get('id') for x in lines] == ids:
        (OUT / f'{job.stem}.jsonl').write_text(''.join(json.dumps(x, ensure_ascii=False) + '\n' for x in lines), encoding='utf-8')
        log(f'{job.stem} OK acct={acct} flags={sum(1 for x in lines if str(x.get("verdict", x.get("action",""))) in ("REJECT","FIX","DROP") or str(x.get("verdict","")).startswith("REJECT"))}')
        return True
    if re.search(r'usage limit|rate limit', (r.stdout or '') + (r.stderr or '') + text, re.I):
        log(f'{job.stem} QUOTA acct={acct}')
    else:
        log(f'{job.stem} BAD acct={acct} got={len(lines)} want={len(ids)} rc={r.returncode}')
    return False


def main():
    global JOBS, OUT, TASK
    ap = argparse.ArgumentParser()
    ap.add_argument('--parallel', type=int, default=4, help='concurrent jobs per account')
    ap.add_argument('--max-five-hour', type=float, default=85)
    ap.add_argument('--jobs', default=str(JOBS))
    ap.add_argument('--out', default=str(OUT))
    ap.add_argument('--task', default=str(TASK))
    a = ap.parse_args()
    JOBS, OUT, TASK = Path(a.jobs), Path(a.out), Path(a.task)
    OUT.mkdir(exist_ok=True)
    fails: dict[str, int] = {}
    while True:
        todo = [j for j in sorted(list(JOBS.glob('*.txt')) + list(JOBS.glob('*.json'))) if not done(j) and fails.get(j.stem, 0) < 3]
        if not todo:
            log('queue empty')
            return
        usable = []
        for acct, home in HOMES.items():
            five, week, reset = quota(home)
            if five < a.max_five_hour and week < 95:
                usable.append(acct)
            log(f'acct={acct} five_hour={five}% weekly={week}%')
        if not usable:
            wake = min(quota(h)[2] for h in HOMES.values()) or time.time() + 1800
            secs = max(300, wake - time.time() + 120)
            log(f'all accounts at limit; sleeping {int(secs)}s')
            time.sleep(secs)
            continue
        wave = todo[: a.parallel * len(usable)]
        with ThreadPoolExecutor(max_workers=len(wave)) as ex:
            futs = {ex.submit(run, j, usable[i % len(usable)]): j for i, j in enumerate(wave)}
            for f, j in futs.items():
                if not f.result():
                    fails[j.stem] = fails.get(j.stem, 0) + 1


if __name__ == '__main__':
    main()
