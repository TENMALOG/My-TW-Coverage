import json,re,sys
R='research-site/'
id=sys.argv[1]; n=int(sys.argv[2]) if len(sys.argv)>2 else 2500
tk=id.split('-AR-')[0]
d=json.load(open(R+f'data/company-facts/{tk}.json',encoding='utf8'))
t=open(d['source']['text_path'],encoding='utf8').read()
f=[x for x in d['facts'] if x['id']==id][0]
p=f['page']
m=re.search(r'\[PDF PAGE %d\]\n(.*?)(?=\[PDF PAGE %d\]|\Z)'%(p,p+1),t,re.S)
print(id,f['statement']);print(re.sub(r'\n\s*\n','\n',m.group(1))[:n])
