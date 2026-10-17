import json,re,sys
tk=sys.argv[1]
d=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
txt=open(d['source']['text_path'],encoding='utf8').read()
parts=re.split(r'\[PDF PAGE (\d+)\]',txt)
pg={int(parts[i]):parts[i+1] for i in range(1,len(parts),2)}
for p in sys.argv[2:]:
    a=p.split(':'); n=int(a[0]); lim=int(a[1]) if len(a)>1 else 3000
    print('#### PAGE',n); print(re.sub(r'[ \t]+',' ',re.sub(r'\n\s*\n+','\n',pg[n]))[:lim])
