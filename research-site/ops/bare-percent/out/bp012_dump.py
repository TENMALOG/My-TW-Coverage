import json,sys
d=json.load(open('research-site/ops/bare-percent/jobs_sonnet/bp012.json',encoding='utf8'))
a,b=int(sys.argv[1]),int(sys.argv[2])
cache={}
for it in d[a:b]:
    t=it['id'].split('-')[0]
    if t not in cache: cache[t]=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
    for f in cache[t]['facts']:
        if f.get('id')==it['id']:
            print('=====',it['id'])
            print(json.dumps({k:f[k] for k in ('statement','period','page','excerpts','attribution')},ensure_ascii=False))
