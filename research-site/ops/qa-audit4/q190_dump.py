import json, sys, re
root = 'research-site/'
ids = [l.strip() for l in open(root + 'ops/qa-audit4/ids_190.txt', encoding='utf8') if l.strip()]
start, end = int(sys.argv[1]), int(sys.argv[2])
W = int(sys.argv[3]) if len(sys.argv) > 3 else 700
cache = {}
def pages(t):
    parts = re.split(r'\n\[PDF PAGE (\d+)\]\n', t)
    return {int(parts[i]): parts[i+1] for i in range(1, len(parts), 2)}
ns = lambda s: re.sub(r'\s+', '', s)
for i, fid in enumerate(ids[start:end], start):
    t = fid.split('-AR-')[0]
    if t not in cache:
        d = json.load(open(root + 'data/company-facts/%s.json' % t, encoding='utf8'))
        cache[t] = (d, pages(open(d['source']['text_path'], encoding='utf8').read()))
    d, pg = cache[t]
    f = [x for x in d['facts'] if x['id'] == fid][0]
    print('=====', i, fid, d['company'], f['field'], '|', f['period'], '| p', f['page'], '|', f['attribution'])
    print('STMT:', f['statement'])
    p = f['page']
    txt = ns(pg.get(p, 'NOPAGE'))
    pos = [txt.find(ns(e)[:12]) for e in f['excerpts']]
    pos = [x for x in pos if x >= 0]
    lo = max(0, (min(pos) if pos else 0) - 200)
    hi = (max(pos) if pos else 0) + W
    print('PAGE:', txt[lo:hi])
    print('NEXT:', ns(pg.get(p+1, ''))[:250])
