import json,sys,re
job,a,b=sys.argv[1],int(sys.argv[2]),int(sys.argv[3])
ids=open(f'research-site/ops/codex-review/jobs_sonnet/{job}.txt',encoding='utf8').read().split()
cache={};seen=set()
def flat(s): return re.sub(r'\s*\n\s*',' ',s)
for i in ids[a:b]:
    t=i.split('-')[0]
    d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
    f=[x for x in d['facts'] if x['id']==i][0]
    p=d['source']['text_path']
    if p not in cache: cache[p]=open(p,encoding='utf8').read()
    txt=cache[p]; pg=f['page']
    def page(n):
        m=re.search(r'\[PDF PAGE %d\]'%n,txt)
        if not m: return ''
        e=re.search(r'\[PDF PAGE %d\]'%(n+1),txt)
        return txt[m.end():e.start() if e else m.end()+6000]
    P=page(pg)
    print('='*6,i,d['company'],'|',f['field'],'|',f['period'],'|p',pg,'|',f['attribution'])
    print('STMT:',f['statement'])
    for e in f['excerpts']: print('EXC:',flat(e)[:300])
    k=P.find(f['excerpts'][0][:20])
    key=(t,pg)
    if key in seen:
        s=max(0,k-250) if k>=0 else 0
        print('PAGE(again):',flat(P[s:s+500]))
    else:
        seen.add(key)
        s=max(0,k-400) if k>=0 else 0
        print('PAGE:',flat(P[s:s+1100]))
    pn=re.sub(r'\s','',P)
    if len(f['excerpts'])>1 and any(re.sub(r'\s','',x)[:12] not in pn for x in f['excerpts'][1:]):
        print('PAGE+1:',flat(page(pg+1)[:900]))
