import json, re, sys
ids = [l.strip() for l in open('research-site/ops/qa-audit4/ids_084.txt', encoding='utf8') if l.strip()]
tk = sys.argv[1]
d = json.load(open(f'research-site/data/company-facts/{tk}.json', encoding='utf8'))
txt = open(d['source']['text_path'], encoding='utf8').read()
pages = {}
for m in re.finditer(r'\[PDF PAGE (\d+)\]\n(.*?)(?=\n\[PDF PAGE \d+\]|\Z)', txt, re.S):
    pages[int(m.group(1))] = m.group(2)
print(d['company'], d['legal_name'])
for f in d['facts']:
    if f['id'] not in ids or not f['id'].startswith(tk):
        continue
    print('=' * 70)
    print(f['id'], f['field'], '|', f['period'], '|', f['attribution'], '| p', f['page'])
    print('STMT:', f['statement'])
    print('EXC:', f['excerpts'])
    if '-p' in sys.argv:
        p = f['page']
        pg = pages.get(p, '')
        ex = f['excerpts'][0][:20] if f['excerpts'] else ''
        i = pg.find(ex)
        print('PAGE', p, ':', pg[max(0, i - 250):i + 650] if i >= 0 else pg[:1200])
