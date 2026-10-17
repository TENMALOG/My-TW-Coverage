import sys,json,os
job=sys.argv[1]
base=r"C:/Users/Neo Pegasus/Documents/ChatGPT/078-kaori sample/artifacts/stock-coverage-audit-20261003/incoming/latest-audit/My-TW-Coverage/research-site/ops/codex-review/"
ids=open(base+f'jobs_sonnet/{job}.txt',encoding='utf8').read().split()
v={}
for fn in sorted(os.listdir(base+'out_sonnet')):
    if fn.startswith(f't04_{job}_') and fn.endswith('.txt'):
        for l in open(base+'out_sonnet/'+fn,encoding='utf8'):
            l=l.strip()
            if not l: continue
            i,vd,r=l.split('|',2); v[int(i)]=(vd,r)
miss=[i for i in range(len(ids)) if i not in v]
if miss: print('missing',miss[:20],len(miss)); 
else:
    with open(base+f'out_sonnet/{job}.jsonl','w',encoding='utf8') as f:
        for i,x in enumerate(ids):
            f.write(json.dumps({"id":x,"verdict":v[i][0],"reason":v[i][1]},ensure_ascii=False)+"\n")
    from collections import Counter
    print(job,Counter(a for a,_ in v.values()))
    for i in sorted(v):
        if v[i][0]=='REJECT': print(ids[i],v[i][1])
