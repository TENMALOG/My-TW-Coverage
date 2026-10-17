import json,collections
d=json.load(open('ops/relations-match/in_2.json',encoding='utf-8'))
M={103:'2379',104:'2317',106:'1316',189:'3037',234:'3702',248:'1301',130:'2330',227:'3036',286:'6988'}
roles={106:'parent',234:'parent'}
B=set([0,9,10,11,12,13,14,19,20,21,32,48,49,57,61,62,74,75,76,78,79,80,82,83,87,88,89,98,99,100,101,102,105,111,117,125+1,127,128,138,139,140,141,142,143,144,145,146,147,159,160,161,162,163,164,180,181,184,185,186,187,190,191,192,194,195,196,197,198,204,208,209,212,213,214,215,216,217,218,219,229+0,230,231,232,233,235,236,237,238,244,256,262,263,283,294,318])
B.discard(229)
roles_fix={246:'subsidiary'}
out=[]
cnt=collections.Counter()
for i,x in enumerate(d):
    if i in M:
        v='MATCH';t=M[i];r='名稱與上市公司法定名稱/簡稱相符（臺/台、股份有限公司差異）'
    elif i in B:
        v='BAD_NAME';t=None;r='非可辨識之獨立組織名稱（代號、泛稱、集團、地區、片段、發行人自身或名稱殘缺）'
    else:
        v='NOT_LISTED';t=None;r='真實組織但非本範圍上市公司（外商、民營公司、政府機關、子公司或海外實體）'
    role=roles.get(i,roles_fix.get(i,x['role']))
    cnt[v]+=1
    out.append(json.dumps({"relation_id":x['relation_id'],"fact_id":x['fact_id'],"counterparty":x['counterparty'],"verdict":v,"counterparty_ticker":t,"role":role,"reason":r},ensure_ascii=False))
open('ops/relations-match/out_2.jsonl','w',encoding='utf-8',newline='\n').write('\n'.join(out)+'\n')
print(len(out),cnt)
