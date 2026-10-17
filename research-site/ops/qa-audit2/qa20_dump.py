import json,re,sys,io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
ids=[l.strip() for l in open('research-site/ops/qa-audit2/ids_0.txt') if l.strip()]
a,b=int(sys.argv[1]),int(sys.argv[2])
cache={}
for i in ids[a:b]:
    t=i.split('-')[0]
    d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
    f=[x for x in d['facts'] if x['id']==i][0]
    p=d['source']['text_path']
    if p not in cache:
        cache[p]=re.split(r'\[PDF PAGE (\d+)\]',open(p,encoding='utf8').read())
    s=cache[p]; pages={int(s[k]):s[k+1] for k in range(1,len(s),2)}
    print('=====',i,d['company'],f['field'],'|',f['period'],'| p',f['page'],'|',f['attribution'])
    print('ST:',f['statement']); print('EX:',f['excerpts'])
    pg=pages.get(f['page'],'')
    ex=f['excerpts'][0]; pos=pg.find(ex)
    lo=max(0,pos-300); print('PAGE:',pg[lo:lo+1300].replace('\n',' / '))
    n=pages.get(f['page']+1,'')
    if len(f['excerpts'])>1 and pg.find(f['excerpts'][-1])<0: print('NEXT:',n[:900].replace('\n',' / '))
