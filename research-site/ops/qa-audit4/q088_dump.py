import json,sys,re
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_088.txt') if l.strip()]
if len(sys.argv)>3: sel=sys.argv[3:]
else: sel=ids[int(sys.argv[1]):int(sys.argv[2])]
cache={}
W=7
for i in sel:
    t=i.split('-AR-')[0]
    d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
    f=[x for x in d['facts'] if x['id']==i][0]
    tp=d['source']['text_path']
    if tp not in cache:
        txt=open(tp,encoding='utf8').read()
        parts=re.split(r'\[PDF PAGE (\d+)\]',txt)
        cache[tp]={int(parts[k]):parts[k+1] for k in range(1,len(parts),2)}
    pages=cache[tp]
    p=f['page']
    print('=====',i,d['company'],f['field'],'|',f['period'],'|',f['attribution'],'| page',p)
    print('STMT:',f['statement']);print('EXC:',f['excerpts'])
    lines=pages.get(p,'').split('\n')
    key=re.sub(r'\s','',f['excerpts'][-1])[:5]
    idx=None
    for n,l in enumerate(lines):
        if key in re.sub(r'\s','',l): idx=n;break
    if idx is None:
        print('--KEY NOT FOUND--'); idx=0
    print('--PAGE',p,'line',idx,'--');print('\n'.join(lines[max(0,idx-W):idx+W]))
