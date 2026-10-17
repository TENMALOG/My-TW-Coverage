import json,sys,re
sys.stdout.reconfigure(encoding='utf8')
R='research-site/'
ids=sys.argv[1:]
for i in ids:
    t=i.split('-AR-')[0]
    f=json.load(open(R+'data/company-facts/%s.json'%t,encoding='utf8'))
    fa=[x for x in f['facts'] if x['id']==i][0]
    txt=open(f['source']['text_path'],encoding='utf8').read()
    parts=re.split(r'\[PDF PAGE (\d+)\]',txt)
    pg={int(parts[k]):parts[k+1] for k in range(1,len(parts),2)}
    p=fa['page'];body=pg.get(p,'')+'\n<<NEXT>>\n'+pg.get(p+1,'')
    print('='*80);print(i,fa['statement'])
    key=fa['excerpts'][0].strip()[:8]
    j=body.find(key)
    if j<0: j=0
    print(body[max(0,j-700):j+1500])
