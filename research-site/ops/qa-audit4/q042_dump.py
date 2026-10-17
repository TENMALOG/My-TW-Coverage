import json,re,sys
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_042.txt') if l.strip()]
lo,hi=int(sys.argv[1]),int(sys.argv[2])
cache={}
for i in ids[lo:hi]:
    tk=i.split('-AR-')[0]
    if tk not in cache:
        d=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
        t=open(d['source']['text_path'],encoding='utf8').read()
        pages=re.split(r'\[PDF PAGE (\d+)\]',t)
        pm={int(pages[k]):pages[k+1] for k in range(1,len(pages),2)}
        cache[tk]=(d,pm)
    d,pm=cache[tk]
    f=[x for x in d['facts'] if x['id']==i][0]
    print('=====',i,d['company'],f['field'],'| period:',f.get('period'),'| attr:',f.get('attribution'),'| page',f['page'])
    print('STMT:',f['statement'])
    for e in f['excerpts']: print('EXC:',e.replace('\n',' '))
    if '--page' in sys.argv:
        print('PAGE:',pm.get(f['page'],'')[:3000])
