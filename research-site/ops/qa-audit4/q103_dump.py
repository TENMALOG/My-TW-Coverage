import json, re, sys
ids = [l.strip() for l in open('research-site/ops/qa-audit4/ids_103.txt', encoding='utf8') if l.strip()]
lo, hi = int(sys.argv[1]), int(sys.argv[2])
cache = {}
seen=set()
for i in ids[lo:hi]:
    tk = i.split('-AR-')[0]
    if tk not in cache:
        d = json.load(open(f'research-site/data/company-facts/{tk}.json', encoding='utf8'))
        t = open(d['source']['text_path'], encoding='utf8').read()
        pages = {int(m.group(1)): m.group(2) for m in re.finditer(r'\[PDF PAGE (\d+)\]\n(.*?)(?=\n\[PDF PAGE \d+\]|\Z)', t, re.S)}
        cache[tk] = (d, pages)
    d, pages = cache[tk]
    f = next(x for x in d['facts'] if x['id'] == i)
    p = f['page']
    print('=' * 80)
    print(i, d['company'], f['field'], '|', f['period'], '|', f['attribution'], '| page', p)
    print('STATEMENT:', f['statement'])
    print('EXCERPTS:', f['excerpts'])
    txt = pages.get(p, '')
    txt = re.sub(r'[ \t]+', ' ', txt)
    flat = re.sub(r'\s+', '', txt)
    pos = -1
    for e in f['excerpts']:
        pos = txt.find(e[:15])
        if pos >= 0: break
    a = max(0, pos-400) if pos>=0 else 0
    key=(tk,p,a)
    if key in seen:
        print('PAGE: same as earlier', a); continue
    seen.add(key)
    print('PAGE:', 'FOUND' if pos>=0 else 'NOTFOUND', txt[a:a+1500].replace(chr(10),' '))
    if len(sys.argv) > 3:
        print('NEXT:', re.sub(r'[ \t]+', ' ', pages.get(p + 1, ''))[:1200])
