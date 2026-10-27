"""P2: read-only Codex extraction for part of a batch, with a quota guard; accounts A (~/.codex) and B (~/.codex-b) in turn.

  .venv/Scripts/python.exe -X utf8 research-site/ops/full-coverage-p2/p2_codex.py b01 TICKER [TICKER ...]

Tickers are run in jobs of 4, two at a time. Before each job the newest rollout of the account is read;
each job goes to the account with the lowest five-hour usage below 90 % (P2_CODEX_HOMES, default
".codex,.codex-b"); when every account is at >= 90 %, out of credits or hits a usage-limit error the queue
stops and the remaining tickers are listed for Claude. Outputs: out/{batch}/codex-{job}.json (one JSON object per
job, as in the P1 run) plus codex.log; load with handoff-20261013/tools/load_codex.py.
"""
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
TASK = ROOT / 'research-site/ops/handoff-20261013/tools/codex_extract_task.md'
RULES = ROOT / 'research-site/ops/handoff-20261013/tools/review_rules_v4.md'
# chairman 2026-10-25: Codex first, accounts A and B in turn (both on gpt-6.1-sol xhigh)
HOMES = [Path.home() / h for h in os.environ.get('P2_CODEX_HOMES', '.codex,.codex-b').split(',')]
CODEX = str(Path(os.environ.get('APPDATA', '')) / 'npm' / 'codex.cmd')
STOP = threading.Event()


def five_hour(home):
    files = sorted((home / 'sessions').rglob('rollout-*.jsonl'), key=lambda p: p.stat().st_mtime, reverse=True)[:5]
    for f in files:
        t = f.read_text(encoding='utf-8', errors='replace')
        # an "out of credits" rollout older than the five-hour window says nothing about the quota now
        if re.search(r'out of credits', t, re.I):
            import time
            return 100.0 if time.time() - f.stat().st_mtime < 5 * 3600 else 0.0
        rl = None
        for m in re.finditer(r'"rate_limits":', t):
            try:
                rl, _ = json.JSONDecoder().raw_decode(t, m.end())
            except Exception:
                pass
        if rl and rl.get('primary'):
            import time
            p = rl['primary']
            return p.get('used_percent', 0) if (p.get('resets_at') or 0) > time.time() else 0.0
    return 0.0


def run(batch, job, pairs, names):
    out = HERE / 'out' / batch
    if STOP.is_set():
        return job, 'SKIPPED', [t for t, _ in pairs]
    used, home = min((five_hour(h), h) for h in HOMES)
    if used >= 90:
        STOP.set()
        return job, f'QUOTA {used}%', [t for t, _ in pairs]
    raw = out / f'codex-{job}.raw.txt'
    lst = '; '.join(f'{t} = {names[t]}' for t, _ in pairs)
    prompt = (f'Read and follow the task file {TASK} exactly; also apply the extraction-relevant rules in {RULES} '
              f'(money needs currency and unit; statement no wider than its excerpts; keep scope limits; name related parties; '
              f'a registered business-scope list is not the main products; no 合計 denominator without a total row; '
              f'skip figures the report contradicts; skip names with suspicious glyphs). Batch tickers and short names: {lst}. '
              'Your final message must be only the single JSON object described in the task file.')
    env = {**os.environ, 'CODEX_HOME': str(home)}
    # chairman 2026-10-24: run account B's extraction on the same model/effort as account A (per job only;
    # ~/.codex-b/config.toml stays unchanged because other projects share that account)
    r = subprocess.run([CODEX, 'exec', '--skip-git-repo-check', '--sandbox', 'read-only', '-c', 'windows.sandbox="unelevated"',
                        '-c', 'model="gpt-6.1-sol"', '-c', 'model_reasoning_effort="xhigh"',
                        '-o', str(raw), prompt], cwd=ROOT, env=env, capture_output=True, text=True, encoding='utf-8', errors='replace')
    blob = (r.stdout or '') + (r.stderr or '')
    if re.search(r'out of credits|usage limit|rate limit', blob, re.I):
        if len(HOMES) > 1:
            HOMES.remove(home)
            return run(batch, job, pairs, names)
        STOP.set()
        return job, f'QUOTA (error) {home.name}', [t for t, _ in pairs]
    text = raw.read_text(encoding='utf-8', errors='replace').strip().strip('`').removeprefix('json').strip() if raw.exists() else ''
    try:
        doc = json.loads(text)
        (out / f'codex-{job}.json').write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding='utf-8')
        got = sorted(set(doc) - {'_notes'})
        return job, f'OK {home.name} notes={doc.get("_notes", "")[:300]}', [t for t, _ in pairs if t not in got]
    except Exception as exc:
        return job, f'BAD {home.name} rc={r.returncode} {type(exc).__name__}', [t for t, _ in pairs]


if __name__ == '__main__':
    batch, tickers = sys.argv[1], sys.argv[2:]
    rows = {r['ticker']: r for r in json.loads((HERE / 'batches' / f'{batch}.json').read_text(encoding='utf-8'))}
    names = {t: rows[t]['company'] for t in tickers}
    # a rerun numbers its jobs after the existing outputs, so earlier codex-NN.json files are never overwritten
    base = max([int(p.name[6:8]) for p in (HERE / 'out' / batch).glob('codex-[0-9][0-9].*')], default=0)
    jobs = [(f'{base + i // 4 + 1:02d}',[(t, names[t]) for t in tickers[i:i + 4]]) for i in range(0, len(tickers), 4)]
    left = []
    with ThreadPoolExecutor(max_workers=2) as pool:
        for job, status, missing in pool.map(lambda j: run(batch, j[0], j[1], names), jobs):
            line = f'{batch} job {job}: {status} | not done: {missing}'
            print(line, flush=True)
            with (HERE / 'out' / batch / 'codex.log').open('a', encoding='utf-8') as fh:
                fh.write(line + '\n')
            left += missing
    print('FOR CLAUDE:', ' '.join(left))
