import json,sys
sys.path.insert(0,'research-site/scripts/annual')
from slice_annual import page_texts
jobs=json.load(open('research-site/ops/renames/jobs/rn_013.json',encoding='utf-8'))
R={
'5529':([("志嘉建設股份有限公司","鉅陞國際開發股份有限公司","",'chinese',91,"鉅陞國際開發股份有限公司(原名志嘉建設股份有限公司)")],"關係報告書會計師複核報告載明原名，無日期"),
'5543':([("","桓鼎股份有限公司","2020 年 9 月",'chinese',63,"本公司於 2020 年 9 月更名為桓鼎股份有限公司")],"報告未載明舊名"),
'5902':([("立中實業股份有限公司","德記事業股份有限公司","民國 79 年 11 月 28 日",'chinese',7,"公司變更名稱德記事業股份有限公司"),
         ("德記事業股份有限公司","德記洋行股份有限公司","民國 84 年 5 月",'chinese',8,"公司股東會決議改名為德記洋行股份有限公司")],"79年條目年份取自公司沿革表年度欄；舊名立中實業見p7民國76年設立條"),
'6021':([("","美好證券","111 年",'chinese',122,"111 年本公司正式更名為美好證券")],"報告未載明舊名，新名以報告寫法「美好證券」"),
}
notes={'5871':"公司沿革的中租迪和合併更名為前身營運公司（中租控股為2014年後之控股公司），非發行人本身；其餘為委員會/守則更名或子公司",
'5515':"僅子公司創建機電更名","6024":"僅子公司更名","6112":"僅投資人/組織/委員會更名","5878":"僅往來保險公司更名","6028":"僅往來保險公司更名",
'5609':"僅委員會與子公司更名","6005":"僅委員會與轉投資事業更名","5531":"僅守則更名","5536":"僅守則/委員會更名","5530":"僅委員會更名"}
out=[]
for j in jobs:
    t=j['id']; rs=[]
    if t in R:
        f=json.load(open(f"research-site/data/company-facts/{t}.json",encoding='utf-8'))
        pt=page_texts(open(f['source']['text_path'],encoding='utf-8').read())
        for fo,nw,d,k,p,ex in R[t][0]:
            assert ex in pt[p],(t,ex)
            rs.append(dict(former_name=fo,new_name=nw,date_text=d,kind=k,page=p,excerpt=ex))
        note=R[t][1]
    else: note=notes.get(t,"命中僅為酬金表欄位名稱、守則/委員會更名或無關內容，無發行人更名")
    out.append(json.dumps(dict(id=t,renames=rs,note=note),ensure_ascii=False))
open('research-site/ops/renames/out/rn_013.jsonl','w',encoding='utf-8').write('\n'.join(out)+'\n')
print(len(out),sum(1 for l in out if '"renames": []' not in l))
