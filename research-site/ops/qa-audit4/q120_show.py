import sys,re
s=open('research-site/ops/qa-audit4/q120_dump2.txt',encoding='utf8').read()
blocks=s.split('='*60+'\n')[1:]
a,b,n=sys.argv[1],sys.argv[2],int(sys.argv[3])
ia=[k for k,x in enumerate(blocks) if x.startswith(a)][0]
ib=[k for k,x in enumerate(blocks) if x.startswith(b)][0]
for x in blocks[ia:ib+1]:
    h,rest=x.split('CTX:',1) if 'CTX:' in x else (x,'')
    rest=re.sub(r'\n\s*\n','\n',rest)
    print('##'+h.strip()+'\nCTX:'+rest[:n]+'\n')
