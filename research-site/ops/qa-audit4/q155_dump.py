import json,sys,re
a,b=int(sys.argv[1]),int(sys.argv[2]); W=int(sys.argv[3]) if len(sys.argv)>3 else 700
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_155.txt',encoding='utf8') if l.strip()]
C={}
def load(t):
    if t not in C:
        d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
        tx=open(d['source']['text_path'],encoding='utf8').read()
        pg={}
        for m in re.finditer(r'\[PDF PAGE (\d+)\]\n(.*?)(?=\n\[PDF PAGE \d+\]|\Z)',tx,re.S): pg[int(m.group(1))]=m.group(2)
        C[t]=(d,pg)
    return C[t]
sq=lambda s:re.sub(r'\s+','',s)
for i in ids[a:b]:
    t=i.split('-AR-')[0]; d,pg=load(t)
    f=[x for x in d['facts'] if x['id']==i][0]
    print('=====',i,f['field'],'|',f['period'],'|p',f['page'],'|',f['attribution'][:6])
    print('S:',f['statement'])
    txt=sq(pg.get(f['page'],''))
    k=-1
    for e in f['excerpts']:
        k=txt.find(sq(e)[:10])
        if k>=0: break
    if k<0: print('P(NOTFOUND p-start):',txt[:W])
    else: print('P:',txt[max(0,k-150):k+W])
