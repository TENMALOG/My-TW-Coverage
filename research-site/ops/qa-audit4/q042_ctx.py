import json,re,sys
ids=sys.argv[1:]
for i in ids:
    tk=i.split('-AR-')[0]
    d=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
    t=open(d['source']['text_path'],encoding='utf8').read()
    pages=re.split(r'\[PDF PAGE (\d+)\]',t)
    pm={int(pages[k]):pages[k+1] for k in range(1,len(pages),2)}
    f=[x for x in d['facts'] if x['id']==i][0]
    pg=pm[f['page']]
    print('=====',i,'page',f['page'],'| STMT:',f['statement'])
    key=f['excerpts'][-1][:14]
    n=re.sub(r'\s+','',pg); k=re.sub(r'\s+','',key)
    j=n.find(k)
    print(n[max(0,j-500):j+500] if j>=0 else 'NOTFOUND '+n[:800])
