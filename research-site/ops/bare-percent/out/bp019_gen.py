import json,re
d=json.load(open('jobs_sonnet/bp019.json',encoding='utf8'))
ids=[x['id'] for x in d]
keep_ids=set("""6488-AR-114 6488-AR-122 6505-AR-02 6505-AR-03 6505-AR-04 6506-AR-11 6506-AR-12 6506-AR-13 6506-AR-14 6506-AR-16 6509-AR-11 6509-AR-12 6509-AR-17 6525-AR-109 6525-AR-110 6526-AR-01 6526-AR-04 6526-AR-05 6531-AR-115 6533-AR-18 6533-AR-19 6552-AR-03 6552-AR-06 6555-AR-13 6558-AR-12 6559-AR-17 6573-AR-11 6579-AR-16 6581-AR-08 6581-AR-19 6592-AR-12 6593-AR-13 6606-AR-10 6606-AR-11 6614-AR-12 6614-AR-13 6614-AR-14 6625-AR-01 6625-AR-02 6625-AR-03 6639-AR-24 6639-AR-25""".split())
def load(t): return json.load(open('../../data/company-facts/%s.json'%t,encoding='utf8'))
pat=re.compile(r'，?(?:佔比|表列合併營收收入比重為|占銷售比率|占比重|占比率|占比例|占比|比重為|比重|比率|比例|占)(\d+(?:\.\d+)?%)。$')
out=[]
for i in ids:
    t=i.split('-')[0]
    k=[f for f in load(t)['facts'] if f['id']==i][0]
    if i in keep_ids:
        out.append(dict(id=i,action='KEEP',reason='陳述已寫明分母（市場、出貨、持股或比較基準），無需修改'));continue
    s=k['statement']
    if k['field'] in('sales_regions','export_share'): den='銷售地區表合計'
    elif k['field']=='revenue_mix': den='該表營業收入合計'
    else: raise SystemExit(i)
    if t=='6585': den='該表合併營收合計'
    m=pat.search(s)
    if not m and i=='6531-AR-104':
        out.append(dict(id=i,action='FIX',new_statement=s.replace('，占比重0.37%','，占該表營業收入淨額合計之0.37%'),reason='補明百分比分母'));continue
    if not m: raise SystemExit('nomatch '+i+s)
    ns=s[:m.start()]+'，占'+den+'之'+m.group(1)+'。'
    out.append(dict(id=i,action='FIX',new_statement=ns,reason='補明百分比分母為'+den))
with open('out/bp019.jsonl','w',encoding='utf8') as f:
    for o in out: f.write(json.dumps(o,ensure_ascii=False)+'\n')
from collections import Counter
print(Counter(o['action'] for o in out),len(out))
for o in out[:3]+out[40:44]: print(o)
