import json,re
d=json.load(open('research-site/ops/qa-audit4/emp_in_2.json',encoding='utf8'))
KEEP={'6023-AR-12':'陳述已指明為元大期貨(香港)有限公司，範圍清楚',
'6023-AR-13':'陳述已指明為元大國際(新加坡)有限公司，範圍清楚',
'6028-AR-15':'陳述已說明為業務員登錄人數而非員工人數表人數，無範圍問題',
'5530-AR-12':'非員工人數表，為年報文字所述禮儀師證照人數，陳述未涉員工表範圍',
'6227-AR-12':'年報文字明載為本公司應用工程處人員及本公司總人數，範圍已清楚',
'6271-AR-17':'陳述已載明員工人數包含同欣菲律賓員工'}
SUF='（員工人數表未載明為母公司或合併範圍）'
out=[]
for it in d:
    i=it['id'];st=it['statement']
    if i in KEEP:
        out.append(dict(id=i,action='KEEP',new_statement='',new_attribution='',reason=KEEP[i]));continue
    if i.startswith('6276-AR-12'):
        ns='員工人數表載明包含子公司，'+st
        out.append(dict(id=i,action='FIX',new_statement=ns,new_attribution='',reason='表頭載明（包含子公司），補上範圍'));continue
    ns=st
    ns=re.sub(r'公司(?=從業|員工|間接|直接|\d)','',ns)
    ns=ns.replace('今國光學員工','員工').replace('德宏從業員工人數表列員工','從業員工人數表列員工')
    ns=ns.rstrip('。')+SUF+'。'
    out.append(dict(id=i,action='FIX',new_statement=ns,new_attribution='',reason='員工人數表未載明範圍，補註並移除暗示母公司範圍之用語'))
with open('research-site/ops/qa-audit4/emp_out_2.jsonl','w',encoding='utf8') as f:
    for o in out: f.write(json.dumps(o,ensure_ascii=False)+'\n')
from collections import Counter
print(Counter(o['action'] for o in out),len(out))
for o in out:
    if o['action']=='FIX' and (o['id'] in('5392-AR-120','6209-AR-120','5475-AR-14','6202-AR-12','6276-AR-121','6230-AR-117','5284-AR-14')): print(o['new_statement'])
