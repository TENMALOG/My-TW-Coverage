import json,sys,os,collections
os.chdir(r"C:/Users/Neo Pegasus/Documents/ChatGPT/078-kaori sample/artifacts/stock-coverage-audit-20261003/incoming/latest-audit/My-TW-Coverage")
ids=[l.strip() for l in open('research-site/ops/qa-audit3/ids_09.txt',encoding='utf-8') if l.strip()]
cache={}
out=[]
for i in ids:
    t=i.split('-AR-')[0]
    if t not in cache:
        cache[t]=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf-8'))
    d=cache[t]
    f=[x for x in d['facts'] if x['id']==i][0]
    txt=open(d['source']['text_path'],encoding='utf-8').read()
    pages=txt.split('\f')
    out.append(dict(id=i,company=d['company'],field=f['field'],statement=f['statement'],period=f.get('period'),attr=f.get('attribution'),page=f['page'],excerpts=f['excerpts'],npages=len(pages)))
json.dump(out,open(os.path.join(os.environ.get('TMPD','.'),'x.json'),'w'),ensure_ascii=False) if False else None
with open('research-site/ops/qa-audit3/qa09_dump.txt','w',encoding='utf-8') as o:
    for x in out:
        o.write(f"=== {x['id']} {x['company']} [{x['field']}] p{x['page']} np={x['npages']}\nST: {x['statement']}\nPER: {x['period']}\nATT: {x['attr']}\nEX: {x['excerpts']}\n")
