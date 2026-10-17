import json, re, sys
ids = [l.strip() for l in open('research-site/ops/qa-audit3/ids_20.txt', encoding='utf-8') if l.strip()]
tick = sys.argv[1]
W = int(sys.argv[2]) if len(sys.argv) > 2 else 8
d = json.load(open(f'research-site/data/company-facts/{tick}.json', encoding='utf-8'))
txt = open(d['source']['text_path'], encoding='utf-8').read()
parts = re.split(r'\[PDF PAGE (\d+)\]', txt)
pages = {int(parts[i]): parts[i+1] for i in range(1, len(parts), 2)}
print('COMPANY', d['company'], d['source']['fy'])
for f in d['facts']:
    if f['id'] in ids:
        print('\n#####', f['id'], f['field'], '|', f['period'], '| p', f['page'], '|', f['attribution'])
        print('S:', f['statement'])
        lines = (pages.get(f['page'], '') ).split('\n')
        nxt = pages.get(f['page']+1, '').split('\n')
        allv = lines + ['--next page--'] + nxt[:25]
        norm = lambda s: re.sub(r'\s+', '', s)
        hit = None
        for e in f['excerpts'][::-1]:
            ne = norm(e)
            for i, l in enumerate(allv):
                if ne[:12] and ne[:12] in norm(l):
                    hit = i; break
            if hit is not None: break
        if hit is None: print('NO HIT; excerpts', f['excerpts']); print('\n'.join(lines[:40])); continue
        print('\n'.join(allv[max(0,hit-W):hit+W+1]))
