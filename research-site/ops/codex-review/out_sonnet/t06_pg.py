import json,re,sys
tk,page,key=sys.argv[1],int(sys.argv[2]),sys.argv[3]
w=int(sys.argv[4]) if len(sys.argv)>4 else 600
d=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
t=open(d['source']['text_path'],encoding='utf8').read()
p=re.split(r'\[PDF PAGE (\d+)\]',t)
pg={int(p[i]):p[i+1] for i in range(1,len(p),2)}
x=pg[page]; i=x.find(key)
print(re.sub(r'\n+',' | ',x[max(0,i-w):i+w]) if i>=0 else 'NOTFOUND')
