import json,sys,re
sys.path.insert(0,'research-site/scripts/annual')
from slice_annual import page_texts
jobs=json.load(open('research-site/ops/renames/jobs/rn_010.json',encoding='utf-8'))
cache={}
def pg(t,p):
    if t not in cache:
        f=json.load(open(f"research-site/data/company-facts/{t}.json",encoding='utf-8'))
        cache[t]=page_texts(open(f['source']['text_path'],encoding='utf-8').read())
    return cache[t][p]
def ex(t,p,start,end):
    x=pg(t,p); i=x.index(start); j=x.index(end,i)+len(end)
    return x[i:j]
R={}
def add(t,former,new,date,kind,p,start,end):
    R.setdefault(t,[]).append(dict(former_name=former,new_name=new,date_text=date,kind=kind,page=p,excerpt=ex(t,p,start,end)))
add('4154','','康樂股份有限公司','2019年','chinese',8,'本公司更名為康樂股份有限公司','康樂股份有限公司')
add('4154','','樂威科股份有限公司','2021年7月','chinese',8,'2021年7月股東會通過變更公司名稱為樂威科股份有限公司','Raku Co., Ltd.')
add('4402','福大材料科技股份有限公司','郡都開發股份有限公司','','chinese',1,'郡都開發股份有限公司','福大材料科技股份有限公司')
add('4413','赤崁科技股份有限公司','飛寶動能股份有限公司','民國 96 年6 月','chinese',78,'本公司原名「赤崁科技股份有限公司」','飛寶動能股份有限公司」')
add('4413','飛寶動能股份有限公司','飛寶企業股份有限公司','民國 105 年6月','chinese',78,'再於民國 105 年6月','飛寶企業股份有限公司」')
add('4426','利冠實業股份有限公司','利勤實業股份有限公司','民國九十年間','chinese',87,'原名為利冠實業股份有限公司','合併後更名為利勤實業股份有限公司')
add('4538','詠成機械鑄造有限公司','詠成機械鑄造(股)公司','73.09.01','chinese',63,'設立名稱為','詠成機械鑄造(股)公司')
add('4538','','大詠成機械(股)公司','98 年 7 月','chinese',63,'98 年 7 月更名為','大詠成機械(股)公司')
add('4538','','大詠城機械股份有限公司','100 年 6 月','chinese',63,'100 年 6 月公司更名為','大詠城機械股份有限公司')
add('4550','長欣機電工程股份有限公司','長佳機電工程股份有限公司','84 年 03 月 16 日','chinese',58,'84 年 03 月 16 日','長佳機電工程股份有限公司')
add('4583','台灣廣用科技(股)公司','台灣精銳科技股份有限公司','','chinese',97,'台灣廣用科技','台灣精銳科技股份有限公司')
NOTE={
'4154':'2019年更名康樂、2021年7月再變更為樂威科（報告未於同句寫出前名，former_name留空）',
'4402':'封面載明原名福大材料科技，年報未載更名日期',
'4426':'民國90年合併原利勤實業後更名；前名利冠實業',
'4538':'公司設立登記沿革註記，共三次更名；後兩筆報告僅寫新名，former_name留空',
'4550':'變更公司名稱 84年3月16日',
'4583':'台灣廣用科技吸收原台灣精銳合併後更名；日期未載',
'3713':'新設控股公司(股份轉換取得頂晶)，非更名；p52為同業三家整併',
'3714':'僅子公司晶元光電更名富采光電及委員會更名；p81「本公司更名換發股票」屬子公司議程，富采控股本身名稱未變',
'3715':'僅子公司更名','3717':'僅委員會及程序名稱更名','4506':'僅轉投資公司更名','4569':'僅子公司更名',
'4577':'僅子公司更名','4716':'僅被投資公司更名','4306':'僅委員會、報告書及子公司原名','4545':'僅競爭者原名',
'4552':'僅子公司更名','4566':'僅蘇州子公司及委員會更名','4563':'僅子公司更名討論案','4581':'僅英文原名描述上市主體設立，非更名',
'3702':'僅子公司/部門更名','3711':'僅委員會更名','4532':'僅委員會更名','4576':'僅委員會更名','4582':'僅守則及辦法更名',
'4554':'僅同業前身描述'}
out=[]
for j in jobs:
    t=j['id']; r=R.get(t,[])
    note=NOTE.get(t,'命中僅為董事酬金級距表欄位名稱修改說明，非公司更名' if not r else '')
    out.append(json.dumps(dict(id=t,renames=r,note=note),ensure_ascii=False))
open('research-site/ops/renames/out/rn_010.jsonl','w',encoding='utf-8').write('\n'.join(out)+'\n')
print(len(out),sum(1 for t in R))
