import json,re,sys
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_074.txt',encoding='utf8') if l.strip()]
want=sys.argv[1]; sel=sys.argv[2:] 
d=json.load(open(f'research-site/data/company-facts/{want}.json',encoding='utf8'))
t=open(d['source']['text_path'],encoding='utf8').read()
parts=re.split(r'\[PDF PAGE (\d+)\]',t)
pages={int(parts[k]):re.sub(r'[ \t]+',' ',parts[k+1]) for k in range(1,len(parts),2)}
for i in ids:
    if i.split('-AR-')[0]!=want: continue
    if sel and i.split('-AR-')[1] not in sel: continue
    f=[x for x in d['facts'] if x['id']==i][0]
    print('='*20); print(i,f['field'],'|',f['period'],'|',f['attribution'],'| p',f['page'])
    print('STMT:',f['statement']); print('EXC:',f['excerpts'])
    p=f['page']; txt=pages.get(p,'')+'\n<<NEXT>>\n'+pages.get(p+1,'')[:1200]
    pos=-1
    for e in f['excerpts']:
        k=re.sub(r'\s+','',e)
        # find loosely
        m=txt.find(e[:12])
        if m>=0: pos=m;break
    if pos<0: print('!!excerpt not found'); print(txt[:2000]); continue
    print('...',txt[max(0,pos-100):pos+550])
