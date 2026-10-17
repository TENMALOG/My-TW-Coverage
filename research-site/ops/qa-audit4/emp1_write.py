import json,re
d=json.load(open('research-site/ops/qa-audit4/emp_in_1.json',encoding='utf8'))
NOTE='（員工人數表未載明為母公司或合併範圍）'
KEEP={'3702-AR-20':'表標題已列大聯大控股公司，陳述已寫明範圍','4907-AR-17':'陳述已寫明員工表標示董事除外之範圍'}
SPEC={
 '3594-AR-15':('員工人數表註載明該表員工資料包含子公司磐旭及磐佳瑞等','表註載明含子公司'),
 '3594-AR-16':('員工人數表註載明該表員工資料包含子公司磐旭及磐佳瑞等','表註載明含子公司'),
 '3715-AR-12':('員工人數表欄位標示為「年度-合併」','表欄位標示合併'),
 '4938-AR-23':('員工資料表註載明資訊僅為和碩聯合科技股份有限公司，不含其他上市子公司','表註載明僅母公司'),
 '4938-AR-24':('員工資料表註載明資訊僅為和碩聯合科技股份有限公司，不含其他上市子公司','表註載明僅母公司'),
 '4938-AR-25':('員工資料表註載明資訊僅為和碩聯合科技股份有限公司，不含其他上市子公司','表註載明僅母公司'),
 '4939-AR-09':('員工人數表註載明上述人數包含子公司','表註載明含子公司'),
 '4956-AR-10':('員工人數表註載明上表揭露本公司合併員工人數資訊','表註載明合併員工人數'),
 '4958-AR-19':('員工人數表註載明上述人數係員工在職人數，未載明為母公司或合併範圍','表註僅載明在職人數，未載明範圍'),
}
def base(s):
    s=s.rstrip('。')
    s=re.sub(r'^(事欣科|和碩|欣厚科技)','',s)
    s=s.replace('公司年報','年報').replace('公司從業員工','從業員工').replace('公司員工','員工').replace('公司研發人員','研發人員')
    s=re.sub(r'^年報載明','年報載明',s)
    return s
out=[]
for it in d:
    i=it['id'];s=it['statement']
    if i in KEEP:
        out.append({'id':i,'action':'KEEP','reason':KEEP[i]});continue
    b=base(s)
    if i in SPEC:
        n,r=SPEC[i]; ns=b+'（'+n+'）。'; reason=r
    elif i=='4915-AR-14':
        ns=b+NOTE+'。'; reason='表未載明實體範圍，僅載明計算對象為正職及派遣工'
    else:
        ns=b+NOTE+'。'; reason='員工人數表未載明範圍，已加註'
    out.append({'id':i,'action':'FIX','new_statement':ns,'new_attribution':'','reason':reason})
with open('research-site/ops/qa-audit4/emp_out_1.jsonl','w',encoding='utf8') as f:
    for o in out: f.write(json.dumps(o,ensure_ascii=False)+'\n')
# number check
bad=0
for it,o in zip(d,out):
    if o['action']!='FIX':continue
    t=it['id'].split('-AR-')[0]
    fj=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
    x=[y for y in fj['facts'] if y['id']==it['id']][0]
    ex=re.sub(r'[\s,]','',' '.join(x['excerpts']))
    for n in re.findall(r'\d[\d,]*(?:\.\d+)?',re.sub(r'(?<=\d),(?=\d)','',o['new_statement'])):
        if n not in ex: print('NUM?',it['id'],n); bad+=1
print(len(out),sum(o['action']=='FIX' for o in out),bad)
for o in out[:3]+out[54:56]+out[99:100]: print(o)
