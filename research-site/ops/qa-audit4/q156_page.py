import json, re, sys
t, p = sys.argv[1], int(sys.argv[2])
d = json.load(open(f'research-site/data/company-facts/{t}.json', encoding='utf-8'))
txt = open(d['source']['text_path'], encoding='utf-8').read()
parts = re.split(r'\[PDF PAGE (\d+)\]', txt)
pg = {int(parts[k]): parts[k+1] for k in range(1, len(parts), 2)}
print(f'#### {t} p{p}')
print(pg[p])
