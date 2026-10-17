import json,sys
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_006.txt') if l.strip()]
cache={}
def pages(path):
    if path not in cache:
        t=open(path,encoding='utf8').read()
        cache[path]=t.split('\f')
    return cache[path]
for i in ids:
    tk=i.split('-AR-')[0]
    d=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
    f=[x for x in d['facts'] if x['id']==i][0]
    print('=====',i,d['company'],'|',f['field'],'|',f['period'],'|',f['attribution'],'| p',f['page'])
    print('STMT:',f['statement'])
    print('EXC:',' // '.join(f['excerpts']))
    if len(sys.argv)>1:
        pg=pages(d['source']['text_path'])
        p=f['page']
        print('PAGE(',len(pg),'):',pg[p-1][:3000] if p-1<len(pg) else 'NA')
