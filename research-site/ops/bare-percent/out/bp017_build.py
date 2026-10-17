import json,re,sys
sys.stdout.reconfigure(encoding='utf8')
d=json.load(open('../jobs_sonnet/bp017.json',encoding='utf8'))
facts={}
for it in d:
    t=it['id'].split('-')[0]
    if t not in facts: facts[t]={f['id']:f for f in json.load(open(f'../../../data/company-facts/{t}.json',encoding='utf8'))['facts']}
def st(i): return facts[i.split('-')[0]][i]['statement']
REG='占銷售地區表合計'; PROD='占產品項目表合計'; TOT='占該表合計'
KEEP=set('''6196-AR-08 6196-AR-16 6196-AR-17 6202-AR-03 6210-AR-04 6210-AR-08 6210-AR-09 6210-AR-10 6210-AR-11 6207-AR-113 6207-AR-114 6208-AR-14 6209-AR-108 6213-AR-05 6213-AR-08 6214-AR-11 6214-AR-12 6214-AR-13 6219-AR-12 6220-AR-15 6220-AR-17 6231-AR-09 6231-AR-10 6231-AR-11 6234-AR-07 6235-AR-08 6237-AR-01 6237-AR-12 6237-AR-13 6239-AR-04 6241-AR-07 6243-AR-106 6244-AR-12 6245-AR-05 6245-AR-06 6245-AR-07 6245-AR-08 6245-AR-09 6246-AR-12 6246-AR-13 6246-AR-14 6246-AR-15 6248-AR-06 6248-AR-07 6257-AR-13 6272-AR-04 6275-AR-17'''.split())
den={}
for i in '6196-AR-09 6196-AR-10 6196-AR-11 6197-AR-07 6197-AR-08 6197-AR-09 6198-AR-107 6202-AR-04 6202-AR-05 6202-AR-06 6203-AR-04 6203-AR-05 6203-AR-06 6204-AR-04 6206-AR-05 6206-AR-06 6206-AR-07 6206-AR-08 6209-AR-106 6209-AR-107 6210-AR-06 6210-AR-07 6215-AR-04 6215-AR-05 6215-AR-06 6217-AR-06 6220-AR-10 6220-AR-11 6220-AR-12 6220-AR-13 6220-AR-14 6224-AR-06 6224-AR-07 6228-AR-07 6228-AR-08 6228-AR-09 6228-AR-10 6228-AR-11 6230-AR-105 6230-AR-106 6230-AR-107 6230-AR-108 6233-AR-05 6243-AR-108 6243-AR-109 6246-AR-05 6246-AR-06 6269-AR-08 6269-AR-09 6269-AR-10 6270-AR-108 6270-AR-109 6270-AR-110 6270-AR-111 6272-AR-03 6274-AR-107 6274-AR-108 6274-AR-109'.split(): den[i]=REG
for i in '6205-AR-101 6205-AR-102 6205-AR-103 6224-AR-03 6224-AR-04 6216-AR-01'.split(): den[i]=PROD
for i in '6207-AR-101 6207-AR-102 6207-AR-103'.split(): den[i]='占營業項目表合計'
for i in '6276-AR-101 6276-AR-102'.split(): den[i]='占營業比重表合計'
for i in '6220-AR-01 6220-AR-02 6220-AR-03 6220-AR-04 6220-AR-05 6220-AR-06'.split(): den[i]='占該表營業收入淨額合計'
for i in '6198-AR-102 6217-AR-02 6236-AR-03 6236-AR-04 6248-AR-02 6248-AR-03'.split(): den[i]=TOT
pats=['占比重','占銷售比重','占銷售比率','營業比率','占比','比重','比率','百分比','占']
def fix(i,dn):
    s=st(i)
    if i in('6233-AR-05',):
        return '114年度內銷（台灣）%s為37.32%%，亞洲地區為62.52%%。'%'銷售比例（'+dn+'）' if False else '114年度內銷（台灣）銷售比例（占銷售地區表合計）為37.32%，亞洲地區為62.52%。'
    if i in ('6270-AR-108','6270-AR-109','6270-AR-110','6270-AR-111'):
        return re.sub(r'比率(\d+%)','比率\1（占銷售地區表合計）',s)
    if i in('6274-AR-107','6274-AR-108','6274-AR-109'):
        return s.replace('，占','，'+dn)
    if i in('6276-AR-101','6276-AR-102'):
        return s.replace('營業比率','營業比率（'+dn+'）')
    if i=='6198-AR-107':
        return s.replace('比重100.00%','比重100.00%（占銷售地區表合計）')
    if i=='6198-AR-102':
        return s.replace('比重100.00%','比重100.00%（占營業收入表合計）')
    for pt in ['占銷售比重','占銷售比率','占比重','占比']:
        if pt in s: return s.replace(pt,dn,1)
    m=re.search(r'(比重|比率|百分比)(?=\d)',s)
    if m: return s[:m.end()]+'（'+dn+'）'+s[m.end():]
    m=re.search(r'，占(?=\d)',s)
    if m: return s[:m.start()]+'，'+dn+s[m.end():]
    raise Exception(i+s)
out=[]
for it in d:
    i=it['id']; r={'id':i}
    if i in KEEP: r.update(action='KEEP',reason='陳述已明示分母、屬成長率或自述市占，無須修改')
    elif i=='6202-AR-08':
        r.update(action='FIX',new_statement='公司於年報自述，以Yole Group全球MCU市場規模推算，114年度MCU總銷售金額為新臺幣23.3億元，在全球市場營收占有率約為0.24%。',new_attribution='公司年報自述（未經獨立驗證的排名或評價）',reason='占有率為公司自行推算，改標自述')
    elif i=='6217-AR-04':
        r.update(action='FIX',new_statement='公司於年報自述，依2024年度營業收入推算，當年度於全球連接器之市場占有率約為0.11%。',new_attribution='公司年報自述（未經獨立驗證的排名或評價）',reason='占有率為公司自行計算，改標自述')
    elif i in den:
        r.update(action='FIX',new_statement=fix(i,den[i]),reason='補明百分比分母為'+den[i].replace('占',''))
    else: raise Exception('unhandled '+i)
    out.append(r)
open('../out/bp017.jsonl','w',encoding='utf8').write('\n'.join(json.dumps(r,ensure_ascii=False) for r in out)+'\n')
for r in out:
    if r['action']=='FIX': print(r['id'],r['new_statement'])
from collections import Counter;print(Counter(r['action'] for r in out),len(out))
