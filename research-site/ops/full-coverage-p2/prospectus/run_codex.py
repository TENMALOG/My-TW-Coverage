"""Prospectus rules v2: read-only Codex extraction, one company per job, accounts A/B as in p2_codex.py.

  .venv/Scripts/python.exe -X utf8 research-site/ops/full-coverage-p2/prospectus/run_codex.py 7915 7924 ...

Outputs prospectus/out/codex-{ticker}.raw.txt and .json; new documents are written to
research-site/data/company-facts-prospectus/{ticker}.json (never overwritten). Log: prospectus/out/codex.log.
"""
import json
import os
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(HERE.parent))
from p2_codex import CODEX, HOMES, five_hour  # noqa: E402

OUT = HERE / 'out'
FACTS = ROOT / 'research-site/data/company-facts-prospectus'
TASK = HERE / 'extract_brief.md'


def run(ticker, name):
    used, home = min((five_hour(h), h) for h in HOMES)
    if used >= 90:
        return ticker, f'QUOTA {used}%'
    raw = OUT / f'codex-{ticker}.raw.txt'
    prompt = (f'Read and follow the task file {TASK} exactly. Ticker and short name: {ticker} = {name}. '
              'Your final message must be only the single JSON object described in the task file.')
    r = subprocess.run([CODEX, 'exec', '--skip-git-repo-check', '--sandbox', 'read-only', '-c', 'windows.sandbox="unelevated"',
                        '-c', 'model="gpt-6.1-sol"', '-c', 'model_reasoning_effort="xhigh"', '-o', str(raw), prompt],
                       cwd=ROOT, env={**os.environ, 'CODEX_HOME': str(home)}, capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    if re.search(r'out of credits|usage limit|rate limit', (r.stdout or '') + (r.stderr or ''), re.I):
        return ticker, f'QUOTA (error) {home.name}'
    text = raw.read_text(encoding='utf-8', errors='replace').strip().strip('`').removeprefix('json').strip() if raw.exists() else ''
    try:
        doc = json.loads(text)
    except Exception as exc:
        return ticker, f'BAD {home.name} rc={r.returncode} {type(exc).__name__}'
    (OUT / f'codex-{ticker}.json').write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding='utf-8')
    if ticker not in doc:
        return ticker, f'SKIPPED {home.name} notes={doc.get("_notes", "")[:300]}'
    dest = FACTS / f'{ticker}.json'
    if not dest.exists():
        dest.write_text(json.dumps(doc[ticker], ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    return ticker, f'OK {home.name} facts={len(doc[ticker]["facts"])} notes={doc.get("_notes", "")[:300]}'


if __name__ == '__main__':
    OUT.mkdir(exist_ok=True)
    FACTS.mkdir(parents=True, exist_ok=True)
    directory = {c['ticker']: c['short_name'] for c in json.loads((ROOT / 'research-site/data/official-directory.json').read_text(encoding='utf-8'))['companies']}
    with ThreadPoolExecutor(max_workers=4) as pool:
        for t, status in pool.map(lambda t: run(t, directory[t]), sys.argv[1:]):
            line = f'{t}: {status}'
            print(line, flush=True)
            with (OUT / 'codex.log').open('a', encoding='utf-8') as fh:
                fh.write(line + '\n')
