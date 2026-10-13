"""Check and render the per-industry analysis sections.

Drafts live in research-site/data/industry-analysis/{slug}.md and cite annual-report facts with
markers like 〔2059-AR-11〕 at the end of every sentence. This script

  * checks every draft: each sentence carries at least one marker; every cited fact exists, passed
    verification, is not rejected by semantic review and belongs to a company of that industry;
    every number in a sentence (except the ticker in 「公司（2059）」) appears in a cited statement;
  * renders chapters/industries/_analysis/{slug}.qmd, turning each marker group into one footnote
    that names the annual report, page and period of every cited fact.

  python research-site/scripts/generic/build_industry_analysis.py [--check-only] [slug ...]

Exit code 1 if any draft fails the check (nothing is rendered for a failing draft).
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from industries import FACTS_DIR, SITE, companies, industry_names  # noqa: E402
from build_company_pages_all import fact_note, semantic_rejects  # noqa: E402

DRAFTS = SITE / 'data/industry-analysis'
OUTDIR = SITE / 'chapters/industries/_analysis'
MARKS = re.compile(r'((?:〔[0-9A-Z]{4,6}-AR-[0-9]{2,3}〕)+)')
ONE = re.compile(r'〔([0-9A-Z]{4,6}-AR-[0-9]{2,3})〕')
NUM = re.compile(r'\d[\d,]*(?:\.\d+)?')
TICKER_PAREN = re.compile(r'（[0-9A-Z]{4,6}）')


def norm_num(s: str) -> str:
    return s.replace(',', '')


def load_industry_facts(folder: str) -> dict[str, tuple[dict, dict]]:
    """fact id -> (company doc, fact) for usable facts of the industry's companies."""
    rejected = semantic_rejects()
    out = {}
    for c in companies():
        if c['industry_folder'] != folder:
            continue
        p = FACTS_DIR / f'{c["ticker"]}.json'
        if not p.exists():
            continue
        doc = json.loads(p.read_text(encoding='utf-8'))
        for f in doc.get('facts') or []:
            if (f.get('verification') or {}).get('status') == 'PASS' and f['id'] not in rejected:
                out[f['id']] = (doc, f)
    return out


def sentences(block: str) -> list[str]:
    """Split a paragraph after each marker group; trailing text without markers is its own item."""
    parts, pos = [], 0
    for m in MARKS.finditer(block):
        parts.append(block[pos:m.end()])
        pos = m.end()
    if block[pos:].strip():
        parts.append(block[pos:])
    return [p.strip() for p in parts if p.strip()]


def check(text: str, facts: dict) -> list[str]:
    problems = []
    # company short names may contain digits (e.g. 91APP-KY); they are not figures
    names = sorted({doc['company'] for doc, _ in facts.values()}, key=len, reverse=True)
    for line in text.splitlines():
        if not line.strip() or line.lstrip().startswith('#'):
            continue
        for s in sentences(line):
            ids = ONE.findall(s)
            if not ids:
                problems.append(f'句子沒有引用標記：{s[:60]}')
                continue
            missing = [i for i in ids if i not in facts]
            if missing:
                problems.append(f'引用的事實不存在、未通過或不屬本產業：{missing}：{s[:60]}')
                continue
            body = TICKER_PAREN.sub('', MARKS.sub('', s))
            for n in names:
                body = body.replace(n, '')
            cited = norm_num(' '.join(facts[i][1]['statement'] + ' ' + facts[i][1]['period'] for i in ids))
            cited = cited.replace('百分之十', '10%')
            for n in NUM.findall(body):
                if norm_num(n) not in cited:
                    problems.append(f'數字 {n} 不在引用的事實中：{s[:60]}')
    return problems


def render(text: str, facts: dict) -> str:
    notes: list[str] = []

    def repl(m):
        ids = list(dict.fromkeys(ONE.findall(m.group(1))))
        notes.append('；'.join(fact_note(*facts[i]) for i in ids))
        return f'[^a{len(notes)}]'

    body = MARKS.sub(repl, text.strip())
    head = '<!-- 由 research-site/scripts/generic/build_industry_analysis.py 依 data/industry-analysis 產生；請勿手動修改。 -->'
    return '\n'.join([head, '', body, ''] + [f'[^a{i}]: {t}' for i, t in enumerate(notes, 1)]) + '\n'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('slugs', nargs='*')
    ap.add_argument('--check-only', action='store_true')
    a = ap.parse_args()
    by_slug = {v['slug']: k for k, v in industry_names().items()}
    slugs = a.slugs or sorted(p.stem for p in DRAFTS.glob('*.md'))
    bad = 0
    OUTDIR.mkdir(parents=True, exist_ok=True)
    for slug in slugs:
        text = (DRAFTS / f'{slug}.md').read_text(encoding='utf-8')
        facts = load_industry_facts(by_slug[slug])
        probs = check(text, facts)
        if probs:
            bad += 1
            print(f'{slug}: {len(probs)} 個問題')
            for p in probs:
                print('  -', p)
            continue
        if not a.check_only:
            (OUTDIR / f'{slug}.qmd').write_text(render(text, facts), encoding='utf-8')
        print(f'{slug}: OK')
    print(f'drafts={len(slugs)} failing={bad}')
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()
