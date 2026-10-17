import json
d=json.load(open('ops/relations-match/in_5.json',encoding='utf-8'))
M={ # idx: (ticker, role, reason)
77:('8249','customer','陳述點名菱光（關係人），對應菱光科技，非發行人本身'),
83:None,

127:('2344','customer','華邦對應華邦電子(華邦電)'),
128:('2344','customer','華邦對應華邦電子(華邦電)'),
125:('6173','supplier','電容器供應商信昌，對應信昌電子陶瓷(信昌電)'),
145:('2383','supplier','基板膠片供應商台光，對應台光電子材料'),
146:('6672','supplier','基板膠片供應商騰輝，對應騰輝電子'),
107:('2455','supplier','陳述明載全新光電，對應全新光電科技'),
192:('2317','customer','鴻海精密對應鴻海精密工業'),
193:('2308','customer','台達電子對應台達電子工業'),
194:('4938','customer','陳述點名和碩聯合，對應和碩聯合科技；輸入文字為截斷片段'),
195:('2395','customer','研華科技對應研華股份有限公司(研華)'),
168:('2308','supplier','台達電子對應台達電子工業'),
214:('1301','supplier','台灣塑膠對應台灣塑膠工業(台塑)'),
286:('2002','supplier','中國鋼鐵公司對應中國鋼鐵股份有限公司(中鋼)'),
271:('2002','supplier','陳述點名中國鋼鐵(股)公司；輸入文字帶有前綴「象」'),
297:('6505','supplier','台塑石化(股)公司對應台塑石化(台塑化)；與發行人關係為董事大股東，進貨角色為供應商'),
306:('2227','supplier','裕隆日產汽車公司對應裕隆日產汽車股份有限公司(裕日車)'),
95:('6548','subsidiary','長華科技(股)公司對應長華科技股份有限公司(長科)，為發行人長華電材之子公司'),
109:('3047','parent','陳述載明母公司為訊舟科技，對應訊舟科技股份有限公司；角色應為母公司'),
}
BAD={0:0}
bad_idx=set("1 2 6 26 27 28 29 32 33 34 35 36 51 52 55 56 57 58 60 70 76 84 87 89 90 91 92 100 102 104 105 113 115 116 117 118 119 132 133 135 164 172 173 181 182 183 184 185 186 210 211 212 218 222 252 233 245 253 282 283 284 285 295 300 301 302 308 21 150 78 279 280 135".split())
bad_idx|={26,27,28,29}
bad_idx={int(x) for x in bad_idx}
bad_idx|={74+1-1} if False else set()
# fix: ensure specific indexes
bad_idx={1,2,5,6,26,27,28,29,32,33,34,35,36,51,52,55,56,57,58,60,70,84,87,89,90,91,92,100,102,103-103+104,105-105+105,113,115,116,117,118,119,132,133,135,150,172,173,181,182,183,184,185,186,210,211,212,218,222,233,252,282,283,284,285,295,300,301,302,308,21,104,105,7-7+7+0,76-76+0}
bad_idx.discard(0)
# remove ones that are NOT bad: 76 (三菱 NOT_LISTED), 7 (睿剛 NOT_LISTED), 135 keep bad(增減變動說明載明), 78 handled below
bad_idx-= {76,7}
bad_idx|={78,81}
bad_idx|={279-279+0}
bad_idx.discard(0)
bad_idx|={105-0}
out=[]
for n,i in enumerate(d):
    if n in M and M[n]:
        t,r,why=M[n];v='MATCH'
    elif n in bad_idx:
        t=None;r=i['role'];v='BAD_NAME';why='非組織名稱：通用詞、截斷片段、代號、或名稱夾帶業務描述'
    else:
        t=None;r=i['role'];v='NOT_LISTED';why='真實機構但不在上市櫃公司清單（外商、民營、政府機關、或子公司/分公司/海外實體）'
    out.append(dict(relation_id=i['relation_id'],fact_id=i['fact_id'],counterparty=i['counterparty'],verdict=v,counterparty_ticker=t,role=r,reason=why))
open('ops/relations-match/out_5.jsonl','w',encoding='utf-8').write(''.join(json.dumps(o,ensure_ascii=False)+'\n' for o in out))
from collections import Counter
print(len(out),Counter(o['verdict'] for o in out))
for n in sorted(bad_idx):print(n,d[n]['counterparty'])
