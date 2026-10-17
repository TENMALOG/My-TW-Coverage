import json,re,sys
sys.stdout.reconfigure(encoding='utf-8')
items=json.load(open('research-site/ops/qa-audit4/emp_in_3.json',encoding='utf-8'))
SUF='（員工人數表未載明為母公司或合併範圍）'
special={
'6573-AR-04':('FIX','年報公司簡介載明，截至2026年3月底，本公司（開曼虹揚）員工總人數約266人。','簡介明稱本公司（開曼虹揚）；改為載明範圍'),
'6684-AR-18':('KEEP',None,'陳述已載明係安格+強弦範圍'),
'8935-AR-18':('KEEP',None,'陳述已載明為清遠邦泰複合材料有限公司，表內標示相符'),
'8935-AR-19':('KEEP',None,'陳述已載明為越南邦泰責任有限公司，表內標示相符'),
'8046-AR-11':('FIX','114年度員工合計9,874人，年報註載明員工人數包含合併財務報告公司。','表註載明含合併財務報告公司'),
'8046-AR-12':('FIX','截至115年3月31日，員工合計9,818人，年報註載明員工人數包含合併財務報告公司。','表註載明含合併財務報告公司'),
'8299-AR-19':('FIX','114年度員工人數合計為4,913人，年報表註載明採用國際財務報導準則（合併主體）。','表註載明合併主體'),
'8299-AR-20':('FIX','截至115年3月31日止員工人數合計為5,056人，年報表註載明採用國際財務報導準則（合併主體）。','表註載明合併主體'),
}
out=[]
for it in items:
    i=it['id']
    if i in special:
        a,s,r=special[i]
    else:
        st=it['statement']
        s=st
        s=re.sub(r'年報(載明|揭露)公司',lambda m:'年報'+m.group(1),s)
        s=re.sub(r'光隆(?=從業)','',s)
        s=re.sub(r'(?<![本])公司(?=\d|員工|從業)','',s)
        s=s.replace('本公司','').replace('年報114年','年報載明114年').replace('2,662','2662')
        s=re.sub(r'，?公司(?=從業|員工)','',s)
        s=s.replace('公司研發','研發').replace('年報114年','年報載明114年')
        s=s.rstrip('。')+SUF+'。'
        a='FIX'; r='員工人數表未載明範圍，補註並移除隱含母公司範圍之用語'
    o={'id':i,'action':a,'new_attribution':''}
    if s: o['new_statement']=s
    o['reason']=r
    out.append(o)
with open('research-site/ops/qa-audit4/emp_out_3.jsonl','w',encoding='utf-8') as f:
    for o in out: f.write(json.dumps(o,ensure_ascii=False)+'\n')
# validate numbers
for it,o in zip(items,out):
    if o['action']=='FIX':
        d=json.load(open(f"research-site/data/company-facts/{it['id'].split('-')[0]}.json",encoding='utf-8'))
        fct=[x for x in d['facts'] if x['id']==it['id']][0]
        ex=' '.join(fct['excerpts'])
        for n in re.findall(r'\d[\d,]*',o['new_statement']):
            if n not in ex and n not in ex.replace(' ','') : print('NUM?',it['id'],n)
    print(o['action'],it['statement'],'=>',o.get('new_statement'))
print(len(out))
