import json,sys,re,os
job=sys.argv[1]; a=int(sys.argv[2]); b=int(sys.argv[3])
R='research-site/'
ids=[l.strip() for l in open(R+'ops/codex-review/jobs_sonnet/'+job+'.txt',encoding='utf8') if l.strip()]
cache={}
def pages(path):
    if path not in cache:
        t=open(path,encoding='utf8').read()
        parts=re.split(r'\[PDF PAGE (\d+)\]',t)
        d={}
        for i in range(1,len(parts),2): d[int(parts[i])]=parts[i+1]
        cache[path]=d
    return cache[path]
def win(txt,exs,pre=200,post=250):
    # map nonspace chars
    idx=[i for i,c in enumerate(txt) if not c.isspace()]
    ns=''.join(txt[i] for i in idx)
    pos=[]
    for e in exs:
        en=re.sub(r'\s+','',e)
        k=ns.find(en[:20])
        if k>=0: pos.append((idx[k],idx[min(k+len(en),len(idx))-1]))
    if not pos: return None
    s=max(0,min(p[0] for p in pos)-pre); e=min(len(txt),max(p[1] for p in pos)+post)
    return txt[s:e]
for n,i in enumerate(ids[a:b],a):
    tk=i.split('-')[0]
    d=json.load(open(R+'data/company-facts/%s.json'%tk,encoding='utf8'))
    f=[x for x in d['facts'] if x['id']==i][0]
    pg=pages(d['source']['text_path'])
    print('=====',n,i,d['company'],'|',f['field'],'|',f['period'],'| p',f['page'],'|',f['attribution'])
    print('STMT:',f['statement'])
    print('EX:',' || '.join(f['excerpts']))
    txt=pg.get(f['page'],'')
    w=win(txt,f['excerpts'][:1]+f['excerpts'][-1:],150 if len(f["excerpts"])<3 else 250,200)
    if w is None:
        w=win(pg.get(f['page']+1,''),f['excerpts'][-1:])
        print('(excerpt on next page)')
        if w is None: w='NOT FOUND '+txt[:500]
    print('PAGE:',w.replace(chr(10),' / ')[:1100])
