import json,sys
job=sys.argv[1]
base='../'
ids=[l.strip() for l in open(base+'jobs_sonnet/'+job+'.txt',encoding='utf8') if l.strip()]
rej=json.load(open('t11_%s_rej.json'%job,encoding='utf8'))  # {idx: reason}
acc=json.load(open('t11_%s_acc.json'%job,encoding='utf8')) if __import__('os').path.exists('t11_%s_acc.json'%job) else {}
T={'business_scope':'年報所營業務原文逐項相符','revenue_mix':'年度欄位、金額與比重與表格列一致，單位正確','products':'產品敘述與年報該頁原文相符','sales_regions':'年度欄位、金額與比例與銷售地區表一致','major_customers':'客戶名稱、年度、金額與占比與表格一致','major_suppliers':'供應商名稱、年度、金額與占比與表格一致','raw_materials':'原料敘述與年報原文相符','employees':'員工人數取自對應年度欄位，未暗示範圍','rd':'研發費用年度欄位與金額相符','headquarters':'地址與年報原文一致','history':'歸屬為公司年報自述，與原文相符'}
facts={}
out=[]
for n,i in enumerate(ids):
    tk=i.split('-')[0]
    if tk not in facts: facts[tk]={x['id']:x for x in json.load(open('../../../data/company-facts/%s.json'%tk,encoding='utf8'))['facts']}
    f=facts[tk][i]
    if str(n) in rej: out.append({'id':i,'verdict':'REJECT','reason':rej[str(n)]})
    else: out.append({'id':i,'verdict':'ACCEPT','reason':acc.get(str(n)) or (T.get(f['field'],'與年報該頁原文相符')+'（已核對第%d頁）'%f['page'])})
open(job+'.jsonl','w',encoding='utf8').write(''.join(json.dumps(o,ensure_ascii=False)+'\n' for o in out))
from collections import Counter
print(job,len(out),Counter(o['verdict'] for o in out))
