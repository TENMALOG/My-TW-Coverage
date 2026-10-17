import json,re,sys
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_017.txt',encoding='utf8') if l.strip()]
start,end=int(sys.argv[1]),int(sys.argv[2])
cache={}
for i in ids[start:end]:
    t=i.split('-AR-')[0]
    if t not in cache:
        d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
        txt=open(d['source']['text_path'],encoding='utf8').read()
        pages=re.split(r'\[PDF PAGE (\d+)\]',txt)
        pm={int(pages[k]):pages[k+1] for k in range(1,len(pages),2)}
        cache[t]=(d,pm)
    d,pm=cache[t]
    f=[x for x in d['facts'] if x['id']==i][0]
    print('=====',i,d['company'],f['field'],f['period'],'p',f['page'],'|',f['attribution'])
    print('STMT:',f['statement'])
    print('EXC:',f['excerpts'])
    p=f['page']
    pg=pm.get(p,'')
    # show window around first excerpt
    ex=f['excerpts'][0]
    idx=pg.find(ex[:12])
    s=max(0,idx-150) if idx>=0 else 0
    print('PAGE:',re.sub(r'[ \t]+',' ',pg[s:s+700]).replace('\n\n','\n'))
