import json, sys, re
sys.stdout.reconfigure(encoding='utf8')
R = 'research-site/'
items = json.load(open(R + 'ops/codex-review/adj_0.json', encoding='utf8'))
lo, hi = int(sys.argv[1]), int(sys.argv[2])
B = int(sys.argv[3]) if len(sys.argv)>3 else 200
A = int(sys.argv[4]) if len(sys.argv)>4 else 450
cache = {}
for it in items[lo:hi]:
    tk = it['id'].split('-')[0]
    d = json.load(open(R + f'data/company-facts/{tk}.json', encoding='utf8'))
    f = next(x for x in d['facts'] if x['id'] == it['id'])
    tp = d['source']['text_path']
    t = cache.get(tp) or open(tp, encoding='utf8').read()
    cache[tp] = t
    print('=' * 70)
    print(it['id'], d.get('company'), '| REVIEWER:', it['reviewer_reason'])
    print('FIELD', f['field'], '| PERIOD', f['period'], '| PAGE', f['page'], '|', f['attribution'])
    print('STMT:', f['statement'])
    print('EXC:', json.dumps(f['excerpts'], ensure_ascii=False))
    ex = f['excerpts'][0]
    i = t.find(ex)
    if i < 0:
        i = t.find(ex[:12])
    if i < 0:
        ns = re.sub(r'\s','',t); idx=[k for k,c in enumerate(t) if not c.isspace()]
        j = ns.find(re.sub(r'\s','',ex)[:15])
        i = idx[j] if j>=0 else -1
    if i < 0:
        print('CTX: (not found)')
    else:
        print('CTX:', t[max(0, i - B):i + A].replace('\n', ' / '))
