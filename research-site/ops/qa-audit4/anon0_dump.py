import json,sys,io
sys.stdout.reconfigure(encoding='utf8')
inp=json.load(open('research-site/ops/qa-audit4/anon_in_0.json',encoding='utf8'))
a,b=int(sys.argv[1]),int(sys.argv[2])
for it in inp[a:b]:
    t=it['id'].split('-AR-')[0]
    d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
    facts=d['facts'] if isinstance(d,dict) and 'facts' in d else d
    f=[x for x in facts if x.get('id')==it['id']]
    print('=====',it['id'])
    print('STMT:',it['statement'])
    if f:
        f=f[0]
        print('PERIOD',f.get('period'),'PAGE',f.get('page'))
        print('EXC:',json.dumps(f.get('excerpts'),ensure_ascii=False)[:900])
    else: print('NOFACT')
