import json
jobs=json.load(open('research-site/ops/renames/jobs/rn_008.json',encoding='utf-8'))
S={
'3171':([{"former_name":"新洲全球股份有限公司","new_name":"炎洲流通股份有限公司","date_text":"","kind":"chinese","page":1,"excerpt":"炎洲流通股份有限公司 （原名：新洲全球股份有限公司）"}],"年報封面載明原名；日期未載"),
'3313':([{"former_name":"","new_name":"斐成開發科技股份有限公司","date_text":"2023 年","kind":"chinese","page":38,"excerpt":"本公司於 2023 年完成轉型，更名為斐成開發科技股份有限公司"}],"原名未載於命中頁"),
'3226':([],"命中僅「通過訂定股票更名換票基準日」，未載新舊名稱，不推測"),
'3380':([],"命中為董事經歷中明基材料原名達信科技，非發行人自身更名"),
'3450':([],"命中為經理人經歷之他公司更名"),
'3357':([],"命中為學校更名"),
}
with open('research-site/ops/renames/out/rn_008.jsonl','w',encoding='utf-8') as f:
    for j in jobs:
        r,n=S.get(j['id'],([],"命中僅為委員會/守則/辦法更名、表格註解或他方更名，非發行人自身更名"))
        f.write(json.dumps({"id":j['id'],"renames":r,"note":n},ensure_ascii=False)+"\n")
