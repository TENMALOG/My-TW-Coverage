import json,sys,re
t,p0,p1=sys.argv[1],int(sys.argv[2]),int(sys.argv[3])
a=int(sys.argv[4]) if len(sys.argv)>4 else 0
b=int(sys.argv[5]) if len(sys.argv)>5 else 4000
d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
txt=open(d['source']['text_path'],encoding='utf8').read()
parts=re.split(r'\[PDF PAGE (\d+)\]',txt)
pg={int(parts[k]):parts[k+1] for k in range(1,len(parts),2)}
for p in range(p0,p1+1):
    s=re.sub(r'\n\s*\n','\n',pg[p]); s=re.sub(r'[ \t]*\n[ \t]*','|',s)
    print('--P',p,'--');print(s[a:b])
