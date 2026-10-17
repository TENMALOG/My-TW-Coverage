import json,re,sys
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_196.txt',encoding='utf8') if l.strip()]
a,b=int(sys.argv[1]),int(sys.argv[2])
cache={}
last=None
for id in ids[a:b]:
    tk=id.split('-AR-')[0]
    if tk not in cache:
        d=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
        t=open(d['source']['text_path'],encoding='utf8').read()
        pg={int(m.group(1)):None for m in re.finditer(r'\[PDF PAGE (\d+)\]',t)}
        parts=re.split(r'\[PDF PAGE (\d+)\]',t)
        pages={int(parts[i]):parts[i+1] for i in range(1,len(parts),2)}
        cache[tk]=(d,pages)
    d,pages=cache[tk]
    f=[x for x in d['facts'] if x['id']==id][0]
    print('=====',id,d['company'],'|',f['field'],'|',f['period'],'|',f['attribution'],'| p',f['page'])
    print('S:',f['statement'])
    if tk!=last:
        pass
    p=f['page']
    txt=re.sub(r'[ \t]+',' ',pages.get(p,'')) 
    ex=f['excerpts'][0] if f['excerpts'] else ''
    key=re.sub(r'\s+','',ex)[:6]
    # find region
    flat=txt
    i=flat.find(ex[:8])
    if i<0: i=0
    print('P:',flat[max(0,i-80):i+800].replace('\n',' / '))
    last=tk
