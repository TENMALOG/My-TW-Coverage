import json,sys
inp=json.load(open('research-site/ops/qa-audit4/adj_in_b0.json',encoding='utf8'))
a,b=int(sys.argv[1]),int(sys.argv[2])
for it in inp[a:b]:
    i=it['id'];t=i.split('-')[0]
    d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
    facts=d['facts'] if isinstance(d,dict) and 'facts' in d else d
    f=[x for x in facts if x.get('id')==i]
    print('=====',i,'|',it['reviewer_reason'])
    if not f: print('NOTFOUND');continue
    print(json.dumps(f[0],ensure_ascii=False,indent=0))
