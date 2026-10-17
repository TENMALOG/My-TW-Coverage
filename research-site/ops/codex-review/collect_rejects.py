"""Collect REJECT verdicts from Codex (out/) and Sonnet (out_sonnet/) second-pass reviews into rejects_all.json."""
import collections
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent


def cat(reason: str) -> str:
    rules = [('denominator', r'分母|占比|占X|占 X'), ('rank', r'排名|名次|項次'), ('employees_scope', r'員工'),
             ('unit', r'幣別|單位'), ('person', r'人名|姓名'), ('other_row', r'「其他」'),
             ('conflict', r'矛盾|不一致|衝突|不符'), ('year', r'年度|年份|期間')]
    for name, pat in rules:
        if re.search(pat, reason):
            return name
    return 'misc'


rej, acc = [], 0
for src, folder in (('codex', 'out'), ('sonnet', 'out_sonnet')):
    for f in sorted((HERE / folder).glob('cr*.jsonl')):
        for line in f.read_text(encoding='utf-8').splitlines():
            if not line.strip():
                continue
            r = json.loads(line)
            if str(r.get('verdict', '')).startswith('REJECT'):
                rej.append({**r, 'src': src, 'job': f.stem, 'cat': cat(r.get('reason', ''))})
            else:
                acc += 1
print('accept', acc, 'reject', len(rej), dict(collections.Counter(r['src'] for r in rej)))
print(dict(collections.Counter(r['cat'] for r in rej)))
(HERE / 'rejects_all.json').write_text(json.dumps(rej, ensure_ascii=False, indent=0), encoding='utf-8')
