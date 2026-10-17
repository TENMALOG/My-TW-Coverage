import json
jobs=json.load(open('research-site/ops/renames/jobs/rn_014.json',encoding='utf-8'))
notes={
'6120':'命中為永續發展委員會更名，非公司本身。',
'6142':'命中為母公司（台灣網通投資控股）及投資對象（元勝國際實業）更名，非發行人本身。',
'6146':'命中為董事會績效評估辦法更名。',
'6147':'命中為委員會及守則更名。',
'6148':'命中為委員會、守則及ESG評鑑更名。',
'6153':'命中為CSR委員會更名。',
'6160':'命中為學校及守則更名。',
'6168':'命中為守則更名。',
'6170':'命中為零售通路客戶更名。',
'6176':'命中為委員會更名。',
'6177':'命中為子公司（定城營造）更名。',
'6182':'命中為委員會更名。',
'6189':'命中為學校、供應商及客戶更名。',
'6191':'命中為投資對象（Lincstech）更名。',
'6196':'命中為子公司（智群智慧）更名。',
'6206':'命中為守則、委員會及辦法更名。',
'6214':'命中為內部單位更名。',
'6218':'命中為守則更名。',
'6139':'命中為子公司更名。',
}
ex={'id':'6199','former_name':'天品投資控股股份有限公司','new_name':'天品聯合企業股份有限公司','date_text':'','kind':'chinese','page':1,'excerpt':'（原名：天品投資控股股份有限公司）'}
out=[]
for j in jobs:
    r=[ex] if j['id']=='6199' else []
    note=notes.get(j['id'],'命中僅為酬金表欄位名稱等無關文字，無公司更名。' if j['hits'] else '')
    if j['id']=='6199': note='年報封面載明原名，僅有封面說明，無日期。'
    out.append({'id':j['id'],'renames':r,'note':note})
with open('research-site/ops/renames/out/rn_014.jsonl','w',encoding='utf-8') as f:
    for o in out: f.write(json.dumps(o,ensure_ascii=False)+'\n')
print(len(out))
