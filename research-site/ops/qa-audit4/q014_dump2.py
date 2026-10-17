import json, re, sys
ids = [l.strip() for l in open('research-site/ops/qa-audit4/ids_014.txt', encoding='utf8') if l.strip()]
lo, hi = int(sys.argv[1]), int(sys.argv[2])
W = int(sys.argv[3]) if len(sys.argv) > 3 else 5
cache = {}
def norm(s): return re.sub(r'\s+', '', s)
for i in ids[lo:hi]:
    t = i.split('-AR-')[0]
    d = json.load(open(f'research-site/data/company-facts/{t}.json', encoding='utf8'))
    f = [x for x in d['facts'] if x['id'] == i][0]
    tp = d['source']['text_path']
    if tp not in cache:
        txt = open(tp, encoding='utf8').read()
        cache[tp] = txt
    txt = cache[tp]
    def page(n):
        m = re.search(r'\[PDF PAGE %d\]' % n, txt)
        if not m: return ''
        e = txt.find('[PDF PAGE %d]' % (n + 1), m.end())
        return txt[m.end():e if e > 0 else len(txt)]
    pg = f['page']
    print('=' * 70)
    print(i, d['company'], '|', f['field'], '|', f['period'], '| p', pg, '|', f['attribution'])
    print('STMT:', f['statement'])
    print('EXC:', f['excerpts'])
    for n in (pg, pg + 1):
        lines = page(n).split('\n')
        keep = set()
        for ex in f['excerpts']:
            ne = norm(ex)[:12]
            for k, l in enumerate(lines):
                if ne and ne in norm(l):
                    keep.update(range(max(0, k - W), min(len(lines), k + W + 1)))
        if keep:
            print('--- p%d ---' % n)
            prev = -2
            for k in sorted(keep):
                if k != prev + 1: print('  ..')
                print(lines[k]); prev = k
        elif n == pg:
            print('--- p%d (no excerpt match; head) ---' % n); print('\n'.join(lines[:40]))
