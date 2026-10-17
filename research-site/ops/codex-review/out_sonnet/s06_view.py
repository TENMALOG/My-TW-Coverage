import json,sys,re
ids=[l.strip() for l in open(sys.argv[1]) if l.strip()]
cache={}
for i in ids:
    t=i.split('-')[0]
    if t not in cache:
        d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
        txt=open(d['source']['text_path'],encoding='utf8').read()
        pages=re.split(r'\[PDF PAGE (\d+)\]',txt)
        pg={int(pages[k]):pages[k+1] for k in range(1,len(pages),2)}
        cache[t]=(d,pg)
    d,pg=cache[t]
    f=[x for x in d['facts'] if x['id']==i][0]
    print('=====',i,f['field'],'| p',f['page'],'|',f['period'],'|',f['attribution'])
    print('STMT:',f['statement'])
    print('EXC:',json.dumps(f['excerpts'],ensure_ascii=False))
    if len(sys.argv)>2:
        p=f['page']
        for q in (p,p+1):
            s=pg.get(q,'')
            print(f'--- page {q} ({len(s)}c)')
            print(s[:int(sys.argv[2])])
