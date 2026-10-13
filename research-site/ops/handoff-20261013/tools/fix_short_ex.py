"""Merge a too-short excerpt (<4 chars) with the next excerpt when they are adjacent in the source page text; else drop it."""
import json, re, sys, datetime
D = 'research-site/data/company-facts'
now = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds')
logs = []
for t in sys.argv[1:]:
    p = f'{D}/{t}.json'
    d = json.load(open(p, encoding='utf-8'))
    text = open(d['source']['text_path'], encoding='utf-8').read()
    for f in d['facts']:
        ex = f['excerpts']
        if not any(len(e) < 4 for e in ex):
            continue
        old = list(ex); new = []
        i = 0
        while i < len(ex):
            e = ex[i]
            if len(e) < 4 and i + 1 < len(ex):
                m = re.search(re.escape(e) + r'\s*' + re.escape(ex[i + 1]), text)
                if m:
                    new.append(m.group(0)); i += 2; continue
            if len(e) >= 4:
                new.append(e)
            i += 1
        f['excerpts'] = new
        logs.append({'ticker': t, 'id': f['id'], 'field': 'excerpts', 'old': old, 'new': new,
                     'reason': '引文少於4字，與相鄰引文合併或刪除', 'at': now})
        print(f['id'], new)
    open(p, 'w', encoding='utf-8').write(json.dumps(d, ensure_ascii=False, indent=1) + '\n')
with open(f'{D}/_manual-fixes.jsonl', 'a', encoding='utf-8') as fh:
    for r in logs:
        fh.write(json.dumps(r, ensure_ascii=False) + '\n')
