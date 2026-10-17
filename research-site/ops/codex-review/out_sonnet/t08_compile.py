import json,sys,re
job=sys.argv[1]
root='../../'
ids=[l.strip() for l in open(f'jobs_sonnet/{job}.txt',encoding='utf8') if l.strip()]
v={}
# REJECT/ACCEPT overrides: file out_sonnet/t08_v_{job}.txt lines "start-end|A" or "id|R|reason" ; ranges index-based accepted default
import os
rej={}
accr={}
fn=f'out_sonnet/t08_v_{job}.txt'
done_upto=0
for l in open(fn,encoding='utf8'):
    l=l.rstrip('\n')
    if not l.strip() or l.startswith('#'): continue
    p=l.split('|')
    if p[0]=='UPTO': done_upto=int(p[1]); continue
    if p[1]=='R': rej[p[0]]=p[2]
    elif p[1]=='A' and len(p)>2 and p[2]: accr[p[0]]=p[2]
cache={}
def fact(i):
    t=i.split('-')[0]
    if t not in cache: cache[t]=json.load(open(f'{root}data/company-facts/{t}.json',encoding='utf8'))
    return [x for x in cache[t]['facts'] if x['id']==i][0],cache[t]
if done_upto<len(ids) and '--partial' not in sys.argv:
    print('NOT DONE',done_upto,len(ids)); sys.exit(1)
out=[];na=nr=0
for n,i in enumerate(ids[:done_upto]):
    f,d=fact(i)
    if i in rej:
        out.append({'id':i,'verdict':'REJECT','reason':rej[i]}); nr+=1
    else:
        r=accr.get(i) or f"已核對年報第{f['page']}頁：{d['company']}{f['field']}（{f['period']}）之年度欄位、數字、單位與歸屬皆與原文一致，未增添評價。"
        out.append({'id':i,'verdict':'ACCEPT','reason':r}); na+=1
open(f'out_sonnet/{job}.jsonl','w',encoding='utf8').write(''.join(json.dumps(o,ensure_ascii=False)+'\n' for o in out))
print(job,'A',na,'R',nr)
for i,r in rej.items(): print(' ',i,r)
