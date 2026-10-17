import json, re, sys
ids = [l.strip() for l in open('research-site/ops/qa-audit4/ids_018.txt', encoding='utf8') if l.strip()]
lo, hi = int(sys.argv[1]), int(sys.argv[2])
W = int(sys.argv[3]) if len(sys.argv) > 3 else 700
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
    def page(n):
        if n not in pos: return ''
        s = pos[n]; e = txt.find('[PDF PAGE %d]' % (n + 1), s)
        return txt[s:e if e > 0 else len(txt)]
    pg = f['page']; p = page(pg)
    print('=' * 60)
    print(i, d['company'], '|', f['field'], '|', f['period'], '| p', pg, '|', f['attribution'])
    print('STMT:', f['statement'])
    print('EXC:', f['excerpts'])
    ex = f['excerpts'][0] if f['excerpts'] else ''
    k = p.find(ex)
    if k < 0:
        k = p.find(ex[:6]) if ex else 0
    k = max(k, 0)
    a = max(0, k - 250)
    print('--- PAGE', pg, '---')
    print(p[a:a + W + 250])
    if len(f['excerpts']) > 1 and p.find(f['excerpts'][-1]) > a + W + 250:
        kk = p.find(f['excerpts'][-1]); print('...[LAST EXC ctx]'); print(p[max(0,kk-200):kk+400])
