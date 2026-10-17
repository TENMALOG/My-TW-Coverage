import json,sys,re
tk,p=sys.argv[1],int(sys.argv[2]); a=int(sys.argv[3]) if len(sys.argv)>3 else 0; n=int(sys.argv[4]) if len(sys.argv)>4 else 3000
d=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
t=open(d['source']['text_path'],encoding='utf8').read()
parts=re.split(r'\[PDF PAGE (\d+)\]',t)
pg={int(parts[i]):parts[i+1] for i in range(1,len(parts),2)}
s=re.sub(r'\s*\n\s*',' ',pg[p])
if len(sys.argv)>5: s=s.replace(' ','')
print(s[a:a+n])
