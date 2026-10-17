import json,sys,re
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_032.txt',encoding='utf8') if l.strip()]
cache={}
lo,hi=int(sys.argv[1]),int(sys.argv[2])
W=int(sys.argv[3]) if len(sys.argv)>3 else 1200
for i in ids[lo:hi]:
    t=i.split('-AR-')[0]
    if t not in cache:
        d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
        txt=open(d['source']['text_path'],encoding='utf8').read()
        parts=re.split(r'\[PDF PAGE (\d+)\]',txt)
        pages={int(parts[k]):parts[k+1] for k in range(1,len(parts),2)}
        cache[t]=(d,pages)
    d,pages=cache[t]
    f=[x for x in d['facts'] if x['id']==i][0]
    p=f['page']
    print('=====',i,f['field'],'|',f['period'],'|',f['attribution'],'| page',p)
    print('STMT:',f['statement'])
    pg=pages.get(p,'')+pages.get(p+1,'')[:600]
    pgn=re.sub(r'\s+',' ',pg)
    # locate excerpt
    pos=-1
    for ex in f['excerpts']:
        key=re.sub(r'\s+','',ex)[:8]
        m=re.search(r'\s*'.join(map(re.escape,key)),pgn)
        if m: pos=m.start();break
    if pos<0: print('!!excerpt not found on page; EXC:',f['excerpts']); print(pgn[:W]);continue
    print(pgn[max(0,pos-200):pos+W])
