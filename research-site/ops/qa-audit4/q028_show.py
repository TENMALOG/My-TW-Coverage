import pickle,re,sys
D=pickle.load(open('research-site/ops/qa-audit4/q028_cache.pkl','rb'))
ids=D['ids'];cache=D['cache']
def page(txt,p):
    m=re.search(r'\[PDF PAGE %d\]\n(.*?)(?=\n\[PDF PAGE \d+\]|\Z)'%p,txt,re.S)
    return m.group(1) if m else ''
a,b=int(sys.argv[1]),int(sys.argv[2])
full=len(sys.argv)>3
for i in ids[a:b]:
    t=i.split('-AR-')[0]
    d,txt=cache[t]
    f=[x for x in d['facts'] if x['id']==i][0]
    print('=====',i,d['company'],f['field'],'|',f['attribution'],'|',f['period'],'p',f['page'])
    print('STMT:',f['statement'])
    print('EXC:',f['excerpts'])
    if full:
        p=f['page']
        print('--PAGE--');print(page(txt,p)[:2500])
