import json, re, sys
ids = [l.strip() for l in open('research-site/ops/qa-audit4/ids_090.txt', encoding='utf8') if l.strip()]
lo, hi = int(sys.argv[1]), int(sys.argv[2])
cache = {}
for i in ids[lo:hi]:
    t = i.split('-AR-')[0]
    d = json.load(open(f'research-site/data/company-facts/{t}.json', encoding='utf8'))
    if t not in cache:
        txt = open(d['source']['text_path'], encoding='utf8').read()
        parts = re.split(r'\[PDF PAGE (\d+)\]', txt)
        cache[t] = {int(parts[k]): parts[k + 1] for k in range(1, len(parts), 2)}
    pages = cache[t]
    f = next(x for x in d['facts'] if x['id'] == i)
    print('=' * 60)
    print(i, d['company'], f['field'], f['period'], f['attribution'], 'p', f['page'])
    print('STMT:', f['statement'])
    p = f['page']
    pg = pages.get(p, '') + '\n' + pages.get(p + 1, '')
    lines = [l for l in pg.split('\n') if l.strip()]
    norm = [re.sub(r'\s+', '', l) for l in lines]
    keep = set()
    for e in f['excerpts']:
        key = re.sub(r'\s+', '', e)[:10]
        for n, l in enumerate(norm):
            if key in l:
                keep.update(range(max(0, n - 7), min(len(lines), n + 5)))
                break
        else:
            print('!! excerpt not found:', e[:40])
    if not keep:
        keep = set(range(min(25, len(lines))))
    prev = -2
    for n in sorted(keep):
        if n != prev + 1:
            print('  ...')
        print(lines[n])
        prev = n
