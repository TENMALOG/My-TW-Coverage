import json,re
jobs=json.load(open('jobs_sonnet/bp010.json',encoding='utf8'))
S='占銷售地區表合計'; R='占營業收入表合計'
fix={}
def add(ids,d):
    for i in ids.split(): fix['-'.join(i.split('-'))]=d
P=lambda t,ns,pre='AR-':[f'{t}-{pre}{n}' for n in ns]
for i in ['3455-AR-08','3455-AR-09']: fix[i]='占內外銷營收合計'
for i in P(3466,['10','11','12','13'])+['3481-AR-02','3481-AR-03','3481-AR-04','3484-AR-07','3485-AR-06','3491-AR-10','3511-AR-05']+P(3498,['06','07','08','09'])+P(3501,['09','10','11','12'])+P(3504,['10','11','12','13'])+P(3520,['07','08','09'])+['3526-AR-04','3526-AR-05','3531-AR-109','3533-AR-105','3533-AR-106','3537-AR-08','3537-AR-09','3537-AR-10','3543-AR-06','3543-AR-07','3548-AR-05']+P(3558,['08','09','10','11'])+P(3577,['10','12','13'])+P(3580,['04','05'])+P(3588,['105','106','107','108','109'])+['3591-AR-06','3592-AR-03','3592-AR-04']+['3593-AR-09','3593-AR-10']+P(3594,['07','08','09','10'])+['3595-AR-117','3595-AR-118','3597-AR-04','3597-AR-05']: fix[i]=S
for i in ['3515-AR-01','3515-AR-02','3520-AR-03','3520-AR-04','3520-AR-05','3543-AR-03','3543-AR-04','3543-AR-05','3585-AR-02','3585-AR-03','3597-AR-02','3597-AR-03','3603-AR-02']: fix[i]=R
fix['3454-AR-12']=None
over={
'3454-AR-12':'公司年報載明，最近二年度並無單一供應商占進貨總額之比重超過10%以上之情事。',
'3577-AR-13':'114年度外銷合計銷售金額為新台幣538,157仟元，占銷售地區表合計45.92%。',
'3596-AR-09':'113年度美洲占主要商品（服務）銷售地區表合計43.0%。',
'3596-AR-10':'113年度亞洲及其他占主要商品（服務）銷售地區表合計30.1%。',
'3596-AR-11':'113年度歐洲占主要商品（服務）銷售地區表合計26.9%。',
'3466-AR-10':None,
}
pat=re.compile(r'(?:占銷售比率|占銷售比例|占銷售金額|占比為|占比重|占比例|占比|佔率|比例為|比重為|比率為|占)(\d[\d.]*%)')
out=[]
for j in jobs:
    i=j['id']
    if i in over and over[i]:
        out.append({'id':i,'action':'FIX','new_statement':over[i],'reason':'補明分母'});continue
    if i in fix and fix[i]:
        s=None
        d=json.load(open(f'../../data/company-facts/{i.split("-")[0]}.json',encoding='utf8'))
        st=[x for x in d['facts'] if x['id']==i][0]['statement']
        s=pat.sub(lambda m:fix[i]+m.group(1),st)
        
        if s==st: print('NOSUB',i,st); continue
        out.append({'id':i,'action':'FIX','new_statement':s,'reason':'百分比補明分母：'+fix[i]});continue
    out.append({'id':i,'action':'KEEP','reason':'陳述已明示分母或非占比數據，原句正確'})
with open('out/bp010.jsonl','w',encoding='utf8') as f:
    for o in out: f.write(json.dumps(o,ensure_ascii=False)+'\n')
from collections import Counter
print(Counter(o['action'] for o in out),len(out),len(jobs))
for o in out:
    if o['action']=='FIX': print(o['id'],o['new_statement'])
