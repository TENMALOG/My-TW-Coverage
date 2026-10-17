import json,sys,re
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_002.txt') if l.strip()]
a,b=int(sys.argv[1]),int(sys.argv[2])
cache={}
for i in ids[a:b]:
    t=i.split('-AR-')[0]
    if t not in cache:
        d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
        txt=open(d['source']['text_path'],encoding='utf8').read()
        parts=re.split(r'\[PDF PAGE (\d+)\]',txt)
        pg={int(parts[k]):parts[k+1] for k in range(1,len(parts),2)}
        cache[t]=(d,pg)
    d,pg=cache[t]
    f=[x for x in d['facts'] if x['id']==i][0]
    p=f['page']
    print('=====',i,d['company'],'|',f['field'],'|',f['period'],'|',f['attribution'],'| p',p)
    print('STMT:',f['statement']); print('EXC:',f['excerpts'])
    txt=pg.get(p,'')
    ex=f['excerpts'][0] if f['excerpts'] else ''
    k=txt.find(ex[:8]) if ex else -1
    if k<0: k=0
    print('PAGE:',txt[max(0,k-60):k+380].replace('\n',' / '))
    if False: print('NEXT:',pg.get(p+1,'')[:500].replace('\n',' / '))
