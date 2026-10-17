import json,sys
inp=json.load(open('adj_in_a.json',encoding='utf-8'))
a,b=int(sys.argv[1]),int(sys.argv[2])
for it in inp[a:b]:
    t=it['id'].split('-')[0]
    d=json.load(open(f'../../data/company-facts/{t}.json',encoding='utf-8'))
    f=[x for x in d['facts'] if x['id']==it['id']][0]
    print('=====',it['id'],'swept' if it['already_swept'] else '')
    print('REASON:',it['reviewer_reason'])
    print('STMT:',f['statement']);print('PERIOD:',f.get('period'),'PAGE',f.get('page'),'ATTR',f.get('attribution'),'FIELD',f.get('field'))
    for e in f['excerpts']:print('  EX:',e[:300])
