import json, re, sys
ids = [l.strip() for l in open('research-site/ops/qa-audit4/ids_085.txt') if l.strip()]
lo, hi = int(sys.argv[1]), int(sys.argv[2])
cache = {}
for i in ids[lo:hi]:
    t = i.split('-AR-')[0]
    d = json.load(open(f'research-site/data/company-facts/{t}.json', encoding='utf8'))
    f = [x for x in d['facts'] if x['id'] == i][0]
    if t not in cache:
        txt = open(d['source']['text_path'], encoding='utf8').read()
        parts = re.split(r'\[PDF PAGE (\d+)\]', txt)
        cache[t] = {int(parts[k]): parts[k+1] for k in range(1, len(parts), 2)}
    pg = f['page']
    print('=' * 80)
    print(i, d['company'], '|', f['field'], '|', f['period'], '|', f['attribution'], '| p', pg)
    print('STMT:', f['statement'])
    print('EXC:', f['excerpts'])
    if '--page' in sys.argv:
        pt = cache[t].get(pg, '')
        pos = -1
        for e in f['excerpts']:
            k = e.strip().splitlines()[0][:12]
            pos = pt.find(k)
            if pos >= 0: break
        a = max(0, pos - 100) if pos >= 0 else 0
        print('--- PAGE', pg, 'pos', pos)
        print(pt[a:a + 450])
