import json,os,re,sys
os.chdir(r"C:/Users/Neo Pegasus/Documents/ChatGPT/078-kaori sample/artifacts/stock-coverage-audit-20261003/incoming/latest-audit/My-TW-Coverage")
ids=[l.strip() for l in open('research-site/ops/qa-audit3/ids_04.txt',encoding='utf-8') if l.strip()]
a,b=int(sys.argv[1]),int(sys.argv[2])
cache={};pc={}
def pages(path):
    if path not in pc:
        t=open(path,encoding='utf-8').read()
        parts=re.split(r'\[PDF PAGE (\d+)\]',t)
        pc[path]={int(parts[i]):parts[i+1] for i in range(1,len(parts),2)}
    return pc[path]
for i in ids[a:b]:
    t=i.split('-AR-')[0]
    if t not in cache: cache[t]=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf-8'))
    d=cache[t]
    f=[x for x in d['facts'] if x['id']==i][0]
    P=pages(d['source']['text_path'])
    pg=f['page']
    print(f"\n######## {i} {d['company']} [{f['field']}] p{pg}\nST: {f['statement']}\nPER: {f.get('period')}\nATT: {f.get('attribution')}\nEX: {f['excerpts']}")
    for p in (pg,):
        txt=re.sub(r'[ \t]+',' ',P.get(p,'(none)'))
        txt=re.sub(r'\n\s*\n+','\n',txt)
        print(f"--- page {p}\n{txt[:2500]}")
