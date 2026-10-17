import json, re, sys
ids = [l.strip() for l in open('research-site/ops/qa-audit4/ids_019.txt', encoding='utf8') if l.strip()]
lo, hi = int(sys.argv[1]), int(sys.argv[2])
cache = {}
for id_ in ids[lo:hi]:
    tk = id_.split('-AR-')[0]
    if tk not in cache:
        d = json.load(open(f'research-site/data/company-facts/{tk}.json', encoding='utf8'))
        t = open(d['source']['text_path'], encoding='utf8').read()
        cache[tk] = (d, t)
    d, t = cache[tk]
    f = next(x for x in d['facts'] if x['id'] == id_)
    pg = f['page']
    m = re.search(r'\[PDF PAGE %d\]\n(.*?)(?=\[PDF PAGE %d\]|\Z)' % (pg, pg + 1), t, re.S)
    txt = m.group(1) if m else 'NOPAGE'
    ex = f['excerpts'][0] if f['excerpts'] else ''
    i = txt.find(ex[:15]) if ex else -1
    if i < 0: i = 0
    seg = txt[max(0, i - 120): i + 380]
    print('=' * 80)
    print(id_, d['company'], f['field'], '|', f['period'], '|', f['attribution'], '| p', pg)
    print('STMT:', f['statement'])
    print('EXC:', f['excerpts'])
    print('PAGE:', seg)
