import json,sys,re
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_006.txt') if l.strip()]
a,b=int(sys.argv[1]),int(sys.argv[2]); W=int(sys.argv[3])
cache={}
for i in ids[a:b]:
    tk=i.split('-AR-')[0]
    d=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
    f=[x for x in d['facts'] if x['id']==i][0]
    p=d['source']['text_path']
    if p not in cache:
        t=open(p,encoding='utf8').read(); parts=re.split(r'\[PDF PAGE (\d+)\]',t); cache[p]={int(parts[k]):parts[k+1] for k in range(1,len(parts),2)}
    pg=cache[p]
    txt=pg.get(f['page'],'')+pg.get(f['page']+1,'')[:800]
    print('=====',i,f['statement'][:90])
    found=False
    for ex in f['excerpts']:
        k=re.sub(r'\s+','',ex)[:8]
        m=re.search(r'\s*'.join(re.escape(c) for c in k),txt)
        if m:
            j=m.start()
            print(re.sub(r'[ \t]+',' ',txt[max(0,j-100):j+W])); found=True; break
    if not found: print('NOT FOUND')
