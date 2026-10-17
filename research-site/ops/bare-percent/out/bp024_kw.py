import json,sys,io
t,kw=sys.argv[1],sys.argv[2]
f=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
txt=open(f['source']['text_path'],encoding='utf8').read()
o=io.open('research-site/ops/bare-percent/out/bp024_kw.txt','a',encoding='utf8')
o.write('=== %s %s\n'%(t,kw))
n=0;i=-1
while n<2:
    i=txt.find(kw,i+1)
    if i<0:break
    o.write(txt[max(0,i-500):i+500]+'\n-----\n');n+=1
