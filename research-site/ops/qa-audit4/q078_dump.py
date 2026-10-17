import json,re,sys
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_078.txt',encoding='utf-8') if l.strip()]
want=sys.argv[1]
cache={}
out=[]
for i in ids:
    t=i.split('-AR-')[0]
    if t!=want: continue
    d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf-8'))
    if t not in cache:
        txt=open(d['source']['text_path'],encoding='utf-8').read()
        cache[t]=dict((int(m.group(1)),m.group(2)) for m in re.finditer(r'\[PDF PAGE (\d+)\]\n(.*?)(?=\n\[PDF PAGE \d+\]|\Z)',txt,re.S))
    f=[x for x in d['facts'] if x['id']==i][0]
    print('=====',i,f['field'],'|',f['period'],'| p',f['page'],'|',f['attribution'])
    print('STMT:',f['statement']);print('EXC:',f['excerpts'])
    if '--pages' in sys.argv:
        for p in (f['page'],f['page']+1):
            print(f'--- page {p}');print(re.sub(r'[ \u3000]{2,}',' ',cache[t].get(p,''))[:int(sys.argv[sys.argv.index('--pages')+1])])
