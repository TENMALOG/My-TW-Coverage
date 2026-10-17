import json,sys,os
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_093.txt') if l.strip()]
cache={}
def pages(tp):
    if tp not in cache:
        t=open(tp,encoding='utf8').read()
        cache[tp]=t.split('\f')
    return cache[tp]
byt={}
for i in ids:
    tk=i.split('-AR-')[0]
    if tk not in byt: byt[tk]=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
sel=sys.argv[1]
for i in ids:
    tk=i.split('-AR-')[0]
    if tk!=sel: continue
    d=byt[tk]
    f=[x for x in d['facts'] if x['id']==i][0]
    print('=====',i,f['field'],'|',f['period'],'|',f['attribution'],'| p',f['page'])
    print('S:',f['statement'])
    print('E:',f['excerpts'])
    if i==[x for x in ids if x.startswith(tk+'-')][0]:
        P=pages(d['source']['text_path'])
        print('npages',len(P))
