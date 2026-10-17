import json,sys,re
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_008.txt') if l.strip()]
lo,hi,W=int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])
cache={}
def getpage(t,p):
    m=re.search(r'\[PDF PAGE %d\]\n(.*?)(?=\[PDF PAGE %d\]|\Z)'%(p,p+1),t,re.S)
    return m.group(1) if m else ''
for i in ids[lo:hi]:
    t=i.split('-AR-')[0]
    d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
    f=[x for x in d['facts'] if x['id']==i][0]
    tp=d['source']['text_path']
    if tp not in cache: cache[tp]=open(tp,encoding='utf8').read()
    p=f['page']
    print('='*60);print(i,d['company'],f['field'],'|',f['period'],'|',f['attribution'],'| p',p)
    print('STMT:',f['statement']);print('EXC:',f['excerpts'])
    txt=getpage(cache[tp],p)
    idx=[j for j,c in enumerate(txt) if not c.isspace()]
    s=''.join(txt[j] for j in idx)
    pos=-1
    for e in f['excerpts'][::-1]:
        k=re.sub(r'\s','',e)[:10]
        pos=s.find(k)
        if pos>=0: break
    if pos<0: print('!! excerpt not found'); print(txt[:W]); continue
    a=idx[max(0,pos-W//3)] if pos-W//3>=0 else 0
    b=idx[min(len(idx)-1,pos+W)]
    print(re.sub(r'[ \t]+',' ',txt[a:b]))
