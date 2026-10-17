import json,sys,re
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_120.txt') if l.strip()]
lo,hi=int(sys.argv[1]),int(sys.argv[2])
cache={}
def norm(s): return re.sub(r'\s+','',s)
for i in ids[lo:hi]:
    t=i.split('-AR-')[0]
    d=cache.setdefault(t,json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8')))
    f=[x for x in d['facts'] if x['id']==i][0]
    txt=open(d['source']['text_path'],encoding='utf8').read()
    pages=re.split(r'\n?\[PDF PAGE \d+\]\n',txt)[1:]
    p=f['page']
    print('='*60);print(i,d['company'],f['field'],f['period'],'|',f['attribution'],'| p',p)
    print('STMT:',f['statement'])
    pg=pages[p-1]+'\n'+(pages[p] if p<len(pages) else '')
    # build normalized with index map
    idx=[];ns=[]
    for k,c in enumerate(pg):
        if not c.isspace(): ns.append(c);idx.append(k)
    nstr=''.join(ns)
    ex=f['excerpts']
    first=norm(ex[0]);last=norm(ex[-1])
    a=nstr.find(first[:30]);b=nstr.find(last[-30:])
    if a<0: print('EXC NOT FOUND',ex);continue
    s=max(0,idx[a]-150);e=idx[min(len(idx)-1,(b if b>=0 else a)+len(last)+40)]+250
    print('CTX:',re.sub(r'[ \t]+',' ',pg[s:e]))
