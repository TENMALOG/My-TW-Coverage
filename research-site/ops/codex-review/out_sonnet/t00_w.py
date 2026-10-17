import sys,json
job=sys.argv[1]
ids=[l.strip() for l in open(f'../jobs_sonnet/{job}.txt') if l.strip()]
spec={}
for l in open(f't00_spec_{job}.txt',encoding='utf8'):
    l=l.rstrip('\n')
    if not l: continue
    i,v,r=l.split('|',2); spec[i]=(v,r)
miss=[i for i in ids if i not in spec]; extra=[i for i in spec if i not in ids]
print('missing',miss,'extra',extra)
if not miss:
    with open(f'{job}.jsonl','w',encoding='utf8') as f:
        for i in ids:
            v,r=spec[i]
            f.write(json.dumps({"id":i,"verdict":"ACCEPT" if v=='A' else "REJECT","reason":r},ensure_ascii=False)+"\n")
    print(job,'A',sum(spec[i][0]=='A' for i in ids),'R',sum(spec[i][0]=='R' for i in ids))
