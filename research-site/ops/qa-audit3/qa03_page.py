import json,re,sys
tk,p=sys.argv[1],int(sys.argv[2]); n=int(sys.argv[3]) if len(sys.argv)>3 else 3000
d=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
t=open(d['source']['text_path'],encoding='utf8').read()
pg=re.split(r'\n\[PDF PAGE (\d+)\]\n',t)
pm={int(pg[k]):pg[k+1] for k in range(1,len(pg),2)}
print(pm.get(p,'MISSING')[:n])
