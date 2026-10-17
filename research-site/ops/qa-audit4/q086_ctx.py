import json, re, sys
ids = [l.strip() for l in open('research-site/ops/qa-audit4/ids_086.txt', encoding='utf8') if l.strip()]
want = sys.argv[1]
cache = {}
def pages(path):
    if path not in cache:
        t = open(path, encoding='utf8').read()
        parts = re.split(r'\[PDF PAGE (\d+)\]', t)
        cache[path] = {int(parts[i]): parts[i+1] for i in range(1, len(parts), 2)}
    return cache[path]
for i in ids:
    tk = i.split('-AR-')[0]
    if tk != want: continue
    d = json.load(open(f'research-site/data/company-facts/{tk}.json', encoding='utf8'))
    f = [x for x in d['facts'] if x['id'] == i][0]
    pg = pages(d['source']['text_path'])
    print('=' * 60)
    print(i, f['field'], '|', f['period'], '| p', f['page'], '|', f['attribution'])
    print('STMT:', f['statement'])
    p = f['page']
    shown = False
    for q in (p, p+1):
        lines = pg.get(q, '').split('\n')
        key = re.sub(r'\s', '', f['excerpts'][0])[:10]
        for k, ln in enumerate(lines):
            if key in re.sub(r'\s', '', ln):
                print(f'--- p{q} line {k}')
                print('\n'.join(l.rstrip() for l in lines[max(0, k-3):k+12]))
                shown = True
                break
        if shown: break
    if not shown: print('!!! excerpt not located; EXC:', f['excerpts'])
