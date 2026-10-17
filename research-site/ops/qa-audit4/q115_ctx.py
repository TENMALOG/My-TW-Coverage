import json, re, sys
cache={}
for i in sys.argv[1:]:
    tk=i.split('-AR-')[0]
    d=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
    t=open(d['source']['text_path'],encoding='utf8').read()
    f=next(x for x in d['facts'] if x['id']==i)
    pages={int(m.group(1)):m.group(2) for m in re.finditer(r'\[PDF PAGE (\d+)\]\n(.*?)(?=\n\[PDF PAGE \d+\]|\Z)',t,re.S)}
    pt=pages[f['page']]
    pt=re.sub(r'[ \t]+',' ',pt); 
    print('='*60,i,f['page']); print(f['statement'])
    for e in f['excerpts'][-1:]:
        k=re.sub(r'\s+','',e)[:12]
        flat=re.sub(r'\s+','',pt)
        j=flat.find(k)
        print('CTX:',flat[max(0,j-300):j+500] if j>=0 else 'NOTFOUND '+pt[:600])
