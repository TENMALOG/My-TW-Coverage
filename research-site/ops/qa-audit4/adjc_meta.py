import json
for t in ["6614","6640","6668","6671","9938","9962"]:
    d=json.load(open(f"data/company-facts/{t}.json",encoding="utf-8"))
    print(t,[ (k,str(v)[:300]) for k,v in d.items() if k!="facts"])
