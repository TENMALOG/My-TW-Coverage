import json,sys,re,os
os.chdir(os.path.dirname(os.path.abspath(__file__))+'/../../..')
root='..'
for fid in sys.argv[1:]:
    t=fid.split('-')[0]
    c=json.load(open(f'data/company-facts/{t}.json',encoding='utf8'))
    f=[y for y in c['facts'] if y['id']==fid][0]
    p=os.path.join(root,c['source']['text_path'])
    txt=open(p,encoding='utf8').read()
    # pages separated by form feed?
    pages=txt.split('\f')
    print('=====',fid,f['page'],len(pages))
    pg=f['page']
    s=pages[pg-1] if len(pages)>pg else txt[:0]
    print(s[:2500])
