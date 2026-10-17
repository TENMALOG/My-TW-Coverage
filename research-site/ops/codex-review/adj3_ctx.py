import json,sys,re
R='research-site/'
out=json.load(open(R+'ops/codex-review/adj3_dump.json',encoding='utf-8'))
ids=sys.argv[1:]
B=500
for o in out:
    if o['id'] not in ids: continue
    t=o['id'].split('-')[0]
    d=json.load(open(R+f'data/company-facts/{t}.json',encoding='utf-8'))
    txt=open(d['source']['text_path'],encoding='utf-8').read()
    parts=re.split(r'\[PDF PAGE (\d+)\]',txt)
    pages={int(parts[i]):parts[i+1] for i in range(1,len(parts),2)}
    pg=o['pg']
    s=pages.get(pg,'')+'\n##NEXT##\n'+pages.get(pg+1,'')
    flat=s
    # locate: last excerpt's first 5 non-space chars sequence loosely
    key=re.sub(r'\s','',o['ex'][-1])[:6]
    pat=r'\s*'.join(re.escape(c) for c in key)
    m=re.search(pat,flat)
    print('=====',o['id'],o['st'][:70])
    if m:
        j=m.start(); print(flat[max(0,j-B):j+250])
    else: print('NOTFOUND key',key)
