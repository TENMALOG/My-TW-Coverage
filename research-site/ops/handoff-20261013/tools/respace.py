"""Usage: respace.py TICKER ... — restore original whitespace in excerpts that an extractor stripped.
Each excerpt is replaced by the exact source substring (on page or page+1) whose normalized form is
identical; whitespace runs collapse to one space. Content never changes (norm(old) == norm(new))."""
import json, re, sys, unicodedata, datetime
sys.path.insert(0, 'research-site/scripts/annual')
from slice_annual import ROOT, norm, split_pages

D = 'research-site/data/company-facts'
now = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds')
WS = re.compile(r'\s+')
logs = []


def index(seg):
    out, idx = [], []
    for i, c in enumerate(seg):
        n = WS.sub('', unicodedata.normalize('NFKC', c))
        out.append(n)
        idx += [i] * len(n)
    return ''.join(out), idx


for t in sys.argv[1:]:
    p = f'{D}/{t}.json'
    d = json.load(open(p, encoding='utf-8'))
    text = (ROOT / d['source']['text_path']).read_text(encoding='utf-8')
    pages = {n: text[s:e] for n, s, e in split_pages(text)}
    changed = 0
    for f in d['facts']:
        new = []
        for e in f['excerpts']:
            ne = norm(e)
            seg = pages.get(f['page'], '') + '\n' + pages.get(f['page'] + 1, '')
            flat, idx = index(seg)
            k = flat.find(ne)
            if k < 0 or not ne:
                new.append(e)
                continue
            orig = WS.sub(' ', seg[idx[k]:idx[k + len(ne) - 1] + 1]).strip()
            assert norm(orig) == ne, (f['id'], e)
            new.append(orig)
        if new != f['excerpts']:
            logs.append({'ticker': t, 'id': f['id'], 'field': 'excerpts', 'old': f['excerpts'], 'new': new,
                         'reason': '還原原文空白（擷取時被刪除，導致數字黏連）', 'at': now})
            f['excerpts'] = new
            changed += 1
    open(p, 'w', encoding='utf-8').write(json.dumps(d, ensure_ascii=False, indent=1) + '\n')
    print(t, 'facts changed', changed)
with open(f'{D}/_manual-fixes.jsonl', 'a', encoding='utf-8') as fh:
    for r in logs:
        fh.write(json.dumps(r, ensure_ascii=False) + '\n')
