import json,re
j=json.load(open('research-site/ops/renames/jobs/rn_013.json',encoding='utf-8'))
for e in j:
    out=[]
    for h in e['hits']:
        for s in h['snippets']:
            if '欄位名稱' in s or '酬金級距' in s: continue
            out.append('  p%d: %s'%(h['page'],s[:300]))
    print('==',e['id'],e['company'],e['legal_name']); print('\n'.join(out))
