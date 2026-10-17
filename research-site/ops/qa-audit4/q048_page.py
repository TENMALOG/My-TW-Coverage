import json,re,sys
t=sys.argv[1]; pg=int(sys.argv[2]); n=int(sys.argv[3]) if len(sys.argv)>3 else 1
d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
txt=open(d['source']['text_path'],encoding='utf8').read()
parts=re.split(r'\[PDF PAGE (\d+)\]',txt)
pages={int(parts[i]):parts[i+1] for i in range(1,len(parts),2)}
for p in range(pg,pg+n): print('--- PAGE',p); print(pages.get(p,''))
