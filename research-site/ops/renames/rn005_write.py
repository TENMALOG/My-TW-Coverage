import json,sys
sys.path.insert(0,'research-site/scripts/annual')
from slice_annual import page_texts
jobs=json.load(open('research-site/ops/renames/jobs/rn_005.json',encoding='utf-8'))
f=json.load(open('research-site/data/company-facts/2612.json',encoding='utf-8'))
pt=page_texts(open(f['source']['text_path'],encoding='utf-8').read())
t=pt[6]
a='偉聯運輸股份有限公司更名為中國航運運輸股份有限公司。'
i=t.find('中國航運運輸股份有限公司。\n',t.find(a)+len(a)-3)
b_start=t.find('中國航運運輸股份有限公司。', t.find(a))
b=t[b_start:t.find('中國航運股份有限公司。',b_start)+len('中國航運股份有限公司。')]
assert a in t and b in t and '93' in b
R={'2612':{"renames":[
 {"former_name":"偉聯運輸股份有限公司","new_name":"中國航運運輸股份有限公司","date_text":"民國91年8月","kind":"chinese","page":6,"excerpt":a},
 {"former_name":"中國航運運輸股份有限公司","new_name":"中國航運股份有限公司","date_text":"民國93年7月","kind":"chinese","page":6,"excerpt":b}],
 "note":"公司沿革頁記載兩次更名；第二筆excerpt含換行，為原頁逐字內容。附註一亦載原名偉聯運輸。"}}
with open('research-site/ops/renames/out/rn_005.jsonl','w',encoding='utf-8') as o:
    for j in jobs:
        r=R.get(j['id'],{"renames":[],"note":"命中僅為委員會、守則、報告書、欄位名稱或子公司/投資事業等更名，非發行公司本身更名。"})
        o.write(json.dumps({"id":j['id'],**r},ensure_ascii=False)+'\n')
