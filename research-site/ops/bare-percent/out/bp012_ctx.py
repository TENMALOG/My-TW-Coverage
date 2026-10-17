import json,sys,re
root='research-site/'
ids=sys.argv[1:]
cache={}
for i in ids:
    t=i.split('-')[0]
    d=json.load(open(f'{root}data/company-facts/{t}.json',encoding='utf8'))
    f=[x for x in d['facts'] if x['id']==i][0]
    txt=open(d['source']['text_path'].replace('audit-v5/','audit-v5/'),encoding='utf8').read()
    pages=re.split(r'\[PDF PAGE (\d+)\]',txt)
    pg={int(pages[k]):pages[k+1] for k in range(1,len(pages),2)}
    p=pg.get(f['page'],'')
    key=re.sub(r'\s+','',f['excerpts'][-1])[:6]
    lines=p.split('\n')
    idx=None
    for n,l in enumerate(lines):
        if re.sub(r'\s+','',l).startswith(key[:4]) or key in re.sub(r'\s+','',l): idx=n;break
    print('=====',i,f['page'])
    if idx is None: print('NOTFOUND');continue
    print('\n'.join(l for l in lines[max(0,idx-14):idx+10] if l.strip()))
