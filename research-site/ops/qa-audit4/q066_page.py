import sys,re
tk=sys.argv[1]
t=open(f'q066_{tk}_txt.txt',encoding='utf8').read()
parts=re.split(r'\[PDF PAGE (\d+)\]',t)
pg={int(parts[i]):parts[i+1] for i in range(1,len(parts),2)}
for p in sys.argv[2:]:
    p=int(p)
    print('=====PAGE',p)
    print(re.sub(r'\n\s*\n+','\n',pg.get(p,'MISSING')))
