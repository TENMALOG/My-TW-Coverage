import json,re,sys
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_067.txt') if l.strip()]
want=sys.argv[1]
cache={}
for i in ids:
    tk=i.split('-AR-')[0]
    if tk!=want: continue
    d=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf-8'))
    if tk not in cache:
        t=open(d['source']['text_path'],encoding='utf-8').read()
        cache[tk]=dict((int(m.group(1)),m.start()) for m in re.finditer(r'\[PDF PAGE (\d+)\]',t)),t
    pos,t=cache[tk]
    f=[x for x in d['facts'] if x['id']==i][0]
    print('=====',i,f['field'],f['period'],'| attr:',f['attribution'],'| p',f['page'])
    print('STMT:',f['statement'])
    print('EXC:',f['excerpts'])
    if '--page' in sys.argv:
        p=f['page']; s=pos[p]; e=pos.get(p+1,len(t))
        print('PAGE:',re.sub(r'[ \t]+',' ',re.sub(r'\n\s*\n+','\n',t[s:e]))[:2500])
