import json, re, sys
ids = [l.strip() for l in open('research-site/ops/qa-audit4/ids_148.txt', encoding='utf-8') if l.strip()]
start, end = int(sys.argv[1]), int(sys.argv[2])
cache = {}; shown=set()
for i in ids[start:end]:
    t = i.split('-AR-')[0]
    d = json.load(open(f'research-site/data/company-facts/{t}.json', encoding='utf-8'))
    if t not in cache:
        txt = open(d['source']['text_path'], encoding='utf-8').read()
        parts = re.split(r'\[PDF PAGE (\d+)\]', txt)
        cache[t] = {int(parts[k]): parts[k+1] for k in range(1, len(parts), 2)}
    f = next(x for x in d['facts'] if x['id'] == i)
    p = f['page']
    print('=' * 60)
    print(i, d['company'], f['field'], '|', f['period'], '|', f['attribution'], '| p', p)
    print('STMT:', f['statement'])
    print('EXC:', f['excerpts'])
    pg = [l for l in cache[t].get(p, '').split('\n') if l.strip()]
    if (t,p) in shown:
        print('(same page shown earlier)'); continue
    shown.add((t,p))
    # find anchor line
    toks = sorted(set(re.findall(r'[\d,\.]{4,}|[\u4e00-\u9fff]{3,}', ' '.join(f['excerpts']))), key=len, reverse=True)
    idx = 0
    for tk in toks:
        h = [k for k,l in enumerate(pg) if tk in l]
        if h: idx = h[0]; break
    a = max(0, idx-14); b = min(len(pg), idx+14)
    print('\n'.join(pg[a:b]))
