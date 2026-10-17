import json,re
d=json.load(open('../jobs_sonnet/bp016.json',encoding='utf8'))
facts={}
for it in d:
    t=it['id'].split('-')[0]
    if t not in facts: facts[t]={f['id']:f for f in json.load(open(f'../../../data/company-facts/{t}.json',encoding='utf8'))['facts']}
def st(i): return facts[i.split('-')[0]][i]['statement']
KEEP={'6115-AR-12','6120-AR-07','6120-AR-08','6120-AR-09','6120-AR-11','6121-AR-16','6125-AR-12','6125-AR-19','6127-AR-04','6127-AR-05',
'6133-AR-09','6133-AR-10','6133-AR-11','6133-AR-12','6133-AR-13','6133-AR-15','6138-AR-111','6141-AR-04','6141-AR-05','6141-AR-09','6141-AR-12','6141-AR-13','6141-AR-16',
'6143-AR-05','6154-AR-06','6158-AR-02','6160-AR-11','6161-AR-14','6164-AR-06','6164-AR-07','6164-AR-08','6164-AR-09','6164-AR-10','6165-AR-09',
'6174-AR-04','6174-AR-05','6174-AR-06','6175-AR-10','6176-AR-04','6176-AR-05','6179-AR-07','6182-AR-09','6183-AR-11','6184-AR-06','6184-AR-07','6184-AR-08',
'6189-AR-11','6195-AR-16','6195-AR-17','6196-AR-06','6196-AR-07'}
DROP={'6153-AR-14':'第三方市場占比未註明年度，無法補足年份，無法修正'}
# (regex, repl) per id prefix groups
def sub(i,pat,rep):
    s=st(i); n=re.sub(pat,rep,s); assert n!=s,(i,s); return n
out=[]
for it in d:
    i=it['id']; r={'id':i}
    if i in KEEP: r.update(action='KEEP',reason='陳述已說明分母或屬非占比之成長率／良率／自述市占，無須修改')
    elif i in DROP: r.update(action='DROP',reason=DROP[i])
    else:
        r['action']='FIX'; na=None
        if i=='6117-AR-20':
            n=st(i).replace('依IDC統計','公司於年報自述，依IDC統計').replace('公司年報稱佔有率','佔有率'); na='公司年報自述（未經獨立驗證的排名或評價）'; rs='占有率為公司依IDC統計自行計算，應標示自述'
        elif i=='6117-AR-21':
            n=st(i).replace('依TrendForce','公司於年報自述，依TrendForce').replace('公司年報稱占有率','占有率'); na='公司年報自述（未經獨立驗證的排名或評價）'; rs='占有率為公司依第三方資料自行計算，應標示自述'
        elif i=='6187-AR-07':
            n=st(i).replace('年報依經濟部','公司於年報自述，依經濟部'); na='公司年報自述（未經獨立驗證的排名或評價）'; rs='市占率為公司自行估算，應標示自述'
        elif i=='6127-AR-06':
            n='公司於年報自述氧化鋁陶瓷基板市佔率，114年度九豪國內市佔率為36%、全球市佔率為13%。'; na='公司年報自述（未經獨立驗證的排名或評價）'; rs='市佔率為公司自身評述，應標示自述'
        elif i=='6153-AR-15':
            n='公司年報引述2025年報導，全球軟板市場主要供應商中，台灣廠商臻鼎（19.9%）和台郡（5.6%）位列全球前五大軟板廠商（原文未載百分比之分母）。'; rs='百分比分母不明，加註原文未載'
        elif i.startswith('6116-AR'):
            n=st(i).replace('占百分比','占產品項目表合計'); rs='補明分母為產品項目表合計'
        elif i.startswith('6115-AR'):
            n=st(i).replace('比率','占銷售地區表合計'); rs='補明分母為銷售地區表合計'
        elif i.startswith('6117-AR'):
            n=st(i).replace('占銷售比例','占銷售地區表合計'); rs='補明分母為銷售地區表合計'
        elif i=='6120-AR-05' or i=='6120-AR-06':
            n=st(i).replace('，占','，占該表合計'); rs='補明分母為該表合計'
        elif i=='6124-AR-102':
            n=st(i).replace('，占','，占該表合計'); rs='補明分母為該表合計'
        elif i.startswith('6134-AR') or i.startswith('6190-AR'):
            n=st(i).replace('占比','占該表合計').replace('比率','占該表合計').replace('比例','占該表合計'); rs='補明分母為該表合計'
        elif i.startswith('6136-AR'):
            n=st(i).replace('業務比重','占營業比重表合計'); rs='補明分母為營業比重表合計'
        elif i.startswith('6142-AR'):
            n=st(i).replace('占比','占銷售地區表合計'); rs='補明分母為銷售地區表合計'
        elif i.startswith('6152-AR'):
            n=st(i).replace('銷售比率','占銷售地區表合計'); rs='補明分母為銷售地區表合計'
        elif i.startswith('6153-AR'):
            n=st(i).replace('占比','占銷售地區表合計'); rs='補明分母為銷售地區表合計'
        elif i.startswith('6156-AR') or i.startswith('6194-AR'):
            n=st(i).replace('占比','占銷售地區表合計').replace('，占','，占銷售地區表合計') if '占比' in st(i) else st(i).replace('，占','，占銷售地區表合計'); rs='補明分母為銷售地區表合計'
        elif i.startswith('6161-AR') or i.startswith('6166-AR') or i.startswith('6191-AR') or i.startswith('6188-AR'):
            n=st(i).replace('占比重','占銷售地區表合計').replace('，占','，占銷售地區表合計',1) if '占銷售地區表合計' not in st(i) else st(i); rs='補明分母為銷售地區表合計'
        elif i.startswith('6168-AR'):
            n=st(i).replace('占比','占銷售地區表合計'); rs='補明分母為銷售地區表合計'
        elif i.startswith('6185-AR'):
            n=st(i).replace('占比','占銷售地區內外銷分佈表合計'); rs='補明分母為銷售地區內外銷分佈表合計'
        elif i.startswith('6187-AR'):
            n=st(i).replace('占比例','占銷售地區表合計'); rs='補明分母為銷售地區表合計'
        else: raise Exception(i)
        assert n!=st(i),i
        r['new_statement']=n
        if na: r['new_attribution']=na
        r['reason']=rs
    out.append(r)
with open('bp016.jsonl','w',encoding='utf8') as f:
    for r in out: f.write(json.dumps(r,ensure_ascii=False)+'\n')
from collections import Counter
print(Counter(r['action'] for r in out),len(out))
for r in out:
    if r['action']=='FIX': print(r['id'],r['new_statement'])
