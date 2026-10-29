"""Semantic review of the P2 Shorts scripts with Codex (second gate, review_task.md), accounts A/B in turn.

  .venv/Scripts/python.exe -X utf8 research-site/ops/shorts/run_review_p2.py [--parallel 3] [--per-run 4]

Each Codex run (workspace-write) reviews a few cout/pNNN.jsonl files and writes reviews/pNNN.jsonl; FIX lines are
re-validated by the reviewer with validate.py (which rewrites those storyboards). A job is done when its review file
has one line per company of its cout file; finished jobs are skipped, so the run can be restarted. Log:
reviews/p2-review.log.
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


def done(job):
    rv, co = HERE / 'reviews' / f'{job}.jsonl', HERE / 'cout' / f'{job}.jsonl'
    if not rv.exists():
        return False
    want = [json.loads(l)['id'] for l in co.read_text(encoding='utf-8').splitlines() if l.strip()]
    try:
        got = [json.loads(l)['id'] for l in rv.read_text(encoding='utf-8').splitlines() if l.strip()]
    except Exception:
        return False
    return got == want


def run(group):
    todo = [j for j in group if not done(j)]
    if not todo:
        return group, 'DONE (skipped)'
    if STOP.is_set():
        return group, 'SKIPPED'
    used, home = min((five_hour(h), h) for h in HOMES)
    if used >= 90:
        STOP.set()
        return group, f'QUOTA {used}%'
    files = ', '.join(f'research-site/ops/shorts/cout/{j}.jsonl' for j in todo)
    prompt = (f'Read and follow research-site/ops/shorts/review_task.md exactly. Review these script files: {files}. '
              'For each, write research-site/ops/shorts/reviews/<same name>.jsonl. Some companies cite prospectus facts '
              '(ids -PS-, base source kind "prospectus"): the same rules apply, with 公開說明書 in place of 年報. '
              'Put temporary files only under research-site/ops/shorts/work-review-p2/. Do not modify any other file. '
              'Final message: one line per file with counts of OK and FIX.')
    log = HERE / 'reviews' / f'{todo[0]}.codex.txt'
    r = subprocess.run([CODEX, 'exec', '--skip-git-repo-check', '--sandbox', 'workspace-write', '-c', 'windows.sandbox="unelevated"',
                        '-c', 'model="gpt-6.1-sol"', '-c', 'model_reasoning_effort="xhigh"', '-o', str(log), prompt],
                       cwd=ROOT, env={**os.environ, 'CODEX_HOME': str(home), 'PYTHONIOENCODING': 'utf-8'},
                       capture_output=True, text=True, encoding='utf-8', errors='replace')
    if re.search(r'out of credits|usage limit|rate limit', (r.stdout or '') + (r.stderr or ''), re.I):
        return group, f'QUOTA (error) {home.name}'
    missing = [j for j in todo if not done(j)]
    return group, (f'OK {home.name}' if not missing else f'INCOMPLETE {home.name}: {missing}')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--parallel', type=int, default=3)
    ap.add_argument('--per-run', type=int, default=4)
    a = ap.parse_args()
    jobs = sorted(p.stem for p in (HERE / 'cout').glob('p[0-9][0-9][0-9].jsonl'))
    groups = [jobs[i:i + a.per_run] for i in range(0, len(jobs), a.per_run)]
    print(f'{len(jobs)} script files in {len(groups)} review runs', flush=True)
    with ThreadPoolExecutor(max_workers=a.parallel) as pool:
        for group, status in pool.map(run, groups):
            line = f'{group[0]}-{group[-1]}: {status}'
            print(line, flush=True)
            with (HERE / 'reviews' / 'p2-review.log').open('a', encoding='utf-8') as fh:
                fh.write(line + '\n')


if __name__ == '__main__':
    main()
