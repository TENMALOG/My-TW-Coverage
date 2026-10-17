import json
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_180.txt') if l.strip()]
for i in ids:
    t=i.split('-AR-')[0]
    d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
    f=[x for x in d['facts'] if x['id']==i][0]
    print(i,f['field'],f['attribution'],f['page'])
