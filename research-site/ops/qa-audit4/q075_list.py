import json
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_075.txt',encoding='utf8') if l.strip()]
for i in ids:
    tk=i.split('-AR-')[0]
    d=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
    f=[x for x in d['facts'] if x['id']==i][0]
    print(i,'|',f['field'],'|',f['period'],'|',f['attribution'],'| p',f['page'])
    print('  S:',f['statement']); print('  E:',json.dumps(f['excerpts'],ensure_ascii=False)[:500])
