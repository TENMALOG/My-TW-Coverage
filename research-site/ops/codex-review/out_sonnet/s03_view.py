import json,sys,re,os
R='../../../'
job,a,b=sys.argv[1],int(sys.argv[2]),int(sys.argv[3])
W=int(sys.argv[4]) if len(sys.argv)>4 else 450
ids=[l.strip() for l in open(f'jobs_sonnet/{job}.txt',encoding='utf8') if l.strip()]
cache={}
last={}
for i,fid in enumerate(ids[a:b],a):
    t=fid.split('-')[0]
    if t not in cache:
        cache[t]=json.load(open(f'{R}research-site/data/company-facts/{t}.json',encoding='utf8')) if False else json.load(open(f'../../data/company-facts/{t}.json',encoding='utf8'))
    d=cache[t]
    f=[x for x in d['facts'] if x['id']==fid][0]
    txt=open(R+'../../../'*0+ '../../'+d['source']['text_path'],encoding='utf8').read() if False else open('../../../'+d['source']['text_path'],encoding='utf8').read()
    pg=f['page']
    parts=re.split(r'\[PDF PAGE (\d+)\]',txt)
    pages={int(parts[k]):parts[k+1] for k in range(1,len(parts),2)}
    print(f'#### {i} {fid} {d["company"]} p{pg} [{f["field"]}] attr={f["attribution"]} period={f["period"]}')
    print('STMT:',f['statement'])
    for e in f['excerpts']:
        print('EXC:',e[:300])
    p=pages.get(pg,'')
    spans=[]
    for e in f['excerpts']:
        k=p.find(e[:30])
        if k<0: k=p.find(e[:12])
        if k>=0: spans.append((max(0,k-W),min(len(p),k+len(e)+W)))
    spans.sort()
    m=[]
    for s in spans:
        if m and s[0]<=m[-1][1]: m[-1]=(m[-1][0],max(m[-1][1],s[1]))
        else: m.append(s)
    for s in m: print('PAGE>>',p[s[0]:s[1]].replace('\n',' | '))
    if not m: print('PAGE(nofind)>>',p[:800].replace('\n',' | '))
    n=pages.get(pg+1,'')
    if any(not e in p for e in f['excerpts']): print('P+1>>',n[:350].replace('\n',' | '))
