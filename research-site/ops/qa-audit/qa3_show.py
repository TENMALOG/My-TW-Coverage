import json,sys,re
ids=[l.strip() for l in open('research-site/ops/qa-audit/ids_3.txt') if l.strip()]
a,b=int(sys.argv[1]),int(sys.argv[2])
cache={}
for i in ids[a:b]:
    t=i.split('-')[0]
    d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
    f=[x for x in d['facts'] if x['id']==i][0]
    print('='*30,i,d['company'],f['field'],'|',f['attribution'],'|',f['period'],'p',f['page'])
    print('STMT:',f['statement'])
    print('EXC:',f['excerpts'])
    tp=d['source']['text_path']
    if tp not in cache: cache[tp]=open(tp,encoding='utf8').read()
    txt=cache[tp]
    pg=f['page']
    m=re.search(r'\[PDF PAGE %d\](.*?)(?=\[PDF PAGE %d\])'%(pg,pg+1),txt,re.S)
    s=m.group(1) if m else ''
    # locate first excerpt, show window
    ex=f['excerpts'][0][:12]
    k=s.find(ex)
    if k<0: k=0
    print('PAGE:',s[max(0,k-300):k+1500].replace('\n',' / '))
