import json,re,sys
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_045.txt') if l.strip()]
lo,hi=int(sys.argv[1]),int(sys.argv[2]); W=int(sys.argv[3]) if len(sys.argv)>3 else 600
cache={}
def norm(s): return re.sub(r'\s+','',s)
for i in ids[lo:hi]:
    tk=i.split('-AR-')[0]
    if tk not in cache:
        d=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
        t=open(d['source']['text_path'],encoding='utf8').read()
        pages={int(m.group(1)):m.group(2) for m in re.finditer(r'\[PDF PAGE (\d+)\]\n(.*?)(?=\n\[PDF PAGE \d+\]\n|\Z)',t,re.S)}
        cache[tk]=(d,pages)
    d,pages=cache[tk]
    f=[x for x in d['facts'] if x['id']==i][0]
    print('=====',i,d['company'],'|',f['field'],'|',f['period'],'|',f['attribution'],'| p',f['page'])
    print('STMT:',f['statement'])
    pg=pages.get(f['page'],'')
    # context: lines around the first excerpt found, keep line structure
    lines=[l.strip() for l in pg.split('\n') if l.strip()]
    flat='\n'.join(lines)
    k=-1
    for e in f['excerpts']:
        e0=e.strip()[:10]
        k=flat.find(e0)
        if k>=0: break
    if k<0: print('(excerpt anchor not found) EXC:',f['excerpts'])
    k=max(k,0)
    print('CTX:',flat[max(0,k-150):k+W])
