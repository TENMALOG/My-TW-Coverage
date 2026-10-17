import json,sys,re
t=sys.argv[1]
d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
txt=open(d['source']['text_path'],encoding='utf8').read()
pages=re.split(r'\[PDF PAGE (\d+)\]',txt)
pg={int(pages[i]):pages[i+1] for i in range(1,len(pages),2)}
for p in sys.argv[2:]:
    print('######## PAGE',p); print(re.sub(r'\n\s*\n+','\n',pg[int(p)]))
