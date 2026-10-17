import json,sys
sys.path.insert(0,'research-site/scripts/annual')
from slice_annual import page_texts
jobs=json.load(open('research-site/ops/renames/jobs/rn_017.json',encoding='utf-8'))
# id -> list of (former,new,date,kind,page,start_anchor,end_anchor)
R={
'6803':[('崑鼎投資控股股份有限公司','崑鼎綠能環保股份有限公司','','chinese',1,'( 原名: 崑鼎投資','控股股份有限公司 )')],
'6952':[('大武山畜產開發股份有限公司','山水畜產開發股份有限公司','104 年 3 月','chinese',91,'本公司原登記名稱為','大武山畜產開發股份有限公司'),
        ('山水畜產開發股份有限公司','大武山牧場科技股份有限公司','111 年 1 月','chinese',91,'國 104 年 3 月及','大武山牧')],
'6953':[('家登自動化股份有限公司','家碩科技股份有限公司','','chinese',1,'(原名：家登自動化','股份有限公司)')],
'6962':[('英屬開曼群島商奕力科技( 開曼) 股份有限公司','ITH Corporation','2021年7月6日','chinese',6,'後於2021年7月6日','更名為ITH Corporation')],
'7578':[('利百景環保科技股份有限公司','利百景股份有限公司','','chinese',1,'(原名：利百景環保','科技股份有限公司)')],
}
notes={'6803':'僅年報封面載明原名，無日期','6953':'年報封面載明原名，無日期','7578':'年報封面載明原名，無日期；p37附註亦提及更名','6962':'原中文名稱更名為英文名 ITH Corporation'}
out=[]
for j in jobs:
    f=json.load(open(f"research-site/data/company-facts/{j['id']}.json",encoding='utf-8'))
    pt=page_texts(open(f['source']['text_path'],encoding='utf-8').read())
    rs=[]
    for fo,ne,d,k,p,a,b in R.get(j['id'],[]):
        t=pt[p];i=t.index(a);e=t.index(b,i)+len(b)
        ex=t[i:e]
        assert len(ex)>=8
        if d: assert d in ex or d in t, d
        rs.append(dict(former_name=fo,new_name=ne,date_text=d,kind=k,page=p,excerpt=ex))
    n=notes.get(j['id'],'' if rs else '命中僅為委員會、法規、子公司、人名或程序更名，非發行公司本身')
    out.append(dict(id=j['id'],renames=rs,note=n))
with open('research-site/ops/renames/out/rn_017.jsonl','w',encoding='utf-8') as fh:
    for o in out: fh.write(json.dumps(o,ensure_ascii=False)+'\n')
print(len(out),sum(1 for o in out if o['renames']))
for o in out:
    for r in o['renames']: print(o['id'],repr(r['excerpt']))
