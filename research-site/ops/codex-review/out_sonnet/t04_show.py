import json,sys,re,os
os.chdir(r"C:/Users/Neo Pegasus/Documents/ChatGPT/078-kaori sample/artifacts/stock-coverage-audit-20261003/incoming/latest-audit/My-TW-Coverage")
job=sys.argv[1]; start=int(sys.argv[2]); end=int(sys.argv[3]); W=int(sys.argv[4]) if len(sys.argv)>4 else 450
ids=open(f'research-site/ops/codex-review/jobs_sonnet/{job}.txt',encoding='utf8').read().split()
cache={}
def pages(t):
    if t not in cache:
        txt=open(t,encoding='utf8').read()
        parts=re.split(r'\[PDF PAGE (\d+)\]',txt)
        d={}
        for i in range(1,len(parts),2): d[int(parts[i])]=parts[i+1]
        cache[t]=d
    return cache[t]
fc={}
for i,fid in enumerate(ids[start:end],start):
    tk=fid.split('-')[0]
    if tk not in fc: fc[tk]=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
    d=fc[tk]; f=[x for x in d['facts'] if x['id']==fid][0]
    P=pages(d['source']['text_path'])
    print(f"=== [{i}] {fid} {d['company']} field={f['field']} p{f['page']} period={f['period']} attr={f['attribution']}")
    print("STMT:",f['statement'])
    spans=[]
    for ex in f['excerpts']:
        found=False
        for pg in (f['page'],f['page']+1):
            t=P.get(pg,'')
            k=t.find(ex)
            if k<0:
                idx=[i for i,c in enumerate(t) if not c.isspace()]
                st=''.join(t[i] for i in idx); e2=''.join(ex.split())
                kk=st.find(e2)
                if kk<0: continue
                k=idx[kk]
            spans.append((pg,max(0,k-W),min(len(t),k+len(ex)+W))); found=True;break
        if not found: print("  !! excerpt not found:",ex[:40])
    # merge
    spans.sort(); m=[]
    for s in spans:
        if m and m[-1][0]==s[0] and s[1]<=m[-1][2]: m[-1]=(s[0],m[-1][1],max(m[-1][2],s[2]))
        else: m.append(s)
    for pg,a,b in m:
        print(f"--p{pg}[{a}:{b}]--");print(re.sub(r'\n+','\n',P[pg][a:b]))
