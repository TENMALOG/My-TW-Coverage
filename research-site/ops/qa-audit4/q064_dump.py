import json, re, sys
ids = [l.strip() for l in open('research-site/ops/qa-audit4/ids_064.txt', encoding='utf8') if l.strip()]
start, end = int(sys.argv[1]), int(sys.argv[2])
cache = {}
def load(t):
    if t in cache: return cache[t]
    d = json.load(open(f'research-site/data/company-facts/{t}.json', encoding='utf8'))
    txt = open(d['source']['text_path'], encoding='utf8').read()
    parts = re.split(r'\[PDF PAGE (\d+)\]', txt)
    pages = {int(parts[i]): parts[i+1] for i in range(1, len(parts), 2)}
    cache[t] = (d, pages)
    return cache[t]
for i in ids[start:end]:
    t = i.split('-AR-')[0]
    d, pages = load(t)
    f = next(x for x in d['facts'] if x['id'] == i)
    print('=' * 80)
    print(i, d['company'], '|', f['field'], '|', f['period'], '|', f['attribution'], '| p', f['page'])
    print('STATEMENT:', f['statement'])
    print('EXCERPTS:', f['excerpts'])
    if '-v' in sys.argv:
        for p in (f['page'], f['page'] + 1):
            print(f'--- page {p} ---')
            print(re.sub(r'[ \t]+', ' ', pages.get(p, '')[:3500]))
