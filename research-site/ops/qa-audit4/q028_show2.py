import pickle,re,sys
D=pickle.load(open('research-site/ops/qa-audit4/q028_cache.pkl','rb'))
ids=D['ids'];cache=D['cache']
def page(txt,p):
    m=re.search(r'\[PDF PAGE %d\]\n(.*?)(?=\n\[PDF PAGE \d+\]|\Z)'%p,txt,re.S)
    return m.group(1) if m else ''
def norm(s): return re.sub(r'\s+','',s)
a,b=int(sys.argv[1]),int(sys.argv[2])
W=int(sys.argv[3]) if len(sys.argv)>3 else 700
for i in ids[a:b]:
    t=i.split('-AR-')[0]
    d,txt=cache[t]
    f=[x for x in d['facts'] if x['id']==i][0]
    print('=====',i,d['company'],f['field'],'|',f['attribution'],'|',f['period'],'p',f['page'])
    print('STMT:',f['statement'])
    pg=page(txt,f['page'])
    npg=norm(pg)
    # find window around first excerpt line that is found
    pos=None
    for e in f['excerpts']:
        k=norm(e)
        j=npg.find(k)
        if j>=0 and len(k)>6: pos=j;break
    if pos is None: print('!!EXCERPT NOT FOUND');print(pg[:W*2]);continue
    # map back approx: show raw text; locate by counting nonspace chars
    cnt=0;rawpos=0
    for idx,ch in enumerate(pg):
        if not ch.isspace():
            if cnt==pos: rawpos=idx;break
            cnt+=1
    s=max(0,rawpos-W//3);print(pg[s:s+W])
