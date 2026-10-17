import json,re,sys,os
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_126.txt',encoding='utf8') if l.strip()]
cache={}
for i in ids:
    t=i.split('-AR-')[0]
    if t not in cache:
        d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
        txt=open(d['source']['text_path'],encoding='utf8').read()
        cache[t]=(d,txt)
    d,txt=cache[t]
    f=[x for x in d['facts'] if x['id']==i]
    if not f: print('##',i,'MISSING');continue
    f=f[0]
    print('##',i,d['company'],'|',f['field'],'|',f['period'],'|',f['attribution'],'| p',f['page'])
    print('S:',f['statement'])
    print('E:',f['excerpts'])
