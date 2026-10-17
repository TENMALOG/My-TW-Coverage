import json,sys
d=json.load(open('research-site/ops/qa-audit4/adj_in_b1.json',encoding='utf8'))
for it in d:
    t=it['id'].split('-')[0]
    f=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
    fa=[x for x in f['facts'] if x.get('id')==it['id']]
    print('=====',it['id'],'| REASON:',it['reviewer_reason'])
    if not fa: print('NOFACT', list(f['facts'][0])); continue
    x=fa[0]
    print(json.dumps(x,ensure_ascii=False))
