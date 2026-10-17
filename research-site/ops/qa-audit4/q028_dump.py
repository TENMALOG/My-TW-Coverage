import json,sys,re
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_028.txt',encoding='utf8') if l.strip()]
cache={}
out=[]
for i in ids:
    t=i.split('-AR-')[0]
    if t not in cache:
        d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
        txt=open(d['source']['text_path'],encoding='utf8').read()
        cache[t]=(d,txt)
    d,txt=cache[t]
    f=[x for x in d['facts'] if x['id']==i][0]
    out.append((i,d['company'],f,txt))
import pickle
pickle.dump({'ids':ids,'cache':cache},open('research-site/ops/qa-audit4/q028_cache.pkl','wb'))
t=cache[ids[0].split('-AR-')[0]][1]
print(len(t), t.count('\f'), repr(t[:300]))
