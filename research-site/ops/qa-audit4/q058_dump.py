import json, re, sys
ids = [l.strip() for l in open('research-site/ops/qa-audit4/ids_058.txt', encoding='utf8') if l.strip()]
tk = sys.argv[1]
d = json.load(open(f'research-site/data/company-facts/{tk}.json', encoding='utf8'))
txt = open(d['source']['text_path'], encoding='utf8').read()
parts = re.split(r'\[PDF PAGE (\d+)\]', txt)
pages = {int(parts[i]): parts[i+1] for i in range(1, len(parts), 2)}
want = [f for f in d['facts'] if f['id'] in ids]
print('COMPANY', d['company'], d['legal_name'])
shown = set()
for f in want:
    print('=== ', f['id'], f['field'], '| period:', f['period'], '| attr:', f['attribution'], '| page', f['page'])
    print('STMT:', f['statement'])
    print('EXC:', f['excerpts'])
for f in want:
    for p in [f['page']] + ([f['page']+1] if len(sys.argv) > 2 else []):
        if p in shown: continue
        shown.add(p)
        t = re.sub(r'[ \t]+', ' ', pages.get(p, ''))
        t = re.sub(r'\n\s*\n+', '\n', t)
        print(f'--- PAGE {p} ---')
        print(t[:int(sys.argv[3]) if len(sys.argv) > 3 else 3500])
