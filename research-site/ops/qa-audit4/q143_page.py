import json,re,sys
t=sys.argv[1]; ps=[int(x) for x in sys.argv[2:]]
d=json.load(open(f'research-site/data/company-facts/{t}.json',encoding='utf8'))
txt=open(d['source']['text_path'],encoding='utf8').read()
parts=re.split(r'\[PDF PAGE (\d+)\]',txt)
pages={int(parts[i]):parts[i+1] for i in range(1,len(parts),2)}
out=open('C:/Users/NEOPEG~1/AppData/Local/Temp/claude/C--Users-Neo-Pegasus-Documents-ChatGPT-078-kaori-sample-artifacts-stock-coverage-audit-20261003-incoming-latest-audit-My-TW-Coverage/1bd92d0e-e36f-4ef8-b701-31d7a9c88c71/scratchpad/q143_page.txt','a',encoding='utf8')
for p in ps:
    out.write(f'#### {t} PAGE {p}\n'+re.sub(r'[ \t]+',' ',pages[p])+'\n')
