import json,sys,re
sys.path.insert(0,'research-site/scripts/annual')
from slice_annual import page_texts
job=json.load(open('research-site/ops/renames/jobs/rn_001.json',encoding='utf8'))
def page(t,p):
    f=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
    return page_texts(open(f['source']['text_path'],encoding='utf8').read())[p]
def cut(t,p,a,b):
    s=re.sub(r'\s+',' ',page(t,p)); i=s.index(a); j=s.index(b,i)+len(b)
    return s[i:j]
R={}
R['1463']=([dict(former_name="強盛染整股份有限公司",new_name="強盛新投資控股股份有限公司",date_text="115年 2 月 1 日",kind="chinese",page=69,
  excerpt=cut('1463',69,"本公司前身為強盛染整股份有限公司","強盛新投資控股股份有限公司"))],
  "報告 p69 稱前身為強盛染整、115年2月轉型為控股公司並更名（p5、p59 亦載變更公司名稱）；但 p68 列強盛染整為子公司，屬分割/股份轉換架構，發行人身分銜接略有不確定，已保守記錄。")
R['1525']=([dict(former_name="江申五金廠",new_name="江申五金製品廠有限公司",date_text="民國 52 年",kind="chinese",page=7,
  excerpt=cut('1525',7,"創立江申五金廠","江申五金製品廠有限公司")),
  dict(former_name="江申五金製品廠有限公司",new_name="江申工業股份有限公司",date_text="民國 67 年",kind="chinese",page=7,
  excerpt=cut('1525',7,"江申五金製品廠有限公司","江申工業股份有限公司"))],
  "公司沿革。第一筆前名「江申五金廠」為創立時名稱（頁面未明寫更名前名稱，僅『創立江申五金廠』）。")
NOTES={'1590':"hits 為亞德客國際集團（開曼）簡介：正碁實業更名為亞德客工業 1990 年是台灣子公司，非上市發行人本身，故不記錄。",
 '1519':"僅涉及轉投資公司眾意能源、華城重電更名，非發行人。",
 '1532':"僅涉及子公司全國物業管理更名，非發行人。",
 '1560':"僅涉及子公司 MKS 更名，非發行人。",
 '1598':"僅涉及子公司益可達科技更名，非發行人。"}
with open('research-site/ops/renames/out/rn_001.jsonl','w',encoding='utf8') as o:
    for e in job:
        t=e['id']
        if t in R: r,n=R[t]
        else: r,n=[],NOTES.get(t,"hits 僅為董監酬金表註（欄位名稱改為…）、委員會/守則/制度更名等，無發行人本身更名。")
        o.write(json.dumps({"id":t,"renames":r,"note":n},ensure_ascii=False)+"\n")
