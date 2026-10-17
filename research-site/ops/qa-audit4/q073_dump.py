import json,re,sys
root='../../../'
ids=[l.strip() for l in open('ids_073.txt') if l.strip()]
want=sys.argv[1]
cache={}
for i in ids:
    t=i.split('-AR-')[0]
    if t!=want: continue
    d=json.load(open(f'../../data/company-facts/{t}.json',encoding='utf8'))
    f=[x for x in d['facts'] if x['id']==i][0]
    txt=open(root+d['source']['text_path'],encoding='utf8').read()
    pages=re.split(r'\[PDF PAGE (\d+)\]',txt)
    pm={int(pages[k]):pages[k+1] for k in range(1,len(pages),2)}
    print('=====',i,f['field'],f['period'],f['attribution'],'p',f['page'])
    print('STMT:',f['statement'])
    print('EXC:',f['excerpts'])
    if '-p' in sys.argv: pass
    pp=sys.argv[2:] 
