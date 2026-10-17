import json, re, sys
ids = [l.strip() for l in open('research-site/ops/qa-audit4/ids_099.txt', encoding='utf8') if l.strip()]
lo, hi = int(sys.argv[1]), int(sys.argv[2])
cache = {}
def pages(path):
    if path not in cache:
        t = open(path, encoding='utf8').read()
        parts = re.split(r'\[PDF PAGE (\d+)\]\n', t)
        cache[path] = {int(parts[i]): parts[i+1] for i in range(1, len(parts), 2)}
    return cache[path]
for i in ids[lo:hi]:
    tk = i.split('-AR-')[0]
    d = json.load(open(f'research-site/data/company-facts/{tk}.json', encoding='utf8'))
    f = next(x for x in d['facts'] if x['id'] == i)
    pg = pages(d['source']['text_path'])
    p = f['page']
    print('=' * 80)
    print(i, d['company'], '|', f['field'], '|', f['period'], '|', f['attribution'], '| p', p)
    print('STMT:', f['statement'])
    print('EXC:', f['excerpts'])
    print('--- PAGE', p)
    txt = pg.get(p, '')
    k = -1
    for e in f['excerpts']:
        k = txt.find(e[:12])
        if k >= 0: break
    k = max(k, 0)
    print(re.sub(chr(10)+'+', chr(10), txt[max(0,k-80):k+330]))
    if sys.argv[3:] == ['next']:
        print('--- PAGE', p + 1)
        print(pg.get(p + 1, '')[:1200])
