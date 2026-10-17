import json,re
d=json.load(open('research-site/ops/bare-percent/jobs_sonnet/bp026.json',encoding='utf8'))
facts={}
def getf(i):
    t=i.split('-')[0]
    if t not in facts: facts[t]={f['id']:f for f in json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))['facts']}
    return facts[t][i]
REV='全年度營業收入合計'; REG='銷售地區表合計'; SAL='全年度銷售金額合計'; PRD='該產品別表合計'
M={}
def s(den,ids):
    for i in ids.split(): M['%s-AR-%s'%tuple(i.split(':'))]=den if False else den
def add(den,pairs):
    for p in pairs.split():
        t,n=p.split(':')
        for x in n.split(','): M[f'{t}-AR-{x}']=den
add('營業收入淨額合計','6658:01,02,03,04 6682:01,02,03 6691:03 6697:02,03 6728:02,03 6743:02,03 6648:07')
add(REG,'6658:08,09 6682:09,10 6683:07,08,09 6715:08,09,10,11 6719:07,08 6720:07,09 6732:06,07 6737:07,08,09,10 6674:05,06 6669:04,05,06,07,08')
add(SAL,'6668:07,08,09 6673:06,07,08 6679:111,112,113 6680:04,05,06 6693:09,10,11 6695:06,07')
add('營業收入合計','6669:03 6673:03,04 6683:01,02 6708:02,03,04,05,06')
add('主要產品表合計','6715:03,04,05,06 6732:04')
add('產品別銷售金額合計','6679:103,104,105')
M['6648-AR-07']='該表銷售金額合計'; M['6668-AR-02']=M['6668-AR-03']='產品別銷售金額合計'
M['6664-AR-09']='該市場銷售值合計'; M['6664-AR-10']='該項目市場銷售值'
pat=re.compile(r'(?<=，)(比重為|表列比[重率]為|營收比率為|占銷售比率|占比|比重|比率|占)([\d.]+%)')
out=[]
for it in d:
    i=it['id']; f=getf(i)
    if i in M:
        st=f['statement']
        if i.startswith('6664'):
            new=re.sub(r'占比([\d.]+%)',lambda m:f'占{M[i]}之{m.group(1)}',st,1)
        else:
            new=pat.sub(lambda m:f'占{M[i]}之{m.group(2)}',st,1)
        if new==st: print('NOCHANGE',i,st)
        for n in re.findall(r'\d[\d,.]*',new):
            if n not in ' '.join(f['excerpts']).replace('\n',' ') and n not in ('114',): print('NUM?',i,n)
        out.append({"id":i,"action":"FIX","new_statement":new,"reason":"百分比原未寫明分母，依表格補上占比對象，未新增數字"})
    else:
        out.append({"id":i,"action":"KEEP","reason":"為成長率、持股比例、已載明範圍之市占率或門檻，分母已明確"})
with open('research-site/ops/bare-percent/out/bp026.jsonl','w',encoding='utf8') as w:
    for o in out: w.write(json.dumps(o,ensure_ascii=False)+'\n')
from collections import Counter
print(Counter(o['action'] for o in out),len(out))
for o in out:
    if o['action']=='FIX': print(o['id'],o['new_statement'])
