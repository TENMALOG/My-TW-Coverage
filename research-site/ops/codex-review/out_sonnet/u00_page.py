import json,re,sys
tk,pg_,a,b=sys.argv[1],int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4])
d=json.load(open('research-site/data/company-facts/%s.json'%tk,encoding='utf8'))
t=open(d['source']['text_path'],encoding='utf8').read()
parts=re.split(r'\[PDF PAGE (\d+)\]',t)
pg={int(parts[i]):parts[i+1] for i in range(1,len(parts)-1,2)}
print(re.sub(r'\s*\n\s*',' ',pg[pg_])[a:b])
