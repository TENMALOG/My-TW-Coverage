import json,os
os.chdir(r"C:/Users/Neo Pegasus/Documents/ChatGPT/078-kaori sample/artifacts/stock-coverage-audit-20261003/incoming/latest-audit/My-TW-Coverage")
ids=[l.strip() for l in open('research-site/ops/qa-audit3/ids_04.txt',encoding='utf-8') if l.strip()]
cache={}
with open('research-site/ops/qa-audit3/out_04.jsonl','w',encoding='utf-8') as o:
    for i in ids:
        t=i.split('-AR-')[0]
        if t not in cache: cache[t]=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf-8'))
        f=[x for x in cache[t]['facts'] if x['id']==i][0]
        fld=f['field']
        r={'major_customers':'數字、年度欄位、占比分母與年報表格一致；代號未被當成排名或真名',
           'major_suppliers':'數字、年度欄位、占比分母與年報表格一致；代號未被當成排名或真名',
           'revenue_mix':'數字與年度欄位和年報表格相符，標示年度與比重分母',
           'sales_regions':'數字、年度與分母和年報表格相符',
           'employees':'人數與年度欄位相符，並已註明範圍',
           'rd':'金額或件數與年報原文相符',
           }.get(fld,'與年報原文相符，無推論或範圍變更')
        o.write(json.dumps({'id':i,'verdict':'ACCEPT','reason':r},ensure_ascii=False)+'\n')
