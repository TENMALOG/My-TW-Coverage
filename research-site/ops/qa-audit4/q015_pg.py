import json,re,sys
tk=sys.argv[1]
d=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
t=open(d['source']['text_path'],encoding='utf8').read()
parts=re.split(r'\n\[PDF PAGE (\d+)\]\n',t)
pages={int(parts[k]):parts[k+1] for k in range(1,len(parts),2)}
for p in sys.argv[2:]:
    print('--- PAGE',p); print(re.sub(r'[ \t]+',' ',pages.get(int(p),'?')))
