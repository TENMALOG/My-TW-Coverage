import json,sys,re
job=sys.argv[1]; start=int(sys.argv[2]); end=int(sys.argv[3])
ids=[l.strip() for l in open(f'research-site/ops/codex-review/jobs_sonnet/{job}.txt',encoding='utf8') if l.strip()][start:end]
cache={}
def load(t):
    if t not in cache:
        d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
        txt=open(d['source']['text_path'],encoding='utf8').read()
        pages=re.split(r'\[PDF PAGE (\d+)\]',txt)
        pg={int(pages[i]):pages[i+1] for i in range(1,len(pages)-1,2)}
        cache[t]=(d,pg)
    return cache[t]
shown=set()
for n,i in enumerate(ids):
    t=i.split('-')[0]
    d,pg=load(t)
    f=[x for x in d['facts'] if x['id']==i][0]
    p=f['page']
    if (t,p) not in shown:
        shown.add((t,p))
        txt=re.sub(r'\s+',' ',pg.get(p,''))
        poss=[txt.find(e[:12]) for e in f['excerpts']]
        poss=[x for x in poss if x>=0] or [0]
        s=max(0,min(poss)-250)
        print(f'##### PAGE {t} {d["company"]} p{p}:',txt[s:s+1500])
        if min(poss)==0 and not any(x>=0 for x in [txt.find(e[:12]) for e in f['excerpts']]):
            print('  [excerpt not on page; next page:]',re.sub(r'\s+',' ',pg.get(p+1,''))[:1200])
    print(f'== {start+n} {i} {f["field"]}|{f["period"]}|{f["attribution"]}')
    print('S:',f['statement'])
    print('E:',' // '.join(f['excerpts']))
