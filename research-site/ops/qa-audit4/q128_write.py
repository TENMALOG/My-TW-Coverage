import json
rej={
'5356-AR-01':'所營業務範圍被縮窄：年報A類含NAS組裝、警用密錄器全部件生產及組裝等，不只電路板打件，僅以「電路板打件」概括電子及光電產品，範圍被縮小',
'5381-AR-16':'「台電需求仍維持在高檔水準」為公司展望／自我評價，卻以「公司年報揭露」為歸屬，應標示為公司年報自述（未經獨立驗證的排名或評價）',
}
ids=[l.strip() for l in open('ids_128.txt') if l.strip()]
with open('out_128.jsonl','w',encoding='utf8') as f:
    for i in ids:
        if i in rej: o={'id':i,'verdict':'REJECT','reason':rej[i]}
        else: o={'id':i,'verdict':'ACCEPT','reason':'數字、年度、欄位與引用頁相符，範圍與歸屬無誤'}
        f.write(json.dumps(o,ensure_ascii=False)+'\n')
print(len(ids))
