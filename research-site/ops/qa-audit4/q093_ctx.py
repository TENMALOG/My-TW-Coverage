import json,sys,re
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_093.txt') if l.strip()]
sel=sys.argv[1]
tk=sel
d=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
t=open(d['source']['text_path'],encoding='utf8').read()
parts=re.split(r'\[PDF PAGE (\d+)\]',t)
pg={int(parts[i]):parts[i+1] for i in range(1,len(parts),2)}
print(d['company'],d['source']['fy'])
for i in ids:
    if not i.startswith(tk+'-'): continue
    f=[x for x in d['facts'] if x['id']==i][0]
    print('=====',i,f['field'],'|',f['period'],'|',f['attribution'],'| p',f['page'])
    print('S:',f['statement'])
    P=pg.get(f['page'],'')
    # locate
    ns=''; mp=[]
    for k,c in enumerate(P):
        if not c.isspace(): ns+=c; mp.append(k)
    key=re.sub(r'\s','',f['excerpts'][-1]) if f['excerpts'] else ''
    j=ns.find(key)
    if j<0: j=ns.find(re.sub(r'\s','',f['excerpts'][0])); 
    if j<0: print('!! NOT FOUND'); continue
    a=mp[j]
    print(P[max(0,a-200):a+300].strip())
