import json,re,sys
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_053.txt') if l.strip()]
tk=sys.argv[1]
d=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
t=open(d['source']['text_path'],encoding='utf8').read()
pages={}
for s in t.split('[PDF PAGE ')[1:]:
    n,_,b=s.partition(']');pages[int(n)]=b
W=int(sys.argv[2]) if len(sys.argv)>2 else 700
for f in d['facts']:
    if f['id'] not in ids: continue
    print('=====',f['id'],f['field'],'|',f['period'],'|',f['attribution'],'| p',f['page'])
    print('STMT:',f['statement'])
    print('EXC:',f['excerpts'])
    for pg in (f['page'],f['page']+1):
        txt=pages.get(pg,'')
        for e in f['excerpts'][:3]:
            k=re.sub(r'\s','',e)[:8]
            # find in whitespace-collapsed text mapping
            idx=[m.start() for m in re.finditer('.',txt)]
            comp=''.join(c for c in txt if not c.isspace())
            pos=[i for i,c in enumerate(txt) if not c.isspace()]
            j=comp.find(k)
            if j>=0:
                s=pos[j]; print(f'--p{pg} ctx:',txt[max(0,s-W//3):s+W].replace('\n',' / ')); break
        else: continue
        break
    else: print('!! excerpt start not found on page/next')
