import json,re
root='research-site/'
jobs=json.load(open(root+'ops/bare-percent/jobs_sonnet/bp012.json',encoding='utf8'))
cache={}
def fact(i):
    t=i.split('-')[0]
    if t not in cache: cache[t]=json.load(open(f'{root}data/company-facts/{t}.json',encoding='utf8'))['facts']
    return [f for f in cache[t] if f['id']==i][0]
R='銷售地區表合計'
den={}
def setd(d,ids):
    for i in ids.split(): den[i]=d
setd(R,'3717-AR-110 3717-AR-111 3717-AR-112 4420-AR-07 4431-AR-06 4431-AR-07 4523-AR-09 4523-AR-10 4526-AR-05 4526-AR-06 4526-AR-07 4526-AR-08 4532-AR-04 4532-AR-05 4532-AR-06 4532-AR-07 4537-AR-12 4542-AR-10 4542-AR-11 4544-AR-10 4544-AR-11 4544-AR-12 4552-AR-12 4552-AR-13 4554-AR-05 4554-AR-06 4555-AR-08 4562-AR-09 4562-AR-10 4562-AR-11 4562-AR-12 4563-AR-05 4563-AR-06 4563-AR-07 4563-AR-08 4565-AR-06 4565-AR-07 4565-AR-08 4565-AR-09 4565-AR-10 4566-AR-05 4566-AR-06 4566-AR-07 4566-AR-08 4566-AR-09 4568-AR-05 4568-AR-06 4568-AR-07 4568-AR-08 4573-AR-07 4573-AR-08 4575-AR-05 4575-AR-06 4575-AR-07 4527-AR-08 4527-AR-09')
setd('該表產品別營收合計','4552-AR-05 4552-AR-06 4552-AR-07 4552-AR-08 4562-AR-02 4562-AR-03 4562-AR-04 4565-AR-02 4565-AR-03 4566-AR-01 4566-AR-02 4566-AR-03 4575-AR-03 4575-AR-04')
setd('該表營業收入淨額合計','4568-AR-02 4568-AR-03 4523-AR-04 4523-AR-05 4523-AR-06 4523-AR-07')
pat=re.compile(r'(占比為|比率為|占比率|占比重|占比|比率|比重|占銷售比率|占)\s*(\d[\d.,]*\s*[%％])')
out=[]
for j in jobs:
    i=j['id']; f=fact(i); r={'id':i}
    if i in den:
        s=f['statement']; ms=list(pat.finditer(s)); print(i) if not ms else None; m=ms[-1]
        num=m.group(2).replace(' ','')
        ns=s[:m.start()]+'占'+den[i]+num+s[m.end():]
        ns=ns.replace('，占','，占') 
        r.update(action='FIX',new_statement=ns,reason='補明百分比分母：'+den[i]+'（依表格合計列）')
    elif i=='4171-AR-10':
        r.update(action='FIX',new_statement='年報稱114年營收來源第一高區域為東南亞地區，占營收43.90%。',reason='原文「占比最高」未明分母，同段後文均為占營收，補明占營收')
    elif i=='4441-AR-01':
        r.update(action='FIX',new_statement='114年度成衣銷售收入為新台幣7,477,093仟元，占營業收入淨額99.96%。',reason='原句將營業收入淨額與項目金額混置，補明比重分母為營業收入淨額')
    elif i=='4527-AR-04':
        r.update(action='FIX',new_statement='公司年報揭露空調系統中最大耗能設備為冰水機，約占空調系統耗能的60%。',reason='原文「約占60%」緊接於空調系統耗能之敘述，補明分母為空調系統耗能')
    elif i=='4538-AR-09':
        r.update(action='FIX',new_statement='年報說明，F及A公司（年報代號）本期銷貨金額較去年減少，致占主要銷貨客戶表所列銷貨比率低於10%，主要係因美國關稅影響需求停滯。',reason='補明10%為主要銷貨客戶表之銷貨占比')
    elif i=='4538-AR-11':
        r.update(action='FIX',new_statement='年報說明，114年度新增多家進貨廠商，致進貨分散，占全年度進貨淨額達10%以上的供應商僅剩一家。',reason='表頭為占全年度進貨淨額比率，補明10%之分母')
    elif i=='4431-AR-08':
        r.update(action='FIX',new_statement='公司於年報自述，以台灣區不織布工業同業公會統計之113年國內不織布總產量155仟噸為基礎，推估公司114年度靜電濾材、熔噴不織布及保溫棉材產量786噸之市場佔有率為0.5%（分母為國內不織布總產量）。',new_attribution='公司年報自述（未經獨立驗證的排名或評價）',reason='占有率為公司自行推估，改為自述並明示分母')
    elif i=='4513-AR-09':
        r.update(action='FIX',new_statement=f['statement'].replace('（年報載明資料來源為經濟部統計處，福裕公司整理）','（資料來源為經濟部統計處，福裕公司整理，占有率分母為我國金屬切削工具機總銷值）'),new_attribution='公司年報自述（未經獨立驗證的排名或評價）',reason='占有率由公司整理計算，改為自述並明示分母')
    elif i=='4523-AR-11':
        r.update(action='FIX',new_statement='公司於年報自述，依經濟部統計處工業產銷存動態調查資料，114年度全國斷路器產品銷售量為23,380,696台，公司同期真空斷路器（VCB）銷售量為34,954台，推估市場佔有率約為0.1495%（分母為全國斷路器銷售量）。',new_attribution='公司年報自述（未經獨立驗證的排名或評價）',reason='占有率為公司推估，改為自述並明示分母')
    else:
        r.update(action='KEEP',reason='陳述已寫明百分比之分母或比較基礎（如占營收、占全國總銷量、市場、成長率、持股比例），無需修改')
    out.append(r)
with open(root+'ops/bare-percent/out/bp012.jsonl','w',encoding='utf8') as fo:
    for r in out: fo.write(json.dumps(r,ensure_ascii=False)+'\n')
from collections import Counter
print(Counter(r['action'] for r in out),len(out))
for r in out:
    if r['action']=='FIX': print(r['id'],r['new_statement'])
