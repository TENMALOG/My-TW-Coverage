import json,sys,re
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_145.txt') if l.strip()]
cache={}
def pages(path):
    if path not in cache:
        t=open(path,encoding='utf8').read()
        cache[path]=re.split(r'\f',t)
    return cache[path]
tk=None
for i in ids:
    t=i.split('-AR-')[0]
    d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
    f=[x for x in d['facts'] if x['id']==i][0]
    print('=====',i,d['company'],f['field'],f['period'],f['attribution'],'p',f['page'])
    print('S:',f['statement'])
    print('E:',f['excerpts'])
    pg=pages(d['source']['text_path'])
    p=f['page']
    if len(sys.argv)>1:
        pass
    if p-1<len(pg):
        txt=pg[p-1]
        # show a window around the first excerpt
        print('PAGE(len',len(txt),'pages',len(pg),'):',txt[:int(sys.argv[1]) if len(sys.argv)>1 else 1500])
