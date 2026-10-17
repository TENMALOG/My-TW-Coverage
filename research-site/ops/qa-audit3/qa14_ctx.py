import json,os,re,sys
os.chdir(r"C:/Users/Neo Pegasus/Documents/ChatGPT/078-kaori sample/artifacts/stock-coverage-audit-20261003/incoming/latest-audit/My-TW-Coverage")
ids=[l.strip() for l in open('research-site/ops/qa-audit3/ids_14.txt',encoding='utf-8') if l.strip()]
a,b=int(sys.argv[1]),int(sys.argv[2])
cache={};pc={}
for i in ids[a:b]:
    t=i.split('-AR-')[0]
    d=cache.setdefault(t,json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf-8')))
    f=[x for x in d['facts'] if x['id']==i][0]
    p=d['source']['text_path']
    if p not in pc:
        txt=open(p,encoding='utf-8').read();pg={}
        for x in re.split(r'(?=\[PDF PAGE \d+\])',txt):
            m=re.match(r'\[PDF PAGE (\d+)\]',x)
            if m: pg[int(m.group(1))]=x
        pc[p]=pg
    pg=pc[p];pgn=int(f['page'])
    body=pg.get(pgn,'')+pg.get(pgn+1,'')
    print('=====',i,f['statement'])
    ex=[e for e in f['excerpts'] if len(re.sub(r'\s','',e))>=4]
    key=ex[-1] if ex else f['excerpts'][-1]
    pat=r'\s*'.join(re.escape(c) for c in re.sub(r'\s+','',key))
    m=re.search(pat,body)
    if not m:
        key=f['excerpts'][0]; pat=r'\s*'.join(re.escape(c) for c in re.sub(r'\s+','',key)); m=re.search(pat,body)
    if m:
        s=max(0,m.start()-int(sys.argv[3])); print(body[s:m.end()+int(sys.argv[4])])
    else: print('NOTFOUND')
