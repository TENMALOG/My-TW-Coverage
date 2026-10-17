import json, re, sys
ids = [l.strip() for l in open('research-site/ops/qa-audit4/ids_081.txt', encoding='utf-8') if l.strip()]
start, end = int(sys.argv[1]), int(sys.argv[2])
cache = {}
def pages(path):
    if path not in cache:
        t = open(path, encoding='utf-8').read()
        parts = re.split(r'\[PDF PAGE (\d+)\]', t)
        cache[path] = {int(parts[i]): parts[i+1] for i in range(1, len(parts), 2)}
    return cache[path]
for fid in ids[start:end]:
    tk = fid.split('-AR-')[0]
    d = json.load(open(f'research-site/data/company-facts/{tk}.json', encoding='utf-8'))
    f = [x for x in d['facts'] if x['id'] == fid][0]
    pg = pages(d['source']['text_path'])
    p = f['page']
    print('=' * 100)
    print(fid, d['company'], f['field'], '|', f['period'], '| p', p, '|', f['attribution'])
    print('STATEMENT:', f['statement'])
    print('EXCERPTS:', f['excerpts'])
    txt = pg.get(p, '')
    nxt = pg.get(p+1, '')
    k=-1
    for e in reversed(f['excerpts']):
        k=txt.find(e[:15])
        if k>=0: break
    print('found' if k>=0 else 'NOT FOUND on page', 'len', len(txt))
    if k>=0:
        print(txt[max(0,k-200):k+300])
    else:
        print(txt[:700]); print('NEXT:', nxt[:500])
