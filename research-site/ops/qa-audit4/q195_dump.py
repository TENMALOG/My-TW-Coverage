import json,sys,re
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_195.txt',encoding='utf8') if l.strip()]
tick=sys.argv[1]
cache={}
def pages(t):
    if t in cache: return cache[t]
    d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
    txt=open(d['source']['text_path'],encoding='utf8').read()
    ps={}
    for m in re.finditer(r'\[PDF PAGE (\d+)\]\n(.*?)(?=\n\[PDF PAGE \d+\]|\Z)',txt,re.S):
        ps[int(m.group(1))]=m.group(2)
    cache[t]=(d,ps);return cache[t]
d,ps=pages(tick)
shown=set()
for i in ids:
    if i.split('-')[0]!=tick: continue
    f=[x for x in d['facts'] if x['id']==i][0]
    print('=====',i,'|',f['field'],'|',f.get('period'),'| p',f['page'],'|',f.get('attribution'))
    print('STMT:',f['statement'])
    for e in f['excerpts']:print('  EX:',e)
    W=int(sys.argv[2]) if len(sys.argv)>2 else 300
    t=re.sub(r'\s+','',ps.get(f['page'],'')+ps.get(f['page']+1,'')[:400])
    for e in f['excerpts'][-1:]:
        k=re.sub(r'\s+','',e)
        j=t.find(k)
        print('  CTX:',('NOTFOUND' if j<0 else t[max(0,j-W):j+len(k)+W]))
