import json,sys,re
tk=sys.argv[1]
d=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
txt=open(d['source']['text_path'],encoding='utf8').read()
parts=re.split(r'\[PDF PAGE (\d+)\]',txt)
pg={int(parts[i]):parts[i+1] for i in range(1,len(parts),2)}
for p in sys.argv[2:]:
    print('=== PAGE',p);print(re.sub(r'[ \t]+',' ',pg.get(int(p),'MISSING')))
