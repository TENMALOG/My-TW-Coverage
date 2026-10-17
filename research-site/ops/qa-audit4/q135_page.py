import json,re,sys
tk,p=sys.argv[1],int(sys.argv[2]); s=int(sys.argv[3]) if len(sys.argv)>3 else 0; n=int(sys.argv[4]) if len(sys.argv)>4 else 3000
d=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
t=open(d['source']['text_path'],encoding='utf8').read()
m=re.search(r'\[PDF PAGE %d\]\n(.*?)(?=\n\[PDF PAGE \d+\]|\Z)'%p,t,re.S)
x=re.sub(r'\s*\n\s*',' / ',m.group(1)); print(x[s:s+n])
