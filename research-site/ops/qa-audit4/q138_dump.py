import json,re,sys,os
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_138.txt') if l.strip()]
cache={}
def pages(t):
    return t
for i in ids:
    tk=i.split('-AR-')[0]
    if tk not in cache:
        d=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
        txt=open(d['source']['text_path'],encoding='utf8').read()
        cache[tk]=(d,txt)
    d,txt=cache[tk]
    f=[x for x in d['facts'] if x['id']==i][0]
    print('=====',i,f['field'],'|',f['period'],'|p',f['page'],'|',f['attribution'])
    print('S:',f['statement'])
    print('E:',' // '.join(f['excerpts']))
