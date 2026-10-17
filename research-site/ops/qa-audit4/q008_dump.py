import json,sys,re
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_008.txt') if l.strip()]
lo,hi=int(sys.argv[1]),int(sys.argv[2])
cache={}
def getpage(t,p):
    m=re.search(r'\[PDF PAGE %d\]\n(.*?)(?=\[PDF PAGE %d\]|\Z)'%(p,p+1),t,re.S)
    return m.group(1) if m else ''
for i in ids[lo:hi]:
    t=i.split('-AR-')[0]
    d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
    f=[x for x in d['facts'] if x['id']==i][0]
    tp=d['source']['text_path']
    if tp not in cache: cache[tp]=open(tp,encoding='utf8').read()
    p=f['page']
    print('='*80);print(i,d['company'],f['field'],'|',f['period'],'|',f['attribution'],'| page',p)
    print('STMT:',f['statement']);print('EXC:',f['excerpts'])
    txt=getpage(cache[tp],p)
    # collapse spaces
    txt=re.sub(r'[ \t]+',' ',txt)
    print('--page',p,'len',len(txt)); print(txt[:int(sys.argv[3]) if len(sys.argv)>3 else 1800])
