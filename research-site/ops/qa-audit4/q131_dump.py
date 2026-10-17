import json, sys, re
ids = [l.strip() for l in open('research-site/ops/qa-audit4/ids_131.txt') if l.strip()]
cache = {}
def load(t):
    if t in cache: return cache[t]
    d = json.load(open(f'research-site/data/company-facts/{t}.json', encoding='utf8'))
    txt = open(d['source']['text_path'], encoding='utf8').read()
    parts = re.split(r'\[PDF PAGE (\d+)\]', txt)
    pages = {int(parts[k]): parts[k + 1] for k in range(1, len(parts), 2)}
    cache[t] = (d, pages)
    return cache[t]
lo, hi = int(sys.argv[1]), int(sys.argv[2])
n = int(sys.argv[3]) if len(sys.argv) > 3 else 2500
for i in ids[lo:hi]:
    t = i.split('-AR-')[0]
    d, pages = load(t)
    f = [x for x in d['facts'] if x['id'] == i][0]
    print('=====', i, d['company'])
    print('STMT:', f['statement'])
    print('FIELD:', f['field'], '| PERIOD:', f['period'], '| ATTR:', f['attribution'], '| PAGE:', f['page'])
    print('EXC:', f['excerpts'])
    if n:
        print('--PAGE', f['page'], '--')
        print(pages.get(f['page'], '')[:n])
