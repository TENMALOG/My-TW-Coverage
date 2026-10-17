import json,sys,re
root='..'
t,kw,n=sys.argv[1],sys.argv[2],int(sys.argv[3]) if len(sys.argv)>3 else 600
f=json.load(open('data/company-facts/%s.json'%t,encoding='utf8'))
s=open(root+'/'+f['source']['text_path'],encoding='utf8').read()
for m in re.finditer(kw,s):
    print('---',m.start());print(s[max(0,m.start()-n):m.start()+n])
    break
