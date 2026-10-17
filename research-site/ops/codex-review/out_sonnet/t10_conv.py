import json
for job in ['cr0060','cr0074','cr0088','cr0102','cr0116','cr0130']:
    base='research-site/ops/codex-review/'
    ids=[l.strip() for l in open(base+f'jobs_sonnet/{job}.txt',encoding='utf8') if l.strip()]
    v={}
    for l in open(base+f'out_sonnet/t10_v_{job}.txt',encoding='utf8'):
        l=l.rstrip('\n')
        if not l: continue
        a,b,c=l.split('|',2); v[a]=(b,c)
    assert all(i in v for i in ids)
    na=nr=0
    with open(base+f'out_sonnet/{job}.jsonl','w',encoding='utf8',newline='\n') as o:
        for i in ids:
            b,c=v[i]
            verdict='ACCEPT' if b=='A' else 'REJECT'
            if b=='A': na+=1
            else: nr+=1
            o.write(json.dumps({'id':i,'verdict':verdict,'reason':c},ensure_ascii=False)+'\n')
    print(job,len(ids),'ACCEPT',na,'REJECT',nr)
