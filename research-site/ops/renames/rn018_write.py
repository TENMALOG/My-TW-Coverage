import json,sys,re
sys.path.insert(0,'research-site/scripts/annual')
from slice_annual import page_texts
jobs=json.load(open('research-site/ops/renames/jobs/rn_018.json',encoding='utf-8'))
R={
'8080':[('印鉐事業','泰霖事業','','chinese',1,'原名 : 印鉐事業')],
'8087':[('華鎂鑫科技股份有限公司','麗升能源科技股份有限公司','','chinese',120,'(原名華鎂鑫科技股份有限公司)')],
'8354':[('','冠好科技股份有限公司','102.06','chinese',41,'公司更名 無 102.06.26經授商字')],
}
N={'8080':'封面載明原名印鉐事業，未載更名日期','8087':'關係企業合併財務報表聲明書載明原名華鎂鑫科技，未載更名日期','8354':'股本形成沿革僅載102.06公司更名，未載舊名；新名取自法定名稱'}
out=[]
for j in jobs:
    t=j['ticker']; rs=[]
    if t in R:
        f=json.load(open(f"research-site/data/company-facts/{t}.json",encoding='utf-8'))
        pt=page_texts(open(f['source']['text_path'],encoding='utf-8').read())
        for fo,nw,d,k,p,ex in R[t]:
            raw=pt[p]
            # find verbatim span
            pat=re.escape(ex).replace(r'\ ',r'\s*')
            m=re.search(pat,raw)
            if not m: print('NOEXCERPT',t,ex); continue
            s=m.group(0)
            rs.append(dict(former_name=fo,new_name=nw,date_text=d,kind=k,page=p,excerpt=s))
    note=N.get(t,'僅為委員會、守則、辦法、董事個人、股務代理或交易對象等更名，非發行公司本身更名')
    out.append({'id':t,'renames':rs,'note':note})
open('research-site/ops/renames/out/rn_018.jsonl','w',encoding='utf-8').write(''.join(json.dumps(o,ensure_ascii=False)+'\n' for o in out))
print(len(out),sum(1 for o in out if o['renames']))
for o in out:
    if o['renames']: print(o)
