import json,re,sys,os
root='../../..'
ids=[l.strip() for l in open('ids_101.txt',encoding='utf8') if l.strip()]
cache={}
def pages(path):
    if path not in cache:
        t=open(os.path.join(root,path),encoding='utf8',errors='replace').read()
        parts=re.split(r'\[PDF PAGE (\d+)\]',t)
        cache[path]={int(parts[i]):parts[i+1] for i in range(1,len(parts),2)}
    return cache[path]
lo,hi=int(sys.argv[1]),int(sys.argv[2])
B=int(os.environ.get('B','12')); A=int(os.environ.get('A','6'))
for id in ids[lo:hi]:
    tk=id.split('-AR-')[0]
    d=json.load(open(f'{root}/research-site/data/company-facts/{tk}.json',encoding='utf8'))
    f=[x for x in d['facts'] if x['id']==id][0]
    print('=====',id,d['company'],f['field'],'p',f['page'],f['period'],f['attribution'])
    print('STMT:',f['statement'])
    print('EXC:',f['excerpts'])
    P=pages(d['source']['text_path'])
    for p in (f['page'],f['page']+1):
        txt=re.sub(r'[ \t]+',' ',P.get(p,''))
        L=[l for l in txt.split('\n') if l.strip()]
        hits=[]
        for e in f['excerpts']:
            for frag in e.split('\n'):
                k=re.sub(r'\s','',frag)[:8]
                if len(k)<4: continue
                for n,l in enumerate(L):
                    if k in re.sub(r'\s','',l): hits.append(n)
        if not hits:
            continue
        a=max(0,min(hits)-B); b=min(len(L),max(hits)+A)
        print(f'--- page {p} lines {a}-{b} of {len(L)}')
        print(chr(10).join(x[:110] for x in L[a:b][:int(os.environ.get('M','22'))]))
