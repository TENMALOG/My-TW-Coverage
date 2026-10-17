import json, re, sys
ids = [l.strip() for l in open('research-site/ops/qa-audit4/ids_055.txt', encoding='utf-8') if l.strip()]
lo, hi = int(sys.argv[1]), int(sys.argv[2])
NL = chr(10)
cache = {}
for i in ids[lo:hi]:
    tk = i.split('-AR-')[0]
    if tk not in cache:
        d = json.load(open(f'research-site/data/company-facts/{tk}.json', encoding='utf-8'))
        t = open(d['source']['text_path'], encoding='utf-8').read()
        pages = {}
        for m in re.finditer(r'\[PDF PAGE (\d+)\]\n(.*?)(?=\n\[PDF PAGE \d+\]\n|\Z)', t, re.S):
            pages[int(m.group(1))] = m.group(2)
        cache[tk] = (d, pages)
    d, pages = cache[tk]
    f = [x for x in d['facts'] if x['id'] == i][0]
    print('=' * 70)
    print(i, d['company'], '| FY', d['source']['fy'])
    print('FIELD', f['field'], '| PERIOD', f['period'], '| ATTR', f['attribution'], '| PAGE', f['page'])
    print('STMT', f['statement'])
    print('EXC', f['excerpts'])
    p = f['page']
    print('--- page', p)
    txt = pages.get(p, '')
    if '--ctx' in sys.argv:
        lines = txt.split(NL)
        keep = set()
        for e in f['excerpts']:
            key = e.split(NL)[0][:12]
            for k, L in enumerate(lines):
                if key and key in L:
                    keep.update(range(max(0, k - 3), min(len(lines), k + 5)))
                    break
        print(NL.join(lines[k][:160] for k in sorted(keep)) if keep else txt[:1500])
    else:
        print(txt[:2500])
    if '--next' in sys.argv:
        print('--- page', p + 1)
        print(pages.get(p + 1, '')[:1500])
