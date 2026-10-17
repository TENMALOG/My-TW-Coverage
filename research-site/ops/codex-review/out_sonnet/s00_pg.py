import json,sys,re
ids=[l.strip() for l in open(sys.argv[1]) if l.strip()]
tk=sys.argv[2]; PRE=int(sys.argv[3]); POST=int(sys.argv[4]); CAP=int(sys.argv[5]) if len(sys.argv)>5 else 3000
d=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
txt=open(d['source']['text_path'],encoding='utf8').read()
pages=re.split(r'\[PDF PAGE (\d+)\]',txt)
pg={int(pages[k]):pages[k+1] for k in range(1,len(pages),2)}
def find(s,key):
    idx=[k for k,c in enumerate(s) if not c.isspace()]
    ns=''.join(s[k] for k in idx); nk=''.join(c for c in key if not c.isspace())
    n=ns.find(nk)
    return (idx[n],idx[min(n+len(nk)-1,len(idx)-1)]) if n>=0 else None
spans={}
print('#### TICKER',tk,d.get('company'))
for i in ids:
    if not i.startswith(tk+'-'): continue
    f=[x for x in d['facts'] if x['id']==i][0]
    print('==',i,f['field'],'p',f['page'],f['period'],f['attribution'])
    print('  S:',f['statement'])
    print('  E:',' | '.join(f['excerpts']))
    p=f['page']
    for ex in f['excerpts']:
        for q in (p,p+1):
            r=find(pg.get(q,''),ex)
            if r:
                a,b=spans.get(q,(10**9,-1)); spans[q]=(min(a,r[0]),max(b,r[1])); break
for q,(a,b) in sorted(spans.items()):
    s=pg[q]; a=max(0,a-PRE); b=min(len(s),b+POST)
    if b-a>CAP: b=a+CAP
    print(f'--- PAGE {q} [{a}:{b}]'); print(s[a:b])
