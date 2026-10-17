import json,sys,re
def page(i,extra=0):
    t=i.split('-AR-')[0]
    d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
    f=[x for x in d['facts'] if x['id']==i][0]
    txt=open(d['source']['text_path'],encoding='utf8').read()
    parts=re.split(r'\[PDF PAGE (\d+)\]',txt)
    pg={int(parts[k]):parts[k+1] for k in range(1,len(parts),2)}
    return f,pg
if __name__=='__main__':
    for i in sys.argv[1:]:
        f,pg=page(i)
        print('#####',i,f['page']); print(pg.get(f['page'],'NOPAGE'))
