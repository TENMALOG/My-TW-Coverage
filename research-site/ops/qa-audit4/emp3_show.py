import json, re, sys
sys.stdout.reconfigure(encoding='utf-8')
R='./'
for fid in sys.argv[2:]:
    tk=fid.split('-')[0]
    d=json.load(open(R+f'research-site/data/company-facts/{tk}.json',encoding='utf-8'))
    f=[x for x in d['facts'] if x['id']==fid][0]
    s=open(R+d['source']['text_path'],encoding='utf-8').read()
    m=re.search(r'\[PDF PAGE %d\]\n(.*?)(?=\n\[PDF PAGE \d+\]|\Z)'%f['page'],s,re.S)
    t=m.group(1)
    n=int(sys.argv[1])
    ex=f['excerpts'][-1]
    nums=re.findall(r'\d[\d,\.]*',ex)
    i=t.find(nums[0]) if nums else 0
    print('==',fid,f['statement'],f['excerpts'],'page',f['page'])
    print(re.sub(r'\n+','|',t[max(0,i-n):i+n//2]))
