import json,re,sys
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_034.txt') if l.strip()]
start,end=int(sys.argv[1]),int(sys.argv[2])
cache={}
def load(t):
    d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
    txt=open(d['source']['text_path'],encoding='utf8').read()
    pages=re.split(r'\n\[PDF PAGE (\d+)\]\n',txt)
    pg={int(pages[i]):pages[i+1] for i in range(1,len(pages)-1,2)}
    return d,pg
for i in ids[start:end]:
    t=i.split('-AR-')[0]
    if t not in cache: cache[t]=load(t)
    d,pg=cache[t]
    f=[x for x in d['facts'] if x['id']==i][0]
    p=f['page']
    print('='*30,i,d['company'],'|',f['field'],'|',f['period'],'|',f['attribution'],'| p',p)
    print('STMT:',f['statement'])
    print('EXC:',f['excerpts'])
    txt=pg.get(p,'??')
    norm=lambda x:re.sub(r'\s+','',x)
    pos=-1
    for e in f['excerpts']:
        k=txt.find(e[:12])
        if k>=0: pos=k;break
    a=0 if pos<0 else max(0,pos-100)
    print('--- PAGE',p,'@',pos); print(' / '.join(x for x in txt[a:a+600].split(chr(10)) if x.strip()))
    if '--next' in sys.argv: print('--- PAGE',p+1); print(pg.get(p+1,'')[:1500])
