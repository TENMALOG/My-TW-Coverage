import json, re, sys
tk = sys.argv[1]
ids = [l.strip() for l in open('research-site/ops/qa-audit4/ids_071.txt', encoding='utf8') if l.strip()]
ids = [i for i in ids if i.split('-AR-')[0] == tk]
d = json.load(open(f'research-site/data/company-facts/{tk}.json', encoding='utf8'))
tx = open(d['source']['text_path'], encoding='utf8').read()
pages = re.split(r'\[PDF PAGE (\d+)\]', tx)
pg = {int(pages[i]): pages[i+1] for i in range(1, len(pages)-1, 2)}
def clean(s):
    return re.sub(r'[ \t]+', ' ', re.sub(r'\n\s*\n+', '\n', s)).strip()
print(tk, d['company'])
shown = set()
for f in d['facts']:
    if f['id'] not in ids:
        continue
    print('=====', f['id'], f['field'], '|', f['period'], '|', f['attribution'], '| p', f['page'])
    print('STMT:', f['statement'])
    for e in f['excerpts']:
        print('  EX:', e.replace('\n', ' '))
    p = f['page']
    t = clean(pg.get(p, ''))
    W = int(sys.argv[2]) if len(sys.argv) > 2 else 700
    key = re.sub(r'\s+', '', f['excerpts'][0])[:8]
    flat = re.sub(r'\s+', '', t)
    # locate in original-clean text by trying first words
    idx = -1
    for e in f['excerpts']:
        w = clean(e).split(' ')[0:3]
        i = t.find(' '.join(w)) if w else -1
        if i >= 0:
            idx = i; break
    if idx < 0: idx = 0
    print('--- PAGE', p, 'ctx@', idx, '/', len(t), '---')
    print(t[max(0, idx-W):idx+W*2])
