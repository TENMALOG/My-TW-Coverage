import json,sys,os,re
os.chdir(r"C:/Users/Neo Pegasus/Documents/ChatGPT/078-kaori sample/artifacts/stock-coverage-audit-20261003/incoming/latest-audit/My-TW-Coverage")
ids=[l.strip() for l in open('research-site/ops/qa-audit3/ids_14.txt',encoding='utf-8') if l.strip()]
a,b=int(sys.argv[1]),int(sys.argv[2])
full=len(sys.argv)>3
cache={};pc={}
def pages(d):
    p=d['source']['text_path']
    if p not in pc:
        txt=open(p,encoding='utf-8').read()
        parts=re.split(r'(?=\[PDF PAGE \d+\])',txt);pg={}
        for x in parts:
            m=re.match(r'\[PDF PAGE (\d+)\]',x)
            if m: pg[int(m.group(1))]=x
        pc[p]=pg
    return pc[p]
for i in ids[a:b]:
    t=i.split('-AR-')[0]
    if t not in cache: cache[t]=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf-8'))
    d=cache[t]; f=[x for x in d['facts'] if x['id']==i][0]
    print(f"=== {i} {d['company']} [{f['field']}] p{f['page']}\nST: {f['statement']}\nPER: {f.get('period')}\nATT: {f.get('attribution')}\nEX: {f['excerpts']}")
    if full:
        pg=pages(d); print('PAGE:',pg.get(int(f['page']),'MISSING')[:3500])
