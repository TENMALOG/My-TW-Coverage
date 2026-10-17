import json,sys,collections
sys.stdout.reconfigure(encoding='utf-8')
jobs=json.load(open('research-site/ops/bare-percent/jobs_sonnet/bp011.json',encoding='utf-8'))
cache={}
def fact(i):
    t=i.split('-')[0]
    if t not in cache: cache[t]=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf-8'))
    return [x for x in cache[t]['facts'] if x['id']==i][0]
KEEP=set("""3603-AR-09 3603-AR-11 3605-AR-15 3605-AR-16 3609-AR-09 3617-AR-11 3617-AR-16 3622-AR-117 3623-AR-04 3624-AR-09 3624-AR-11 3624-AR-12 3625-AR-07 3630-AR-06 3630-AR-07 3633-AR-10 3645-AR-08 3646-AR-07 3652-AR-12 3652-AR-15 3652-AR-22 3659-AR-07 3661-AR-08 3663-AR-21 3665-AR-13 3669-AR-12 3672-AR-18 3675-AR-06 3675-AR-15 3684-AR-08 3684-AR-15 3684-AR-16 3684-AR-17 3685-AR-08 3687-AR-06 3689-AR-09 3689-AR-10 3689-AR-14 3689-AR-15 3693-AR-21 3694-AR-08 3701-AR-08 3702-AR-14 3708-AR-08 3708-AR-22 3710-AR-06 3710-AR-07 3715-AR-09 3715-AR-10 3717-AR-102""".split())
R={
'3624-AR-08':"公司表示銷售至中國大陸市場營業持續大幅成長，佔30-40%（原文未明確寫明分母）。",
'3684-AR-07':"114年度外銷占營收比重為66.28%，內銷占營收比重為33.63%。",
'3704-AR-15':"年報載明最近二年度無任一進貨對象占全年度進貨總額超過10%以上。",
'3675-AR-10':"114年度主要客戶表列示A客戶占銷貨淨額22.69%，B客戶占銷貨淨額17.66%。",
'3675-AR-11':"114年度主要供應商表列示甲供應商占進貨淨額31.01%。",
'3712-AR-105':"114年度3C零組件營業金額為新台幣268,822仟元，占產品營業比重表合計0.82%，合計營業金額為新台幣32,820,918仟元；年報註明營業額為合併財報營收。",
'3623-AR-03':"114年度觸控面板銷售金額為294,824仟元，占營業比重表合計99.84%。",
'3680-AR-03':"114年度內銷占銷售地區表合計之62%。",
'3717-AR-109':"114年度內銷銷售額為新台幣360,782仟元，占銷售地區表合計6%。",
'3715-AR-06':"114年度合併內銷金額占銷售地區表合計9.3%。",
'3715-AR-07':"114年度合併以下單客戶所在國家為基礎歸類，中國大陸銷售金額占銷售地區表合計36.45%。",
'3687-AR-06':None,
}
def den(i,f):
    fl=f['field']; s=f['statement']
    if fl=='sales_regions' or fl=='export_share': return '占銷售地區表合計'
    if fl=='revenue_mix': return '占該表營業收入合計' 
    raise Exception(i)
out=[];c=collections.Counter()
import re
for j in jobs:
    i=j['id'];f=fact(i)
    if i in KEEP:
        out.append({'id':i,'action':'KEEP','reason':'陳述已自帶分母或為成長率／明確定義之比率，無需補充'});c['KEEP']+=1;continue
    if i in R:
        ns=R[i]
    else:
        s=f['statement']
        d=den(i,f)
        if i=='3712-AR-112': ns=None
        if i.startswith('3712-AR-1') and f['field']=='revenue_mix': d='占產品營業比重表合計'
        if f['field']=='revenue_mix':
            if i.startswith('3605') or i.startswith('3603'): d='占主要產品表合計'
            if i.startswith('3622'): d='占該表營業收入淨額合計'
            if i.startswith('3628'): d='占主要產品營業收入表合計'
            if i.startswith('3663'): d='占合併財報銷售表合計'
            if i.startswith('3693') or i.startswith('3694') or i.startswith('3710') : d='占該表營業收入合計'
            if i.startswith('3714'): d='占2025年度營業比重表合計'
        if f['field']=='export_share' and i.startswith('3616'): d='占銷售地區表合計'
        # insert denominator before first percentage figure phrase
        m=re.search(r'(占比為|占比重|占比|比重為|比重|比率為|比率|比例|占)(?=[\d])|(占比重|占比|比重為|比重|比率為|比率|比例)(?=\d)',s)
        ns=None
        for pat in [r'(占比重|占比為|占比|比重為|比重|比率為|比率|比例為|比例|占)(\d[\d.]*%)']:
            ns=re.sub(pat,lambda mm:d+mm.group(2),s)
        if ns==s or ns is None: raise Exception('nochange '+i+s)
    out.append({'id':i,'action':'FIX','new_statement':ns,'reason':'補明百分比分母，未新增數字'});c['FIX']+=1
with open('research-site/ops/bare-percent/out/bp011.jsonl','w',encoding='utf-8') as fo:
    for o in out: fo.write(json.dumps(o,ensure_ascii=False)+'\n')
print(c)
for o in out:
    if o['action']=='FIX': print(o['id'],o['new_statement'])
