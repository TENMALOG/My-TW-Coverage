import sys,json
F='research-site/ops/codex-review/'
job=sys.argv[1]
ids=open(F+f'jobs_sonnet/{job}.txt',encoding='utf8').read().split()
d={}
for l in open(F+f'out_sonnet/t12_n_{job}.txt',encoding='utf8'):
    l=l.rstrip('\n')
    if not l.strip(): continue
    i,v,r=l.split('|',2); d[i]=(v,r)
miss=[i for i in ids if i not in d]; extra=[i for i in d if i not in ids]
print(job,'miss',miss,'extra',extra)
if miss or extra: sys.exit(1)
with open(F+f'out_sonnet/{job}.jsonl','w',encoding='utf8',newline='\n') as f:
    for i in ids:
        v,r=d[i]
        f.write(json.dumps({'id':i,'verdict':'ACCEPT' if v=='A' else 'REJECT','reason':r},ensure_ascii=False)+'\n')
c=[d[i][0] for i in ids]; print('A',c.count('A'),'R',c.count('R'))
