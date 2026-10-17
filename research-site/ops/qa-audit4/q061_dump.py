import json,re,sys
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_061.txt') if l.strip()]
tick=sys.argv[1]
cache={}
for i in ids:
    t=i.split('-AR-')[0]
    if t!=tick: continue
    d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
    if t not in cache:
        cache[t]=open(d['source']['text_path'],encoding='utf8').read()
    txt=cache[t]
    f=[x for x in d['facts'] if x['id']==i][0]
    print('='*20,i,'|',d['company'],'| field',f['field'],'| period',f['period'],'| page',f['page'],'| attr',f['attribution'])
    print('STMT:',f['statement'])
    print('EXC:',f['excerpts'])
    p=f['page']
    m=re.search(r'\[PDF PAGE %d\]\n(.*?)(?=\[PDF PAGE %d\]|\Z)'%(p,p+1),txt,re.S)
    pg=m.group(1) if m else ""
    k=[pg.find(e[:8]) for e in f["excerpts"] if pg.find(e[:8])>=0]
    s=max(0,(min(k) if k else 0)-300)
    print("PAGE TEXT:", pg[s:s+650].replace(chr(10)," "))
