import json, re, sys
tk = sys.argv[1]; pgs = [int(x) for x in sys.argv[2:]]
d = json.load(open(f'research-site/data/company-facts/{tk}.json', encoding='utf8'))
t = open(d['source']['text_path'], encoding='utf8').read()
parts = re.split(r'\[PDF PAGE (\d+)\]', t)
pages = {int(parts[k]): parts[k+1] for k in range(1, len(parts), 2)}
for p in pgs:
    s = re.sub(r'[ \t]+', ' ', pages.get(p, ''))
    s = re.sub(r'\n\s*\n+', '\n', s)
    print('#### PAGE', p); print(s)
