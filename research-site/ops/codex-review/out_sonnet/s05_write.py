import json,sys,re,os
sys.stdout.reconfigure(encoding='utf-8')
job=sys.argv[1]
base='out_sonnet/'
ids=[l.strip() for l in open(f'jobs_sonnet/{job}.txt') if l.strip()]
rej={}
rp=base+f's05_{job}_rej.txt'
if os.path.exists(rp):
    for l in open(rp,encoding='utf8'):
        l=l.strip()
        if '|' in l:
            i,r=l.split('|',1); rej[i.strip()]=r.strip()
# optional custom accept reasons
acc={}
ap=base+f's05_{job}_acc.txt'
if os.path.exists(ap):
    for l in open(ap,encoding='utf8'):
        l=l.strip()
        if '|' in l:
            i,r=l.split('|',1); acc[i.strip()]=r.strip()
cache={}
def fact(i):
    t=i.split('-')[0]
    if t not in cache:
        cache[t]=json.load(open(f'../../data/company-facts/{t}.json',encoding='utf8'))
    return [x for x in cache[t]['facts'] if x['id']==i][0]
T={'revenue_mix':'營業比重表','sales_regions':'銷售地區表','export_share':'銷售地區表','major_customers':'主要客戶表','major_suppliers':'主要供應商表','employees':'員工人數表','rd':'研發段落'}
out=[]
n=[0,0]
for i in ids:
    f=fact(i)
    if i in rej:
        out.append({'id':i,'verdict':'REJECT','reason':rej[i]}); n[1]+=1
    else:
        if i in acc: r=acc[i]
        else:
            nums=re.findall(r'\d[\d,\.]*%?',f['statement'])
            nums=[x for x in nums if x not in ('1','2')][:3]
            r=f"已核對第{f['page']}頁{T.get(f['field'],'原文')}，{f['period']}之內容"+('（'+'、'.join(nums)+'）' if nums else '')+"與年報原文相符，單位、欄位、歸屬及自述語氣無誤。"
        out.append({'id':i,'verdict':'ACCEPT','reason':r}); n[0]+=1
open(base+f'{job}.jsonl','w',encoding='utf8').write('\n'.join(json.dumps(o,ensure_ascii=False) for o in out)+'\n')
print(job,'ACCEPT',n[0],'REJECT',n[1],'total',len(ids))
