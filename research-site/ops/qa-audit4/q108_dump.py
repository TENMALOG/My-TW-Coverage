import json, re, sys
ids = [l.strip() for l in open('research-site/ops/qa-audit4/ids_108.txt', encoding='utf-8') if l.strip()]
want = sys.argv[1:]  # optional tickers
cache = {}
seen=set()
for i in ids:
    t = i.split('-AR-')[0]
    if want and t not in want:
        continue
    d = json.load(open(f'research-site/data/company-facts/{t}.json', encoding='utf-8'))
    f = next(x for x in d['facts'] if x['id'] == i)
    if t not in cache:
        txt = open(d['source']['text_path'], encoding='utf-8').read()
        parts = re.split(r'\[PDF PAGE (\d+)\]', txt)
        cache[t] = {int(parts[k]): parts[k + 1] for k in range(1, len(parts), 2)}
    pg = f['page']
    pages = cache[t]
    print('=' * 80)
    print(i, f['field'], '|', f['period'], '|', f['attribution'], '| p', pg)
    print('STMT:', f['statement'])
    print('EXC:', f['excerpts'])
    for p in (pg,):
        body = pages.get(p, '')
        # locate first excerpt
        ex = f['excerpts'][0][:12] if f['excerpts'] else ''
        k = body.find(ex)
        s = max(0, k - 400) if k >= 0 else 0
        key=(t,p)
        if key in seen:
            print('--- page same as shown above')
        else:
            seen.add(key)
            print(f'--- page {p}')
            print(body[:2600])
