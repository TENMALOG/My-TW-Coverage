import json, re, sys
job, a, b = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
F = 'research-site/ops/codex-review/'
ids = [l.strip() for l in open(F + 'jobs_sonnet/' + job + '.txt', encoding='utf8') if l.strip()]
cache = {}
def load(t):
    if t not in cache:
        cache[t] = open(t, encoding='utf8').read()
    return cache[t]
def page(txt, n):
    m = re.search(r'\[PDF PAGE %d\]' % n, txt)
    if not m:
        return ''
    m2 = re.search(r'\[PDF PAGE \d+\]', txt[m.end():])
    return txt[m.start(): m.end() + (m2.start() if m2 else len(txt))]
for i, fid in enumerate(ids[a:b], a):
    t = fid.split('-')[0]
    d = json.load(open('research-site/data/company-facts/%s.json' % t, encoding='utf8'))
    f = [x for x in d['facts'] if x['id'] == fid][0]
    txt = load(d['source']['text_path'])
    print('=== #%d %s [%s] %s | %s | p%s | %s' % (i, fid, d['company'], f['field'], f['period'], f['page'], f['attribution']))
    print('ST:', f['statement'])
    pg = page(txt, f['page']) + page(txt, f['page'] + 1)
    idx = [j for j, c in enumerate(pg) if not c.isspace()]
    s = ''.join(pg[j] for j in idx)
    spans = []
    for e in f['excerpts']:
        e2 = re.sub(r'\s+', '', e)
        k = s.find(e2)
        if k < 0: k = s.find(e2[:12])
        spans.append(k)
        print('EX:', e.replace('\n',' '))
    sp = [x for x in spans if x >= 0] or [0]
    k0, k1 = min(sp), max(sp)
    lo = idx[max(0, k0 - 1)]
    hi = idx[min(len(idx) - 1, k1 + 40)]
    lo = max(0, lo - 60); hi = min(len(pg), hi + 150)
    print('EX:', ' | '.join(re.sub(r'\s+',' ',e) for e in f['excerpts'])[:260])
    print('CTX:', pg[lo:hi].replace('\n', ' / '))
