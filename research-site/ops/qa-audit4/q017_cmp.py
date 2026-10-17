import json,re,sys
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_017.txt',encoding='utf8') if l.strip()]
start,end=int(sys.argv[1]),int(sys.argv[2])
cache={}
for n,i in enumerate(ids[start:end],start):
    t=i.split('-AR-')[0]
    if t not in cache:
        d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
        txt=open(d['source']['text_path'],encoding='utf8').read()
        pages=re.split(r'\[PDF PAGE (\d+)\]',txt)
        cache[t]=(d,{int(pages[k]):pages[k+1] for k in range(1,len(pages),2)})
    d,pm=cache[t]
    f=[x for x in d['facts'] if x['id']==i][0]
    print('=====',n,i,d['company'],f['field'],f['period'],'p',f['page'],'|',f['attribution'])
    print('STMT:',f['statement'])
    pg=pm.get(f['page'],'')
    nums=set(re.findall(r'\d[\d,\.]*\d|\d',f['statement']))
    nums={x for x in nums if len(x)>=3}
    lines=[l for l in pg.split('\n') if any(x in l for x in nums)]
    for l in lines[:6]: print('  >',re.sub(r'\s+',' ',l)[:200])
    # header lines
    hdr=[l for l in pg.split('\n') if re.search(r'年度|單位|占全|比率|比重',l)][:4]
    for l in hdr: print('  H',re.sub(r'\s+',' ',l)[:120])
