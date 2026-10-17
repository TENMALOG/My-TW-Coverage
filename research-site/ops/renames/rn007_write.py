import json,sys
sys.path.insert(0,'research-site/scripts/annual')
from slice_annual import page_texts
jobs=json.load(open('research-site/ops/renames/jobs/rn_007.json',encoding='utf-8'))
def R(i,fo,nw,d,k,p,ex): return {"former_name":fo,"new_name":nw,"date_text":d,"kind":k,"page":p,"excerpt":ex}
S={
'2924':{"renames":[R('2924','開曼東凌','開曼群島宏太股份有限公司','民國 111 年 11 月','chinese',10,'開曼群島宏太股份有限公司(原名:開曼東凌)')],
 "note":"沿革頁列於民國111年項下「11 月正式更名為「開曼群島宏太股份有限公司」」；原名僅寫「開曼東凌」(98年設立時為開曼東凌股份有限公司)。date_text為年份標題加月份組合。"},
'3018':{"renames":[R('3018','同開科技工程股份有限公司','隆銘綠能科技工程股份有限公司','民國 111 年','chinese',61,'完成公司更名由同開科技工程股份有限公司改為隆銘綠能科技工程股份有限公')],
 "note":"沿革頁民國111年項下記載；excerpt為原文逐字截取(原文公司二字間有換行空格)。"},
'3085':{"renames":[R('3085','創新新零售股份有限公司','台鋼新零售股份有限公司','','chinese',69,'(原：創新新零售股份有限公司)')],
 "note":"年報封面及第69頁載明「原：創新新零售股份有限公司」；更名日期未於年報明載(第46頁僅有114/06/23董事會訂定更名換發股票基準日案)，故date_text留空。"},
'3128':{"renames":[R('3128','','昇銳智慧科技股份有限公司','114.7.11','chinese',71,'訂定本公司更名「換發有價證券作業計畫書」案')],
 "note":"年報僅記載董事會決議更名換發有價證券，未寫明原名及新名；新名取自年報目錄/封面之公司名；經理人學歷出現「昇銳電子(股)公司」但未明言為原名，故former_name留空不猜。date_text取自該董事會日期114.7.11。"},
}
out=[]
for j in jobs:
    r=S.get(j['id'],{"renames":[],"note":"命中僅為委員會、守則、辦法、欄位名稱、基金會、子公司/投資事業/關係人/董監經理人等更名，非發行公司本身更名。"})
    for x in r['renames']:
        t=page_texts(open(json.load(open(f"research-site/data/company-facts/{j['id']}.json",encoding='utf-8'))['source']['text_path'],encoding='utf-8').read())[x['page']]
        assert x['excerpt'] in t,(j['id'],x['excerpt'])
    out.append({"id":j['id'],**r})
with open('research-site/ops/renames/out/rn_007.jsonl','w',encoding='utf-8') as o:
    for r in out:o.write(json.dumps(r,ensure_ascii=False)+'\n')
print(len(out))
