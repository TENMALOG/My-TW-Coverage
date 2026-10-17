import json, re, sys
sys.path.insert(0,'research-site/ops/qa-audit4')
ids=sys.argv[1:]
for i in ids:
    t=i.split('-AR-')[0]
    d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
    txt=open(d['source']['text_path'],encoding='utf8').read()
    parts=re.split(r'\[PDF PAGE (\d+)\]',txt)
    pages={int(parts[k]):parts[k+1] for k in range(1,len(parts),2)}
    f=next(x for x in d['facts'] if x['id']==i)
    print('='*60,i,f['statement'])
    n=f['page']
    lines=(pages.get(n,'')+'\n'+pages.get(n+1,'')).split('\n')
    # key: numbers in statement
    nums=re.findall(r'\d[\d,\.]*\d',f['statement'])
    nums=[x for x in nums if len(x)>=3] or nums
    hit=set()
    for idx,l in enumerate(lines):
        ll=re.sub(r'\s+','',l)
        if any(re.sub(r'\s+','',x) in ll for x in nums[:3]):
            hit.add(idx)
    for idx in sorted(hit)[:1]:
        print('\n'.join(re.sub(r'[ \t]+',' ',x) for x in lines[max(0,idx-4):idx+2]))
        print('..')
    if not hit: print('NO NUMERIC HIT')
