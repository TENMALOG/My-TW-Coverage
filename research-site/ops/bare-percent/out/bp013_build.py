import json
d=json.load(open('ops/bare-percent/jobs_sonnet/bp013.json',encoding='utf8'))
facts={}
def fact(i):
    t=i.split('-')[0]
    if t not in facts: facts[t]=json.load(open(f'data/company-facts/{t}.json',encoding='utf8'))
    return next(f for f in facts[t]['facts'] if f['id']==i)
REG="占銷售地區表合計"; TAB="占該表合計"
fix={}
for i in "4575-AR-08 4576-AR-08 4576-AR-09 4576-AR-10 4576-AR-11 4729-AR-06 4908-AR-05 4908-AR-06 4908-AR-08 4916-AR-08 4916-AR-09 4924-AR-09 4924-AR-10 4927-AR-04 4935-AR-05 4935-AR-06 4938-AR-06 4938-AR-07 4938-AR-08 4938-AR-09 4939-AR-05 4942-AR-08 4942-AR-09 4952-AR-04 4958-AR-06 4958-AR-07 4960-AR-06 4960-AR-07 4961-AR-108 4961-AR-109 4966-AR-04 4966-AR-05 4967-AR-07 4967-AR-08 4967-AR-09 4967-AR-10 4968-AR-108 4968-AR-109 4968-AR-110 4973-AR-07 4973-AR-08 4973-AR-09 4973-AR-10 4974-AR-04 4976-AR-06 4976-AR-07 4977-AR-08 4977-AR-09 4979-AR-04 4979-AR-05 4980-AR-07 4980-AR-08 4980-AR-09 4980-AR-10 4987-AR-10 4987-AR-11 4987-AR-12 4994-AR-07 4994-AR-08".split(): fix[i]=("rep",REG)
for i in "4576-AR-04 4576-AR-05 4584-AR-03 4584-AR-04 4584-AR-05 4971-AR-01 4971-AR-02 4925-AR-04".split(): fix[i]=("rep",TAB)
fix["4609-AR-01"]=("rep","占該表銷售淨額合計")
fix["4749-AR-01"]=("rep","占該表合計")
fix["4931-AR-01"]=("rep","占該表合計")
fix["4972-AR-01"]=("rep","占該表合計")
fix["4967-AR-11"]=("rep","占銷貨淨額")
fix["4967-AR-12"]=("rep","占銷貨淨額")
fix["4943-AR-05"]=("txt","2025年度主要產品銷售至中國大陸之金額占銷售地區表合計94.56%，2024年度為86.53%（表註：係指銷售開曼群島以外之地區）。")
fix["4960-AR-10"]=("txt","公司於年報自述高質化產品佔比朝40%前進（原文未載明分母）。")
out=[]
for it in d:
    i=it['id']; f=fact(i)
    if i in fix:
        k,v=fix[i]; s=f['statement']
        if k=="rep":
            assert s.endswith("。"),i
            s=s[:-1]+"（"+v+"）。"
        else: s=v
        out.append({"id":i,"action":"FIX","new_statement":s,"reason":"裸百分比補明分母，僅引用excerpts內數字"})
    else:
        out.append({"id":i,"action":"KEEP","reason":"陳述已載明比率基礎（成長率、持股、市佔基礎、占銷貨/進貨淨額或統計母體）"})
open('ops/bare-percent/out/bp013.jsonl','w',encoding='utf8').write("\n".join(json.dumps(o,ensure_ascii=False) for o in out)+"\n")
from collections import Counter;print(len(out),Counter(o['action'] for o in out))
