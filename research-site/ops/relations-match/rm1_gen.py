import json,collections
d=json.load(open('ops/relations-match/in_1.json',encoding='utf8'))
M={ # idx: (ticker, role, reason)
 38:('2231','supplier','聲明稱「為升電裝」，與為升電裝工業(2231)相符；年報稱其為母公司，採購關係角色為供應商'),
 53:('2317','supplier','鴻海公司即鴻海精密工業(2317)'),
 55:('2317','customer','鴻海公司即鴻海精密工業(2317)'),
 63:('4919','subsidiary','聲明明確稱子公司新唐科技股份有限公司，對應新唐(4919)'),
 69:('2409','supplier','友達光電(股)公司即友達光電(2409)'),
 71:('3481','supplier','群創光電(股)公司即群創光電(3481)'),
 140:('1303','supplier','南亞塑膠即南亞塑膠工業(1303)'),
 177:('1101','supplier','台灣水泥股份有限公司即臺灣水泥(1101)，臺/台差異'),
 190:('2010','supplier','春源鋼鐵工業(股)公司即春源鋼鐵工業(2010)'),
 209:('2330','customer','台灣積體電路製造(股)公司即台積電(2330)'),
 210:('2520','customer','冠德建設(股)公司即冠德建設(2520)'),
 250:('2618','supplier','長榮航空(股)公司即長榮航空(2618)'),
 251:('2610','supplier','中華航空(股)公司即中華航空(2610)'),
}
# BAD_NAME indexes (generic, code names, fragments, group counts)
BAD=set([43,51,52,54,56,57,58,62,65,87,90,105,106,107,108,129,130,132,133,134,135,136,137,138,139,141,144,150,164,167,168,169,170,171,172,173,178,200,201,202,203,204,220,221,222,223,230,231,232,233,234,235,236,242,246,254,264,265,266,267,268,278,279,297,298,301,307,309,310,319])
# fix indices: items use 0-based idx from candidate listing
BAD-= {164,105,200,222}
BAD|= {296,211,160,61,95,238}
# per-item reasons for NOT_LISTED
res=[]
for i,x in enumerate(d):
    c=x['counterparty']
    if i in M:
        t,r,why=M[i];v='MATCH'
    elif i in BAD:
        v='BAD_NAME';t=None;r=x['role'];why='非明確組織名稱（泛稱、代號、斷詞片段或數量描述）'
    else:
        v='NOT_LISTED';t=None;r=x['role']
        why='真實組織但不在上市櫃清單（外商、民營、政府機關、或上市公司之子公司/分公司/關係企業）'
        if i in (96,164,226,88,85,18): why='指向發行人本身或其子公司，非另一家上市公司'
        if i==44: why='納智捷為品牌/關係企業，非清單中之智捷(8176)'
        if i in (26,): why='日產指日本日產汽車，非裕隆日產(2227)'
    res.append({"relation_id":x['relation_id'],"fact_id":x['fact_id'],"counterparty":c,"verdict":v,"counterparty_ticker":t,"role":r,"reason":why})
with open('ops/relations-match/out_1.jsonl','w',encoding='utf8') as f:
    for r in res: f.write(json.dumps(r,ensure_ascii=False)+'\n')
print(len(res),collections.Counter(r['verdict'] for r in res))
for i in sorted(BAD): print(i,d[i]['counterparty'])
