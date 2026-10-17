import json, re, sys
ids = [l.strip() for l in open('research-site/ops/qa-audit4/ids_141.txt', encoding='utf8') if l.strip()]
start, end = int(sys.argv[1]), int(sys.argv[2])
cache = {}
for i in ids[start:end]:
    tk = i.split('-AR-')[0]
    if tk not in cache:
        d = json.load(open(f'research-site/data/company-facts/{tk}.json', encoding='utf8'))
        t = open(d['source']['text_path'], encoding='utf8').read()
        pages = {}
        parts = re.split(r'\[PDF PAGE (\d+)\]', t)
        for k in range(1, len(parts), 2):
            pages[int(parts[k])] = parts[k + 1]
        cache[tk] = (d, pages)
    d, pages = cache[tk]
    f = next(x for x in d['facts'] if x['id'] == i)
    p = f['page']
    flat = re.sub(r'\s+', '', pages.get(p, '') + pages.get(p + 1, ''))
    nums = re.findall(r'\d[\d,\.]*', f['statement'])
    miss = [n for n in nums if n.rstrip('.,') not in flat]
    exm = [e for e in f['excerpts'] if re.sub(r'\s+', '', e) not in flat]
    print(i, d['company'], '|', f['field'], '|', f['period'], '|', f['attribution'], '| p', p)
    print('  S:', f['statement'])
    print('  E:', ' // '.join(e.strip() for e in f['excerpts']))
    if miss or exm:
        print('  !! missing nums', miss, 'missing excerpts', exm)
