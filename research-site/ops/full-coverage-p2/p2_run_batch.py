"""P2: unattended fetch + Codex extraction for one batch (chairman 2026-10-25: keep P2 running around the clock).

  .venv/Scripts/python.exe -X utf8 research-site/ops/full-coverage-p2/p2_run_batch.py b04 [--fetch-only] [--no-wait]

--fetch-only stops after step 1 (prefetch for Claude extraction); --no-wait ends at the quota guard
instead of sleeping, so Claude (Sonnet xhigh) can take the remaining tickers.

1. p2_fetch.py, then p2_retry.py when a fetch hit a server error (skipped when fetch.jsonl is complete).
2. p2_codex.py for every ticker with a report that has neither a codex-NN.json entry nor a company-facts file;
   when both accounts are at the quota guard, sleep until the earliest five-hour reset (+2 min) and go on.
Keeps the machine from idle sleep while it runs (SetThreadExecutionState; no setting is changed).
Writes nothing to company-facts: loading, verification and review stay with Claude. Log: out/{batch}/run.log.
"""
import ctypes
import json
import re
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PY = str(ROOT / '.venv/Scripts/python.exe')
batch = sys.argv[1]
FETCH_ONLY, NO_WAIT = '--fetch-only' in sys.argv, '--no-wait' in sys.argv
out = HERE / 'out' / batch
out.mkdir(parents=True, exist_ok=True)
ctypes.windll.kernel32.SetThreadExecutionState(0x80000000 | 0x00000001)  # ES_CONTINUOUS | ES_SYSTEM_REQUIRED


def log(msg):
    line = time.strftime('%m-%d %H:%M ') + msg
    print(line, flush=True)
    with (out / 'run.log').open('a', encoding='utf-8') as fh:
        fh.write(line + '\n')


def py(*args):
    return subprocess.run([PY, '-X', 'utf8', *args], cwd=ROOT, capture_output=True, text=True, encoding='utf-8', errors='replace')


def fetch_log():
    p = out / 'fetch.jsonl'
    return {json.loads(l)['ticker']: json.loads(l) for l in p.read_text(encoding='utf-8').splitlines() if l.strip()} if p.exists() else {}


rows = json.loads((HERE / 'batches' / f'{batch}.json').read_text(encoding='utf-8'))
if len(fetch_log()) < len(rows) or not (out / 'financials.json').exists():
    log('fetch start')
    r = py(str(HERE / 'p2_fetch.py'), batch)
    log(f'fetch rc={r.returncode} ' + (r.stdout or '')[-300:].replace('\n', ' | '))
if any(str(x).startswith('error') for v in fetch_log().values() for x in v.values()):
    r = py(str(HERE / 'p2_retry.py'), batch)
    log(f'retry rc={r.returncode} ' + (r.stdout or '')[-300:].replace('\n', ' | '))

for loop in range(0 if FETCH_ONLY else 12):
    done = set()
    for f in out.glob('codex-[0-9][0-9].json'):
        done |= set(json.loads(f.read_text(encoding='utf-8'))) - {'_notes'}
    todo = [r['ticker'] for r in rows if fetch_log().get(r['ticker'], {}).get('fy') and r['ticker'] not in done
            and not (ROOT / f"research-site/data/company-facts/{r['ticker']}.json").exists()]
    # a garbled text layer needs Claude (PyMuPDF re-extraction) first; Codex only skips it again
    garbled = [t for t in todo if json.loads((ROOT / f'research-site/data/annual-slices/{t}.json').read_text(encoding='utf-8')).get('garbled')]
    if garbled:
        log(f'garbled, left for Claude: {garbled}')
        todo = [t for t in todo if t not in garbled]
    if not todo:
        log('extraction complete')
        break
    log(f'codex round {loop + 1}: {len(todo)} tickers')
    r = subprocess.run([PY, '-X', 'utf8', str(HERE / 'p2_codex.py'), batch, *todo], cwd=ROOT,
                       capture_output=True, text=True, encoding='utf-8', errors='replace')
    log('codex: ' + ' | '.join(l[:90] for l in (r.stdout or '').splitlines()))
    if 'QUOTA' in (r.stdout or '') and NO_WAIT:
        log('quota: ending (--no-wait); remaining tickers left for Claude')
        break
    if 'QUOTA' in (r.stdout or ''):
        resets = []
        for home in (Path.home() / '.codex', Path.home() / '.codex-b'):
            for f in sorted((home / 'sessions').rglob('rollout-*.jsonl'), key=lambda p: p.stat().st_mtime)[-3:]:
                resets += [int(x) for x in re.findall(r'"resets_at":\s*(\d+)', f.read_text(encoding='utf-8', errors='replace'))]
        future = [t for t in resets if t > time.time()]
        wait = (min(future) - time.time() + 120) if future else 1800
        log(f'quota: sleeping {int(wait // 60)} min')
        time.sleep(max(60, wait))
else:
    if not FETCH_ONLY:
        log('stopped after 12 rounds; tickers left for Claude')
