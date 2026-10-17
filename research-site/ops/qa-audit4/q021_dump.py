import json, sys, re
ids = [l.strip() for l in open('research-site/ops/qa-audit4/ids_021.txt') if l.strip()]
cache = {}
def load(t):
    if t not in cache:
        d = json.load(open(f'research-site/data/company-facts/{t}.json', encoding='utf8'))
        txt = open(d['source']['text_path'], encoding='utf8').read()
        cache[t] = (d, txt)
    return cache[t]
want = sys.argv[1:]
for i in ids:
    t = i.split('-AR-')[0]
    if want and t not in want:
        continue
    d, txt = load(t)
    f = [x for x in d['facts'] if x['id'] == i][0]
    print('=====', i, d['company'], f['field'], f['period'], f['attribution'], 'p', f['page'])
    print('S:', f['statement'])
    print('E:', f['excerpts'])
    pg = f['page']
    def page(n):
        m = re.search(r'\[PDF PAGE %d\]\n(.*?)(?=\n\[PDF PAGE %d\]|\Z)' % (n, n + 1), txt, re.S)
        return m.group(1) if m else ''
    p = page(pg) + ' <<NEXT>> ' + page(pg + 1)
    p = re.sub(r'\s+', ' ', p)
    ex = re.sub(r'\s+', ' ', f['excerpts'][-1])[:10] if f['excerpts'] else ''
    k = p.find(ex)
    s = max(0, k - 120) if k >= 0 else 0
    print('P%s:' % ('' if k >= 0 else '(excerpt-not-found)'), p[s:s + 480])
