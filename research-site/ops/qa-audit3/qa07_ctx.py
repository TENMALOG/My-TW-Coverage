import json,re,sys
R='research-site/'
tk,p,key=sys.argv[1],int(sys.argv[2]),sys.argv[3]
w=int(sys.argv[4]) if len(sys.argv)>4 else 700
d=json.load(open(R+f'data/company-facts/{tk}.json',encoding='utf8'))
t=open(d['source']['text_path'],encoding='utf8').read()
m=re.search(r'\[PDF PAGE %d\]\n(.*?)(?=\[PDF PAGE %d\]|\Z)'%(p,p+1),t,re.S)
pg=m.group(1)
for mm in re.finditer(re.escape(key),pg):
    i=mm.start(); print('-----');print(pg[max(0,i-w):i+w]); break
else: print('NOKEY',len(pg)); print(pg[:1500])
