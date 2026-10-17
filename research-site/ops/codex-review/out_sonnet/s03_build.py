import json,sys
job=sys.argv[1]
ids=[l.strip() for l in open(f'jobs_sonnet/{job}.txt',encoding='utf8') if l.strip()]
v={}
for l in open(f'out_sonnet/s03_v_{job}.txt',encoding='utf8'):
    l=l.rstrip('\n')
    if not l: continue
    i,a,r=l.split(' ',2); v[int(i)]=(a,r)
miss=[i for i in range(len(ids)) if i not in v]
assert not miss,miss
with open(f'out_sonnet/{job}.jsonl','w',encoding='utf8') as f:
    for i,x in enumerate(ids):
        f.write(json.dumps({'id':x,'verdict':'ACCEPT' if v[i][0]=='A' else 'REJECT','reason':v[i][1]},ensure_ascii=False)+'\n')
print(job,len(ids),sum(1 for i in v.values() if i[0]=='R'))
