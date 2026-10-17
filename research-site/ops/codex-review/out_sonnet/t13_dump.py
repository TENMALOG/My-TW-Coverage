import json, re, sys
job, start, end = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
base = 'research-site/ops/codex-review/'
ids = [l.strip() for l in open(base + 'jobs_sonnet/%s.txt' % job, encoding='utf8') if l.strip()]
cache = {}
def pages(path):
    if path not in cache:
        t = open(path, encoding='utf8').read()
        parts = re.split(r'\[PDF PAGE (\d+)\]', t)
        cache[path] = {int(parts[i]): parts[i + 1] for i in range(1, len(parts), 2)}
    return cache[path]
def fnd(t, e):
    idx = [k for k, c in enumerate(t) if not c.isspace()]
    st = ''.join(t[k] for k in idx)
    es = re.sub(r'\s+', '', e)
    j = st.find(es)
    if j < 0 or not es:
        return -1, 0
    return idx[j], idx[j + len(es) - 1] - idx[j] + 1
BEF, AFT = 260, 120
seen = {}
for n, fid in enumerate(ids[start:end], start):
    tk = fid.split('-')[0]
    d = json.load(open('research-site/data/company-facts/%s.json' % tk, encoding='utf8'))
    f = [x for x in d['facts'] if x['id'] == fid][0]
    pg = pages(d['source']['text_path'])
    print('=' * 40)
    print('#%d %s %s FY%s | %s | p%s | %s | %s' % (n, fid, d['company'], d['source'].get('fy'), f['field'], f['page'], f['period'], f['attribution']))
    print('STMT:', f['statement'])
    iv = {}
    miss = []
    for e in f['excerpts']:
        ok = False
        for p in (f['page'], f['page'] + 1, f['page'] - 1):
            t = pg.get(p, '')
            i, L = fnd(t, e)
            if i >= 0:
                iv.setdefault(p, []).append((max(0, i - BEF), min(len(t), i + L + AFT)))
                ok = True; break
        if not ok: miss.append(e[:60])
    for p, l in iv.items():
        l.sort(); m = []
        for a, b in l:
            if m and a <= m[-1][1]: m[-1] = (m[-1][0], max(m[-1][1], b))
            else: m.append((a, b))
        for a, b in m:
            w = pg[p][a:b].replace('\n', ' | ')
            key = (tk, p, a // 100, b // 100)
            if key in seen and seen[key][1] == w:
                print('[p%d] (同 #%d 上下文)' % (p, seen[key][0]))
            else:
                seen[key] = (n, w)
                print('[p%d] %s' % (p, w))
    if miss: print('!! 未找到excerpt:', miss)
