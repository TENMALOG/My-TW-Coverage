import json,sys
sys.path.insert(0,'research-site/scripts/annual')
from slice_annual import page_texts
jobs=json.load(open('research-site/ops/renames/jobs/rn_011.json',encoding='utf-8'))
R={
'4738':([("尚志精密化學股份有限公司","大同精密化學股份有限公司","",'chinese',1,"原名：尚志精密化學股份有限公司")],"封面載明原名尚志精密化學，未載更名日期"),
'4765':([("磐采油墨有限公司","磐采股份有限公司","中華民國九十四年八月",'chinese',48,"由原「磐采油墨有限公司」更名為「磐采股份有限公司」")],"註4同時載明改制為股份有限公司"),
'4915':([("鴻傳投資股份有限公司","致伸科技股份有限公司","",'chinese',37,"原名鴻傳投資 ( 股 ) 公司")],"p37載明本集團原名鴻傳投資(股)公司，96年12月28日合併原致伸科技；更名日期未明載，名稱以報告簡稱為準"),
'4950':([("牧東光電股份有限公司","金耘國際股份有限公司","114 年2月份",'chinese',5,"「牧東光電股份有限公司」 更名為 「金耘國際股份有限公司」")],""),
'4977':([("","PCL TECHNOLOGIES, INC.","98年5月",'english',9,"98年5月 本公司正式更名為PCL TECHNOLOGIES, INC.")],"p9載明設立時為PCL HOLDING, INC.，但未明載98年5月更名前的名稱，故former_name留空"),
}
N={
'4912':"僅獨立董事個人姓名更名",'4903':"僅法人董事之母公司更名，非本公司",'4763':"僅子公司濟南大自然更名；本公司(開曼)設立時即為現名",
'4953':"命中僅為委員會議案更名，報告未載本公司更名",'4924':"僅子公司更名",'4916':"僅轉投資公司更名",'4906':"僅子公司Genix Networks更名",
'4960':"僅對方公司更名",'4968':"僅子公司更名",'4980':"僅股東更名",'4994':"僅部門及人員姓名更名",'5014':"僅子公司更名",'4935':"僅政策/廠名更名",
}
out=[]
for j in jobs:
    k=j['ticker']; rs=[]; note=N.get(k,"")
    if k in R:
        pt=page_texts(open(json.load(open(f"research-site/data/company-facts/{k}.json",encoding='utf-8'))['source']['text_path'],encoding='utf-8').read())
        for f,n,d,kind,p,ex in R[k][0]:
            assert ex in pt[p],(k,ex)
            if d: assert d in pt[p],(k,d)
            rs.append(dict(former_name=f,new_name=n,date_text=d,kind=kind,page=p,excerpt=ex))
        note=R[k][1]
    elif not note: note="命中僅為董事酬金級距表欄位名稱、委員會或制度更名，非公司更名"
    out.append(json.dumps(dict(id=k,renames=rs,note=note),ensure_ascii=False))
open('research-site/ops/renames/out/rn_011.jsonl','w',encoding='utf-8').write("\n".join(out)+"\n")
print(len(out),sum(1 for l in out if '"former_name"' in l))
