import json, re, sys
ids = [l.strip() for l in open('research-site/ops/qa-audit4/ids_132.txt', encoding='utf8') if l.strip()]
sel = sys.argv[1]
cache = {}
for i in ids:
    tk = i.split('-AR-')[0]
    if not i.startswith(sel):
        continue
    d = json.load(open(f'research-site/data/company-facts/{tk}.json', encoding='utf8'))
    if tk not in cache:
        t = open(d['source']['text_path'], encoding='utf8').read()
        parts = re.split(r'\[PDF PAGE (\d+)\]\n', t)
        cache[tk] = {int(parts[k]): parts[k + 1] for k in range(1, len(parts), 2)}
    f = [x for x in d['facts'] if x['id'] == i][0]
    print('=====', i, f['field'], '|', f['statement'], '|', f['period'], '|', f['attribution'], '| p', f['page'])
    print('EXC:', f['excerpts'])
    if '--page' in sys.argv:
        p = f['page']
        txt = cache[tk].get(p, '') + ' <<NEXT>> ' + cache[tk].get(p + 1, '')
        txt = re.sub(r'[ \t]+', ' ', txt)
        pos = -1
        for e in f['excerpts']:
            pos = txt.find(re.sub(r'[ \t]+', ' ', e))
            if pos >= 0:
                break
        if pos < 0:
            print('!! excerpt not found on cited page; searching doc')
            for q, tx in cache[tk].items():
                tx2 = re.sub(r'\s+', '', tx)
                for e in f['excerpts']:
                    e2 = re.sub(r'\s+', '', e)
                    k = tx2.find(e2)
                    if k >= 0:
                        print('FOUND page', q, ':', tx2[max(0, k - 60):k + 250])
            pos = 0
        print(txt[max(0, pos - 100):pos + 300])
