import json,csv,glob,re,os
cat={}
for r in csv.DictReader(open('catalog/release-scope-companies.csv',encoding='utf-8-sig')):
    cat[r['ticker']]=[r['company']]
for t in cat:
    p='data/company-facts/%s.json'%t
    if os.path.exists(p):
        try:
            j=json.load(open(p,encoding='utf-8'))
            def find(o):
                if isinstance(o,dict):
                    for k,v in o.items():
                        if k=='legal_name' and isinstance(v,str):return v
                        r=find(v)
                        if r:return r
                elif isinstance(o,list):
                    for v in o:
                        r=find(v)
                        if r:return r
            ln=find(j)
            if ln:cat[t].append(ln)
        except Exception as e:pass
def norm(s):
    s=s.replace('臺','台').replace('股份有限公司','').replace('(股)公司','').replace('有限公司','').replace('(股)','').replace('（股）','')
    return re.sub(r'[\s()（）,\.]','',s).lower()
d=json.load(open('ops/relations-match/in_2.json',encoding='utf-8'))
out=open('ops/relations-match/rm2_cands.txt','w',encoding='utf-8')
for i,x in enumerate(d):
    c=norm(x['counterparty'])
    hits=[]
    for t,ns in cat.items():
        for n in ns:
            nn=norm(n)
            if len(nn)>=2 and len(c)>=2 and (nn==c or (len(c)>=3 and nn in c) or (len(nn)>=3 and c in nn) or (len(c)>=2 and nn.startswith(c))):
                hits.append('%s:%s'%(t,'/'.join(ns)));break
    out.write('%d|%s|%s\n'%(i,x['counterparty'],'; '.join(hits[:6])))
