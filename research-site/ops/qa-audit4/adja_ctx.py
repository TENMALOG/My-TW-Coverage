import json,sys,re
t,p,key=sys.argv[1],int(sys.argv[2]),sys.argv[3]; w=int(sys.argv[4]) if len(sys.argv)>4 else 500
d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
txt=open(d['source']['text_path'],encoding='utf8').read()
parts=re.split(r'\[PDF PAGE (\d+)\]',txt)
m={int(parts[k]):parts[k+1] for k in range(1,len(parts),2)}
for pp in (p,p+1):
    s=re.sub(r'[ \t]+',' ',m.get(pp,''))
    i=s.find(key)
    if i>=0:
        print('--page',pp);print(s[max(0,i-w):i+w]);break
else: print('NOTFOUND')
