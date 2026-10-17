import json, re, sys
ids = [l.strip() for l in open('research-site/ops/qa-audit4/ids_124.txt', encoding='utf8') if l.strip()]
s, e = int(sys.argv[1]), int(sys.argv[2])
cache = {}
def norm(x): return re.sub(r'\s+', '', x)
for i in ids[s:e]:
    t = i.split('-AR-')[0]
    d = json.load(open(f'research-site/data/company-facts/{t}.json', encoding='utf8'))
    if t not in cache:
        txt = open(d['source']['text_path'], encoding='utf8').read()
        parts = re.split(r'\[PDF PAGE (\d+)\]', txt)
        cache[t] = {int(parts[k]): parts[k+1] for k in range(1, len(parts)-1, 2)}
    f = [x for x in d['facts'] if x['id'] == i][0]
    pg = cache[t].get(f['page'], '')
    n = norm(pg)
    print('='*80); print(i, d['company'], f['field'], f['period'], '|', f['attribution'], '| p', f['page'])
    print('STMT:', f['statement'])
    for ex in f['excerpts']:
        k = n.find(norm(ex)[:15])
        print('EXC:', ex[:200], '| found' if k>=0 else '| NOTFOUND')
    k = n.find(norm(f['excerpts'][0])[:15])
    if k < 0: k = 0
    print('CTX:', n[max(0,k-150):k+550])
