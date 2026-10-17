import json, re, sys
ids = [l.strip() for l in open('research-site/ops/qa-audit4/ids_124.txt', encoding='utf8') if l.strip()]
start, end = int(sys.argv[1]), int(sys.argv[2])
cache = {}
for i in ids[start:end]:
    t = i.split('-AR-')[0]
    d = json.load(open(f'research-site/data/company-facts/{t}.json', encoding='utf8'))
    if t not in cache:
        txt = open(d['source']['text_path'], encoding='utf8').read()
        parts = re.split(r'\[PDF PAGE (\d+)\]', txt)
        pages = {int(parts[k]): parts[k + 1] for k in range(1, len(parts) - 1, 2)}
        cache[t] = pages
    pages = cache[t]
    f = [x for x in d['facts'] if x['id'] == i][0]
    print('=' * 100)
    print(i, d['company'], '|', f['field'], '|', f['period'], '|', f['attribution'], '| page', f['page'])
    print('STMT:', f['statement'])
    print('EXC:', f['excerpts'])
    p = f['page']
    print('--- PAGE', p)
    print(pages.get(p, '')[:int(sys.argv[3]) if len(sys.argv) > 3 else 3500])
