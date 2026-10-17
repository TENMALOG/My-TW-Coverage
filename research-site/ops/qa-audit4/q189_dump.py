import json, re, sys, os
ids = [l.strip() for l in open('research-site/ops/qa-audit4/ids_189.txt', encoding='utf8') if l.strip()]
start, end = int(sys.argv[1]), int(sys.argv[2])
cache = {}
for i in ids[start:end]:
    t = i.split('-AR-')[0]
    d = json.load(open(f'research-site/data/company-facts/{t}.json', encoding='utf8'))
    f = [x for x in d['facts'] if x['id'] == i][0]
    if t not in cache:
        txt = open(d['source']['text_path'], encoding='utf8').read()
        parts = re.split(r'\[PDF PAGE (\d+)\]', txt)
        pg = {int(parts[k]): parts[k+1] for k in range(1, len(parts), 2)}
        cache[t] = pg
    pg = cache[t]
    p = f['page']
    print('=' * 80)
    print(i, d['company'], f['field'], '|', f['period'], '|', f['attribution'], '| page', p)
    print('STMT:', f['statement'])
    print('EXC:', f['excerpts'])
    if '-v' in sys.argv:
        print('PAGE TEXT:', pg.get(p, '')[:2500])
        print('NEXT:', pg.get(p+1, '')[:800])
