import json,re
d=json.load(open('research-site/ops/qa-audit4/emp_in_2.json',encoding='utf8'))
KW=r'本公司|合併|子公司|集團|台灣|臺灣|大陸|海外|外籍|外勞|不含|含|境內|國內|母公司|總公司|分公司|廠|地區|註'
out=[]
for n,it in enumerate(d):
    t=it['id'].split('-AR-')[0]
    f=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
    x=[y for y in f['facts'] if y['id']==it['id']][0]
    txt=open(f['source']['text_path'],encoding='utf8',errors='replace').read()
    parts=re.split(r'\[PDF PAGE (\d+)\]',txt)
    pages={int(parts[i]):parts[i+1] for i in range(1,len(parts),2)}
    pt=pages.get(x['page'],'')+pages.get(x['page']+1,'')[:600]
    s='';idx=[]
    for i,c in enumerate(pt):
        if not c.isspace(): idx.append(i); s+=c
    nums=[re.sub(r'\s+','',e) for e in x['excerpts']]
    p=-1
    for e in nums[::-1]:
        p=s.find(e)
        if p>=0:break
    if p<0:
        print(n,it['id'],'NOTFOUND',x['excerpts']);continue
    pos=idx[p]
    hs=[m.start() for m in re.finditer(r'從業員工|從業人員|員工資料|員工人數|員工資訊|人員資料',pt[:pos+5])]
    hp=hs[-1] if hs else max(0,pos-300)
    hp=max(hp-60,0)
    # table start: employee header; region through 平均年
    end=pt.find('平',pos)
    region=pt[hp:pos+60]
    out.append(dict(n=n,id=it['id'],co=f['company'],st=x['statement'],region=re.sub(r'\s*\n\s*',' / ',region)))
json.dump(out,open('research-site/ops/qa-audit4/emp2_regions.json','w',encoding='utf8'),ensure_ascii=False)
for o in out:
    r=o['region']
    ks=sorted(set(re.findall(KW,r)))
    print(o['n'],o['id'],o['co'],'|',o['st'],'|',ks)
