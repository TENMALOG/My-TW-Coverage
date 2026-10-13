"""Apply analysis-review fixes to the drafts.

  python research-site/ops/handoff-20261013/tools/apply_anarev.py REVIEW.jsonl [...]

Each review line: {"slug", "sentence" (first 30 chars of the sentence), "problem", "fix"}.
The sentence is located in research-site/data/industry-analysis/{slug}.md (it must match exactly
once); the whole sentence including its trailing 〔ID〕 markers is replaced by `fix`, or removed
when fix == "DELETE". Unmatched lines are reported and left for manual handling. Every change is
logged to research-site/data/industry-analysis/_review-log.jsonl.
"""
import datetime
import json
import re
import sys
from pathlib import Path

D = Path('research-site/data/industry-analysis')
SENT = r'(?:〔[0-9A-Z]{4,6}-AR-[0-9]{2,3}〕)+'
now = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds')
log = (D / '_review-log.jsonl').open('a', encoding='utf-8')
miss = 0
for path in sys.argv[1:]:
    for line in Path(path).read_text(encoding='utf-8').splitlines():
        if not line.strip():
            continue
        r = json.loads(line)
        if r.get('problem') == 'NONE' or not r.get('sentence'):
            continue
        p = D / f'{r["slug"]}.md'
        t = p.read_text(encoding='utf-8')
        hits = [m for m in re.finditer(re.escape(r['sentence']) + r'.*?' + SENT, t, flags=re.S)]
        if len(hits) != 1:
            miss += 1
            print('UNMATCHED', r['slug'], len(hits), r['sentence'])
            continue
        old = hits[0].group(0)
        new = '' if r['fix'].strip() == 'DELETE' else r['fix'].strip()
        p.write_text(t.replace(old, new, 1), encoding='utf-8')
        log.write(json.dumps({'slug': r['slug'], 'old': old, 'new': new, 'problem': r['problem'],
                              'source': Path(path).name, 'at': now}, ensure_ascii=False) + '\n')
print('unmatched', miss)
