"""Write Shorts scripts for the P2 companies with Codex (read-only), accounts A/B as in full-coverage-p2/p2_codex.py.

  .venv/Scripts/python.exe -X utf8 research-site/ops/shorts/run_codex_p2.py [--parallel 3]

Jobs of 8 tickers (P2 companies with a base file) go to jobs/pNNN.txt; each Codex run follows codex_task.md and its
JSON Lines answer is saved as cout/pNNN.jsonl (raw answer in cout/pNNN.raw.txt). Finished jobs are skipped, so the
run can be restarted; when every account is at >= 90 % of its five-hour quota the queue stops. Log: cout/p2-codex.log.
"""
import argparse
import json
import os
import re
import subprocess
import sys
import threading
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT / 'research-site/ops/full-coverage-p2'))
from p2_codex import CODEX, HOMES, five_hour  # noqa: E402

STOP = threading.Event()


def tickers():
    out = []
    for b in range(1, 14):
        for r in json.loads((ROOT / f'research-site/ops/full-coverage-p2/batches/b{b:02d}.json').read_text(encoding='utf-8')):
            if (HERE / 'base' / f'{r["ticker"]}.json').exists():
                out.append(r['ticker'])
    return out


def run(job):
    ids = (HERE / 'jobs' / f'{job}.txt').read_text(encoding='utf-8').split()
    out = HERE / 'cout' / f'{job}.jsonl'
    if out.exists() and len([l for l in out.read_text(encoding='utf-8').splitlines() if l.strip()]) == len(ids):
        return job, 'DONE (skipped)'
    if STOP.is_set():
        return job, 'SKIPPED'
    used, home = min((five_hour(h), h) for h in HOMES)
    if used >= 90:
        STOP.set()
        return job, f'QUOTA {used}%'
    raw = HERE / 'cout' / f'{job}.raw.txt'
    prompt = (f'Read and follow research-site/ops/shorts/codex_task.md exactly. Your id file is '
              f'research-site/ops/shorts/jobs/{job}.txt. Your final message must be only the JSON Lines.')
    r = subprocess.run([CODEX, 'exec', '--skip-git-repo-check', '--sandbox', 'read-only', '-c', 'windows.sandbox="unelevated"',
                        '-c', 'model="gpt-6.1-sol"', '-c', 'model_reasoning_effort="xhigh"', '-o', str(raw), prompt],
                       cwd=ROOT, env={**os.environ, 'CODEX_HOME': str(home)}, capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    if re.search(r'out of credits|usage limit|rate limit', (r.stdout or '') + (r.stderr or ''), re.I):
        return job, f'QUOTA (error) {home.name}'
    lines = [l.strip() for l in (raw.read_text(encoding='utf-8', errors='replace') if raw.exists() else '').splitlines()
             if l.strip().startswith('{')]
    got = []
    for l in lines:
        try:
            got.append(json.loads(l)['id'])
        except Exception:
            return job, f'BAD JSON {home.name}'
    if got != ids:
        return job, f'BAD ids {home.name}: got {len(got)} of {len(ids)}'
    out.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    return job, f'OK {home.name}'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--parallel', type=int, default=3)
    a = ap.parse_args()
    ts = tickers()
    jobs = []
    for i in range(0, len(ts), 8):
        job = f'p{i // 8 + 1:03d}'
        f = HERE / 'jobs' / f'{job}.txt'
        if not f.exists():
            f.write_text('\n'.join(ts[i:i + 8]) + '\n', encoding='utf-8')
        jobs.append(job)
    print(f'{len(ts)} companies in {len(jobs)} jobs', flush=True)
    with ThreadPoolExecutor(max_workers=a.parallel) as pool:
        for job, status in pool.map(run, jobs):
            line = f'{job}: {status}'
            print(line, flush=True)
            with (HERE / 'cout' / 'p2-codex.log').open('a', encoding='utf-8') as fh:
                fh.write(line + '\n')


if __name__ == '__main__':
    main()
