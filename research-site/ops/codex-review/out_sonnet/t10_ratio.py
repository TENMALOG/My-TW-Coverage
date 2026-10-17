import json,re,sys
for job in ['cr0060','cr0074','cr0088','cr0102','cr0116','cr0130']:
    ids=[l.strip() for l in open(f'research-site/ops/codex-review/jobs_sonnet/{job}.txt',encoding='utf8') if l.strip()]
    cache={};tx={}
    for i in ids:
        tk=i.split('-')[0]
        if tk not in cache: cache[tk]=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
        d=cache[tk]; f=[x for x in d['facts'] if x['id']==i][0]
        s=f['statement']
        m=re.findall(r'(\d[\d,]*\.?\d*)(仟元|千元)',s)
        p=re.findall(r'(\d+\.?\d*)%',s)
        if not m or not p: continue
        A=float(m[0][0].replace(',',''))
        P=float(p[-1]) if len(p)>0 else None
        path=d['source']['text_path']
        if path not in tx:
            t=open(path,encoding='utf8').read()
            parts=re.split(r'\[PDF PAGE (\d+)\]',t); tx[path]={int(parts[k]):parts[k+1] for k in range(1,len(parts),2)}
        txt=tx[path].get(f['page'],'')+tx[path].get(f['page']+1,'')[:3000]
        txt=re.sub(r'(?<=\d)\s*,\s*(?=\d)',',',txt)
        nums=set(float(x.replace(',','')) for x in re.findall(r'\d[\d,]*\.?\d*',txt) if x.replace(',','').replace('.','').isdigit())
        tol=0.06 if '.' in p[-1] else 0.55
        ok=any(T>A and abs(A/T*100-P)<=tol for T in nums if T>0)
        if not ok: print(job,i,A,P,s[:60])
