import json,sys,io,re
R='research-site/'
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
for fid,kw in [a.split(':',1) for a in sys.argv[1:]]:
    t=fid.split('-')[0]
    c=json.load(open(R+'data/company-facts/%s.json'%t,encoding='utf8'))
    f=[x for x in c['facts'] if x['id']==fid][0]
    txt=open(c['source']['text_path'],encoding='utf8').read()
    pages=re.split(r'\[PDF PAGE \d+\]',txt)[1:]
    print('=====',fid,'pages',len(pages))
    for p in (f['page'],f['page']+1):
        s=pages[p-1] if p-1<len(pages) else ''
        for m in re.finditer(kw,s):
            print('--p%d:'%p, s[max(0,m.start()-400):m.end()+400].replace('\n',' | '))
            break
