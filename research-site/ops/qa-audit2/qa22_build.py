import json
ids=[l.strip() for l in open('research-site/ops/qa-audit2/ids_2.txt') if l.strip()]
v={}
for l in open('research-site/ops/qa-audit2/qa22_v.txt',encoding='utf8'):
    l=l.rstrip('\n')
    if not l: continue
    i,a,r=l.split('|',2); v[i]=('ACCEPT' if a=='A' else 'REJECT',r)
assert set(ids)==set(v) and len(ids)==len(v),(set(ids)-set(v),set(v)-set(ids))
with open('research-site/ops/qa-audit2/out_2.jsonl','w',encoding='utf8') as f:
    for i in ids: f.write(json.dumps({'id':i,'verdict':v[i][0],'reason':v[i][1]},ensure_ascii=False)+'\n')
print(len(ids))
