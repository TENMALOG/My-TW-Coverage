import json,re,sys
t=sys.argv[1]; 
d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
txt=open(d['source']['text_path'],encoding='utf8').read()
parts=re.split(r'\[PDF PAGE (\d+)\]',txt)
pages={int(parts[k]):parts[k+1] for k in range(1,len(parts),2)}
for p in sys.argv[2:]:
    p=int(p); print('#### PAGE',p)
    print(re.sub(r'\n\s*\n+','\n',re.sub(r'[ \t]+',' ',pages.get(p,''))))
