import json,sys,re
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_095.txt') if l.strip()]
t0=sys.argv[1]
d=json.load(open(f'research-site/data/company-facts/{t0}.json',encoding='utf8'))
txt=open(d['source']['text_path'],encoding='utf8').read()
parts=re.split(r'\[PDF PAGE (\d+)\]',txt)
pages={int(parts[k]):parts[k+1] for k in range(1,len(parts),2)}
print(d['company'])
for i in ids:
    if i.split('-AR-')[0]!=t0: continue
    f=next(x for x in d['facts'] if x['id']==i)
    print('=====',i,f['field'],f['period'],f['attribution'],'p',f['page'])
    print('S:',f['statement'])
    p=f['page']
    lines=[l for l in (pages.get(p,'')+'\n'+pages.get(p+1,'')).split('\n') if l.strip()]
    keep=set()
    for e in f['excerpts']:
        key=re.sub(r'\s+','',e)[:8]
        for n,l in enumerate(lines):
            if key in re.sub(r'\s+','',l):
                keep.update(range(max(0,n-2),min(len(lines),n+4)));break
        else: print('!! nf',e[:40])
    prev=-2
    for n in sorted(keep):
        if n!=prev+1: print('  ...')
        print(lines[n]); prev=n
