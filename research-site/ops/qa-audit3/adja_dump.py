import json,sys
sys.stdout.reconfigure(encoding='utf8')
R='research-site/'
d=json.load(open(R+'ops/qa-audit3/adj_in_a.json',encoding='utf8'))
for it in d:
    i=it['id'];t=i.split('-AR-')[0]
    f=json.load(open(R+'data/company-facts/%s.json'%t,encoding='utf8'))
    fa=[x for x in f['facts'] if x['id']==i][0]
    txt=open(f['source']['text_path'],encoding='utf8').read()
    pages=txt.split('\f')
    p=fa['page']
    print('='*100);print(i,'FY',f['source']['fy'],f['company'],'pages',len(pages))
    print('REASON:',it['reviewer_reason'])
    print('STMT:',fa['statement']);print('PERIOD:',fa['period'],'PAGE',p,'ATTR',fa['attribution'],'FIELD',fa['field'])
    for e in fa['excerpts']: print('EXC:',e)
    if '--page' in sys.argv:
        for q in (p,p+1):
            if 0<q<=len(pages): print('--- page',q);print(pages[q-1][:3500])
