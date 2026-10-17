import json,re
d=json.load(open('research-site/ops/qa-audit4/emp_in_1.json',encoding='utf8'))
KW=r'本公司|子公司|合併|台灣|臺灣|海外|國內|大陸|外籍|外勞|境內|總公司|集團|含|不含|僅|母公司|分公司|廠'
for i,it in enumerate(d):
    t=it['id'].split('-AR-')[0]
    f=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
    x=[y for y in f['facts'] if y['id']==it['id']][0]
    tx=open(f['source']['text_path'],encoding='utf8').read()
    pages=re.split(r'\[PDF PAGE (\d+)\]',tx)
    pg={int(pages[i]):pages[i+1] for i in range(1,len(pages)-1,2)}
    txt=pg.get(x['page'],'')
    ex=x['excerpts'][-1]
    m=re.search(r'從業員工|員工資料|員工人數|員\s*工\s*人\s*數',txt)
    s=m.start() if m else 0
    e=re.search(r'合\s*計[^\n]*',txt[s:]); end=s+(e.end() if e else 300)
    win=txt[max(0,s-30):end+200]
    hits=re.findall(KW,re.sub(r'\s','',win))
    print(i,it['id'],'heading' if m else 'NOHEAD',hits[:8])
