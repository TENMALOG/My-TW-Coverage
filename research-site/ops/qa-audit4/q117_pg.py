import json,re,sys
tk=sys.argv[1]
d=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
t=open(d['source']['text_path'],encoding='utf8').read()
pg=re.split(r'\n\[PDF PAGE (\d+)\]\n',t)
pages={int(pg[k]):pg[k+1] for k in range(1,len(pg),2)}
for p in map(int,sys.argv[2:]):
    print('#### page',p); print(re.sub(r'\n\s*\n+','\n',pages[p]))
