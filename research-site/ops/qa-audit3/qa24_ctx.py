import json,re,sys
for i in sys.argv[1:]:
    t=i.split('-AR-')[0]
    d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
    f=[x for x in d['facts'] if x['id']==i][0]
    txt=open(d['source']['text_path'],encoding='utf8').read()
    pg=re.split(r'\n?\[PDF PAGE (\d+)\]\n',txt)
    pm={int(pg[k]):pg[k+1] for k in range(1,len(pg),2)}
    p=f['page']; s=pm.get(p,'MISSING')
    ex=f['excerpts'][-1]
    key=re.sub(r'\s+','',ex)
    flat=s
    # locate by first 6 non-space chars of last excerpt line
    k=ex.split('\n')[0][:6]
    pos=s.find(k)
    if pos<0: pos=0
    print('=====',i,'p',p,'pos',pos,'len',len(s))
    print(s[max(0,pos-200):pos+550])
