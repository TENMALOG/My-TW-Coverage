import json,re,sys
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_049.txt') if l.strip()]
cache={}
def load(t):
    if t not in cache:
        d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
        txt=open(d['source']['text_path'],encoding='utf8').read()
        pages=re.split(r'\[PDF PAGE (\d+)\]',txt)
        pg={int(pages[i]):pages[i+1] for i in range(1,len(pages),2)}
        cache[t]=(d,pg)
    return cache[t]
lo,hi=int(sys.argv[1]),int(sys.argv[2]); W=int(sys.argv[3]) if len(sys.argv)>3 else 1200
for i in ids[lo:hi]:
    t=i.split('-AR-')[0]
    d,pg=load(t)
    f=[x for x in d['facts'] if x['id']==i][0]
    print('=====',i,d['company'],f['field'],'| period:',f['period'],'| attr:',f['attribution'],'| page',f['page'])
    print('STATEMENT:',f['statement'])
    print('EXCERPTS:',f['excerpts'])
    p=f['page']; txt=pg.get(p,'')+'\n--NEXT--\n'+pg.get(p+1,'')
    ex=f['excerpts'][0] if f['excerpts'] else ''
    k=txt.find(ex[:15]) if ex else -1
    if k<0: k=0
    print('PAGE:',txt[max(0,k-W//3):k+W])
