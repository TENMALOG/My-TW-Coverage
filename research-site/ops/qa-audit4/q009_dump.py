import json,re,sys,os
root='../../..'
ids=[l.strip() for l in open('ids_009.txt') if l.strip()]
a,b=int(sys.argv[1]),int(sys.argv[2])
cache={}
for id in ids[a:b]:
    tk=id.split('-AR-')[0]
    if tk not in cache:
        d=json.load(open(f'{root}/research-site/data/company-facts/{tk}.json',encoding='utf8'))
        t=open(f"{root}/"+d['source']['text_path'],encoding='utf8').read()
        pages=re.split(r'\[PDF PAGE (\d+)\]',t)
        pg={int(pages[i]):pages[i+1] for i in range(1,len(pages),2)}
        cache[tk]=(d,pg)
    d,pg=cache[tk]
    f=[x for x in d['facts'] if x['id']==id][0]
    print('=====',id,d['company'],f['field'],'|',f['attribution'],'|',f['period'],'p',f['page'])
    print('STMT:',f['statement'])
    print('EXC:',f['excerpts'])
    p=f['page']
    txt=pg.get(p,'')
    # compact
    txt=re.sub(r'[ \t]+',' ',txt); txt=re.sub(r'\n\s*\n+','\n',txt)
    n=lambda x:re.sub(r'\s+','',x)
    nt=n(txt); pos=-1
    for e in f['excerpts']:
        k=n(e)[:25]
        if k in nt: pos=nt.index(k); break
    if pos<0: print('PAGE(start, excerpt not located):',re.sub(r'\s+',' ',txt)[:1500])
    else:
        print('PAGE(window):',nt[max(0,pos-150):pos+650])
