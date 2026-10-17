import json
d=json.load(open('research-site/ops/renames/jobs/rn_004.json',encoding='utf8'))
N={'2371':'僅協會更名','2375':'僅子公司更名','2376':'僅委員會與子公司更名','2392':'僅被收購子公司更名','2395':'僅被併購標的品牌更名','2432':'僅子公司更名','2444':'僅產品更名','2460':'僅越南子公司更名','2465':'僅子公司更名','2409':'僅委員會與子公司更名','2412':'僅方案、委員會、辦法更名'}
with open('research-site/ops/renames/out/rn_004.jsonl','w',encoding='utf8') as f:
    for e in d:
        n=N.get(e['id'],'命中僅為委員會、辦法、單位或酬金表欄位名稱更名，非公司本身更名')
        f.write(json.dumps({'id':e['id'],'renames':[],'note':n},ensure_ascii=False)+'\n')
print(len(d))
