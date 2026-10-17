import json,re,sys
tk,p=sys.argv[1],int(sys.argv[2]); n=int(sys.argv[3]) if len(sys.argv)>3 else 1500
d=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
t=open(d['source']['text_path'],encoding='utf8').read()
parts=re.split(r'\[PDF PAGE (\d+)\]',t)
pg={int(parts[i]):parts[i+1] for i in range(1,len(parts),2)}
print(re.sub(r'[ \t]+',' ',pg[p])[:n])
