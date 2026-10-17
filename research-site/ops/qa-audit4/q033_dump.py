import json, re, sys
ids = [l.strip() for l in open('research-site/ops/qa-audit4/ids_033.txt', encoding='utf8') if l.strip()]
start, end = int(sys.argv[1]), int(sys.argv[2])
cache = {}
def norm(s): return re.sub(r'\s+','',s)
for id_ in ids[start:end]:
    tk = id_.split('-AR-')[0]
    d = cache.get(tk) or json.load(open(f'research-site/data/company-facts/{tk}.json', encoding='utf8'))
    cache[tk] = d
    f = [x for x in d['facts'] if x['id'] == id_][0]
    t = open(d['source']['text_path'], encoding='utf8').read()
    parts = re.split(r'\n\[PDF PAGE (\d+)\]\n', t)
    pages = {int(parts[i]): parts[i + 1] for i in range(1, len(parts) - 1, 2)}
    p = f['page']
    print('=' * 60)
    print(id_, d['company'], '|', f['field'], '|', f.get('period'), '|', f['attribution'], '| p', p)
    print('STMT:', f['statement'])
    print('EXC:', f['excerpts'])
    pg = pages.get(p, '')
    # locate excerpt (whitespace-insensitive)
    idx = -1
    m = [(i,c) for i,c in enumerate(pg) if not c.isspace()]
    ns = ''.join(c for _,c in m)
    k = ns.find(norm(f['excerpts'][0])[:12]) if f['excerpts'] else -1
    if k >= 0: idx = m[k][0]
    if idx < 0: idx = 0
    a = max(0, idx - 250)
    print('--- page', p, '(window)')
    print(pg[a: idx + 1000])
    if len(pg) - (idx+1000) < 100:
        print('--- page', p + 1, 'head')
        print(pages.get(p + 1, '')[:500])
