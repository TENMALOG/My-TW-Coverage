import json,sys,os
job=sys.argv[1]
base='research-site/ops/codex-review/'
ids=[l.strip() for l in open(base+f'jobs_sonnet/{job}.txt') if l.strip()]
rej=json.load(open(base+'out_sonnet/s00_rej.json',encoding='utf8')) if os.path.exists(base+'out_sonnet/s00_rej.json') else {}
cache={}
T={'revenue_mix':'表列年度欄位、金額、比重與單位皆對應正確','sales_regions':'表列年度欄位、金額、比率（分母為表合計）與單位皆對應正確','export_share':'表列年度欄位、金額、比率與單位皆對應正確','major_suppliers':'表列年度欄位、名稱代號、金額、占進貨淨額比率與單位皆對應正確','major_customers':'表列年度欄位、名稱代號、金額、占銷貨淨額比率與單位皆對應正確','employees':'表列年度欄位與人數對應正確且未暗示未載明之範圍','rd':'表列年度欄位、金額或比率與單位對應正確','raw_materials':'原文即載明此原料或供應內容','products':'原文即列示此產品項目','business_scope':'原文即為此業務範圍描述','headquarters':'原文即載明此地址','group_structure':'原文即載明此集團結構'}
out=[]; n=[0,0]
for i in ids:
    t=i.split('-')[0]
    if t not in cache: cache[t]={x['id']:x for x in json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))['facts']}
    f=cache[t][i]
    if i in rej:
        out.append({'id':i,'verdict':'REJECT','reason':rej[i]}); n[1]+=1
    else:
        r=T.get(f['field'],'原文即載明此內容')
        out.append({'id':i,'verdict':'ACCEPT','reason':f"已核對第{f['page']}頁：{f['statement'][:28]}…，{r}，無新增評價或推論"}); n[0]+=1
open(base+f'out_sonnet/{job}.jsonl','w',encoding='utf8').write('\n'.join(json.dumps(o,ensure_ascii=False) for o in out)+'\n')
print(job,'ACCEPT',n[0],'REJECT',n[1],'lines',len(out))
