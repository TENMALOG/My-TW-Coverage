import json, re, sys
t, pg = sys.argv[1], [int(x) for x in sys.argv[2:]]
d = json.load(open(f'research-site/data/company-facts/{t}.json', encoding='utf8'))
txt = open(d['source']['text_path'], encoding='utf8').read()
pages = re.split(r'\[PDF PAGE (\d+)\]', txt)
pm = {int(pages[k]): pages[k+1] for k in range(1, len(pages), 2)}
for p in pg:
    print('#### PAGE', p)
    print(re.sub(r'\n\s*\n+', '\n', pm.get(p, '')))
