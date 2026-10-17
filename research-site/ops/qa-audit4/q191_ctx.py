import json,sys,re
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_191.txt',encoding='utf-8') if l.strip()]
tick=sys.argv[1]; W=int(sys.argv[2]) if len(sys.argv)>2 else 500
d=json.load(open(f'research-site/data/company-facts/{tick}.json',encoding='utf-8'))
txt=open(d['source']['text_path'],encoding='utf-8').read()
pages=re.split(r'\n\[PDF PAGE (\d+)\]\n',txt)
P={int(pages[i]):pages[i+1] for i in range(1,len(pages),2)}
for i in ids:
    if i.split('-AR-')[0]!=tick: continue
    f=[x for x in d['facts'] if x['id']==i][0]
    pg=P.get(f['page'],'')
    print('=====',i,f['field'],'|',f['period'],'|',f['attribution'],'| p',f['page'])
    print('S:',f['statement'])
    ex=f['excerpts'][0]
    key=re.sub(r'\s','',ex)[:12]
    flat=pg
    # locate by whitespace-insensitive search
    idx=-1
    pos=[];s=''
    for k,c in enumerate(pg):
        if not c.isspace(): pos.append(k); s+=c
    m=s.find(key)
    if m<0: print('!! excerpt not found on page'); print(pg[:W*2]); continue
    st=pos[m]
    print('CTX:',pg[max(0,st-W//2):st+W*2].replace('\n',' / '))
