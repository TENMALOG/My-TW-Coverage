import json,sys,re
d=json.load(open('research-site/ops/qa-audit4/emp_in_2.json',encoding='utf8'))
lo,hi=int(sys.argv[1]),int(sys.argv[2])
for it in d[lo:hi]:
    t=it['id'].split('-AR-')[0]
    f=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
    x=[y for y in f['facts'] if y['id']==it['id']][0]
    txt=open(f['source']['text_path'],encoding='utf8',errors='replace').read()
    parts=re.split(r'\[PDF PAGE (\d+)\]',txt)
    pages={int(parts[i]):parts[i+1] for i in range(1,len(parts),2)}
    pg=x['page']; pt=pages.get(pg,'')
    last=x['excerpts'][-1]
    key=re.sub(r'\s+','',last)
    # find position in whitespace-stripped text mapping
    idx=[];s=''
    for i,c in enumerate(pt):
        if not c.isspace(): idx.append(i); s+=c
    p=s.find(key)
    if p<0: p=s.find(re.sub(r'\s+','',x['excerpts'][0]))
    pos=idx[p] if p>=0 else 0
    print('=====',it['id'],f['company'],'|',x['statement'],'| pg',pg)
    print(re.sub(r'\s*\n\s*',' / ',pt[max(0,pos-650):pos+150]))
