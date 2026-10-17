import json, re, sys
ids = [l.strip() for l in open('research-site/ops/qa-audit4/ids_076.txt', encoding='utf-8') if l.strip()]
cache = {}
def load(t):
    if t in cache: return cache[t]
    d = json.load(open(f'research-site/data/company-facts/{t}.json', encoding='utf-8'))
    txt = open(d['source']['text_path'], encoding='utf-8').read()
    parts = re.split(r'\[PDF PAGE (\d+)\]', txt)
    pages = {int(parts[i]): parts[i+1] for i in range(1, len(parts), 2)}
    cache[t] = (d, pages)
    return cache[t]
start, end = int(sys.argv[1]), int(sys.argv[2])
lastp = None
for i in ids[start:end]:
    t = i.split('-AR-')[0]
    d, pages = load(t)
    f = next(x for x in d['facts'] if x['id'] == i)
    print('=' * 80)
    print(i, d['company'], f['field'], '|', f['period'], '|', f['attribution'], '| p', f['page'])
    print('STMT:', f['statement'])
    key = (t, f['page'])
    if key != lastp:
        p = f['page']
        for q in (p, p + 1):
            print(f'--- PAGE {q} ---')
            print(pages.get(q, '')[:3500])
        lastp = key
    else:
        print('(same page as previous)')
