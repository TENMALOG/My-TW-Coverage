"""Usage: prep_batches.py SCRATCH PREFIX SIZE INDUSTRY [INDUSTRY...] — slice pending tickers and write batch files."""
import csv, os, glob, json, subprocess, sys
S, prefix, size, inds = sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4:]
have = {os.path.basename(f).split('_')[0] for f in glob.glob('audit-v5/source-cache/research-site/mops-annual/*_F04.json')}
facts = {os.path.basename(f)[:4] for f in glob.glob('research-site/data/company-facts/[0-9]*.json')}
rows = [r for r in csv.DictReader(open('research-site/catalog/release-scope-companies.csv', encoding='utf-8-sig'))
        if r['industry_folder'] in inds and r['ticker'] in have and r['ticker'] not in facts]
T = [r['ticker'] for r in rows]; name = {r['ticker']: r['company'] for r in rows}
subprocess.run([sys.executable, '-X', 'utf8', 'research-site/scripts/annual/slice_annual.py', '--tickers', *T], capture_output=True)
ok, skip = [], []
for t in T:
    d = json.load(open(f'research-site/data/annual-slices/{t}.json', encoding='utf-8'))
    if d['garbled'] or int(d['fy']) < 2024:
        skip.append((t, name[t], 'garbled' if d['garbled'] else f"fy{d['fy']}"))
    else:
        ok.append((t, name[t], d['fy'], d['legal_name_source']))
batches = [ok[i:i + size] for i in range(0, len(ok), size)]
for i, b in enumerate(batches, 1):
    open(f'{S}/batch_{prefix}{i}.txt', 'w', encoding='utf-8').write(', '.join(f'{t} {n}' for t, n, fy, src in b) +
        ''.join(f'\nNOTE: {t} report is FY{fy} ({int(fy) - 1911}年度) — label periods accordingly.' for t, n, fy, src in b if fy != '2025'))
print('pending', len(T), 'ok', len(ok), 'batches', len(batches), 'skip', skip)
print('suspect names', [(t, n, src) for t, n, fy, src in ok if 'not_in_text' in src or src == 'cover_heuristic'])
