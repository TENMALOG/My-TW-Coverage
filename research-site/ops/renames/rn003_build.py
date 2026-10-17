import json
d = json.load(open('research-site/ops/renames/jobs/rn_003.json', encoding='utf-8'))
notes = {
 '2239': '命中為子公司長春誠泰更名及英文原名敘述，非發行人本身更名',
 '2340': '第82頁載明110年變更公司名稱為「台亞半導體股份有限公司」，但報告未寫出舊名，依規定不臆測，故不記錄',
 '2338': '命中為母公司、子公司及被投資公司更名，非發行人本身',
 '2332': '命中為法人董事及內部委員會更名，非發行人本身',
 '2353': '命中為倚天酷碁(子公司)合併更名及RBA組織更名，非發行人本身',
 '2250': '命中為子公司(馬來西亞、香港 IKKA)原名，非發行人本身',
}
with open('research-site/ops/renames/out/rn_003.jsonl', 'w', encoding='utf-8') as f:
    for e in d:
        n = notes.get(e['id'], '命中皆為委員會、守則、報告書、組織或董事學歷等更名及酬金填表說明，非發行人本身更名')
        f.write(json.dumps({'id': e['id'], 'renames': [], 'note': n}, ensure_ascii=False) + '\n')
