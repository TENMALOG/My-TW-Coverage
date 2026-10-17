import json, re, sys
tk = sys.argv[1]
ids = [l.strip() for l in open('research-site/ops/qa-audit4/ids_007.txt', encoding='utf8') if l.strip()]
ids = [i for i in ids if i.split('-AR-')[0] == tk]
d = json.load(open(f'research-site/data/company-facts/{tk}.json', encoding='utf8'))
t = open(d['source']['text_path'], encoding='utf8').read()
parts = re.split(r'\n\[PDF PAGE (\d+)\]\n', t)
pages = {int(parts[i]): parts[i+1] for i in range(1, len(parts), 2)}
fm = {f['id']: f for f in d['facts']}
need = set()
print('COMPANY', d['company'], d['legal_name'])
for i in ids:
    f = fm[i]
    print('---', i, f['field'], '| period:', f.get('period'), '| attr:', f.get('attribution'), '| page', f['page'])
    print('  S:', f['statement'])
    print('  E:', f['excerpts'])
    need.add(f['page'])
for p in sorted(need):
    if p in pages:
        print('=== PAGE', p)
        print(re.sub(r'[ \t]+', ' ', pages[p])[:int(sys.argv[2]) if len(sys.argv) > 2 else 3500])
