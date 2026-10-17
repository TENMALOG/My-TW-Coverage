import json,sys
sys.stdout.reconfigure(encoding='utf8')
d=json.load(open('../jobs_sonnet/bp017.json',encoding='utf8'))
facts={}
for it in d:
    t=it['id'].split('-')[0]
    if t not in facts: facts[t]={f['id']:f for f in json.load(open(f'../../../data/company-facts/{t}.json',encoding='utf8'))['facts']}
f0=list(facts.values())[0]
k=list(f0.values())[0]
print(list(k.keys()))
for it in d:
    f=facts[it['id'].split('-')[0]][it['id']]
    print('##',it['id'],'|',f.get('statement'),'|',f.get('period'),'|',f.get('attribution'),'| p',f.get('page'))
    for e in f.get('excerpts',[]):
        print('   >',json.dumps(e,ensure_ascii=False)[:400])
