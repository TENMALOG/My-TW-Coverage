import json,sys,re
sys.path.insert(0,'research-site/scripts/annual')
from slice_annual import page_texts
jobs=json.load(open('research-site/ops/renames/jobs/rn_015.json',encoding='utf-8'))
# id -> list of (former,new,date,kind,page,regex to extract excerpt)
R={
'6222':[('','','115 年 2 月 25 日','chinese',44,r'115 年 2 月 25 日.{0,40}變更公司名稱辦理換發股票作業相關事宜案')],
'6236':[('康呈科技股份有限公司','中湛股份有限公司','','chinese',1,r'\(更名前：康呈科技股份有限公司\)')],
'6240':[('松崗數位文創股份有限公司','松崗國際興業股份有限公司','','chinese',1,r'\(原名：松崗數位文創股份有限公司\)')],
'6241':[('','鑫永洋科技股份有限公司','114.11.07','chinese',25,r'5\.本公司更名案。\s*6\.修訂「公司章程」')],
'6451':[('Amtec Holdings Limited','ShunSin Technology Holdings Limited','2013 年 8 月 28 日','english',11,r'原名稱為 Amtec Holdings\s+Limited，於 2013 年 8 月 28 日經股東會決議變更本公司名稱')],
}
NOTE={
'6222':'年報僅載115年2月25日董事會決議因應變更公司名稱辦理換發股票，未載新舊名稱；其餘命中為無關。',
'6236':'封面載更名前為康呈科技股份有限公司；更名日期未載。',
'6240':'封面載原名松崗數位文創股份有限公司；更名日期未載。p71 之數位瑞崎(原名新采國際開發)為訴訟對方，不計。',
'6241':'年報僅載114.11.07董事會「本公司更名案」及更名換票基準日，未載舊名；新名依年報內文通稱鑫永洋科技；證券簡稱易通展可能為舊名但年報未載，不臆測。',
'6451':'僅英文名稱變更(開曼控股公司原名 Amtec Holdings Limited)。',
}
out=[]
for j in jobs:
    t=j['id']; rs=[]
    if t in R:
        f=json.load(open(f"research-site/data/company-facts/{t}.json",encoding='utf-8'))
        pt=page_texts(open(f['source']['text_path'],encoding='utf-8').read())
        for fo,nw,d,k,p,rx in R[t]:
            m=re.search(rx,pt[p],re.S); assert m,(t,rx)
            ex=m.group(0); assert ex in pt[p] and len(ex)>=8
            rs.append(dict(former_name=fo,new_name=nw,date_text=d,kind=k,page=p,excerpt=ex))
    note=NOTE.get(t,'命中僅為委員會、辦法、守則、部門、子公司或產品等更名，非發行公司本身更名。')
    out.append(json.dumps(dict(id=t,renames=rs,note=note),ensure_ascii=False))
open('research-site/ops/renames/out/rn_015.jsonl','w',encoding='utf-8',newline='\n').write('\n'.join(out)+'\n')
print(len(out))
