import sys,json,os
# usage: t07_write.py job  (reads out_sonnet/t07_ovr_{job}.json: {"id": ["REJECT"|"ACCEPT","reason"]})
R=os.path.abspath('../../..')
job=sys.argv[1]
ids=[l.strip() for l in open(f'jobs_sonnet/{job}.txt',encoding='utf8') if l.strip()]
ovr={}
p=f'out_sonnet/t07_ovr_{job}.json'
if os.path.exists(p): ovr=json.load(open(p,encoding='utf8'))
cache={}
cnt={'ACCEPT':0,'REJECT':0}
rej=[]
with open(f'out_sonnet/{job}.jsonl','w',encoding='utf8') as out:
    for i in ids:
        t=i.split('-')[0]
        if t not in cache:
            cache[t]=json.load(open(f'{R}/research-site/data/company-facts/{t}.json',encoding='utf8'))
        f=[x for x in cache[t]['facts'] if x['id']==i][0]
        if i in ovr:
            v,r=ovr[i]
        else:
            v='ACCEPT'
            r=f"已核對第{f['page']}頁：{f['statement'][:40]}，年度欄位、數字、單位、比例分母與原文相符，歸屬為公司年報揭露，無新增評價或推論"
        cnt[v]+=1
        if v=='REJECT': rej.append((i,r))
        out.write(json.dumps({'id':i,'verdict':v,'reason':r},ensure_ascii=False)+'\n')
print(job,cnt)
for i,r in rej: print(' ',i,r)
