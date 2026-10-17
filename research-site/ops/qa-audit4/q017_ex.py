import json,re,sys
ids=[l.strip() for l in open('research-site/ops/qa-audit4/ids_017.txt',encoding='utf8') if l.strip()]
for n in map(int,sys.argv[1:]):
    i=ids[n];t=i.split('-AR-')[0]
    d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
    txt=open(d['source']['text_path'],encoding='utf8').read()
    pages=re.split(r'\[PDF PAGE (\d+)\]',txt)
    pm={int(pages[k]):pages[k+1] for k in range(1,len(pages),2)}
    f=[x for x in d['facts'] if x['id']==i][0]
    pg=re.sub(r'[ \t]+',' ',pm[f['page']])
    print('=====',n,i,f['field'],f['period']);print('STMT:',f['statement'])
    for e in f['excerpts']:
        e1=re.sub(r'\s+','',e)
        flat=re.sub(r'\s+','',pg)
        k=flat.find(e1[:15]) 
        if k>=0:
            print(' EXC@',flat[max(0,k-60):k+len(e1)+150]); break
