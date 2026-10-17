import json,sys,re
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_035.txt',encoding='utf8') if l.strip()]
want=sys.argv[1]; W=int(sys.argv[2]) if len(sys.argv)>2 else 400
d=json.load(open(f'research-site/data/company-facts/{want}.json',encoding='utf8'))
t=open(d['source']['text_path'],encoding='utf8').read()
pages=re.split(r'\[PDF PAGE (\d+)\]',t)
pg={int(pages[i]):pages[i+1] for i in range(1,len(pages),2)}
def ns(s): return re.sub(r'\s+','',s)
for i in ids:
    if i.split('-AR-')[0]!=want: continue
    f=[x for x in d['facts'] if x['id']==i][0]
    print('\n==',i,f['field'],'|',f['period'],'|',f['attribution'],'| p',f['page'])
    print('S:',f['statement'])
    print('EX:',' || '.join(e.replace('\n',' ') for e in f['excerpts']))
    txt=pg.get(f['page'],'')+pg.get(f['page']+1,'')
    idx=[m.start() for m in re.finditer(r'\S',txt)]
    flat=''.join(txt[k] for k in idx)
    ps=[flat.find(ns(e)[:20]) for e in f['excerpts'] if ns(e)]
    ps=[p for p in ps if p>=0]
    if not ps: print('!! not found'); continue
    lo=min(ps); hi=max(ps)+len(ns(f['excerpts'][-1]))
    a=idx[max(0,lo-W)]; b=idx[min(len(idx)-1,hi+W)]
    print('CTX:',re.sub(r'\s*\n\s*',' / ',txt[a:b]))
