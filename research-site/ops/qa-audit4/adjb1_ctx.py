import json,sys,re
W=int(__import__('os').environ.get('W','500'))
for id_ in sys.argv[1:]:
    t=id_.split('-')[0]
    f=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
    x=[a for a in f['facts'] if a['id']==id_][0]
    txt=open(f['source']['text_path'],encoding='utf8').read()
    m=re.search(r'\[PDF PAGE %d\]\n(.*?)(?=\[PDF PAGE %d\]|\Z)'%(x['page'],x['page']+1),txt,re.S)
    pg=m.group(1)
    print('#####',id_,'len',len(pg))
    k=x['excerpts'][-1][:8]
    i=pg.find(k)
    if i<0:
        k2=x['excerpts'][0][:6]; i=pg.find(k2)
    print(pg[max(0,i-W):i+W] if i>=0 else pg[:2*W])
