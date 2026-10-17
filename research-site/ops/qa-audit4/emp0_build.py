import json,re,sys
sys.path.insert(0,'research-site/ops/qa-audit4')
from emp0_dec4 import D
inp=json.load(open('research-site/ops/qa-audit4/emp_in_0.json',encoding='utf8'))
out=[];bad=[]
def nums(s): return set(re.findall(r'\d[\d,\.]*',s))
for it in inp:
    i=it['id']
    if i not in D: bad.append(('missing',i)); continue
    a,st,r=D[i]
    t=i.split('-AR-')[0]
    f=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
    x=[y for y in f['facts'] if y['id']==i][0]
    if a=='FIX':
        ex=' '.join(x['excerpts']).replace(',','')+' '+' '.join(x['excerpts']).replace(' ','')
        for n in nums(st.replace(',','')):
            n=n.rstrip('.')
            if n and n not in ex and n not in x['statement'].replace(',',''): bad.append(('num',i,n))
    rec={"id":i,"action":a,"new_statement":st if a=='FIX' else "","new_attribution":"","reason":r}
    out.append(rec)
extra=set(D)-{it['id'] for it in inp}
print(len(out),'extra',extra,'bad',bad)
if not bad:
    with open('research-site/ops/qa-audit4/emp_out_0.jsonl','w',encoding='utf8') as fh:
        for r in out: fh.write(json.dumps(r,ensure_ascii=False)+'\n')
    from collections import Counter; print(Counter(r['action'] for r in out))
