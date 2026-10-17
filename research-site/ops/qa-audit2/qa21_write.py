import json,sys,collections
sys.stdout.reconfigure(encoding='utf-8')
d='research-site/ops/qa-audit2/'
ids=[l.strip() for l in open(d+'ids_1.txt',encoding='utf-8') if l.strip()]
v={}
for l in open(d+'qa21_v.tsv',encoding='utf-8'):
    l=l.rstrip('\n')
    if not l: continue
    i,a,r=l.split('|',2); v[i]=(a,r)
miss=[i for i in ids if i not in v]; print('missing',miss, 'extra',[i for i in v if i not in ids])
with open(d+'out_1.jsonl','w',encoding='utf-8') as f:
    for i in ids:
        a,r=v[i]; f.write(json.dumps({"id":i,"verdict":"ACCEPT" if a=='A' else "REJECT","reason":r},ensure_ascii=False)+'\n')
c=collections.Counter(x[0] for x in v.values()); print(c)
