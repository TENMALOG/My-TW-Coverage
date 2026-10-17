import json,re,sys
i=sys.argv[1]; kw=sys.argv[2]; b=int(sys.argv[3]) if len(sys.argv)>3 else 300; a=int(sys.argv[4]) if len(sys.argv)>4 else 700
tk=i.split('-AR-')[0]
d=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
f=[x for x in d['facts'] if x['id']==i][0]
t=open(d['source']['text_path'],encoding='utf8').read()
parts=re.split(r'\[PDF PAGE (\d+)\]',t)
pages={int(parts[k]):parts[k+1] for k in range(1,len(parts),2)}
pg=pages.get(f['page'],'')+'\n[[NEXT]]\n'+pages.get(f['page']+1,'')
k=pg.find(kw)
print('##',i,'fy',d['source']['fy'],'found' if k>=0 else 'NOTFOUND')
if k>=0: print(pg[max(0,k-b):k+a])
