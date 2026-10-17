import json, re, sys
ids = [l.strip() for l in open('research-site/ops/qa-audit4/ids_014.txt', encoding='utf8') if l.strip()]
lo, hi = int(sys.argv[1]), int(sys.argv[2])
cache = {}
for i in ids[lo:hi]:
    t = i.split('-AR-')[0]
    d = json.load(open(f'research-site/data/company-facts/{t}.json', encoding='utf8'))
    f = [x for x in d['facts'] if x['id'] == i][0]
    tp = d['source']['text_path']
    if tp not in cache:
        txt = open(tp, encoding='utf8').read()
        cache[tp] = {int(m.group(1)): m.end() for m in re.finditer(r'\[PDF PAGE (\d+)\]', txt)}, txt
    pos, txt = cache[tp]
    pg = f['page']
    def page(n):
        if n not in pos: return ''
        s = pos[n]
        nxt = [v for k, v in pos.items() if k == n + 1]
        e = txt.find('[PDF PAGE %d]' % (n + 1), s)
        return txt[s:e if e > 0 else len(txt)]
    print('=' * 80)
    print(i, d['company'], '|', f['field'], '|', f['period'], '| p', pg, '|', f['attribution'])
    print('STMT:', f['statement'])
    print('EXC:', f['excerpts'])
    p = page(pg)
    print('--- PAGE', pg, '---')
    print(p[:3500])
    if len(p) > 3500: print('...[trunc]')
    pn = page(pg + 1)
    print('--- NEXT PAGE head ---')
    print(pn[:700])
