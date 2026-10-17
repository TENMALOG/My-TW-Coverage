import json,sys,re
t=sys.argv[1]
d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
txt=open(d['source']['text_path'],encoding='utf8').read()
parts=re.split(r'\[PDF PAGE (\d+)\]',txt)
pg={int(parts[k]):parts[k+1] for k in range(1,len(parts),2)}
for p in sys.argv[2:]:
    s=re.sub(r'\n\s*\n+','\n',pg[int(p)])
    print('#### PAGE',p); print(s[:int(4000)])
