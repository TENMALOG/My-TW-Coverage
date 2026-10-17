import json, re, sys, os
ids = [l.strip() for l in open('research-site/ops/qa-audit4/ids_043.txt', encoding='utf8') if l.strip()]
lo, hi = int(sys.argv[1]), int(sys.argv[2])
cache = {}
sel=[a for a in sys.argv[3:] if a.startswith("2") or a.startswith("3")]
for i in (sel or ids[lo:hi]):
    t = i.split('-AR-')[0]
    d = json.load(open(f'research-site/data/company-facts/{t}.json', encoding='utf8'))
    f = [x for x in d['facts'] if x['id'] == i][0]
    if t not in cache:
        txt = open(d['source']['text_path'], encoding='utf8').read()
        parts = re.split(r'\[PDF PAGE (\d+)\]', txt)
        pg = {int(parts[k]): parts[k+1] for k in range(1, len(parts), 2)}
        cache[t] = pg
    pg = cache[t]
    print('=' * 80)
    print(i, d['company'], f['field'], f['period'], 'p', f['page'], f['attribution'])
    print('STMT:', f['statement'])
    p = f['page']
    body = pg.get(p, '')
    # shorten: if excerpts present, show page trimmed
    print('--- PAGE', p)
    print(re.sub(r'\n\s*\n+', '\n', body)[:2500])
    if '--next' in sys.argv:
        print('--- PAGE', p+1)
        print(re.sub(r'\n\s*\n+', '\n', pg.get(p+1, ''))[:1200])
