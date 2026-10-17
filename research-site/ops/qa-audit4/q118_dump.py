import json, re, sys
ids = [l.strip() for l in open('research-site/ops/qa-audit4/ids_118.txt', encoding='utf8') if l.strip()]
start, end = int(sys.argv[1]), int(sys.argv[2])
cache = {}
for i in ids[start:end]:
    t = i.split('-AR-')[0]
    d = json.load(open(f'research-site/data/company-facts/{t}.json', encoding='utf8'))
    f = [x for x in d['facts'] if x['id'] == i][0]
    if t not in cache:
        txt = open(d['source']['text_path'], encoding='utf8').read()
        parts = re.split(r'\[PDF PAGE (\d+)\]', txt)
        cache[t] = {int(parts[k]): parts[k+1] for k in range(1, len(parts), 2)}
    pg = cache[t]
    p = f['page']
    print('=' * 70)
    print(i, f['field'], '|', f['period'], '|', f['attribution'], '| page', p)
    print('STMT:', f['statement'])
    print('EXC:', f['excerpts'])
    if '--page' in sys.argv:
        print('--- PAGE TEXT ---')
        print(pg.get(p, '')[:3500])
