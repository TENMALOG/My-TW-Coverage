import json, re, sys
root = 'research-site/'
ids = [l.strip() for l in open(root + 'ops/qa-audit4/ids_102.txt', encoding='utf-8') if l.strip()]
tick = sys.argv[1]
d = json.load(open(root + 'data/company-facts/%s.json' % tick, encoding='utf-8'))
t = open(d['source']['text_path'], encoding='utf-8').read()
parts = re.split(r'\[PDF PAGE (\d+)\]', t)
pages = {int(parts[i]): parts[i + 1] for i in range(1, len(parts), 2)}
print('COMPANY', d['company'], d['legal_name'])
need = set()
for f in d['facts']:
    if f['id'] in ids:
        print('---', f['id'], f['field'], '| period:', f.get('period'), '| attr:', f.get('attribution'), '| page', f['page'])
        print('STMT:', f['statement'])
        print('EXC:', f['excerpts'])
        need.add(f['page'])
        need.add(f['page'] + 1)
print('\n====== PAGES')
for p in sorted(need):
    if p in pages:
        print('##### PAGE', p)
        print(pages[p])
