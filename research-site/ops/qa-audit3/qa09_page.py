import json,sys,re
t_=sys.argv[1]
d=json.load(open(f'research-site/data/company-facts/{t_}.json',encoding='utf-8'))
txt=open(d['source']['text_path'],encoding='utf-8').read()
parts=re.split(r'(?=\[PDF PAGE \d+\])',txt)
pg={}
for p in parts:
    m=re.match(r'\[PDF PAGE (\d+)\]',p)
    if m: pg[int(m.group(1))]=p
for a in sys.argv[2:]:
    n=int(a); print('#### PAGE',n); print(pg.get(n,'MISSING'))
