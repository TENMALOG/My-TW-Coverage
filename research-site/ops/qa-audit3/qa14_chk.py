import json,os,re
os.chdir(r"C:/Users/Neo Pegasus/Documents/ChatGPT/078-kaori sample/artifacts/stock-coverage-audit-20261003/incoming/latest-audit/My-TW-Coverage")
ids=[l.strip() for l in open('research-site/ops/qa-audit3/ids_14.txt',encoding='utf-8') if l.strip()]
n=lambda s:re.sub(r'\s+','',s)
cache={};pc={}
for i in ids:
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
    body=n(pg.get(pgn,'')+pg.get(pgn+1,''))
    miss=[e for e in f['excerpts'] if n(e) not in body]
    if miss: print(i,'MISSING',miss)
