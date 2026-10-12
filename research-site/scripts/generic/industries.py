"""Shared helpers for the industry-generic site generators.

- industry list ordered by company count (desc, then folder name)
- stable ASCII slug per industry_folder (e.g. 'Electronic Components' -> 'electronic-components')
- Traditional Chinese display names from research-site/data/industry-names.csv
  (a trailing '?' in name_zh marks a translation awaiting human review; it is stripped for display)
- small shared readers / formatting helpers used by the page builders
"""
from __future__ import annotations

import csv
import json
import re
from collections import Counter
from decimal import ROUND_HALF_UP, Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SITE = ROOT / 'research-site'
CATALOG = SITE / 'catalog'
DATA = SITE / 'data'
NAMES_CSV = DATA / 'industry-names.csv'
VERIFIED = DATA / 'verified-sentences.jsonl'
FINANCIALS = DATA / 'financials/fy2025-financials-all.json'
FACTS_DIR = DATA / 'company-facts'
ASSESSMENT = '2026-10-08'
AERO_FOLDER = 'Aerospace & Defense'
AERO_TICKERS = ('2208', '2630', '2634', '2644', '2645', '4541', '4546', '4572', '6753', '8222')


def slugify(folder: str) -> str:
    """Stable ASCII slug: lowercase, '&' and every non-alphanumeric run become a single '-'."""
    s = re.sub(r'[^a-z0-9]+', '-', folder.lower().replace('&', ' '))
    return re.sub(r'-+', '-', s).strip('-')


def companies() -> list[dict]:
    with open(CATALOG / 'release-scope-companies.csv', encoding='utf-8-sig') as fh:
        return list(csv.DictReader(fh))


def claims() -> list[dict]:
    with open(CATALOG / 'release-scope-claims.csv', encoding='utf-8-sig') as fh:
        return list(csv.DictReader(fh))


def industry_names(path: Path = NAMES_CSV) -> dict[str, dict]:
    """{industry_folder: {'slug', 'name_zh' (display, '?' stripped), 'uncertain': bool}}."""
    out = {}
    with open(path, encoding='utf-8-sig') as fh:
        rows = list(csv.DictReader(fh))
    for r in rows:
        raw = r['name_zh'].strip()
        if r['slug'] != slugify(r['industry_folder']):
            raise SystemExit(f'industry-names.csv: slug {r["slug"]!r} != slugify({r["industry_folder"]!r})')
        out[r['industry_folder']] = {'slug': r['slug'], 'name_zh': raw.rstrip('?？'),
                                     'uncertain': raw.endswith(('?', '？'))}
    slugs = [v['slug'] for v in out.values()]
    if len(set(slugs)) != len(slugs):
        raise SystemExit('industry-names.csv: duplicate slugs')
    return out


def ordered_industries(rows: list[dict] | None = None) -> list[tuple[str, int]]:
    """[(industry_folder, company_count)] ordered by count desc, then folder name."""
    cnt = Counter(r['industry_folder'] for r in (rows if rows is not None else companies()))
    return sorted(cnt.items(), key=lambda x: (-x[1], x[0]))


def display_name(folder: str, names: dict | None = None) -> str:
    names = names if names is not None else industry_names()
    return names[folder]['name_zh'] if folder in names else folder


def jsonl(path) -> list[dict]:
    return [json.loads(l) for l in Path(path).read_text(encoding='utf-8').splitlines() if l.strip()]


def load_verified(path: Path = VERIFIED) -> dict[str, list[dict]]:
    out: dict[str, list[dict]] = {}
    if path.exists():
        for r in jsonl(path):
            out.setdefault(r['ticker'], []).append(r)
    return out


def load_financials(path: Path = FINANCIALS) -> dict[str, dict]:
    return {r['ticker']: r for r in json.loads(path.read_text(encoding='utf-8'))}


# ---------- formatting ----------

_MD_SPECIAL = re.compile(r'([\\`*_\[\]<>#$@|~^])')


def md_escape(text: str) -> str:
    """Escape Markdown/Pandoc specials so verified wording renders literally.
    Wikilink brackets [[X]] from original sentences are reduced to X first.
    Lenticular brackets 〔〕 are reserved for filters/refs.lua markers; they are swapped for （）."""
    t = re.sub(r'\[\[([^\]]+)\]\]', r'\1', text)
    t = t.replace('〔', '（').replace('〕', '）')
    t = _MD_SPECIAL.sub(r'\\\1', t)
    return re.sub(r'\s*\n\s*', ' ', t).strip()


def fmt_m(k) -> str:
    """仟元 -> 百萬元, half-up rounding."""
    return f'{(Decimal(k) / 1000).quantize(Decimal(1), rounding=ROUND_HALF_UP):,}'


def fmt_k(k) -> str:
    return f'{int(k):,}'


def fmt_pct(v) -> str:
    return '—' if v is None else f'{v:.2f}%'


def roc_year(y: int | str) -> int:
    return int(y) - 1911
