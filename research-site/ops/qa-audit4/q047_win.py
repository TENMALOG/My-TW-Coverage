import json,sys,re
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_047.txt') if l.strip()]
t0=sys.argv[1]; W=int(sys.argv[2]) if len(sys.argv)>2 else 600
d=json.load(open(f'research-site/data/company-facts/{t0}.json',encoding='utf8'))
txt=open(d['source']['text_path'],encoding='utf8').read()
for i in ids:
    if i.split('-AR-')[0]!=t0: continue
    f=[x for x in d['facts'] if x['id']==i][0]
    print('=====',i,f['field'],f['period'],f['attribution'],'p',f['page'])
    print('S:',f['statement'])
    pg=f['page']
    m=re.search(r'\[PDF PAGE %d\]\n(.*?)(?=\[PDF PAGE %d\]|\Z)'%(pg,pg+1),txt,re.S)
    s=m.group(1) if m else ''
    pos=-1
    for e in f['excerpts']:
        k=re.sub(r'\s+',' ',e)[:10]
        j=re.sub(r'[ \t]+',' ',s).find(k)
        if j>=0: pos=j;break
    ss=re.sub(r'[ \t]+',' ',s)
    if pos<0: print('(excerpt not found) E:',f['excerpts']); print(ss[:W*2])
    else: print(ss[max(0,pos-100):pos+W])
