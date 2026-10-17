import json,re,sys
job,start,end=sys.argv[1],int(sys.argv[2]),int(sys.argv[3])
root='research-site/'
ids=[l.strip() for l in open(root+'ops/codex-review/jobs_sonnet/%s.txt'%job,encoding='utf8') if l.strip()][start:end]
cache={}
def pages(path):
    if path not in cache:
        t=open(path,encoding='utf8').read()
        parts=re.split(r'\[PDF PAGE (\d+)\]',t)
        cache[path]={int(parts[i]):parts[i+1] for i in range(1,len(parts)-1,2)}
    return cache[path]
fc={}
for i in ids:
    tk=i.split('-')[0]
    if tk not in fc: fc[tk]=json.load(open(root+'data/company-facts/%s.json'%tk,encoding='utf8'))
    d=fc[tk]
    f=[x for x in d['facts'] if x['id']==i][0]
    print('=====',i,d['company'],f['field'],'|',f['attribution'],'| p',f['page'],'|',f['period'])
    print('STMT:',f['statement'])
    print('EXC:',' // '.join(f['excerpts']))
    pg=pages('../'*0+d['source']['text_path']) if False else pages(d['source']['text_path'])
    p=pg.get(f['page'],'')
    pos=p.find(f['excerpts'][0][:15]) if f['excerpts'] else 0
    pos=max(pos,0)
    a=max(0,pos-150)
    print('PAGE:',re.sub(r'\n+','⏎',p[a:a+520]))
    if len(f['excerpts'])>1 and f['excerpts'][-1][:12] not in p:
        print('NEXT:',re.sub(r'\n+','⏎',pg.get(f['page']+1,'')[:900]))
