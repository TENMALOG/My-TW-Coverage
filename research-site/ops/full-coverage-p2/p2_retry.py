"""P2: retry annual-report fetches that failed with a server error (not 'not_found') and slice only those.

  .venv/Scripts/python.exe -X utf8 research-site/ops/full-coverage-p2/p2_retry.py b01

Rewrites the failed lines of out/{batch}/fetch.jsonl (keeps the earlier errors under 'previous');
other slices are not touched, so extraction running on them is unaffected. 10 s between companies.
"""
import json
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT / 'research-site/scripts'))
import fetch_mops_annual as fma  # noqa: E402

batch = sys.argv[1]
log = HERE / 'out' / batch / 'fetch.jsonl'
rows = [json.loads(l) for l in log.read_text(encoding='utf-8').splitlines() if l.strip()]
retried = []
for r in rows:
    if r.get('fy') or not any(str(r.get(k, '')).startswith(('error', 'rate_limited')) for k in ('fy2025', 'fy2024')):
        continue
    prev = {k: r.pop(k) for k in ('fy2025', 'fy2024') if k in r}
    r['previous'] = prev
    for fy in (2025, 2024):
        try:
            m = fma.fetch(r['ticker'], fy)
        except Exception as exc:
            m = {'status': f'error {type(exc).__name__}: {exc}'[:200]}
        r[f'fy{fy}'] = m.get('status')
        if m.get('status') == 'captured':
            r.update({'fy': fy, 'filename': m['filename'], 'pages': m.get('pages')})
            retried.append(r['ticker'])
            break
        time.sleep(5)
    print(r['ticker'], r['company'], r.get('fy', '—'), r.get('fy2025'), r.get('fy2024', ''), flush=True)
    time.sleep(10)
log.write_text(''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in rows), encoding='utf-8')
if retried:
    subprocess.run([sys.executable, '-X', 'utf8', str(ROOT / 'research-site/scripts/annual/slice_annual.py'), '--tickers', *retried], cwd=ROOT, check=True)
print('captured on retry:', retried)
