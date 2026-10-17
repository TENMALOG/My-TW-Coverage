import json,sys,re
i=sys.argv[1];kw=sys.argv[2] if len(sys.argv)>2 else None
w=int(sys.argv[3]) if len(sys.argv)>3 else 700
t=i.split('-')[0]
d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
f=[x for x in d['facts'] if x['id']==i][0]
txt=open(d['source']['text_path'],encoding='utf8').read()
m=re.search(r'\[PDF PAGE %d\]'%f['page'],txt)
s=m.start() if m else 0
m2=re.search(r'\[PDF PAGE %d\]'%(f['page']+1),txt)
e=m2.start()+1500 if m2 else s+6000
p=txt[s:e]
if kw:
    pat=r'\s*'.join(re.escape(c) for c in kw if not c.isspace())
    for m in re.finditer(pat,p):
        print('...',p[max(0,m.start()-w):m.end()+w].replace('\n',' '),'\n---');break
else: print(p[:3000])
