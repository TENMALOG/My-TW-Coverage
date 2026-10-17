import json,re,sys
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_048.txt') if l.strip()]
cache={}
def load(t):
    if t not in cache:
        d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
        txt=open(d['source']['text_path'],encoding='utf8').read()
        cache[t]=(d,txt)
    return cache[t]
lo,hi=int(sys.argv[1]),int(sys.argv[2])
for i in ids[lo:hi]:
    t=i.split('-AR-')[0]
    d,txt=load(t)
    f=[x for x in d['facts'] if x['id']==i][0]
    print('=====',i,d['company'],f['field'],'| period:',f['period'],'| attr:',f['attribution'],'| page',f['page'])
    print('STATEMENT:',f['statement'])
    print('EXCERPTS:',f['excerpts'])
    if '--page' in sys.argv:
        pass
