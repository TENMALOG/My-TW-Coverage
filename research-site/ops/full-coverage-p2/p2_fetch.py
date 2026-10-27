"""P2: fetch annual reports (FY2025, else FY2024), slice them, and build the financial summary for one batch.

  .venv/Scripts/python.exe -X utf8 research-site/ops/full-coverage-p2/p2_fetch.py b01

Low frequency: one company at a time, 3 s between companies (fetch_mops_annual.py makes up to three
requests per report). Results: out/{batch}/fetch.jsonl, out/{batch}/financials.json; slices go to
research-site/data/annual-slices/ (legal name from the official directory when it occurs in the text).
"""
import json
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT / 'research-site/scripts'))
sys.path.insert(0, str(ROOT / 'research-site/scripts/annual'))
import fetch_mops_annual as fma  # noqa: E402
import build_financials_all as bfa  # noqa: E402

batch = sys.argv[1]
rows = json.loads((HERE / 'batches' / f'{batch}.json').read_text(encoding='utf-8'))
out = HERE / 'out' / batch
out.mkdir(parents=True, exist_ok=True)
log = out / 'fetch.jsonl'
done = {json.loads(l)['ticker'] for l in log.read_text(encoding='utf-8').splitlines() if l.strip()} if log.exists() else set()
for r in rows:
    t = r['ticker']
    if t in done:
        continue
    rec = {'ticker': t, 'company': r['company'], 'market': r['market']}
    for fy in (2025, 2024):
        for attempt in range(4):
            try:
                m = fma.fetch(t, fy)
                break
            except fma.RateLimited:
                time.sleep(60 * (2 ** attempt))  # MOPS said 查詢過量: back off, never hammer
            except Exception as exc:
                m = {'status': f'error {type(exc).__name__}: {exc}'[:200]}
                break
        else:
            m = {'status': 'rate_limited'}
        rec[f'fy{fy}'] = m.get('status')
        if m.get('status') == 'captured':
            rec.update({'fy': fy, 'filename': m['filename'], 'pages': m.get('pages')})
            break
        time.sleep(3)
    with log.open('a', encoding='utf-8') as fh:
        fh.write(json.dumps(rec, ensure_ascii=False) + '\n')
    print(t, r['company'], rec.get('fy', '—'), rec.get('fy2025'), rec.get('fy2024', ''), flush=True)
    time.sleep(3)

captured = [json.loads(l) for l in log.read_text(encoding='utf-8').splitlines() if l.strip()]
tickers = [r['ticker'] for r in captured if r.get('fy')]
if tickers:
    subprocess.run([sys.executable, '-X', 'utf8', str(ROOT / 'research-site/scripts/annual/slice_annual.py'), '--tickers', *tickers], cwd=ROOT, check=True)

data, sources = {}, {}
for year in (113, 114):
    for typek in ('sii', 'otc', 'rotc'):
        meta = bfa.fetch(typek, year, False)
        for tk, rec in bfa.parse_all(meta).items():
            data.setdefault(tk, {})[year] = (rec, typek)
            sources.setdefault(tk, {})[year] = meta
fin = []
for r in rows:
    tk = r['ticker']
    rec = {'ticker': tk, 'company': r['company'], 'market': r['market'],
           'basis': '合併綜合損益表彙總（公開資訊觀測站 t163sb04，第四季＝全年度）', 'years': {}}
    for year, label in ((113, '2024'), (114, '2025')):
        if year not in data.get(tk, {}):
            continue
        row, typek = data[tk][year]
        items = {k: bfa.num(v) for k, v in row['row'].items() if k not in ('公司代號', '公司名稱')}
        rev = items.get('營業收入')
        gp = next((items[g] for g in bfa.GROSS if items.get(g) is not None), None)
        oi = items.get('營業利益（損失）')
        m = sources[tk][year]
        rec['years'][label] = {'mops_company_name': row['row'].get('公司名稱'), 'typek': typek, 'table_kind': row['kind'], 'items_k': items,
                               'gross_margin_pct': round(gp / rev * 100, 2) if rev and gp is not None else None,
                               'operating_margin_pct': round(oi / rev * 100, 2) if rev and oi is not None else None,
                               'source': {'url': m['url'], 'post': m['post'], 'raw_sha256': m['raw_sha256'], 'captured_at': m['captured_at']}}
    rec['formula'] = 'margin = item / 營業收入 × 100，四捨五入至小數第二位'
    fin.append(rec)
(out / 'financials.json').write_text(json.dumps(fin, ensure_ascii=False, indent=1), encoding='utf-8')
print(f'{batch}: reports {len(tickers)}/{len(rows)}, financials {sum(1 for f in fin if f["years"])}/{len(rows)}')
