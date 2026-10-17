import json, re, sys
ids = [l.strip() for l in open('research-site/ops/qa-audit4/ids_097.txt', encoding='utf-8') if l.strip()]
want = sys.argv[1] if len(sys.argv) > 1 else None
cache = {}
for i in ids:
    tk = i.split('-AR-')[0]
    if want and tk != want:
        continue
    d = json.load(open(f'research-site/data/company-facts/{tk}.json', encoding='utf-8'))
    if tk not in cache:
        t = open(d['source']['text_path'], encoding='utf-8').read()
        pages = re.split(r'\n\[PDF PAGE (\d+)\]\n', t)
        pm = {int(pages[k]): pages[k + 1] for k in range(1, len(pages), 2)}
        cache[tk] = pm
        print('=== ', tk, d['company'], d['legal_name'], 'fy', d['source']['fy'])
    f = next(x for x in d['facts'] if x['id'] == i)
    print('\n#', i, f['field'], '|', f['period'], '| p', f['page'], '|', f['attribution'])
    print('S:', f['statement'])
    print('E:', f['excerpts'])
    pm = cache[tk]
    if '-p' in sys.argv:
        pg = f['page']
        print('--- PAGE', pg)
        print(re.sub(r'[ \t]+', ' ', pm.get(pg, '')))
