import json,re,sys
root='../../../'
ids=[l.strip() for l in open('ids_024.txt',encoding='utf8') if l.strip()]
start,end=int(sys.argv[1]),int(sys.argv[2])
cache={}
def pages(t):
    txt=open(root+t,encoding='utf8',errors='replace').read()
    parts=re.split(r'\[PDF PAGE (\d+)\]',txt)
    return {int(parts[i]):parts[i+1] for i in range(1,len(parts),2)}
for id in ids[start:end]:
    tk=id.split('-AR-')[0]
    d=json.load(open(root+f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
    f=[x for x in d['facts'] if x['id']==id][0]
    tp=d['source']['text_path']
    if tp not in cache: cache[tp]=pages(tp)
    P=cache[tp]
    print('='*30,id,d['company'])
    print('FIELD',f['field'],'| PERIOD',f.get('period'),'| ATTR',f['attribution'],'| PAGE',f['page'])
    print('STMT',f['statement'])
    print('EXC',f['excerpts'])
    pg=f['page']
    for p in (pg,):
        t=P.get(p,'')
        t=re.sub(r'[ \t]+',' ',t); t=re.sub(r'\n\s*\n+','\n',t)
        # trim to window around first excerpt
        ex=f['excerpts'][0] if f['excerpts'] else ''
        key=re.sub(r'\s+','',ex)[:8]
        tt=t
        print('--PAGE',p,'len',len(t))
        W=int(sys.argv[3]) if len(sys.argv)>3 else 1400
        idx=[i for i,c in enumerate(tt) if not c.isspace()]
        comp=''.join(tt[i] for i in idx)
        pos=-1
        for e in f['excerpts']:
            k=re.sub(r'\s+','',e)[:10]
            pos=comp.find(k)
            if pos>=0: break
        st=idx[pos] if pos>=0 else 0
        st=max(0,st-250)
        print(tt[st:st+W])
