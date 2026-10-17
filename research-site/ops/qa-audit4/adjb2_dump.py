import json,sys
d=json.load(open('ops/qa-audit4/adj_in_b2.json',encoding='utf8'))
out=open('ops/qa-audit4/adjb2_dump.txt','w',encoding='utf8')
for x in d:
    t=x['id'].split('-')[0]
    f=json.load(open(f'data/company-facts/{t}.json',encoding='utf8'))
    fl=f if isinstance(f,list) else (f.get('facts') or f.get('items') or f)
    hit=[a for a in fl if a.get('id')==x['id']] if isinstance(fl,list) else []
    out.write('=== '+x['id']+' | '+x['reviewer_reason']+'\n')
    out.write(json.dumps(hit[0] if hit else {'keys':list(f)[:10] if isinstance(f,dict) else None},ensure_ascii=False,indent=1)+'\n')
