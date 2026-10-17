import json,re,sys
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_198.txt') if l.strip()]
cache={}
def pages(tk):
    d=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
    t=open(d['source']['text_path'],encoding='utf8').read()
    parts=re.split(r'\n\[PDF PAGE (\d+)\]\n',t)
    return d,{int(parts[i]):parts[i+1] for i in range(1,len(parts),2)}
want=sys.argv[1:]
for i in ids:
    tk=i.split('-AR-')[0]
    if want and tk not in want: continue
    if tk not in cache: cache[tk]=pages(tk)
    d,pg=cache[tk]
    f=[x for x in d['facts'] if x['id']==i][0]
    p=f['page']
    print('=====',i,'|',f['field'],'|',f['period'],'|',f['attribution'],'| p',p)
    print('STMT:',f['statement'])
    txt=re.sub(r'[ \t]+',' ',pg.get(p,'')+'\n'+pg.get(p+1,'')[:0])
    nz=[j for j,c in enumerate(txt) if not c.isspace()]
    flat=''.join(txt[j] for j in nz)
    ok=False
    for e in sorted(f['excerpts'],key=len,reverse=True):
        k=flat.find(re.sub(r'\s','',e)[:10])
        if k>=0:
            a=nz[k]; print('PAGE:',txt[max(0,a-120):a+420].replace('\n','/')); ok=True; break
    if not ok: print('NOMATCH',f['excerpts'])
