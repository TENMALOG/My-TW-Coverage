import json, re, sys
ids = [l.strip() for l in open('research-site/ops/qa-audit4/ids_118.txt', encoding='utf8') if l.strip()]
start, end = int(sys.argv[1]), int(sys.argv[2])
cache = {}
ns = lambda s: re.sub(r'\s+', '', s)
for i in ids[start:end]:
    t = i.split('-AR-')[0]
    d = json.load(open(f'research-site/data/company-facts/{t}.json', encoding='utf8'))
    f = [x for x in d['facts'] if x['id'] == i][0]
    if t not in cache:
        txt = open(d['source']['text_path'], encoding='utf8').read()
        parts = re.split(r'\[PDF PAGE (\d+)\]', txt)
        cache[t] = {int(parts[k]): parts[k+1] for k in range(1, len(parts), 2)}
    p = f['page']
    print('=' * 60); print(i, f['statement'])
    for pp in (p, p+1):
        lines = cache[t].get(pp, '').split('\n')
        # find last excerpt
        ex = ns(f['excerpts'][-1])[:12]
        ex0 = ns(f['excerpts'][0])[:12]
        hit = None
        for k, l in enumerate(lines):
            if ex and ex in ns(l) or (ex[:6] and ex[:6] in ns(l)):
                hit = k; break
        if hit is None and pp == p: print('!! no hit on page', p)
        if hit is not None:
            print(f'--- p{pp} ---'); print('\n'.join(lines[max(0,hit-8):hit+7])); break
