import json,sys,re
sys.stdout.reconfigure(encoding='utf8')
for fid in sys.argv[1:]:
    t=fid.split('-')[0]
    d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
    f=[x for x in d['facts'] if x['id']==fid][0]
    txt=open(d['source']['text_path'],encoding='utf8').read()
    m=re.search(r'\[PDF PAGE %d\]\n(.*?)(?=\[PDF PAGE %d\])'%(f['page'],f['page']+1),txt,re.S)
    p=re.sub(r'[ \t]+',' ',m.group(1)) if m else ''
    num=[e for e in f['excerpts'] if re.search(r'\d{3}',e)]
    k=(num[0] if num else f['excerpts'][0]).split()[1:3]
    k=(num[0] if num else f['excerpts'][0]).replace(' ','')[:6]
    ps=p.replace(' ','')
    j=ps.find(k)
    print('###',fid,f['page'])
    print(ps[max(0,j-700):j+300] if j>=0 else 'NOTFOUND '+ps[:300])
