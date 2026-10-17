import json
jobs = json.load(open('jobs/rn_019.json', encoding='utf-8'))
R = {
 "8477": ([{"former_name":"創業家兄弟股份有限公司","new_name":"創業家數位股份有限公司","date_text":"114 年 5 月 20 日股東會決議通過，114 年 6 月 26 日完成變更登記","kind":"chinese","page":6,"excerpt":"股東會決議通過，將公司名稱由「創業家兄弟股份有限公司」"}],"本公司自述更名"),
 "8932": ([{"former_name":"宏大拉鍊股份有限公司","new_name":"智通科創股份有限公司","date_text":"","kind":"chinese","page":86,"excerpt":"(原名：宏大拉鍊股份有限公司)"}],"原名僅見於末頁封底資訊，無日期"),
 "8442": ([{"former_name":"","new_name":"WW HOLDING INC.","date_text":"2014.05","kind":"english","page":13,"excerpt":"2014.05 更名為 WW HOLDING INC."}],"集團沿革載2014.05更名為WW HOLDING INC.，未載原名；2001.02 展盛皮具更名為子公司事項，未收"),
 "8472": ([{"former_name":"","new_name":"","date_text":"","kind":"chinese","page":51,"excerpt":"5. 變更公司名稱案"}],"董事會議案載「變更公司名稱案」，報告內未載新舊名稱與日期（報告內仍稱夠麻吉；legal_name 為納維康生技，疑為更名後名稱，但頁面未載）"),
 "8455": ([],"1991年更名為ダイトーエムイー為日本營運子公司（大藤電機）事項，非發行人（2014年設立之開曼控股公司）；其餘為守則、供應商更名"),
 "8437": ([],"僅為間接子公司更名（珠海美地等）"),
 "8916": ([],"僅為委員會、子公司（光隆羽絨制品）更名"),
 "8462": ([],"亞力山大健康休閒俱樂部更名為所述品牌/公司沿革，非發行人柏文本身"),
 "8936": ([],"僅為海水淡化廠設施名稱變更"),
}
with open('out/rn_019.jsonl','w',encoding='utf-8') as f:
    for j in jobs:
        r, n = R.get(j['id'], ([], "命中僅為委員會、守則、報告書、文件或酬金級距欄位等更名，非發行人更名"))
        f.write(json.dumps({"id":j['id'],"renames":r,"note":n}, ensure_ascii=False)+"\n")
