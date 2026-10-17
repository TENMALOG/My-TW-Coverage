import json,sys,re
sys.stdout.reconfigure(encoding='utf8')
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_091.txt') if l.strip()]
want=sys.argv[1]; n=int(sys.argv[2])
cache={}
for i in ids:
    t=i.split('-AR-')[0]
    if t!=want or int(i.split('-AR-')[1])<int(sys.argv[3]): continue
    d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
    f=[x for x in d['facts'] if x['id']==i][0]
    p=d['source']['text_path']
    if p not in cache:
        txt=open(p,encoding='utf8').read()
        cache[p]=dict((int(a),b) for a,b in re.findall(r'\[PDF PAGE (\d+)\](.*?)(?=\[PDF PAGE \d+\]|\Z)',txt,re.S))
    pages=cache[p]
    pg=f['page']
    print('=====',i,f['field'],'|',f['period'],'|',f['attribution'],'| p',pg)
    print('STMT:',f['statement'])
    print('EXC:',[re.sub(r'\s+',' ',e) for e in f['excerpts']])
    pt=pages.get(pg,'')+pages.get(pg+1,'')[:600]
    pn=re.sub(r'\s+','',pt)
    shown=False
    for e in reversed(f['excerpts']):
        k=re.sub(r'\s+','',e)
        j=pn.find(k)
        if j>=0 and len(k)>6:
            print('CTX:',pt and pn[max(0,j-n//3):j+len(k)+n//2]); shown=True; break
    if not shown: print('NOTFOUND; PAGE:',re.sub(r'[ \t]+',' ',pt)[:n*3])
