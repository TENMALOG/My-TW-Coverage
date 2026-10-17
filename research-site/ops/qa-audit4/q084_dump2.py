import json, re, sys
ids = [l.strip() for l in open('research-site/ops/qa-audit4/ids_084.txt', encoding='utf8') if l.strip()]
tk = sys.argv[1]
d = json.load(open(f'research-site/data/company-facts/{tk}.json', encoding='utf8'))
txt = open(d['source']['text_path'], encoding='utf8').read()
pages = {int(m.group(1)): m.group(2) for m in re.finditer(r'\[PDF PAGE (\d+)\]\n(.*?)(?=\n\[PDF PAGE \d+\]|\Z)', txt, re.S)}
print(d['company'])
seen = {}
for f in d['facts']:
    if f['id'] not in ids: continue
    print(f"## {f['id']} {f['field']} | {f['period']} | {f['attribution']} | p{f['page']}\nS: {f['statement']}\nE: {f['excerpts']}")
    seen.setdefault(f['page'], f['excerpts'][0][:15] if f['excerpts'] else '')
for p, ex in seen.items():
    pg = pages.get(p, ''); i = pg.find(ex)
    print(f'---- PAGE {p}\n', pg[max(0, i-150):i+900] if i >= 0 else pg[:1200])
