import json,re,sys
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_051.txt') if l.strip()]
cache={}
def pages(tp):
    if tp not in cache:
        t=open(tp,encoding='utf8').read()
        parts=re.split(r'\[PDF PAGE (\d+)\]',t)
        cache[tp]={int(parts[i]):parts[i+1] for i in range(1,len(parts),2)}
    return cache[tp]
last=None
for i in ids:
    tk=i.split('-AR-')[0]
    d=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
    f=[x for x in d['facts'] if x['id']==i][0]
    print('=====',i,d['company'],f['field'],'|',f['period'],'|',f['attribution'],'| p',f['page'])
    print('STMT:',f['statement'])
    print('EXC:',f['excerpts'])
    if len(sys.argv)>1 and sys.argv[1]=='pages':
        pg=pages(d['source']['text_path'])
        key=(tk,f['page'])
        print('PAGE%d:'%f['page'],pg.get(f['page'],'')[:2500])
