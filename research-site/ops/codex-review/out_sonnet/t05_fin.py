import sys,json
job=sys.argv[1]
base='research-site/ops/codex-review/'
ids=open(base+f'jobs_sonnet/{job}.txt',encoding='utf8').read().split()
v={}
for l in open(base+f'out_sonnet/t05_{job}.txt',encoding='utf8'):
    l=l.rstrip('\n')
    if not l.strip(): continue
    i,verd,r=l.split('|',2); v[i.strip()]=(verd.strip(),r.strip())
miss=[i for i in ids if i not in v]
if miss: print('MISSING',len(miss),miss[:5]); sys.exit(1)
with open(base+f'out_sonnet/{job}.jsonl','w',encoding='utf8') as f:
    for i in ids:
        f.write(json.dumps({"id":i,"verdict":v[i][0],"reason":v[i][1]},ensure_ascii=False)+'\n')
print(job,'ACCEPT',sum(1 for i in ids if v[i][0]=='ACCEPT'),'REJECT',[ (i,v[i][1]) for i in ids if v[i][0]=='REJECT'])
