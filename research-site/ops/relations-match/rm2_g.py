import csv,sys,json,os,re
rows=list(csv.DictReader(open('catalog/release-scope-companies.csv',encoding='utf-8-sig')))
names=sys.argv[1:]
for n in names:
    h=[r['ticker']+':'+r['company'] for r in rows if n in r['company'] or r['company'] in n]
    print(n,'->',h)
