import json, re, sys
NL = chr(10)
ids = [l.strip() for l in open('research-site/ops/qa-audit4/ids_113.txt', encoding='utf8') if l.strip()]
tick = sys.argv[1]
W = int(sys.argv[2]) if len(sys.argv) > 2 else 10
d = json.load(open(f'research-site/data/company-facts/{tick}.json', encoding='utf8'))
txt = open(d['source']['text_path'], encoding='utf8').read()
parts = re.split(r'\[PDF PAGE (\d+)\]', txt)
pages = {int(parts[i]): parts[i + 1] for i in range(1, len(parts), 2)}
print('COMPANY', d['company'], d['legal_name'])
for f in d['facts']:
    if f['id'] not in ids or not f['id'].startswith(tick + '-'):
        continue
    print('=' * 70)
    print(f['id'], '|', f['field'], '|', f['period'], '|', f['attribution'], '| page', f['page'])
    print('STATEMENT:', f['statement'])
    print('EXCERPTS:', [e.replace(NL, ' / ') for e in f['excerpts']])
    p = f['page']
    pg = [l for l in pages.get(p, 'NA').split(NL) if l.strip()]
    hit = set()
    for ex in f['excerpts']:
        key = ex.split(NL)[-1].strip()[:12]
        for n, l in enumerate(pg):
            if key and key in l:
                hit.add(n)
    if not hit:
        hit = {0}
    out = sorted({m for n in hit for m in range(max(0, n - W // 3), min(len(pg), n + W))})
    print('--- PAGE', p, '(window)')
    print(NL.join(pg[m] for m in out))
