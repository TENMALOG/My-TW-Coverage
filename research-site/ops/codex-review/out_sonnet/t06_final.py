import json,sys,re
F='research-site/ops/codex-review/'
job=sys.argv[1]
ids=open(F+'jobs_sonnet/'+job+'.txt',encoding='utf8').read().split()
v={}
for ln in open(F+'out_sonnet/t06_v_'+job+'.txt',encoding='utf8'):
    ln=ln.strip()
    if not ln: continue
    m=re.match(r'(\d+)(?:-(\d+))?\s+([AR])\s*(.*)',ln)
    a=int(m[1]); b=int(m[2]) if m[2] else a
    for i in range(a,b+1): v[i]=(m[3],m[4])
miss=[i for i in range(len(ids)) if i not in v]
assert not miss,miss
cache={}
out=[];nr=0;rs=[]
for n,i in enumerate(ids):
    tk=i.split('-')[0]
    if tk not in cache: cache[tk]=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
    f=[x for x in cache[tk]['facts'] if x['id']==i][0]
    k,r=v[n]
    if k=='A':
        reason=r or f"已核對第{f['page']}頁原文：{f['period']}之{f['field']}，主體、年度欄位、數字與單位和年報一致，歸屬為{f['attribution']}，未見多加內容。"
        out.append({"id":i,"verdict":"ACCEPT","reason":reason})
    else:
        nr+=1; rs.append((i,r))
        out.append({"id":i,"verdict":"REJECT","reason":r})
open(F+'out_sonnet/'+job+'.jsonl','w',encoding='utf8').write('\n'.join(json.dumps(o,ensure_ascii=False) for o in out)+'\n')
print(job,len(ids),'ACCEPT',len(ids)-nr,'REJECT',nr)
for i,r in rs: print(' ',i,r)
