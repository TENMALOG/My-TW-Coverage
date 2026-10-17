import json,sys
sys.path.insert(0,'research-site/scripts/annual')
from slice_annual import page_texts
jobs=json.load(open('research-site/ops/renames/jobs/rn_012.json',encoding='utf-8'))
R={
'5243':[("Multiwin Precision Ind. Co., Ltd.","Eson Precision Ind. Co., Ltd.","101 年 2 月","english",12,"原名Multiwin Precision Ind.")],
'5345':[("天揚精密科技股份有限公司","馥鴻建設股份有限公司","","chinese",1,"(原名：天揚精密科技股份有限公司)")],
'5348':[("系通科技股份有限公司","正能量智能股份有限公司","","chinese",1,"（原名稱為系通科技股份有限公司）")],
'5381':[("合正科技股份有限公司","光譜電工股份有限公司","","chinese",1,"(原名：合正科技股份有限公司)")],
'5398':[("力瑋實業股份有限公司","慕康生技醫藥股份有限公司","民國一０六年六月二十八日","chinese",97,"原名力瑋實業股份有限公司")],
'5432':[("達威","新門","","chinese",92,"新門(更名前為達威)公司前董事")],
}
N={'5202':'僅子公司(台鋼資通訊工程更名力新創新科技)與法人董事更名，非發行人本身',
'5321':'僅稱「110年更名換股」，未載明前名，且可能指類股變更，未記錄',
'5225':'僅子公司更名','5227':'僅子公司與委員會更名','5209':'僅守則、委員會、產品更名'}
fc={}
out=[]
for j in jobs:
    t=j['id']; rs=[]
    if t in R:
        f=json.load(open(f"research-site/data/company-facts/{t}.json",encoding='utf-8'))
        pt=page_texts(open(f['source']['text_path'],encoding='utf-8').read())
        for fo,n,d,k,p,ex in R[t]:
            assert ex in pt[p],(t,ex)
            rs.append(dict(former_name=fo,new_name=n,date_text=d,kind=k,page=p,excerpt=ex))
    out.append(json.dumps(dict(id=t,renames=rs,note=N.get(t,'' if rs else '命中頁僅為委員會/守則/酬金表欄位等更名，非發行人更名')),ensure_ascii=False))
open('research-site/ops/renames/out/rn_012.jsonl','w',encoding='utf-8').write('\n'.join(out)+'\n')
print(len(out))
