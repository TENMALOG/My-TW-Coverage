import json,re,sys
tk,p,s,n=sys.argv[1],int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4])
d=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
t=open(d['source']['text_path'],encoding='utf8').read()
parts=re.split(r'\[PDF PAGE (\d+)\]',t)
pg={int(parts[k]):parts[k+1] for k in range(1,len(parts),2)}
print(pg[p][s:s+n])
