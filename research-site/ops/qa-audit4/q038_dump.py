import json, re, sys, os
ids = [l.strip() for l in open('research-site/ops/qa-audit4/ids_038.txt', encoding='utf8') if l.strip()]
start, end = int(sys.argv[1]), int(sys.argv[2])
cache = {}
for i in ids[start:end]:
    t = i.split('-AR-')[0]
    if t not in cache:
        cache[t] = json.load(open(f'research-site/data/company-facts/{t}.json', encoding='utf8'))
    d = cache[t]
    f = [x for x in d['facts'] if x['id'] == i][0]
    txt = open(d['source']['text_path'], encoding='utf8').read()
    pages = re.split(r'\[PDF PAGE (\d+)\]', txt)
    pm = {int(pages[k]): pages[k+1] for k in range(1, len(pages), 2)}
    p = f['page']
    print('=' * 100)
    print(i, d['company'], d['legal_name'], '|', f['field'], '|', f['period'], '|', f['attribution'], '| page', p)
    print('STATEMENT:', f['statement'])
    print('EXCERPTS:', f['excerpts'])
    body = pm.get(p, '')
    # trim page text: show lines near the excerpts
    lines = body.split('\n')
    keys = [e[:12] for e in f['excerpts']]
    idx = set()
    for n, l in enumerate(lines):
        if any(k and k in l for k in keys):
            for m in range(max(0, n-6), min(len(lines), n+7)):
                idx.add(m)
    if not idx:
        idx = set(range(min(len(lines), 40)))
    print('PAGE TEXT (trimmed):')
    for m in sorted(idx):
        print('  ', lines[m][:200])
