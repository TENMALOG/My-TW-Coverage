import json,sys,os,glob
root='research-site/data/company-facts/'
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_180.txt',encoding='utf8') if l.strip()]
cache={}
def load(t):
    if t not in cache: cache[t]=json.load(open(root+t+'.json',encoding='utf8'))
    return cache[t]
d=load(ids[0].split('-AR-')[0])
print(list(d.keys()))
for k,v in d.items():
    if k!='facts': print(k,str(v)[:400])
f=d['facts'][0] if 'facts' in d else None
print(json.dumps(f,ensure_ascii=False)[:1500])
