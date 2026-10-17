import json, re, sys
ids = [l.strip() for l in open('research-site/ops/qa-audit4/ids_070.txt', encoding='utf8') if l.strip()]
sel = sys.argv[1:]  # tickers
cache = {}
for t in sel:
    d = json.load(open(f'research-site/data/company-facts/{t}.json', encoding='utf8'))
    txt = open(d['source']['text_path'], encoding='utf8').read()
    pages = {}
    parts = re.split(r'\[PDF PAGE (\d+)\]', txt)
    for i in range(1, len(parts), 2):
        pages[int(parts[i])] = parts[i + 1]
    print('=====', t, d['company'], 'fy', d['source']['fy'])
    for f in d['facts']:
        if f['id'] not in ids:
            continue
        print('--', f['id'], f['field'], '|', f['period'], '|', f['attribution'], '| p', f['page'])
        print('STMT:', f['statement'])
        print('EXC:', f['excerpts'])
    pg = set(f['page'] for f in d['facts'] if f['id'] in ids)
    for p in sorted(pg):
        print(f'##### PAGE {p}')
        print(re.sub(r'[ \t]+', ' ', re.sub(r'\n\s*\n+', '\n', pages.get(p, 'MISSING'))))
        continue
        print(re.sub(r'[ \t]+', ' ', re.sub(r'\n\s*\n+', '\n', pages.get(p + 1, 'MISSING')))[:1500])
