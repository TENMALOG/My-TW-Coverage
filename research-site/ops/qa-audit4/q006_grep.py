import json,sys,re
i=sys.argv[1]; kw=sys.argv[2]; W=int(sys.argv[3]) if len(sys.argv)>3 else 700
tk=i.split('-AR-')[0]
d=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
f=[x for x in d['facts'] if x['id']==i][0]
t=open(d['source']['text_path'],encoding='utf8').read()
parts=re.split(r'\[PDF PAGE (\d+)\]',t); pg={int(parts[k]):parts[k+1] for k in range(1,len(parts),2)}
txt=pg.get(f['page'],'')+pg.get(f['page']+1,'')
m=re.search(r'\s*'.join(re.escape(c) for c in kw),txt)
print('page',f['page'], 'FOUND' if m else 'NOT FOUND')
if m: print(re.sub(r'[ \t]+',' ',txt[max(0,m.start()-150):m.start()+W]))
