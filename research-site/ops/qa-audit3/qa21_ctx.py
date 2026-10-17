import json,re,sys
ids=[l.strip() for l in open('research-site/ops/qa-audit3/ids_21.txt') if l.strip()]
for t in sys.argv[1].split(','):
    d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
    txt=open(d['source']['text_path'],encoding='utf8').read()
    parts=re.split(r'\[PDF PAGE (\d+)\]',txt)
    pages={int(parts[i]):parts[i+1] for i in range(1,len(parts),2)}
    print('=====',t,d['company'])
    for f in d['facts']:
        if f['id'] not in ids: continue
        print('---',f['id'],f['field'],'|',f['period'],'|',f['attribution'],'| p',f['page'])
        print('STMT:',f['statement'])
        p=f['page']; pg=pages.get(p,'')+pages.get(p+1,'')
        sq=lambda s:re.sub(r'\s+','',s)
        # build map
        idx=[i for i,c in enumerate(pg) if not c.isspace()]
        flat=''.join(pg[i] for i in idx)
        for e in f["excerpts"][-1:]:
            k=sq(e)
            pos=flat.find(k[:25]) if k else -1
            if pos<0: print('  !! NOT FOUND:',e[:60]); continue
            a=idx[max(0,pos-120)]; b=idx[min(len(idx)-1,pos+len(k)+200)]
            print('  CTX:',pg[a:b].replace('\n',' / '))
