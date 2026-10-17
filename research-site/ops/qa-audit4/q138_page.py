import json,sys,re
tk=sys.argv[1]; pgs=[int(x) for x in sys.argv[2:]]
d=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
t=open(d['source']['text_path'],encoding='utf8').read()
parts=re.split(r'\[PDF PAGE (\d+)\]',t)
m={int(parts[i]):parts[i+1] for i in range(1,len(parts),2)}
for p in pgs:
    print('######## PAGE',p); print(m.get(p,'')[:6000])
