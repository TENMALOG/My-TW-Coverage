import json,sys,re
ids=[l.strip() for l in open('research-site/ops/qa-audit3/ids_25.txt') if l.strip()]
start,end=int(sys.argv[1]),int(sys.argv[2])
cache={}
for n,i in enumerate(ids[start:end],start):
    t=i.split('-AR-')[0]
    d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
    f=[x for x in d['facts'] if x['id']==i][0]
    p=d['source']['text_path']
    if p not in cache: cache[p]=open(p,encoding='utf8').read()
    pp=re.split(r'\[PDF PAGE (\d+)\]',cache[p]); pages={int(pp[k]):pp[k+1] for k in range(1,len(pp),2)}
    print('='*20,n,i,d['company'],'p',f['page'],f['field'],'|',f['period'],'|',f['attribution'])
    print('STMT',f['statement'])
    print('EXC',[e[:150] for e in f['excerpts']])
    txt=pages.get(f['page'],'')+('\n[NEXT]\n'+pages.get(f['page']+1,'')[:600])
    # window
    pos=-1
    for e in f['excerpts']:
        k=txt.find(e[:15])
        if k>=0: pos=k;break
    if pos<0: pos=0
    a=max(0,pos-150); print(txt[a:a+480])
