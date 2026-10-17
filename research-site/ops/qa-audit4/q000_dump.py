import json,re,sys
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_000.txt') if l.strip()]
lo,hi=int(sys.argv[1]),int(sys.argv[2]); W=int(sys.argv[3]) if len(sys.argv)>3 else 500
cache={}
for id in ids[lo:hi]:
    tk=id.split('-AR-')[0]
    d=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
    if tk not in cache:
        t=open(d['source']['text_path'],encoding='utf8').read()
        parts=re.split(r'\[PDF PAGE (\d+)\]',t)
        cache[tk]={int(parts[i]):parts[i+1] for i in range(1,len(parts),2)}
    f=[x for x in d['facts'] if x['id']==id][0]
    p=f['page']; tx=cache[tk].get(p,'')
    print('='*60);print(id,d['company'],'|',f['field'],'|',f['period'],'|',f['attribution'],'| p',p)
    print('STMT:',f['statement'])
    ex=f['excerpts'][0] if f['excerpts'] else ''
    i=tx.find(ex[:25]) if ex else -1
    if i<0: i=0; print('!!excerpt not on page')
    print('CTX:',tx[max(0,i-W//3):i+len(ex)+W].replace('\t',' '))
