import json, re, sys
ids = [l.strip() for l in open('research-site/ops/qa-audit4/ids_062.txt', encoding='utf8') if l.strip()]
tick = sys.argv[1]
cache = {}
d = json.load(open(f'research-site/data/company-facts/{tick}.json', encoding='utf8'))
txt = open(d['source']['text_path'], encoding='utf8').read()
parts = re.split(r'\[PDF PAGE (\d+)\]', txt)
pages = {int(parts[i]): parts[i + 1] for i in range(1, len(parts), 2)}
print('COMPANY', d['company'], d['legal_name'], d['source']['fy'])
for f in d['facts']:
    if f['id'] not in ids or not f['id'].startswith(tick):
        continue
    print('=' * 70)
    print(f['id'], f['field'], '|', f['period'], '|', f['attribution'], '| p', f['page'])
    print('STMT:', f['statement'])
    p = f['page']
    full = re.sub(r'[ \t]+\n', '\n', pages.get(p, 'NOPAGE'))
    print('--- PAGE', p)
    print(full[:3500])
    if len(sys.argv) > 2:
        print('--- PAGE', p + 1)
        print(pages.get(p + 1, '')[:2500])
