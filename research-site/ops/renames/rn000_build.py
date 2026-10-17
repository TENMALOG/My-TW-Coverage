import json,sys
sys.path.insert(0,'research-site/scripts/annual')
from slice_annual import page_texts
jobs=json.load(open('research-site/ops/renames/jobs/rn_000.json',encoding='utf8'))
def pg(t):
    f=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
    return page_texts(open(f['source']['text_path'],encoding='utf8').read())
S={
'1316':[('上曜塑膠股份有限公司','上曜開發科技股份有限公司','99 年','chinese',54,'本公司前身為上曜塑膠股份有限公司，99 年核准變更為上曜開發科技股份有限公司'),
        ('上曜開發科技股份有限公司','上曜建設開發股份有限公司','105 年','chinese',54,'99 年核准變更為上曜開發科技股份有限公司，105 年正式更名為上曜建設開發股份有限公司')],
'1418':[('東華合纖股份有限公司','東華龍股份有限公司','','chinese',1,'(原名：東華合纖股份有限公司)')],
}
notes={'1316':'公司沿革於永續章節以文字記載兩次更名','1418':'封面註明原名，年報內未見更名日期'}
out=[]
for e in jobs:
    t=e['ticker'];rs=[]
    for a,b,d,k,p,x in S.get(t,[]):
        assert x in pg(t)[p],(t,x)
        rs.append(dict(former_name=a,new_name=b,date_text=d,kind=k,page=p,excerpt=x))
    out.append(json.dumps(dict(id=t,renames=rs,note=notes.get(t,'命中僅為委員會、守則、辦法、報告書、轉投資事業、子公司或交易對手等更名，非發行公司本身；無自身更名記載' if True else '')),ensure_ascii=False))
open('research-site/ops/renames/out/rn_000.jsonl','w',encoding='utf8',newline='\n').write('\n'.join(out)+'\n')
print(len(out))
