import json,sys,re
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_031.txt') if l.strip()]
cache={}
def pg(path,p):
    if path not in cache:
        t=open(path,encoding='utf-8').read()
        parts=re.split(r'\n\[PDF PAGE (\d+)\]\n',t)
        dd={}
        for k in range(1,len(parts),2): dd[int(parts[k])]=parts[k+1]
        cache[path]=dd
    return cache[path]
start,end=int(sys.argv[1]),int(sys.argv[2])
W=int(sys.argv[3]) if len(sys.argv)>3 else 350
for i in ids[start:end]:
    tk=i.split('-AR-')[0]
    d=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf-8'))
    f=[x for x in d['facts'] if x['id']==i][0]
    print('=====',i,d['company'],'|',f['field'],'|',f.get('period'),'|',f.get('attribution'),'| p',f['page'])
    print('STMT:',f['statement'])
    dd=pg(d['source']['text_path'],f['page'])
    p=dd.get(f['page'],'')
    # window: from first excerpt to last excerpt
    pos=[p.find(e.split('\n')[0][:20]) for e in f['excerpts']]
    pos=[x for x in pos if x>=0]
    if pos:
        a=max(0,min(pos)-W); b=min(len(p),max(pos)+W)
        print('PAGE:',p[a:b])
    else:
        print('EXC NOT FOUND; page head:',p[:1200])
