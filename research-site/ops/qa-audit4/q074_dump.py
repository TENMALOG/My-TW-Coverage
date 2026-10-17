import json,re,sys
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_074.txt',encoding='utf8') if l.strip()]
want=sys.argv[1]
cache={}
pages={}
shown=set()
for i in ids:
    tk=i.split('-AR-')[0]
    if tk!=want: continue
    d=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
    if tk not in pages:
        t=open(d['source']['text_path'],encoding='utf8').read()
        parts=re.split(r'\[PDF PAGE (\d+)\]',t)
        pages[tk]={int(parts[k]):parts[k+1] for k in range(1,len(parts),2)}
    f=[x for x in d['facts'] if x['id']==i][0]
    print('='*30); print(i,f['field'],'|',f['period'],'|',f['attribution'],'| p',f['page'])
    print('STMT:',f['statement']); print('EXC:',f['excerpts'])
    p=f['page']
    for q in (p,p+1):
        if q in shown and q!=p: continue
        if (tk,q) in shown: 
            print(f'[page {q} shown above]'); continue
        shown.add((tk,q))
        print(f'--- PAGE {q} ---'); print(re.sub(r'[ \t]+',' ',pages[tk].get(q,'')) [:3500])
