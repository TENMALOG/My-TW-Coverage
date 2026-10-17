import json,sys,re
ids=[l.strip() for l in open('ids_128.txt') if l.strip()]
want=sys.argv[1]
for i in ids:
    t=i.split('-AR-')[0]
    if t!=want: continue
    d=json.load(open(f'../../data/company-facts/{t}.json',encoding='utf8'))
    txt=open('../../../'+d['source']['text_path'],encoding='utf8').read()
    pages=re.split(r'\[PDF PAGE (\d+)\]',txt)
    pm={int(pages[k]):pages[k+1] for k in range(1,len(pages),2)}
    f=[x for x in d['facts'] if x['id']==i][0]
    print('=====',i,f['field'],'|',f.get('period'),'| p',f['page'],'|',f['attribution'])
    print('STMT:',f['statement'])
    for e in f['excerpts']:print('  EX:',e)
    print('--- page text')
