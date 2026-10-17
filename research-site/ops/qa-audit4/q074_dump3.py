import json,re,sys
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_074.txt',encoding='utf8') if l.strip()]
want=sys.argv[1]
d=json.load(open(f'research-site/data/company-facts/{want}.json',encoding='utf8'))
t=open(d['source']['text_path'],encoding='utf8').read()
parts=re.split(r'\[PDF PAGE (\d+)\]',t)
pages={int(parts[k]):parts[k+1] for k in range(1,len(parts),2)}
def win(txt,excs,before=150,after=900):
    ns=[];idx=[]
    for i,c in enumerate(txt):
        if not c.isspace(): ns.append(c); idx.append(i)
    ns=''.join(ns)
    for e in excs:
        k=re.sub(r'\s+','',e)
        for L in (len(k),20,10):
            m=ns.find(k[:L])
            if m>=0:
                s=idx[m]; return re.sub(r'[ \t]+',' ',txt[max(0,s-before):s+after])
    return None
for i in ids:
    if i.split('-AR-')[0]!=want: continue
    f=[x for x in d['facts'] if x['id']==i][0]
    print('='*10,i,f['field'],'|',f['period'],'|',f['attribution'],'| p',f['page'])
    print('STMT:',f['statement']); 
    p=f['page']
    w=win(pages.get(p,''),f['excerpts'])
    if w is None:
        w=win(pages.get(p+1,''),f['excerpts'])
        print('(found on next page)' if w else '!!NOT FOUND')
        if w is None: w=re.sub(r'[ \t]+',' ',pages.get(p,''))[:1500]
    print(w)
