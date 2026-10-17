import json,re
items=json.load(open('research-site/ops/qa-audit4/rowrank_in.json',encoding='utf-8'))
out=[]
for it in items:
    s=it['statement']; n=s
    n=re.sub(r'(進貨|銷貨)表排名\d+的',r'\1表所列的',n)
    n=re.sub(r'列名進貨對象第\d+項，','列於主要供應商表，',n)
    n=re.sub(r'列名銷貨對象第\d+項，','列於主要客戶表，',n)
    n=re.sub(r'(表列[^，]*?)第\d+順位為',r'\1包括',n)
    n=re.sub(r'，在年報(主要[^，]*?表)中列於第\d+項',lambda m:'，列於年報'+m.group(1),n)
    n=n.replace('某客戶（A）','某客戶（年報代號A）').replace('某客戶（B）','某客戶（年報代號B）')
    assert n!=s and not re.search(r'第\d|排名',n),(it['id'],n)
    out.append({"id":it['id'],"action":"FIX","new_statement":n,"new_attribution":"","reason":"年報表列序號非排名，移除序號並保留金額、比例與年度"})
with open('research-site/ops/qa-audit4/rowrank_out.jsonl','w',encoding='utf-8') as f:
    for o in out: f.write(json.dumps(o,ensure_ascii=False)+'\n')
for o in out: print(o['new_statement'])
