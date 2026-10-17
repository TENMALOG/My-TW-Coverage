import json, re, sys
ids = [l.strip() for l in open('research-site/ops/qa-audit4/ids_076.txt', encoding='utf-8') if l.strip()]
cache = {}
def load(t):
    if t in cache: return cache[t]
    d = json.load(open(f'research-site/data/company-facts/{t}.json', encoding='utf-8'))
    txt = open(d['source']['text_path'], encoding='utf-8').read()
    parts = re.split(r'\[PDF PAGE (\d+)\]', txt)
    pages = {int(parts[i]): parts[i+1] for i in range(1, len(parts), 2)}
    cache[t] = (d, pages); return cache[t]
a, b = int(sys.argv[1]), int(sys.argv[2])
for i in ids[a:b]:
    t = i.split('-AR-')[0]; d, pages = load(t)
    f = next(x for x in d['facts'] if x['id'] == i)
    print('=' * 60)
    print(i, d['company'], f['field'], '|', f['period'], '|', f['attribution'], '| p', f['page'])
    print('STMT:', f['statement'])
    pg = pages.get(f['page'], '')
    ex = f['excerpts']
    # locate first and last excerpt
    def norm(s): return re.sub(r'\s+', '', s)
    npg = norm(pg)
    # build map of normalized idx -> original idx
    idx = [k for k, c in enumerate(pg) if not c.isspace()]
    pos = []
    for e in ex:
        n = norm(e); p = npg.find(n)
        if p >= 0: pos.append(p)
    if pos:
        s = max(0, min(pos) - 60); e2 = min(len(npg), max(pos) + 150)
        os_ = idx[s]; oe = idx[min(e2, len(idx)) - 1]
        print('CTX:', pg[os_:oe + 1].strip())
    else:
        print('EXCERPT NOT FOUND; EXC:', ex)
    print('EXC:', ex)
