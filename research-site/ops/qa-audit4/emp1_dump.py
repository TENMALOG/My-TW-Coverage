import json,re,sys
d=json.load(open('research-site/ops/qa-audit4/emp_in_1.json',encoding='utf8'))
lo,hi=int(sys.argv[1]),int(sys.argv[2])
cache={}
for it in d[lo:hi]:
    t=it['id'].split('-AR-')[0]
    f=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
    x=[y for y in f['facts'] if y['id']==it['id']][0]
    p=x['page']
    tx=open(f['source']['text_path'],encoding='utf8').read()
    pages=re.split(r'\[PDF PAGE (\d+)\]',tx)
    pg={int(pages[i]):pages[i+1] for i in range(1,len(pages)-1,2)}
    txt=pg.get(p,'')
    m=re.search(r'從業員工|員工資料|員工人數',txt)
    s=max(0,(m.start() if m else 0)-250)
    print('=====',it['id'],f['company'],'p',p)
    print('STMT:',x['statement'])
    print('EXC:',x['excerpts'])
    print('PAGE:',txt[s:s+1000].replace('\n',' | '))
