import json, re, sys
tk = sys.argv[1]
d = json.load(open(f'research-site/data/company-facts/{tk}.json', encoding='utf-8'))
t = open(d['source']['text_path'], encoding='utf-8').read()
pages = re.split(r'\n\[PDF PAGE (\d+)\]\n', t)
pm = {int(pages[k]): pages[k + 1] for k in range(1, len(pages), 2)}
ids = [l.strip() for l in open('research-site/ops/qa-audit4/ids_097.txt', encoding='utf-8') if l.strip().startswith(tk + '-')]
ps = sorted({f['page'] for f in d['facts'] if f['id'] in ids})
for p in ps:
    print('--- PAGE', p)
    print(re.sub(r'[ \t]+', ' ', pm.get(p, '')))
