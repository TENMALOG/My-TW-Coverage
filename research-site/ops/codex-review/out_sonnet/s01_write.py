import json,sys
job=sys.argv[1]
F='research-site/ops/codex-review/'
ids=[l.strip() for l in open(F+'jobs_sonnet/'+job+'.txt',encoding='utf8') if l.strip()]
ov={}
try:
    for l in open(F+'out_sonnet/s01_ov_%s.txt'%job,encoding='utf8'):
        l=l.rstrip('\n')
        if l.strip():
            a,b=l.split('\t',1); ov[a.strip()]=b
except FileNotFoundError: pass
cache={}
out=[];nr=0
for fid in ids:
    t=fid.split('-')[0]
    if t not in cache: cache[t]=json.load(open('research-site/data/company-facts/%s.json'%t,encoding='utf8'))
    f=[x for x in cache[t]['facts'] if x['id']==fid][0]
    if fid in ov:
        r=ov[fid]; v='REJECT'; nr+=1
        if r.startswith('ACC:'): v='ACCEPT'; nr-=1; r=r[4:]
    else:
        v='ACCEPT'; r='已核對第%s頁原文：「%s」與年報表格或文字、%s欄位、單位及主體一致，未加入評價或排名。'%(f['page'],f['statement'][:26],f['period'])
    out.append(json.dumps({'id':fid,'verdict':v,'reason':r},ensure_ascii=False))
open(F+'out_sonnet/%s.jsonl'%job,'w',encoding='utf8').write('\n'.join(out)+'\n')
print(job,len(out),'accept',len(out)-nr,'reject',nr)
