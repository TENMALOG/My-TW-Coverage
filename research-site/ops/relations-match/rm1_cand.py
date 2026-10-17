import json,csv,glob,re,sys,os
sys.stdout.reconfigure(encoding='utf8')
cat={}
for r in csv.DictReader(open('catalog/release-scope-companies.csv',encoding='utf-8-sig')): cat[r['ticker']]=[r['company']]
for f in glob.glob('data/company-facts/*.json'):
    try:
        j=json.load(open(f,encoding='utf8'))
    except Exception: continue
    t=os.path.basename(f)[:-5]
    ln=None
    if isinstance(j,dict):
        ln=j.get('legal_name') or (j.get('company') or {}).get('legal_name') if isinstance(j.get('company'),dict) else j.get('legal_name')
    if ln: cat.setdefault(t,[]).append(ln)
def norm(s): return s.replace('臺','台').replace('股份有限公司','').replace('(股)公司','').replace('（股）公司','').replace('有限公司','')
d=json.load(open('ops/relations-match/in_1.json',encoding='utf8'))
for i,x in enumerate(d):
    c=x['counterparty'];n=norm(c);cands=[]
    for t,names in cat.items():
        for nm in names:
            m=norm(nm)
            if len(n)>=2 and len(m)>=2 and (n in m or m in n): cands.append((t,nm));break
    print(i,x['ticker'],x['company'],x['role'],c,'|',x['statement'][:80],'||',cands[:4])
