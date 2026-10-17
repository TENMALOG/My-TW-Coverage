import json,re,sys
t=sys.argv[1]; only=set(sys.argv[2:])
ids=set(l.strip() for l in open('research-site/ops/qa-audit4/ids_137.txt') if l.strip())
d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
txt=open(d['source']['text_path'],encoding='utf8').read()
parts=re.split(r'\[PDF PAGE (\d+)\]',txt)
pg={int(parts[i]):re.sub(r'\n\s*\n+','\n',parts[i+1]) for i in range(1,len(parts),2)}
def sq(s): return re.sub(r'\s+','',s)
if not only: print('=====',t,d['company'],d['legal_name'],d['source']['fy'])
for f in d['facts']:
    if f['id'] in ids and (not only or f['id'] in only):
        print('##',f['id'],f['field'],'|',f['period'],'| p',f['page'],'|',f['attribution'])
        print('  S:',f['statement'])
        p=f['page']
        body=pg.get(p,'')+'\n'+pg.get(p+1,'')[:1500]
        # build squeezed with index map
        idx=[i for i,c in enumerate(body) if not c.isspace()]
        sb=''.join(body[i] for i in idx)
        best=None
        for e in f['excerpts']:
            k=sq(e)[:30]
            j=sb.find(k)
            if j>=0: best=(j if best is None else best); 
            else: print('  [NOTFOUND',e[:30],']')
        if best is not None:
            # window anchored at the first found excerpt
            first=min(sb.find(sq(e)[:30]) for e in f['excerpts'] if sb.find(sq(e)[:30])>=0)
            a=idx[max(0,first-60)]; 
            print('  >>',body[a:a+(900 if only else 600)].replace('\n',' / '))
