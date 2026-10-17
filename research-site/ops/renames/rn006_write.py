import json,sys,re
sys.path.insert(0,'research-site/scripts/annual')
from slice_annual import page_texts
jobs=json.load(open('research-site/ops/renames/jobs/rn_006.json',encoding='utf-8'))
def pages(i):
    f=json.load(open(f"research-site/data/company-facts/{i}.json",encoding='utf-8'))
    return page_texts(open(f['source']['text_path'],encoding='utf-8').read())
def ex(i,p,pat,before=0,after=0):
    t=pages(i)[p];m=re.search(pat,t);assert m,(i,p,pat)
    return t[max(0,m.start()-before):m.end()+after]
R={}
R['2642']=([dict(former_name='昱捷物流(股)公司',new_name='台灣宅配通(股)公司',date_text='89.07',kind='chinese',page=79,
  excerpt=ex('2642',79,r'由昱捷物流 \(股\)公司更名為\s*台灣宅配通\(股\)公司'))],'')
R['2762']=([dict(former_name='World Fitness Services Ltd.',new_name='World Gym Corporation',date_text='2025年',kind='english',page=15,
  excerpt=ex('2762',15,r'由原先的 World Fitness\s+Services Ltd\.更名為 World Gym Corporation'))],'中文名稱世界健身股份有限公司未變，僅英文名稱更名；2025/5/13董事會有「本公司名稱變更案」')
R['2885']=([dict(former_name='復華金控',new_name='元大金控',date_text='91.02',kind='chinese',page=158,
  excerpt=ex('2885',158,r'復華金控（\s*更名\s*為元大金控）為股份轉換'))],'股本形成過程表；同表另載子公司復華證金/復華證券/亞太銀行更名，未收錄')
R['2887']=([dict(former_name='',new_name='台新新光金融控股股份有限公司',date_text='114 年 7 月 24 日',kind='chinese',page=6,
  excerpt=ex('2887',6,r'本公司已於 114 年 7 月 24 日與新光金控完成合併，\s*合併後更名為「台新新光金融控股股份有限公司」'))],'報告未明載前名(僅稱與新光金控合併後更名)，故former_name留空；台新人壽更名新光人壽屬子公司未收錄')
R['2724']=([dict(former_name='FX Hotels Group Inc.',new_name='Architectural Aesthetics Global Development CO.,LTD.',date_text='',kind='english',page=1,
  excerpt=ex('2724',1,r'FX Hotels Group Inc\.'))],'封面字型亂碼，括號內疑為「曾用名」，僅FX Hotels Group Inc.可辨；p62關係企業表載發行人本身91.01.15成立、97.05.07更名、112.11.06更名，但未載各次名稱，故未另列；台灣富驛與藝舍公司合併更名屬子公司')
out=[]
for j in jobs:
    r,n=R.get(j['id'],([], '命中頁僅為委員會/辦法/部門/子公司/投資事業等更名或欄位名稱修改，非發行人本身更名'))
    out.append(json.dumps(dict(id=j['id'],renames=r,note=n),ensure_ascii=False))
open('research-site/ops/renames/out/rn_006.jsonl','w',encoding='utf-8').write('\n'.join(out)+'\n')
print(len(out),sum(1 for l in out if '"former_name"' in l))
