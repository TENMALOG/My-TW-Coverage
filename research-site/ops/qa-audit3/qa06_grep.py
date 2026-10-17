import json,re,sys
R='research-site/'
id,pat,w=sys.argv[1],sys.argv[2],int(sys.argv[3])
tk=id.split('-AR-')[0]
d=json.load(open(R+f'data/company-facts/{tk}.json',encoding='utf8'))
t=open(d['source']['text_path'],encoding='utf8').read()
f=[x for x in d['facts'] if x['id']==id][0];p=f['page']
for q in (p,p+1):
    m=re.search(r'\[PDF PAGE %d\]\n(.*?)(?=\[PDF PAGE %d\]|\Z)'%(q,q+1),t,re.S)
    pg=m.group(1) if m else ''
    for mm in re.finditer(pat,pg):
        print('p',q,':',pg[max(0,mm.start()-w):mm.end()+w]);print('----')
