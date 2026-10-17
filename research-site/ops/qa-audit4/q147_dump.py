import json, re, sys
ids = [l.strip() for l in open('research-site/ops/qa-audit4/ids_147.txt', encoding='utf8') if l.strip()]
start, end = int(sys.argv[1]), int(sys.argv[2])
cache = {}
for i in ids[start:end]:
    tk = i.split('-AR-')[0]
    if tk not in cache:
        d = json.load(open(f'research-site/data/company-facts/{tk}.json', encoding='utf8'))
        t = open(d['source']['text_path'], encoding='utf8').read()
        pages = {}
        parts = re.split(r'\[PDF PAGE (\d+)\]', t)
        for k in range(1, len(parts), 2):
            pages[int(parts[k])] = parts[k + 1]
        cache[tk] = (d, pages)
    d, pages = cache[tk]
    f = next(x for x in d['facts'] if x['id'] == i)
    print('=' * 80)
    print(i, d['company'], '|', f['field'], '|', f['period'], '|', f['attribution'], '| page', f['page'])
    print('STMT:', f['statement'])
    print('EXC:', f['excerpts'])
    p = f['page']
    txt = re.sub(r'[ \t]+', ' ', pages.get(p, ''))
    txt = re.sub(r'\n\s*\n+', '\n', txt)
    # window around first excerpt
    key = f['excerpts'][0][:8] if f['excerpts'] else ''
    pos = txt.find(key)
    if pos < 0:
        pos = 0
    s = max(0, pos - 60)
    print(f'--- page {p} [{s}:] ---')
    print(txt[s:s + 380])
