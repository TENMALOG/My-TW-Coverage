import json,sys
sys.path.insert(0,'research-site/scripts/annual')
from slice_annual import page_texts
jobs=json.load(open('research-site/ops/renames/jobs/rn_009.json',encoding='utf-8'))
notes={
'3465':'僅委員會更名（薪資報酬委員會），非公司本身',
'3490':'僅審計委員會更名，非公司本身',
'3499':'僅內部守則更名',
'3521':'報告僅載董事會通過「公司名稱及所在地變更案」並辦理更名換發有價證券，未載明舊名與新名全稱；宏潤興業（原鴻潤建設）為子公司',
'3552':'僅獨立董事個人更名',
'3555':'僅子公司更名','3609':'僅子公司更名','3633':'僅子公司更名','3680':'僅轉投資事業更名',
'3664':'僅控制公司（光聚晶電，原大宇資訊）更名，非發行人','3673':'僅子公司更名','3672':'僅子公司更名',
'3548':'僅內部規章／子公司更名','3687':'僅委員會及子公司（歐付寶）更名',
'3541':'僅內部守則更名及客戶更名','3661':'僅學校更名及章程條文，與公司無關',
}
out=[]
for j in jobs:
    r=[]
    if j['id']=='3521':
        f=json.load(open('research-site/data/company-facts/3521.json',encoding='utf-8'))
        pt=page_texts(open(f['source']['text_path'],encoding='utf-8').read())
        ex='通過本公司公司名稱及所在地變更案'
        assert ex in pt[40]
        r=[{"former_name":"","new_name":"","date_text":"114.08.11","kind":"chinese","page":40,"excerpt":ex}]
        r[0]["new_name"]="台鋼建設事業股份有限公司"
    out.append({"id":j['id'],"renames":r,"note":notes.get(j['id'],'命中頁僅為酬金表欄位名稱、內部規章或子公司等非發行人更名' if not r else '')})
with open('research-site/ops/renames/out/rn_009.jsonl','w',encoding='utf-8',newline='\n') as fh:
    for o in out: fh.write(json.dumps(o,ensure_ascii=False)+'\n')
print(len(out),sum(1 for o in out if o['renames']))
