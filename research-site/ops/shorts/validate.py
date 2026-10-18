"""Validate Short scripts against the facts they cite; write the storyboards the stage renders.

  python research-site/ops/shorts/validate.py scripts/*.jsonl

For each script line: every cited fact id must belong to the company's base file; every number in a text
or item must occur in the cited facts' statements (comma-insensitive); percentages in mix/regions must sum
to at most 101. A failing field is dropped (not the whole Short) and reported. Writes storyboard/{ticker}.json
(base data + accepted script fields) and prints a summary.
"""
import glob
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
NUM = re.compile(r'\d[\d,]*(?:\.\d+)?')
PERSON = re.compile(r'[一-鿿]{2,3}(先生|女士|小姐)|[一-鿿][OＯ○〇][一-鿿]')


def nums(s):
    return {m.group(0).replace(',', '') for m in NUM.finditer(s or '')}


def supported(text_nums, facts, ids):
    pool = ''.join(facts[i]['statement'] for i in ids if i in facts).replace(',', '')
    pool_nums = nums(pool)
    return [n for n in text_nums if n not in pool_nums and n not in pool]


def check(field, obj, facts):
    ids = obj.get('facts') or []
    if not ids or any(i not in facts for i in ids):
        return f'{field}: unknown or missing fact ids {ids}'
    texts = []
    if 'text' in obj:
        texts.append(obj['text'])
    texts += obj.get('lines') or []
    for it in obj.get('items') or []:
        texts.append(f'{it[0]} {it[1]}')
    if obj.get('year'):
        texts.append(str(obj['year']))
    bad = supported(set().union(*[nums(t) for t in texts]) if texts else set(), facts, ids)
    if field in ('mix', 'regions'):
        bad = [b for b in bad if b != str(obj.get('year'))] if any(str(obj.get('year')) in facts[i]['period'] for i in ids) else bad
    if bad:
        return f'{field}: numbers not in cited facts {bad}'
    if any(PERSON.search(t) for t in texts):
        return f'{field}: natural-person name'
    if field in ('mix', 'regions'):
        tot = sum(float(it[1]) for it in obj['items'])
        if tot > 101 or not 2 <= len(obj['items']) <= 6:
            return f'{field}: items sum {tot} / count {len(obj["items"])}'
    return None


def main(paths):
    out = HERE / 'storyboard'
    out.mkdir(exist_ok=True)
    ok = dropped = 0
    for p in paths:
        for line in Path(p).read_text(encoding='utf-8').splitlines():
            if not line.strip():
                continue
            sc = json.loads(line)
            base = json.loads((HERE / 'base' / f"{sc['ticker']}.json").read_text(encoding='utf-8'))
            facts = {f['id']: f for f in base['facts']}
            sb = {k: v for k, v in base.items() if k != 'facts'}
            notes = []
            for field in ('hook', 'what', 'mix', 'regions'):
                obj = sc.get(field)
                if not obj:
                    continue
                err = check(field, obj, facts)
                if err:
                    notes.append(err)
                    dropped += 1
                else:
                    sb[field] = obj
            sb['cards'] = []
            for c in sc.get('cards') or []:
                err = check('card', c, facts)
                if err:
                    notes.append(err)
                    dropped += 1
                else:
                    if any(facts[i].get('attribution', '').startswith('公司年報自述') for i in c['facts']):
                        c['self'] = True
                    sb['cards'].append(c)
            sb['tags'] = [t for t in sc.get('tags') or [] if not NUM.search(t)][:3]
            sb['notes'] = notes
            (out / f"{sc['ticker']}.json").write_text(json.dumps(sb, ensure_ascii=False, indent=1), encoding='utf-8')
            ok += 1
            if notes:
                print(sc['ticker'], '; '.join(notes))
    print(f'storyboards {ok}; fields dropped {dropped}')


if __name__ == '__main__':
    main([p for a in sys.argv[1:] for p in glob.glob(a)])
