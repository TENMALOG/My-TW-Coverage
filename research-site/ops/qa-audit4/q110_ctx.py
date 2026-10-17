import json,re,io
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_110.txt',encoding='utf8') if l.strip()]
out=io.open('research-site/ops/qa-audit4/q110_ctx.txt','w',encoding='utf8')
cache={}
def pages(txt):
    parts=re.split(r'\n\[PDF PAGE (\d+)\]\n',txt)
    return {int(parts[i]):parts[i+1] for i in range(1,len(parts),2)}
for i in ids:
    t=i.split('-AR-')[0]
    if t not in cache:
        d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
        cache[t]=(d,pages(open(d['source']['text_path'],encoding='utf8').read()))
    d,P=cache[t]
    f=[x for x in d['facts'] if x['id']==i][0]
    pg=P.get(f['page'],'')
    out.write('\n=====%s p%s | %s\n'%(i,f['page'],f['statement']))
    # find best excerpt anchor: last excerpt
    shown=False
    for e in reversed(f['excerpts']):
        key=re.sub(r'\s+','',e)
        flat=re.sub(r'\s+','',pg)
        idx=flat.find(key[:25])
        if idx>=0:
            # map back: crude, show flat context
            out.write('CTX(flat): '+flat[max(0,idx-250):idx+len(key)+350]+'\n'); shown=True;break
    if not shown: out.write('NOT FOUND in page; page head: '+pg[:600]+'\n')
out.close()
