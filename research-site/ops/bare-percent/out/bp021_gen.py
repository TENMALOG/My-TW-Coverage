import json,re
jobs=json.load(open('jobs_sonnet/bp021.json',encoding='utf8'))
KEEP={'6755-AR-07','6757-AR-09','6763-AR-22','6770-AR-19x','6775-AR-03','6775-AR-13','6776-AR-13','6781-AR-22','6784-AR-10','6789-AR-23','6791-AR-09','6799-AR-13','6803-AR-17','6803-AR-18','6811-AR-14','6811-AR-16','6818-AR-11','6821-AR-14','6825-AR-09','6835-AR-12','6840-AR-08','6854-AR-09','6855-AR-10','6858-AR-11','6862-AR-07','6862-AR-08','6869-AR-06','6870-AR-08','6870-AR-09','6873-AR-11','6874-AR-10','6877-AR-05','6877-AR-06','6878-AR-13','6878-AR-14','6878-AR-15','6881-AR-09','6887-AR-15'}
special={
'6770-AR-19':'公司於年報自述，以研究機構預估114年全球晶圓代工公司總產值1,745億美元為基準，公司114全年合併營收約新台幣467.3億元，位居全球前十大晶圓代工公司之列，市占率約達1%（占前述全球晶圓代工公司總產值）。',
'6776-AR-11':'公司於年報自述，依公開資訊觀測站資料，2025年上市、上櫃及興櫃電子通路業共計營收3.55兆（原文未載幣別），展碁銷售額占該電子通路業共計營收之比重為0.82%。',
'6755-AR-05':'114年度內銷台灣營業收入為新台幣151,431仟元，占銷售地區表合計5.67%。',
'6755-AR-06':'114年度外銷中國營業收入為新台幣2,293,491仟元，占銷售地區表合計85.87%。',
}
den={'revenue_mix':'占該表合計','sales_regions':'占銷售地區表合計','export_share':'占銷售地區表合計'}
rev_net={'6757-AR-02','6757-AR-03','6761-AR-03','6761-AR-04','6761-AR-05','6839-AR-01','6839-AR-02','6805-AR-01','6805-AR-02','6805-AR-03','6753-AR-01'}
out=[]
for j in jobs:
    i=j['id'];t=i.split('-')[0]
    d=json.load(open(f'../../data/company-facts/{t}.json',encoding='utf8'))
    f=[x for x in d['facts'] if x['id']==i][0];s=f['statement']
    if i in special:
        out.append(dict(id=i,action='FIX',new_statement=special[i],reason='補明市占率或占比之分母'));continue
    if i in KEEP:
        out.append(dict(id=i,action='KEEP',reason='陳述已寫明比率之分母或為成長率，無需修改'));continue
    fld=f['field']
    dn='占營業收入淨額' if i in rev_net else den.get(fld,'占銷售地區表合計')
    if fld=='revenue_mix' and i in rev_net: dn='占該表合計'
    if i in ('6839-AR-01','6839-AR-02','6761-AR-03','6761-AR-04','6761-AR-05','6757-AR-02','6757-AR-03'): dn='占營業收入淨額合計'
    s2=s
    # replace the percent phrasing
    m=re.search(r'(，|,)?(比重為|比重|占百分比|占比重|占銷售比率|占比率|銷售比重為|銷售比重|比率為|比率|比例為|比例|占比|占)\s*([\d.]+%)',s)
    if not m: print('NOMATCH',i,s);continue
    pre=s[:m.start()];post=s[m.end():]
    s2=pre+'，'+dn+m.group(3)+post
    s2=s2.replace('（銷售地區表）','').replace('（營業比重表）','')
    s2=s2.replace('，，','，').replace('。。','。')
    out.append(dict(id=i,action='FIX',new_statement=s2,reason='補明百分比之分母'))
open('out/bp021.jsonl','w',encoding='utf8').write('\n'.join(json.dumps(o,ensure_ascii=False) for o in out)+'\n')
from collections import Counter
print(Counter(o['action'] for o in out),len(out),len(jobs))
for o in out:
    if o['action']=='FIX':print(o['id'],o['new_statement'])
