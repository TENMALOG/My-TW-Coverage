import json,re,sys
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_100.txt') if l.strip()]
cache={}
def load(t):
    if t in cache: return cache[t]
    d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
    txt=open(d['source']['text_path'],encoding='utf8').read()
    pages={int(m.group(1)):m.group(2) for m in re.finditer(r'\[PDF PAGE (\d+)\]\n(.*?)(?=\n\[PDF PAGE \d+\]|\Z)',txt,re.S)}
    cache[t]=(d,pages);return cache[t]
t0=sys.argv[1]
for i in ids:
    t=i.split('-AR-')[0]
    if t!=t0: continue
    d,pages=load(t)
    f=[x for x in d['facts'] if x['id']==i][0]
    print('=====',i,f['field'],'|',f['period'],'|',f['attribution'],'| p',f['page'])
    print('STMT:',f['statement'])
    print('EXC:',f['excerpts'])
if len(sys.argv)>2:
    d,pages=load(t0)
    for p in sys.argv[2:]:
        print('---- PAGE',p);print(pages.get(int(p),'')[:4000])
