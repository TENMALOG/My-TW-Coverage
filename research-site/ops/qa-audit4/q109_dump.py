import json,sys
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_109.txt') if l.strip()]
tks=sorted(set(i.split('-AR-')[0] for i in ids))
for tk in tks:
    d=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
    print('\n=====',tk,d['company'],d['source']['fy'],d['source']['text_path'])
    for f in d['facts']:
        if f['id'] in ids:
            print('##',f['id'],f['field'],f['period'],'p',f['page'],f['attribution']);print(f['statement']);print('EX:',f['excerpts'])
