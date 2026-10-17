import json,sys
job=sys.argv[1]
base='research-site/ops/codex-review/'
ids=[l.strip() for l in open(base+'jobs_sonnet/%s.txt'%job,encoding='utf8') if l.strip()]
v={}
for l in open(base+'out_sonnet/u00_v.txt',encoding='utf8'):
    l=l.rstrip('\n')
    if not l: continue
    i,x,r=l.split('|',2); v[i]=(x,r)
miss=[i for i in ids if i not in v]
if miss: print('MISSING',miss); sys.exit(1)
with open(base+'out_sonnet/%s.jsonl'%job,'w',encoding='utf8',newline='\n') as f:
    for i in ids:
        x,r=v[i]; f.write(json.dumps({'id':i,'verdict':'ACCEPT' if x=='A' else 'REJECT','reason':r},ensure_ascii=False)+'\n')
a=sum(1 for i in ids if v[i][0]=='A'); print(job,len(ids),'ACCEPT',a,'REJECT',len(ids)-a)
for i in ids:
    if v[i][0]=='R': print(' ',i,v[i][1])
