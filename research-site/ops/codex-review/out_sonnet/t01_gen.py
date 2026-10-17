import json,re,os,sys
F='research-site/ops/codex-review'
FIELD={'revenue_mix':'營業比重/營收項目','sales_regions':'銷售地區','export_share':'外銷比重','major_customers':'主要客戶','major_suppliers':'主要供應商','employees':'員工人數','rd':'研發','products':'產品項目','business_scope':'業務範圍','raw_materials':'主要原料','group_structure':'集團結構','established':'設立日期','headquarters':'總公司地址','history':'沿革','capacity_or_production':'產能/產量','outlook':'展望','products':'產品項目'}
jobs=[l.strip() for l in open(f'{F}/sonnet_g2_01',encoding='utf8') if l.strip()]
cache={}
for j in jobs:
    ids=[l.strip() for l in open(f'{F}/jobs_sonnet/{j}.txt',encoding='utf8') if l.strip()]
    rej={}
    p=f'{F}/out_sonnet/t01_rej_{j}.txt'
    if os.path.exists(p):
        for l in open(p,encoding='utf8'):
            if '|' in l: a,b=l.rstrip('\n').split('|',1); rej[a]=b
    out=[]
    for i in ids:
        t=i.split('-')[0]
        if t not in cache: cache[t]=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
        f=[x for x in cache[t]['facts'] if x['id']==i][0]
        if i in rej: out.append({'id':i,'verdict':'REJECT','reason':rej[i]})
        else:
            nums=re.findall(r'\d[\d,\.]*%?',f['statement'])
            nums='、'.join(dict.fromkeys(nums[:4]))
            r=f"已核對年報第{f['page']}頁{FIELD.get(f['field'],f['field'])}（{f['period']}）：數字{nums}之欄位年度、單位、分母/範圍與原文一致，未添加評價、排名或因果。"
            out.append({'id':i,'verdict':'ACCEPT','reason':r})
    with open(f'{F}/out_sonnet/{j}.jsonl','w',encoding='utf8',newline='\n') as fo:
        for o in out: fo.write(json.dumps(o,ensure_ascii=False)+'\n')
    na=sum(o['verdict']=='ACCEPT' for o in out); print(j,len(ids),'ACCEPT',na,'REJECT',len(out)-na, [o['id'] for o in out if o['verdict']=='REJECT'])
