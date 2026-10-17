import json,re,sys
i,key,w=sys.argv[1],sys.argv[2],int(sys.argv[3])
tk=i.split('-AR-')[0]
d=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
t=open(d['source']['text_path'],encoding='utf8').read()
pages=re.split(r'\[PDF PAGE (\d+)\]',t)
pm={int(pages[k]):pages[k+1] for k in range(1,len(pages),2)}
f=[x for x in d['facts'] if x['id']==i][0]
n=re.sub(r'\s+','',pm[f['page']])
j=n.find(key)
print(i,j,n[max(0,j-w):j+w] if j>=0 else n[:300])
