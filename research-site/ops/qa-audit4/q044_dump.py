import json,sys,re,os
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_044.txt') if l.strip()]
cache={}
out=[]
for i in ids:
    t=i.split('-AR-')[0]
    if t not in cache:
        d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
        txt=open(d['source']['text_path'],encoding='utf8').read()
        cache[t]=(d,{f['id']:f for f in d['facts']},txt)
    d,fm,txt=cache[t]
    f=fm.get(i)
    print('='*30,i,d['company'])
    if not f: print('MISSING');continue
    print({k:v for k,v in f.items() if k not in('verification','id')})
