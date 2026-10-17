import json, re, sys
ids = [l.strip() for l in open('research-site/ops/qa-audit4/ids_098.txt', encoding='utf8') if l.strip()]
start, end = int(sys.argv[1]), int(sys.argv[2])
cache = {}
for i in ids[start:end]:
    t = i.split('-AR-')[0]
    if t not in cache:
        d = json.load(open(f'research-site/data/company-facts/{t}.json', encoding='utf8'))
        txt = open(d['source']['text_path'], encoding='utf8').read()
        pages = re.split(r'\[PDF PAGE (\d+)\]', txt)
        pg = {int(pages[k]): pages[k + 1] for k in range(1, len(pages), 2)}
        cache[t] = (d, pg)
    d, pg = cache[t]
    f = next(x for x in d['facts'] if x['id'] == i)
    print('=' * 80)
    print(i, d['company'], f['field'], '|', f['period'], '|', f['attribution'], '| page', f['page'])
    print('STATEMENT:', f['statement'])
    print('EXCERPTS:', f['excerpts'])
    if len(sys.argv) > 3:
        p = f['page']
        for q in (p, p + 1):
            if q in pg:
                print(f'--- PAGE {q} ---')
                print(pg[q][:int(sys.argv[3])])
