import json,re,sys,collections
sys.stdout.reconfigure(encoding='utf8')
jobs=json.load(open('research-site/ops/bare-percent/jobs_sonnet/bp008.json',encoding='utf8'))
cache={}
def fact(i):
    t=i.split('-')[0]
    if t not in cache: cache[t]=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
    return [x for x in cache[t]['facts'] if x['id']==i][0]
REG='銷售地區表合計'; MIX='該表產品別合計'
fix={}
def add(ids,d):
    for i in ids.split(): fix[i]=d
add('3058-AR-09 3058-AR-13 3060-AR-07 3060-AR-08 3060-AR-09 3066-AR-05 3066-AR-06 3088-AR-10 3088-AR-11 3088-AR-12 3095-AR-06 3095-AR-07 3097-AR-06 3097-AR-08 3122-AR-108 3122-AR-109 3128-AR-07 3128-AR-08 3149-AR-06 3152-AR-04 3152-AR-05 3152-AR-06 3152-AR-07 3163-AR-07 3163-AR-08 3163-AR-09 3163-AR-10 3167-AR-06 3167-AR-07 3191-AR-05 3206-AR-04 3206-AR-05 3206-AR-06 3207-AR-07 3207-AR-08 3209-AR-05 3209-AR-06 3213-AR-05 3213-AR-06 3213-AR-07 3213-AR-08 3217-AR-03 3217-AR-04 3217-AR-05 3229-AR-05',REG)
add('3231-AR-05 3231-AR-06 3231-AR-07','外銷地區分佈表合計')
add('3060-AR-02 3060-AR-03 3095-AR-04 3095-AR-05 3147-AR-03 3147-AR-04 3147-AR-05 3147-AR-06 3147-AR-07 3152-AR-03 3163-AR-03 3163-AR-04 3163-AR-05 3163-AR-06 3167-AR-02 3167-AR-03 3168-AR-02 3168-AR-03 3206-AR-02 3206-AR-03 3229-AR-03 3231-AR-01 3231-AR-02 3232-AR-02 3232-AR-03 3232-AR-04 3232-AR-05',MIX)
# 3229-AR-03 is 磷銅球 revenue; 3229-AR-05 region
fix['3229-AR-03']=MIX
tok=re.compile(r'(占銷售比率|占銷售金額|占比為|占比|比重為|比重|比例為|比例|百分比為|百分比|占)(?=\d)')
dropids={'3097-AR-12':'僅列「其他」列，並無具體客戶可供陳述'}
out=[];cnt=collections.Counter()
for j in jobs:
    i=j['id']
    if i in dropids:
        out.append({'id':i,'action':'DROP','reason':dropids[i]});cnt['DROP']+=1
    elif i in fix:
        d=fix[i];s=fact(i)['statement']
        ns=tok.sub(lambda m:'占'+d+'之',s)
        assert ns!=s,i
        out.append({'id':i,'action':'FIX','new_statement':ns,'reason':f'百分比分母未明，補明為{d}'});cnt['FIX']+=1
    else:
        out.append({'id':i,'action':'KEEP','reason':'陳述已載明百分比的分母或屬成長率／預測，並無分母疑義'});cnt['KEEP']+=1
with open('research-site/ops/bare-percent/out/bp008.jsonl','w',encoding='utf8') as f:
    for o in out: f.write(json.dumps(o,ensure_ascii=False)+'\n')
print(cnt,len(out))
for o in out:
    if o['action']=='FIX': print(o['id'],o['new_statement'])
