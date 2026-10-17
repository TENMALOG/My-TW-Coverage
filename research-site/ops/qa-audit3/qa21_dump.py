import json,re,sys
ids=[l.strip() for l in open('research-site/ops/qa-audit3/ids_21.txt') if l.strip()]
want=sys.argv[1].split(',')
for t in want:
    d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
    txt=open(d['source']['text_path'],encoding='utf8').read()
    parts=re.split(r'\[PDF PAGE (\d+)\]',txt)
    pages={int(parts[i]):parts[i+1] for i in range(1,len(parts),2)}
    print('=====',t,d['company'],d['source']['filename'])
    for f in d['facts']:
        if f['id'] in ids:
            print('---',f['id'],f['field'],'|',f['period'],'|',f['attribution'],'| p',f['page'])
            print('STMT:',f['statement'])
            print('EXC:',f['excerpts'])
            if '-v' in sys.argv:
                for p in (f['page'],f['page']+1):
                    print(f'[p{p}]',pages.get(p,'')[:3500])
