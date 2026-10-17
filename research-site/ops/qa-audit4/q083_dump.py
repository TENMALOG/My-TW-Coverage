import json,sys,re
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_083.txt') if l.strip()]
cache={}
def load(t):
    if t in cache: return cache[t]
    d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
    txt=open(d['source']['text_path'],encoding='utf8').read()
    pages=txt.split('\f')
    cache[t]=(d,pages); return cache[t]
for i in ids:
    t=i.split('-AR-')[0]
    d,pages=load(t)
    f=[x for x in d['facts'] if x['id']==i][0]
    print('=====',i,d['company'],'|',f['field'],'|',f['period'],'|p',f['page'],'|',f['attribution'])
    print('STMT:',f['statement'])
    print('EXC:',f['excerpts'])
    if len(sys.argv)>1 and sys.argv[1]=='pg':
        p=f['page']
        print('PAGES',len(pages))
        for q in (p,):
            print('--- page',q); print(pages[q-1][:2500] if q-1<len(pages) else 'NA')
