import json
d=json.load(open('research-site/ops/renames/jobs/rn_020.json',encoding='utf-8'))
notes={
'9925':'僅委員會更名','9930':'僅內部委員會更名','9933':'僅委員會、守則、轉投資公司(東南實業、GCEH、BKRF)更名',
'9934':'僅子公司東莞成霖更名','9937':'僅守則、委員會及外部評鑑更名','9939':'僅委員會更名','9940':'僅委員會、守則及轉投資公司更名',
'9941':'僅被投資公司觔斗雲聯網科技更名；其餘為評鑑用語','9945':'命中僅為酬金表欄位名稱修改','9946':'僅提名委員會更名',
'9957':'命中僅為酬金表欄位名稱修改','9958':'僅子公司PT Century Indonesia Wind Energy更名','9960':'命中僅為酬金表欄位名稱修改','9962':'命中僅為酬金表欄位名稱修改'}
with open('research-site/ops/renames/out/rn_020.jsonl','w',encoding='utf-8') as f:
    for e in d:
        f.write(json.dumps({"id":e['ticker'],"renames":[],"note":notes[e['ticker']]},ensure_ascii=False)+"\n")
