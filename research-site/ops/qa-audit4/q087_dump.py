import json, re, sys
ids = [l.strip() for l in open('research-site/ops/qa-audit4/ids_087.txt', encoding='utf8') if l.strip()]
lo, hi = int(sys.argv[1]), int(sys.argv[2])
cache = {}
def pages(path):
    if path not in cache:
        t = open(path, encoding='utf8').read()
        parts = re.split(r'\[PDF PAGE (\d+)\]', t)
        cache[path] = {int(parts[i]): parts[i+1] for i in range(1, len(parts), 2)}
    return cache[path]
for i in ids[lo:hi]:
    tk = i.split('-AR-')[0]
    d = json.load(open(f'research-site/data/company-facts/{tk}.json', encoding='utf8'))
    f = next(x for x in d['facts'] if x['id'] == i)
    pg = pages(d['source']['text_path'])
    print('=' * 80)
    print(i, f['field'], f['period'], f['attribution'], 'page', f['page'])
    print('STATEMENT:', f['statement'])
    print('EXCERPTS:', f['excerpts'])
    p = f['page']
    txt = pg.get(p, '') + chr(10) + '[[NEXTPAGE]]' + chr(10) + pg.get(p + 1, '')
    pos = -1
    for e in sorted(f['excerpts'], key=len, reverse=True):
        m = re.search(r'\s*'.join(re.escape(c) for c in re.sub(r'\s+','',e)), txt)
        if m:
            pos = m.start(); break
    if pos < 0:
        print('(excerpt not found; page head)'); print(txt[:1500])
    else:
        print('--- CONTEXT'); print(txt[max(0, pos-80):pos+420])
