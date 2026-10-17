import json,re,sys,glob
sys.stdout.reconfigure(encoding='utf8')
D={}
for f in sorted(glob.glob('research-site/ops/codex-review/adj0_dec_*.py')):
    ns={}; exec(open(f,encoding='utf8').read(),ns); D.update(ns['D'])
items=json.load(open('research-site/ops/codex-review/adj_0.json',encoding='utf8'))
out=[];cnt={};warn=0
ALLOWED={"公司年報揭露","公司年報自述（未經獨立驗證的排名或評價）","公司年報引述第三方資料"}
for it in items:
    i=it['id']; act,st,at,rs=D[i]; tk=i.split('-')[0]
    d=json.load(open(f'research-site/data/company-facts/{tk}.json',encoding='utf8'))
    f=next(x for x in d['facts'] if x['id']==i)
    r={"id":i,"action":act}
    if act=='FIX':
        r["new_statement"]=st
        if at: assert at in ALLOWED; r["new_attribution"]=at
        ex=re.sub(r'[\s,]','',' '.join(f['excerpts']))
        for n in re.findall(r'\d[\d,]*\.?\d*',st):
            n2=n.replace(',','').rstrip('.')
            if n2 not in ex: print('NUMWARN',i,n); warn+=1
    r["reason"]=rs
    out.append(r); cnt[act]=cnt.get(act,0)+1
open('research-site/ops/codex-review/adj_out_0.jsonl','w',encoding='utf8').write('\n'.join(json.dumps(r,ensure_ascii=False) for r in out)+'\n')
print(len(out),cnt,warn, set(D)-{x['id'] for x in items})
