import json,sys
for t,i in [("6887","16"),("6614","01"),("6614","04"),("6614","11"),("6640","06"),("6668","19"),("6671","02"),("9938","10"),("9962","03")]:
    d=json.load(open(f"data/company-facts/{t}.json",encoding="utf-8"))
    fs=d.get("facts") if isinstance(d,dict) else d
    for f in fs:
        if f.get("id")==f"{t}-AR-{i}":
            print("=====",f["id"]); print(json.dumps(f,ensure_ascii=False,indent=1))
