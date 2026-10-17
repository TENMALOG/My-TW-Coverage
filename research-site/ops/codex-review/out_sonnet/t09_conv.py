import sys,json
job=sys.argv[1]
ids=open(f'../jobs_sonnet/{job}.txt',encoding='utf8').read().split()
m={}
for l in open(f't09_{job}.txt',encoding='utf8'):
    l=l.rstrip('\n')
    if not l.strip(): continue
    i,v,r=l.split('|',2)
    assert i not in m,i
    m[i]=(v,r)
miss=[i for i in ids if i not in m]; extra=[i for i in m if i not in ids]
print(job,'ids',len(ids),'have',len(m),'missing',miss[:5],len(miss),'extra',extra)
if not miss and not extra:
    with open(f'{job}.jsonl','w',encoding='utf8') as f:
        for i in ids:
            v,r=m[i]
            f.write(json.dumps({"id":i,"verdict":"ACCEPT" if v=='A' else "REJECT","reason":r},ensure_ascii=False)+'\n')
    print('A',sum(1 for i in ids if m[i][0]=='A'),'R',sum(1 for i in ids if m[i][0]=='R'))
