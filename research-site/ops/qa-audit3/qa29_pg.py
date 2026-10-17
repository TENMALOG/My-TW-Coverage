import json,re,sys
R='research-site/'
tk=sys.argv[1]; p=int(sys.argv[2]); n=int(sys.argv[3]); s=int(sys.argv[4]); e=int(sys.argv[5])
d=json.load(open(R+f'data/company-facts/{tk}.json',encoding='utf8'))
t=open(d['source']['text_path'],encoding='utf8').read()
m=re.search(r'\[PDF PAGE %d\]\n(.*?)(?=\[PDF PAGE %d\]|\Z)'%(p,p+n),t,re.S)
print(m.group(1)[s:e])
