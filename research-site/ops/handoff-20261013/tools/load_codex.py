"""Usage: load_codex.py CODEX_JSON — write each company document to research-site/data/company-facts/ (new files only)."""
import json, os, sys
d = json.load(open(sys.argv[1], encoding='utf-8'))
print('notes:', d.pop('_notes', ''))
for t, doc in d.items():
    p = f'research-site/data/company-facts/{t}.json'
    if os.path.exists(p):
        print(t, 'EXISTS, not overwritten'); continue
    assert doc.get('ticker', t) == t
    open(p, 'w', encoding='utf-8').write(json.dumps(doc, ensure_ascii=False, indent=1) + '\n')
    print(t, doc.get('company'), len(doc['facts']), 'facts')
