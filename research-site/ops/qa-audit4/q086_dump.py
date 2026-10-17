import json, re, sys
ids = [l.strip() for l in open('research-site/ops/qa-audit4/ids_086.txt', encoding='utf8') if l.strip()]
want = sys.argv[1] if len(sys.argv) > 1 else None
cache = {}
def pages(path):
    if path not in cache:
        t = open(path, encoding='utf8').read()
        parts = re.split(r'\[PDF PAGE (\d+)\]', t)
        d = {}
        for i in range(1, len(parts), 2):
            d[int(parts[i])] = parts[i + 1]
        cache[path] = d
    return cache[path]
for i in ids:
    tk = i.split('-AR-')[0]
    if want and tk != want:
        continue
    d = json.load(open(f'research-site/data/company-facts/{tk}.json', encoding='utf8'))
    f = [x for x in d['facts'] if x['id'] == i][0]
    pg = pages(d['source']['text_path'])
    print('=' * 70)
    print(i, f['field'], '|', f['period'], '| p', f['page'], '|', f['attribution'])
    print('STMT:', f['statement'])
    print('EXC:', f['excerpts'])
    p = f['page']
    if '--page' in sys.argv:
        print('--- PAGE', p)
        print(pg.get(p, '')[:6000])
        print('--- PAGE', p + 1)
        print(pg.get(p + 1, '')[:2500])
