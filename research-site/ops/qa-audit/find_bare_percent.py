"""List live (PASS, not rejected) facts whose statement has a percentage but names no denominator.

  python research-site/ops/qa-audit/find_bare_percent.py   -> research-site/ops/qa-audit/bare_percent.json
"""
import glob
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
FACTS = ROOT / 'research-site/data/company-facts'
DENOM = re.compile(r'占[^，。；%]{0,30}(合計|淨額|總額|營收|營業收入|收入|比重表|銷售地區表|該表|總計|小計|市場|產值|總量|總產量|進貨|銷貨|銷售額|總數|人數)'
                   r'|營業比重|營收比重|比重表|分母|佔[^，。；%]{0,30}(合計|淨額|總額|營收|營業收入|收入|市場|該表)')
last = {}
for line in (FACTS / '_semantic-review.jsonl').read_text(encoding='utf-8').splitlines():
    if line.strip():
        r = json.loads(line)
        last[r['id']] = r['verdict']
out = []
for f in sorted(glob.glob(str(FACTS / '[0-9]*.json'))):
    for x in json.loads(Path(f).read_text(encoding='utf-8'))['facts']:
        if (x.get('verification') or {}).get('status') != 'PASS' or last.get(x['id']) == 'REJECT':
            continue
        s = x['statement']
        if re.search(r'\d\s*%|％', s) and not DENOM.search(s):
            out.append({'id': x['id'], 'reviewer_reason': '統一掃描：百分比未寫明分母（依表補上分母；無法確定分母者 DROP）', 'source': 'bare_percent_sweep'})
(Path(__file__).parent / 'bare_percent.json').write_text(json.dumps(out, ensure_ascii=False, indent=0), encoding='utf-8')
print(len(out))
