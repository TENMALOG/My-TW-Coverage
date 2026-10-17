import json,sys,re
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_047.txt') if l.strip()]
cache={}
def load(t):
    if t not in cache:
        d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
        txt=open(d['source']['text_path'],encoding='utf8').read()
        cache[t]=(d,txt)
    return cache[t]
which=sys.argv[1]
for i in ids:
    t=i.split('-AR-')[0]
    if t!=which: continue
    d,txt=load(t)
    f=[x for x in d['facts'] if x['id']==i][0]
    print('=====',i,f['field'],f['period'],f['attribution'],'p',f['page'])
    print('S:',f['statement'])
    print('E:',f['excerpts'])
    pg=f['page']
    for p in (pg,pg+1) if len(sys.argv)<3 else (pg,):
        m=re.search(r'\[PDF PAGE %d\]\n(.*?)(?=\[PDF PAGE %d\]|\Z)'%(p,p+1),txt,re.S)
        if m and (p==pg or sys.argv[-1]=='n'):
            s=m.group(1)
            key=re.sub(r'\s','',f['excerpts'][-1])[:12]
            # window
            flat=s
            idx=flat.find(f['excerpts'][-1][:8])
            print('--page',p,'len',len(s))
            seen=globals().setdefault('seen',set())
            if (t,p) not in seen:
                seen.add((t,p)); print(s[:3500])
            else: print('(page printed earlier)')
