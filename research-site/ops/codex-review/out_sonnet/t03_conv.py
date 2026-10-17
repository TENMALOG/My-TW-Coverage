import sys,json
job=sys.argv[1]
ids=[l.strip() for l in open(f'../jobs_sonnet/{job}.txt',encoding='utf8') if l.strip()]
dec={}
for l in open(f't03_dec_{job}.txt',encoding='utf8'):
    l=l.rstrip('\n')
    if not l: continue
    i,v,r=l.split('|',2); dec[i]=(v,r)
miss=[i for i in ids if i not in dec]; extra=[i for i in dec if i not in ids]
print(job,'missing',miss,'extra',extra)
if not miss and not extra:
    with open(f'{job}.jsonl','w',encoding='utf8') as f:
        for i in ids:
            v,r=dec[i]; f.write(json.dumps({"id":i,"verdict":"ACCEPT" if v=='A' else "REJECT","reason":r},ensure_ascii=False)+'\n')
    print('A',sum(1 for i in ids if dec[i][0]=='A'),'R',sum(1 for i in ids if dec[i][0]=='R'))
