import json, re, sys
ids = [l.strip() for l in open('research-site/ops/qa-audit4/ids_115.txt', encoding='utf8') if l.strip()]
start, end = int(sys.argv[1]), int(sys.argv[2])
cache = {}
for i in ids[start:end]:
    tk = i.split('-AR-')[0]
    if tk not in cache:
        d = json.load(open(f'research-site/data/company-facts/{tk}.json', encoding='utf8'))
        t = open(d['source']['text_path'], encoding='utf8').read()
        pages = {}
        for m in re.finditer(r'\[PDF PAGE (\d+)\]\n(.*?)(?=\n\[PDF PAGE \d+\]|\Z)', t, re.S):
            pages[int(m.group(1))] = m.group(2)
        cache[tk] = (d, pages)
    d, pages = cache[tk]
    f = next(x for x in d['facts'] if x['id'] == i)
    p = f['page']
    print('=' * 80)
    print(i, f['field'], '|', f['period'], '|', f['attribution'], '| page', p)
    print('STMT:', f['statement'])
    print('EXC:', f['excerpts'])
    if '--page' in sys.argv:
        pt = re.sub(r'[ \t]+', ' ', pages.get(p, ''))
        pt = re.sub(r'\n\s*\n+', '\n', pt)
        print('PAGE TEXT:', pt[:2500])
